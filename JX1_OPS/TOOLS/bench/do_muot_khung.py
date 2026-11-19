"""Do do muot hinh tren LD (#255): quay man hinh vai giay khi nhan vat chay, tach khung, do dich chuyen nen giua hai khung.
Chi doc/ghi qua adb toi MOT emulator (--serial). Khong mat khau/khoa.
Chay: python -I -X utf8 do_muot_khung.py --serial emulator-5556 --nhan A --giay 3 [--chay x1 y1 x2 y2]
Ket qua: JSON (so khung, so khung dung yen, trung binh/lech chuan dich chuyen, p95) in ra va ghi D:/JX-build/muot/<nhan>.json
Phuong phap: screenrecord (so khung theo thoi gian thuc), ffmpeg ra khung xam 1/2 kich thuoc, khop khoi mot mieng nen
(vung giua-trai, tranh HUD) theo SAD trong +-R pixel; do dich chuyen giua hai khung lien tiep.
Chi so: stand_pct = % cap khung gan nhu khong dich (giat theo nhip 18 Hz -> cao); cv = do lech/trung binh (cao = khong deu)."""
import argparse
import json
import statistics
import subprocess
import sys
import time
from pathlib import Path

ADB = r"C:\LDPlayer\LDPlayer9\adb.exe"
FFMPEG = r"C:\Users\PC\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v9.0.2.exe"
W, H = 960, 540
OUT = Path(r"D:\JX-build\muot")


def adb(serial, *a, timeout=60):
    p = subprocess.run([ADB, "-s", serial, *a], capture_output=True, timeout=timeout)
    return p.stdout


def match(prev, cur, x0, y0, bw, bh, r):
    best, bd = None, (0, 0)
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            s = 0
            for y in range(0, bh, 2):
                a = (y0 + y) * W + x0
                b = (y0 + y + dy) * W + x0 + dx
                ra, rb = prev[a:a + bw:2], cur[b:b + bw:2]
                s += sum(abs(i - j) for i, j in zip(ra, rb))
            if best is None or s < best:
                best, bd = s, (dx, dy)
    return bd, best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serial", required=True)
    ap.add_argument("--nhan", required=True)
    ap.add_argument("--giay", type=int, default=3)
    ap.add_argument("--chay", nargs=4, type=int, help="tap x y de nhan vat di toi truoc khi quay (pixel man hinh 1920x1080)")
    ar = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    if ar.chay:
        adb(ar.serial, "shell", "input", "tap", str(ar.chay[0]), str(ar.chay[1]))
        time.sleep(0.8)
    adb(ar.serial, "shell", "rm", "-f", "/sdcard/muot.mp4")
    # ghi o do phan giai that, 3 giay; luc quay nhan vat dang chay
    adb(ar.serial, "shell", "screenrecord", "--size", "1920x1080", "--bit-rate", "20000000", "--time-limit", str(ar.giay), "/sdcard/muot.mp4", timeout=ar.giay + 30)
    mp4 = OUT / (ar.nhan + ".mp4")
    mp4.write_bytes(adb(ar.serial, "exec-out", "cat", "/sdcard/muot.mp4"))
    p = subprocess.run([FFMPEG, "-v", "error", "-i", str(mp4), "-fps_mode", "passthrough", "-vf", "scale=%d:%d,format=gray" % (W, H), "-f", "rawvideo", "-"],
                       capture_output=True, timeout=120)
    raw = p.stdout
    n = len(raw) // (W * H)
    frames = [raw[i * W * H:(i + 1) * W * H] for i in range(n)]
    x0, y0, bw, bh, r = 120, 220, 220, 200, 6  # mieng nen ben trai-giua (tranh HUD), tim +-6 px o 960x540
    mags, same = [], 0
    for a, b in zip(frames, frames[1:]):
        (dx, dy), sad = match(a, b, x0 + r, y0 + r, bw - 2 * r, bh - 2 * r, r)
        m = (dx * dx + dy * dy) ** 0.5
        mags.append(m)
        if m < 0.5:
            same += 1
    res = {"nhan": ar.nhan, "khung": n, "cap": len(mags), "dung_yen": same,
           "stand_pct": round(100.0 * same / max(1, len(mags)), 1),
           "dich_tb": round(statistics.mean(mags), 2) if mags else None,
           "dich_lech": round(statistics.pstdev(mags), 2) if mags else None,
           "cv": round(statistics.pstdev(mags) / statistics.mean(mags), 2) if mags and statistics.mean(mags) > 0 else None,
           "dich_theo_khung": [round(m, 1) for m in mags]}
    (OUT / (ar.nhan + ".json")).write_text(json.dumps(res), "utf8")
    print({k: v for k, v in res.items() if k != "dich_theo_khung"})


if __name__ == "__main__":
    main()
