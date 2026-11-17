"""Full cycle: fixture loopback dùng đúng codec BOT, không có secret lưu trên đĩa."""

from contextlib import contextmanager
from datetime import date
from pathlib import Path
import secrets
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import unittest

from test_tester import HELLO  # Nạp bootstrap -I và tái dùng vector handshake E-05a.
from JX1_OPS.BOT import packets
from JX1_OPS.BOT.crypto import from_account_begin
from JX1_OPS.BOT.framing import FrameDecoder, pack_frame
from JX1_OPS.BOT.session import TEST_HOST, GS_PORT
from JX1_OPS.TESTER.core import Config, run_scenario
from JX1_OPS.TESTER.scenarios import FULL_CYCLE


@contextmanager
def cycle_server(missing=False, changed=False, bad_permit=False, real=False, permit_host=None, permit_port=None):
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(10)
    listener.settimeout(.2)
    port = listener.getsockname()[1]
    stopped = threading.Event()
    errors, records, handlers, sockets = [], [], [], []
    visits, permits = {}, {}

    def handle(sock):
        try:
            with sock:
                sock.settimeout(40)
                tx, rx = from_account_begin(HELLO)
                sock.sendall(pack_frame(HELLO))
                decoder, pending = FrameDecoder(), []

                def send(payload):
                    sock.sendall(pack_frame(tx.apply(payload)))

                def receive():
                    while not pending:
                        data = sock.recv(4096)
                        if not data:
                            decoder.finish()
                            return None
                        pending.extend(decoder.feed(data))
                    return rx.apply(pending.pop(0))

                first = receive()
                if first is None:
                    return
                if first[0] == packets.C2S.LOGIN:
                    fields = list(packets.LOGIN.unpack(first))
                    account = fields[4].split(b"\0", 1)[0]
                    fields[2] = packets.LOGIN_ACTION | 1
                    send(packets.LOGIN.pack(*fields))
                    visits[account] = visits.get(account, 0) + 1
                    role = packets.ROLE.pack(account.ljust(64, b"\0"), 0, 1,
                                             2 if changed and visits[account] > 1 else 1)
                    send(packets.ROLE_HEADER.pack(packets.S2C.ROLE_LIST, 0, 0, 0, 0)
                         + bytes([0 if missing else 1]) + (b"" if missing else role))
                    selected = receive()
                    if missing:
                        if selected is not None:
                            raise AssertionError("Không được chọn/tạo role khi thiếu gói")
                        return
                    if selected != packets.select_role(account):
                        raise AssertionError("SELECT_ROLE không khớp")
                    guid = secrets.token_bytes(16)
                    permits[guid] = account
                    send(packets.PERMIT.pack(packets.S2C.PERMIT_LOGIN, guid,
                         account.ljust(64, b"\0"), account.ljust(32, b"\0"), bytes(64), 1,
                         socket.inet_aton(permit_host or ("192.168.1.50" if bad_permit else
                                             "127.0.0.1" if real else TEST_HOST)),
                         permit_port if permit_port is not None else port if real else GS_PORT))
                    if receive() is not None:
                        raise AssertionError("Gateway phải đóng sau chọn role")
                elif first[0] == packets.C2S.LOGIC_LOGIN:
                    account = permits.pop(first[1:])
                    send(b"\x49" + bytes(303) + packets.PING.pack(packets.S2C.PING, 1)
                         + packets.SYNC.pack(packets.S2C.SYNC_END, 1, port))
                    messages, actions, run_at, skill_at = [], [], None, None
                    if real:
                        sock.settimeout(.2)
                    while True:
                        try:
                            message = receive()
                        except socket.timeout:
                            send(packets.PING.pack(packets.S2C.PING, 1))
                            continue
                        if message is None:
                            break
                        messages.append(message[0])
                        if message[0] == packets.C2S.RUN:
                            actions.append(packets.ACTION.unpack(message))
                            run_at = time.monotonic()
                        elif message[0] == packets.C2S.SKILL:
                            actions.append(packets.ACTION.unpack(message))
                            skill_at = time.monotonic()
                        elif message[0] == packets.C2S.SYNC_END:
                            if message != packets.SYNC.pack(packets.C2S.SYNC_END, 1, port):
                                raise AssertionError("ACK END phải đủ 9 byte và khớp")
                        elif message[0] == packets.C2S.CP_LOCK and message != struct.pack("<Bi", packets.C2S.CP_LOCK, 1):
                            raise AssertionError("CP_LOCK sai")
                    # Không giữ login payload/password/GUID trong bằng chứng.
                    records.append((account, messages, actions,
                                    None if run_at is None or skill_at is None else skill_at - run_at))
                else:
                    raise AssertionError("Gói đầu ngoài fixture")
        except BaseException as error:
            errors.append(type(error).__name__)  # Không phát payload/secret khi lỗi fixture.

    def serve():
        while not stopped.is_set():
            try:
                sock, _ = listener.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            sockets.append(sock)
            handler = threading.Thread(target=handle, args=(sock,), daemon=True)
            handlers.append(handler)
            handler.start()

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    try:
        yield Config("127.0.0.1", port), records, errors
    finally:
        stopped.set()
        listener.close()
        thread.join(1)
        for handler in handlers:
            handler.join(1)
        for sock in sockets:
            sock.close()


