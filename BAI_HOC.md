# Bài học khi dựng server JX (VM JX-Server, <LAN-IP>)

Ghi ngắn theo mục, cập nhật trong lúc làm. Không ghi mật khẩu vào file này. Chi tiết và bằng chứng nằm ở `docs-analysis/reports/`.

## Cổng

| Cổng | Tiến trình | Dùng để | Ghi chú |
|---|---|---|---|
| 1433 | SQL Server (`SQLEXPRESS`) | DB `account` | Chỉ dùng nội bộ VM |
| 5001 | `Goddess` | Lưu nhân vật | Phải bấm Start |
| 5002 | `Sword3PaySys` | Tài khoản, đăng nhập dịch vụ | |
| 5003, 5004, 5005 | `S3Relay` | Transfer, Chat, Tong (theo `gs001_cfg.ini`) | |
| 7776 | `S3Relay` | `RELAY_SIBLING_PORT` | Có trong mã nguồn, không phải bất thường |
| 7777 | Chưa có | `RELAY_ROUTE_PORT`, đích của "root" trong S3Relay | Chưa có tiến trình nào nghe |
| 56722 | `Bishop` | Client kết nối | Mã cứng trong client |
| 56732 | `Bishop` | Game server kết nối | |
| 51189 | `gs001` | Client vào game | `gs002` trở đi dùng cổng kế tiếp |

## Thứ tự và thao tác khởi động

1. SQL Server, `Sword3PaySys`, `Goddess`, `S3Relay`, `Bishop`, `gs001`.
2. Các exe có giao diện và không tự chạy dịch vụ:
   - `Goddess`: bấm **Start**.
   - `S3Relay`: hộp thoại **login root** hiện ngay khi mở.
   - `Bishop`: hộp thoại **Login**, sau đó bấm **Startup**.
3. Đăng nhập của `S3Relay` và `Bishop` là tài khoản dịch vụ trong bảng `ServerList`, không phải `<sql-admin>`. Dùng tên `<service-account>` với `netpass` trong `gw\database.ini`.
4. `Sword3PaySys` bỏ qua kiểm tra IP và MAC khi nguồn là 192.168.x.x, nên không cần sửa `ServerList` (`S3PAccount.cpp:427`).
5. `S3Relay` báo `FAIL: reclient gateway` là bình thường khi `Bishop` chưa chạy. Hết lỗi sau khi bấm Startup.

## Lỗi đã gặp và cách sửa

- **SQL Setup qua WinRM thất bại** (`error generating the XML document`, `CryptographicException: Access is denied`): DPAPI không chạy được trong phiên đăng nhập mạng. Sửa: chạy setup trong phiên desktop của VM.
- **Không nên cài bằng scheduled task kèm mật khẩu**: mật khẩu sẽ nằm trong file XML của task.
- **Phiên Claude Code trên máy thật không có quyền Admin**: `Start-Service WinRM` và `TrustedHosts` phải do chủ máy chạy. Mã `sc query` 1077 nghĩa là chưa có lần khởi động nào tới được Windows.
- **`keyboardputstring` có thể làm rơi ký tự**: một dấu ngoặc kép nghi bị mất nên PowerShell chạy nhầm lệnh `Setup` của Pester. Sau khi gõ mật khẩu phải đăng nhập thử để xác nhận.
- **Hộp thoại tường lửa Windows chiếm focus khi exe mở cổng**: phím Enter có thể thành Allow access. Sửa: tạo trước luật Inbound Block cho từng exe thì hộp thoại không hiện.
- **Exe chạy qua WinRM sẽ chết khi phiên đóng và không có giao diện**: khởi động bằng scheduled task, `LogonType Interactive`, user đang đăng nhập, `ExecutionTimeLimit` bằng 0. Task không chứa mật khẩu.
- **UI Automation không thấy nút của các exe này**: dùng Win32 `EnumChildWindows` và `BM_CLICK`.
- **`BM_CLICK` có thể không có tác dụng khi cửa sổ không ở phía trước**: gửi `WM_COMMAND` với mã nút (`GetDlgCtrlID`) tới cửa sổ cha.
- **PowerShell đổi `$null` thành chuỗi rỗng khi gọi `FindWindow`**: bọc lời gọi trong hàm C#, truyền `null` từ đó.
- **`Get-Content` rồi `Set-Content` có thể đổi mã hóa file cấu hình**: thay thế theo byte bằng Latin-1 (codepage 28591).
- **`pfirewall.log` không ghi tiến trình**: bật `auditpol` mục Filtering Platform Connection (failure), đọc sự kiện 5157 để biết exe nào bị chặn.
- **Máy thật lỗi WMI** (`Get-NetIPAddress`: Invalid class): dùng `ipconfig` thay thế. Chưa rõ nguyên nhân.

## Quyết định đã chọn

| Quyết định | Lý do |
|---|---|
| `Port=1433` ở `[account]` của cả hai `database.ini` | SQL thật ở 1433. Đã xác nhận: `Sword3PaySys` nối được 1000 phiên vào DB `account` |
| Giữ nguyên `Port` ở `[serverlist]` | Chưa có lý do đổi |
| Cho ghi mật khẩu `<sql-admin>` vào cấu hình, chỉ trong VM | Exe cần dạng rõ. Chủ máy cho phép riêng, không đưa vào git hay báo cáo |
| Chặn VM ra ngoài LAN bằng một luật Outbound Block | Block thắng mọi luật Allow, không phải đổi hành động mặc định |
| Chặn inbound từng exe trong lúc thử | Tránh hộp thoại tường lửa. Các cổng 5001-5005 chỉ cần nội bộ |
| Không chạy `S3RelayServer.exe` | Không nằm trong danh sách đã duyệt |
| Giữ `Goddess` ở chế độ `DB` | Không đổi mặc định khi chưa có lý do |
| Chỉ mở 56722, 51189 cho `<LAN-IP>` | Đủ để kiểm tra từ máy thật, chưa cần mở cho điện thoại |
| Giữ nguyên 28 bản đồ thiếu | Server vẫn chạy với 772 bản đồ; xem lại sau khi thử client thật |

## `gs001`

- Nạp mất khoảng 7 phút trên VM 4 CPU, 6 GB RAM, dùng khoảng 2,2 GB bộ nhớ. Cổng 51189 mở trước, các kết nối tới gateway chỉ có sau khi nạp xong.
- Log `gameser_log` chỉ ghi bản đồ nạp thành công. Bản đồ lỗi chỉ in ra console, dạng `Load (i) Fail Map ID: X`.
- Đọc được bộ đệm console (9001 dòng) bằng `AttachConsole` và `ReadConsoleOutputCharacter` từ phiên desktop.
- Tên thư mục script tiếng Trung lưu dạng GBK, trên Windows codepage 1252 trông như `¶«±±Çø`. Exe vẫn tìm thấy, nên dạng hiển thị này tự nó không phải lỗi.
- **28 bản đồ lỗi (`NpcNum:-1`) là do thiếu `.wor` trong PAK của server**, không phải lỗi mã hóa. Danh sách ID ở `reports/05-c2-chay-server.md`. Client có 5/28, 23 bản đồ không có ở đâu.
- **Kiểm tra file trong PAK không cần chạy exe**: băm đường dẫn `\maps\<tên>.wor` viết thường theo `g_FileName2Id` (ký tự có dấu, byte từ 0x80 là số âm), rồi dò bảng chỉ mục 16 byte/entry. Đã đối chứng 772/772 bản đồ nạp được.
- Đường dẫn `E:/_bin_v2_/gs/Logs/script_errors.txt` ghi cứng trong mã nguồn, chỉ dùng khi script lỗi. Vô hại trên VM không có ổ E:.
- `WorldSet_gs001.ini` có nhiều dòng `WorldNN` hơn `Count`; exe chỉ nạp `Count` dòng đầu (800).

