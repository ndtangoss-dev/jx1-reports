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

# Bổ sung 19/11 (#216): kích thước record cố định suy từ struct client bản A (pack 1),
# chỉ cho ID chưa có trong FIXED_SIZES; đã đối chiếu 40/42 ID trùng với bảng server và
# kiểm bằng frame đồng bộ thật từ gs001 Test-36 (khung phải chia khít). Nguồn: Classes/gamecore/KProtocol.cpp:17 + KProtocol.h.
CLIENT_FIXED_SIZES = MappingProxyType({
    220: 9,  # REF_ITEM_SYNC (KProtocol.h:3518-3523); bảng client lệch 1 chỗ ở đuôi, [CHƯA KIỂM] bằng frame thật
    98: 5, 101: 1, 103: 2, 104: 2, 105: 5, 107: 5, 108: 9, 109: 8, 110: 1, 111: 4, 113: 5,
    114: 27, 115: 7, 116: 14, 117: 25, 124: 69, 125: 73, 126: 67, 127: 5, 128: 9, 130: 73,
    131: 9, 132: 5, 133: 5, 135: 6, 137: 5, 138: 2, 140: 149, 142: 5, 146: 5, 151: 1, 152: 153,
    153: 269, 156: 9, 157: 66, 161: 2, 164: 5, 165: 5, 166: 5, 167: 41, 168: 5, 169: 6,
    171: 282, 173: 67, 175: 7, 176: 10, 178: 9, 181: 9, 182: 69, 184: 450, 185: 13, 186: 1,
    191: 1729, 193: 13, 194: 185, 196: 2, 198: 33, 199: 6, 200: 45, 201: 33, 202: 25, 205: 19,
    211: 308, 212: 2, 214: 41, 217: 20, 218: 2, 219: 9,
})
FIXED_SIZES = MappingProxyType({**CLIENT_FIXED_SIZES, **FIXED_SIZES})

# CP:17-173: -1 => WORD ở offset 1, tổng = 1 + WORD, theo
# C/../gamescene/KgameWorld.cpp:5142-5145. Chỉ ID có mục -1 rõ ràng;
# không áp quy tắc này cho mọi ID lạ. 195 là biến độ dài (CP:147).
VARIABLE_IDS = frozenset((
    65, 66, 69, 71, 72, 76, 79, 87, 88, 97, 112, 123,
    129, 136, 139, 141, 148, 149, 162, 163, 170, 172, 195, 215, 216,
    # s2c_extend*: KProtocol.cpp:179-183 đặt -1 (biến độ dài, 1 + WORD).
    250, 251, 252, 253, 254,
))
# Prefix không gồm tên; server gửi strlen(name), không gửi byte NUL.
# ID 70: 31 byte (int32, KProtocol.h CURPLAYER_NORMAL cũ), ID 77: 223 byte; thấy ở exe thật 19/11.
LIVE_ALT_SIZES = MappingProxyType({70: 31, 77: 223})
EXTEND_IDS = frozenset((250, 251, 252, 253, 254))
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
            alt = LIVE_ALT_SIZES.get(protocol)
            if alt and size:
                # exe gs001 thật (Test-36) gửi layout nhỏ (int32/Cocos); ưu tiên nó, chỉ dùng size
                # theo nguồn server khi biên sau size nhỏ không hợp lệ mà biên sau size nguồn thì có.
                def plausible(at):
                    return at == len(payload) or payload[at] in FIXED_SIZES or payload[at] in VARIABLE_IDS
                live_ok = offset + alt <= len(payload) and plausible(offset + alt)
                src_ok = offset + size <= len(payload) and plausible(offset + size)
                if live_ok or not src_ok:
                    size = alt
            if not size and any(r[0] in EXTEND_IDS for r in result):
                # Client thật (KgameWorld.cpp:5134-5136) gặp ID lạ thì `break` bỏ phần đuôi frame;
                # server nhồi rác bộ nhớ sau gói extend (thấy ở 251 thông báo hệ thống).
                # Chỉ nới khi frame đã có record extend (250-254); frame khác vẫn fail-closed.
                break
            if not size:
                raise ProtocolError("Gói GS chưa hỗ trợ: ID=" + str(protocol) + " offset=" + str(offset) +
                                    "; xem E-01b-thieu-giao-thuc.md")
        if size > remaining:
            raise ProtocolError("Record GS bị cắt/layout chưa hỗ trợ: ID=" + str(protocol))
        result.append(payload[offset:offset + size])
        offset += size
    return result
