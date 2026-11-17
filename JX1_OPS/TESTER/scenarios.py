"""Kịch bản smoke/full_cycle chỉ dùng máy chủ giả và dữ liệu tổng hợp."""

import socket
import secrets
import time

from JX1_OPS.BOT import packets
from JX1_OPS.BOT.session import Channel, Session, State, TEST_HOST, GS_PORT, validate_target
from .core import Redactor, Scenario, SkipStep, Step


def connect_fake(context):
    if context.config.host != "127.0.0.1":
        raise ValueError("smoke_login chỉ cho máy chủ giả 127.0.0.1")
    channel = Channel(socket.create_connection((context.config.host, context.config.port), timeout=2))
    context.state["channel"] = channel
    channel.handshake(time.monotonic() + 2)
    context.log("Đã nhận ACCOUNT_BEGIN tổng hợp; không lưu khóa")


def sync_fake(context):
    session = Session(timeout=2)
    context.state["session"] = session
    channel = context.state["channel"]
    # Dùng Session.poll của BOT, không sửa validate_target hay connector thật.
    original_receive = channel.receive

    def receive(deadline=None):
        data = original_receive(deadline)
        context.packet("nhận", data)
        return data

    channel.receive = receive
    session.game, session.client_key, session.state = channel, 0x01020304, State.SYNCING
    deadline = time.monotonic() + 2
    while session.state == State.SYNCING:
        session.poll(deadline)
    if session.state != State.IN_GAME:
        raise AssertionError("Không chuyển IN_GAME")
    context.log("IN_GAME theo vector tổng hợp; gs001 thật chưa kiểm")


def close_fake(context):
    context.state["session"].close()
    context.log("Đã đóng kết nối máy chủ giả")


SMOKE_LOGIN = Scenario("smoke_login", (
    Step("connect_fake", connect_fake, "Nhận ACCOUNT_BEGIN tổng hợp", 3, "blocker"),
    Step("sync_fake", sync_fake, "Nhận END, gửi ACK 9 byte + CP_LOCK, trạng thái IN_GAME", 3),
    Step("close_fake", close_fake, "Đóng phiên", 1, "minor"),
))


def _local_channel(context):
    # Endpoint thật duy nhất là fixture loopback, kể cả permit mang địa chỉ logic BOT.
    if context.config.host != "127.0.0.1":
        raise ValueError("full_cycle chỉ cho máy chủ giả 127.0.0.1")
    channel = Channel(socket.create_connection((context.config.host, context.config.port), timeout=2))
    context.state["channel"] = channel
    channel.handshake(time.monotonic() + 2)
    return channel


def login_cycle(context):
    if "credentials" not in context.state:
        # Chỉ dữ liệu tổng hợp trong RAM; không đọc tài khoản thật hoặc ghi auth payload.
        password = secrets.token_hex(8)
        context.state["credentials"] = (context.bot, password)
        context.redactor.values.extend(Redactor((password,)).values)
    account, password = context.state["credentials"]
    gateway = _local_channel(context)
    context.state["gateway"] = gateway
    request = packets.login(account, password, 1, 1)
    gateway.send(request)
    deadline = time.monotonic() + 2
    packets.check_login_response(gateway.receive(deadline), request)
    roles = packets.role_list(gateway.receive(deadline))
    role = next((role for role in roles if role.name == context.bot.encode("ascii")), None)
    context.state["role"] = role
    if "initial_role" not in context.state:
        context.state["initial_role"] = role
    context.log("Bishop giả chấp nhận login; đã đọc danh sách nhân vật tổng hợp")


def create_cycle(context):
    if context.state["role"] is not None:
        raise SkipStep("Nhân vật tổng hợp đã có; không cần tạo. BOT chưa có request/response tạo nhân vật cho nhánh chưa có")
    raise SkipStep("BOT thiếu request/response tạo nhân vật và mã kết quả; không đoán giao thức (E-01b)")


