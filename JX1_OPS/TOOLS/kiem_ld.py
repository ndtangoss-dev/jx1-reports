"""#200: liet ke cua so LDPlayer dang HIEN (chi doc, khong dong/go). In so luong; Tong quan ghi LD-HIEN vao SONNET-SONG.md."""
import ctypes
from ctypes import wintypes


def ld_hien():
    u = ctypes.windll.user32
    kq = []
    EP = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

    def cb(h, _):
        if u.IsWindowVisible(h) and not u.IsIconic(h):
            b = ctypes.create_unicode_buffer(256)
            u.GetWindowTextW(h, b, 256)
            c = ctypes.create_unicode_buffer(256)
            u.GetClassNameW(h, c, 256)
            if 'ldplayer' in b.value.lower() or 'ldplayer' in c.value.lower() or 'dnplayer' in c.value.lower():
                kq.append((b.value, c.value))
        return True
    u.EnumWindows(EP(cb), 0)
    return kq


if __name__ == '__main__':
    r = ld_hien()
    print(len(r))
    for t, c in r:
        print(t, '|', c)
