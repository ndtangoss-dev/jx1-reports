# MÔI TRƯỜNG THẬT

Lập 2026-11-16 bởi Sonnet PM (task 0-02). Chỉ dùng lệnh đọc. Nhãn: [XÁC MINH] = đã chạy lệnh hôm nay; [CHƯA KIỂM] = chưa.

## Máy thật
| Mục | Giá trị | Nhãn |
|---|---|---|
| RAM trống | khoảng 24 GB (tiến trình đang dùng khoảng 14 GB) | [XÁC MINH] |
| Ổ C | trống 140 GB / 476 GB | [XÁC MINH] |
| Ổ D | trống 1384 GB / 1863 GB | [XÁC MINH] |
| WMI/CIM | lỗi; dùng `[IO.DriveInfo]`, `Get-Counter` | [XÁC MINH] |
| Git | 2.56.0, credential helper hệ thống = `manager` (Git Credential Manager) | [XÁC MINH] |
| VirtualBox | 7.2.22 (`C:\Program Files\Oracle\VirtualBox\VBoxManage.exe`, không có trong PATH) | [XÁC MINH] |

## VM
| VM | Trạng thái | RAM/CPU | Mạng | MAC | Nhãn |
|---|---|---|---|---|---|
| `JX-Server-D` (Main) | **đang chạy** | 6144 MB / 4 | bridged | 080027AD6D3F | [XÁC MINH] |
| `JX-Server` (cũ) | tắt | chưa đọc | chưa đọc | chưa đọc | [XÁC MINH] chỉ về sự tồn tại |
| `JX-Test-36` (thử) | tắt, **không có snapshot** | 6144 MB / 4 | **bridged** | 080027CAE833 | [XÁC MINH] |

**Đính chính (đối chiếu `docs-analysis/reports/42-ke-hoach-vm-thu.md`, mục "Chuyển JX-Test-36 sang Bridged"):** bridged là chủ ý từ 2026-11-12, vì Host-only không cho máy thật và LDPlayer nối tới VM. IP trong VM thử là `192.168.1.150` (Main VM là `.50`), MAC khác nhau, nên không trùng. **Không đổi NIC.** Lưu ý còn mở theo báo cáo 42 [BÁO CÁO, chưa kiểm lại]: WinRM tới VM thử từng bị "Access denied" (user MU1, mật khẩu trống, chưa đặt mật khẩu); forwarder và portproxy trên máy thật vẫn trỏ `192.168.1.50`, nên đường Tailscale không tới VM thử; gs001 trong VM thử quảng bá IP Tailscale `100.95.186.86`. Hai VM bật cùng lúc cần đủ RAM (đủ: khoảng 24 GB trống).

Việc "VM thử chạy được server tự dựng 36 Hz" **[CHƯA KIỂM]**: chưa bật VM.

## Android
| Mục | Giá trị | Nhãn |
|---|---|---|
| LDPlayer | đang chạy (`dnplayer`), bản ở `D:\LDPlayer\LDPlayer9` và `C:\LDPlayer\LDPlayer9` | [XÁC MINH] |
| adb | `D:\Android\sdk\platform-tools\adb.exe`; `emulator-5554` ở trạng thái device | [XÁC MINH] |
| Client đã vá | `D:\Android\b\Client` | [XÁC MINH] thư mục tồn tại |
| APK mới nhất | `D:\Android\b\Client\proj.android\app\build\outputs\apk\debug\projectdebug-debug.apk`, 95.022.761 byte, sửa 14/11/2026 10:51 | [XÁC MINH] |
| APK trong LDPlayer là bản nào (P46/P47?) | chưa so | [CHƯA KIỂM] |
| Công cụ build | `D:\Android\{gradle-8.7,jdk,sdk}` | [XÁC MINH] tồn tại; chưa thử build |

## Codex CLI
| Mục | Giá trị | Nhãn |
|---|---|---|
| Không có trong PATH | | [XÁC MINH] |
| Tệp chạy được | `C:\Users\PC\.codex\.sandbox-bin\codex.exe` → `codex-cli 0.166.0-alpha.5.1` | [XÁC MINH] |
| Cấu hình | `C:\Users\PC\.codex\config.toml`; tôi không đọc nội dung và không sửa (giữ nguyên model và cấu hình theo Q-12) | [XÁC MINH] |
| `codex exec` nền, sandbox workspace-write, cấu hình xingchi có hoạt động không | chưa thử | [CHƯA KIỂM] (task 0-03, 0-09) |

## Việc kế tiếp từ kiểm kê này
1. 0-02b: bật `JX-Test-36` (bridged, `.150`), giải quyết WinRM/đăng nhập, kiểm server 36 Hz. Mật khẩu lấy từ Credential Manager, không ghi vào file.
2. 0-03: thử `codex exec` bằng đường dẫn đầy đủ ở trên.
3. Máy hiện chạy Main VM 6 GB; bật thêm VM thử 6 GB vẫn đủ RAM (khoảng 24 GB trống).
