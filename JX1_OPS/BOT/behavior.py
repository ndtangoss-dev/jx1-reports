"""Hành vi thuần offline theo E-08; nhận plaintext, trả lệnh, không gửi mạng.

Profile GS LE/pack1 được chọn rõ ràng, ABI runtime [CHƯA KIỂM].
Encoding tên, quan hệ thù địch, tầm/cooldown runtime [CHƯA KIỂM].
"""

from dataclasses import dataclass, replace
import math
import struct

from . import packets
from .framing import ProtocolError
from .worldsync import split_records


@dataclass(frozen=True)
class Skill:
    skill_id: int
    level: int
    add: int
    experience: int


@dataclass(frozen=True)
class Npc:
    npc_id: int
    x: int = 0
    y: int = 0
    kind: object = None  # 77 nKind chưa thấy sender gán; cần 76 để phân loại.
    name: bytes = b""
    camp: object = None
    doing: object = None
    level: object = None
    template: object = None
    life_ratio: object = None
    max_life: object = None
    hurt_frames: object = None
    dead: bool = False

    @property
    def estimated_life(self):
        # Chỉ là snapshot ước lượng; không phải damage hay ACK một hit.
        if self.dead:
            return 0
        if (self.max_life is None or self.max_life < 0 or
                self.life_ratio is None or not 0 <= self.life_ratio <= 1000):
            return None
        return self.max_life * self.life_ratio // 1000


def decode_record(record):
    """Giải mã đúng một record. Không đoán/fallback sang layout Cocos 223 byte."""
    records = split_records(record)
    if len(records) != 1:
        raise ProtocolError("Decoder cần đúng một record")
    protocol = record[0]
    if protocol == 69:
        return tuple(Skill(*values) for values in struct.iter_unpack("<HBBi", record[3:]))
    if protocol == 76:
        setting = struct.unpack_from("<I", record, 24)[0]
        return Npc(
            npc_id=struct.unpack_from("<I", record, 20)[0],
            x=struct.unpack_from("<i", record, 12)[0],
            y=struct.unpack_from("<i", record, 16)[0],
            kind=record[11], name=record[42:], camp=record[4], doing=record[10],
            level=setting & 0xFFFF, template=setting >> 16,
            life_ratio=struct.unpack_from("<i", record, 38)[0])
    if protocol == 77 and len(record) < 227:
        # Layout Cocos 223 byte của exe thật: chỉ tin id và tọa độ (offset 1/5/9 trùng).
        return Npc(npc_id=struct.unpack_from("<I", record, 1)[0],
                   x=struct.unpack_from("<i", record, 5)[0],
                   y=struct.unpack_from("<i", record, 9)[0])
    if protocol == 77:
        # Bỏ các field chưa được sender khởi tạo, kể cả nLifeYu khi HP<=0.
        return Npc(
            npc_id=struct.unpack_from("<I", record, 1)[0],
            x=struct.unpack_from("<i", record, 5)[0],
            y=struct.unpack_from("<i", record, 9)[0],
            camp=record[21], doing=record[23],
            life_ratio=struct.unpack_from("<i", record, 126)[0],
            max_life=struct.unpack_from("<q", record, 189)[0])
    if protocol == 91:
        return struct.unpack_from("<Iiii", record, 1)
    if protocol == 92:
        return (struct.unpack_from("<I", record, 1)[0], record[5:69].split(b"\0", 1)[0])
    return None


def attack_target(skill_id, target_id):
    """C2S 77: X=-1, Y là wire UINT ID, không phải index nội bộ.

    Handler nguồn từ chối Y âm: không wrap ID có bit cao sang signed int.
    """
    packets.uint32(target_id, "target_id")
    return packets.skill(skill_id, -1, target_id)


@dataclass(frozen=True)
class Action:
    kind: str
    target_id: int
    payload: bytes


