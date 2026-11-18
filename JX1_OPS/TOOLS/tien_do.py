#!/usr/bin/env python
"""Sinh STATE/TIEN-DO.md tu front-matter TASKS/*.md (#107.5, L4): 3 dong dau DANG LAM / KE TIEP / BI CHAN + so do Mermaid <=30 nut.
Chay: python -I TOOLS/tien_do.py   (moi lan push va moi lan guard chay). Chi doc TASKS, ghi mot file STATE/TIEN-DO.md."""
import glob, os, re, time

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
RUN = ('running', 'dang chay', 'in_progress', 'doing')
DONE = ('done', 'xong', 'merged', 'closed', 'superseded', 'active')  # active = bao cao cu dang dung, khong phai viec ke tiep
BLOCK = ('blocked', 'bi chan', 'cho chu')


def front(p):
    try:
        s = open(p, encoding='utf-8').read()
    except OSError:
        return None
    m = re.match(r'---\s*\n(.*?)\n---', s, re.S)
    if not m:
        return None
    d = {}
    for ln in m.group(1).splitlines():
        k, _, v = ln.partition(':')
        if _:
            d[k.strip()] = v.strip().strip('"')
    return d


def stage(t):
    i = t['id']
    if i.startswith(('R-', 'S-', 'K-', 'U-01', 'A-')):
        return 1  # hieu game / chuan hoa
    if i.startswith(('U-02', 'T-', 'N-')):
        return 2  # duong truyen + exe
    return 3      # tick / do phan hoi / do hoa


def main():
    tasks = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'TASKS', '*.md'))):
        if os.path.basename(p).startswith('_'):
            continue  # _MAU-TASK.md la mau
        d = front(p)
        if d and d.get('id'):
            d['st'] = d.get('status', '').lower()
            d['title'] = d.get('title', '')
            tasks.append(d)
    byid = {t['id']: t for t in tasks}
    # #109: doi chieu dau .done cua worker (D:\JX-wt\<ID>.done): exit!=0 -> chet, exit=0 -> cho gop
    for t in tasks:
        t['dead'] = t['merge'] = False
        if t['st'] in RUN:
            try:
                x = re.sub(r'[^ -~]', '', open(r'D:\JX-wt\%s.done' % t['id'], encoding='utf-16' if False else 'utf-8', errors='ignore').read())
                t['merge' if 'exit=0' in x else 'dead'] = True
            except OSError:
                pass
    run = [t for t in tasks if t['st'] in RUN and not t['dead'] and not t['merge']]
    dead = [t for t in tasks if t['dead']]
    merge = [t for t in tasks if t['merge']]
    todo = [t for t in tasks if t['st'] not in DONE + RUN + BLOCK]
    blk = [t for t in tasks if t['st'] in BLOCK]
    fmt = lambda L: ', '.join('%s' % t['id'] for t in L) or '(không)'
    out = ['# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc %s, đừng sửa tay)' % time.strftime('%Y-%m-%d %H:%M'), '',
           'ĐANG LÀM: ' + fmt(run), 'KẾ TIẾP: ' + fmt(todo[:6]), 'BỊ CHẶN: ' + fmt(blk), '',
           'Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.', '']
    shown = (run + dead + merge + blk + todo)[:30]
    out += ['```mermaid', 'flowchart LR']
    for n, name in ((1, 'Chặng 1 hiểu game'), (2, 'Chặng 2 truyền tải + exe'), (3, 'Chặng 3 tick và đồ họa')):
        out.append('  subgraph S%d["%s"]' % (n, name))
        for t in shown:
            if stage(t) == n:
                lab = t['id'].replace('-', '_')
                mark = 'chạy' if t in run else ('chết' if t in dead else ('chờ gộp' if t in merge else ('chặn' if t in blk else 'chờ')))
                out.append('    %s["%s %s"]' % (lab, t['id'], mark))
        out.append('  end')
    for t in shown:
        for dep in re.findall(r'[A-Z0-9]+-[0-9a-z]+', t.get('depends_on', '')):
            if dep in byid and byid[dep] in shown:
                out.append('  %s --> %s' % (dep.replace('-', '_'), t['id'].replace('-', '_')))
    out += ['```', '', 'Tổng: %d việc, %d đang làm (+%d chết, %d chờ gộp), %d chờ, %d bị chặn, %d xong.' % (len(tasks), len(run), len(dead), len(merge), len(todo), len(blk), len([t for t in tasks if t['st'] in DONE])), '']
    open(os.path.join(ROOT, 'STATE', 'TIEN-DO.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out))


if __name__ == '__main__':
    main()
