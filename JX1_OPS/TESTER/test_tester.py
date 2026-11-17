"""Test tổng hợp; chỉ mở socket 127.0.0.1 trong fixture máy chủ giả."""

from contextlib import contextmanager, redirect_stderr
from datetime import date
import argparse
import hashlib
import importlib.util
import io
import multiprocessing
import os
from pathlib import Path
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("tester_bootstrap", Path(__file__).with_name("bootstrap.py"))
bootstrap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bootstrap)
bootstrap.load_packages()

from JX1_OPS.BOT.crypto import RollingXor
from JX1_OPS.BOT.framing import FrameDecoder, pack_frame
from JX1_OPS.TESTER.core import Config, Context, Redactor, Result, Scenario, SkipStep, Step, run_scenario
from JX1_OPS.TESTER.reporting import report_lock, write_report
from JX1_OPS.TESTER.run import bot_list, main
from JX1_OPS.TESTER.scenarios import SMOKE_LOGIN

# Vector từ BOT/test_bot.py và test_worldsync.py; đều là dữ liệu tổng hợp.
HELLO = bytes.fromhex("200000000000000087a9cbed10325476") + bytes(16)
END = bytes.fromhex("430100000004030201")
PING = bytes.fromhex("8f04030201")


@contextmanager
def fake_server(count, malformed=False, visibility_fault=None, visibility=False):
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(5)
    listener.settimeout(8)
    received, errors, handlers = [], [], []

    def handle(sock):
        try:
            with sock:
                sock.settimeout(4)
                tx, rx = RollingXor(0x12345678), RollingXor(0x89ABCDEF)
                if visibility:
                    visibility_dialogue(sock, tx, rx, received, visibility_fault)
                    return
                payload = b"\xff" + bytes(400) if malformed else b"\x49" + bytes(303) + PING + END
                wire = pack_frame(HELLO) + pack_frame(tx.apply(payload))
                # TCP fragmentation/coalescing qua BOT.Channel, không phát minh codec.
                for offset in range(0, len(wire), 7):
                    sock.sendall(wire[offset:offset + 7])
                decoder, messages = FrameDecoder(), []
                while True:
                    data = sock.recv(4096)
                    if not data:
                        break
                    messages.extend(rx.apply(frame) for frame in decoder.feed(data))
                received.append(messages)
        except BaseException as error:
            errors.append(error)

    def serve():
        try:
            for _ in range(count):
                sock, _ = listener.accept()
                thread = threading.Thread(target=handle, args=(sock,), daemon=True)
                handlers.append(thread)
                thread.start()
        except OSError as error:
            errors.append(error)

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    try:
        yield Config("127.0.0.1", listener.getsockname()[1]), received, errors
    finally:
        listener.close()
        thread.join(1)
        for handler in handlers:
            handler.join(1)


