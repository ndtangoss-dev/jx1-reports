"""Vector tự dựng từ source; socket giả hoàn toàn, không kết nối VM/loopback.

Kết quả không chứng minh binary đang chạy tương thích hoặc Bot đã online.
"""

import importlib.util
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

package_dir = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "jx1bot", package_dir / "__init__.py", submodule_search_locations=[str(package_dir)])
package = importlib.util.module_from_spec(spec)
sys.modules["jx1bot"] = package
spec.loader.exec_module(package)

from jx1bot import packets
from jx1bot.crypto import RollingXor, from_account_begin
from jx1bot.framing import FrameDecoder, ProtocolError, pack_frame
from jx1bot.session import Channel, Session, State, check_admission, validate_target

# Chỉ dữ liệu tự dựng: các khóa không thuộc tài khoản/server nào.
HELLO = bytes.fromhex("200000000000000087a9cbed10325476") + bytes(16)
GUID = bytes(range(16))
ACCOUNT = "offline_bot"
PASSWORD = "synthetic-only"
ROLE_NAME = b"offline_role"
CLIENT_KEY = 0x01020304


class FramingTests(unittest.TestCase):
    def test_golden_frame_includes_header(self):
        self.assertEqual(pack_frame(b"\x82\x01"), bytes.fromhex("04008201"))

    def test_every_split_and_coalesced_frames(self):
        wire = pack_frame(b"abc") + pack_frame(bytes(range(255))) + pack_frame(b"z")
        for split in range(len(wire) + 1):
            decoder = FrameDecoder()
            self.assertEqual(decoder.feed(wire[:split]) + decoder.feed(wire[split:]),
                             [b"abc", bytes(range(255)), b"z"])
            decoder.finish()

    def test_byte_at_a_time(self):
        decoder, result = FrameDecoder(), []
        for value in bytes.fromhex("04008201030043"):
            result += decoder.feed(bytes([value]))
        self.assertEqual(result, [b"\x82\x01", b"\x43"])

    def test_invalid_lengths_poison_decoder(self):
        for size in (0, 1, 2):
            decoder = FrameDecoder()
            with self.assertRaises(ProtocolError):
                decoder.feed(struct.pack("<H", size))
            with self.assertRaises(ProtocolError):
                decoder.feed(pack_frame(b"x"))

    def test_size_boundary_and_eof(self):
        self.assertEqual(pack_frame(bytes(65533))[:2], b"\xff\xff")
        for data in (b"", bytes(65534)):
            with self.assertRaises(ProtocolError):
                pack_frame(data)
        for data in (b"\x03", b"\x04\x00x"):
            decoder = FrameDecoder()
            decoder.feed(data)
            with self.assertRaises(ProtocolError):
                decoder.finish()


class CryptoTests(unittest.TestCase):
    def test_golden_word_tail_and_next_key(self):
        cipher = RollingXor(0x12345678)
        self.assertEqual(cipher.apply(bytes(range(7))).hex(), "785736117c5332")
        self.assertEqual(cipher.key, 0x3C5EFC8D)
        self.assertEqual(cipher.apply(b"\x82\x01").hex(), "0ffd")

    def test_wrapping_and_empty(self):
        cipher = RollingXor(0xFFFFFFFF)
        self.assertEqual(cipher.apply(b""), b"")
        self.assertEqual(cipher.key, 0xFFFFFFFF)
        self.assertEqual(cipher.apply(b"\0"), b"\xff")
        self.assertEqual(cipher.key, 0x080883E6)

    def test_account_begin_complement_and_direction(self):
        rx, tx = from_account_begin(HELLO)
        self.assertEqual(rx.key, 0x12345678)
        self.assertEqual(tx.key, 0x89ABCDEF)
        tx.apply(b"abc")
        self.assertEqual(rx.key, 0x12345678)

    def test_unsupported_mode_and_bad_hello(self):
        for hello in (HELLO[:-1], HELLO + b"x", b"\x21" + HELLO[1:], HELLO[:1] + b"\x01" + HELLO[2:]):
            with self.assertRaises(ProtocolError):
                from_account_begin(hello)

    def test_round_trip_varied_frames(self):
        enc, dec = RollingXor(0xFFFFFFFF), RollingXor(0xFFFFFFFF)
        for length in (1, 2, 3, 4, 5, 8, 65, 147, 65533):
            value = bytes(i % 256 for i in range(length))
            self.assertEqual(dec.apply(enc.apply(value)), value)
            self.assertEqual(dec.key, enc.key)