## Truy cập từ xa và client

- `[GameServer] Ip` là địa chỉ `Bishop` gửi cho client. `[Gateway] Ip` là kết nối nội bộ, tách biệt.
- `Ip` phải chứa `localIp` (`KSOServer.cpp:887`), nếu không `gs` không khởi động được. Đổi `Ip` sang mạng khác thì đổi cả `localIp`.
- `netsh portproxy` làm VM thấy nguồn là máy thật, nên không cần đổi tường lửa VM.
- Máy thật lỗi WMI: `New-NetFirewallRule`, `Get-NetIPAddress` không dùng được, phải dùng `netsh`. `Get-PSDrive` báo ổ trống 0 GB là sai, dùng `[IO.DriveInfo]`.
- Mỗi snapshot live tốn khoảng 3 GB. Theo dõi ổ C.
- Dựng APK cần JDK 17, Android SDK 34, build-tools 34.0.0, NDK `25.2.9519653`, CMake `3.30.5`, Gradle 8.7; đã cài ở `D:\Android`.
- **`Java heap space` khi build có thể là của client Gradle**, không phải heap build. `gradle.bat` mặc định `-Xmx64m`; hơn 200 000 dòng cảnh báo trình biên dịch làm ngập client. Xem log daemon: nếu có `client disconnection detected` và không có `OutOfMemoryError` thì đặt `GRADLE_OPTS=-Xmx512m`, ghi log thẳng ra file. Đừng tăng heap build.
- `sdkmanager.bat` qua PowerShell tách dấu `;` trong tên gói: dùng `--package_file`.
- Không chạy `gradlew` của gói không rõ nguồn; dùng bản Gradle chính thức đã kiểm SHA256.
- **Snapshot live khi `gs001` đã nạp đầy bộ nhớ từng làm `VBoxSVC` crash** (`.sav` 13 GB, chạy 15 phút). Không chụp snapshot live khi server đang chạy.
- Trên máy thật, `Test-Connection` cũng hỏng vì lỗi WMI: dùng `ping.exe`.
- Client tải tiếp bằng Range, server CDN phải hỗ trợ.
- CDN phải đặt gốc ở `data_cdn`, không phải `data_cdn\data`: client gọi `/data/paklist.ini` và mọi `.pak` có tiền tố `data/`. Client không coi 404 là lỗi, lưu trang lỗi thành file; dấu hiệu là "0 b / 330 b, 0/0 File" (330 byte là trang 404 của Python). Sau khi sửa phải xóa dữ liệu ứng dụng.
- Đưa APK sang điện thoại qua Tailscale: dùng Taildrop (`tailscale file cp <apk> <tên-máy>:`, xem đích bằng `tailscale file cp --targets`), không cần mở thêm cổng hay quyền Admin.
- Cổng 80 trên máy thật do `ReportServer` (SQL Server Reporting Services) giữ qua `http.sys` (PID 4), nên bind báo `WinError 10013`. Phản hồi 403, 404 lúc đó là của `http.sys`, không phải của CDN: phải đọc log server trước khi tin kết quả `curl`. Client không dùng được cổng khác 80.
- `Bishop` không lọc `gs` theo IP. `ServerList` chỉ dùng cho đăng nhập dịch vụ. `GameSvrIP` trong `Bishop.cfg` không được đọc.
- `Goddess` tự tạo `roledb` khi thiếu (`DBTable.cpp:110`). Thay `roledb` phải xóa cả `log.*` vì có `DB_RECOVER`.
- `Goddess` tự sao lưu vào `gw\database\<ngày>`, các bản này cũng chứa dữ liệu nhân vật.

## Chơi thử

- Phím chính cho ngồi thiền khi `m_FightMode == 0`, trước cả bước chọn chiêu (`KNpcAI.cpp:1406`). Ở Ba Lăng Huyện, đi bộ qua cổng không bật được chiến đấu (chưa rõ vì sao); sang Biện Kinh thì đánh được.
- Xem đường Tailscale bằng `tailscale ping <ip>`: `via DERP` là qua máy chủ trung gian (đo được 100-190 ms), `direct` mới là nối thẳng.

- Bộ cài Tailscale tự thêm luật `Tailscale-Process` cho UDP của `tailscaled`, nên tường lửa Windows không cản nối thẳng.
- Router nhà nằm sau CGNAT (IP WAN dạng `10.x`), nên chuyển tiếp UDP 41641 không có tác dụng. Chủ máy chọn giữ đường qua DERP Singapore. Kiểm tra IP WAN trước khi cấu hình chuyển tiếp cổng.
- Dùng chung Wi-Fi với máy chủ và giữ Tailscale bật: chủ máy đo ping trong game 49-100 ms. Không cần cài thêm gì.
- Trên 4G yếu, độ trễ qua DERP vọt lên 0,5-2,2 giây khi game gửi 30-60 KB/s, rồi về khoảng 100 ms khi hết dữ liệu. Wi-Fi yếu cũng gây ping rất cao. Chưa tách được phần do 4G và phần do DERP.
- Luật `Tailscale-In` của bộ cài cho phép mọi giao thức tới địa chỉ Tailscale máy thật (profile Domain, Private). Giới hạn "chỉ điện thoại" của cổng 56722, 51189 vì thế không tuyệt đối; muốn chặt hơn thì dùng ACL của Tailscale.

## Tài khoản chơi

- Tạo tài khoản phải có đủ 2 bảng: `Account_Info` và `Account_Habitus` (`iFlag=0`, `dEndDate` còn hạn). Thiếu bảng sau thì log ghi `No Money`, client báo "Đăng nhập quá hạn".

## Chưa rõ

- Vì sao script `...5石?对话.lua` báo lỗi nạp. Bản gốc có hai file khác nhau ở một ký tự (`U+0086` và `U+2020`), nội dung khác nhau. Chưa rõ do tên hay cú pháp Lua.
- Cổng root 7777 có cần cho chơi trong LAN không, và có phải của `S3RelayServer.exe` không. Vì vậy `<service-account>` trong `S3Relay` chưa được kiểm tra thực sự; ở `Bishop` thì đã được chấp nhận.
- Các gói bị chặn trong khoảng 2 phút đầu sau khi `Sword3PaySys` khởi động chưa truy được tiến trình gửi, vì audit bật sau đó.
- SHA256 của exe chưa tra trên VirusTotal.

## Cần nhớ khi làm tiếp

- Log cũ, `roledb` và bản `account.sql` còn chứa dữ liệu người chơi thật. Đã xóa 672 tài khoản khỏi DB, nhưng các snapshot cũ và lịch sử git vẫn còn. Không xuất ra báo cáo.
- 56722 và 51189 hiện chỉ cho `<LAN-IP>`. Muốn cho điện thoại vào phải mở rộng `RemoteAddress` của `JX in Bishop 56722 may that` và `JX in gs001 51189 may that`.
- Máy thật đang bật WinRM và có `TrustedHosts=<LAN-IP>`. Chủ máy quyết định có tắt sau khi xong không.

