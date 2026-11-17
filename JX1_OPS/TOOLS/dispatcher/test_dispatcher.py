"""Offline regression tests; never run Codex, Scheduled Tasks, network, or key reads."""
import importlib.util
import json
import os
import subprocess
from pathlib import Path
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("dispatcher", HERE / "dispatcher.py")
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="test-", dir=HERE)
        self.root = Path(self.temp.name)
        self.tasks = self.root / "TASKS"
        self.tasks.mkdir()
        (self.tasks / ".fake-tasks-only").touch()
        self.args = SimpleNamespace(state_dir=self.root / "STATE", tasks_dir=self.tasks,
                                    worktree_root=self.root / "worktrees", fake_worker=True,
                                    fake_keys="fake-a,fake-b", keys_dir=self.root / "keys",
                                    allow_task=[], mode="fake", backoff_scale=0,
                                    budget_file=self.root / "budget.json")
        self.dispatcher = None

    def tearDown(self):
        if self.dispatcher:
            for tid, run in list(self.dispatcher.running.items()):
                self.dispatcher.stop(tid, run)
            self.dispatcher.close()
        self.temp.cleanup()

    def task(self, tid, extra=""):
        readonly = "" if "readonly:" in extra else "readonly: true\n"
        (self.tasks / (tid + ".md")).write_text(
            f"---\nid: {tid}\nstatus: active\n{readonly}worktree: {self.root / tid}\n{extra}---\nFake task only.\n",
            encoding="utf-8")

    def make(self):
        self.dispatcher = D.Dispatcher(self.args)
        return self.dispatcher

    def complete(self, d):
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            d.tick()
            if not d.running and all(r["status"] in D.TERMINAL for r in d.state["tasks"].values()):
                return
            time.sleep(0.03)
        self.fail("fake workers did not finish in 10 seconds")


