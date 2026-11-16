"""Tập con ID sinh từ bảng A-06; layout đối chiếu source trong báo cáo E-01.

Profile rõ ràng: Windows little-endian, uint/int/BOOL 4 byte, bool 1,
NAME_LENGHT=64, ACC_LENGTH=32, password=64, #pragma pack(1).
Chưa xác minh profile này với binary trong JX-Test-36.
"""

import hashlib
import hmac
import ipaddress
import struct
from dataclasses import dataclass
from enum import IntEnum

from .framing import ProtocolError


class C2S(IntEnum):
    LOGIN = 65
    LOGIC_LOGIN = 66
    SYNC_END = 67
    RUN = 76
    SKILL = 77
    SELECT_ROLE = 108
    PING = 122
    CP_LOCK = 124
    SIT = 130


class S2C(IntEnum):
    PERMIT_LOGIN = 52
    ROLE_LIST = 55
    LOGIN = 65
    SYNC_END = 67
    PING = 143


LOGIN = struct.Struct("<BHiI32s64sIII16sIII")
ROLE_HEADER = struct.Struct("<BIIBI")  # pDataBuffer offset 14; sizeof có [1] =15
ROLE = struct.Struct("<64sBBB")
PERMIT = struct.Struct("<B16s64s32s64sB4sH")
SYNC = struct.Struct("<BiI")
PING = struct.Struct("<BI")
ACTION = struct.Struct("<Biii")
LOGIN_ACTION = 0x050000
ACTION_FILTER = 0xFF0000
PROTOCOL_VERSION = 1


def uint32(value, field):
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 0xFFFFFFFF:
        raise ProtocolError(field + " phải là uint32")
    return value


def int32(value, field):
    if isinstance(value, bool) or not isinstance(value, int) or not -2147483648 <= value <= 2147483647:
        raise ProtocolError(field + " phải là int32")
    return value


def cstring(value, size, field, encoding="ascii"):
    if not isinstance(value, str) or not value or "\0" in value:
        raise ProtocolError(field + " rỗng hoặc chứa NUL")
    try:
        data = value.encode(encoding, errors="strict")
    except (LookupError, UnicodeError):
        raise ProtocolError("Không mã hóa được " + field) from None
    if len(data) >= size:
        raise ProtocolError(field + " vượt độ dài byte")
    return data.ljust(size, b"\0")


def _text(data):
    if b"\0" not in data:
        raise ProtocolError("Chuỗi wire thiếu NUL")
    return data.split(b"\0", 1)[0]


def password_md5(password, encoding="ascii"):
    data = cstring(password, 17, "password", encoding).split(b"\0", 1)[0]
    return hashlib.md5(data, usedforsecurity=False).hexdigest().upper().encode("ascii")


def login(account, password, region, enter_map, encoding="ascii"):
    # Klogin.cpp:479-489; Bishop/GamePlayer.cpp:826-856 đọc các trường này.
    acc = cstring(account, 17, "account", encoding).ljust(32, b"\0")
    digest = password_md5(password, encoding).ljust(64, b"\0")
    uint32(region, "region")
    if region == 0:
        raise ProtocolError("region phải >0, không tự đoán cấu hình VM")
    uint32(enter_map, "enter_map")
    return LOGIN.pack(C2S.LOGIN, LOGIN.size - 1, LOGIN_ACTION, 0, acc,
                      digest, 0, 0, 0, b"\0" * 16, region, enter_map, PROTOCOL_VERSION)


def check_login_response(payload, request):
    if len(payload) != LOGIN.size or len(request) != LOGIN.size:
        raise ProtocolError("Layout KLoginAccountInfo không khớp profile")
    p, size, param, _, acc, digest, *tail = LOGIN.unpack(payload)
    expected = LOGIN.unpack(request)
    if p != S2C.LOGIN or size != LOGIN.size - 1 or param & ACTION_FILTER != LOGIN_ACTION:
        raise ProtocolError("Header phản hồi đăng nhập không hợp lệ")
    if not hmac.compare_digest(_text(acc), _text(expected[4])) or not hmac.compare_digest(_text(digest), _text(expected[5])):
        raise ProtocolError("Phản hồi không thuộc yêu cầu đăng nhập này")
    result = param & ~ACTION_FILTER
    if result != 1:
        raise ProtocolError("Bishop từ chối đăng nhập, mã " + str(result))
    if tail[-1] != PROTOCOL_VERSION:
        raise ProtocolError("ProtocolVersion phản hồi không khớp")


@dataclass(frozen=True)
class Role:
    name: bytes
    sex: int
    series: int
    level: int