def visibility_dialogue(sock, tx, rx, received, fault):
    """Script trace độc lập; không gọi luật/observer visibility để tạo đáp án.

    NPC identity offset chỉ là hợp đồng dữ liệu giả, không khẳng định ABI thật.
    Hai viewer người thật 101/102, Bot 201; phase điều khiển qua RUN tổng hợp.
    """
    def record(protocol, npc):
        size = {76: 42, 77: 227, 84: 9}[protocol]
        data = bytearray(size)
        data[0] = protocol
        if protocol == 76:
            struct.pack_into("<H", data, 1, size - 1)
        struct.pack_into("<I", data, 3 if protocol == 76 else 1, npc)
        return bytes(data)

    sock.sendall(pack_frame(HELLO))
    decoder, viewer, last_phase, attacked = FrameDecoder(), None, 0, False
    summary = {"viewer": None, "phases": [], "skills": 0}
    received.append(summary)
    while True:
        data = sock.recv(4096)
        if not data:
            return
        for frame in decoder.feed(data):
            request = rx.apply(frame)
            protocol, x, y, map_id = packets_action(request)
            if protocol == 77:
                assert viewer == 101 and last_phase == 1 and (x, y, map_id) == (1, -1, 201)
                attacked = True
                summary["skills"] += 1
                continue
            assert protocol == 76 and map_id == 1 and x == last_phase + 1
            if viewer is None:
                assert y in (101, 102, 201)
                viewer = summary["viewer"] = y
            assert y == viewer
            last_phase = x
            summary["phases"].append(x)
            other = 102 if viewer == 101 else 101
            # Scripts cố định theo viewer/phase; Bot luôn có cả A/B trong trace.
            if x == 1:
                ids = (101, 102, 201) if viewer == 201 else (viewer, 201)
                events = [(76, npc) for npc in ids] + [(77, 201)]
            elif x == 2:
                if viewer == 101:
                    assert attacked
                events = [(84, 201)]
            elif x == 3:
                events = ([] if viewer == 201 else [(76, other)]) + [(76, 201), (77, 201)]
            elif x in (4, 6):
                events = ([] if viewer == 201 else [(84, other)]) + [(77, 201)]
            elif x in (5, 7):
                events = ([] if viewer == 201 else [(76, other)]) + [(77, 201)]
            else:
                events = [(77, npc) for npc in (101, 102, 201)]
            if viewer == 102:
                if fault == "hidden_sync" and x == 1:
                    events.append((77, 101))
                if fault == "hidden_add_remove" and x == 1:
                    events.extend(((76, 101), (84, 101)))
                if fault == "shared_remove" and x == 2:
                    events = [(77, 102)]
                if fault == "missing_remove" and x == 6:
                    events = [(77, 201)]
                if fault == "missing_add" and x == 7:
                    events = [(77, 101), (77, 201)]
                if fault == "cap_leak" and x == 4:
                    events = [(77, 201)]
                if fault == "cap_bot" and x == 4:
                    events.append((84, 201))
            payload = b"".join(record(*event) for event in events)
            if fault == "disabled_diff" and viewer == 102 and x == 9:
                payload = payload[:-1] + b"\x01"
            wire = pack_frame(tx.apply(payload))
            for offset in range(0, len(wire), 7):
                sock.sendall(wire[offset:offset + 7])


def packets_action(request):
    # Chỉ giải action fixture, không giữ payload trong log/kết quả.
    assert len(request) == 13
    return struct.unpack("<Biii", request)


def okay(context):
    context.state["owner"] = context.bot
    context.log("synthetic log")


def check_state(context):
    assert context.state["owner"] == context.bot


def fail_one(context):
    if context.bot == "bot01":
        raise ValueError("synthetic failure")


def forever(context):
    context.packet("nhận", b"\xff" + bytes(range(256)) * 2)
    context.log("before hang")
    time.sleep(60)


def abrupt_exit(context):
    os._exit(7)


def skip(context):
    raise SkipStep("Không áp dụng")


def false_result(context):
    return False


def secret_failure(context):
    secret = context.config.secrets[0]
    print(secret * 2000)
    context.log("password='unknown synthetic password' " + secret)
    context.packet("gửi", b"\x41" + secret.encode() * 100)
    raise ValueError(secret + " " + hashlib.md5(secret.encode()).hexdigest().upper())


