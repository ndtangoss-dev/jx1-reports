import json
import os
import threading
import unittest
from http.client import HTTPConnection
from unittest.mock import patch

from app import (
    ACTION_TOKEN_ENV,
    ActionGuard,
    DashboardApp,
    JxadmDryRunProvider,
    StaticStatusProvider,
    create_server,
    validate_bind_host,
)


SNAPSHOT = {
    "generated_at": "2026-11-17T00:00:00+00:00",
    "server": {
        "status": "unverified",
        "mode": "fixture",
        "bind_host": "127.0.0.1",
        "source": "offline fixture",
    },
    "accounts": [{"name": "offline_fixture", "status": "unverified", "session": "not queried", "source": "fixture"}],
    "notes": ["fixture only"],
}


class JxWebTests(unittest.TestCase):
    def test_bind_host_is_loopback_only_and_main_vm_is_blocked(self):
        self.assertEqual(validate_bind_host("127.0.0.1"), "127.0.0.1")
        self.assertEqual(validate_bind_host("::1"), "::1")
        for host in ("0.0.0.0", "192.168.1.50", "::ffff:192.168.1.50", "localhost"):
            with self.subTest(host=host), self.assertRaises(ValueError):
                validate_bind_host(host)

    def test_jxadm_provider_stays_dry_run(self):
        snapshot = JxadmDryRunProvider().snapshot()
        self.assertEqual(snapshot["server"]["mode"], "dry-run")
        self.assertEqual(snapshot["server"]["bind_host"], "127.0.0.1")
        self.assertEqual(snapshot["jxadm_preview"]["mode"], "dry-run")
        self.assertIn("SELECT", snapshot["jxadm_preview"]["statements"][0]["sql"])

    def test_action_guard_requires_token_and_two_steps(self):
        guard = ActionGuard(ttl_seconds=60)
        with patch.dict(os.environ, {ACTION_TOKEN_ENV: "test-token"}, clear=False):
            with self.assertRaises(PermissionError):
                guard.prepare("refresh", "wrong")
            result = guard.prepare("refresh", "test-token")
            self.assertEqual(result["step"], "confirm")
            guard.confirm("refresh", "test-token", result["challenge"])
            with self.assertRaises(PermissionError):
                guard.confirm("refresh", "test-token", result["challenge"])

    def test_http_status_html_and_action_endpoint(self):
        guard = ActionGuard(ttl_seconds=60)
        server = create_server(provider=StaticStatusProvider(SNAPSHOT), port=0, action_guard=guard)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            connection = HTTPConnection("127.0.0.1", server.server_port, timeout=3)
            connection.request("GET", "/api/status")
            response = connection.getresponse()
            self.assertEqual(response.status, 200)
            payload = json.loads(response.read())
            self.assertEqual(payload["accounts"][0]["name"], "offline_fixture")
            connection.request("GET", "/")
            response = connection.getresponse()
            page = response.read().decode("utf-8")
            self.assertEqual(response.status, 200)
            self.assertIn('name="viewport"', page)
            self.assertIn("offline_fixture", page)
            with patch.dict(os.environ, {ACTION_TOKEN_ENV: "test-token"}, clear=False):
                body = json.dumps({"action": "refresh", "step": "prepare"})
                connection.request("POST", "/api/actions", body=body, headers={"Content-Type": "application/json", "X-JXWEB-ACTION-TOKEN": "test-token"})
                response = connection.getresponse()
                challenge = json.loads(response.read())["challenge"]
                self.assertEqual(response.status, 202)
                body = json.dumps({"action": "refresh", "step": "confirm", "challenge": challenge})
                connection.request("POST", "/api/actions", body=body, headers={"Content-Type": "application/json", "X-JXWEB-ACTION-TOKEN": "test-token"})
                response = connection.getresponse()
                self.assertEqual(response.status, 501)
                self.assertIn("write adapter", response.read().decode("utf-8"))
            connection.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)

    def test_http_rejects_nonexistent_path(self):
        server = create_server(provider=StaticStatusProvider(SNAPSHOT), port=0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            connection = HTTPConnection("127.0.0.1", server.server_port, timeout=3)
            connection.request("GET", "/missing")
            response = connection.getresponse()
            self.assertEqual(response.status, 404)
            self.assertEqual(json.loads(response.read())["error"], "not found")
            connection.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)

    def test_ipv6_loopback_server_can_bind(self):
        server = create_server(provider=StaticStatusProvider(SNAPSHOT), host="::1", port=0)
        try:
            self.assertEqual(server.server_address[0], "::1")
        finally:
            server.server_close()


if __name__ == "__main__":
    unittest.main()