## Bot AI (khảo sát, 2026-11-11)
- Bot tổ đội: client Python không giao diện, dùng lại mã hóa XOR khóa xoay từ gói `ACCOUNT_BEGIN` 0x20. Chi tiết ở `reports/16-khao-sat-bot-ai.md`.
- Bot Tống Kim: NPC Lua, hai NPC thường khác phe là kẻ địch (`KNpcSet.cpp:214-218`). Kịch bản `sj_creatnpc.lua` đã tạo lính hai phe.
- Hàm `PARTNER_*` có trong 33 file Lua nhưng không có trong mã nguồn server: đừng dựa vào.
- Tham số 8, 9 của `AddNpc` là cờ vàng và boss, không phải phe. Đặt phe bằng `SetNpcCurCamp`.

## Tạm nghỉ 2026-11-11
- Đã tắt CDN (cổng 80) và tắt VM bằng ACPI (`acpipowerbutton`), VM về `poweroff` sau 80 giây.
- Giữ nguyên: cổng Tailscale 56722/51189/80 (chỉ điện thoại), WinRM, TrustedHosts, dữ liệu, snapshot. `ReportServer` vẫn đang tắt.
- Hôm sau: bật VM, chạy lại 5 exe theo thứ tự, chạy `cdn_server.py` nếu cần thử điện thoại.

## Nhân bản VM sang ổ D (2026-11-11)
- `clonevm --mode machine` gộp 24 snapshot thành 1 đĩa 41 GB trong 6 phút. Với `keepdisknames`, đĩa mang tên lớp snapshot cuối `{fc58d1dc-...}.vmdk`.
- `keepallmacs` giữ MAC nên IP bridged `<LAN-IP>` không đổi. Không bật hai VM cùng lúc.
- Từ nay VM dùng là `JX-Server-D`. `C:\VMs\JX-disk\Windows 10 x64.vmdk` là đĩa nền của chuỗi snapshot cũ, chỉ xóa cùng `unregistervm JX-Server --delete`.
- Bộ phân loại quyền chặn lệnh có mật khẩu viết thẳng: chủ máy cho phép bằng luật `PowerShell($sec = ConvertTo-SecureString:*)` trong `.claude/settings.local.json` (không vào git).

## CDN cổng 8080 (2026-11-11)
- `ReportServer` là dịch vụ Windows `Automatic`, tự bật lại sau khi máy thật khởi động lại. `http.sys` giữ cổng 80 độc quyền, Python không bind chung được (`WinError 10013`).
- Client ghép `http://<down>/` (`KUpdateLayer.cpp:355`), nên `down=` mã hóa `<TAILSCALE-IP>:8080` (đúng 18 ký tự, bằng giới hạn `simply_crypt`) đổi được cổng CDN mà không sửa mã nguồn.
- Luật `Tailscale-In` cho mọi cổng vào địa chỉ Tailscale của máy thật, nên cổng 8080 không cần luật tường lửa mới. Giới hạn người truy cập do `--allow` của `cdn_server.py` đảm nhiệm.
- Lệnh chạy: `python -I -u docs-analysis\scripts\cdn_server.py --bind <TAILSCALE-IP> --port 8080 --allow <TAILSCALE-IP> --root data_cdn --override data/update10.pak=docs-analysis\out\tailscale\update10.pak`. Khóa override phải là `data/update10.pak`, không phải `update10.pak`.
- Windows PowerShell 5.1 không có `[Text.Encoding]::Latin1`, dùng `GetEncoding(28591)`.

## portproxy / iphlpsvc không nghe sau reboot máy thật (2026-11-11)
- Triệu chứng: điện thoại qua được bước tải (CDN cổng 8080) nhưng kẹt ở chọn máy chủ. `netsh interface portproxy show all` vẫn có <TAILSCALE-IP>:56722 và :51189 → <LAN-IP>, `iphlpsvc` Running/Automatic, nhưng `netstat` không có socket nghe và kết nối từ máy thật bị từ chối. Bishop không nhận gói nào.
- Bài học: luật `portproxy` còn trong cấu hình và dịch vụ Running KHÔNG có nghĩa là cổng đang nghe. Sau mỗi lần máy thật khởi động lại phải kiểm `netstat -ano | Select-String 'LISTENING'` đúng địa chỉ và cổng.
- Nguyên nhân gốc: chưa kiểm chứng. Giả thuyết: `iphlpsvc` lên trước khi adapter Tailscale có địa chỉ `<TAILSCALE-IP>` rồi không bind lại.
- Cách chữa đúng cần Admin (`Restart-Service iphlpsvc`); chủ máy dặn không tự sửa `iphlpsvc` hay `ReportServer`, nên không làm.
- Cách tạm đã dùng (chủ máy duyệt): `docs-analysis/scripts/tcp_forwarder.py` bind đúng 2 địa chỉ:cổng Tailscale, chỉ nhận `<TAILSCALE-IP>`, không ghi nội dung gói. Dừng bằng `dung_forwarder.ps1`. Kết quả: đăng nhập, vào gs001, ping khoảng 150 ms.
- Chẩn đoán nhanh bằng log forwarder: gói VM→điện thoại 34 byte = ACCOUNT_BEGIN (Bishop sống); phiên đăng nhập thật dài vài giây và hàng trăm byte; phiên vào gs001 trên 51189 kéo gần 1 MB dữ liệu.
- Đối chiếu đăng nhập ở `gw\payserver_log\<ngày>\*.log`: dòng `User <tên> Login ... Login Success!`, `Freeze Account`, `Logout`.
- Đã soạn nhưng chưa chạy: `khoi_dong_forwarder.ps1`, `dang_ky_forwarder.ps1`, `huy_dang_ky_forwarder.ps1` (xem báo cáo 20).
- `Get-CimInstance Win32_OperatingSystem` trên máy thật lỗi (WMI), không đọc được giờ khởi động; dùng giờ ghi trong log.
- Task `JX-UI`: hành động bị đổi nhiều lần sang script trợ giúp (`C:\JX\sql\ui*.ps1`, `console.ps1`). Ghi lại để dọn cuối; xem báo cáo 19 mục 4. Qua WinRM, trigger của các tác vụ `JX-*` đọc không ra, mâu thuẫn với lần kiểm trước.

## Tác vụ khởi động forwarder (2026-11-11)
- Tác vụ Task Scheduler có thể dọn tiến trình con khi tiến trình chính kết thúc. Script khởi động một dịch vụ nền phải chờ nó (`$p | Wait-Process`) để tác vụ ở trạng thái Running. Chưa kiểm chứng bằng reboot.
- Đăng ký tác vụ trigger `AtLogOn` cho chính người dùng hiện tại không cần Admin: `Register-ScheduledTask` chạy được ở phiên thường (LogonType Interactive, RunLevel Limited).
- `forwarder.log` bị ghi đè mỗi lần script khởi động forwarder (do `-RedirectStandardOutput`); lưu log cần thiết trước khi reboot.

