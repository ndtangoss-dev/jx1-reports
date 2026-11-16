"""Cipher.h:19-27; SocketClient.cpp:487-510; KSG_EncodeDecode.cpp:14-35.

XOR lặp bốn byte khóa; khóa tiến MỘT lần mỗi payload, không mỗi TCP recv.
Đây là giao thức legacy, không phải mã hóa bảo mật hiện đại.
"""

import struct

from .framing import ProtocolError

MASK = 0xFFFFFFFF
ACCOUNT_BEGIN = struct.Struct("<BB6sII16s")


class RollingXor:
    def __init__(self, key):
        if not 0 <= key <= MASK:
            raise ProtocolError("Khóa XOR phải là uint32")
        self.key = key

    def apply(self, payload):
        if not payload:
            return b""  # KSG_EncodeDecode.h:21,35: không tiến khóa khi rỗng
        key_bytes = self.key.to_bytes(4, "little")
        result = bytes(b ^ key_bytes[i % 4] for i, b in enumerate(payload))
        self.key = (self.key * 31 + 134775813) & MASK
        return result


def from_account_begin(payload):
    if len(payload) != ACCOUNT_BEGIN.size:
        raise ProtocolError("ACCOUNT_BEGIN phải dài 32 byte")
    protocol, mode, _, server_key, client_key, _ = ACCOUNT_BEGIN.unpack(payload)
    if protocol != 0x20 or mode != 0:
        raise ProtocolError("ACCOUNT_BEGIN sai ID hoặc mode chưa hỗ trợ")
    return RollingXor((~server_key) & MASK), RollingXor((~client_key) & MASK)
