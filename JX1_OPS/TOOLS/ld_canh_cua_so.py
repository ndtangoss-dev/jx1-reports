"""Bo canh nen (#236): vai giay quet mot lan, cua so LDPlayer/dnplayer nao dang hien va khong bi thu nho thi thu nho lai.
Chay: pythonw -I ld_canh_cua_so.py (khong cua so). Chi dung ctypes, khong dong vao tien trinh nao."""
import ctypes
import ctypes.wintypes as wt
import os
import time

u, k = ctypes.windll.user32, ctypes.windll.kernel32
SW_SHOWMINNOACTIVE = 7
EnumProc = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)


def exe_of(hwnd):
    pid = wt.DWORD()
    u.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    h = k.OpenProcessQuery = k.OpenProcess(0x1000, False, pid.value)
    if not h:
        return ""
    buf = ctypes.create_unicode_buffer(520)
    n = wt.DWORD(520)
    k.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(n))
    k.CloseHandle(h)
    return os.path.basename(buf.value).lower()


def sweep():
    out = []

    def cb(hwnd, _):
        if u.IsWindowVisible(hwnd) and not u.IsIconic(hwnd) and exe_of(hwnd) in ("dnplayer.exe", "ldplayer.exe", "ldplayerbox.exe"):
            u.ShowWindow(hwnd, SW_SHOWMINNOACTIVE)
            out.append(hwnd)
        return True

    u.EnumWindows(EnumProc(cb), 0)
    return out


if __name__ == "__main__":
    while True:
        try:
            sweep()
        except Exception:
            pass
        time.sleep(3)