class Hunt:
    """Một world context, không socket/sleep/worker nền.

    step nhận vị trí đã quan sát, thời gian monotonic và allowlist NPC đã được
    bên gọi xác định là quái hợp lệ. Mỗi bước trả tối đa một lệnh; bên gọi phải
    phản ánh vị trí thật trước bước kế, không coi RUN là đã tới nơi.
    """

    healing_status = "[CHƯA KIỂM] TODO: thiếu giao thức hồi máu và điều kiện dùng"
    bot_kill_credit = "[CHƯA KIỂM]"

    def __init__(self, context, *, search_range, attack_range, action_interval):
        for value in (search_range, attack_range, action_interval):
            if (isinstance(value, bool) or not isinstance(value, (int, float)) or
                    not math.isfinite(value) or value < 0):
                raise ProtocolError("Tầm/khoảng hành động phải hữu hạn và không âm")
        if action_interval == 0 or attack_range > search_range:
            raise ProtocolError("Cần interval>0 và attack_range<=search_range")
        self.search_range = search_range
        self.attack_range = attack_range
        self.action_interval = action_interval
        self.reset_context(context)

    def reset_context(self, context):
        """Bắt buộc gọi khi đổi map/phiên/vòng đời ID; không tự suy từ 76/77."""
        if context is None:
            raise ProtocolError("Cần world context tường minh")
        self.context = context
        self.npcs = {}
        self.skills = {}
        self.target_id = None
        self.target_deaths = set()
        self.next_action = 0.0
        self.last_time = None

    def feed(self, payload):
        # Giải mã toàn frame trước khi sửa bảng, tránh áp dụng một prefix lỗi.
        events = [(record[0], decode_record(record)) for record in split_records(payload)]
        for protocol, event in events:
            if protocol == 69:
                self.skills = {s.skill_id: s for s in event}
            elif protocol in (76, 77):
                old = self.npcs.get(event.npc_id)
                if old is not None and (old.dead or (protocol == 77 and event.doing in (10, 21))):
                    continue  # Snapshot trễ không làm sống lại tombstone.
                if old is not None:
                    if protocol == 76:
                        event = replace(event, max_life=old.max_life, hurt_frames=old.hurt_frames)
                    else:
                        event = replace(event, kind=old.kind, name=old.name,
                                        level=old.level, template=old.template,
                                        hurt_frames=old.hurt_frames)
                self.npcs[event.npc_id] = event
            elif protocol == 91:
                npc_id, frames, x, y = event
                old = self.npcs.get(npc_id)
                if old is not None and not old.dead:
                    self.npcs[npc_id] = replace(old, x=x, y=y, hurt_frames=frames)
            elif protocol == 92:
                npc_id, name = event
                old = self.npcs.get(npc_id, Npc(npc_id))
                self.npcs[npc_id] = replace(old, dead=True, life_ratio=0, name=name)
                if self.target_id == npc_id:
                    self.target_deaths.add(npc_id)
                    self.target_id = None

    def step(self, *, x, y, map_id, now, skill_id, eligible_ids):
        """Chọn gần nhất trong tầm, RUN tới hoặc C2S 77; không khẳng định hit."""
        # Dùng cùng ràng buộc tọa độ/map với lệnh RUN hiện có.
        packets.run(x, y, map_id)
        packets.int32(skill_id, "skill_id")
        if (isinstance(now, bool) or not isinstance(now, (int, float)) or
                not math.isfinite(now) or now < 0 or
                (self.last_time is not None and now < self.last_time)):
            raise ProtocolError("Thời gian phải hữu hạn, không âm và không giảm")
        allowed = set(eligible_ids)
        for npc_id in allowed:
            packets.uint32(npc_id, "eligible_id")
        self.last_time = now
        candidates = []
        for npc in self.npcs.values():
            distance = (npc.x - x) ** 2 + (npc.y - y) ** 2
            if (npc.npc_id in allowed and npc.kind == 0 and not npc.dead and
                    npc.doing not in (10, 21) and 0 <= npc.npc_id <= 0x7FFFFFFF and
                    npc.x >= 0 and npc.y >= 0 and distance <= self.search_range ** 2):
                candidates.append((distance, npc.npc_id, npc))
        if not candidates:
            self.target_id = None
            return None
        distance, self.target_id, npc = min(candidates)
        skill = self.skills.get(skill_id)
        if skill is None or skill.level <= 0 or now < self.next_action:
            return None
        if distance > self.attack_range ** 2:
            action = Action("run", npc.npc_id, packets.run(npc.x, npc.y, map_id))
        else:
            action = Action("attack", npc.npc_id, attack_target(skill_id, npc.npc_id))
        self.next_action = now + self.action_interval
        return action

    def heal(self):
        # TODO: không suy hồi máu từ SIT, HP ratio hay nLifeYu.
        raise ProtocolError(self.healing_status)
