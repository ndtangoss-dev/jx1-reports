"""Thu số đo từ MỘT Bot vào gs001 Test-36, xuất JSON cho jx1_bench.py (P-02/B-04).

Đây là đo phía Bot, không phải đo trong VM:
  tick_ms  = khoảng cách giữa hai frame S2C liên tiếp tới Bot (xấp xỉ nhịp gửi của gs001);
  mạng     = byte RX/TX của chính socket Bot theo cửa sổ 5 s (không phải cả interface guest);
  frame_samples = CHƯA CÓ (cần client thật), ghi mảng rỗng.
Tài khoản/mật khẩu/khóa chỉ lấy từ biến môi trường như cli.py. Chạy: python -I -X utf8 <file> <giây> <out.json>
"""
import importlib.util
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOT = HERE.parent.parent / "BOT"
spec = importlib.util.spec_from_file_location("jx1bot", BOT / "__init__.py", submodule_search_locations=[str(BOT)])
pkg = importlib.util.module_from_spec(spec)
sys.modules["jx1bot"] = pkg
spec.loader.exec_module(pkg)
from jx1bot.session import Channel, Session  # noqa: E402

WINDOW = 5.0


def main():
    seconds = float(sys.argv[1])
    out = Path(sys.argv[2])
    game_stats = {"rx": 0, "tx": 0, "frames": []}
    receive, send = Channel.receive, Channel.send

    def counting_receive(self, deadline=None):
        data = receive(self, deadline)
        if self is session.game:
            game_stats["rx"] += len(data) + 2
            game_stats["frames"].append((time.monotonic(), game_stats["rx"], game_stats["tx"]))
        return data

    def counting_send(self, payload):
        if self is session.game:
            game_stats["tx"] += len(payload) + 2
        return send(self, payload)

    Channel.receive, Channel.send = counting_receive, counting_send
    session = Session()
    env = os.environ
    session.login(env["JX_BOT_ACCOUNT"], env["JX_BOT_PASSWORD"], env["JX_BOT_ROLE"], 1, 0,
                  int(env["JX_BOT_CLIENT_KEY"], 0), 0)
    start = len(game_stats["frames"])
    session.hold(seconds)
    session.close()
    frames = game_stats["frames"][start:]
    ticks = [{"tick_ms": round((b[0] - a[0]) * 1000, 3)} for a, b in zip(frames, frames[1:])]
    t0 = frames[0][0]
    network, last = [], None
    for t, rx, tx in frames:
        if last is None or t - last >= WINDOW:
            network.append({"time_s": round(t - t0, 3), "rx_bytes": rx, "tx_bytes": tx})
            last = t
    if network[-1]["time_s"] != round(frames[-1][0] - t0, 3):
        t, rx, tx = frames[-1]
        network.append({"time_s": round(t - t0, 3), "rx_bytes": rx, "tx_bytes": tx})
    out.write_text(json.dumps({
        "sample_kind": "bot_side_one_bot",
        "target": {"name": "JX-Test-36", "ip": "192.168.56.150"},
        "network_mode": "cumulative",
        "network_adapter": "bot-socket-gs001",
        "tick_samples": ticks,
        "network_samples": network,
        "frame_samples": [],
    }, indent=1), encoding="utf8")
    print("frames", len(frames), "ticks", len(ticks), "net", len(network))


if __name__ == "__main__":
    main()
