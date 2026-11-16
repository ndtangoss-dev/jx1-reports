"""Chạy được bằng python -I JX1_OPS/BOT/cli.py --help; không cần PYTHONPATH."""

import argparse
import importlib.util
import math
import os
from pathlib import Path
import sys

# -I bỏ thư mục script khỏi sys.path; nạp đúng package anh em, không site ngoài.
if __package__ in (None, ""):
    package_dir = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "jx1bot", package_dir / "__init__.py", submodule_search_locations=[str(package_dir)])
    package = importlib.util.module_from_spec(spec)
    sys.modules["jx1bot"] = package
    spec.loader.exec_module(package)
    __package__ = "jx1bot"

from .framing import ProtocolError
from .session import Session, TEST_HOST


def main(argv=None):
    parser = argparse.ArgumentParser(description="E-01: một Bot trên JX-Test-36; runtime chưa kiểm")
    parser.add_argument("--connect", action="store_true", help="Thực sự kết nối; mặc định chỉ hiện hướng dẫn")
    parser.add_argument("--host", default=TEST_HOST)
    parser.add_argument("--region", type=int, help="nSelSererIdx đã đối chiếu VM thử")
    parser.add_argument("--enter-map", type=int, help="nEnterMapIdx đã đối chiếu VM thử")
    parser.add_argument("--observed-online", type=int, help="Số online quan sát gần nhất, 0..99")
    parser.add_argument("--encoding", default="ascii", help="Encoding byte đã xác nhận; mặc định ASCII")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--seconds", type=float, default=10.0)
    parser.add_argument("--run", nargs=3, type=int, metavar=("X", "Y", "MAP"))
    parser.add_argument("--skill", nargs=3, type=int, metavar=("ID", "X", "Y"))
    posture = parser.add_mutually_exclusive_group()
    posture.add_argument("--sit", action="store_true")
    posture.add_argument("--stand", action="store_true")
    args = parser.parse_args(argv)
    if not args.connect:
        parser.print_help()
        return 0
    if args.region is None or args.enter_map is None or args.observed_online is None:
        parser.error("--connect cần --region, --enter-map, --observed-online")
    required = ("JX_BOT_ACCOUNT", "JX_BOT_PASSWORD", "JX_BOT_ROLE", "JX_BOT_CLIENT_KEY")
    if any(not os.environ.get(k) for k in required):
        parser.error("Cần biến môi trường: " + ", ".join(required))
    session = None
    try:
        if not math.isfinite(args.seconds) or args.seconds < 0:
            raise ProtocolError("--seconds phải hữu hạn và >=0")
        from . import packets
        # Kiểm hành động trước khi mở socket, không lộ dữ liệu đầu vào khi báo lỗi.
        if args.run:
            packets.run(*args.run)
        if args.skill:
            packets.skill(*args.skill)
        try:
            client_key = int(os.environ["JX_BOT_CLIENT_KEY"], 0)
        except ValueError:
            raise ProtocolError("JX_BOT_CLIENT_KEY phải là uint32 dạng số") from None
        session = Session(args.host, args.timeout)
        session.login(os.environ[required[0]], os.environ[required[1]], os.environ[required[2]],
                      args.region, args.enter_map, client_key, args.observed_online, args.encoding)
        print("Đã nhận đồng bộ theo profile nguồn; chưa xác minh hành vi gameplay.")
        if args.run:
            session.run(*args.run)
        if args.skill:
            session.skill(*args.skill)
        if args.sit or args.stand:
            session.sit(args.sit)
        session.hold(args.seconds)
        return 0
    except (ProtocolError, EOFError) as error:
        print("Dừng: " + str(error), file=sys.stderr)
        return 2
    except OSError:
        print("Dừng do lỗi kết nối hoặc timeout; không tự thử lại.", file=sys.stderr)
        return 3
    except KeyboardInterrupt:
        return 130
    finally:
        if session is not None:
            session.close()


if __name__ == "__main__":
    # Windows pipes có thể mặc định cp1252; -I bỏ PYTHONIOENCODING.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
