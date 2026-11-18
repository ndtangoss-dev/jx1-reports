"""Khu HIEU (M1.b): loc goi tin tu MA-NGUON/goi-tin.md. Chi doc."""
import os, re, html


def doc(goc):
    f = os.path.join(goc, 'MA-NGUON', 'goi-tin.md')
    if not os.path.isfile(f):
        return []
    nhom, rows = '', []
    for l in open(f, encoding='utf-8', errors='replace').read().splitlines():
        if l.startswith('## '):
            nhom = l[3:].strip()
        elif l.startswith('|') and not l.startswith('|---') and not l.startswith('| Mã'):
            c = [x.strip() for x in l.strip('|').split('|')]
            if len(c) >= 4:
                rows.append((nhom, c[0], c[1].strip('`'), c[2], c[3]))
    return rows


def trang(goc, q='', nhom=''):
    rows = doc(goc)
    if not rows:
        return '<h2>Gói tin</h2><div class="hop do">Chưa có MA-NGUON/goi-tin.md.</div>'
    ds = sorted(set(r[0] for r in rows))
    opt = '<option value="">Tất cả nhóm</option>' + ''.join('<option%s>%s</option>' % (' selected' if x == nhom else '', html.escape(x)) for x in ds)
    out = ['<h2>HIỂU — gói tin (%d gói)</h2>' % len(rows),
           '<form method="get" action="/khu/goi"><input name="q" value="%s" placeholder="Tên, mã số hoặc chú thích (vd: ping, 33, 登录)"><select name="n">%s</select><p><button>Lọc</button></p></form>' % (html.escape(q), opt)]
    ql = q.lower()
    kq = [r for r in rows if (not nhom or r[0] == nhom) and (not ql or ql in r[2].lower() or ql == r[1] or ql in r[3].lower())]
    out.append('<p>%d gói khớp (hiện tối đa 200).</p><table><tr><th>Nhóm</th><th>Mã</th><th>Tên</th><th>Chú thích</th><th>Tệp dùng</th></tr>' % len(kq))
    for r in kq[:200]:
        out.append('<tr>' + ''.join('<td>%s</td>' % html.escape(x) for x in r) + '</tr>')
    out.append('</table>')
    return ''.join(out)