def request():
    return packets.login(ACCOUNT, PASSWORD, 1, 0)


def response(result=1):
    data = bytearray(request())
    struct.pack_into("<i", data, 3, 0x050000 | result)
    return bytes(data)


def roles():
    # KProtocol.h:1819: offset pDataBuffer=14; count trước RoleBaseInfo.
    return bytes.fromhex("37") + struct.pack("<IIBI", 68, 0, 0, 1) + b"\x01" + ROLE_NAME.ljust(64, b"\0") + b"\x00\x02\x19"


def permit(host=b"\xc0\xa8\x38\x96", port=51189):
    return packets.PERMIT.pack(52, GUID, ROLE_NAME.ljust(64, b"\0"),
                               ACCOUNT.encode().ljust(32, b"\0"), bytes(64), 1, host, port)


class PacketTests(unittest.TestCase):
    def test_md5_uppercase_and_login_offsets(self):
        self.assertEqual(packets.password_md5("abc"), b"900150983CD24FB0D6963F7D28E17F72")
        data = packets.login("abc", "abc", 2, 3)
        self.assertEqual(len(data), 147)
        self.assertEqual(data[:11].hex(), "4192000000050000000000")
        self.assertEqual(data[11:43], b"abc" + bytes(29))
        self.assertEqual(data[43:107], b"900150983CD24FB0D6963F7D28E17F72" + bytes(32))
        self.assertEqual(data[-12:].hex(), "020000000300000001000000")

    def test_reject_truncating_credentials(self):
        for account, password in (("a" * 17, "abc"), ("abc", "b" * 17), ("a\0b", "abc"), ("abc", ""), ("é", "abc")):
            with self.assertRaises(ProtocolError):
                packets.login(account, password, 1, 0)

    def test_auth_checks_result_account_hash_size_version(self):
        packets.check_login_response(response(), request())
        invalid = [response(3), response()[:-1]]
        for offset in (1, 11, 43, 143):
            data = bytearray(response())
            data[offset] ^= 1
            invalid.append(bytes(data))
        for data in invalid:
            with self.assertRaises(ProtocolError):
                packets.check_login_response(data, request())

    def test_role_and_permit(self):
        role = packets.role_list(roles())[0]
        self.assertEqual((role.name, role.sex, role.series, role.level), (ROLE_NAME, 0, 2, 25))
        self.assertEqual(packets.select_role(role.name), b"\x6c" + ROLE_NAME.ljust(64, b"\0"))
        destination = packets.permit_login(permit(), ACCOUNT, ROLE_NAME)
        self.assertEqual((destination.host, destination.port), ("192.168.56.150", 51189))
        self.assertEqual(packets.logic_login(destination.guid), b"\x42" + GUID)

    def test_role_permit_bad_lengths_and_identity(self):
        for data in (roles()[:-1], roles() + b"x"):
            with self.assertRaises(ProtocolError):
                packets.role_list(data)
        for data, role in ((permit()[:-1], ROLE_NAME), (permit(), b"other")):
            with self.assertRaises(ProtocolError):
                packets.permit_login(data, ACCOUNT, role)

    def test_action_golden_vectors(self):
        self.assertEqual(packets.run(1, 2, 3).hex(), "4c010000000200000003000000")
        self.assertEqual(packets.skill(7, -1, 99).hex(), "4d07000000ffffffff63000000")
        self.assertEqual(packets.sit(True).hex(), "8201")
        self.assertEqual(packets.sit(False).hex(), "8200")
        self.assertEqual(packets.ping_reply(bytes.fromhex("8f04030201"), 0x05060708).hex(),
                         "7a0403020108070605")

    def test_bad_actions(self):
        for make in (lambda: packets.run(-1, 0, 0), lambda: packets.run(2**31, 0, 0),
                     lambda: packets.skill(0, 0, 0), lambda: packets.skill(1, -2, 0),
                     lambda: packets.skill(1, -1, -1), lambda: packets.sit(1)):
            with self.assertRaises(ProtocolError):
                make()

    def test_sync_golden_and_key_mismatch(self):
        data = bytes.fromhex("430100000004030201")
        self.assertEqual(packets.sync_reply(data, CLIENT_KEY), data)
        for payload, key in ((b"\x43", CLIENT_KEY), (data, 0), (b"\x43" + bytes(8), CLIENT_KEY)):
            with self.assertRaises(ProtocolError):
                packets.sync_reply(payload, key)

    def test_bundle_and_reject_unknown_without_scanning(self):
        sync = bytes.fromhex("430100000004030201")
        ping = bytes.fromhex("8f04030201")
        self.assertEqual(packets.game_messages(sync + ping), [sync, ping])
        for data in (b"\x44" + sync, b"\x8f\x43", sync + b"\x99"):
            with self.assertRaises(ProtocolError):
                packets.game_messages(data)


