"""Smoke chỉ handshake/sync tổng hợp; không gọi login hay dùng tài khoản thật."""

import socket
import time

from JX1_OPS.BOT.session import Channel, Session, State
from .core import Scenario, Step


def connect_fake(context):
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