## VM cũ trên ổ C: khác biệt cần biết khi sao lưu (2026-11-11)
- `.vbox` của `JX-Server` trỏ đĩa nền bằng đường dẫn tuyệt đối `C:/VMs/JX-disk/Windows 10 x64.vmdk` (ngoài thư mục VM). Copy riêng thư mục VM không đủ; phải kèm `C:\VMs\JX-disk` (40 GB).
- Snapshot chụp lúc VM chạy để lại 20 file `.sav` = 70 GB (hơn nửa dung lượng VM). Chưa kiểm chứng `clonevm --mode all` có giữ chúng không.
- Copy thư mục rồi `registervm` sẽ trùng UUID với VM đang đăng ký; muốn có bản đăng ký được phải dùng `clonevm` (UUID mới).
- `clonevm` chạy qua `VBoxSVC` dùng chung với VM đang chạy; vì `VBoxSVC` từng crash nên chỉ clone lúc VM D đã tắt. Sao chép nguyên văn bằng robocopy không qua `VBoxSVC` nên an toàn hơn.

## Sao lưu VM cũ bằng robocopy (2026-11-11)
- Mã thoát robocopy 0-7 là thành công (1 = đã chép file); chỉ 8 trở lên là lỗi. Harness báo "failed" cho mã khác 0 của lệnh cuối cùng, nên đọc log và FAILED thay vì tin chữ "failed".
- 142,7 GB chép trong khoảng 19 phút (~131-138 MB/s) với `/IPG:5`, trong lúc VM D vẫn chạy. Băm SHA256 hai phía song song mất khoảng 22 phút.
- Đếm snapshot không cần VirtualBox: đếm phần tử `<Snapshot>` trong `.vbox` (24).

## registervm bản sao thất bại vì đĩa mồ côi còn đăng ký (2026-11-11)
- `unregistervm` (không `--delete`) giải phóng đĩa nền và các đĩa chênh lệch của VM nhưng đĩa `JX-Server.vdi` không gắn vào VM vẫn còn trong danh sách đĩa của VirtualBox ở vị trí cũ, nên `registervm` bản sao báo `E_INVALIDARG` (UUID `7b13c650…` đã tồn tại ở `C:\VMs\JX-Server\JX-Server.vdi`).
- Đọc nguyên nhân ở `%USERPROFILE%\.VirtualBox\VBoxSVC.log` (tìm `Cannot register the hard disk`); VBoxManage chỉ in `E_INVALIDARG` mơ hồ.
- Trước khi `unregistervm` nên chạy `list hdds` và tìm mọi đĩa cùng UUID trong `.vbox` mà không gắn vào VM.
- Cách gỡ: `VBoxManage showmediuminfo disk <uuid>` (không có "In use by VMs" = không dùng) rồi `closemedium disk <uuid>` (không `--delete`), sau đó `registervm` thành công. Thời gian trong `VBoxSVC.log` là thời gian trôi kể từ khi `VBoxSVC` khởi động, không phải giờ đồng hồ.
- Khởi động VM trùng MAC với VM đang chạy chỉ an toàn khi cáp ảo ngắt: `modifyvm <vm> --cableconnected1 off`, kiểm `cableconnected1="off"` trước `startvm`.

## Giải phóng ổ C (2026-11-11)
- Xóa VM cũ sau khi đã chuyển bản sao thành VM đăng ký trên D: chỉ xóa file thường bằng `Remove-Item -LiteralPath <thư mục> -Recurse -Force` cho đúng 2 thư mục (không dùng `unregistervm --delete` vì VM đã gỡ đăng ký từ trước). Xóa 142,7 GB mất 3 giây; ổ C từ 19,7 GB lên 162,4 GB.
- Trước khi xóa: kiểm `list hdds` không còn đĩa dưới `C:\`, `C:\VMs` chỉ chứa đúng 2 thư mục, không có reparse point (junction/symlink), và `Resolve-Path` khớp tuyệt đối với đường dẫn được duyệt.
- Thư mục `D:\VMs\Backup\JX-Server-archive` giờ vừa là bản lưu trữ vừa là VM `JX-Server` đã đăng ký (cáp mạng ảo ngắt, trùng MAC với `JX-Server-D`). Chỉ bật mạng cho VM này sau khi tắt `JX-Server-D` hoặc đổi MAC.

## Khởi động server trên VM `JX-Server` (archive, 11/11/2026)
- Không có WinRM (cần mật khẩu `<vm-admin>`) thì điều khiển qua cửa sổ VM: `VBoxManage controlvm JX-Server keyboardputscancode E0 5B 13 93 E0 DB` (Win+R), gõ `powershell -NoExit`, rồi `keyboardputstring`. Đọc kết quả bằng `screenshotpng`.
- Trong VM chính sách chạy script chặn `& file.ps1`; dùng `powershell -NoProfile -ExecutionPolicy Bypass -File C:\JX\sql\ui.ps1` (chỉ cho tiến trình đó).
- `C:\JX\sql\ui.ps1` bấm Start của Goddess, `ui2.ps1` điền login root của S3Relay, `ui3.ps1` điền Login Bishop, `ui4.ps1` bấm Startup. Các script lấy `netpass` từ `database.ini` trong VM, không chứa mật khẩu.
- Script báo "clicked [Start]" nhưng nút không đổi khi cửa sổ không ở phía trước. Đưa cửa sổ lên (Alt+Tab bằng `keyboardputscancode 38 0f 8f b8`) rồi gửi phím Space (`39 b9`) thì Goddess chạy ("Enable DB", cổng 5001).
- Hộp thoại `login root` của S3Relay nằm sau cửa sổ khác, Alt+Tab không tới; `AppActivate` trả False; ui2.ps1 chạy 3 lần không điền được. Dừng theo quy tắc 3 lần.
- S3Relay: Alt+Tab từ PowerShell tới hộp thoại `login root` rồi gõ trực tiếp `keyboardputstring` (Name, Tab, Pswd, Enter) thì qua; cổng 5003/5004/5005/7776 nghe (PID S3Relay). Hộp thoại trống nghĩa là script chưa điền do cửa sổ không ở phía trước.
- Bishop: hộp thoại Login không nằm trong Alt+Tab và Alt+Esc; phím gõ rơi vào PowerShell hoặc Goddess. Chưa điền được; xem báo cáo cuối phiên. Cẩn thận: sau Alt+Tab phải chụp màn hình xác nhận cửa sổ nào đang nhận phím trước khi gõ.
- Bishop: `AppActivate` theo PID (`Add-Type -AssemblyName Microsoft.VisualBasic; [Microsoft.VisualBasic.Interaction]::AppActivate($pid)`) đưa hộp Login lên phía trước, sau đó gõ trực tiếp <service-account>/netpass thì qua; cửa sổ chính `[enable]` sau khi bấm Startup (Space), cổng 56722/56732 nghe.
- `keyboardputstring` làm rơi dấu ngoặc kép `"` và dấu backtick; dùng nháy đơn.
- `gs001` trên `JX-Server` (archive) thoát im lặng khi đang nạp (script rồi bản đồ), 3 lần: lần 1 sau ~2,5 phút ở "Start loading script:0"; lần 2 tương tự; lần 3 sống ~1 phút, nạp tới Map OK ID 24 (NpcNum 718) thì biến mất. Không có sự kiện Application Error, log `gameser_log` và `gw\*_log` rỗng/1 byte. Chưa rõ nguyên nhân. Cùng cấu hình VM (6144 MB, 4 CPU) với JX-Server-D, nơi sáng nay gs001 chạy được.