class DispatcherTests(Fixture):
    def test_five_fake_tasks_and_key_capacity(self):
        for n in range(5):
            self.task(f"FAKE-{n}")
        d = self.make()
        d.tick()
        self.assertEqual(len(d.running), 5)
        self.assertLessEqual(max(D.Counter(r["key"] for r in d.state["tasks"].values()).values()), 3)
        self.complete(d)
        self.assertEqual([r["status"] for r in d.state["tasks"].values()], ["done"] * 5)
        self.assertEqual(sum(r["tokens"] for r in d.state["tasks"].values()), 100)
        for name in ("QUEUE.json", "QUEUE.md", "QUEUE.heartbeat", "SU-KIEN.log"):
            self.assertTrue((self.args.state_dir / name).is_file())
        self.assertNotIn("blocked", (self.args.state_dir / "QUEUE.md").read_text(encoding="utf-8"))

    def test_dependency_resource_and_priority(self):
        self.task("ONE", "priority: 1\ntai_nguyen: [exclusive]\n")
        self.task("TWO", "priority: 2\ntai_nguyen: [exclusive]\n")
        self.task("THREE", "depends_on: [ONE]\n")
        d = self.make()
        d.tick()
        self.assertEqual(list(d.running), ["ONE"])
        self.assertEqual(d.state["tasks"]["TWO"]["reason"], "worktree/resource busy")
        self.assertEqual(d.state["tasks"]["THREE"]["reason"], "waiting for dependencies")
        self.complete(d)
        self.assertTrue(all(r["status"] == "done" for r in d.state["tasks"].values()))

    def test_transient_retry_rotates_key_and_fallback(self):
        self.task("RETRY", "fake_result: 503\nmodel: astra\n")
        d = self.make()
        d.tick()
        first_key = d.state["tasks"]["RETRY"]["key"]
        self.complete(d)
        row = d.state["tasks"]["RETRY"]
        self.assertEqual((row["status"], row["attempts"], row["fallback_model"]), ("done", 2, "sol"))
        self.assertNotEqual(row["key"], first_key)

    def test_timeout_and_retry_exhaustion(self):
        self.task("TIMEOUT", "fake_result: timeout\ntimeout_s: 0.05\nretry: 1\n")
        d = self.make()
        self.complete(d)
        row = d.state["tasks"]["TIMEOUT"]
        self.assertEqual((row["status"], row["reason"], row["attempts"]), ("blocked", "timeout", 2))
        self.assertFalse(d.running)

    def test_only_active_undone_codex_and_strict_input(self):
        self.task("DONE")
        (self.tasks / "DONE.done").touch()
        self.task("OTHER", "agent: other\n")
        self.task("BAD", "retry: 99\n")
        self.task("GOOD")
        tasks, errors = D.scan(self.tasks, self.args.worktree_root, True)
        self.assertEqual([t["id"] for t in tasks], ["GOOD"])
        self.assertEqual(errors, [{"file": "BAD.md", "reason": "ValueError"}])
        tasks, _ = D.scan(self.tasks, self.args.worktree_root, True, {"DONE"})
        self.assertEqual([t["id"] for t in tasks], ["DONE", "GOOD"])

    def test_keys_discovered_without_opening_files(self):
        self.args.keys_dir.mkdir()
        (self.args.keys_dir / "example.txt").touch()
        (self.args.keys_dir / "unsafe name.txt").touch()
        with patch.object(Path, "open", side_effect=AssertionError("key content read")):
            self.assertEqual(D.discover_keys(self.args.keys_dir), ["example"])

    def test_budget_missing_stale_limits_and_reservations(self):
        d = self.make()
        d.a.fake_worker = False
        t = {"reserve_usd": 10}
        self.assertFalse(d.budget_ok(t))
        now = D.utc()
        b = dict(date=now[:10], updated_at=now, daily_usd=389, cumulative_usd=100)
        self.args.budget_file.write_text(json.dumps(b), encoding="utf-8")
        self.assertTrue(d.budget_ok(t))
        d.state["tasks"]["RESERVED"] = dict(status="done", reserved_at=now, reserved_usd=1)
        self.assertFalse(d.budget_ok(t))
        d.state["tasks"].clear()
        b.update(daily_usd=0, cumulative_usd=1490)
        self.args.budget_file.write_text(json.dumps(b), encoding="utf-8")
        self.assertFalse(d.budget_ok(t))
        b.update(updated_at="2000-01-01T00:00:00+00:00", cumulative_usd=0)
        self.args.budget_file.write_text(json.dumps(b), encoding="utf-8")
        self.assertFalse(d.budget_ok(t))

    def test_exclusive_lock_and_restart_blocks_old_worker(self):
        d = self.make()
        with self.assertRaises(FileExistsError):
            D.Dispatcher(self.args)
        d.state["tasks"]["OLD"] = {"status": "launching"}
        d.save()
        d.close()
        self.dispatcher = None
        d = self.make()
        self.assertEqual(d.state["tasks"]["OLD"]["status"], "blocked")
        self.assertTrue(d.state["tasks"]["OLD"]["reason"].startswith("restart:"))

    def test_cli_five_fake_workers_and_readonly_dry_run(self):
        for n in range(5):
            self.task(f"CLI-{n}")
        command = [sys.executable, "-I", str(HERE / "dispatcher.py"),
                   "--tasks-dir", str(self.tasks), "--state-dir", str(self.args.state_dir),
                   "--worktree-root", str(self.root), "--keys-dir", str(self.root / "no-keys")]
        dry = subprocess.run(command + ["--dry-run"], capture_output=True, text=True, timeout=10)
        self.assertEqual(dry.returncode, 0, dry.stderr)
        self.assertEqual(len(json.loads(dry.stdout)["tasks"]), 5)
        self.assertFalse(self.args.state_dir.exists())
        fake = subprocess.run(command + ["--fake-worker", "--until-idle", "--interval", "0.03",
                                         "--max-seconds", "10"], capture_output=True, text=True, timeout=15)
        self.assertEqual(fake.returncode, 0, fake.stderr)
        self.assertEqual(json.loads(fake.stdout), {"states": {"done": 5}, "scan_errors": []})
        print('CLI 5 fake tasks: {"states": {"done": 5}, "scan_errors": []}')

    def test_429_cooldown_and_output_not_transport_error(self):
        self.assertEqual(D.transient_errors('{"type":"turn.completed","usage":{"input_tokens":429}}'), [])
        self.assertEqual(D.transient_errors('{"type":"item.completed","item":{"text":"503"}}'), [])
        self.assertEqual(D.transient_errors('{"type":"error","message":"HTTP 429"}'), ["429"])
        self.task("RATE", "fake_result: 429\n")
        self.args.fake_keys = "fake-a"
        d = self.make()
        d.streak["fake-a"] = 2
        d.tick()
        deadline = time.monotonic() + 5
        while d.running and time.monotonic() < deadline:
            time.sleep(0.03)
            d.poll()
        self.assertEqual(d.streak["fake-a"], 3)
        self.assertGreater(d.cooldown["fake-a"], time.time() + 590)
        d.tick()
        self.assertFalse(d.running)
        self.assertEqual(d.state["tasks"]["RATE"]["reason"], "waiting for key slot")

    def test_real_launcher_arguments_without_execution(self):
        self.task("REAL")
        d = self.make()
        wt = self.root / "REAL"
        wt.mkdir()
        Path(str(wt) + ".prompt.txt").write_text("approved fake prompt", encoding="utf-8")
        task = D.scan(self.tasks, self.args.worktree_root, True)[0][0]
        d.a.fake_worker = False
        d.a.launcher = HERE.parent / "chay_codex.ps1"
        row = {"status": "ready"}
        d.state["tasks"]["REAL"] = row
        with patch.object(D.subprocess, "run", return_value=SimpleNamespace(returncode=0)) as run:
            d.launch(task, "fake-a", row)
        call = run.call_args
        self.assertEqual(call.kwargs["env"]["JX_CODEX_KEY"], "fake-a")
        self.assertIn("gpt-6.1-sol", call.args[0])
        self.assertIn("max", call.args[0])
        # The mocked external worker never existed, so do not issue Stop-ScheduledTask.
        d.running.clear()


