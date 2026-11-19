"""Vector E-08 chép nguyên byte; chỉ dữ liệu tổng hợp, không kết nối mạng."""

import struct
import unittest

# test_bot nạp package cạnh file để unittest discover hoạt động với python -I.
import test_bot  # noqa: F401
from jx1bot.behavior import Hunt, attack_target, decode_record
from jx1bot.framing import ProtocolError

SKILLS = bytes.fromhex("45 0A 00 07 00 02 01 D2 04 00 00")
SPAWN = bytes.fromhex("""
4C 2C 00 00 00 00 00 00 00 00 01 00
E8 03 00 00 D0 07 00 00 78 56 34 12 0A 00 14 00
00 00 00 00 00 00 00 00 00 00 E8 03 00 00 4D 6F 62
""")
NORMAL = bytes.fromhex("""
4D 78 56 34 12 E8 03 00 00 D0 07 00 00 00 00 00
00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 EE 02
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 90 01 00
00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00
""")
HURT = bytes.fromhex("5B 78 56 34 12 06 00 00 00 E8 03 00 00 D0 07 00 00")
DEATH = bytes.fromhex("""
5C 78 56 34 12 4D 6F 62 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00
""")
ATTACK = bytes.fromhex("4D 07 00 00 00 FF FF FF FF 78 56 34 12")
TARGET = 0x12345678


def spawn(npc_id, x=1000, y=2000, kind=0):
    data = bytearray(SPAWN)
    struct.pack_into("<iiI", data, 12, x, y, npc_id)
    data[11] = kind
    return bytes(data)


