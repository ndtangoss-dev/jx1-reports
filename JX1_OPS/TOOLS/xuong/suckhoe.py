"""Khu Sức khỏe (M0): kiểm đường dẫn, Python, git, adb, VM. Chỉ ĐỌC, không sửa gì."""
import os, sys, glob, shutil, subprocess

BASE = r'C:\Jx1CocoV3'
DUONG_DAN = [
    ('Kho vận hành (jx1-ops)', None),
    ('Mã client', glob.glob(os.path.join(BASE, 'Folder', 'Client2912*', 'Client2912', 'Client', 'Classes'))),
    ('Mã server (gameserver)', [os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline', 'gameserver', 'Sources')]),
    ('Mã server (gateway)', [os.path.join(BASE, 'SwordOnline', 'SwordOnline', 'jxOnline', 'gateway', 'Sources')]),
    ('Bản A client (qh9A)', [r'D:\JX-build\qh9A']),
    ('Công cụ Android', [r'D:\Android']),
]
VBOX = r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'


def _chay(args, timeout=15):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:  # noqa
        return -1, str(e)


def kiem_tra(goc_kho):
    """Trả danh sách (ten, trang_thai['xanh'|'vang'|'do'], ghi_chu)."""
    kq = []
    v = sys.version_info
    kq.append(('Python', 'xanh' if v >= (3, 8) else 'do', '%d.%d.%d' % v[:3]))
    for ten, ds in DUONG_DAN:
        if ds is None:
            ok = os.path.isdir(goc_kho)
            kq.append((ten, 'xanh' if ok else 'do', goc_kho))
        else:
            ok = [d for d in ds if os.path.isdir(d)]
            kq.append((ten, 'xanh' if ok else 'do', ok[0] if ok else 'không thấy: ' + (ds[0] if ds else '(không có)')))
    git = shutil.which('git')
    if git:
        c, o = _chay([git, '--version'])
        kq.append(('git', 'xanh' if c == 0 else 'do', o.splitlines()[0] if o else ''))
    else:
        kq.append(('git', 'do', 'không có trong PATH'))
    adb = shutil.which('adb') or next(iter(glob.glob(r'D:\Android\**\adb.exe', recursive=True)), None)
    if adb:
        c, o = _chay([adb, 'version'])
        kq.append(('adb', 'xanh' if c == 0 else 'vang', adb))
    else:
        kq.append(('adb', 'vang', 'chưa tìm thấy adb.exe (cần cho khu Build)'))
    if os.path.exists(VBOX):
        c, o = _chay([VBOX, 'list', 'runningvms'])
        if c == 0:
            vm = [l.split('"')[1] for l in o.splitlines() if '"' in l]
            kq.append(('VM đang chạy', 'xanh' if vm else 'vang', ', '.join(vm) or 'không có VM nào đang chạy'))
        else:
            kq.append(('VM đang chạy', 'vang', 'không đọc được: ' + o[:80]))
    else:
        kq.append(('VM đang chạy', 'vang', 'không thấy VBoxManage'))
    return kq
