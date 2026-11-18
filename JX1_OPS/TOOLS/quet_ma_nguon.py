#!/usr/bin/env python
"""#143.3: quet ma nguon game (CHI DOC) -> bang mo ta bang chu vao JX1_OPS/MA-NGUON/.
Chay: python -I -X utf8 TOOLS/quet_ma_nguon.py
Khong sua ma game. Chi ghi vao thu muc ket qua. Khong chep exe/APK/khoa."""
import os, re, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'MA-NGUON')
BASE = r'C:\Jx1CocoV3'
CLIENT = glob.glob(os.path.join(BASE, 'Folder', 'Client2912*', 'Client2912', 'Client', 'Classes'))
SERVER = [os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline', 'gameserver', 'Sources'),
          os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline', 'gateway', 'Sources')]
PROTO = [os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline', 'gameserver', 'Headers', 'KProtocolDef.h'),
         os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline', 'gateway', 'Headers', 'KProtocolDef.h')]
EXT = ('.cpp', '.h', '.hpp', '.c', '.cc', '.mm')
SKIP = ('Release', 'Debug', 'Win32', '.git')

FUNC = re.compile(r'^[A-Za-z_][\w\s\*&:<>,~]*?\b((?:\w+::)?~?\w+)\s*\([^;{}]*\)\s*(?:const)?\s*$')
CALL = re.compile(r'\b([A-Za-z_]\w{3,})\s*\(')
KW = set('if for while switch return sizeof catch else do case new delete defined static_cast dynamic_cast reinterpret_cast const_cast'.split())


def rd(p):
    b = open(p, 'rb').read()
    for enc in ('utf-8', 'gbk'):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return b.decode('gbk', errors='replace')


def files(roots):
    for r in roots:
        for d, ds, fs in os.walk(r):
            ds[:] = [x for x in ds if x not in SKIP]
            for f in fs:
                if f.lower().endswith(EXT):
                    yield os.path.join(d, f)


def head_comment(t):
    for ln in t.splitlines()[:40]:
        s = ln.strip()
        m = re.match(r'(//+|/\*+|\*)\s*(.*)', s)
        if m and len(m.group(2).strip('*/ -=')) > 6 and not re.search(r'(?i)copyright|\$Id|filename|^file', m.group(2)):
            return m.group(2).strip('*/ ')[:100]
    return ''


def scan(roots, label, base):
    infos = {}
    defs = {}
    for p in files(roots):
        t = rd(p)
        rel = os.path.relpath(p, base).replace(os.sep, '/')
        fl = []
        lines = t.splitlines()
        for i, ln in enumerate(lines):
            if ln[:1] in (' ', '\t', '#', '/', '{', '}', '') or ln.startswith('//'):
                continue
            m = FUNC.match(ln.rstrip())
            if m and i + 1 < len(lines) and lines[i + 1].strip().startswith('{') or (m and ln.rstrip().endswith(')') and False):
                n = m.group(1)
                if n.split('::')[-1] not in KW:
                    fl.append(n)
                    defs.setdefault(n.split('::')[-1], rel)
        infos[rel] = (len(lines), head_comment(t), fl, t)
    out = ['# Bản đồ mã nguồn %s (tự sinh bởi TOOLS/quet_ma_nguon.py, chỉ đọc)' % label, '',
           'Mỗi tệp: số dòng, câu chú thích đầu, hàm định nghĩa (tối đa 25), hàm của dự án mà tệp gọi tới (tối đa 15, theo tần suất). "Gọi tới" chỉ khớp theo tên, chưa phân biệt trùng tên.', '']
    for rel in sorted(infos):
        n, hc, fl, t = infos[rel]
        calls = collections.Counter(c for c in CALL.findall(t) if c in defs and defs[c] != rel and c not in KW)
        out.append('## `%s`' % rel)
        out.append('- %d dòng. %s' % (n, hc or '(không có chú thích đầu)'))
        if fl:
            out.append('- Hàm: ' + ', '.join('`%s`' % f for f in fl[:25]) + (' …(+%d)' % (len(fl) - 25) if len(fl) > 25 else ''))
        if calls:
            out.append('- Gọi tới: ' + ', '.join('`%s`→%s' % (c, os.path.basename(defs[c])) for c, _ in calls.most_common(15)))
        out.append('')
    return out, infos


def protocols(allsrc):
    out = ['# Danh sách gói tin client↔server (tự sinh, chỉ đọc)', '',
           'Lấy từ các `enum *_PROTOCOL` trong `KProtocolDef.h` (gameserver và gateway). Mã gói = thứ tự trong enum (bắt đầu từ 0 nếu không gán). "Tệp dùng" là các tệp nguồn nhắc tới tên gói.', '']
    for p in PROTO:
        if not os.path.exists(p):
            continue
        t = rd(p)
        lab = 'gameserver' if 'gameserver' in p else 'gateway'
        for m in re.finditer(r'enum\s+(\w+)\s*\{(.*?)\n\};?', t, re.S):
            ename, body = m.group(1), m.group(2)
            if 'PROTOCOL' not in ename and ename not in ('relay_PROTOCOL',):
                continue
            out += ['## %s (%s)' % (ename, lab), '', '| Mã | Tên | Chú thích | Tệp dùng |', '|---|---|---|---|']
            idx = 0
            for ln in body.splitlines():
                ln = ln.strip()
                m2 = re.match(r'(\w+)\s*(?:=\s*([\w+x ]+))?\s*,?\s*(?://(.*))?$', ln)
                if not m2 or ln.startswith('//') or not ln:
                    continue
                name, val, cm = m2.group(1), m2.group(2), (m2.group(3) or '').strip()
                if val and re.fullmatch(r'\d+|0x[0-9a-fA-F]+', val.strip()):
                    idx = int(val.strip(), 0)
                users = [rel for rel, (_, _, _, tx) in allsrc.items() if name in tx][:4]
                out.append('| %d | `%s` | %s | %s |' % (idx, name, cm.replace('|', '/')[:60], ', '.join('`%s`' % os.path.basename(u) for u in users) or '-'))
                idx += 1
            out.append('')
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    allsrc = {}
    parts = []
    if CLIENT:
        o, inf = scan(CLIENT, 'client', CLIENT[0])
        parts.append(('client', o, len(inf)))
        allsrc.update({'client/' + k: v for k, v in inf.items()})
    base = os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline')
    o, inf = scan(SERVER, 'server (gameserver + gateway)', base)
    parts.append(('server', o, len(inf)))
    allsrc.update({'server/' + k: v for k, v in inf.items()})
    for name, o, n in parts:
        open(os.path.join(OUT, 'ban-do-%s.md' % name), 'w', encoding='utf-8', newline='\n').write('\n'.join(o) + '\n')
        print(name, n, 'tep')
    open(os.path.join(OUT, 'goi-tin.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(protocols(allsrc)) + '\n')
    open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8', newline='\n').write(
        '# MA-NGUON\n\nTự sinh bởi `TOOLS/quet_ma_nguon.py` (chỉ ĐỌC mã game, chỉ GHI vào thư mục này). Kho PUBLIC: chỉ bảng mô tả bằng chữ, không mã nguồn, không exe/APK, không khóa.\n\n'
        '- `ban-do-client.md`, `ban-do-server.md`: tệp nào làm gì, hàm nào gọi hàm nào (khớp theo tên).\n- `goi-tin.md`: bảng gói tin client↔server.\n- Chuỗi chữ và nhập khẩu của exe: `exe-chuoi.md` (TOOLS/quet_exe.py, làm sau).\n')


if __name__ == '__main__':
    main()
