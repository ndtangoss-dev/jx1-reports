#!/usr/bin/env python3
"""P1 dispatcher. Default: read-only plan; real launches require an explicit allowlist."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}\Z")
TERMINAL = {"done", "needs_review", "blocked"}
MODEL = {"sol": "gpt-6.1-sol", "astra": "gpt-6-astra"}


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def number(value, default, minimum=0):
    result = float(default if value is None else value)
    if not math.isfinite(result) or result < minimum:
        raise ValueError("invalid nonnegative number")
    return result


def sequence(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    value = str(value).strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [x.strip().strip("\"'") for x in value.split(",") if x.strip()]


def front(path):
    """Small strict front-matter subset, no YAML execution/dependencies."""
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0] != "---":
        return None
    data = {}
    for line in lines[1:]:
        if line == "---":
            return data
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*):\s*(.*?)\s*", line)
        if not match or match[1] in data:
            raise ValueError("unsupported or duplicate front-matter field")
        data[match[1]] = match[2].strip("\"'")
    raise ValueError("missing front-matter terminator")


def scan(tasks_dir, worktree_root, fake=False, retry_ids=()):
    tasks, errors, seen = [], [], set()
    for path in sorted(tasks_dir.glob("*.md")):
        try:
            data = front(path)
            if not data or data.get("status") != "active":
                continue
            tid = data.get("id", "")
            if not ID.fullmatch(tid) or tid != path.stem or tid in seen:
                raise ValueError("id must be unique and match filename")
            seen.add(tid)
            if data.get("agent", "codex") != "codex":
                continue
            wt = Path(data.get("worktree", str(worktree_root / tid))).resolve()
            if not fake and wt != (worktree_root / tid).resolve():
                raise ValueError("worktree must equal worktree-root/id")
            if (path.with_suffix(".done").exists() or Path(str(wt) + ".done").exists()) and tid not in retry_ids:
                continue
            model = data.get("model", "sol")
            if model not in MODEL:
                raise ValueError("model must be sol or astra")
            effort = data.get("effort", "max")
            if effort not in {"low", "medium", "high", "xhigh", "max"}:
                raise ValueError("unsupported effort")
            priority = int(data.get("priority", 3))
            retry = int(data.get("retry", 2))
            if priority not in range(1, 6) or retry not in range(0, 3):
                raise ValueError("priority 1..5; retry 0..2 (maximum 3 attempts)")
            tasks.append(dict(id=tid, path=str(path.resolve()), worktree=str(wt),
                              model=model, effort=effort, priority=priority,
                              age=path.stat().st_mtime, retry=retry,
                              timeout_s=number(data.get("timeout_s"), 900, 0.01),
                              readonly=data.get("readonly", "false").lower() == "true",
                              depends_on=sequence(data.get("depends_on")),
                              resources=sequence(data.get("tai_nguyen")),
                              key_pool=data.get("key_pool", "any"),
                              reserve_usd=number(data.get("budget_usd"), 10, 0.01),
                              fake_result=data.get("fake_result", "success")))
        except (OSError, ValueError) as exc:
            # Never echo task contents or arbitrary exceptions containing input data.
            errors.append(dict(file=path.name, reason=type(exc).__name__))
    return sorted(tasks, key=lambda t: (t["priority"], t["age"], t["id"])), errors


def discover_keys(directory):
    # Directory metadata only. Do not open any key file.
    return sorted(p.stem for p in directory.glob("*.txt")
                  if p.is_file() and ID.fullmatch(p.stem))


def atomic(path, value):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(value, encoding="utf-8")
    tmp.replace(path)


class Dispatcher:
    def __init__(self, args):
        self.a = args
        self.state_dir = args.state_dir
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.lock = self.state_dir / "dispatcher.lock"
        # Exclusive creation: a crashed lock requires operator review, never steal it.
        self.lock_fd = os.open(self.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(self.lock_fd, str(os.getpid()).encode("ascii"))
        self.running = {}
        self.last_heartbeat = 0
        self.cooldown = {}
        self.streak = Counter()
        try:
            path = self.state_dir / "QUEUE.json"
            self.state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"tasks": {}}
            if self.state.get("mode", args.mode) != args.mode:
                raise ValueError("state mode mismatch; use a separate state directory")
            self.state["mode"] = args.mode
            self.cooldown = self.state.get("key_cooldown", {})
            self.streak = Counter(self.state.get("key_429_streak", {}))
            for row in self.state["tasks"].values():
                if row["status"] in {"running", "launching"}:
                    row.update(status="blocked", reason="restart: verify previous worker before manual reset")
            self.keys = (sequence(args.fake_keys) if args.fake_worker else discover_keys(args.keys_dir))
            if not self.keys or len(set(self.keys)) != len(self.keys) or not all(ID.fullmatch(k) for k in self.keys):
                raise ValueError("no valid unique key names")
        except BaseException:
            self.close()
            raise

    def close(self):
        os.close(self.lock_fd)
        self.lock.unlink()

    def event(self, tid, event):
        with (self.state_dir / "SU-KIEN.log").open("a", encoding="utf-8") as out:
            out.write(f"{utc()} {tid} {event}\n")

    def save(self):
        self.state["updated_at"] = utc()
        self.state["key_cooldown"] = self.cooldown
        self.state["key_429_streak"] = dict(self.streak)
        atomic(self.state_dir / "QUEUE.json", json.dumps(self.state, ensure_ascii=False, indent=2))
        lines = ["# QUEUE", "", f"Cập nhật: {utc()}; mode: {self.a.mode}",
                 f"Ngân sách: {self.state.get('budget_status', 'chưa đọc')}", "",
                 "| id | trạng thái | khóa | giao | xong | giây | token | 429 | thử lại | lý do |",
                 "|---|---|---|---|---|---|---:|---:|---:|---|"]
        for tid, r in sorted(self.state["tasks"].items()):
            fields = [tid, r["status"], r.get("key", ""), r.get("started_at", ""),
                      r.get("finished_at", ""), str(round(r.get("seconds", 0), 2)),
                      str(r.get("tokens", 0)), str(r.get("429", 0)),
                      str(max(0, r.get("attempts", 0) - 1)), r.get("reason", "")]
            lines.append("| " + " | ".join(fields) + " |")
        atomic(self.state_dir / "QUEUE.md", "\n".join(lines) + "\n")
        if time.monotonic() - self.last_heartbeat >= 60:
            atomic(self.state_dir / "QUEUE.heartbeat", utc() + "\n")
            self.last_heartbeat = time.monotonic()

    def budget_ok(self, task):
        if self.a.fake_worker:
            self.state["budget_status"] = "fake: 0 USD"
            return True
        try:
            b = json.loads(self.a.budget_file.read_text(encoding="utf-8-sig"))
            now = datetime.now(timezone.utc)
            updated = datetime.fromisoformat(b["updated_at"])
            if b["date"] != now.date().isoformat() or not 0 <= (now - updated).total_seconds() <= 300:
                raise ValueError("stale snapshot")
            daily = number(b["daily_usd"], 0)
            total = number(b["cumulative_usd"], 0)
            # Conservative: keep all reservations, including running workers, charged.
            # A fresh dashboard snapshot alone cannot acknowledge unspent worker cost.
            reserved = sum(r.get("reserved_usd", 0) for r in self.state["tasks"].values())
            permitted = daily + reserved + task["reserve_usd"] < 400 and total + reserved + task["reserve_usd"] < 1500
            self.state["budget_status"] = "OK" if permitted else "BLOCKED: budget cap/reservations"
            return permitted
        except (OSError, ValueError, KeyError, TypeError):
            self.state["budget_status"] = "BLOCKED: missing/invalid/stale budget snapshot"
            return False

    def launch(self, task, key, row):
        tid = task["id"]
        attempt = row.get("attempts", 0) + 1
        # Persist intent before creating a worker: crash recovery must not duplicate it.
        row.update(status="launching", key=key, attempts=attempt, started_at=utc(),
                   reserved_usd=row.get("reserved_usd", 0) + task["reserve_usd"], reserved_at=utc())
        self.save()
        if self.a.fake_worker:
            log = self.state_dir / f"{tid}.{attempt}.log"
            done = self.state_dir / f"{tid}.{attempt}.done"
            stream = log.open("w", encoding="utf-8")
            try:
                proc = subprocess.Popen([sys.executable, "-I", str(Path(__file__).resolve()),
                                         "--worker-child", str(done), task["fake_result"], str(attempt)],
                                        stdout=stream, stderr=subprocess.STDOUT)
            finally:
                stream.close()
        else:
            wt = Path(task["worktree"])
            prompt = Path(str(wt) + ".prompt.txt")
            if not wt.is_dir() or not prompt.is_file():
                row.update(status="blocked", reason="missing worktree or approved prompt")
                return
            log, done = Path(str(wt) + ".codex.log"), Path(str(wt) + ".done")
            env = os.environ.copy()
            env["JX_CODEX_KEY"] = key
            try:
                # Existing launcher owns key handling and Scheduled Task isolation.
                result = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-File",
                                         str(self.a.launcher), "-Id", tid, "-PromptFile", str(prompt),
                                         "-Model", MODEL[task["model"]], "-Effort", task["effort"]],
                                        env=env, capture_output=True, timeout=60)
            except (OSError, subprocess.TimeoutExpired):
                row.update(status="blocked", reason="launcher uncertain; inspect Scheduled Task")
                return
            if result.returncode:
                row.update(status="blocked", reason="launcher failed; inspect Scheduled Task")
                return
            proc = None
        row.update(status="running", key=key, attempts=attempt, started_at=utc(),
                   start_epoch=time.time(), reason="", log=str(log), done=str(done))
        self.running[tid] = dict(proc=proc, task=task, log=log, done=done, start=time.monotonic())
        self.event(tid, "running")
        self.save()

    def stop(self, tid, run):
        if self.a.fake_worker:
            proc = run["proc"]
            if proc.poll() is None:
                proc.kill()
            proc.wait(timeout=10)
        else:
            # Stop-ScheduledTask terminates the worker job; do not launch a retry
            # until the operator has verified that its descendants are gone.
            result = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command",
                                     f"$ErrorActionPreference='Stop'; Stop-ScheduledTask -TaskName 'JX-codex-{tid}'"],
                                    capture_output=True, timeout=30)
            if result.returncode:
                raise RuntimeError("cannot confirm stop")

    def poll(self):
        for tid, run in list(self.running.items()):
            row, task = self.state["tasks"][tid], run["task"]
            elapsed = time.monotonic() - run["start"]
            timedout = elapsed >= task["timeout_s"]
            done = run["done"].exists()
            exited = self.a.fake_worker and run["proc"].poll() is not None
            if not (timedout or done or exited):
                continue
            if timedout or (self.a.fake_worker and done):
                try:
                    self.stop(tid, run)
                except (OSError, RuntimeError, subprocess.TimeoutExpired):
                    row.update(status="blocked", reason="stop unconfirmed; operator must verify")
                    # Keep the slot/resources reserved; never duplicate a live worker.
                    continue
            text = run["log"].read_text(encoding="utf-8", errors="replace") if run["log"].exists() else ""
            errors = transient_errors(text)
            row["429"] = row.get("429", 0) + sum(x == "429" for x in errors)
            row["tokens"] = row.get("tokens", 0) + tokens(text)
            marker = run["done"].read_text(encoding="utf-8-sig").strip() if done else ""
            success = bool(re.match(r"exit=0(?:\s|$)", marker)) and not errors and not timedout
            row.update(seconds=elapsed, finished_at=utc())
            if success:
                row.update(status="done" if task["readonly"] else "needs_review", reason="")
                self.streak[row["key"]] = 0
            else:
                reason = "timeout" if timedout else "429" if "429" in errors else "503" if "503" in errors else "stream disconnected" if errors else "worker exit/missing done"
                retryable = self.a.fake_worker or (bool(errors) and done)
                if reason == "429":
                    self.streak[row["key"]] += 1
                    if self.streak[row["key"]] >= 3:
                        self.cooldown[row["key"]] = time.time() + 600
                else:
                    self.streak[row["key"]] = 0
                if retryable and row["attempts"] <= task["retry"]:
                    delay = (30, 120, 600)[min(row["attempts"] - 1, 2)] * self.a.backoff_scale
                    row.update(status="ready", reason=reason, next_at=time.time() + delay)
                    if reason == "503" and task["readonly"] and task["model"] == "astra":
                        row["fallback_model"] = "sol"
                else:
                    row.update(status="blocked", reason=reason)
            del self.running[tid]
            self.event(tid, row["status"] + (":" + row["reason"] if row["reason"] else ""))

    def tick(self):
        self.poll()
        retry_ids = {tid for tid, r in self.state["tasks"].items()
                     if r["status"] == "ready" and r.get("attempts", 0)}
        tasks, errors = scan(self.a.tasks_dir, self.a.worktree_root, self.a.fake_worker, retry_ids)
        self.state["scan_errors"] = errors
        if not self.a.fake_worker and any(r.get("reason", "").startswith(("restart:", "launcher", "stop unconfirmed", "dispatcher stopped", "timeout"))
                                          for r in self.state["tasks"].values() if r["status"] == "blocked"):
            self.state["budget_status"] = "BLOCKED: verify previous worker before new launches"
            self.save()
            return
        for task in tasks:
            tid = task["id"]
            if self.a.allow_task and tid not in self.a.allow_task:
                continue
            row = self.state["tasks"].setdefault(tid, {"status": "ready", "attempts": 0})
            if row["status"] in TERMINAL or tid in self.running or row.get("next_at", 0) > time.time():
                continue
            if any(self.state["tasks"].get(dep, {}).get("status") != "done" and
                   not (self.a.tasks_dir / (dep + ".done")).is_file()
                   for dep in task["depends_on"]):
                row["reason"] = "waiting for dependencies"
                continue
            if any(task["worktree"] == r["task"]["worktree"] or
                   set(task["resources"]) & set(r["task"]["resources"]) for r in self.running.values()):
                row["reason"] = "worktree/resource busy"
                continue
            loads = Counter(self.state["tasks"][t]["key"] for t in self.running)
            available = [k for k in self.keys if loads[k] < 3 and self.cooldown.get(k, 0) <= time.time()
                         and task["key_pool"] in ("any", k)]
            if len(self.running) >= min(16, 3 * len(self.keys)) or not available:
                row["reason"] = "waiting for key slot"
                continue
            # Prefer another key after a transient failure, then lowest load.
            key = min(available, key=lambda k: (k == row.get("key"), loads[k], k))
            if not self.budget_ok(task):
                row["reason"] = "budget gate"
                continue
            if row.get("fallback_model"):
                task["model"] = row["fallback_model"]
            self.launch(task, key, row)
        self.save()


def tokens(text):
    total = 0
    for line in text.splitlines():
        try:
            obj = json.loads(line)
            if obj.get("type") == "turn.completed":
                usage = obj.get("usage", {})
                total += int(usage.get("input_tokens", 0)) + int(usage.get("output_tokens", 0))
        except (ValueError, TypeError, AttributeError):
            continue
    return total


def transient_errors(text):
    errors = []
    for line in text.splitlines():
        try:
            obj = json.loads(line)
        except ValueError:
            obj = None
        # Usage counts and successful model output are not transport failures.
        if isinstance(obj, dict):
            if obj.get("type") not in {"error", "turn.failed"}:
                continue
            line = json.dumps(obj.get("error", obj.get("message", "")))
        errors.extend(re.findall(r"\b(?:429|503)\b|stream disconnected", line, re.I))
    return [e.lower() for e in errors]


def child(done, outcome, attempt):
    if outcome == "timeout":
        time.sleep(30)
    time.sleep(0.12)
    failure = outcome in {"429", "503", "stream"} and attempt == 1 or outcome == "fail"
    if failure:
        print("stream disconnected" if outcome == "stream" else outcome, flush=True)
    print(json.dumps({"type": "turn.completed", "usage": {"input_tokens": 12, "output_tokens": 8}}), flush=True)
    atomic(Path(done), "exit=" + ("1" if failure else "0") + "\n")
    return 1 if failure else 0


def main(argv=None):
    if len(sys.argv) > 1 and sys.argv[1] == "--worker-child":
        return child(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    p = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parents[2]
    p.add_argument("--tasks-dir", type=Path, default=root / "TASKS")
    p.add_argument("--state-dir", type=Path, default=root / "STATE")
    p.add_argument("--keys-dir", type=Path, default=Path(r"C:\Users\PC\.jx1keys"))
    p.add_argument("--worktree-root", type=Path, default=Path(r"D:\JX-wt"))
    p.add_argument("--launcher", type=Path, default=root / "TOOLS" / "chay_codex.ps1")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--fake-worker", action="store_true")
    mode.add_argument("--run-real", action="store_true")
    p.add_argument("--allow-task", action="append", default=[])
    p.add_argument("--fake-keys", default="fake-a,fake-b")
    p.add_argument("--budget-file", type=Path)
    p.add_argument("--interval", type=float, default=20)
    p.add_argument("--backoff-scale", type=float, default=1)
    p.add_argument("--max-seconds", type=float, default=0)
    p.add_argument("--until-idle", action="store_true")
    a = p.parse_args(argv)
    if a.interval <= 0 or a.backoff_scale < 0 or a.max_seconds < 0:
        p.error("invalid timing")
    if a.run_real and (not a.allow_task or not a.budget_file or a.backoff_scale != 1):
        p.error("real mode requires --allow-task and --budget-file; backoff-scale must be 1")
    if not all(ID.fullmatch(t) for t in a.allow_task):
        p.error("invalid task id")
    if a.fake_worker and not (a.tasks_dir.resolve() / ".fake-tasks-only").is_file():
        p.error("fake mode requires .fake-tasks-only marker in an isolated task directory")
    if not a.fake_worker and not a.run_real:
        tasks, errors = scan(a.tasks_dir, a.worktree_root)
        print(json.dumps({"mode": "dry-run", "tasks": [t["id"] for t in tasks
              if not a.allow_task or t["id"] in a.allow_task], "keys": discover_keys(a.keys_dir),
                          "scan_errors": errors}, ensure_ascii=True, indent=2))
        return 1 if errors else 0
    a.mode = "fake" if a.fake_worker else "real"
    d = Dispatcher(a)
    start = time.monotonic()
    try:
        while True:
            d.tick()
            if a.until_idle and not d.running and not any(r["status"] == "ready" and r.get("next_at", 0)
                                                         for r in d.state["tasks"].values()):
                break
            if a.max_seconds and time.monotonic() - start >= a.max_seconds:
                break
            time.sleep(a.interval)
    finally:
        for tid, run in list(d.running.items()):
            try:
                d.stop(tid, run)
                d.state["tasks"][tid].update(status="blocked", reason="dispatcher stopped; verify worker")
            except (OSError, RuntimeError, subprocess.TimeoutExpired):
                d.state["tasks"][tid].update(status="blocked", reason="stop unconfirmed; operator must verify")
        d.save()
        d.close()
    print(json.dumps({"states": dict(Counter(r["status"] for r in d.state["tasks"].values())),
                      "scan_errors": d.state["scan_errors"]}, ensure_ascii=True))
    return 1 if d.state["scan_errors"] or any(r["status"] not in {"done", "needs_review"}
                                             for r in d.state["tasks"].values()) else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as exc:
        print("dispatcher: " + type(exc).__name__ + "; inspect state/lock and input schema", file=sys.stderr)
        sys.exit(2)