class MemorySocket:
    def __init__(self, data, step=65536):
        self.data = bytearray(data)
        self.step = step
        self.sent = bytearray()
        self.closed = False

    def recv(self, size):
        size = min(size, self.step)
        result = bytes(self.data[:size])
        del self.data[:size]
        return result

    def sendall(self, data):
        self.sent.extend(data)

    def settimeout(self, timeout):
        pass

    def close(self):
        self.closed = True


def channel_for(messages, step=65536):
    encoder = RollingXor(0x12345678)
    wire = pack_frame(HELLO) + b"".join(pack_frame(encoder.apply(p)) for p in messages)
    sock = MemorySocket(wire, step)
    channel = Channel(sock)
    channel.handshake()
    return channel


def sent_messages(channel):
    decoder, cipher = FrameDecoder(), RollingXor(0x89ABCDEF)
    return [cipher.apply(p) for p in decoder.feed(channel.sock.sent)]


class ChannelSessionTests(unittest.TestCase):
    def test_framing_crypto_partial_tcp_integration(self):
        for step in (1, 2, 7, 65536):
            channel = channel_for([b"first", b"second"], step)
            self.assertEqual(channel.receive(), b"first")
            self.assertEqual(channel.receive(), b"second")
            channel.send(b"one")
            channel.send(b"two")
            self.assertEqual(sent_messages(channel), [b"one", b"two"])

    def test_eof_and_no_send_before_handshake(self):
        channel = Channel(MemorySocket(b"\x03\0"))
        with self.assertRaises(ProtocolError):
            channel.send(b"x")
        with self.assertRaises(ProtocolError):
            channel.handshake()

    def test_target_and_capacity_guards_before_socket(self):
        for host, port in (("192.168.1.50", 56722), ("::ffff:192.168.1.50", 56722),
                           ("3232235826", 56722), ("localhost", 56722),
                           ("192.168.56.150", 80), ("192.168.56.151", 51189)):
            with self.assertRaises(ProtocolError):
                validate_target(host, port)
        for observed in (-1, 100, True, 1.5):
            with self.assertRaises(ProtocolError):
                check_admission(observed)
        check_admission(99)
        with patch("jx1bot.session.socket.create_connection") as connect:
            with self.assertRaises(ProtocolError):
                Channel.connect("192.168.1.50", 56722, 1)
            connect.assert_not_called()

    def make_session(self, permit_data=None, game_data=None):
        gateway = channel_for([response(), roles(), permit() if permit_data is None else permit_data])
        game = channel_for([bytes.fromhex("430100000004030201")] if game_data is None else game_data)
        calls = []
        def connect(host, port, timeout):
            calls.append((host, port))
            return gateway if port == 56722 else game
        return Session(connector=connect), gateway, game, calls

    def test_source_profile_flow_and_actions_offline(self):
        session, gateway, game, calls = self.make_session()
        session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 99)
        self.assertEqual(session.state, State.IN_GAME)
        self.assertEqual(calls, [("192.168.56.150", 56722), ("192.168.56.150", 51189)])
        self.assertTrue(gateway.sock.closed)
        with patch("jx1bot.session.time.sleep"):
            session.run(1, 2, 3)
            session.skill(7, -1, 99)
            session.sit(True)
            session.sit(False)
        self.assertEqual(sent_messages(gateway), [request(), packets.select_role(ROLE_NAME)])
        self.assertEqual(sent_messages(game), [b"\x42" + GUID, bytes.fromhex("430100000004030201"),
            bytes.fromhex("7c01000000"), packets.run(1, 2, 3), packets.skill(7, -1, 99), b"\x82\x01", b"\x82\0"])
        session.close()
        self.assertTrue(game.sock.closed)

    def test_redirect_to_main_never_connects_gs(self):
        session, gateway, game, calls = self.make_session(permit_data=permit(b"\xc0\xa8\x01\x32"))
        with self.assertRaisesRegex(ProtocolError, "Main VM"):
            session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 0)
        self.assertEqual(len(calls), 1)
        self.assertEqual(session.state, State.CLOSED)
        self.assertTrue(gateway.sock.closed)
        self.assertEqual(game.sock.sent, b"")

    def test_unknown_sync_fails_closed_no_game_actions(self):
        session, _, game, _ = self.make_session(game_data=[b"\x44" + bytes.fromhex("430100000004030201")])
        with self.assertRaisesRegex(ProtocolError, "chưa hỗ trợ"):
            session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 0)
        self.assertEqual(session.state, State.CLOSED)
        self.assertTrue(game.sock.closed)
        self.assertEqual(sent_messages(game), [b"\x42" + GUID])

    def test_actions_require_in_game(self):
        session = Session()
        for action in (lambda: session.run(1, 2, 3), lambda: session.skill(7, -1, 99), lambda: session.sit()):
            with self.assertRaises(ProtocolError):
                action()

    def test_idle_answers_ping_without_movement(self):
        session, _, game, _ = self.make_session(game_data=[
            bytes.fromhex("430100000004030201"), bytes.fromhex("8f04030201")])
        session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 0)
        with patch("jx1bot.session.time.monotonic", return_value=1.0):
            session.poll()
        self.assertEqual(sent_messages(game)[-1].hex(), "7a04030201e8030000")
        self.assertEqual(session.state, State.IN_GAME)
        session.close()

    def test_hold_deadline_keeps_session_until_caller_closes(self):
        session, _, game, _ = self.make_session()
        session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 0)
        before = bytes(game.sock.sent)
        with patch.object(game, "receive", side_effect=TimeoutError), patch("jx1bot.session.time.monotonic", return_value=10.0):
            session.hold(10)
        self.assertEqual(session.state, State.IN_GAME)
        self.assertEqual(bytes(game.sock.sent), before)
        session.close()

    def test_18hz_action_spacing(self):
        session, _, game, _ = self.make_session()
        session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 0)
        with patch("jx1bot.session.time.monotonic", return_value=10.0), patch("jx1bot.session.time.sleep") as sleep:
            session.sit(True)
            session.sit(False)
            sleep.assert_called_once()
            self.assertAlmostEqual(sleep.call_args.args[0], 1 / 18)
        session.close()


if __name__ == "__main__":
    unittest.main()
