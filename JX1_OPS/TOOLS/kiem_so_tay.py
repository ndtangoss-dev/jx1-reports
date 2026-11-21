#!/usr/bin/env python
"""Kiem luat L20 (chu chot 21/11): bao cao cua A/B co chu XONG/DONE phai co dong 'DA DOC SO TAY: <tep>'
(hoac 'KHONG CO SO TAY ...'). Thieu thi ghi vao STATE/TRA-LAI-SO-TAY.md (Tong quan so huu, A/B doc dau moi luot).
Chi doc, chi ghi mot tep STATE. Dung: python kiem_so_tay.py [ROOT]   (mac dinh: cha cua TOOLS)
Moc: chi xet muc co gio >= L20_FROM trong ngay hien tai (tranh lam ngap muc cu)."""
import os, re, sys, time, hashlib

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [('A', 'HOP-THU/TU-SONNET.md'), ('B', 'HOP-THU/A-B.md')]
OUT = os.path.join(ROOT, 'STATE', 'TRA-LAI-SO-TAY.md')
NOTE = re.compile(r'(ĐÃ ĐỌC SỔ TAY|DA DOC SO TAY|KHÔNG CÓ SỔ TAY|KHONG CO SO TAY)', re.I)
DONE = re.compile(r'\b(XONG|DONE)\b', re.I)
OPS = re.compile(r'(đã đọc #|da doc #|ket-thuc-ca|kết thúc ca|tat may|tắt máy|/tiep-tuc|tiep-quan|tiếp quản|nhip tim|nhịp tim|kiểm tắt-bật|kiem tat-bat)', re.I)
HEAD = re.compile(r'^(#{2,4} |- \[\d|\*\*)')
GAME = re.compile(r'(cuong hoa|cường hóa|phi phong|phi phòng|ngua|ngựa|roi do|rơi đồ|quai|quái|boss|trang bi|trang bị|giat|giật|tick|ping|do ben|độ bền|tai phu|tài phú|goi tin|gói tin|giao dien|giao diện|ky nang|kỹ năng|nhiem vu|nhiệm vụ|bot)', re.I)
FROM_H = int(os.environ.get('L20_FROM_HOUR', '12'))   # moc "tu 12:00 ngay hom nay" (L20 hieu luc 11:46)


def entries(text):
    cur, out = [], []
    for ln in text.splitlines():
        if HEAD.match(ln) and cur:
            out.append('\n'.join(cur)); cur = []
        cur.append(ln)
    if cur:
        out.append('\n'.join(cur))
    return out


def stamp_ok(e):
    m = re.search(r'(\d{1,2})/(\d{1,2})\s+(\d{1,2}):(\d{2})', e[:200]) or re.search(r'\b(\d{1,2}):(\d{2})\b', e[:120])
    if not m:
        return True
    h = int(m.group(3)) if len(m.groups()) == 4 else int(m.group(1))
    return h >= FROM_H


def main():
    bad = []
    for who, rel in FILES:
        try:
            txt = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        except OSError:
            continue
        for e in entries(txt)[-25:]:
            if not DONE.search(e) or NOTE.search(e) or OPS.search(e[:600]) or not GAME.search(e) or not stamp_ok(e):
                continue
            bad.append((who, rel, e.strip().splitlines()[0][:140], hashlib.md5(e.encode('utf-8')).hexdigest()[:8]))
    lines = ['# TRẢ LẠI — báo cáo thiếu dòng "ĐÃ ĐỌC SỔ TAY" (L20) — Tổng quản tự sinh %s, đừng sửa tay' % time.strftime('%Y-%m-%d %H:%M'), '']
    if not bad:
        lines.append('Không có báo cáo nào đang thiếu.')
    else:
        lines.append('A/B đọc tệp này ĐẦU MỖI LƯỢT. Mục nào của mình: bổ sung dòng "ĐÃ ĐỌC SỔ TAY: <tệp trong HIEU-GAME/>" (hoặc "KHÔNG CÓ SỔ TAY cho phần này" + tạo mục thiếu trong hàng đợi) rồi mới được ghi XONG. Chưa bổ sung = trạng thái PARTIAL.')
        lines.append('')
        for who, rel, head, h in bad:
            lines.append('- [%s] %s — %s (mã %s)' % (who, rel, head, h))
    new = '\n'.join(lines) + '\n'
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    try:
        old = open(OUT, encoding='utf-8').read()
    except OSError:
        old = ''
    # chi ghi khi noi dung (khong tinh dong thoi gian) doi, de khong sinh commit rac
    strip = lambda s: '\n'.join(s.splitlines()[1:])
    if strip(old) != strip(new):
        open(OUT, 'w', encoding='utf-8', newline='\n').write(new)
    print('thieu=%d' % len(bad))


if __name__ == '__main__':
    main()
