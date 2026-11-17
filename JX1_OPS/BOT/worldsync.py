"""Tách record GS, profile Windows LE/pack1 của source server; không đoán ABI.

ID theo C/KProtocolDef.h; chọn fixed/-1 theo C/KProtocol.cpp (CP).
Kích thước theo S/KProtocol.h khi khác C; dẫn nguồn đầy đủ ở báo cáo E-01b.
Mỗi payload là một frame đã giải XOR. TCP fragmentation do FrameDecoder xử lý;
record bị cắt tại cuối frame là lỗi, không nối/scan sang frame kế tiếp.
"""

import struct
from types import MappingProxyType

from .framing import ProtocolError

# Khai triển từng nhóm field, không dùng native alignment của máy chạy Python.
CURPLAYER = struct.calcsize("<BIHBBB4I7HiIBBBi2H6i")  # S:1276-1319
CUR_NORMAL = struct.calcsize("<B3qB3qiB")             # S:1261-1274
WORLD = struct.calcsize("<BiiBIi256sBiB6i")           # S:1419-1440
PLAYER = struct.calcsize("<B8IB2iB128si4B8i")         # C:28-66
PLAYER_NORMAL = struct.calcsize("<BI7iBi6B5iB4i4B5i128sI64sB")  # C:76-119
NPC_NORMAL = struct.calcsize("<BI4i4B4iB4i64s11iB3iBiBiq3i18B")  # S:323-369
# KTime=5 int, KLockItem=2 int32 (H/GameDataDef.h:472-479,491-505).
ITEM = struct.calcsize("<BI9i19iH6i5i6i516s64s3iB4i2ii")  # S:993-1038

FIXED_SIZES = MappingProxyType({
    67: 9, 68: CURPLAYER, 70: CUR_NORMAL, 73: WORLD,
    74: PLAYER, 75: PLAYER_NORMAL, 77: NPC_NORMAL, 78: 25,
    80: 6, 81: 6, 82: 6, 83: 13, 84: 9, 85: 13, 86: 13,
    89: 13, 90: 265, 91: 17, 92: 69, 93: 6, 94: 6, 95: 2, 96: 37,
    118: ITEM, 119: 21, 120: 13, 121: 5, 122: 37,
    143: 5, 144: 69, 145: 25, 147: 37, 150: 1,
    154: 9, 155: 69, 158: 37, 159: 1, 160: 2, 174: 5, 177: 1,
    188: 1, 189: 1, 192: ITEM, 197: 1,
    203: 9, 204: 13, 206: 25, 207: 5, 210: 525, 213: 13,
})

# CP:17-173: -1 => WORD ở offset 1, tổng = 1 + WORD, theo
# C/../gamescene/KgameWorld.cpp:5142-5145. Chỉ ID có mục -1 rõ ràng;
# không áp quy tắc này cho mọi ID lạ. 195 là biến độ dài (CP:147).
VARIABLE_IDS = frozenset((
    65, 66, 69, 71, 72, 76, 79, 87, 88, 97, 112, 123,
    129, 136, 139, 141, 148, 149, 162, 163, 170, 172, 195, 215, 216,
))
# Prefix không gồm tên; server gửi strlen(name), không gửi byte NUL.
VARIABLE_BOUNDS = MappingProxyType({69: (3, 643), 76: (42, 106), 79: (62, 142)})


def split_records(payload):
    """Kiểm toàn bộ frame trước khi trả list; lỗi đuôi không được ACK đầu frame."""
    if not payload:
        raise ProtocolError("Payload GS rỗng")
    result, offset = [], 0
    while offset < len(payload):
        protocol = payload[offset]
        remaining = len(payload) - offset
        if protocol in VARIABLE_IDS:
            if remaining < 3:
                raise ProtocolError("Header độ dài GS bị cắt")
            size = 1 + struct.unpack_from("<H", payload, offset + 1)[0]
            minimum, maximum = VARIABLE_BOUNDS.get(protocol, (3, 65533))
            if not minimum <= size <= maximum:
                raise ProtocolError("Độ dài record GS không hợp lệ: ID=" + str(protocol))
            if protocol == 69 and (size - 3) % 8:
                raise ProtocolError("Danh sách skill không chia hết record 8 byte")
        else:
            size = FIXED_SIZES.get(protocol)
            if not size:
                raise ProtocolError("Gói GS chưa hỗ trợ: ID=" + str(protocol) +
                                    "; xem E-01b-thieu-giao-thuc.md")
        if size > remaining:
            raise ProtocolError("Record GS bị cắt/layout chưa hỗ trợ: ID=" + str(protocol))
        result.append(payload[offset:offset + size])
        offset += size
    return result
