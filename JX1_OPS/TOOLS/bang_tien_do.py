#!/usr/bin/env python3
"""Dung "Bang tien do" (HTML, doc tren dien thoai) tu TASKS/BACKLOG.md, STATE/TRANG-THAI.md, STATE/KHOA.md.

Chay lai moi khi cap nhat cac file nay (hook post-commit cua kho goi script nay).
Trang thai task lay theo thu tu: bang "## Tien do task" trong TRANG-THAI.md > front matter TASKS/<ID>.md > "cho".
Chi doc nguon, chi ghi vao --out. Khong dua dia chi IP vao kho: IP doc tu <out>/config.json (khong commit).

  python bang_tien_do.py [--root JX1_OPS] [--out D:\\JX-dash]
"""
import argparse, html, json, os, re, shutil, sys, time, unicodedata

ST = {'xong': ('Xong', 'ok'), 'dang chay': ('Đang chạy', 'run'), 'cho': ('Chờ', 'wait'), 'loi': ('Lỗi', 'bad')}


def norm(s):
    s = unicodedata.normalize('NFD', s.lower().strip().strip('*').strip()).replace('đ', 'd')
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')
    s = re.sub(r'\s+', ' ', s)
    if s.startswith(('xong', 'done', 'dat')): return 'xong'
    if s.startswith(('dang', 'active', 'review', 'chay')): return 'dang chay'
    if s.startswith(('loi', 'blocked', 'ket', 'that bai')): return 'loi'
    return 'cho'


def read(p):
    try:
        return open(p, encoding='utf-8').read()
    except OSError:
        return ''


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def parse_backlog(text):
    phases, cur = [], None
    for ln in text.splitlines():
        m = re.match(r'##\s+(.*)', ln)
        if m:
            cur = {'name': m.group(1).strip(), 'tasks': []}; phases.append(cur); continue
        if cur is not None and ln.startswith('|'):
            c = cells(ln)
            if len(c) >= 2 and re.match(r'^[0-9A-Za-z]+-[0-9A-Za-z]+$', c[0]) and c[0] != 'ID':
                cur['tasks'].append({'id': c[0], 'title': c[1], 'who': c[3] if len(c) > 3 else ''})
    return [p for p in phases if p['tasks']]


def section(text, head):
    m = re.search(r'^##\s+' + head + r'.*?$\n(.*?)(?=^##\s|\Z)', text, re.S | re.M)
    return m.group(1) if m else ''


def status_table(state):
    out = {}
    for ln in section(state, 'Tiến độ task').splitlines():
        if ln.startswith('|'):
            c = cells(ln)
            if len(c) >= 2 and re.match(r'^[0-9A-Za-z]+-[0-9A-Za-z]+$', c[0]) and c[0] != 'ID':
                out[c[0]] = (norm(c[1]), c[2] if len(c) > 2 else '')
    return out


def front(root, tid):
    t = read(os.path.join(root, 'TASKS', tid + '.md'))
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    if m:
        d = re.search(r'^status:\s*([A-Za-z]+)', m.group(1), re.M)
        if d: return norm(d.group(1))
    return None


def workers(root, state):
    rows = []
    for ln in section(read(os.path.join(root, 'STATE', 'KHOA.md')), 'Đang giữ').splitlines():
        if ln.startswith('|'):
            c = cells(ln)
            if len(c) >= 4 and re.match(r'^[0-9A-Za-z]+-[0-9A-Za-z]+', c[0]) and c[0] != 'Task':
                rows.append({'task': c[0], 'who': c[1], 'res': c[3], 'since': c[4] if len(c) > 4 else ''})
    m = re.search(r'Worker đang chạy:\s*(.*)', state)
    return rows, (m.group(1).strip() if m else '')


def budget(state):
    b = section(state, 'Ngân sách Codex')
    caps = {'5h': 50, 'ngay': 200, '7ngay': 1000}
    used = None
    m = re.search(r'Đã dùng:\s*([\d.,]+)\s*USD\s*/\s*7 ngày', b)
    if m: used = float(m.group(1).replace('.', '').replace(',', '.'))
    exp = re.search(r'hết hạn\s*([\d/]+)', b)
    nw = re.search(r'Số worker hiện tại:\s*([^\n]+)', b)
    return {'used7': used, 'caps': caps, 'expiry': exp.group(1) if exp else '', 'workers': nw.group(1) if nw else ''}


