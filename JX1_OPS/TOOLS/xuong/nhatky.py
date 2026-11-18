"""Nhật ký thao tác + lọc khóa/mật khẩu + sinh BUGS/XUONG-<số>.md."""
import os, re, time, subprocess, hashlib

DATA = os.environ.get('XUONG_DATA', r'D:\JX-xuong')
LOGDIR = os.path.join(DATA, 'logs')
ANHDIR = os.path.join(DATA, 'anh')

_BI_MAT = [
    (re.compile(r'(?i)\b(password|passwd|pwd|mat\s*khau|secret|token|api[_-]?key|bearer)\b\s*[:=]\s*\S+'), r'\1=***'),
    (re.compile(r'\bsk-[A-Za-z0-9_\-]{12,}'), 'sk-***'),
    (re.compile(r'(?i)(authorization:\s*)\S+(\s+\S+)?'), r'\1***'),
]


def loc(text):
    for rx, rep in _BI_MAT:
        text = rx.sub(rep, text)
    return text


def _file():
    os.makedirs(LOGDIR, exist_ok=True)
    return os.path.join(LOGDIR, time.strftime('%Y-%m-%d') + '.log')


def ghi(khu, thao_tac, loi=''):
    dong = '%s | %s | %s | %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), khu, loc(thao_tac), loc(loi).replace('\n', ' / '))
    try:
        with open(_file(), 'a', encoding='utf-8') as f:
            f.write(dong + '\n')
    except OSError:
        pass
    return dong


def cuoi(n=200):
    try:
        with open(_file(), encoding='utf-8') as f:
            return f.read().splitlines()[-n:]
    except OSError:
        return []


def chup_man_hinh(ten):
    """Chụp màn hình bằng PowerShell/System.Drawing (nếu có phiên desktop). Lưu ngoài kho."""
    os.makedirs(ANHDIR, exist_ok=True)
    p = os.path.join(ANHDIR, ten + '.png')
    ps = ("Add-Type -AssemblyName System.Windows.Forms,System.Drawing;"
          "$b=[System.Windows.Forms.SystemInformation]::VirtualScreen;"
          "$bmp=New-Object System.Drawing.Bitmap $b.Width,$b.Height;"
          "$g=[System.Drawing.Graphics]::FromImage($bmp);"
          "$g.CopyFromScreen($b.Left,$b.Top,0,0,$bmp.Size);"
          "$bmp.Save('%s')" % p.replace("'", "''"))
    try:
        subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, timeout=20)
    except Exception:
        return ''
    return p if os.path.exists(p) else ''


def bao_loi(thu_muc_bugs, version, trang, mo_ta):
    """Sinh BUGS/XUONG-NNN.md (đã lọc bí mật). Trả (đường dẫn file, mã)."""
    os.makedirs(thu_muc_bugs, exist_ok=True)
    so = 1
    for f in os.listdir(thu_muc_bugs):
        m = re.match(r'XUONG-(\d+)\.md$', f)
        if m:
            so = max(so, int(m.group(1)) + 1)
    ma = 'XUONG-%03d' % so
    anh = chup_man_hinh(ma)
    nd = ['# %s — báo lỗi từ Xưởng JX1' % ma, '',
          '- Giờ: ' + time.strftime('%Y-%m-%d %H:%M:%S'),
          '- Phiên bản Xưởng: ' + version,
          '- Trang đang mở: ' + loc(trang)[:200],
          '- Ảnh màn hình (không đưa lên kho): ' + (anh or '(không chụp được)'), '',
          '## Mô tả của người dùng', '', loc(mo_ta)[:4000] or '(trống)', '',
          '## 200 dòng nhật ký cuối (đã lọc khóa/mật khẩu)', '', '```'] + [loc(x) for x in cuoi(200)] + ['```', '']
    p = os.path.join(thu_muc_bugs, ma + '.md')
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(nd))
    ghi('BAO-LOI', 'tạo ' + ma)
    return p, ma


def ma_truy_cap():
    """Mã truy cập: biến môi trường XUONG_CODE, hoặc file D:\\JX-xuong\\ma.txt (tạo ngẫu nhiên, không ghi vào kho)."""
    m = os.environ.get('XUONG_CODE')
    if m:
        return m
    os.makedirs(DATA, exist_ok=True)
    p = os.path.join(DATA, 'ma.txt')
    if not os.path.exists(p):
        open(p, 'w').write(hashlib.sha256(os.urandom(32)).hexdigest()[:10])
    return open(p).read().strip()
