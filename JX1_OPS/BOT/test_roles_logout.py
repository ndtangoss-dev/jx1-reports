"""Vector plaintext tổng hợp E-07; socket giả, không mạng/VM/DB."""

import struct
import unittest
from unittest.mock import patch

import test_bot  # nạp package cạnh file khi chạy python -I unittest discover
from jx1bot import packets
from jx1bot.framing import ProtocolError, pack_frame
from jx1bot.session import Channel, Session, State


CREATE = bytes.fromhex(
    "45 0B 00 00 00 00 00 00 00 00 01 00 00 00 00 00 35 00 42 6F 74 41 62 63 00")
CREATE_OK = b"\x9d" + bytes(64) + b"\x01"
CREATE_FAIL = b"\x9d" + bytes(65)
EMPTY_LIST = bytes.fromhex("37 01 00 00 00 01 00 00 00 00 00 00 00 00 00")
ONE_ROLE = (bytes.fromhex("37 44 00 00 00 01 00 00 00 00 00 00 00 00 01")
            + b"BotAbc" + bytes(58) + b"\x00\x00\x01")


class RoleVectorsTests(unittest.TestCase):
    def test_create_exact_e07_vector_and_frame(self):
        payload = packets.new_player(b"BotAbc", 0, 0, 53, 1)
        self.assertEqual(payload, CREATE)
        self.assertEqual(len(payload), 25)
        self.assertEqual(pack_frame(payload), b"\x1b\x00" + CREATE)

    def test_create_wire_widths_name_boundaries_and_explicit_bytes(self):
        for name in (b"B" * 6, b"B" * 16, b"\x80" * 6):
            payload = packets.new_player(name, 255, 255, 65535, 0xffffffff)
            self.assertEqual(len(payload), 19 + len(name))
            self.assertEqual(struct.unpack_from("<I", payload, 1)[0], 5 + len(name))
            self.assertEqual(payload[9], 0)  # chuẩn hóa, không phải capture client
            self.assertEqual(payload[14:18], b"\xff" * 4)
            self.assertEqual(payload[18:], name + b"\0")

    def test_create_rejects_bad_input_before_packing(self):
        for name in (b"", b"B" * 5, b"B" * 17, b"Bot\0Abc", "BotAbc", bytearray(b"BotAbc")):
            with self.subTest(name=name), self.assertRaises(ProtocolError):
                packets.new_player(name, 0, 0, 53, 1)
        for field, values in (("gender", (-1, 256, True, 1.5)),
                              ("series", (-1, 256, False)),
                              ("native_place", (-1, 65536, True)),
                              ("region", (0, -1, 2**32, True))):
            for value in values:
                args = dict(name=b"BotAbc", gender=0, series=0, native_place=53, region=1)
                args[field] = value
                with self.subTest(field=field, value=value), self.assertRaises(ProtocolError):
                    packets.new_player(**args)

    def test_response_exact_e07_vectors_and_ignored_name(self):
        self.assertIs(packets.new_player_response(CREATE_OK), True)
        self.assertIs(packets.new_player_response(CREATE_FAIL), False)
        # Sender chỉ gán tên[0]=NUL; không diễn giải/so sánh 63 byte rác.
        self.assertIs(packets.new_player_response(b"\x9d\0" + b"\xff" * 63 + b"\x01"), True)
        self.assertEqual(pack_frame(CREATE_OK)[:2], b"\x44\x00")

    def test_response_rejects_truncation_coalescing_id_and_invalid_bool(self):
        bad = [CREATE_OK[:i] for i in range(66)]
        bad += [CREATE_OK + b"\0", CREATE_OK * 2, b"\x38" + CREATE_OK[1:]]
        bad += [CREATE_OK[:-1] + bytes([value]) for value in (2, 255)]
        for payload in bad:
            with self.subTest(length=len(payload)), self.assertRaises(ProtocolError):
                packets.new_player_response(payload)

    def test_role_lists_exact_e07_and_multiple_roles(self):
        self.assertEqual(packets.role_list(EMPTY_LIST), [])
        self.assertEqual(packets.role_list(ONE_ROLE), [packets.Role(b"BotAbc", 0, 0, 1)])
        self.assertEqual(len(ONE_ROLE), 82)
        self.assertEqual(pack_frame(ONE_ROLE)[:2], b"\x54\x00")
        second = b"OtherBot".ljust(64, b"\0") + b"\x01\x04\xff"
        payload = (packets.ROLE_HEADER.pack(55, 135, 1, 1, 99)
                   + b"\x02" + ONE_ROLE[15:] + second)
        self.assertEqual(packets.role_list(payload)[1], packets.Role(b"OtherBot", 1, 4, 255))

    def test_role_list_rejects_bad_length_count_name_and_dword_level(self):
        bad = [ONE_ROLE[:i] for i in range(len(ONE_ROLE))]
        bad += [ONE_ROLE + b"\0", ONE_ROLE + bytes(3), b"\x38" + ONE_ROLE[1:]]
        for offset, value in ((1, 67), (1, 791030), (14, 0), (14, 2)):
            payload = bytearray(ONE_ROLE)
            if offset == 1:
                struct.pack_into("<I", payload, offset, value)
            else:
                payload[offset] = value
            bad.append(bytes(payload))
        bad += [ONE_ROLE[:15] + b"B" * 64 + ONE_ROLE[-3:],
                ONE_ROLE[:15] + bytes(64) + ONE_ROLE[-3:]]
        for payload in bad:
            with self.subTest(length=len(payload)), self.assertRaises(ProtocolError):
                packets.role_list(payload)


