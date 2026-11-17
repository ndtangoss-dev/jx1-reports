"""Luồng đăng nhập chuẩn bị cho VM thử; kiểm chứng bằng loopback, không tự chạy VM."""

from dataclasses import dataclass
import os
import socket
import time

from JX1_OPS.BOT import packets
from JX1_OPS.BOT.session import Channel, Session, State, check_admission
from .core import Redactor, Scenario, Step


@dataclass(frozen=True, repr=False)
class Credentials:
    account: str
    password: str
    role: bytes
    client_key: int
    region: int
    enter_map: int
    observed_online: int
    encoding: str


def environment_credentials(context):
    prefix = "JX1_" + context.bot.upper() + "_"
    names = ("ACCOUNT", "PASSWORD", "ROLE", "CLIENT_KEY", "REGION", "ENTER_MAP", "OBSERVED_ONLINE")
    values = [os.environ.get(prefix + name, "") for name in names]
    # Đăng ký trước mọi validation/exception; không đưa giá trị vào message/log.
    context.redactor.values.extend(Redactor(values).values)
    if not all(values):
        raise ValueError("Thiếu biến môi trường bắt buộc cho bot (xem README)")
    encoding = os.environ.get(prefix + "ENCODING", "ascii")
    try:
        account, password, role, key, region, enter_map, online = values
        key, region, enter_map, online = (int(value, 0) for value in (key, region, enter_map, online))
        packets.uint32(key, "client_key")
        check_admission(online)
        packets.login(account, password, region, enter_map, encoding)
        role = packets.cstring(role, 64, "role", encoding).split(b"\0", 1)[0]
    except (ValueError, LookupError):
        raise ValueError("Biến môi trường bot không hợp lệ (xem profile BOT/README)") from None
    return Credentials(account, password, role, key, region, enter_map, online, encoding)


def guarded_channel(context, host, port, *, game=False):
    # Kiểm ngay tại ranh giới socket, cả Bishop lẫn endpoint do permit trả về.
    context.config.validate_endpoint(host, port, game=game)
    channel = Channel(socket.create_connection((host, port), timeout=2))
    try:
        channel.handshake(time.monotonic() + 2)
    except BaseException:
        channel.close()
        raise
    return channel


def login_real(context):
    credentials = environment_credentials(context)
    context.state["credentials"] = credentials
    gateway = guarded_channel(context, context.config.host, context.config.port)
    context.state["gateway"] = gateway
    request = packets.login(credentials.account, credentials.password, credentials.region,
                            credentials.enter_map, credentials.encoding)
    gateway.send(request)
    packets.check_login_response(gateway.receive(time.monotonic() + 2), request)
    context.log("Login response hợp lệ theo profile BOT; không ghi auth payload")


def role_real(context):
    credentials = context.state["credentials"]
    roles = packets.role_list(context.state["gateway"].receive(time.monotonic() + 2))
    if credentials.role not in {role.name for role in roles}:
        raise ValueError("Nhân vật yêu cầu không có trong danh sách; không tự tạo nhân vật")
    context.log("Đã đối chiếu nhân vật yêu cầu trong role list; không ghi tên")


def enter_real(context):
    credentials, gateway = context.state["credentials"], context.state["gateway"]
    gateway.send(packets.select_role(credentials.role))
    permit = packets.permit_login(gateway.receive(time.monotonic() + 2),
                                  credentials.account, credentials.role, credentials.encoding)
    channel = guarded_channel(context, permit.host, permit.port, game=True)
    session = Session(timeout=2)
    context.state["session"] = session
    session.game, session.client_key, session.state = channel, credentials.client_key, State.SYNCING
    channel.send(packets.logic_login(permit.guid))
    gateway.close()
    context.state.pop("gateway")
    deadline = time.monotonic() + 2
    while session.state == State.SYNCING:
        session.poll(deadline)
    if session.state != State.IN_GAME:
        raise AssertionError("Không chuyển IN_GAME")
    context.log("IN_GAME theo parser BOT sau SYNC_END/ACK và CP_LOCK; ABI thật [CHƯA KIỂM]")


def hold_real(context):
    session = context.state["session"]
    if session.state != State.IN_GAME:
        raise AssertionError("Chưa IN_GAME")
    session.hold(30)
    if session.state != State.IN_GAME:
        raise AssertionError("Phiên không còn IN_GAME")
    context.log("Đã giữ kết nối 30 s và xử lý PING nếu nhận; không chứng minh gameplay/lưu nhân vật")


def close_real(context):
    context.state["session"].close()
    context.log("Đã đóng TCP; logout ứng dụng và lưu dữ liệu [CHƯA KIỂM]")


REAL_LOGIN = Scenario("real_login", (
    Step("real_login", login_real, "Đăng nhập bằng biến môi trường qua endpoint đã kiểm", 3, "blocker"),
    Step("role", role_real, "Role yêu cầu có trong danh sách", 3),
    Step("enter_game", enter_real, "Permit đúng allowlist, logic login và sync IN_GAME", 5),
    Step("hold_session", hold_real, "Giữ phiên 30 s, xử lý PING theo BOT", 35),
    Step("close", close_real, "Đóng TCP, không nhận là logout ứng dụng", 1, "minor"),
))
