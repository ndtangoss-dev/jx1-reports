"""Tạo một vai thử cho tài khoản thử trên JX-Test-36 (Q-58). Mật khẩu chỉ từ biến môi trường JX_BOT_PASSWORD.
Chạy: python -I JX1_OPS/TOOLS/bot_tao_role.py <account> <tên 6..16 byte> <region> <enter_map> [native_place 53|54]"""
import importlib.util, os, sys, time
from pathlib import Path
d = Path(__file__).resolve().parent.parent / "BOT"
spec = importlib.util.spec_from_file_location("jx1bot", d / "__init__.py", submodule_search_locations=[str(d)])
pkg = importlib.util.module_from_spec(spec); sys.modules["jx1bot"] = pkg; spec.loader.exec_module(pkg)
from jx1bot import packets
from jx1bot.session import Channel, BISHOP_PORT, TEST_HOST, validate_target

acc, name, region, emap = sys.argv[1], sys.argv[2].encode(), int(sys.argv[3]), int(sys.argv[4])
validate_target(TEST_HOST, BISHOP_PORT)
req = packets.login(acc, os.environ["JX_BOT_PASSWORD"], region, emap)
ch = Channel.connect(TEST_HOST, BISHOP_PORT, 10.0)
dl = time.monotonic() + 15
ch.send(req)
packets.check_login_response(ch.receive(dl), req)
roles = packets.role_list(ch.receive(dl))
print("vai hien co:", len(roles))
if not any(r.name == name for r in roles):
    ch.send(packets.new_player(name, 0, 0, int(sys.argv[5]) if len(sys.argv) > 5 else 53, region))
    print("tao vai ->", packets.new_player_response(ch.receive(dl)))
ch.close()
