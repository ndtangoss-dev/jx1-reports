"""B-03: kiểm harness bằng trace giả và các trace lỗi chủ động."""

from datetime import date
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("tester_bootstrap", Path(__file__).with_name("bootstrap.py"))
bootstrap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bootstrap)
bootstrap.load_packages()

from JX1_OPS.BOT.framing import ProtocolError
from JX1_OPS.TESTER.core import run_scenario
from JX1_OPS.TESTER.visibility import VISIBILITY, NpcView
from test_tester import fake_server


class VisibilityTests(unittest.TestCase):
    def test_three_sessions_and_todos(self):
        with fake_server(3, visibility=True) as (config, received, errors):
            results = run_scenario(VISIBILITY, ["bot01"], config)
        self.assertEqual(errors, [])
        self.assertEqual([r.status for r in results], ["PASS"] * 6 + ["BỎ QUA"] * 2)
        self.assertEqual({item["viewer"] for item in received}, {101, 102, 201})
        self.assertEqual(sum(item["skills"] for item in received), 1)
        for item in received:
            self.assertEqual(item["phases"], list(range(1, 10)))
        for result in results[-2:]:
            self.assertIn("TODO", result.message)
            self.assertIn("[CHƯA KIỂM]", result.message)
            self.assertIn("E-07/E-08", result.message)
        self.assertTrue(all(r.packets for r in results[1:6]))

    def test_bad_traces_fail_at_matching_criterion(self):
        for fault, step in (("hidden_sync", "solo"), ("hidden_add_remove", "solo"),
                            ("shared_remove", "shared_bot_remove"),
                            ("cap_leak", "group_cap"), ("cap_bot", "group_cap"),
                            ("missing_remove", "refresh"), ("missing_add", "refresh"),
                            ("disabled_diff", "disabled")):
            with self.subTest(fault=fault):
                with fake_server(3, visibility=True, visibility_fault=fault) as (config, _, errors):
                    results = run_scenario(VISIBILITY, ["bot01"], config)
                self.assertEqual(errors, [])
                failures = [r for r in results if r.status == "FAIL"]
                self.assertEqual([r.step for r in failures], [step])
                self.assertIn("AssertionError", failures[0].message)

    def test_observer_rejects_truncated_frame_without_partial_state(self):
        view = NpcView()
        # ADD hợp lệ theo fixture, sau đó record bị cắt: không áp ADD nửa frame.
        add = b"\x4c\x29\x00\x65\x00\x00\x00" + bytes(35)
        with self.assertRaises(ProtocolError):
            view.apply(add + b"\x54")
        self.assertEqual(view.visible, set())

    def test_visibility_isolated_cli_and_masked_report(self):
        with tempfile.TemporaryDirectory() as temp:
            with fake_server(3, visibility=True) as (config, received, errors):
                completed = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("run.py")),
                    "--scenario", "visibility", "--bots", "bot01", "--host", config.host,
                    "--port", str(config.port), "--out", temp], capture_output=True, timeout=20)
            self.assertEqual(completed.returncode, 0, completed.stderr.decode("utf-8"))
            self.assertEqual(errors, [])
            self.assertEqual(len(received), 3)
            text = (Path(temp) / f"{date.today().isoformat()}-visibility.md").read_text(encoding="utf-8")
            self.assertIn("BỎ QUA", text)
            self.assertIn("TODO", text)
            self.assertIn("ID=0x4c", text)
            self.assertFalse(list(Path(temp).glob("BUG-*.md")))


if __name__ == "__main__":
    unittest.main()
