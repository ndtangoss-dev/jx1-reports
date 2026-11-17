"""B-03: ba phiên fixture, kiểm trace NPC; không phải client gs001 thật.

ID/kích thước từ BOT.worldsync/E-01b. Offset identity dưới đây chỉ là hợp
đồng fixture, CHƯA xác minh ABI gs001; không dùng để suy semantic gameplay.
RUN x=phase là bộ điều khiển fixture, không phải API đổi nhóm server thật.
"""

import socket
import struct
import time

from JX1_OPS.BOT import packets
from JX1_OPS.BOT.session import Channel
from JX1_OPS.BOT.worldsync import split_records
from .core import Scenario, SkipStep, Step

A, B, BOT = 101, 102, 201


class NpcView:
    """Tái dựng tập thấy được từ ADD(76), SYNC(77), REMOVE(84) fixture."""

    def __init__(self):
        self.visible = set()

    def apply(self, payload):
        records = split_records(payload)  # validate toàn frame trước khi đổi state
        visible, events = set(self.visible), []
        for record in records:
            protocol = record[0]
            if protocol not in (76, 77, 84):
                raise AssertionError("Trace visibility chứa ID ngoài hợp đồng fixture")
            npc = struct.unpack_from("<I", record, 3 if protocol == 76 else 1)[0]
            if protocol == 76:
                if npc in visible:
                    raise AssertionError("ADD lặp NPC đã thấy")
                visible.add(npc)
            elif protocol == 77:
                if npc not in visible:
                    raise AssertionError("SYNC NPC chưa có ADD hoặc đã REMOVE")
            else:
                if npc not in visible:
                    raise AssertionError("REMOVE NPC chưa thấy")
                visible.remove(npc)
            events.append((protocol, npc))
        self.visible = visible
        return events


class ThreeSessions:
    def __init__(self):
        self.channels = {}
        self.views = {npc: NpcView() for npc in (A, B, BOT)}

    def close(self):
        for channel in self.channels.values():
            channel.close()


def connect_visibility(context):
    if context.config.host != "127.0.0.1":
        raise ValueError("visibility chỉ cho máy chủ giả 127.0.0.1")
    group = ThreeSessions()
    context.state["visibility"] = group
    for npc in (A, B, BOT):
        channel = Channel(socket.create_connection(
            (context.config.host, context.config.port), timeout=2))
        group.channels[npc] = channel
        channel.handshake(time.monotonic() + 2)
    context.log("Ba phiên fixture: người chơi A, B và Bot; chưa login/game thật")


def phase(context, number, expected, required=(), forbidden=()):
    group = context.state["visibility"]
    traces = {}
    for npc, channel in group.channels.items():
        channel.send(packets.run(number, npc, 1))
        payload = channel.receive(time.monotonic() + 2)
        context.packet("nhận", payload)
        events = group.views[npc].apply(payload)
        if any(protocol in (76, 77) and target not in expected[npc]
               for protocol, target in events):
            raise AssertionError(f"phase={number} viewer={npc}: ADD/SYNC NPC phải ẩn")
        if group.views[npc].visible != set(expected[npc]):
            raise AssertionError(f"phase={number} viewer={npc}: tập NPC khác kỳ vọng")
        if not set(required).issubset(events) or set(forbidden).intersection(events):
            raise AssertionError(f"phase={number} viewer={npc}: thiếu/thừa sự kiện NPC")
        traces[npc] = payload
        context.log(f"phase={number} viewer={npc} events={events} visible={sorted(group.views[npc].visible)}")
    return traces


SOLO = {A: (A, BOT), B: (B, BOT), BOT: (A, B, BOT)}
OPEN = {npc: (A, B, BOT) for npc in (A, B, BOT)}


def solo_visibility(context):
    phase(context, 1, SOLO, required=((76, BOT), (77, BOT)))


def shared_bot_remove(context):
    # C2S SKILL đã có; remove chỉ chứng minh biến mất chung, chưa chứng minh kill.
    context.state["visibility"].channels[A].send(packets.skill(1, -1, BOT))
    phase(context, 2, {A: (A,), B: (B,), BOT: (A, B)}, required=((84, BOT),))


def group_visibility(context):
    phase(context, 3, OPEN, required=((76, BOT), (77, BOT)))  # MaxVisible=2
    phase(context, 4, SOLO, forbidden=((84, BOT),))  # MaxVisible=1, A/B khác nhóm con


def refresh_visibility(context):
    phase(context, 5, OPEN)  # vào lại cùng nhóm: phải ADD trước SYNC
    phase(context, 6, SOLO)  # rời nhóm: phải REMOVE, không SYNC người đã ẩn
    phase(context, 7, OPEN)  # vào lại lần nữa: bắt thiếu ADD / state cũ


def disabled_visibility(context):
    baseline = phase(context, 8, OPEN)
    disabled = phase(context, 9, OPEN)
    if baseline != disabled:
        raise AssertionError("Enabled=0 khác trace baseline gốc fixture")
    context.log("Enabled=0 bằng từng byte trace baseline fixture; ảnh/game thật [CHƯA KIỂM]")


def todo_skill_visibility(context):
    raise SkipStep("TODO tiêu chí 3 [CHƯA KIỂM]: thiếu giải mã HP/hurt/death và kết quả nhắm mục tiêu/AoE; C2S SKILL 77 đã có nhưng chưa đủ (E-07/E-08)")


def todo_invite_visibility(context):
    raise SkipStep("TODO tiêu chí 4 [CHƯA KIỂM]: thiếu request/response mời đội, giao dịch, PK và mã từ chối tương ứng; không đoán ID/layout (E-07/E-08)")


VISIBILITY = Scenario("visibility", (
    Step("connect_2p1bot", connect_visibility, "Mỗi lượt mở ba phiên fixture A/B/Bot", 8),
    Step("solo", solo_visibility, "1: A/B không thấy nhau, cùng nhận ADD/SYNC Bot"),
    Step("shared_bot_remove", shared_bot_remove, "2: A gửi SKILL; cả A/B nhận REMOVE Bot; kill thật [CHƯA KIỂM]"),
    Step("group_cap", group_visibility, "5: trace MaxVisible=2 và =1, Bot không bị tính vào trần", 5),
    Step("refresh", refresh_visibility, "6: vào/rời/vào nhóm không ghost, không thiếu ADD", 5),
    Step("disabled", disabled_visibility, "7: so byte baseline và Enabled=0 fixture", 5),
    Step("todo_skill", todo_skill_visibility, "3: TODO thiếu semantic combat"),
    Step("todo_invite", todo_invite_visibility, "4: TODO thiếu gói/mã từ chối"),
))