CSS = """
:root{--bg:#f6f7f9;--card:#fff;--tx:#1b1f24;--mut:#5d6773;--bd:#dde1e6;--ok:#1a8f4a;--run:#1666d6;--wait:#8a929c;--bad:#d1342f;--okb:#e3f5ea;--runb:#e1ecfb;--waitb:#eceef1;--badb:#fbe5e4}
@media(prefers-color-scheme:dark){:root{--bg:#101316;--card:#1a1e23;--tx:#e8ebee;--mut:#9aa4af;--bd:#2c333b;--ok:#4cc57d;--run:#6aa6ff;--wait:#8d97a2;--bad:#ff7b76;--okb:#17301f;--runb:#16273f;--waitb:#242a31;--badb:#3a1c1b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;padding:12px 16px 40px;max-width:720px;margin-inline:auto}
h1{font-size:20px;margin:6px 0 2px}h2{font-size:16px;margin:0 0 8px}.sub{color:var(--mut);font-size:13px;margin-bottom:12px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px 14px;margin:0 0 12px}
.bar{height:10px;border-radius:6px;background:var(--waitb);overflow:hidden;display:flex}.bar i{display:block;height:100%}
.bar .ok{background:var(--ok)}.bar .run{background:var(--run)}.bar .bad{background:var(--bad)}
.row{display:flex;justify-content:space-between;gap:8px;font-size:14px;margin:0 0 6px}.row b{font-weight:600}.mut{color:var(--mut)}
.t{display:flex;gap:8px;align-items:flex-start;padding:8px 0;border-top:1px solid var(--bd);font-size:14px}.t:first-of-type{border-top:0}
.id{font-weight:700;min-width:44px}.tt{flex:1}.pill{font-size:12px;padding:2px 8px;border-radius:10px;white-space:nowrap}
.p-ok{background:var(--okb);color:var(--ok)}.p-run{background:var(--runb);color:var(--run)}.p-wait{background:var(--waitb);color:var(--wait)}.p-bad{background:var(--badb);color:var(--bad)}
.btns{display:flex;gap:10px;flex-wrap:wrap}.btn{flex:1;min-width:140px;text-align:center;padding:12px;border-radius:10px;background:var(--run);color:#fff;text-decoration:none;font-weight:600}
details summary{cursor:pointer;font-weight:600;list-style:none}.note{font-size:13px;color:var(--mut)}
"""


