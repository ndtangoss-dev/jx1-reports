#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CHO THU DAI (Chat viet 18/11/2026 theo Q-54): lenh CHO xac dinh cho Sonnet, KHONG ton token.
Sonnet chay lenh nay thay cho tu viet vong ngu. Lenh chi tra quyen cho Sonnet khi:
  - co thu moi cua Chat (dong CHAT-DAY moi trong VONG.md hoac muc moi trong CHO-SONNET.md)  -> exit 10
  - Tong quan bao co viec cho gop (XONG-CHO-GOP trong STATE/TIEU-YEU.md)                   -> exit 11
  - het han toi da (--phut, mac dinh 9; Bash Claude Code chi cho <=10 phut)                                                    -> exit 12
Moi --nhip phut (mac dinh 5) lenh GHI nhip tim vao HOP-THU/NHIP-TIM.md va day len kho de
Chat/chu thay Sonnet con song. Chay:  python TOOLS/cho_thu.py [--phut 9] [--nhip 5] [--dry]
Chay tu thu muc goc repo van hanh (nhanh jx1-ops). Chi dung git fetch/commit --only, KHONG dong cay lam viec.
"""
import argparse, datetime, os, re, subprocess, sys, time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
VONG = 'JX1_OPS/HOP-THU/VONG.md'
CHO = 'JX1_OPS/HOP-THU/CHO-SONNET.md'
TY = 'JX1_OPS/STATE/TIEU-YEU.md'
NHIP = 'JX1_OPS/HOP-THU/NHIP-TIM.md'
BR = 'jx1-ops'
# Q-75: JX1_SONNET=B -> hop thu rieng cua Sonnet B (mac dinh A, khong doi hanh vi)
B = os.environ.get('JX1_SONNET', 'A').upper() == 'B'
if B:
    CHO = 'JX1_OPS/HOP-THU/CHO-SONNET-B.md'
    NHIP = 'JX1_OPS/HOP-THU/NHIP-TIM-B.md'
DAY_RE = r'CHAT-DAY-B #(\d+)' if B else r'CHAT-DAY #(\d+)'
LET_RE = r'^## #B-\d+' if B else r'^## #\d+'

def git(*a, check=False):
    r = subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    return r.returncode, (r.stdout or '')

def show(path):
    rc, out = git('show', f'origin/{BR}:{path}')
    return out if rc == 0 else ''

def max_chat_day(txt):
    n = [int(m) for m in re.findall(DAY_RE, txt)]
    return max(n) if n else 0

def n_letters(txt):
    return len(re.findall(LET_RE, txt, flags=re.M))

def co_gop(txt):
    """#250: chi tinh viec XONG-CHO-GOP co owner trung voi JX1_SONNET (mac dinh A; task khong ghi owner = A)."""
    me = os.environ.get('JX1_SONNET', 'A').upper()
    for m in re.finditer(r'^\|\s*([^|\s]+)\s*\|\s*XONG-CHO-GOP\s*\|', txt, re.M):
        owner = 'A'
        try:
            t = open(os.path.join(REPO, 'JX1_OPS', 'TASKS', m.group(1) + '.md'), encoding='utf-8').read(2000)
            o = re.search(r'^owner:\s*([AB])', t, re.M)
            owner = o.group(1) if o else 'A'
        except OSError:
            pass
        if owner == me:
            return True
    return False

def nhip(msg, dry):
    now = datetime.datetime.now().strftime('%d/%m %H:%M:%S')
    path = os.path.join(REPO, NHIP.replace('/', os.sep))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'# NHIP TIM Sonnet (cho_thu.py)\nLan cuoi: {now}\nTrang thai: {msg}\n')
    if dry:
        print('[dry] ghi nhip tim', now); return
    git('add', '--', NHIP)
    git('commit', '--only', '-m', f'Nhip tim Sonnet {now}', '--', NHIP)
    for _ in range(2):
        git('fetch', '-q', 'origin', BR)
        rc, _o = git('push', '-q', 'origin', f'HEAD:{BR}')
        if rc == 0:
            break
        git('pull', '--rebase', '--autostash', '-q', 'origin', BR)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--phut', type=int, default=9)  # 19/11: lenh Bash cua Claude Code toi da 10 phut -> 9
    ap.add_argument('--nhip', type=int, default=5)
    ap.add_argument('--giay', type=int, default=60)
    ap.add_argument('--dry', action='store_true')
    a = ap.parse_args()
    git('fetch', '-q', 'origin', BR)
    base_day = max_chat_day(show(VONG))
    base_let = n_letters(show(CHO))
    t0 = time.time(); last = None
    print(f'cho_thu: bat dau, CHAT-DAY cuoi=#{base_day}, so thu={base_let}, toi da {a.phut} phut', flush=True)
    while True:
        el = (time.time() - t0) / 60
        if last is None or el - last >= a.nhip:
            nhip(f'dang cho thu moi, da cho {int(el)} phut (CHAT-DAY cuoi #{base_day})', a.dry); last = el
        git('fetch', '-q', 'origin', BR)
        d, l = max_chat_day(show(VONG)), n_letters(show(CHO))
        if d > base_day or l > base_let:
            print(f'THU MOI: CHAT-DAY #{d}, so thu {l}. Hay: git pull --rebase --autostash, doc thu, lam.', flush=True); sys.exit(10)
        if co_gop(show(TY)):
            print('CO VIEC CHO GOP (XONG-CHO-GOP trong TIEU-YEU.md). Hay gop.', flush=True); sys.exit(11)
        if el >= a.phut:
            print(f'HET HAN {a.phut} phut, khong co thu moi.', flush=True); sys.exit(12)
        if a.dry and el >= 0.02:
            print('[dry] ket thuc thu'); sys.exit(0)
        time.sleep(a.giay if not a.dry else 1)

if __name__ == '__main__':
    main()