def enter_cycle(context):
    role = context.state.get("role")
    if role is None:
        raise SkipStep("Chưa có nhân vật; phụ thuộc gói tạo nhân vật BOT chưa hỗ trợ")
    gateway = context.state["gateway"]
    gateway.send(packets.select_role(role.name))
    account, _ = context.state["credentials"]
    permit = packets.permit_login(gateway.receive(time.monotonic() + 2), account, role.name)
    validate_target(permit.host, permit.port)
    if (permit.host, permit.port) != (TEST_HOST, GS_PORT):
        raise AssertionError("Permit giả không đúng đích logic BOT")
    channel = _local_channel(context)
    session = Session(timeout=2)
    context.state["session"] = session
    # Giá trị tổng hợp lấy từ cổng fixture, không phải khóa thật hoặc cơ chế tìm khóa.
    session.game, session.client_key, session.state = channel, context.config.port, State.SYNCING
    channel.send(packets.logic_login(permit.guid))
    gateway.close()
    context.state.pop("gateway")
    deadline = time.monotonic() + 2
    while session.state == State.SYNCING:
        session.poll(deadline)
    if session.state != State.IN_GAME:
        raise AssertionError("Không chuyển IN_GAME")
    context.log("IN_GAME tổng hợp sau SYNC_END/ACK và CP_LOCK")


def _in_game(context):
    session = context.state.get("session")
    if session is None or session.state != State.IN_GAME:
        raise SkipStep("Chưa vào game do thiếu nhân vật/gói tạo nhân vật")
    return session


def walk_cycle(context):
    session = _in_game(context)
    session.run(100, 200, 1)  # Tọa độ/map chỉ thuộc fixture, không suy từ dữ liệu bỏ qua.
    session.hold(30)
    context.log("Đã gửi RUN tới tọa độ tổng hợp và duy trì phiên đủ 30 s; chưa xác nhận vị trí thực")


def skill_cycle(context):
    _in_game(context).skill(1, -1, 1)  # Skill/NPC do fixture quy định, không chọn mục tiêu thật.
    context.log("Đã gửi một SKILL tới NPC tổng hợp; chưa xác nhận sát thương/quái chết")


def kill_cycle(context):
    raise SkipStep("Thiếu giải mã trạng thái NPC, skill sở hữu và xác nhận sát thương/death; E-01b chỉ tách/bỏ qua record")


def logout_cycle(context):
    for name in ("session", "gateway", "channel"):
        value = context.state.pop(name, None)
        if value is not None:
            value.close()
    context.log("Đã đóng socket giả bằng BOT.close; chưa gửi logout ứng dụng")
    raise SkipStep("BOT chưa có request/response logout ứng dụng; đóng TCP không chứng minh lưu nhân vật")


def reenter_cycle(context):
    if context.state["initial_role"] is None:
        raise SkipStep("Nhân vật chưa được tạo; chưa thể vào lại")
    login_cycle(context)
    if context.state["role"] is None:
        raise AssertionError("Nhân vật biến mất trong danh sách sau khi vào lại")
    enter_cycle(context)


def verify_cycle(context):
    _in_game(context)
    if context.state["role"] != context.state["initial_role"]:
        raise AssertionError("Thông tin danh sách nhân vật thay đổi sau khi vào lại")
    context.log("Danh sách giữ nguyên tên/giới tính/hệ/level tổng hợp; chưa kiểm toàn bộ trạng thái nhân vật")


def persistence_cycle(context):
    raise SkipStep("Thiếu giải mã/snapshot vị trí, HP, trang bị, hành trang và xác nhận lưu sau logout; chưa chứng minh nhân vật còn nguyên")


FULL_CYCLE = Scenario("full_cycle", (
    Step("login", login_cycle, "Login và role list qua API packets/Channel hiện có", 3, "blocker"),
    Step("create_character", create_cycle, "Tạo nếu chưa có, hoặc BỎ QUA có lý do"),
    Step("enter_game", enter_cycle, "Chọn role, permit, logic login, sync IN_GAME", 3),
    Step("walk_30s", walk_cycle, "Gửi RUN tổng hợp và hold 30 giây", 35),
    Step("attack_one", skill_cycle, "Gửi đúng một SKILL tới NPC fixture"),
    Step("verify_kill", kill_cycle, "Xác nhận đánh chết một quái hoặc ghi thiếu giao thức"),
    Step("logout", logout_cycle, "Đóng socket; ghi rõ thiếu logout ứng dụng"),
    Step("reenter", reenter_cycle, "Login lại và sync IN_GAME", 6),
    Step("verify_role", verify_cycle, "Tên/giới tính/hệ/level trong role list giữ nguyên"),
    Step("verify_persistence", persistence_cycle, "Toàn trạng thái nhân vật hoặc ghi thiếu giao thức"),
))