def build(root, out):
    backlog = read(os.path.join(root, 'TASKS', 'BACKLOG.md'))
    state = read(os.path.join(root, 'STATE', 'TRANG-THAI.md'))
    phases = parse_backlog(backlog)
    tbl = status_table(state)
    wk, wk_line = workers(root, state)
    bd = budget(state)
    cfg = {}
    try:
        cfg = json.load(open(os.path.join(out, 'config.json'), encoding='utf-8'))
    except (OSError, ValueError):
        pass
    tot = {'ok': 0, 'run': 0, 'wait': 0, 'bad': 0}
    ph_html = []
    for ph in phases:
        cnt = {'ok': 0, 'run': 0, 'wait': 0, 'bad': 0}
        rows = []
        for t in ph['tasks']:
            s, note = tbl.get(t['id'], (None, ''))
            s = s or front(root, t['id']) or 'cho'
            k = ST[s][1]; cnt[k] += 1; tot[k] += 1
            title = t['title']; title = title if len(title) < 140 else title[:137] + '...'
            rows.append('<div class="t"><span class="id">%s</span><span class="tt">%s%s</span><span class="pill p-%s">%s</span></div>' % (
                html.escape(t['id']), html.escape(title), ('<br><span class="note">%s</span>' % html.escape(note)) if note else '', k, ST[s][0]))
        n = len(ph['tasks']); pct = round(100 * cnt['ok'] / n)
        bar = '<div class="bar"><i class="ok" style="width:%.1f%%"></i><i class="run" style="width:%.1f%%"></i><i class="bad" style="width:%.1f%%"></i></div>' % (
            100 * cnt['ok'] / n, 100 * cnt['run'] / n, 100 * cnt['bad'] / n)
        op = ' open' if cnt['run'] or cnt['bad'] or (0 < cnt['ok'] < n) else ''
        ph_html.append('<div class="card"><details%s><summary><div class="row"><b>%s</b><span>%d%% · %d/%d</span></div>%s</summary><div style="margin-top:8px">%s</div></details></div>' % (
            op, html.escape(ph['name']), pct, cnt['ok'], n, bar, ''.join(rows)))
    n_all = sum(tot.values()) or 1
    allbar = '<div class="bar"><i class="ok" style="width:%.1f%%"></i><i class="run" style="width:%.1f%%"></i><i class="bad" style="width:%.1f%%"></i></div>' % (
        100 * tot['ok'] / n_all, 100 * tot['run'] / n_all, 100 * tot['bad'] / n_all)
    summary = '<div class="card"><div class="row"><b>Tổng</b><span>%d%% · %d/%d task xong</span></div>%s<div class="note" style="margin-top:8px"><span class="pill p-ok">Xong %d</span> <span class="pill p-run">Đang chạy %d</span> <span class="pill p-wait">Chờ %d</span> <span class="pill p-bad">Lỗi %d</span></div></div>' % (
        round(100 * tot['ok'] / n_all), tot['ok'], n_all, allbar, tot['ok'], tot['run'], tot['wait'], tot['bad'])
    if wk:
        w_html = ''.join('<div class="t"><span class="id">%s</span><span class="tt">%s<br><span class="note">%s%s</span></span></div>' % (
            html.escape(w['task']), html.escape(w['who']), html.escape(w['res']), (' · từ ' + html.escape(w['since'])) if w['since'] else '') for w in wk)
    else:
        w_html = ''
    w_html += '<div class="note">%s</div>' % html.escape('Worker Codex: ' + (wk_line or 'không có'))
    workers_card = '<div class="card"><h2>Worker đang làm gì</h2>%s</div>' % w_html
    if bd['used7'] is not None:
        c7 = bd['caps']['7ngay']; pc = min(100, 100 * bd['used7'] / c7)
        bud = '<div class="row"><span>Đã dùng 7 ngày</span><b>%g / %g USD</b></div><div class="bar"><i class="run" style="width:%.1f%%"></i></div>' % (bd['used7'], c7, pc)
    else:
        bud = '<div class="note">Chưa có số đo.</div>'
    bud += '<div class="note" style="margin-top:8px">Trần cứng: 50 USD/5 giờ · 200 USD/ngày · 1.000 USD/7 ngày%s. %s</div>' % (
        (' · khóa hết hạn ' + html.escape(bd['expiry'])) if bd['expiry'] else '', html.escape(('Worker: ' + bd['workers']) if bd['workers'] else ''))
    budget_card = '<div class="card"><h2>Ngân sách Codex</h2>%s</div>' % bud
    base = cfg.get('base', '')
    btn = ''
    if base:
        btn = '<div class="card"><h2>Sơ đồ Graphify</h2><div class="btns"><a class="btn" href="%s/graph-server.html">Sơ đồ server</a><a class="btn" href="%s/graph-client.html">Sơ đồ client</a></div><div class="note" style="margin-top:8px">Cần bật Tailscale trên điện thoại.</div></div>' % (html.escape(base), html.escape(base))
    else:
        btn = '<div class="card"><h2>Sơ đồ Graphify</h2><div class="note">Chưa cấu hình địa chỉ (config.json).</div></div>'
    now = time.strftime('%d/%m/%Y %H:%M')
    doc = ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>Bảng tiến độ JX1</title><style>%s</style></head><body><h1>Bảng tiến độ JX1</h1><div class="sub">Dựng lúc %s từ BACKLOG.md và TRANG-THAI.md</div>%s%s%s%s%s</body></html>') % (
        CSS, now, summary, ''.join(ph_html), workers_card, budget_card, btn)
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(doc)
    return tot


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument('--root', default=os.path.dirname(here))
    ap.add_argument('--out', default=r'D:\JX-dash')
    ap.add_argument('--graphs', action='store_true', help='chep graph.html server/client vao --out')
    a = ap.parse_args()
    root = a.root
    if not os.path.exists(os.path.join(root, 'TASKS', 'BACKLOG.md')):
        alt = os.path.join(root, 'JX1_OPS')
        if os.path.exists(os.path.join(alt, 'TASKS', 'BACKLOG.md')):
            root = alt  # chu cho nham thu muc cha: tu dung JX1_OPS
        else:
            raise SystemExit('LOI: khong thay TASKS/BACKLOG.md duoi --root=%s (dung --root <thu muc JX1_OPS>). KHONG ket luan "bang hong/mat" khi chua kiem tham so.' % a.root)
    tot = build(root, a.out)
    if not any(tot.values()):
        raise SystemExit('LOI: bang rong 0/0, kiem --root va TASKS/BACKLOG.md truoc khi bao.')
    if a.graphs:
        for src, name in ((r'D:\JX-build\src18\jxOnline\graphify-out\graph.html', 'graph-server.html'), (r'D:\Android\b\Client\Classes\graphify-out\graph.html', 'graph-client.html')):
            if os.path.exists(src): shutil.copy2(src, os.path.join(a.out, name))
    print('Da dung %s: %s' % (os.path.join(a.out, 'index.html'), tot))


if __name__ == '__main__':
    main()