class LogoutTests(unittest.TestCase):
    def setUp(self):
        self.network = patch("socket.create_connection", side_effect=AssertionError("Không được mở mạng"))
        self.network.start()
        self.addCleanup(self.network.stop)

    def test_logout_all_states_game_then_gateway_and_no_application_bytes(self):
        for state in State:
            events = []
            session = Session()
            session.state = state
            game = Channel(test_bot.MemorySocket(b""))
            gateway = Channel(test_bot.MemorySocket(b""))
            session.game, session.gateway = game, gateway
            def closed_game():
                self.assertEqual(session.state, State.CLOSED)
                with self.assertRaises(ProtocolError):
                    session.run(1, 2, 3)
                events.append("game")
            game.sock.close = closed_game
            gateway.sock.close = lambda: events.append("gateway")
            session.logout()
            session.close()
            self.assertEqual(events, ["game", "gateway"])
            self.assertEqual((game.sock.sent, gateway.sock.sent), (b"", b""))  # E-07 ε
            self.assertEqual((session.game, session.gateway, session.client_key), (None, None, None))
            self.assertEqual(session.next_action, 0)

    def test_logout_partial_sessions_and_no_resources(self):
        for field in (None, "game", "gateway"):
            session = Session()
            if field:
                channel = Channel(test_bot.MemorySocket(b""))
                setattr(session, field, channel)
            session.logout()
            self.assertEqual(session.state, State.CLOSED)
            if field:
                self.assertTrue(channel.sock.closed)

    def test_close_failure_still_closes_other_socket_and_clears_resources(self):
        events = []
        session = Session()
        session.game = Channel(test_bot.MemorySocket(b""))
        session.gateway = Channel(test_bot.MemorySocket(b""))
        game, gateway = session.game, session.gateway
        def fail():
            events.append("game")
            raise OSError("synthetic close failure")
        game.sock.close = fail
        gateway.sock.close = lambda: events.append("gateway")
        with self.assertRaisesRegex(OSError, "synthetic close failure"):
            session.logout()
        self.assertEqual(events, ["game", "gateway"])
        self.assertTrue(game.closed and gateway.closed)
        self.assertEqual((session.state, session.game, session.gateway), (State.CLOSED, None, None))
        session.logout()

    def test_channel_discards_pending_partial_frame_and_blocks_io_after_close(self):
        channel = Channel(test_bot.MemorySocket(b""))
        channel.pending.append(CREATE_OK)
        channel.decoder.feed(b"\x44")  # EOF giữa frame bị bỏ khi chủ động thoát
        channel.rx = channel.tx = object()
        channel.close()
        self.assertEqual((list(channel.pending), channel.decoder.buffer), ([], b""))
        self.assertEqual((channel.rx, channel.tx), (None, None))
        with patch.object(channel.sock, "recv") as recv, patch.object(channel.sock, "sendall") as send:
            for call in (channel.receive, channel.handshake, lambda: channel.send(CREATE)):
                with self.assertRaisesRegex(ProtocolError, "đã đóng"):
                    call()
            recv.assert_not_called()
            send.assert_not_called()


if __name__ == "__main__":
    unittest.main()