class TesterTests(unittest.TestCase):
    def test_smoke_five_bots_sequential_and_parallel(self):
        for workers in (1, 5):
            with self.subTest(workers=workers), fake_server(5) as (config, received, errors):
                results = run_scenario(SMOKE_LOGIN, [f"bot{i:02d}" for i in range(1, 6)], config, workers)
            self.assertEqual([r.status for r in results], ["PASS"] * 15)
            self.assertEqual(errors, [])
            self.assertEqual(len(received), 5)
            for messages in received:
                self.assertEqual(len(messages), 3)
                self.assertEqual(messages[0][0], 0x7A)  # PING_REPLY
                self.assertEqual(messages[1:], [END, b"\x7c\x01\0\0\0"])

    def test_state_preserved_and_independent(self):
        scenario = Scenario("state", (Step("set", okay, "set"), Step("check", check_state, "owner")))
        results = run_scenario(scenario, ["bot01", "bot02"], Config("127.0.0.1", 1), 2)
        self.assertEqual([r.status for r in results], ["PASS"] * 4)

    def test_exception_isolates_bot_and_skips_remaining(self):
        scenario = Scenario("fail", (Step("first", fail_one, "pass"), Step("next", okay, "pass")))
        results = run_scenario(scenario, ["bot01", "bot02"], Config("127.0.0.1", 1), 2)
        self.assertEqual([r.status for r in results], ["FAIL", "BỎ QUA", "PASS", "PASS"])

    def test_timeout_kills_worker_and_keeps_evidence(self):
        scenario = Scenario("hang", (Step("hang", forever, "return", .15), Step("next", okay, "pass")))
        started = time.monotonic()
        results = run_scenario(scenario, ["bot01"], Config("127.0.0.1", 1))
        self.assertLess(time.monotonic() - started, 4)
        self.assertEqual([r.status for r in results], ["FAIL", "BỎ QUA"])
        self.assertIn("Timeout", results[0].message)
        self.assertIn("before hang", results[0].logs)
        self.assertEqual(len(bytes.fromhex(results[0].packets[0]["hex"])), 256)
        self.assertEqual(multiprocessing.active_children(), [])

    def test_abrupt_worker_exit_is_fail(self):
        scenario = Scenario("exit", (Step("exit", abrupt_exit, "return"),))
        results = run_scenario(scenario, ["bot01"], Config("127.0.0.1", 1))
        self.assertEqual(results[0].status, "FAIL")
        self.assertIn("Worker", results[0].message)

    def test_skip_and_false(self):
        scenario = Scenario("skip", (Step("skip", skip, "skip"), Step("false", false_result, "true")))
        results = run_scenario(scenario, ["bot01"], Config("127.0.0.1", 1))
        self.assertEqual([r.status for r in results], ["BỎ QUA", "FAIL"])

    def test_malformed_fake_packet_creates_bug_and_hex(self):
        with tempfile.TemporaryDirectory() as temp:
            with fake_server(1, malformed=True) as (config, _, errors):
                results = run_scenario(SMOKE_LOGIN, ["bot01"], config)
            self.assertEqual(errors, [])
            self.assertEqual([r.status for r in results], ["PASS", "FAIL", "BỎ QUA"])
            report = write_report(temp, SMOKE_LOGIN, ["bot01"], results, branch="test", commit="synthetic")
            text = report.read_text(encoding="utf-8")
            self.assertIn("nhận; ID=0xff; 401 byte; hex=ff" + "00" * 255, text)
            self.assertIn("BUG-001.md", text)

    def test_secret_redaction_across_worker_report_and_bug(self):
        secret = "synthetic-private-abcdef"
        scenario = Scenario("secret", (Step("fail", secret_failure, "password=hidden"),))
        with tempfile.TemporaryDirectory() as temp:
            results = run_scenario(scenario, ["bot01"], Config("127.0.0.1", 1, (secret,)))
            write_report(temp, scenario, ["bot01"], results, (secret,), "test", "synthetic")
            text = "".join(path.read_text(encoding="utf-8") for path in Path(temp).glob("*.md"))
            for value in (secret, secret.encode().hex(), hashlib.md5(secret.encode()).hexdigest().upper(),
                          "unknown synthetic password"):
                self.assertNotIn(value, text)
            self.assertIn("[ẨN]", text)
            self.assertIn("gửi; ID=0x41", text)

    def test_environment_and_key_redaction(self):
        with patch.dict(os.environ, {"JX_BOT_ACCOUNT": "synthetic-account", "JX_BOT_CLIENT_KEY": "0x11223344"}):
            redactor = Redactor()
        cleaned = redactor.clean("synthetic-account 0x11223344 287454020 44332211 token=unknown")
        for value in ("synthetic-account", "0x11223344", "287454020", "44332211", "unknown"):
            self.assertNotIn(value, cleaned)

    def test_bug_dedup_open_only_max_number_and_history(self):
        scenario = Scenario("bugs", (Step("a", okay, "pass", severity="blocker"),))
        def failure(bot="bot01", message="same"):
            return Result(bot, "a", "FAIL", .01, message, ["log"])
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            (out / "BUG-009.md").write_text("# historical\nStatus: CLOSED\n", encoding="utf-8")
            first = write_report(out, scenario, ["bot01"], [failure()], branch="test", commit="synthetic")
            second = write_report(out, scenario, ["bot02"], [failure("bot02")], branch="test", commit="synthetic")
            self.assertNotEqual(first, second)
            bug = out / "BUG-010.md"
            text = bug.read_text(encoding="utf-8")
            self.assertIn("tái hiện lần 2", text)
            self.assertIn("bot02", text)
            self.assertIn("Độ nặng: blocker", text)
            write_report(out, scenario, ["bot01"], [failure()], branch="test", commit="synthetic")
            self.assertIn("tái hiện lần 3", bug.read_text(encoding="utf-8"))
            bug.write_text(bug.read_text(encoding="utf-8").replace("Status: OPEN", "Status: CLOSED"), encoding="utf-8")
            write_report(out, scenario, ["bot01"], [failure()], branch="test", commit="synthetic")
            self.assertTrue((out / "BUG-011.md").exists())
            write_report(out, scenario, ["bot01"], [failure(message="different")], branch="test", commit="synthetic")
            self.assertTrue((out / "BUG-012.md").exists())

    def test_report_lock_refuses_concurrent_write(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            with report_lock(out):
                with self.assertRaises(RuntimeError):
                    with report_lock(out):
                        pass
            self.assertFalse((out / ".tester.lock").exists())

    def test_missing_invalid_cli_config_no_socket(self):
        with patch("socket.create_connection", side_effect=AssertionError("network forbidden")):
            for args in ([], ["--scenario", "smoke_login"],
                         ["--scenario", "smoke_login", "--bots", "bot01", "--host", "192.168.56.150", "--port", "1", "--out", "."],
                         ["--scenario", "smoke_login", "--bots", "bot01", "--host", "127.0.0.1", "--port", "0", "--out", "."]):
                with self.subTest(args=args), redirect_stderr(io.StringIO()) as stream:
                    with self.assertRaises(SystemExit) as error:
                        main(args)
                    self.assertEqual(error.exception.code, 2)
                    self.assertIn("usage:", stream.getvalue())

    def test_bot_ranges_and_invalid_step(self):
        self.assertEqual(bot_list("bot01..bot05"), [f"bot{i:02d}" for i in range(1, 6)])
        self.assertEqual(bot_list("bot02,bot05"), ["bot02", "bot05"])
        for value in ("bot05..bot01", "bot01,bot01", "bot06", "../bot01"):
            with self.assertRaises(argparse.ArgumentTypeError):
                bot_list(value)
        for value in (0, -1, float("inf"), float("nan")):
            with self.assertRaises(ValueError):
                Step("a", okay, "pass", value)

    def test_isolated_cli_end_to_end(self):
        with tempfile.TemporaryDirectory() as temp, fake_server(1) as (config, _, errors):
            completed = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("run.py")),
                "--scenario", "smoke_login", "--bots", "bot01", "--host", config.host,
                "--port", str(config.port), "--out", temp], capture_output=True, timeout=12)
            self.assertEqual(completed.returncode, 0, completed.stderr.decode("utf-8"))
            report = Path(temp) / f"{date.today().isoformat()}-smoke_login.md"
            self.assertIn("PASS", report.read_text(encoding="utf-8"))
            self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
