#!/usr/bin/env python
"""Dat status trong front-matter TASKS/<ID>.md (#109). Dung: python -I TOOLS/set_status.py <ID> running|done|failed [ghi chu]
Goi tu chay_codex.ps1 (running), guard.ps1 (running lai / failed), buoc merge (done). Sau do sinh lai TIEN-DO.md."""
import os, re, subprocess, sys

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')


def main():
    if len(sys.argv) < 3:
        print('dung: set_status.py <ID> <status> [ghi chu]')
        return 2
    i, st = sys.argv[1], sys.argv[2]
    note = ' '.join(sys.argv[3:])
    p = os.path.join(ROOT, 'TASKS', i + '.md')
    s = open(p, encoding='utf-8').read()
    m = re.match(r'(---\s*\n)(.*?)(\n---)', s, re.S)
    if not m:
        print('khong co front-matter: ' + p)
        return 1
    body = m.group(2)
    line = 'status: ' + st
    if re.search(r'(?m)^status:.*$', body):
        body = re.sub(r'(?m)^status:.*$', line, body, count=1)
    else:
        body += '\n' + line
    if note:
        nl = 'status_note: "%s"' % note.replace('"', "'")
        if re.search(r'(?m)^status_note:.*$', body):
            body = re.sub(r'(?m)^status_note:.*$', nl, body, count=1)
        else:
            body += '\n' + nl
    open(p, 'w', encoding='utf-8', newline='\n').write(m.group(1) + body + m.group(3) + s[m.end():])
    subprocess.run([sys.executable, '-I', os.path.join(ROOT, 'TOOLS', 'tien_do.py')])
    print('%s -> %s' % (i, st))
    return 0


sys.exit(main())