class FakeProcess:
    """Deterministic worker for multi-minute deadlines; no real executable."""
    def __init__(self):
        self.returncode = None

    def poll(self):
        return self.returncode

    def kill(self):
        self.returncode = -9

    def wait(self, timeout=None):
        return self.returncode


class WatchdogTests(Fixture):
    def attach(self, d, tid, *, key="fake-a", extra="", marker=None):
        if not (self.tasks / (tid + ".md")).exists():
            self.task(tid, extra)
        task = next(t for t in D.scan(self.tasks, self.args.worktree_root, True, {tid})[0] if t["id"] == tid)
        row = d.state["tasks"].setdefault(tid, {})
        row.update(status="running", key=key, attempts=row.get("attempts", 0) + 1)
        log = self.args.state_dir / (tid + ".log")
        done = self.args.state_dir / (tid + ".done")
        log.write_text("", encoding="utf-8")
        if done.exists():
            done.unlink()
        if marker:
            done.write_text(marker, encoding="utf-8")
        run = dict(proc=FakeProcess(), task=task, log=log, done=done, start=100,
                   last_progress=100, log_mtime=D.mtime(log), previous_done=None)
        row.update(log=str(log), done=str(done))
        d.running[tid] = run
        return row, run

    def test_watchdog_thresholds_and_log_progress(self):
        d = self.make()
        row, run = self.attach(d, "READ")
        with patch.object(D.time, "monotonic", return_value=399.9):
            d.poll()
        self.assertEqual(row["status"], "running")
        stamp = D.mtime(run["log"]) + 1_000_000_000
        os.utime(run["log"], ns=(stamp, stamp))
        with patch.object(D.time, "monotonic", return_value=400):
            d.poll()
        self.assertEqual(run["last_progress"], 400)
        with patch.object(D.time, "monotonic", return_value=700):
            d.poll()
        self.assertEqual((row["status"], row["watchdog_retries"]), ("ready", 1))
        self.assertEqual(row["log_mtime_ns"], stamp)
        row, run = self.attach(d, "WRITE", extra="readonly: false\n")
        self.assertEqual(run["task"]["watchdog_s"], 600)
        with patch.object(D.time, "monotonic", return_value=699.9):
            d.poll()
        self.assertEqual(row["status"], "running")
        with patch.object(D.time, "monotonic", return_value=700):
            d.poll()
        self.assertEqual(row["reason"], "watchdog: log stalled")

    def test_watchdog_missing_log_and_two_retries_only(self):
        d = self.make()
        for attempt in range(3):
            row, run = self.attach(d, "STUCK")
            run["log"].unlink()
            run["log_mtime"] = None
            with patch.object(D.time, "monotonic", return_value=400):
                d.poll()
            self.assertEqual(run["proc"].returncode, -9)
            self.assertEqual(row["status"], "ready" if attempt < 2 else "blocked")
        self.assertEqual((row["attempts"], row["watchdog_retries"]), (3, 2))

    def test_watchdog_prefers_less_loaded_key(self):
        d = self.make()
        row, _ = self.attach(d, "STUCK")
        _, busy = self.attach(d, "BUSY", key="fake-a")
        busy["last_progress"] = 400
        with patch.object(D.time, "monotonic", return_value=400):
            d.tick()
        self.assertEqual(row["key"], "fake-b")
        self.assertEqual(row["attempts"], 2)

    def test_stop_failure_keeps_slot_and_blocks_new_launch(self):
        d = self.make()
        row, _ = self.attach(d, "STUCK")
        self.task("NEW")
        with patch.object(d, "stop", side_effect=RuntimeError("fake stop failed")) as stop:
            with patch.object(D.time, "monotonic", return_value=400):
                d.tick()
                d.tick()
        self.assertEqual(stop.call_count, 1)
        self.assertEqual(list(d.running), ["STUCK"])
        self.assertEqual(row["status"], "blocked")

    def test_watchdog_key_load_preference_survives_waiting_for_slot(self):
        d = self.make()
        row, _ = self.attach(d, "STUCK", key="fake-a")
        _, busy = self.attach(d, "BUSY", key="fake-b")
        busy["last_progress"] = 400
        d.cooldown.update({k: time.time() + 1000 for k in d.keys})
        with patch.object(D.time, "monotonic", return_value=400):
            d.tick()
            self.assertEqual(row["reason"], "waiting for key slot")
            self.assertTrue(row["watchdog_pending"])
            d.cooldown.clear()
            d.tick()
        # Old key has zero workers, alternate has one: keep the less loaded key.
        self.assertEqual(row["key"], "fake-a")
        self.assertNotIn("watchdog_pending", row)

    def test_retry_limit_does_not_consume_failures_and_paces_all_launches(self):
        self.args.backoff_scale = 1
        d = self.make()
        for attempt in range(4):
            row, run = self.attach(d, "RATE", marker="exit=1\n", extra="retry: 1\n")
            run["log"].write_text("429 exceeded retry limit\n", encoding="utf-8")
            with patch.object(D.time, "time", return_value=1000), patch.object(D.time, "monotonic", return_value=101):
                d.poll()
            self.assertEqual(row["status"], "ready")
            self.assertEqual(row.get("failures", 0), 0)
        self.assertEqual(row["rate_limit_retries"], 4)
        self.assertEqual(row["next_at"], 1020)
        self.assertEqual(d.streak["fake-a"], 0)
        self.task("NEW")
        with patch.object(D.time, "time", return_value=1019):
            d.tick()
        self.assertFalse(d.running)
        with patch.object(D.time, "time", return_value=1020):
            d.tick()
        self.assertEqual(len(d.running), 1)
        self.assertEqual(d.state["dispatch_not_before"], 1040)
        # Four provider retries still leave the first true-error retry available.
        for tid, active in list(d.running.items()):
            d.stop(tid, active)
        d.running.clear()
        row, run = self.attach(d, "RATE", marker="exit=1\n")
        run["log"].write_text("503\n", encoding="utf-8")
        with patch.object(D.time, "monotonic", return_value=101):
            d.poll()
        self.assertEqual((row["status"], row["failures"]), ("ready", 1))

    def test_retry_limit_detection_requires_exit_one_and_transport_diagnostic(self):
        self.assertFalse(D.retry_limit_429('{"type":"item.completed","item":{"text":"429 exceeded retry limit"}}'))
        self.assertTrue(D.retry_limit_429('{"type":"error","message":"exceeded retry limit, last status: 429"}'))
        self.assertFalse(D.retry_limit_429('429 exceeded retry limit\n{"type":"turn.failed","error":{"message":"fatal invalid input"}}'))
        d = self.make()
        row, run = self.attach(d, "FAIL", marker="exit=2\n", extra="retry: 0\n")
        run["log"].write_text("429 exceeded retry limit\n", encoding="utf-8")
        with patch.object(D.time, "monotonic", return_value=101):
            d.poll()
        self.assertEqual((row["status"], row["failures"]), ("blocked", 1))
        self.assertNotIn("rate_limit_retries", row)

    def test_provider_incident_pauses_probes_every_120_seconds_and_recovers(self):
        d = self.make()
        d.probe = Mock(side_effect=[False, True])
        status = self.args.state_dir / "TRANG-THAI.md"
        status.write_text("# PM notes\nKeep this text.\n", encoding="utf-8")
        for tid in ("A", "B", "C"):
            self.attach(d, tid)
        self.task("NEW")
        with patch.object(D.time, "time", return_value=1000), patch.object(D.time, "monotonic", return_value=400):
            d.tick()
        self.assertTrue(d.state["provider_incident"]["active"])
        self.assertFalse(d.running)
        self.assertIn("sự cố nhà cung cấp", status.read_text(encoding="utf-8"))
        self.assertIn("Keep this text.", status.read_text(encoding="utf-8"))
        with patch.object(D.time, "time", return_value=1119):
            d.tick()
        d.probe.assert_not_called()
        with patch.object(D.time, "time", return_value=1120):
            d.tick()
        self.assertEqual(d.probe.call_count, 1)
        with patch.object(D.time, "time", return_value=1239):
            d.tick()
        self.assertEqual(d.probe.call_count, 1)
        with patch.object(D.time, "time", return_value=1240):
            d.tick()
        self.assertEqual(d.probe.call_count, 2)
        self.assertFalse(d.state["provider_incident"]["active"])
        self.assertEqual(len(d.running), 4)
        self.assertIn("đã hồi phục", status.read_text(encoding="utf-8"))

    def test_incident_restart_and_fake_probe_never_reads_keys(self):
        d = self.make()
        d.state["provider_incident"] = dict(active=True, next_probe_at=0)
        d.save()
        d.close()
        self.dispatcher = None
        d = self.make()
        with patch.object(D, "probe_provider", side_effect=AssertionError("real probe called")):
            self.assertTrue(d.check_provider())
        self.assertTrue(d.state["provider_incident"]["active"])
        self.assertGreater(d.state["provider_incident"]["next_probe_at"], time.time() + 119)

    def test_two_stalls_do_not_trigger_incident_and_fresh_done_wins_deadline(self):
        d = self.make()
        for tid in ("A", "B"):
            self.attach(d, tid)
        row, _ = self.attach(d, "COMPLETE", marker="exit=0\n")
        with patch.object(D.time, "monotonic", return_value=2000):
            d.poll()
        self.assertFalse(d.state.get("provider_incident"))
        self.assertEqual(row["status"], "done")

    def test_seen_all_tracks_mtime_and_survives_restart(self):
        d = self.make()
        marker = self.args.state_dir / "SAME.done"
        marker.write_text("exit=0", encoding="utf-8")
        d.observe_completions()
        d.observe_completions()
        events = self.args.state_dir / "SU-KIEN.log"
        self.assertEqual(events.read_text(encoding="utf-8").count("done-observed"), 1)
        stamp = D.mtime(marker) + 1_000_000_000
        os.utime(marker, ns=(stamp, stamp))
        d.observe_completions()
        self.assertEqual(events.read_text(encoding="utf-8").count("done-observed"), 2)
        d.save()
        d.close()
        self.dispatcher = None
        d = self.make()
        d.observe_completions()
        self.assertEqual(events.read_text(encoding="utf-8").count("done-observed"), 2)

    def test_stale_done_is_ignored_until_mtime_changes(self):
        d = self.make()
        row, run = self.attach(d, "RERUN", marker="exit=0\n")
        run["previous_done"] = D.mtime(run["done"])
        with patch.object(D.time, "monotonic", return_value=101):
            d.poll()
        self.assertEqual(row["status"], "running")
        stamp = D.mtime(run["done"]) + 1_000_000_000
        os.utime(run["done"], ns=(stamp, stamp))
        with patch.object(D.time, "monotonic", return_value=102):
            d.poll()
        self.assertEqual(row["status"], "done")

    def test_real_probe_request_is_mocked_and_secrets_never_persist(self):
        response = Mock(status=200)
        response.read.return_value = b'{"status":"completed"}'
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        opener = Mock()
        opener.open.return_value = response
        # Synthetic value stays in memory; no credential file is created/read.
        with patch.object(Path, "read_text", return_value="synthetic-test-value"), patch.object(D.request, "build_opener", return_value=opener):
            self.assertTrue(D.probe_provider("https://example.invalid/v1/responses", self.root, "fake-a", D.MODEL["sol"]))
        req = opener.open.call_args.args[0]
        self.assertEqual(req.method, "POST")
        self.assertEqual(req.get_header("User-agent"), "codex_cli_rs/0.166.0")
        self.assertEqual(json.loads(req.data)["max_output_tokens"], 16)
        self.assertEqual(opener.open.call_args.kwargs["timeout"], 15)
        self.assertIsNone(D.NoRedirect().redirect_request(req, None, 302, "", {}, "https://example.invalid/other"))
        with patch.object(Path, "read_text", side_effect=AssertionError("unexpected key read")):
            self.assertFalse(D.probe_provider("http://example.invalid/v1/responses", self.root, "fake-a", "fake"))

    def test_watchdog_kills_and_reaps_actual_isolated_fake_worker(self):
        self.task("PROCESS", "fake_result: timeout\n")
        d = self.make()
        d.tick()
        active = d.running["PROCESS"]
        active["last_progress"] = time.monotonic() - 301
        # Avoid treating initial file creation as progress in this artificial jump.
        active["log_mtime"] = D.mtime(active["log"])
        d.poll()
        self.assertIsNotNone(active["proc"].poll())
        self.assertNotIn("PROCESS", d.running)
        self.assertEqual(d.state["tasks"]["PROCESS"]["reason"], "watchdog: log stalled")

    def test_real_stop_command_is_mocked_and_checks_scheduled_task(self):
        d = self.make()
        d.a.fake_worker = False
        with patch.object(D.subprocess, "run", return_value=SimpleNamespace(returncode=0)) as stop:
            d.stop("SAFE-ID", {})
        command = stop.call_args.args[0][-1]
        self.assertIn("Stop-ScheduledTask -TaskName 'JX-codex-SAFE-ID'", command)
        self.assertIn("Get-ScheduledTask", command)
        with patch.object(D.subprocess, "run", return_value=SimpleNamespace(returncode=1)):
            with self.assertRaises(RuntimeError):
                d.stop("SAFE-ID", {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
