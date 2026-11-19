"""E-09: đếm record người chơi khác (S2C id 74/75) mà MỘT Bot nhận trong N giây, để so Enabled=0 với Enabled=1 Solo.
Biến môi trường như cli.py. Chạy: python -I -X utf8 contar_nguoi_choi.py <giây>   (không in bí mật)"""
import collections
import importlib.util
import os
import sys
from pathlib import Path

BOT = Path(__file__).resolve().parent.parent.parent / "BOT"
spec = importlib.util.spec_from_file_location("jx1bot", BOT / "__init__.py", submodule_search_locations=[str(BOT)])
pkg = importlib.util.module_from_spec(spec)
sys.modules["jx1bot"] = pkg
spec.loader.exec_module(pkg)
from jx1bot.session import Channel, Session  # noqa: E402
from jx1bot.worldsync import split_records  # noqa: E402

counts = collections.Counter()
receive = Channel.receive


def counting(self, deadline=None):
    data = receive(self, deadline)
    if self is session.game:
        try:
            for m in split_records(data):
                counts[m[0]] += 1
        except Exception:
            counts["loi_tach"] += 1
    return data


Channel.receive = counting
session = Session()
env = os.environ
session.login(env["JX_BOT_ACCOUNT"], env["JX_BOT_PASSWORD"], env["JX_BOT_ROLE"], 1, 0, int(env["JX_BOT_CLIENT_KEY"], 0), 0)
session.hold(float(sys.argv[1]))
session.close()
print("player_74_75", counts[74] + counts[75], "npc_77", counts[77], "tong_id", sum(counts.values()), "chi_tiet_74_75_77", counts[74], counts[75], counts[77])