## gs001 crash khi nạp bản đồ (2026-11-11 chiều)
- Mã thoát đọc được qua task: `Get-ScheduledTaskInfo JX-gs001` → `LastTaskResult` = `0xC0000005` (access violation). Không có sự kiện Application Error, nhưng `gs001` tự ghi dump vào `gs\DumpInfo\v1.0-<ngày>-<giờ>-<pid>-<tid>.dmp` (12,5 MB).
- Console `gs001` in chậm hơn log rất nhiều: lúc console mới tới "Map OK ID 23" thì `gameser_log\gs001\<ngày>\<giờ>.log` đã ghi 44 bản đồ. Muốn biết tiến độ nạp thật phải đọc log, không đọc console.
- Trên `JX-Server-D` (17:14): nạp script mất khoảng 6 phút, bắt đầu nạp bản đồ 17:20:03, crash 17:20:27 ngay sau bản đồ thứ 44 (`...2.wor`). Log buổi sáng (09:20) qua được đúng chỗ này (`...3.wor` kế tiếp) và nạp đủ 809 dòng. Không file nào trong `gs` đổi hôm nay ngoài log và dump.
- Không có kết nối nào qua forwarder lúc crash (forwarder.log không có dòng NHAN).
- **Nguyên nhân gs001 crash (đã xác minh bằng dump, báo cáo 29):** `gs001` mở cổng 51189 trước khi tạo `m_pCoreServerShell`; một kết nối TCP mở rồi đóng vào 51189 trong lúc nạp (~7 phút) gọi hàm qua con trỏ NULL ở luồng mạng `Heaven.dll` (`gs001.exe+0x1EF81`). Đừng thử cổng 51189 (kể cả `Test-NetConnection`, `TcpClient`) và đừng mở game trên điện thoại cho tới khi console có "Server start succeeded". Kiểm tra sẵn sàng bằng console/log hoặc `Get-NetTCPConnection` trong VM.
- Đọc minidump không cần debugger: PowerShell đọc byte theo định dạng minidump (stream 6 ngoại lệ, 4 module, 3 luồng, 5 bộ nhớ); CONTEXT x64 dài 1232 byte, RIP ở offset 0xF8, RSP 0x98. Trong PowerShell `$m` và `$M` là cùng một biến.

## Tối ưu nhịp client (2026-11-11, báo cáo 31)
- Build APK phải đặt `ANDROID_USER_HOME=D:\Android\user`; thiếu biến này Gradle tự tạo khóa debug mới ở `%USERPROFILE%\.android` và APK không cài đè được. Kiểm chữ ký bằng `apksigner verify --print-certs` (đúng: `a48601f7…`).
- Nguồn client GBK: không sửa bằng công cụ Edit; vá bằng Python đọc/ghi latin-1, mỗi neo phải khớp đúng 1 lần, sao lưu trước.
- `KCoreShell::Goto` từng đặt lại `m_nSendMoveFrames` mỗi khung, làm mọi giới hạn gửi lệnh joystick vô hiệu.

## Mất sát thương khi vừa chạy vừa đánh (2026-11-11, báo cáo 33)
- Server: một ô lệnh mỗi nhân vật, gói xử lý ngay khi tới, thực thi ở nhịp 18 Hz; gói chạy tới sau gói kỹ năng trước nhịp đó xóa kỹ năng. Client không tắt Nagle nên khi đang chạy gói kỹ năng bị gộp với gói chạy sau nó (RTT ~150 ms) → mất. Hoạt ảnh/va chạm vẫn hiện vì client tự mô phỏng (`KMissle::ProcessCollision`); sát thương chỉ từ `s2c_npchurt`. Không dùng hoạt ảnh làm bằng chứng sát thương.
- `CCLOG` bị loại trong native Release của dự án; muốn log trên điện thoại dùng `__android_log_print` (log tag `JXFIX`).
- PowerShell 5.1 làm rơi dấu `"` khi truyền đoạn mã vào `python -c`: ghi script ra file rồi chạy.

## Đợt 34: nội suy đạn, đánh giá 36 Hz (2026-11-11)
- Nội suy hình ảnh làm được ngay trong hàm vẽ (`KMissle::Paint`): phát hiện vị trí logic đổi, đi tiếp từ vị trí đang vẽ; không cần sửa logic bay.
- 36 Hz không chỉ là đổi `GAME_FPS`: tốc độ là số nguyên/nhịp (13-24% lẻ), số khung nằm trong `skills.txt`, `missles.txt`, `npcs.txt`, ~950 dòng Lua, pak client và 16 trường gói tin. Chưa làm; xem báo cáo 34 mục 5.
- "Đi tiếp từ vị trí đang vẽ" làm hình trễ tới ~1,4 nhịp ở 60 FPS (có giới hạn, không tích lũy).

