"""ClientStage.cpp:136-166,235-264,279-284: WORD gồm cả hai byte đầu."""

import struct


class ProtocolError(ValueError):
    """Dữ liệu không phù hợp phần giao thức đã xác minh."""


def pack_frame(payload):
    if not 1 <= len(payload) <= 65533:
        raise ProtocolError("Payload phải dài 1..65533 byte")
    return struct.pack("<H", len(payload) + 2) + payload


class FrameDecoder:
    """Giữ phần khung TCP chưa đủ; không đoán lại ranh giới khi lỗi."""

    def __init__(self):
        self.buffer = bytearray()
        self.failed = False

    def feed(self, data):
        if self.failed:
            raise ProtocolError("Decoder đã lỗi; cần kết nối mới")
        self.buffer.extend(data)
        frames = []
        offset = 0
        while len(self.buffer) - offset >= 2:
            length = struct.unpack_from("<H", self.buffer, offset)[0]
            if length < 3:
                self.failed = True
                self.buffer.clear()
                raise ProtocolError("Độ dài khung dưới 3")
            if len(self.buffer) - offset < length:
                break
            frames.append(bytes(self.buffer[offset + 2:offset + length]))
            offset += length
        del self.buffer[:offset]
        return frames

    def finish(self):
        if self.failed or self.buffer:
            raise ProtocolError("EOF giữa khung hoặc decoder đã lỗi")
