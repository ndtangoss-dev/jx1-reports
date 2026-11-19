"""Kiem nhanh "duong vao" Test-36 (B-034): in MOT dong ket qua + ma thoat (0 = SAN SANG, 1 = CHUA).
Chi doc: netstat, tailscale ping, forwarder.log, vm_chay chain-up (idempotent, chi kiem tra neu chuoi da song).
Chay: python -I -X utf8 kiem_duong_vao.py [--ip-pc 100.95.186.86] [--phone 100.123.183.6] [--bo-qua-vm]"""
import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FWD_DIR = r"C:\Jx1CocoV3\docs-analysis"
FWD_SCRIPT = os.path.join(FWD_DIR, "scripts", "tcp_forwarder.py")
FWD_LOG = os.path.join(FWD_DIR, "out", "forwarder.log")
PORTS = (56722, 51189)
DICH_T36 = "192.168.56.150"
DICH_D = "192.168.1.50"


def run(cmd, timeout=60):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=timeout).stdout
    except Exception as e:  # noqa: BLE001
        return "ERR %s" % e


def forwarder(ip_pc):
    net = run(["netstat", "-ano"])
    pids = {}
    for p in PORTS:
        m = re.search(r"%s:%d\s+\S+\s+LISTENING\s+(\d+)" % (re.escape(ip_pc), p), net)
        pids[p] = m.group(1) if m else None
    if not all(pids.values()):
        return False, "forwarder KHONG nghe %s" % ",".join(str(p) for p in PORTS if not pids[p])
    pid = pids[PORTS[0]]
    st = run(["powershell", "-NoProfile", "-Command",
              "(Get-Process -Id %s).StartTime.ToString('s')" % pid]).strip()
    dich = None
    if os.path.exists(FWD_LOG):
        raw = open(FWD_LOG, "rb").read()
        txt = raw.decode("utf-16" if (raw[:2] in (bytes([255,254]), bytes([254,255])) or bytes(1) in raw[:64]) else "utf-8", errors="replace")
        for line in txt.splitlines():
            m = re.search(r"NGHE \S+:56722 -> (\S+):56722", line)
            if m:
                dich = m.group(1)
    if dich == DICH_D:
        return False, "forwarder pid %s tro Server D (vung do) -> chay CHAY-CHUYEN-T36.bat" % pid
    if dich != DICH_T36:
        return False, "forwarder pid %s dich la %s (khong phai Test-36)" % (pid, dich)
    cu = ""
    try:
        mt = os.path.getmtime(FWD_SCRIPT)
        import datetime
        if st and datetime.datetime.fromisoformat(st).timestamp() < mt:
            cu = ", MA CU (forwarder bat truoc khi sua tcp_forwarder.py) -> chay lai CHAY-CHUYEN-T36.bat"
    except Exception:  # noqa: BLE001
        pass
    return True, "forwarder pid %s -> Test-36 bat %s%s" % (pid, st, cu)


def tailscale(phone):
    st = run(["tailscale", "status"])
    line = next((l for l in st.splitlines() if phone in l), "")
    if not line:
        return None, "dien thoai khong co trong tailscale"
    if "offline" in line:
        return None, "dien thoai offline tren tailscale"
    out = run(["tailscale", "ping", "-c", "3", "--timeout", "3s", phone], 40)
    m = re.findall(r"pong from .*? via (\S+) in (\d+)ms", out)
    if not m:
        return None, "tailscale ping khong tra loi"
    via, ms = m[-1]
    kind = "RELAY/DERP" if "DERP" in via.upper() else "TRUC TIEP"
    return kind == "TRUC TIEP", "tailscale %s %sms" % (kind, ms)


def vm():
    out = run([sys.executable, "-I", "-X", "utf8", os.path.join(HERE, "vm_chay.py"), "chain-up"], 150)
    if "CHUOI LEN DU" in out or "da noi du" in out:
        return True, "gs001 da noi du"
    return False, "gs001/chuoi CHUA du (dang nap ban do ~10 phut?)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ip-pc", default="100.95.186.86")
    ap.add_argument("--phone", default="100.123.183.6")
    ap.add_argument("--bo-qua-vm", action="store_true")
    a = ap.parse_args()
    ok_f, m_f = forwarder(a.ip_pc)
    ok_v, m_v = (True, "bo qua vm") if a.bo_qua_vm else vm()
    ok_t, m_t = tailscale(a.phone)
    # ok_t None = chua do duoc (dien thoai offline): khong tinh la loi may, chi canh bao
    san_sang = ok_f and ok_v
    print("%s | %s | %s | %s" % ("SAN SANG" if san_sang else "CHUA SAN SANG", m_f, m_v, m_t))
    return 0 if san_sang else 1


if __name__ == "__main__":
    sys.exit(main())