## Đợt 35: biên dịch server từ mã nguồn (2026-11-11)
- Mã cũ (v100/v140) biên dịch được bằng v143 sau 4 chỗ sửa trên bản copy: macro `snprintf`/`vsnprintf` trong `acc_auto.h`, `/Zc:sizedDealloc-`, `/NODEFAULTLIB:libcpmt.lib` chỉ cho Engine, shim `__imp___iob_func` cho `ms64.lib`.
- `JXAll_GameServer.sln` ánh xạ `Release|Win32` sang `Template|x64`: dựng từng project, `Platform=x64` (gs001 gốc là x64). `Core` dùng cấu hình `Server Release`.
- Cờ liên kết áp cho mọi project làm hỏng project khác: dùng điều kiện theo `$(MSBuildProjectName)` trong `Directory.Build.props`.
- Lần copy mã nguồn trước bỏ `Lib\release` nên thiếu thư viện có sẵn (libdb181...). Bản dựng ra `..\..\..\..\..\..\_bin_v2_\gs\` tức `D:\JX-build\_bin_v2_\gs\`, không đè server thật.

## Đợt 37: khe lệnh đơn của server (2026-11-11)
- `KNpc::m_Command` chỉ có một chỗ, ghi bởi `SendSerCommand`, đọc một lần mỗi tick ở `ProcCommand`; gói client xử lý ngoài tick (mỗi vòng `Breathe`), nên lệnh cuối trong cửa sổ tick thắng. Khi `m_ProcessAI == 0` (đang diễn kỹ năng) mọi lệnh bị bỏ và ô bị xóa.
- Đề xuất hai làn (di chuyển/hành động) có hạn sống tính bằng ms, độc lập với 18 hay 36 Hz. Chi tiết: báo cáo 37. Chưa sửa mã, chưa đo trên server chạy thật.

## Đợt 38: mô phỏng khe lệnh (2026-11-11)
- Mô phỏng ngoài game (`docs-analysis/tools/sim_command_slot.py`) cho thấy: lệnh dừng "cứng" của đề xuất A vẫn làm mất 9,5 % kỹ năng ở 18 Hz; phải dùng lệnh dừng mềm (A2). Đo trước khi sửa mã cứu được một lỗi thiết kế.
- Tick mau (36 Hz) không sửa mất lệnh mà còn làm lệnh bấm sát cuối hoạt cảnh bị bỏ nhiều hơn, vì ô lệnh bị đọc và xóa ở mọi tick kể cả lúc bận.
- Chạy Python bằng `python -I` thì không thấy thư mục script: thêm `sys.path.insert(0, '.')` khi cần `import` module cùng thư mục. Dùng `zlib.crc32` thay `hash()` cho seed (chuỗi bị băm ngẫu nhiên mỗi lần chạy).

## Vòng 39/41 - A2 và xác nhận build
- Build tự dựng chỉ giống EXE gốc về import/export; nguồn mới hơn EXE (chuỗi PasstSkillLevel, TestMaxLife chỉ có ở bản mới). Không suy ra tương thích từ việc build xong.
- ACP 1252 làm chuỗi Trung thành `??`: dùng /source-charset:.936 /execution-charset:.936 và đổi file UTF-8 BOM sang GBK.
- Client không gửi stop khi thả cần (KHRocker.cpp:457-486).

## Vòng 42 - Clone VM thử JX-Test-36
- SAI LẦM: lần clone đầu tưởng treo vì kích thước file trong thư mục đích đứng yên, nên đã dừng nó. Thực tế NTFS chỉ cập nhật kích thước khi đóng file. Đo tiến độ bằng dung lượng trống ổ (`[IO.DriveInfo]`) hoặc `Get-Counter \PhysicalDisk(*)\Disk Write Bytes/sec` (chạy được dù WMI lỗi). Clone 42 GB trên cùng ổ D chạy khoảng 37-42 MB/s.
- `clonevm` chạy qua tool có thể treo đầu ra; chạy bằng `Start-Process` với `-RedirectStandardError` (tiến độ ghi ra stderr) và theo dõi PID.
- Clone lỗi để lại thư mục đích (NVRAM, vmdk, .vbox) -> lần sau báo `VERR_ALREADY_EXISTS` ở bước NVRAM (sau khi chép xong đĩa). Dùng thư mục đích mới (`--basefolder D:\VMs\Test`), không xóa đồ cũ khi chưa duyệt.
- Phần thừa: `D:\VMs\JX-Test-36` (khoảng 42 GB, không đăng ký VM; vmdk `{d0df66c5...}` vẫn nằm trong media registry). Chờ chủ máy duyệt xóa.
- Guest Control với mật khẩu trống thường bị chặn bởi chính sách LimitBlankPasswordUse=1 (mật khẩu trống chỉ dùng được khi đăng nhập trực tiếp trên console).

## 2026-11-12 - gs001 t? d?ng ch?t khi n?p script (x64)
- L?i: `long h = _findfirst()` c?t handle 64 bit -> 0xC0000005 trong `_findnext`. S?a: `intptr_t`. Chi ti?t `patches/fix-findfirst/`.
- WER LocalDumps không th?y crash v́ ti?n tŕnh t? b?t ngo?i l?; dùng b? g? l?i nh? (DEBUG_ONLY_THIS_PROCESS) ho?c tác v? bao ghi mă thoát.
- M?t kh?u `<vm-admin-test>` luu trong Credential Manager (target `JX-Test-36-<vm-admin-test>`), l?y b?ng `scripts/<vm-admin-test>_cred.ps1` (Get-JxCred). Không xoay m?t kh?u m?i l?n n?a.
- Ch? ti?n tŕnh dài: dùng Bash run_in_background; PowerShell ch?n Start-Sleep dài.

## 2026-11-12 - Fix35: client crash khi vào game + gs001 ch?t khi nhân v?t dang nh?p
- Client: tombstone #00/#01 gi?i b?ng `llvm-addr2line` trên `obj/arm64-v8a/libMyGame.so` (kh?p Build ID) -> `KSubWorld::FindRegion` <- `Mps2Map` <- `SyncNpcMin` <- `KTranSence::update`. Gói d?ng b? NPC t?i lúc `m_Region` c̣n NULL (tru?c `LoadMapC`). S?a: `if (!m_Region) return -1;` (`[fix35]`). Sao luu `D:\Android\b\backup-fix35\`.
- Server (b?n t? d?ng x64): `KPlayer.cpp:7606` `CallFunction(...,"ds",nParam)` thi?u tham s? chu?i -> `lua_pushstring` con tr? rác -> 0xC0000005 trong `LuaLibDll strlen` khi ch?y `online.lua`. S?a thêm `""`. "Đang nh?p quá h?n" l?n sau là h? qu?: Bishop v?n tr? d?a ch? gs001 nhung gs001 dă ch?t.
- ?nh n?n nét hon: m?i APK g?c->fix35 có assets gi?ng h?t (ch? khác libMyGame.so), c?u h́nh d? h?a (AppDelegate, GLES3 8888/24/8) không d?i. So v?i APK cu c?a nhà phát hành (`data_cdn/data/jxmobile.apk`, armeabi-v7a): `longin_bg.png` 1280x640/1,64 MB thay 1120x630/0,81 MB, `transence.png` cùng c? nhung 1,45 MB thay 0,84 MB (ít nén màu hon). Không ph?i do fix31-34.
- Rà `CallFunction` l?ch s? tham s?: ch? c̣n ch? 7606 (script `cfcheck.py` trong scratchpad, có báo sai do b?t nh?m tên hàm).
- Fix35 vào game: màn den + "Đang k?t n?i máy ch?" l?p + "Đang nh?p thành công" l?p v?i gs001 t? d?ng. Bishop log m?i ~3 s "LogIn Succes ... port 51189" -> client n?i l?i liên t?c. Nguyên nhân g?c: ngu?n server (`gameserver\Headers\KProtocol.h` 01/2026, `header\GameDataDef.h`) là NHÁNH KHÁC v?i client 2912 (KProtocol.h 11/2025): nhi?u tru?ng máu/mana `int`->`__int64` (d?ng b? d?i, lên c?p, VIP/trùng sinh), thêm `turn`, `m_nLevel`, khác enum `room_*`, `series_*`, `MAX_MESSAGE_LENGTH`. Mă gói (KProtocolDef.h) gi?ng nhau nên không báo l?i rơ, ch? d?c sai d? li?u. Server g?c (exe 2025-11) kh?p client.
- Không ch?y gs001 t? d?ng v?i DB th?t lâu: c?u trúc d? li?u nhân v?t có th? l?ch -> nguy co ghi h?ng.
- Kh?i d?ng gs001 g?c trên VM th?: ch?n t?m 51189 b?ng tu?ng l?a VM trong lúc n?p (rule `JX tam chan 51189 khi nap`), g? khi xong (báo cáo 29).
- Quy?t d?nh ch? máy (2026-11-12): dùng server g?c d? th? Fix35; nhánh A2 t? d?ng t?m d?ng, ch? gi? làm nghiên c?u. VM th? dang ch?y gs001 G?C (`C:\JX\ServerNew\_bin_v2_\gs`), T2/A2 gi? nguyên trong `C:\JX\Bisect\T2`.

## 2026-11-12 - Fix36: gi?t b?n d? + nhánh 36Hz
- Đo tru?c khi s?a: thêm log `JXPERF` (tag logcat) do t?ng ph?n khung (Breathe, SetFocusPosition, Paint, PaintMap, Preprocess, ch? n?p, x? lư gói) và các pha Director (gap/upd/visit/render). Gi? thuy?t minimap/camera SAI: regchg không trùng khung gi?t.
- Nguyên nhân th?t: `KgameWorldVN::custom_update` g?i `TextureCache::removeUnusedTextures()` M?I GIÂY (khi FPS>20) -> khung sau `Paint` gi?i mă/t?i l?i sprite 80-120 ms; 106/106 khung gi?t roi dúng cùng m?c ms trong giây. Có t? b?n g?c. S?a: ki?m tra m?i 10 s, ch? d?n khi cache > 384 MB (do th?c t? 26-47 MB). LDPlayer: khung >40 ms 197 -> 12, h66 ~3/5s -> 0,1.
- LDPlayer làm máy th?: b?t ADB b?ng `basicSettings.adbDebug: 1` trong `vms\config\leidian0.config` (ghi UTF-8 KHÔNG BOM; có BOM th́ LDPlayer reset c?u h́nh). Forwarder/CDN nh?n danh sách `--allow` phân cách d?u ph?y; thêm <TAILSCALE-IP> (chính máy th?t) d? LDPlayer di qua. Tài kho?n game th? `<test-account-2>` trong DB VM th?, m?t kh?u ? Credential Manager (`Get-JxGameCred`).
- Client dang nh?p: k?t n?i Bishop b? ng?t n?u không b?m Đang nh?p trong ~60 s; ph?i m? l?i app.
- Server t? d?ng: thêm 7 struct gói client v? b? c?c client 2912; `tagRoleEnterGame` (Name ngay sau bLock, g?i 66 byte), `tagGuidableInfo` b? 2 tru?ng, `tagGameSvrInfo` g?i kích thu?c g?c. Dùng `structcmp.py` (scratchpad) so struct client/server theo tru?ng.
- 36Hz: ṿng l?p exe d?c `LogicFps` (18/36) t? gs001_cfg.ini; CoreServer nh?p l? ch? ch?y `JxHalfLoop` (n?a bu?c di chuy?n + NormalSync cho NPC dang di), nh?p ch?n ch?y d?y d? nhu 18Hz và `ServeMove` tr? ph?n dă di -> gi? t?c d?, m?i b? d?m th?i gian v?n don v? 18Hz. Exe d?y gói m?i ṿng khi 36 (tru?c: ṿng l? = 9 l?n/s).
- Không ch?y 2 gs001 cùng lúc trên VM 6 GB: b?n th? hai ném ngo?i l? C++ khi n?p (nghi h?t b? nh?).
- S?A L?I gi? d?nh: struct gateway (gs<->Bishop/Goddess) c?a Bishop/Goddess g?c là d?nh d?ng M?I (kh?p header server, ví d? tagQueryMapInfo 145 byte), ch? struct gói CLIENT là d?nh d?ng cu. Đ?i tagRoleEnterGame/tagGuidableInfo/tagGameSvrInfo theo client làm Bishop báo "Máy ch? chua ho?t d?ng" -> dă hoàn tác.
- So kích thu?c th?t thay v́ so tên tru?ng: probe in sizeof cho m?i struct chung, client biên d?ch b?ng NDK clang (aarch64, ch?y trên LDPlayer qua adb), server b?ng MSVC x64. Luu ư client `DWORD = unsigned long` = 8 byte trên arm64.
- gs001.exe t? d?ng: `OperationRequest(SSOI_LAUNCH, (unsigned int)pCloneServer)` c?t con tr? IServer -> crash `KPlayerPK::SetNormalPKState` khi dang nh?p (HUD 0/0, "Đang l?y danh sách nhân v?t"). S?a: tham s? uParam c?a OperationRequest/GetGameData/OperationRequestInfo thành uintptr_t, b? ép (unsigned int) ? exe. C̣n ~270 ch? ép con tr? 32 bit khác trong CoreServer (ph?n l?n mă client) chua rà.
- B? t? d?ng d?y d? (exe+DLL, A2) vào game du?c v?i client Fix36 (HUD dúng, di du?c), tick 18 Hz trung b́nh ~0,8 ms; LogicFps=36 cho SvrFPS 36/36, tick ~0,6 ms.
- Đ?c log console gs001: b? g? l?i nh? (dbg2.cs) chuy?n stdout ra file; AttachConsole t? tác v? không dùng du?c (l?i 5). Log Bishop n?m trong listbox c?a s?: d?c b?ng LB_GETTEXT (C:\JX\sql\lbdump.ps1).

## Phase 46 (2026-11-12)
- Giật màn hình khi di chuyển do nội suy răng cưa 18 Hz (fix33 luôn "đi tiếp từ vị trí đang vẽ" nên khung đầu mỗi nhịp đi chậm ~0,47 lần). Đo bằng tỉ lệ tốc độ camera khung-sau-nhịp/khung-khác, không đo bằng số khung chậm. Sửa: chỉ đi tiếp từ vị trí đang vẽ khi vị trí đó lệch khỏi đường nội suy cũ.
- Khung chậm khi đổi vùng nằm trong pha vẽ (giải mã SPR + tạo texture + đọc SPR từ kho trên luồng chính). Cột "dt" của JXPERF hitch là thời gian khung TRƯỚC, đừng hiểu nhầm thành "thời gian ngoài vòng vẽ".
- Bản đồ lớn mở bằng CHẠM ĐÚP minimap (<6 nhịp); adb: input tap & sleep 0.12; input tap.
- Công cụ sửa file GBK theo byte (bpatch): KHÔNG bao giờ gọi với chuỗi tạm/placeholder. Một lần gọi thử đã thay nhầm một dòng thành "x"; phát hiện nhờ kiểm tra lại và khôi phục từ backup-p46. Luôn so file với bản sao lưu sau khi sửa.
- Phong Lăng Độ: quái đánh nhân vật đứng yên, nhân vật test cấp 200 đã chết một lần (mất ~50% bạc).
- Phong Lăng Độ là khu vực đặc thù: không dùng trực tiếp Thần Hành Phù; phải dùng Thổ Địa Phù trước rồi mới Thần Hành Phù đi thành thị (chủ dự án xác nhận). Dùng ngay khi HP < 40%.

## 2026-11-13 - Goddess khong len khi bam Start (ket sau 3+ lan)
- Sword3PaySys (PID 4704) len binh thuong; SQL Server Running; Goddess chay nhung tieu de van "[Disable]", cong 5001 khong nghe.
- Da thu: (1) ui.ps1 BM_CLICK -> log "clicked [Start]" nhung khong co tac dung; (2) chay lai ui.ps1; (3) WM_COMMAND (id=1) toi cua so cha sau ShowWindow/SetForegroundWindow -> van [Disable].
- Cua so Goddess khi minimize/khong ve lai; chua xem duoc hop thoai/loi nao. Chua kiem tra: log goddes_log (chi co 2026_11_10, 2026_11_11), ket noi SQL cua Goddess, firewall (khong doc duoc: PowerShell khong Admin).
- Bai hoc: FindWindow theo tieu de co the tra 0 khi go qua keyboardputstring; dung (Get-Process X).MainWindowHandle. Dung `$'\''` trong bash de chen dau nhay don vao lenh go.

## 2026-11-13 - U003: giai nen PAK doc-only theo ten GBK
- Hash id phai tinh tren byte GBK cua ten (khong latin-1). Tool: D:\JX1_U003_work\tools\u003_extract.py. Python -I khong doc PYTHONIOENCODING: dung sys.stdout.reconfigure(encoding='utf-8').
- File thu tu ve that la 贴图顺序表.txt (kind file chi toi .txt), ban .ini nho hon khong duoc nap.
- Lenh restart Goddess bi ngat: Stop-Process bi Access denied (khong kill duoc), Goddess PID 9968 van chay, tieu de [Disable]; khong co thay doi.

## 2026-11-13 - U003 G0: ban sort-table that va thu tu nap PAK
- Client nap PAK theo thu tu package.ini, PAK dau tien co id thang (KPakList.cpp:66-77, 171-200). Khong dung "ban moi nhat" hay "ban lon nhat". Tool: D:\JX1_U003_work\tools\pak_winner.py.
- Sort-table MainMan that nam trong updata02 (44 section, 12 slot, khong co canh); setting-new.pak khong nam trong danh sach nap -> khong phan tich file tu setting-new.
- Heredoc python trong bash lam hong dau `\` -> luon dung Write cho script co duong dan Windows/ten \settings\...

## 2026-11-13 - U003 G0 bo sung: skill -> missle, package.ini
- Skill co BaseSkill=1 thi ChildSkillId la MISSLE id (KSkills.cpp:1775,1929), MisslesForm chi la enum hinh dang (SkillDef.h:117). Dung de truy projectile: 375 -> Missles 181 (雷动九天.spr) ; va cham 387 -> Missles 193 (雷击术.spr).
- Xac dinh package.ini that bang md5 assets/package.ini trong cac APK da build (data_cdn\apk): ban A (Resources). Khong dung data/data/package.ini.
- Header SPR: <HHHHHHHH> W,H,cx,cy,frames,colors,dirs,interval o offset 4; khop AnimFileInfo cua Missles.

## U003 G0 bổ sung lần cuối (báo cáo 53)
- Sửa nhận định cũ: UI cooldown gốc CÓ (`KgameWorld.cpp:5527-5540`, `timeLoopLayer`); tìm bằng grep `_nextUseTime`/`cdLabel`, không chỉ grep "cooldown". Bài học: grep theo tên biến thật, không theo từ khoá tiếng Anh.
- `FillLineObstacle` là che sáng, không phải vật cản đi lại; đừng nhầm khi dựng vật cản Unity.
- AttackSpeed (NpcS) = số khung game, nạp ở `KNpcTemplate.cpp:50`.

## U003 G0.5 (báo cáo 55)
- `pak_extract.py` chỉ xử lý nén cả file; entry cờ byte cao 0x11 (TYPE_FRAME, nén từng khung) báo "lookbehind overrun" (66 entry trong spr+skills mẫu). Giải bằng đường khung (`XPackFile.cpp:597-741`); cần bổ sung vào công cụ.
- `interval` SPR không thống nhất: vật thể cảnh = ms thật; quái/người không dùng (kéo giãn theo khung logic); đạn dùng cột Missles.txt.
- Skill 375 sinh 16 đạn (4x4) trễ ngẫu nhiên, KHÔNG phải 4 (sửa báo cáo 52-54). 193 sinh tại vị trí đạn 181 va chạm.
- Bảng sắp xếp bộ phận tra bằng chỉ số hướng sprite 0-based (DirN-1); LineN khớp số khung tuyệt đối.
- Dump file GBK: dùng tools/dump_src.py, Read không đọc được; heredoc làm mất dấu `\` trong đường dẫn.
- Quét spr.pak chỉ lấy mẫu 2500/14616 entry (0 lỗi); phần còn lại chưa kiểm.

## U003 G0.6 (báo cáo 56)
- Client KHÔNG tính sát thương/Hit từ va chạm đạn (`KMissle::ProcessDamage` rỗng, `DoCollision` chỉ sinh hiệu ứng/193). Hit của NPC chỉ chạy khi nhận gói server `s2c_npchurt`; tìm bằng cách truy ngược `DoHurt` -> `ProcNetCommand` -> `NetCommandHurt`.
- Skill 375 và 387 có `DoHurt=0` (cột bảng Skills); đòn thường skill 1 có `DoHurt=80`. Không có Hit cho 375 theo gốc; Hit nếu thêm là DESIGN DECISION.
- `DoHurt` bị bỏ qua khi đang hurt/death: Hit không chồng, không kéo dài; Death ghi đè Hit.
- Damage number gốc = hiệu số máu giữa hai gói đồng bộ (gộp), font `number_16_r.fnt`, tối đa 5 tầng/quái, 50 lần vẽ. U003 dùng từng lần nhận sát thương là khác gốc.
- `DmgInterval` ở server là khoảng chặn gây sát thương mỗi missile (`KMissle.cpp:1788-1796` server).
- Cooldown gốc 375: `TimePerCast=0` nên không có độ dài cooldown; cơ chế UI cooldown vẫn có (BC 53). Cooldown 1 s của U003 là luật thiết kế riêng.
- Bảng NpcS/Skills trích nằm ở file tên `38ebcb17__script_skill.bin` (NpcS) và `ec1243ff__script_skill.bin` (Skills): tên file extract không phản ánh nội dung, kiểm cột header trước khi dùng.

## U003 G0.7 (báo cáo 58)
- `Attrib` trong bảng Skills là phân loại kỹ năng (`m_nAttrib`), KHÔNG chứa sát thương. Sát thương nằm ở `LvlSetting/LvlData` (`lightingdamage_v`...) trong Lua cấp độ (`kunlun.lua`); cả 375 lẫn 387 đều có. Đừng suy nguồn sát thương từ tên cột; lần theo hàm tiêu thụ (`CalcDamage`).
- Missile mang dữ liệu sát thương của skill sinh ra nó: 181 = dữ liệu 375, 193 = dữ liệu 387. Gốc: sát thương tức thì khi va chạm, mỗi missile chạm tối đa một lần (`ColVanish`); không có tick 500/1000 ms (đó là luật U003).
- `nWaitTime` của lần cast người chơi mặc định 0; độ trễ 16 đạn = `WaitTime + k*Data + (+rand(Data) | -rand(Data/2))` tính theo tick logic. Hz client chưa xác minh, không quy ra giây.
- Tên hàm trong báo cáo cũ có thể nhầm biến thể: `ccgetTxtData` (NPC), `_g`, `_p` khác nhau; kiểm lại tên hàm trước khi trích dòng.
- Anchor NPC: `REF_SPOT` + header Center=(0,0) + Width>160 ⇒ trừ (160,192); khớp hình học ani001.
- Toạ độ buildin trong `Region_C.dat` là MPS tuyệt đối, không phải cục bộ vùng. Map 45 thiếu 18/140 Region_C và không có Tree.
- Bảng tên action quái thường (`npc动作表.txt`): chỉ số 7 = Wound, 8 = Die, khớp enum `CLIENTACTION`.

## U003 G1/G2 (báo cáo 59, 60)
- Entry SPR trong PAK có cờ 0x10000000 và dữ liệu bắt đầu bằng `SPR\0` là nén theo từng khung (TYPE_FRAME): header+palette thô, bảng (csize,lsize), khung UCL riêng. `pak_extract.extract` báo `lookbehind overrun`; phải tự ghép lại (đã làm trong Tools của project U003).
- Đạn: `AnimFile2 "6,1,2"` = 6 khung, 1 hướng, interval 2 tick logic mỗi khung; không dùng `interval` ms trong header SPR.
- Hiệu ứng skill neo theo Center của header (181: 196,345): tia sét rơi xuống từ trên cao so với ô sinh; đừng dùng neo (160,192) cho chúng.
- Sửa file Python/Shell bằng heredoc trong Git Bash làm mất `\` và có thể chèn byte NUL; dùng Write/Edit.
- Test skill phải cố định AI quái, nếu không mục tiêu chạy khỏi ô 181 đứng yên và không có va chạm.
- Unity batchmode: Start-Process -Wait có thể treo sau khi build xong; dùng WaitForExit có timeout và đọc log.
