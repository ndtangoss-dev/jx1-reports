"""Read-mostly JX1 internal dashboard using only Python's standard library.

The default provider asks :mod:`jxadm` for an ``online`` dry-run plan.  It does
not open a socket or connect to SQL.  A status provider can be replaced with a
fixture in tests or by a future, separately approved adapter.
"""

from __future__ import annotations

import argparse
import copy
import hmac
import html
import importlib.util
import ipaddress
import json
import os
import re
import secrets
import socket
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol
from urllib.parse import urlsplit


DEFAULT_BIND_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
MAIN_VM_HOST = "192.168.1.50"
ACTION_TOKEN_ENV = "JXWEB_ACTION_TOKEN"
MAX_REQUEST_BYTES = 16 * 1024
_ACTION_NAME = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")


def validate_bind_host(host: str) -> str:
    """Validate a numeric loopback address and reject the Main VM address."""

    if not isinstance(host, str) or "%" in host:
        raise ValueError("bind host must be a loopback IP literal")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        raise ValueError("bind host must be a loopback IP literal") from None
    if address == ipaddress.ip_address(MAIN_VM_HOST) or getattr(address, "ipv4_mapped", None) == ipaddress.ip_address(MAIN_VM_HOST):
        raise ValueError("Main VM address is blocked")
    if not address.is_loopback:
        raise ValueError("bind host must be a loopback IP literal")
    return str(address)