class BehaviorTests(unittest.TestCase):
    def hunt(self):
        return Hunt(("offline-session", 1, 1), search_range=500,
                    attack_range=20, action_interval=1)

    def step(self, hunt, now=0, x=1000, y=2000, ids=(TARGET,), skill_id=7):
        return hunt.step(x=x, y=y, map_id=1, now=now, skill_id=skill_id, eligible_ids=ids)

    def test_exact_e08_decode_vectors(self):
        self.assertEqual(tuple(map(len, (SKILLS, SPAWN, NORMAL, HURT, DEATH, ATTACK))),
                         (11, 45, 227, 17, 69, 13))
        skill, = decode_record(SKILLS)
        self.assertEqual((skill.skill_id, skill.level, skill.add, skill.experience), (7, 2, 1, 1234))
        npc = decode_record(SPAWN)
        self.assertEqual((npc.npc_id, npc.x, npc.y, npc.kind, npc.name, npc.level, npc.template),
                         (TARGET, 1000, 2000, 0, b"Mob", 10, 20))
        npc = decode_record(NORMAL)
        self.assertEqual((npc.npc_id, npc.life_ratio, npc.max_life, npc.estimated_life),
                         (TARGET, 750, 400, 300))
        self.assertIsNone(npc.kind)
        self.assertEqual(decode_record(HURT), (TARGET, 6, 1000, 2000))
        self.assertEqual(decode_record(DEATH), (TARGET, b"Mob"))
        self.assertEqual(attack_target(7, TARGET), ATTACK)

    def test_uint_id_and_attack_signed_handler_limit(self):
        self.assertEqual(decode_record(spawn(0xFFFFFFFF)).npc_id, 0xFFFFFFFF)
        self.assertEqual(attack_target(7, 0x7FFFFFFF)[9:], b"\xff\xff\xff\x7f")
        for npc_id in (-1, 0x80000000, 0xFFFFFFFF, 2**32, True):
            with self.subTest(npc_id=npc_id), self.assertRaises(ProtocolError):
                attack_target(7, npc_id)

    def test_truncation_extra_record_and_cocos_rejected(self):
        for record in (SKILLS, SPAWN, NORMAL, HURT, DEATH):
            for cut in range(len(record)):
                if cut == 223 and record[0] == 77:
                    continue  # layout Cocos 223 của exe thật được chấp nhận (tọa độ thôi)
                with self.subTest(protocol=record[0], cut=cut), self.assertRaises(ProtocolError):
                    decode_record(record[:cut])
        for record in (NORMAL[:222], SPAWN + HURT, DEATH + b"\0"):
            with self.assertRaises(ProtocolError):
                decode_record(record)

    def test_spawn_lengths_and_skill_boundaries(self):
        for count in (0, 64):
            record = bytearray(SPAWN[:42] + b"N" * count)
            struct.pack_into("<H", record, 1, len(record) - 1)
            self.assertEqual(decode_record(bytes(record)).name, b"N" * count)
        for count in (0, 80):
            record = struct.pack("<BH", 69, 2 + 8 * count) + SKILLS[3:] * count
            self.assertEqual(len(decode_record(record)), count)
        for record in (b"\x45\x03\0\0", struct.pack("<BH", 69, 650) + bytes(648),
                       struct.pack("<BH", 76, 106) + bytes(104)):
            with self.assertRaises(ProtocolError):
                decode_record(record)

    def test_merge_hurt_and_death_not_kill_credit(self):
        hunt = self.hunt()
        hunt.feed(SKILLS + SPAWN + NORMAL)
        self.assertEqual(hunt.npcs[TARGET].name, b"Mob")
        self.assertEqual(self.step(hunt).payload, ATTACK)
        hunt.feed(HURT)
        self.assertEqual(hunt.npcs[TARGET].hurt_frames, 6)
        self.assertEqual(hunt.npcs[TARGET].estimated_life, 300)
        self.assertFalse(hunt.npcs[TARGET].dead)
        hunt.feed(DEATH + DEATH + NORMAL + SPAWN + HURT)
        self.assertTrue(hunt.npcs[TARGET].dead)
        self.assertEqual(hunt.npcs[TARGET].estimated_life, 0)
        self.assertEqual(hunt.target_deaths, {TARGET})
        self.assertEqual(hunt.bot_kill_credit, "[CHƯA KIỂM]")
        self.assertIsNone(self.step(hunt, now=1))

    def test_death_without_hurt_or_known_npc_and_name_tail(self):
        hunt = self.hunt()
        data = DEATH[:9] + b"Z" * 60
        hunt.feed(data + SPAWN)
        self.assertTrue(hunt.npcs[TARGET].dead)
        self.assertEqual(hunt.npcs[TARGET].name, b"Mob")
        self.assertEqual(hunt.target_deaths, set())

    def test_zero_ratio_and_doing_do_not_confirm_death(self):
        hunt = self.hunt()
        hunt.feed(SKILLS + SPAWN)
        data = bytearray(NORMAL)
        struct.pack_into("<i", data, 126, 0)
        hunt.feed(bytes(data))
        self.assertFalse(hunt.npcs[TARGET].dead)
        self.assertEqual(self.step(hunt).kind, "attack")
        for doing in (10, 21):
            data[23] = doing
            hunt.feed(bytes(data))
            self.assertFalse(hunt.npcs[TARGET].dead)
            self.assertEqual(hunt.target_deaths, set())

    def test_nearest_move_wait_attack_repeat_then_next_target(self):
        hunt = self.hunt()
        hunt.feed(SKILLS + SPAWN + spawn(TARGET + 1, x=1100))
        ids = (TARGET, TARGET + 1)
        first = self.step(hunt, x=900, ids=ids)
        self.assertEqual((first.kind, first.target_id), ("run", TARGET))
        self.assertEqual(first.payload.hex(), "4ce8030000d007000001000000")
        self.assertIsNone(self.step(hunt, now=0.5, ids=ids))
        # Không tự dịch chuyển vị trí sau RUN.
        self.assertEqual(self.step(hunt, now=1, x=900, ids=ids).kind, "run")
        self.assertEqual(self.step(hunt, now=2, ids=ids).payload, ATTACK)
        self.assertEqual(self.step(hunt, now=3, ids=ids).payload, ATTACK)
        hunt.feed(DEATH)
        following = self.step(hunt, now=4, ids=ids)
        self.assertEqual((following.kind, following.target_id), ("run", TARGET + 1))

    def test_candidate_guards_and_tie_break(self):
        hunt = self.hunt()
        hunt.feed(SKILLS + NORMAL)
        self.assertIsNone(self.step(hunt))  # Không tin nKind chưa được sender gán.
        hunt.feed(spawn(1, x=1001) + spawn(2, x=999) + spawn(3, kind=1) +
                  spawn(4, x=1501) + spawn(0xFFFFFFFF))
        self.assertEqual(self.step(hunt, ids=(2, 1)).target_id, 1)
        self.assertIsNone(self.step(hunt, now=1, ids=(3, 4, 0xFFFFFFFF)))
        self.assertIsNone(hunt.target_id)
        self.assertIsNone(self.step(hunt, now=2, ids=()))
        self.assertEqual(self.step(hunt, now=3, x=501, ids=(1,)).kind, "run")  # Đúng biên 500.

    def test_skill_missing_zero_level_and_empty_refresh_block_actions(self):
        hunt = self.hunt()
        hunt.feed(SPAWN)
        self.assertIsNone(self.step(hunt))
        zero = bytearray(SKILLS)
        zero[5] = 0
        hunt.feed(bytes(zero))
        self.assertIsNone(self.step(hunt, now=1))
        hunt.feed(SKILLS)
        self.assertIsNone(self.step(hunt, now=2, skill_id=8))
        self.assertEqual(self.step(hunt, now=3).payload, ATTACK)
        hunt.feed(b"\x45\x02\0")
        self.assertIsNone(self.step(hunt, now=4))

    def test_frame_atomicity_and_context_reset(self):
        hunt = self.hunt()
        for bad in (SPAWN + b"\xff", SPAWN + HURT[:-1]):
            with self.assertRaises(ProtocolError):
                hunt.feed(bad)
            self.assertEqual(hunt.npcs, {})
        hunt.feed(SKILLS + SPAWN)
        self.step(hunt)
        hunt.feed(DEATH)
        hunt.reset_context(("new-session", 2, 2))
        self.assertEqual((hunt.npcs, hunt.skills, hunt.target_deaths), ({}, {}, set()))
        hunt.feed(SPAWN)
        self.assertFalse(hunt.npcs[TARGET].dead)
        self.assertIsNone(self.step(hunt))

    def test_config_clock_and_heal_guards(self):
        for options in ({"search_range": -1}, {"attack_range": 501},
                        {"action_interval": 0}, {"search_range": float("nan")}):
            args = dict(search_range=500, attack_range=20, action_interval=1)
            args.update(options)
            with self.assertRaises(ProtocolError):
                Hunt("offline", **args)
        hunt = self.hunt()
        self.step(hunt, now=2)
        for now in (1, -1, True, float("inf"), float("nan")):
            with self.assertRaises(ProtocolError):
                self.step(hunt, now=now)
        with self.assertRaisesRegex(ProtocolError, r"\[CHƯA KIỂM\] TODO"):
            hunt.heal()