class FullCycleTests(unittest.TestCase):
    def test_cli_full_cycle_two_bots_real_30_seconds(self):
        with tempfile.TemporaryDirectory() as temp:
            with cycle_server() as (config, records, errors):
                completed = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("run.py")),
                    "--scenario", "full_cycle", "--bots", "bot01,bot02", "--workers", "2",
                    "--host", config.host, "--port", str(config.port), "--out", temp],
                    capture_output=True, timeout=48)
            self.assertEqual(completed.returncode, 0, completed.stderr.decode("utf-8"))
            self.assertEqual(errors, [])
            self.assertEqual(len(records), 4)  # Hai phiên game/bot, kể cả vào lại.
            for account in (b"bot01", b"bot02"):
                sessions = [record for record in records if record[0] == account]
                active = next(record for record in sessions if record[2])
                self.assertEqual(active[2], [(packets.C2S.RUN, 100, 200, 1),
                                             (packets.C2S.SKILL, 1, -1, 1)])
                self.assertGreaterEqual(active[3], 29.9)
                for record in sessions:
                    self.assertEqual(record[1][:3], [packets.C2S.PING, packets.C2S.SYNC_END, packets.C2S.CP_LOCK])
            report = (Path(temp) / f"{date.today().isoformat()}-full_cycle.md").read_text(encoding="utf-8")
            self.assertEqual(report.count("PASS ("), 12)
            self.assertEqual(report.count("BỎ QUA ("), 8)
            self.assertNotIn("FAIL (", report)
            self.assertIn("chưa chứng minh nhân vật còn nguyên", report)

    def test_missing_character_skips_without_guessing(self):
        with cycle_server(missing=True) as (config, records, errors):
            results = run_scenario(FULL_CYCLE, ["bot01"], config)
        self.assertEqual(errors, [])
        self.assertEqual(records, [])
        self.assertEqual(results[0].status, "PASS")
        self.assertTrue(all(result.status == "BỎ QUA" for result in results[1:]))
        self.assertIn("request/response tạo nhân vật", results[1].message)

    def test_changed_character_fails_verification(self):
        # Bỏ bước chờ/skill trong case âm; case CLI trên kiểm 30 s thật.
        from JX1_OPS.TESTER.core import Scenario
        short = Scenario("full_cycle_changed", tuple(step for step in FULL_CYCLE.steps
                         if step.name not in ("walk_30s", "attack_one")))
        with cycle_server(changed=True) as (config, _, errors):
            results = run_scenario(short, ["bot01"], config)
        self.assertEqual(errors, [])
        result = next(result for result in results if result.step == "verify_role")
        self.assertEqual(result.status, "FAIL")
        self.assertIn("thay đổi", result.message)
        self.assertEqual(results[-1].status, "BỎ QUA")

    def test_redirect_main_is_rejected_without_external_socket(self):
        from JX1_OPS.TESTER.core import Scenario
        short = Scenario("full_cycle_redirect", FULL_CYCLE.steps[:3])
        with cycle_server(bad_permit=True) as (config, records, errors):
            results = run_scenario(short, ["bot01"], config)
        self.assertEqual(errors, [])
        self.assertEqual(records, [])
        self.assertEqual(results[-1].status, "FAIL")
        self.assertIn("CHẶN CỨNG Main VM", results[-1].message)


if __name__ == "__main__":
    unittest.main()
