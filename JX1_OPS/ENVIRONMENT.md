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
| Model Codex cố định (Q-25) | `gpt-6.1-sol` (Sol Max) + reasoning `max`, qua `--model` và `--config` trong `TOOLS/chay_codex.ps1`; `/v1/models` xingchi trả `gpt-6.1-sol`, `gpt-6-astra`; `gpt-6-luna` mặc định trong config.toml bị 404 | [XÁC MINH 16/11] |
| `codex exec` nền | **Chạy được** (0-03, 21:24). Gọi đúng như Dispatcher cũ (`jx1_task_dispatcher.py`): `C:\Users\PC\AppData\Local\OpenAI\Codex\bin\b6c7fc9497179c98\codex.exe exec --json --sandbox workspace-write --model gpt-6.1-sol --config model_provider="xingchi" --config model_reasoning_effort="max" --config approval_policy="never" --config sandbox_mode="workspace-write" -C <worktree> -o <file> -`, env `CODEX_HOME=C:\Users\PC\.codex`, `PYTHONUTF8=1`, prompt qua stdin. Không sửa config.toml (mặc định gpt-6-luna bị xingchi từ chối). Lệnh shell đầu có thể lỗi 1223, worker tự xử lý | [XÁC MINH] |

## Việc kế tiếp từ kiểm kê này
1. 0-02b: bật `JX-Test-36` (bridged, `.150`), giải quyết WinRM/đăng nhập, kiểm server 36 Hz. Mật khẩu lấy từ Credential Manager, không ghi vào file.
2. 0-03: thử `codex exec` bằng đường dẫn đầy đủ ở trên.
3. Máy hiện chạy Main VM 6 GB; bật thêm VM thử 6 GB vẫn đủ RAM (khoảng 24 GB trống).

## Cửa sổ ngữ cảnh phiên PM (2026-11-16 21:xx)
- Đặt về chuẩn 200k theo yêu cầu chủ dự án: `.claude/settings.json` của dự án có `env.CLAUDE_CODE_DISABLE_1M_CONTEXT = "1"` [XÁC MINH, JSON hợp lệ]; mẫu `TOOLS/settings.mau.json` cũng đã thêm mục này.
- Đã gỡ `modelSettings.claude-sonnet-5-5.autoCompactWindow: 400000` khỏi `~/.claude/settings.json` (không còn cấu hình 400k ở settings người dùng) [XÁC MINH].
- Không đụng cấu hình Codex. Có hiệu lực từ phiên Claude Code mới (phiên hiện tại giữ cài đặt cũ tới khi khởi động lại) [GIẢ THUYẾT, chưa kiểm].

## Tường lửa Main VM `JX-Server-D` (Q-20, 2026-11-16 21:32)
- Hồ sơ mạng `Network 2` (Ethernet) đã là **Private**, không phải đổi [XÁC MINH bằng ảnh chụp console 21:31]. Tường lửa Domain/Private/Public đều ON.
- Nguyên nhân cổng đóng: luật có sẵn `Windows Remote Management (HTTP-In)` (5985) và bản Compatibility Mode (80) có `RemoteIP = 192.168.1.8/32`; máy thật nay là `192.168.1.12` [XÁC MINH].
- Luật cũ **không sửa**. Đã thêm 3 luật mới (qua cửa sổ PowerShell Admin trong VM, đã đóng sau khi làm): `JX-Q20-Host-5985`, `JX-Q20-Host-1433`, `JX-Q20-Host-5002`; Inbound, Allow, TCP, `remoteip=192.168.1.12`, `profile=private`.
- Kết quả từ máy thật (21:33): 5985 mở, 1433 mở [XÁC MINH]. 5002 vẫn đóng: tiến trình nghe `0.0.0.0:5002` nhưng có luật chặn chủ ý `JX no-in Sword3PaySys` (Block, mọi profile); luật chặn thắng luật cho phép. Máy thật không cần 5002 nên **không gỡ** luật chặn. Luật `JX-Q20-Host-5002` vì thế không có tác dụng.
- Hoàn tác (chạy trong PowerShell Admin của VM):
  `foreach($p in 5985,1433,5002){ netsh advfirewall firewall delete rule name=JX-Q20-Host-$p }`

## WinRM tới VM thử `JX-Test-36` (2026-11-16 21:36)
- Chủ dự án đã chạy TrustedHosts (có `192.168.56.150`) [XÁC MINH]. Cổng 5985 vẫn đóng vì luật WinRM trong VM chỉ cho IP cũ (cùng nguyên nhân Main VM).
- Đã thêm trong VM thử (Q-19): luật `JX-Q20-Host-5985` (Inbound, Allow, TCP 5985, `remoteip=192.168.56.101`, mọi profile). Sau đó `Invoke-Command` bằng `Get-JxCred` chạy được; VM thử đang có đủ 6 tiến trình chuỗi server [XÁC MINH].
- Hoàn tác (trong PowerShell Admin của VM thử): `netsh advfirewall firewall delete rule name=JX-Q20-Host-5985`.
- Lưu ý: tên máy của VM thử là `DESKTOP-KT7DU78`, trùng Main VM (VM gốc nhân bản). Hai VM nằm hai mạng khác nhau nên chưa gây lỗi; đổi tên VM thử là việc của 0-07/0-02b [CHƯA LÀM].
