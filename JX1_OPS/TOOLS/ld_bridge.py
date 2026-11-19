"""Cầu adb danh sách trắng cho tiểu yêu tester (Q-70 mục A, #234).
Chạy trên máy thật (có adb). Tiểu yêu KHÔNG chạy adb; nó ghi lệnh JSON vào <thư mục>/lenh/<id>.json,
cầu chạy rồi ghi <thư mục>/ket-qua/<id>.json (+ <id>.png nếu chụp màn hình) và xóa lệnh.
Chỉ tới đúng MỘT emulator (--serial), chỉ các lệnh dưới đây, không shell tùy ý. Mọi lệnh ghi vào nhat-ky.log.
Lệnh: {"id":"001","cmd":"screenshot"} | tap x y | swipe x1 y1 x2 y2 ms | text "ascii" | key BACK|HOME|ENTER |
      start | stop | logcat n [bo-loc] | dnat (đặt lại DNAT 56722/51189/8080 sang host)
Chạy: python -I -X utf8 ld_bridge.py --serial emulator-5558 --dir D:\\JX-wt\\TS-02\\.ldbridge
Không có mật khẩu/khóa trong tệp; gõ chữ chỉ ASCII in được, tối đa 64 ký tự."""
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ADB = r"C:\LDPlayer\LDPlayer9\adb.exe"
PKG = "com.jxclient.hoiuctruyenky"
KEYS = {"BACK": 4, "HOME": 3, "ENTER": 66, "DEL": 67}
DNAT_DST = "100.95.186.86"
DNAT_TO = "192.168.56.101"
DNAT_PORTS = (56722, 51189, 8080)
INT = re.compile(r"^-?\d{1,5}$")


def adb(serial, *args, binary=False, timeout=30):
    p = subprocess.run([ADB, "-s", serial, *args], capture_output=True, timeout=timeout)
    return p.stdout if binary else p.stdout.decode("utf8", "replace") + p.stderr.decode("utf8", "replace")


def ints(a, n):
    if len(a) != n or not all(INT.fullmatch(str(x)) for x in a):
        raise ValueError("can %d so nguyen" % n)
    return [int(x) for x in a]


def run(serial, cmd, a, out, cid):
    if cmd == "screenshot":
        png = adb(serial, "exec-out", "screencap", "-p", binary=True)
        (out / (cid + ".png")).write_bytes(png)
        return "png %d byte" % len(png)
    if cmd == "tap":
        x, y = ints(a, 2)
        return adb(serial, "shell", "input", "tap", str(x), str(y)) or "ok"
    if cmd == "swipe":
        v = ints(a, 5)
        if not 50 <= v[4] <= 5000:
            raise ValueError("ms 50..5000")
        return adb(serial, "shell", "input", "swipe", *map(str, v)) or "ok"
    if cmd == "text":
        s = str(a[0]) if a else ""
        if not re.fullmatch(r"[A-Za-z0-9 ._@-]{1,64}", s):
            raise ValueError("chi ASCII A-Za-z0-9 ._@- toi da 64")
        # game (Cocos EditBox) rot/lon chu khi giao ca chuoi: go tung ky tu, cach 0.3 giay
        for ch in s:
            adb(serial, "shell", "input", "text", "%s" if ch == " " else ch)
            time.sleep(0.3)
        return "ok"
    if cmd == "key":
        if a[0] not in KEYS:
            raise ValueError("phim cho phep: " + ",".join(KEYS))
        return adb(serial, "shell", "input", "keyevent", str(KEYS[a[0]])) or "ok"
    if cmd == "start":
        return adb(serial, "shell", "monkey", "-p", PKG, "1")
    if cmd == "stop":
        return adb(serial, "shell", "am", "force-stop", PKG) or "ok"
    if cmd == "logcat":
        n = ints(a[:1], 1)[0]
        flt = str(a[1]) if len(a) > 1 else ""
        if not re.fullmatch(r"[A-Za-z0-9_.:-]{0,32}", flt) or not 1 <= n <= 500:
            raise ValueError("logcat n 1..500, bo loc ASCII ngan")
        txt = adb(serial, "logcat", "-d", "-t", str(n))
        return "\n".join(l for l in txt.splitlines() if flt in l)
    if cmd == "dnat":
        res = []
        for port in DNAT_PORTS:
            rule = "iptables -t nat -C OUTPUT -d %s -p tcp --dport %d -j DNAT --to-destination %s:%d" % (DNAT_DST, port, DNAT_TO, port)
            add = rule.replace(" -C ", " -A ")
            res.append(adb(serial, "shell", "su -c '%s || %s'" % (rule, add)) or "ok %d" % port)
        return "\n".join(res)
    raise ValueError("lenh khong co trong danh sach trang")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serial", required=True)
    ap.add_argument("--dir", required=True)
    ap.add_argument("--once", action="store_true")
    ar = ap.parse_args()
    if not re.fullmatch(r"emulator-\d{4}", ar.serial):
        sys.exit("serial phai la emulator-NNNN")
    root = Path(ar.dir)
    (root / "lenh").mkdir(parents=True, exist_ok=True)
    (root / "ket-qua").mkdir(exist_ok=True)
    log = root / "nhat-ky.log"
    while True:
        for f in sorted((root / "lenh").glob("*.json")):
            cid = re.sub(r"[^A-Za-z0-9_-]", "", f.stem)[:40] or "x"
            res = {"id": cid, "ok": False}
            try:
                c = json.loads(f.read_text("utf8"))
                cmd, a = c["cmd"], c.get("args", [])
                res["cmd"] = cmd
                res["out"] = run(ar.serial, cmd, a, root / "ket-qua", cid)
                res["ok"] = True
            except Exception as e:  # lỗi lệnh không làm sập cầu
                res["loi"] = "%s: %s" % (type(e).__name__, e)
            res["luc"] = time.strftime("%H:%M:%S")
            (root / "ket-qua" / (cid + ".json")).write_text(json.dumps(res, ensure_ascii=False), "utf8")
            with log.open("a", encoding="utf8") as lg:
                lg.write(json.dumps({k: res.get(k) for k in ("luc", "id", "cmd", "ok", "loi")}, ensure_ascii=False) + "\n")
            f.unlink()
        if ar.once:
            return
        time.sleep(1.0)


if __name__ == "__main__":
    main()