def role_list(payload):
    # KProtocol.h:1819-1826; Klogin.cpp:1033-1065.
    if len(payload) < ROLE_HEADER.size + 1 or payload[0] != S2C.ROLE_LIST:
        raise ProtocolError("Danh sách nhân vật bị cắt hoặc sai ID")
    count = payload[ROLE_HEADER.size]
    # Trường nDataLen có biến thể đóng gói: chưa dùng để đoán ranh giới.
    if len(payload) != ROLE_HEADER.size + 1 + count * ROLE.size:
        raise ProtocolError("Role list gộp/đệm hoặc layout chưa hỗ trợ")
    result = []
    for i in range(count):
        name, sex, series, level = ROLE.unpack_from(payload, ROLE_HEADER.size + 1 + i * ROLE.size)
        name = _text(name)
        if not name:
            raise ProtocolError("Tên nhân vật rỗng")
        result.append(Role(name, sex, series, level))
    return result


def select_role(name):
    if not isinstance(name, bytes) or not 1 <= len(name) <= 63 or b"\0" in name:
        raise ProtocolError("Tên nhân vật phải dài 1..63 byte và không chứa NUL")
    return bytes([C2S.SELECT_ROLE]) + name.ljust(64, b"\0")


@dataclass(frozen=True, repr=False)
class Permit:
    guid: bytes
    host: str
    port: int


def permit_login(payload, account, role, encoding="ascii"):
    if len(payload) != PERMIT.size:
        raise ProtocolError("Layout tagNotifyPlayerLogin chưa hỗ trợ")
    p, guid, name, acc, _, allowed, address, port = PERMIT.unpack(payload)
    if p != S2C.PERMIT_LOGIN or allowed != 1 or port == 0 or guid == b"\0" * 16:
        raise ProtocolError("Bishop không cấp phép vào game hợp lệ")
    expected = cstring(account, 32, "account", encoding).split(b"\0", 1)[0]
    if _text(name) != role or _text(acc) != expected:
        raise ProtocolError("Permit không thuộc nhân vật/tài khoản đã chọn")
    return Permit(guid, str(ipaddress.IPv4Address(address)), port)


def logic_login(guid):
    if not isinstance(guid, bytes) or len(guid) != 16 or guid == b"\0" * 16:
        raise ProtocolError("GUID phải là 16 byte khác zero")
    return bytes([C2S.LOGIC_LOGIN]) + guid


def sync_reply(payload, expected_key):
    uint32(expected_key, "client_key")
    if len(payload) != SYNC.size:
        raise ProtocolError("CLIENT_SYNC_END phải dài 9 byte theo profile Cocos")
    p, allowed, key = SYNC.unpack(payload)
    if p != S2C.SYNC_END or allowed != 1 or key != expected_key:
        raise ProtocolError("CLIENT_SYNC_END từ chối hoặc khóa client không khớp")
    return SYNC.pack(C2S.SYNC_END, allowed, expected_key)


def run(x, y, map_id):
    for name, v in (("x", x), ("y", y), ("map_id", map_id)):
        int32(v, name)
        if v < 0:
            raise ProtocolError(name + " không được âm")
    return ACTION.pack(C2S.RUN, x, y, map_id)


def skill(skill_id, x, y):
    for name, v in (("skill_id", skill_id), ("x", x), ("y", y)):
        int32(v, name)
    if skill_id <= 0 or x < -1 or y < 0:
        raise ProtocolError("Skill cần id>0, x>=-1, y>=0; x=-1 dùng NPC ID")
    return ACTION.pack(C2S.SKILL, skill_id, x, y)


def sit(enabled):
    if not isinstance(enabled, bool):
        raise ProtocolError("sit yêu cầu bool")
    return bytes([C2S.SIT, int(enabled)])


def ping_reply(payload, now_ms):
    if len(payload) != PING.size or payload[0] != S2C.PING:
        raise ProtocolError("PING_COMMAND không hợp lệ")
    uint32(now_ms, "now_ms")
    _, server_time = PING.unpack(payload)
    return struct.pack("<BII", C2S.PING, server_time, now_ms)


def game_messages(payload):
    """Chỉ tách record đã biết; không quét byte 0x43/0x8F bên trong dữ liệu."""
    offset = 0
    result = []
    sizes = {S2C.SYNC_END: SYNC.size, S2C.PING: PING.size}
    while offset < len(payload):
        protocol = payload[offset]
        size = sizes.get(protocol)
        if size is None:
            raise ProtocolError("Gói GS chưa hỗ trợ: ID=" + str(protocol) +
                                "; xem E-01-thieu-giao-thuc.md")
        if offset + size > len(payload):
            raise ProtocolError("Record GS bị cắt")
        result.append(payload[offset:offset + size])
        offset += size
    return result
