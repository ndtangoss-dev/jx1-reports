"""Một Bot, hai kết nối nối tiếp; không tự khởi động server hoặc thử lại login."""

import ipaddress
import math
import socket
import struct
import time
from collections import deque
from enum import Enum

from . import packets
from .crypto import from_account_begin
from .framing import FrameDecoder, ProtocolError, pack_frame
from .worldsync import split_records

TEST_HOST = "192.168.56.150"
MAIN_HOST = "192.168.1.50"
BISHOP_PORT = 56722
GS_PORT = 51189
MAX_ONLINE = 100
SERVER_HZ = 18


def validate_target(host, port):
    # Không DNS, hostname, IPv6 mapped, dạng số nguyên hoặc redirect sang Main VM.
    try:
        address = ipaddress.IPv4Address(host)
    except (ipaddress.AddressValueError, TypeError):
        raise ProtocolError("Chỉ cho phép IPv4 literal của JX-Test-36") from None
    if str(address) == MAIN_HOST:
        raise ProtocolError("CHẶN CỨNG Main VM 192.168.1.50")
    if str(address) != TEST_HOST or port not in (BISHOP_PORT, GS_PORT):
        raise ProtocolError("Chỉ cho phép JX-Test-36 và cổng 56722/51189")
    return str(address)


def check_admission(observed_online):
    if isinstance(observed_online, bool) or not isinstance(observed_online, int) or not 0 <= observed_online < MAX_ONLINE:
        raise ProtocolError("Cần số online quan sát 0..99 trước khi thêm một Bot")


class Channel:
    def __init__(self, sock):
        self.sock = sock
        self.decoder = FrameDecoder()
        self.pending = deque()
        self.rx = self.tx = None
        self.closed = False

    @classmethod
    def connect(cls, host, port, timeout):
        host = validate_target(host, port)
        channel = cls(socket.create_connection((host, port), timeout=timeout))
        try:
            channel.handshake(time.monotonic() + timeout)
        except BaseException:
            channel.close()
            raise
        return channel

    def _frame(self, deadline=None):
        if self.closed:
            raise ProtocolError("Kênh đã đóng")
        while not self.pending:
            if deadline is not None:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("Hết thời gian chờ gói")
                self.sock.settimeout(remaining)
            data = self.sock.recv(65536)
            if not data:
                self.decoder.finish()
                raise EOFError("Server đóng kết nối")
            self.pending.extend(self.decoder.feed(data))
        return self.pending.popleft()

    def handshake(self, deadline=None):
        if self.closed:
            raise ProtocolError("Kênh đã đóng")
        if self.rx is not None:
            raise ProtocolError("ACCOUNT_BEGIN đã được xử lý")
        self.rx, self.tx = from_account_begin(self._frame(deadline))

    def send(self, payload):
        if self.closed:
            raise ProtocolError("Kênh đã đóng")
        if self.tx is None:
            raise ProtocolError("Chưa nhận ACCOUNT_BEGIN")
        pack_frame(payload)  # kiểm kích thước trước khi tiến khóa
        self.sock.sendall(pack_frame(self.tx.apply(payload)))

    def receive(self, deadline=None):
        if self.closed:
            raise ProtocolError("Kênh đã đóng")
        if self.rx is None:
            raise ProtocolError("Chưa nhận ACCOUNT_BEGIN")
        return self.rx.apply(self._frame(deadline))

    def close(self):
        if self.closed:
            return
        self.closed = True  # chặn I/O trước khi giải phóng tài nguyên
        try:
            self.sock.close()
        finally:
            self.pending.clear()
            self.decoder.buffer.clear()
            self.rx = self.tx = None


class State(Enum):
    NEW = "new"
    BISHOP = "bishop"
    AUTHENTICATED = "authenticated"
    ROLE_SELECTED = "role_selected"
    SYNCING = "syncing"
    IN_GAME = "in_game"
    CLOSED = "closed"


