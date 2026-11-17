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
from unittest.mock import patch

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("dispatcher", HERE / "dispatcher.py")
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)


class DispatcherTests(unittest.TestCase):
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
        (self.tasks / (tid + ".md")).write_text(
            f"---\nid: {tid}\nstatus: active\nreadonly: true\nworktree: {self.root / tid}\n{extra}---\nFake task only.\n",
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
