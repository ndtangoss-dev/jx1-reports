"""Khu HIEU (M1.a): xem MA-NGUON/*.md va tim chu. Chi doc, chi trong thu muc MA-NGUON."""
import os, html


def _dir(goc):
    return os.path.join(goc, 'MA-NGUON')


def trang(goc, f='', q=''):
    d = _dir(goc)
    if not os.path.isdir(d):
        return '<h2>HIỂU</h2><div class="hop do">Chưa có thư mục MA-NGUON.</div>'
    ds = sorted(x for x in os.listdir(d) if x.lower().endswith('.md'))
    ds_html = ' · '.join('<a href="/khu/hieu?f=%s">%s</a>' % (html.escape(x), html.escape(x)) for x in ds)
    out = ['<h2>HIỂU — mã nguồn và gói tin</h2><p>%s</p>' % ds_html,
           '<form method="get" action="/khu/hieu"><input name="q" value="%s" placeholder="Tìm chữ (ví dụ: ping, KItem)"><input type="hidden" name="f" value="%s"><p><button>Tìm</button></p></form>' % (html.escape(q), html.escape(f))]
    if f:
        if os.path.basename(f) != f or f not in ds:
            return '<h2>HIỂU</h2><div class="hop do">Tên file không hợp lệ.</div>'
        dong = open(os.path.join(d, f), encoding='utf-8', errors='replace').read().splitlines()
        if q:
            kq = [(i + 1, l) for i, l in enumerate(dong) if q.lower() in l.lower()][:300]
            out.append('<h3>%s — %d dòng khớp (tối đa 300)</h3><pre>%s</pre>' % (html.escape(f), len(kq), html.escape('\n'.join('%d: %s' % x for x in kq))))
        else:
            out.append('<h3>%s</h3><pre>%s</pre>' % (html.escape(f), html.escape('\n'.join(dong[:400]))))
            if len(dong) > 400:
                out.append('<p><i>Chỉ hiện 400/%d dòng đầu; dùng ô Tìm.</i></p>' % len(dong))
    elif q:
        kq = []
        for x in ds:
            for i, l in enumerate(open(os.path.join(d, x), encoding='utf-8', errors='replace').read().splitlines()):
                if q.lower() in l.lower():
                    kq.append('%s:%d: %s' % (x, i + 1, l))
                    if len(kq) >= 300:
                        break
            if len(kq) >= 300:
                break
        out.append('<h3>%d dòng khớp (tối đa 300)</h3><pre>%s</pre>' % (len(kq), html.escape('\n'.join(kq))))
    return ''.join(out)
