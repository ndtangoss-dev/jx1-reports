"""Thang tải BOT trên Test-36 (#226 mục 2): chạy N Bot song song, thu số đo phía Bot + phía VM.
Tài khoản botld001..botldNNN, vai BotLdNNN (tạo bằng bot_tao_role.py). Mật khẩu/khóa chỉ từ biến môi trường:
JX_BOT_PASSWORD, JX_BOT_CLIENT_KEY. Chạy: python -I -X utf8 <file> <N> <giây> <thư mục out>
Số đo VM (RAM/CPU gs001) do script PowerShell ngoài lấy qua WinRM, không nằm ở đây."""
import json
import os
import statistics
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    n, secs, out = int(sys.argv[1]), float(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    procs = []
    for i in range(1, n + 1):
        env = dict(os.environ, JX_BOT_ACCOUNT="botld%03d" % i, JX_BOT_ROLE="BotLd%03d" % i)
        f = out / ("bot%03d.json" % i)
        procs.append((i, f, subprocess.Popen(
            [sys.executable, "-I", "-X", "utf8", str(HERE / "collect_bot_metrics.py"), str(secs), str(f)],
            env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)))
        time.sleep(1.2)  # nhẹ tay với Bishop: vào từng Bot một
    ok, ticks, rx = 0, [], []
    fails = []
    for i, f, p in procs:
        txt = p.communicate(timeout=secs + 120)[0]
        if p.returncode == 0 and f.exists():
            d = json.loads(f.read_text("utf8"))
            ok += 1
            ticks += [t["tick_ms"] for t in d["tick_samples"]]
            net = d["network_samples"]
            if len(net) > 1:
                rx.append(net[-1]["rx_bytes"] * 8 / 1000 / max(net[-1]["time_s"], 1))
        else:
            fails.append((i, txt.strip().splitlines()[-1:] if txt.strip() else []))
    ticks.sort()
    res = {"n": n, "vao_duoc": ok, "loi": fails[:5],
           "tick_ms": {"mean": round(statistics.mean(ticks), 1), "p50": ticks[len(ticks) // 2],
                       "p95": ticks[int(len(ticks) * .95)], "max": ticks[-1]} if ticks else None,
           "rx_kbps_moi_bot": round(statistics.mean(rx), 1) if rx else None}
    (out / "tong.json").write_text(json.dumps(res, indent=1), "utf8")
    print(json.dumps(res))


if __name__ == "__main__":
    main()
