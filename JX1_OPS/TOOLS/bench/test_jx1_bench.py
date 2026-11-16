import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import jx1_bench

HERE = Path(__file__).resolve().parent


class BenchAnalysisTests(unittest.TestCase):
    def fixture(self):
        return jx1_bench.load_payload(HERE / "sample_metrics.json")

    def test_expected_sample_metrics(self):
        result = jx1_bench.analyze_payload(self.fixture())
        self.assertEqual(result["target"]["ip"], jx1_bench.TEST_VM_IP)
        self.assertAlmostEqual(result["tick"]["avg_ms"], 51.0)
        self.assertAlmostEqual(result["tick"]["p95_ms"], 53.7)
        self.assertAlmostEqual(result["network"]["rx_mbps"], 8.0)
        self.assertAlmostEqual(result["network"]["tx_mbps"], 4.0)
        self.assertAlmostEqual(result["network"]["total_mbps"], 12.0)
        self.assertAlmostEqual(result["network"]["seconds"], 4.5)
        self.assertAlmostEqual(result["frames"]["avg_fps"], 59.0)
        self.assertAlmostEqual(result["frames"]["min_fps"], 58.0)
        self.assertAlmostEqual(result["frames"]["p05_fps"], 58.1)

    def test_interval_rates_use_total_time_not_mean_of_rates(self):
        data = self.fixture()
        data["network_mode"] = "interval"
        data["network_samples"] = [
            {"rx_bytes": 1000000, "tx_bytes": 500000, "interval_s": 1},
            {"rx_bytes": 1000000, "tx_bytes": 500000, "interval_s": 3},
        ]
        result = jx1_bench.analyze_payload(data)
        self.assertAlmostEqual(result["network"]["rx_mbps"], 4.0)
        self.assertAlmostEqual(result["network"]["tx_mbps"], 2.0)

    def test_cumulative_counter_reset_or_bad_time_fails(self):
        for field, value in (("rx_bytes", 0), ("tx_bytes", 0), ("time_s", 0), ("time_s", -1)):
            with self.subTest(field=field, value=value):
                data = self.fixture()
                data["network_samples"][1][field] = value
                with self.assertRaises(jx1_bench.InputError):
                    jx1_bench.analyze_payload(data)

    def test_missing_network_mode_or_baseline_fails(self):
        for mode in ("missing", "one_sample"):
            data = self.fixture()
            if mode == "missing":
                data.pop("network_mode")
            else:
                data["network_samples"] = data["network_samples"][:1]
            with self.subTest(mode=mode), self.assertRaises(jx1_bench.InputError):
                jx1_bench.analyze_payload(data)

    def test_main_vm_is_rejected_in_target_and_nested_metadata(self):
        for location in ("target", "metadata_value", "metadata_key"):
            data = self.fixture()
            if location == "target":
                data["target"]["ip"] = jx1_bench.MAIN_VM_IP
            elif location == "metadata_value":
                data["metadata"] = {"url": "http://" + jx1_bench.MAIN_VM_IP + "/"}
            else:
                data["metadata"] = {jx1_bench.MAIN_VM_IP: "blocked"}
            with self.subTest(location=location):
                with self.assertRaisesRegex(jx1_bench.InputError, "Main VM bi chan"):
                    jx1_bench.analyze_payload(data)

    def test_network_input_is_blocked_before_file_read(self):
        paths = (
            "//" + jx1_bench.MAIN_VM_IP + "/share/metrics.json",
            "//" + jx1_bench.TEST_VM_IP + "/share/metrics.json",
        )
        for name in paths:
            with self.subTest(path=name), patch.object(Path, "read_text") as reader:
                with self.assertRaises(jx1_bench.InputError):
                    jx1_bench.load_payload(Path(name))
                reader.assert_not_called()

    def test_other_target_is_rejected(self):
        for field, value in (("name", "other-fixture"), ("ip", "127.0.0.1")):
            data = self.fixture()
            data["target"][field] = value
            with self.subTest(field=field), self.assertRaises(jx1_bench.InputError):
                jx1_bench.analyze_payload(data)

    def test_bad_values_and_empty_series_fail(self):
        for value in (-1, True, None, "50", float("nan"), float("inf")):
            data = self.fixture()
            data["tick_samples"][0]["tick_ms"] = value
            with self.subTest(value=value), self.assertRaises(jx1_bench.InputError):
                jx1_bench.analyze_payload(data)
        for key in ("tick_samples", "network_samples", "frame_samples"):
            data = self.fixture()
            data[key] = []
            with self.subTest(series=key), self.assertRaises(jx1_bench.InputError):
                jx1_bench.analyze_payload(data)

    def test_invalid_interval_and_ambiguous_frames_fail(self):
        for sample in (
            {"fps": 60}, {"frames": 60, "interval_s": 0},
            {"fps": 60, "frames": 60, "interval_s": 1},
            {"interval_s": 1},
        ):
            data = self.fixture()
            data["frame_samples"] = [sample]
            with self.subTest(sample=sample), self.assertRaises(jx1_bench.InputError):
                jx1_bench.analyze_payload(data)

    def test_utf8_bom_is_accepted_and_bad_json_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "metrics.json"
            path.write_text(json.dumps(self.fixture()), encoding="utf-8-sig")
            self.assertEqual(jx1_bench.load_payload(path)["network_mode"], "cumulative")
            path.write_text("{", encoding="utf-8")
            with self.assertRaises(jx1_bench.InputError):
                jx1_bench.load_payload(path)

    def test_cli_failure_has_no_partial_table(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = jx1_bench.main(["--input", "//" + jx1_bench.MAIN_VM_IP + "/metrics.json"])
        self.assertEqual(code, 2)
        self.assertEqual(out.getvalue(), "")
        self.assertIn("Main VM bi chan", err.getvalue())

    def test_one_command_from_another_directory_outputs_table_and_json(self):
        with tempfile.TemporaryDirectory() as temp:
            for extra in ([], ["--json"]):
                result = subprocess.run(
                    [sys.executable, "-I", str(HERE / "jx1_bench.py"), *extra],
                    cwd=temp, capture_output=True, text=True, timeout=15,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                if extra:
                    self.assertEqual(json.loads(result.stdout)["frames"]["avg_fps"], 59.0)
                else:
                    for label in ("gs001 tick p95", "guest RX", "guest TX", "client FPS trung binh"):
                        self.assertIn(label, result.stdout)


if __name__ == "__main__":
    unittest.main()