class Session:
    def __init__(self, host=TEST_HOST, timeout=10.0, connector=Channel.connect):
        validate_target(host, BISHOP_PORT)
        if not math.isfinite(timeout) or timeout <= 0:
            raise ProtocolError("Timeout phải hữu hạn và >0")
        self.host, self.timeout, self.connector = host, timeout, connector
        self.state = State.NEW
        self.gateway = self.game = None
        self.client_key = None
        self.next_action = 0.0

    def _expect(self, state):
        if self.state != state:
            raise ProtocolError("Sai trạng thái phiên: " + self.state.value)

    def login(self, account, password, role_name, region, enter_map,
              client_key, observed_online, encoding="ascii"):
        self._expect(State.NEW)
        check_admission(observed_online)
        packets.uint32(client_key, "client_key")
        request = packets.login(account, password, region, enter_map, encoding)
        role_bytes = packets.cstring(role_name, 64, "role", encoding).split(b"\0", 1)[0]
        self.client_key = client_key
        deadline = time.monotonic() + self.timeout
        try:
            self.gateway = self.connector(self.host, BISHOP_PORT, self.timeout)
            self.state = State.BISHOP
            self.gateway.send(request)
            packets.check_login_response(self.gateway.receive(deadline), request)
            self.state = State.AUTHENTICATED
            roles = packets.role_list(self.gateway.receive(deadline))
            if role_bytes not in {r.name for r in roles}:
                raise ProtocolError("Nhân vật yêu cầu không có trong danh sách")
            self.gateway.send(packets.select_role(role_bytes))
            self.state = State.ROLE_SELECTED
            permit = packets.permit_login(self.gateway.receive(deadline), account, role_bytes, encoding)
            # Permit mang IP công khai của gs001 (cấu hình cho client thật), không phải IP host-only;
            # Bot không đi theo địa chỉ server báo, luôn nối vào VM thử đã kiểm.
            validate_target(self.host, permit.port)
            if permit.host == "192.168.1.50":
                raise ProtocolError("CHẶN CỨNG Main VM 192.168.1.50 (permit trỏ Main VM)")
            if permit.port != GS_PORT:
                raise ProtocolError("Permit không trỏ đúng cổng gs001 của VM thử")
            self.game = self.connector(self.host, permit.port, self.timeout)
            self.game.send(packets.logic_login(permit.guid))
            self.gateway.close()
            self.gateway = None
            self.state = State.SYNCING
            self.poll(deadline)
            while self.state == State.SYNCING:
                self.poll(deadline)
        except BaseException:
            self.close()
            raise

    def poll(self, deadline=None):
        if self.state not in (State.SYNCING, State.IN_GAME):
            raise ProtocolError("Chưa có kết nối game")
        try:
            messages = split_records(self.game.receive(deadline))
            # Không ACK một frame có SYNC_END lặp/sai key ở phía sau.
            ends = [m for m in messages if m[0] == packets.S2C.SYNC_END]
            if ends:
                self._expect(State.SYNCING)
                if len(ends) != 1:
                    raise ProtocolError("SYNC_END lặp trong frame")
                packets.sync_reply(ends[0], self.client_key)
            for message in messages:
                if message[0] == packets.S2C.PING:
                    self.game.send(packets.ping_reply(message, int(time.monotonic() * 1000) & 0xFFFFFFFF))
                elif message[0] == packets.S2C.SYNC_END:
                    self._expect(State.SYNCING)
                    reply = packets.sync_reply(message, self.client_key)
                    self.game.send(reply)
                    self.game.send(struct.pack("<Bi", packets.C2S.CP_LOCK, 1))
                    self.state = State.IN_GAME
        except TimeoutError:
            raise
        except BaseException:
            self.close()
            raise

    def _action(self, payload):
        self._expect(State.IN_GAME)
        now = time.monotonic()
        if now < self.next_action:
            time.sleep(self.next_action - now)
        try:
            self.game.send(payload)
            self.next_action = time.monotonic() + 1 / SERVER_HZ
        except BaseException:
            self.close()
            raise

    def run(self, x, y, map_id):
        self._action(packets.run(x, y, map_id))

    def skill(self, skill_id, x, y):
        self._action(packets.skill(skill_id, x, y))

    def sit(self, enabled=True):
        self._action(packets.sit(enabled))

    def hold(self, seconds):
        self._expect(State.IN_GAME)
        if not math.isfinite(seconds) or seconds < 0:
            raise ProtocolError("Thời gian đứng yên phải hữu hạn và >=0")
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            try:
                self.poll(deadline)
            except TimeoutError:
                break

    def close(self):
        # E-07: logout không có application payload/ACK lưu. BOT chặn hành
        # động trước, đóng game rồi Bishop còn sót, kể cả một close bị lỗi.
        channels = (self.game, self.gateway)
        self.gateway = self.game = None
        self.state = State.CLOSED
        self.client_key = None
        self.next_action = 0.0
        error = None
        for channel in channels:
            if channel is not None:
                try:
                    channel.close()
                except OSError as exc:
                    if error is None:
                        error = exc
        if error is not None:
            raise error

    def logout(self):
        """Thoát bằng đóng socket; không xác nhận DB persistence [CHƯA KIỂM]."""
        self.close()
