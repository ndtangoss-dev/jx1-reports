"""Vector tổng hợp từ khai báo nguồn; không socket thật, không capture."""

import struct
import unittest

from test_bot import (ACCOUNT, PASSWORD, ROLE_NAME, CLIENT_KEY, GUID,
                      channel_for, sent_messages, response, roles, permit)
from jx1bot import worldsync
from jx1bot.framing import ProtocolError
from jx1bot.session import Session, State

END = bytes.fromhex("430100000004030201")
PING = bytes.fromhex("8f04030201")


def variable(protocol, body):
    return struct.pack("<BH", protocol, len(body) + 2) + body


def sync_vectors():
    # Độ dài đếm riêng từ S/KProtocol.h, không lấy từ bảng đang được test.
    # Byte 67/143 được đặt trong body để bắt lỗi scan marker.
    return [
        b"\x49" + bytes(303),                      # WORLD_SYNC 304
        variable(76, bytes(39) + b"NPC\x43\x8f"),  # prefix 42 + tên
        b"\x4e" + bytes(24),                       # NPC player min 25
        b"\x4a" + bytes(210),                      # PLAYER_SYNC 211
        b"\x44" + bytes(82),                       # CURPLAYER_SYNC 83
        variable(69, struct.pack("<HBBi", 7, 1, 0, 0)),
        b"\x46" + bytes(54),                       # GS normal 55 (C:31)
        b"\x4b" + bytes(301),                      # PLAYER_NORMAL 302
        b"\x4d" + bytes(226),                      # GS NPC normal 227 (C:223)
        variable(79, bytes(59) + b"item\x43\x8f"), # OBJ prefix 62
        b"\x76" + bytes(807),                      # ITEM_SYNC 808
        b"\x77" + bytes(20),                       # ITEM_REMOVE 21
        variable(148, b"\x43\x8f"),               # CP -1, WORD không gồm ID
    ]


def session_for(payloads, step=65536):
    gateway = channel_for([response(), roles(), permit()])
    game = channel_for(payloads, step)
    def connect(host, port, timeout):
        return gateway if port == 56722 else game
    return Session(connector=connect), game


def login(session):
    session.login(ACCOUNT, PASSWORD, ROLE_NAME.decode(), 1, 0, CLIENT_KEY, 0)


class WorldSyncTests(unittest.TestCase):
    def test_source_layout_vectors_and_concatenation(self):
        vectors = sync_vectors() + [END, PING]
        self.assertEqual(worldsync.split_records(b"".join(vectors)), vectors)

    def test_each_truncated_fixed_record_rejected(self):
        for protocol, length in worldsync.FIXED_SIZES.items():
            for cut in range(1, length):
                with self.subTest(protocol=protocol, cut=cut), self.assertRaises(ProtocolError):
                    worldsync.split_records(bytes([protocol]) + bytes(cut - 1))

    def test_variable_header_short_zero_one_and_truncated_body(self):
        for data in (b"\x45", b"\x45\x02", b"\x45\0\0", b"\x45\1\0",
                     b"\x45\x0a\0" + bytes(7), b"\x4c\2\0", b"\x4f\2\0"):
            with self.subTest(data=data), self.assertRaises(ProtocolError):
                worldsync.split_records(data)

    def test_skill_count_alignment_and_empty_list(self):
        self.assertEqual(worldsync.split_records(b"\x45\2\0"), [b"\x45\2\0"])
        maximum = variable(69, bytes(80 * 8))
        self.assertEqual(worldsync.split_records(maximum), [maximum])
        for body in (bytes(1), bytes(7), bytes(81 * 8)):
            with self.assertRaises(ProtocolError):
                worldsync.split_records(variable(69, body))

    def test_variable_boundaries_and_no_marker_scanning(self):
        for protocol, prefix, capacity in ((76, 42, 64), (79, 62, 80)):
            for namesize in (0, capacity):
                record = variable(protocol, bytes(prefix - 3) + bytes(namesize))
                self.assertEqual(worldsync.split_records(record + END), [record, END])
            with self.assertRaises(ProtocolError):
                worldsync.split_records(variable(protocol, bytes(prefix - 3 + capacity + 1)))
        record = variable(148, END + PING)
        self.assertEqual(worldsync.split_records(record), [record])

    def test_unknown_and_empty_rejected(self):
        for data in (b"", b"\xff" + END, b"\x40\x02\0" + END, b"\xdc\x02\0"):
            with self.assertRaises(ProtocolError):
                worldsync.split_records(data)

    def test_whole_frame_validated_before_return(self):
        for suffix in (b"\xff", b"\x45\0\0", b"\x8f\x43"):
            with self.assertRaises(ProtocolError):
                worldsync.split_records(END + suffix)

    def test_stream_through_end_and_tcp_fragmentation(self):
        for step in (1, 7, 65536):
            for bundled in (False, True):
                records = sync_vectors() + [END]
                session, game = session_for([b"".join(records)] if bundled else records, step)
                login(session)
                self.assertEqual(session.state, State.IN_GAME)
                self.assertEqual(sent_messages(game), [b"\x42" + GUID, END, b"\x7c\1\0\0\0"])
                session.close()

    def test_no_ack_before_end_and_world_records_after_login(self):
        session, game = session_for([b"".join(sync_vectors()), END, b"".join(sync_vectors())])
        session.game, session.client_key, session.state = game, CLIENT_KEY, State.SYNCING
        session.poll()
        self.assertEqual(session.state, State.SYNCING)
        self.assertEqual(sent_messages(game), [])
        session.poll()
        session.poll()
        self.assertEqual(session.state, State.IN_GAME)
        self.assertEqual(sent_messages(game), [END, b"\x7c\1\0\0\0"])
        session.close()

    def test_bad_tail_key_duplicate_or_one_byte_end_closes_without_ack(self):
        for payload in (END + b"\xff", END + b"\x45\x01\0", END + END,
                        END[:-1], b"\x43", END[:5] + bytes(4)):
            session, game = session_for([payload])
            with self.subTest(payload=payload), self.assertRaises(ProtocolError):
                login(session)
            self.assertEqual(session.state, State.CLOSED)
            self.assertTrue(game.sock.closed)
            self.assertEqual(sent_messages(game), [b"\x42" + GUID])

    def test_record_cannot_continue_in_next_frame(self):
        world = sync_vectors()[0]
        session, game = session_for([world[:20], world[20:] + END])
        with self.assertRaises(ProtocolError):
            login(session)
        self.assertTrue(game.sock.closed)
        self.assertEqual(sent_messages(game), [b"\x42" + GUID])

    def test_end_replay_after_login_closes_without_second_ack(self):
        session, game = session_for([END, END])
        login(session)
        with self.assertRaises(ProtocolError):
            session.poll()
        self.assertEqual(session.state, State.CLOSED)
        self.assertEqual(sent_messages(game), [b"\x42" + GUID, END, b"\x7c\1\0\0\0"])
