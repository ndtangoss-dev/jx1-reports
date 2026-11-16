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
| `JX-Server-D` (Main) | **aborted** lúc 20:13 (giờ máy) ngày 16/11; không do tôi tắt; chưa bật lại | 6144 MB / 4 | bridged (cấu hình cũ, chưa đổi; không bật khi chưa được phép) | 080027AD6D3F | [XÁC MINH] 20:55 |
| `JX-Server` (cũ) | tắt | chưa đọc | chưa đọc | chưa đọc | [XÁC MINH] chỉ về sự tồn tại |
| `JX-Test-36` (thử) | **đang chạy** (VBox báo running; không có snapshot) | 6144 MB / 4 | **Host-only** (chuyển lúc đang chạy ngày 16/11 khoảng 20:35; trước đó bridged từ 12/11) | 080027CAE833 | [XÁC MINH] 20:55 |

**Quyết định Q-17:** không bật VM nào ở chế độ bridged khi chủ dự án chưa cho phép. Bridged từ 12/11 là chủ ý cũ (báo cáo 42) nhưng đã bị bỏ.

### Kiểm tra mạng bên trong `JX-Test-36` (2026-11-16 20:40, đọc từ màn hình VM) [XÁC MINH]
| Mục | Giá trị |
|---|---|
| Card | Intel PRO/1000 MT, MAC `08-00-27-CA-E8-33` |
| IP | tĩnh `192.168.1.150`, DHCP tắt |
| Gateway | **không có** |
| DNS | `192.168.1.1` (router/mesh) |
| Dịch vụ chia sẻ mạng | ICS (`SharedAccess`, `icssvc`) và `RemoteAccess` đều Stopped; không có dịch vụ DHCP/DNS server; không có portproxy |
| Tên máy Windows | `DESKTOP-KT7DU78` (máy thật là `DESKTOP-5NGFN70`, khác). Main VM là bản gốc của bản sao này nên **có khả năng cao trùng tên** [GIẢ THUYẾT, chưa kiểm vì Main VM đang aborted] |

**Kết luận về nguyên nhân [CHƯA XÁC ĐỊNH]:** trong VM không có thứ gì tự chia sẻ mạng hay cấp DHCP. Hai giả thuyết còn lại, chưa kiểm chứng: (1) tên máy trùng với Main VM (NetBIOS, LLMNR, mDNS) cùng DUID DHCPv6 trùng vì là bản sao; (2) hai card ảo bridged cùng nối vào một card Realtek của máy thật và phát quảng bá, hoặc router ghi nhận IP `.150` lạ. Không loại trừ nguyên nhân khác ngoài VM.

**Chưa khớp lời kể:** chủ dự án nói đã tắt VM thử, nhưng VBox báo `JX-Test-36` vẫn **running** lúc 20:30, còn `JX-Server-D` (Main) ở trạng thái **aborted** lúc 20:13. Có khả năng đã tắt nhầm Main VM. Tôi không tắt VM nào; tôi chỉ chuyển card của VM thử sang Host-only lúc đang chạy để cắt ngay đường ra LAN.

### Đề xuất mạng VM thử (chờ duyệt, vùng Đỏ mục 5)
Báo cáo 42: lỗi cũ do VM đặt `192.168.1.150` trong khi card Host-only của máy thật chỉ có `169.254.83.226` (lệch dải). Đề xuất dùng dải riêng **`192.168.56.0/24`**, không trùng LAN nhà:
1. Máy thật: **không cần đổi gì.** Card "VirtualBox Host-Only Ethernet Adapter" (tên `Ethernet 3`) hiện là `192.168.56.101` [XÁC MINH 20:58]; lệch dải ở báo cáo 42 chỉ vì VM đặt `192.168.1.150`. (IP LAN của máy thật nay là `192.168.1.12`, không còn `.8` như ghi trong CLAUDE.md [XÁC MINH].)
2. VM thử: đổi IP sang `192.168.56.150/24`, không gateway, không DNS ra ngoài; đổi tên máy thành `JXTEST36` (tránh trùng Main VM).
3. Trong VM: đổi `Ip` trong các `gs00N_cfg.ini` và cấu hình Bishop/Goddess từ `192.168.1.150` sang `192.168.56.150` (theo byte, có `.bak`).
4. LDPlayer nối tới `192.168.56.150` qua máy thật (NAT của LDPlayer đi theo bảng định tuyến máy thật) [GIẢ THUYẾT, thử sau khi áp dụng]. Dùng lệnh `adb shell ping` để kiểm.
Việc "VM thử chạy server" [XÁC MINH một phần]: gs001 `A2T2` (exe gốc + DLL A2) đã lên và nối Goddess 5001, S3Relay 5003–5005, Bishop 56732. "36 Hz" **[CHƯA KIỂM]**: `A2T2` là nhánh lệnh `CmdLane` (báo cáo 38/44), chưa phải bản 36 Hz từ `D:\JX-build\src18`.

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

## Cửa sổ ngữ cảnh phiên PM (2026-11-16 21:xx)
- Đặt về chuẩn 200k theo yêu cầu chủ dự án: `.claude/settings.json` của dự án có `env.CLAUDE_CODE_DISABLE_1M_CONTEXT = "1"` [XÁC MINH, JSON hợp lệ]; mẫu `TOOLS/settings.mau.json` cũng đã thêm mục này.
- Đã gỡ `modelSettings.claude-sonnet-5-5.autoCompactWindow: 400000` khỏi `~/.claude/settings.json` (không còn cấu hình 400k ở settings người dùng) [XÁC MINH].
- Không đụng cấu hình Codex. Có hiệu lực từ phiên Claude Code mới (phiên hiện tại giữ cài đặt cũ tới khi khởi động lại) [GIẢ THUYẾT, chưa kiểm].
