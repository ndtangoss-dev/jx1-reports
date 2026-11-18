#!/usr/bin/env python
"""Hook SessionStart/PreCompact cua Claude Code (#107.1-2, LUAT-COT-LOI L3).
  start      : in LUAT-COT-LOI.md vao ngu canh (startup, resume).
  postcompact: in LUAT-COT-LOI.md, roi TIEN-DO.md, THU-HIEN-HANH.md, QUYET-DINH.md (duoi) theo thu tu L3, kem nhac doc lich su chat.
  precompact : ghi khoi "DANG LAM DO" vao STATE/TRANG-THAI.md, commit, push nhanh jx1-ops. Loi bat ky -> khong chan.
"""
import os, subprocess, sys, time

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
REPO = os.path.dirname(ROOT)


def show(rel, tail=None):
    p = os.path.join(ROOT, rel)
    try:
        s = open(p, encoding='utf-8').read()
    except OSError:
        print('[khong doc duoc %s]' % rel)
        return
    if tail and len(s) > tail:
        s = '...\n' + s[-tail:]
    print('===== %s =====\n%s' % (rel, s))


def git(*a):
    return subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True, timeout=40)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'start'
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if mode == 'start':
        print('DOC LUAT COT LOI TRUOC MOI VIEC (JX1_OPS/STATE/LUAT-COT-LOI.md):')
        show('STATE/LUAT-COT-LOI.md')
    elif mode == 'postcompact':
        print('NGU CANH VUA BI NEN. Doc theo thu tu L3: LUAT-COT-LOI -> TIEN-DO -> THU-HIEN-HANH + thu moi -> QUYET-DINH -> lich su chat jsonl (tu lan push cuoi tru 15 phut, 60 phut-3 gio, chi loi chu va tra loi cuoi cua PM).')
        show('STATE/LUAT-COT-LOI.md')
        show('STATE/TIEN-DO.md', 4000)
        show('HOP-THU/THU-HIEN-HANH.md', 6000)
        show('STATE/QUYET-DINH.md', 3000)
        show('STATE/TRANG-THAI.md', 3000)
    elif mode == 'precompact':
        p = os.path.join(ROOT, 'STATE', 'TRANG-THAI.md')
        stamp = time.strftime('%Y-%m-%d %H:%M')
        blk = ('\n## ĐANG LÀM DỞ (%s, hook PreCompact)\n'
               '- Sắp nén ngữ cảnh. PM mới đọc LUAT-COT-LOI.md, TIEN-DO.md, THU-HIEN-HANH.md, QUYET-DINH.md rồi lịch sử chat.\n'
               '- Việc đang dở, bước và lệnh chạy lại: xem dòng trạng thái cuối trong TRANG-THAI.md và TASKS/*.md (status running); PM ghi chi tiết ở đây nếu kịp.\n' % stamp)
        with open(p, 'a', encoding='utf-8') as f:
            f.write(blk)
        git('add', 'JX1_OPS/STATE/TRANG-THAI.md')
        git('commit', '-m', 'PreCompact: ghi DANG LAM DO\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>')
        git('push', 'origin', 'HEAD')


try:
    main()
except Exception as e:
    print('[hook_luat loi: %s]' % e)
sys.exit(0)
