# C2 – Chuẩn bị trước khi chạy exe

**Trạng thái: XONG phần chuẩn bị. Chưa chạy exe server nào.**

## Đã làm
- Snapshot: `c2-truoc-cau-hinh` (UUID <uuid>), `c2-truoc-chay-exe` (UUID <uuid>).
- Theo quyết định của chủ máy:
  - `gw\database.ini`, `gs\database.ini`: `[account] Server=.\SQLEXPRESS`, `Port=1433`, `PassWord` là mật khẩu `<sql-admin>` mới.
  - `gs\database.ini`: `[serverlist] Server=<LAN-IP>`.
  - `gw\relay_config.ini`: `[root] password` là mật khẩu `<sql-admin>` mới.
  - Mật khẩu chỉ nằm trong các file cấu hình trong VM, được chủ máy cho phép riêng. Bản gốc lưu ở `.bak` cùng thư mục.
- Giữ nguyên `Port` ở `[serverlist]` (15002 ở gw, 5002 ở gs).
- Chặn VM ra ngoài LAN: luật Outbound Block `JX block ra ngoai LAN`, chặn mọi địa chỉ trừ loopback và <LAN-IP>/24, cùng IPv6 `2000::/3`.
- Bật ghi log gói bị chặn: `%systemroot%\system32\LogFiles\Firewall\pfirewall.log`.

## Bằng chứng
- `Test-NetConnection` <IP>:443 và <IP>:53: thất bại. Ping <LAN-IP>: thành công. WinRM từ máy thật vẫn hoạt động.
- Defender quét `C:\JX\ServerNew` (103 giây): 0 phát hiện.
- VC++ x86: có `vcruntime140.dll` và `msvcp140.dll` trong `SysWOW64`.
- Mốc cổng trước khi chạy exe (09:44:47): chỉ có 1433.
- SHA256 của tất cả exe/dll: `C:\JX\hashes.csv` trong VM (37 dòng). Năm exe sẽ chạy, đều `NotSigned`:

| Exe | SHA256 |
|---|---|
| `gw\Sword3PaySys.exe` | `D53FDCE0154AF86FBEB333D9FD61356154B49C69728CEB681B8FE3C58F4EF092` |
| `gw\Goddess.exe` | `DC5A19265E257C4325108EFF2579496FFE33C3BDEE6B9639B549F53D079F4A31` |
| `gw\S3Relay.exe` | `1C5ED41630C7055274E63FBC7216B0BE6384ABD15A1D010B5366D68A9ADB2F10` |
| `gw\Bishop.exe` | `71EFF11C12EDDB92C15DDDC574247D08B0FA3A6C8B1EAE564FF059DEDE906B6E` |
| `gs\gs001.exe` | `DD44D425E205FD482FD287144BDC3D95AD90F42BDA92556A66C1214A463D4295` |

## Lưu ý
- Các hash chưa được tra trên VirusTotal.
- Chưa mở cổng inbound cho LAN (56722, 51189). Việc này cần khi thử từ máy khác.

## Bước kế
Hỏi và chạy lần lượt: `Sword3PaySys`, `Goddess`, `S3Relay`, `Bishop`, `gs001`.
