#!/usr/bin/env python
"""Hook SessionStart/PreCompact cua Claude Code (#107.1-2, LUAT-COT-LOI L3).
  start      : in LUAT-COT-LOI.md vao ngu canh (startup, resume).
  postcompact: in LUAT-COT-LOI.md, roi TIEN-DO.md, THU-HIEN-HANH.md, QUYET-DINH.md (duoi) theo thu tu L3, kem nhac doc lich su chat.
  precompact : ghi khoi "DANG LAM DO" vao STATE/TRANG-THAI.md, commit, push nhanh jx1-ops. Loi bat ky -> khong chan.
"""
import os, subprocess, sys, time

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
REPO = os.path.dirname(ROOT)
NL = chr(10)


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
        import re, glob
        stamp = time.strftime('%Y-%m-%d %H:%M')
        run = []
        for f in sorted(glob.glob(os.path.join(ROOT, 'TASKS', '*.md'))):
            try:
                t = open(f, encoding='utf-8').read(1500)
            except OSError:
                continue
            if re.search(r'(?m)^status:\s*(running|in_progress|doing)', t):
                run.append(os.path.basename(f)[:-3])
        lastn = '(không rõ)'
        try:
            tus = open(os.path.join(ROOT, 'HOP-THU', 'TU-SONNET.md'), encoding='utf-8').read()
            m = re.findall(r'Nhận #(\d+)', tus)
            if m:
                lastn = '#' + max(m, key=int)
        except OSError:
            pass
        p = os.path.join(ROOT, 'STATE', 'BAN-GIAO.md')
        s = open(p, encoding='utf-8').read()
        a2 = s.index('## Bản bàn giao hiện tại')
        b2 = s.index(NL + '## ', a2 + 5)
        blk = NL.join(['## Bản bàn giao hiện tại',
                       '- Thời điểm: %s (hook PreCompact tự ghi đè)' % stamp,
                       '- Việc đang chạy (TASKS status running): %s' % (', '.join(run) or '(không)'),
                       '- Thư cuối đã nhận: %s' % lastn,
                       '- Sắp nén ngữ cảnh: PM mới đọc LUAT-COT-LOI.md, TIEN-DO.md, THU-HIEN-HANH.md, QUYET-DINH.md rồi lịch sử chat; chi tiết việc dở ở dòng trạng thái cuối TRANG-THAI.md.']) + NL
        open(p, 'w', encoding='utf-8', newline=NL).write(s[:a2] + blk + s[b2:])
        git('add', 'JX1_OPS/STATE/BAN-GIAO.md')
        git('commit', '-m', 'PreCompact: ghi de BAN-GIAO\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>')
        git('push', 'origin', 'HEAD')


try:
    main()
except Exception as e:
    print('[hook_luat loi: %s]' % e)
sys.exit(0)