def _load_jxadm() -> Any:
    """Load the sibling offline module without importing third-party code."""

    path = Path(__file__).resolve().parents[1] / "jxadm" / "jxadm.py"
    spec = importlib.util.spec_from_file_location("jxadm_for_jxweb", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("jxadm source is unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StatusProvider(Protocol):
    def snapshot(self) -> Mapping[str, Any]:
        """Return JSON-serializable server and account observations."""


class JxadmDryRunProvider:
    """Build a status snapshot from jxadm's offline ``online`` plan."""

    def __init__(self, account: str = "offline_fixture", *, host: str = DEFAULT_BIND_HOST) -> None:
        self.host = validate_bind_host(host)
        self._jxadm = _load_jxadm()
        self.account = self._jxadm.validate_account(account)

    def snapshot(self) -> Mapping[str, Any]:
        plan = self._jxadm.account_plan("online", self.account, host=self.host)
        preview = plan.preview()
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "server": {
                "status": "unverified",
                "mode": "dry-run",
                "bind_host": self.host,
                "source": "jxadm.account_plan(online)",
            },
            "accounts": [
                {
                    "name": self.account,
                    "status": "unverified",
                    "session": "not queried",
                    "source": "jxadm dry-run",
                }
            ],
            "jxadm_preview": preview,
            "notes": [
                "Dry-run only; no SQL connection or live server observation was made.",
                "Online interpretation of client and login dates remains unverified.",
            ],
        }


class StaticStatusProvider:
    """Small deterministic provider for offline tests and local demonstrations."""

    def __init__(self, snapshot: Mapping[str, Any]) -> None:
        self._snapshot = copy.deepcopy(dict(snapshot))

    def snapshot(self) -> Mapping[str, Any]:
        return copy.deepcopy(self._snapshot)


@dataclass(frozen=True)
class _Challenge:
    action: str
    expires_at: float


class ActionGuard:
    """Require an environment token and a one-time two-step confirmation."""

    def __init__(
        self,
        *,
        env_name: str = ACTION_TOKEN_ENV,
        ttl_seconds: int = 300,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        if ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")
        self.env_name = env_name
        self.ttl_seconds = ttl_seconds
        self._clock = clock
        self._challenges: dict[str, _Challenge] = {}
        self._lock = threading.Lock()

    @staticmethod
    def _validate_action(action: str) -> str:
        if not isinstance(action, str) or not _ACTION_NAME.fullmatch(action):
            raise ValueError("action must be a simple lowercase name")
        return action

    def _token_ok(self, token: str | None) -> bool:
        expected = os.environ.get(self.env_name)
        return bool(expected and token and hmac.compare_digest(token, expected))

    def prepare(self, action: str, token: str | None) -> dict[str, Any]:
        action = self._validate_action(action)
        if not self._token_ok(token):
            raise PermissionError("action token is missing or invalid")
        challenge = secrets.token_urlsafe(24)
        with self._lock:
            self._challenges[challenge] = _Challenge(action, self._clock() + self.ttl_seconds)
        return {"challenge": challenge, "expires_in": self.ttl_seconds, "step": "confirm"}

    def confirm(self, action: str, token: str | None, challenge: str | None) -> None:
        action = self._validate_action(action)
        if not self._token_ok(token):
            raise PermissionError("action token is missing or invalid")
        if not isinstance(challenge, str) or not challenge:
            raise PermissionError("confirmation challenge is required")
        with self._lock:
            saved = self._challenges.pop(challenge, None)
        if saved is None or saved.action != action or saved.expires_at < self._clock():
            raise PermissionError("confirmation challenge is invalid or expired")


ActionWriter = Callable[[str, Mapping[str, Any]], Mapping[str, Any] | None]


@dataclass
class DashboardApp:
    provider: StatusProvider
    bind_host: str = DEFAULT_BIND_HOST
    action_guard: ActionGuard | None = None
    writer: ActionWriter | None = None

    def __post_init__(self) -> None:
        self.bind_host = validate_bind_host(self.bind_host)
        if self.action_guard is None:
            self.action_guard = ActionGuard()

    def snapshot(self) -> Mapping[str, Any]:
        return self.provider.snapshot()


def _text(value: Any, fallback: str = "—") -> str:
    if value is None or value == "":
        value = fallback
    return html.escape(str(value), quote=True)


def render_dashboard(snapshot: Mapping[str, Any]) -> str:
    server = snapshot.get("server", {})
    accounts = snapshot.get("accounts", [])
    if not isinstance(server, Mapping):
        server = {}
    if not isinstance(accounts, list):
        accounts = []
    cards = []
    for account in accounts:
        if not isinstance(account, Mapping):
            continue
        cards.append(
            "<article class='card'><h3>{}</h3><dl>"
            "<dt>Trạng thái</dt><dd>{}</dd>"
            "<dt>Phiên</dt><dd>{}</dd>"
            "<dt>Nguồn</dt><dd>{}</dd></dl></article>".format(
                _text(account.get("name")),
                _text(account.get("status")),
                _text(account.get("session")),
                _text(account.get("source")),
            )
        )
    if not cards:
        cards.append("<article class='card'><p>Chưa có tài khoản trong snapshot.</p></article>")
    notes = snapshot.get("notes", [])
    if not isinstance(notes, list):
        notes = []
    note_html = "".join(f"<li>{_text(note)}</li>" for note in notes)
    return """<!doctype html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>JX1 • Trạng thái nội bộ</title>
<style>
:root{{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:#172033;background:#f4f7fb}}
body{{margin:0;min-width:280px;font-size:18px;line-height:1.45}}
main{{max-width:980px;margin:auto;padding:clamp(1rem,4vw,2.5rem)}}
h1{{font-size:clamp(1.65rem,6vw,2.5rem);margin:.2rem 0 .3rem}}
h2{{font-size:clamp(1.25rem,4vw,1.7rem);margin:1.5rem 0 .7rem}}
.muted{{color:#526174}}.grid{{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}
.card{{background:#fff;border:1px solid #d9e1ec;border-radius:14px;padding:1rem;box-shadow:0 2px 10px #17203312}}
dl{{margin:0}}.card dt{{color:#526174;font-size:.9rem;margin-top:.55rem}}.card dd{{margin:0;font-weight:600;overflow-wrap:anywhere}}
ul{{padding-left:1.4rem}}.badge{{display:inline-block;border-radius:999px;padding:.2rem .65rem;background:#e5eefc}}
@media (prefers-color-scheme:dark){{:root{{color:#e8edf5;background:#111827}}.card{{background:#1f2937;border-color:#374151}}.muted,.card dt{{color:#b6c3d6}}.badge{{background:#243b63}}}}
</style></head><body><main>
<header><h1>JX1 • Trạng thái nội bộ</h1>
<p class="muted">Chế độ quan sát, không tự kết nối máy chủ.</p></header>
<section aria-labelledby="server-heading"><h2 id="server-heading">Máy chủ</h2>
<article class="card"><dl>
<dt>Trạng thái</dt><dd><span class="badge">{server_status}</span></dd>
<dt>Chế độ</dt><dd>{server_mode}</dd>
<dt>Bind</dt><dd>{bind_host}</dd>
<dt>Nguồn</dt><dd>{server_source}</dd>
<dt>Cập nhật</dt><dd>{generated_at}</dd>
</dl></article></section>
<section aria-labelledby="accounts-heading"><h2 id="accounts-heading">Tài khoản</h2>
<div class="grid">{cards}</div></section>
<section aria-labelledby="notes-heading"><h2 id="notes-heading">Ghi chú</h2><ul>{notes}</ul></section>
</main></body></html>""".format(
        server_status=_text(server.get("status")),
        server_mode=_text(server.get("mode")),
        bind_host=_text(server.get("bind_host")),
        server_source=_text(server.get("source")),
        generated_at=_text(snapshot.get("generated_at")),
        cards="".join(cards),
        notes=note_html or "<li>Không có ghi chú.</li>",
    )


def _json_bytes(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def make_handler(app: DashboardApp) -> type[BaseHTTPRequestHandler]:
    """Create a request handler closed over one dashboard application."""

    class DashboardHandler(BaseHTTPRequestHandler):
        server_version = "JXWeb/0.1"
        sys_version = ""

        def _send(self, status: int, body: bytes, content_type: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, status: int, payload: Mapping[str, Any]) -> None:
            self._send(status, _json_bytes(payload), "application/json; charset=utf-8")

        def _error(self, status: int, message: str) -> None:
            self._json(status, {"error": message})

        def _snapshot(self) -> Mapping[str, Any] | None:
            try:
                return app.snapshot()
            except Exception:
                self._error(HTTPStatus.SERVICE_UNAVAILABLE, "status provider unavailable")
                return None

        def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
            path = urlsplit(self.path).path
            if path == "/healthz":
                self._json(HTTPStatus.OK, {"ok": True, "bind_host": app.bind_host})
                return
            if path == "/api/status":
                snapshot = self._snapshot()
                if snapshot is not None:
                    self._json(HTTPStatus.OK, snapshot)
                return
            if path == "/":
                snapshot = self._snapshot()
                if snapshot is not None:
                    self._send(HTTPStatus.OK, render_dashboard(snapshot).encode("utf-8"), "text/html; charset=utf-8")
                return
            self._error(HTTPStatus.NOT_FOUND, "not found")

        def do_POST(self) -> None:  # noqa: N802 - stdlib handler API
            if urlsplit(self.path).path != "/api/actions":
                self._error(HTTPStatus.NOT_FOUND, "not found")
                return
            length_text = self.headers.get("Content-Length")
            try:
                length = int(length_text or "-1")
            except ValueError:
                length = -1
            if length < 0 or length > MAX_REQUEST_BYTES:
                self._error(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, "request body is too large or missing")
                return
            try:
                body = json.loads(self.rfile.read(length).decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                self._error(HTTPStatus.BAD_REQUEST, "request body must be UTF-8 JSON")
                return
            if not isinstance(body, Mapping):
                self._error(HTTPStatus.BAD_REQUEST, "request body must be an object")
                return
            action = body.get("action")
            step = body.get("step")
            token = self.headers.get("X-JXWEB-ACTION-TOKEN")
            try:
                if step == "prepare":
                    result = app.action_guard.prepare(action, token)  # type: ignore[union-attr]
                    self._json(HTTPStatus.ACCEPTED, result)
                    return
                if step != "confirm":
                    raise ValueError("step must be prepare or confirm")
                app.action_guard.confirm(action, token, body.get("challenge"))  # type: ignore[union-attr]
                if app.writer is None:
                    self._error(HTTPStatus.NOT_IMPLEMENTED, "write adapter is not configured")
                    return
                result = app.writer(action, body.get("payload", {}))
                self._json(HTTPStatus.OK, {"ok": True, "result": result})
            except ValueError as error:
                self._error(HTTPStatus.BAD_REQUEST, str(error))
            except PermissionError as error:
                self._error(HTTPStatus.FORBIDDEN, str(error))
            except Exception:
                self._error(HTTPStatus.INTERNAL_SERVER_ERROR, "write action failed")

        def log_message(self, _format: str, *args: Any) -> None:
            # Do not log request headers, query strings, or bodies that may contain secrets.
            return

    return DashboardHandler


def create_server(
    *,
    provider: StatusProvider | None = None,
    host: str = DEFAULT_BIND_HOST,
    port: int = DEFAULT_PORT,
    action_guard: ActionGuard | None = None,
    writer: ActionWriter | None = None,
) -> ThreadingHTTPServer:
    host = validate_bind_host(host)
    if not isinstance(port, int) or not 0 <= port <= 65535:
        raise ValueError("port must be between 0 and 65535")
    app = DashboardApp(provider or JxadmDryRunProvider(host=host), host, action_guard, writer)
    server_class = ThreadingHTTPServer
    if ":" in host:
        class IPv6ThreadingHTTPServer(ThreadingHTTPServer):
            address_family = socket.AF_INET6

        server_class = IPv6ThreadingHTTPServer
    server = server_class((host, port), make_handler(app))
    server.daemon_threads = True
    server.app = app  # type: ignore[attr-defined]
    return server


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="JX1 offline-first internal dashboard")
    parser.add_argument("--host", default=DEFAULT_BIND_HOST, help="loopback IP literal")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--account", default="offline_fixture")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        server = create_server(provider=JxadmDryRunProvider(args.account, host=args.host), host=args.host, port=args.port)
    except (RuntimeError, ValueError) as error:
        _parser().error(str(error))
    print(f"JXWeb listening on http://{args.host}:{server.server_port}/ (dry-run)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
