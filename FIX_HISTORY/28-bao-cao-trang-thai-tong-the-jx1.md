# 28 - Báo cáo trạng thái tổng thể JX1 (bàn giao)

Ngày: 2026-11-11, khoảng 16:30 đến 17:00 giờ máy thật. Báo cáo chỉ đọc: lúc viết, không khởi động, tắt, reboot hay sửa gì. Không có mật khẩu, token hay thông tin đăng nhập trong file này.

## TÓM TẮT 5 DÒNG
1. Chỉ có **2 VM đăng ký**, cả hai nằm trên ổ D: `JX-Server-D` (poweroff) và `JX-Server` (đang chạy; đây chính là bản archive, không có VM thứ ba). Chúng **trùng MAC**, không bao giờ để cả hai nối mạng cùng lúc.
2. Môi trường đã từng chạy cả 6 thành phần thành công và được điện thoại chơi thật là `JX-Server-D` (sáng 11/11, `gs001` nạp xong 772 bản đồ). Trên `JX-Server` (archive) hôm nay `gs001` thoát im lặng 3 lần.
3. Hiện chạy trong `JX-Server`: SQL, `Sword3PaySys`, `Goddess`, `S3Relay`, `Bishop`. `gs001` **không chạy**, cổng 51189 đóng. Game chưa chơi được.
4. Máy thật: CDN 8080 và forwarder 56722/51189 đang chạy; task forwarder đã tự chạy sau reboot (đã kiểm chứng), task CDN đã đăng ký nhưng chưa thử qua reboot.
5. Chưa tìm ra nguyên nhân `gs001` thoát. Chưa có tài liệu nào trong repo nói về kế hoạch Unity.

**Cần tôi quyết định: có** (chọn VM chính, xem mục 9).

---

## 1. Sự thật đã kiểm chứng hôm nay (lệnh chạy trong phiên này)

### 1.1 VM (từ `VBoxManage list vms`, `showvminfo --machinereadable`, `list hdds`)
| | `JX-Server-D` | `JX-Server` (archive) |
|---|---|---|
| UUID | `<uuid>` | `<uuid>` |
| Trạng thái | `poweroff` (từ 07:12:14Z) | `running` (từ 08:48:09Z, tức khoảng 15:48 giờ máy) |
| File `.vbox` | `D:\VMs\JX-Server-D\JX-Server-D.vbox` | `D:\VMs\Backup\JX-Server-archive\JX-Server\JX-Server.vbox` |
| Đĩa đang gắn | `D:\VMs\JX-Server-D\Snapshots\{<uuid>}.vmdk` | `D:\VMs\Backup\JX-Server-archive\JX-Server\Snapshots\{<uuid>}.vmdk` |
| Snapshot | 0 | 24 (hiện tại `truoc-doi-ip-roledb`, thêm `apk-bat-dau` nằm cuối chuỗi) |
| RAM / CPU | 6144 MB / 4 | 6144 MB / 4 |
| NIC | bridged, `Realtek PCIe GbE Family Controller #2`, MAC `080027AD6D3F`, cáp `on` | cùng card, cùng MAC, cáp `on` (tôi đã nối lại hôm nay theo yêu cầu của chủ máy) |

- Hai đĩa có **cùng tên file** `{fc58d1dc-…}.vmdk` nhưng ở hai thư mục khác nhau (do clone dùng `keepdisknames`). Không phải cùng một file. Tôi chưa so UUID của hai đĩa trong VirtualBox.
- 27 đĩa đăng ký: 1 dưới `D:\VMs\JX-Server-D\Snapshots`, 1 là `JX-Server.vdi` dưới thư mục `JX-Server`, 1 đĩa nền `Windows 10 x64.vmdk` dưới `JX-disk`, 24 dưới `JX-Server\Snapshots`. Không có đĩa nào dưới `C:\`.
- Chỉ `JX-Server` thuộc `list runningvms`.
- **Phân biệt:** `JX-Server-D` là bản clone độc lập, thư mục gốc `D:\VMs\JX-Server-D`. `JX-Server` là VM cũ đã chuyển từ ổ C sang `D:\VMs\Backup\JX-Server-archive` rồi đăng ký lại (báo cáo 24, 25); thư mục này **cũng là bản lưu trữ duy nhất** của VM cũ. Bản trên ổ C đã xóa theo phê duyệt (C còn trống 162,4 GB theo báo cáo/BAI_HOC; chưa đo lại hôm nay).

### 1.2 Bên trong `JX-Server` (đọc qua cửa sổ PowerShell của user `<vm-user>`, không dùng WinRM)
- Dịch vụ: `MSSQL$SQLEXPRESS` Running, `SQLBrowser` Running, `SQLAgent$SQLEXPRESS` Stopped.
- Tiến trình đang chạy: `sqlservr` (PID 3704), `Sword3PaySys` (1976), `Goddess` (1644), `S3Relay` (3572), `Bishop` (4708). **Không có `gs001`.**
- Cổng LISTENING trong VM: 1433, 5001, 5002, 5003, 5004, 5005, 7776, 56722, 56732. Không có 51189.
- Từ máy thật: 56722 nối được; 51189 đóng (kiểm tra lúc 16:39 và sau đó).
- RAM trống 3728/6125 MB, pagefile 3200 MB (đo lúc `gs001` không chạy).
- Sáu task `JX-*` (Sword3PaySys, Goddess, S3Relay, Bishop, gs001, UI) ở trạng thái Ready (đọc lúc đầu phiên).
- Cách đăng nhập hộp thoại: `Bishop` và `S3Relay` được điền bằng tài khoản dịch vụ `<service-account>` theo cách đã ghi trong `BAI_HOC.md`; không ghi mật khẩu ở đây.
- Sự kiện lỗi Application trong 90 phút: chỉ `vmtoolsd.exe` (VMware Tools sót lại, mã `0xc0000096`) lúc 16:29. **Không có** sự kiện Application Error nào của `gs001.exe`.

### 1.3 Máy thật
- Tailscale: địa chỉ `<TAILSCALE-IP>` có trên adapter (ipconfig). Không đọc được `tailscale status` (chưa tìm đúng đường dẫn CLI trong lệnh kiểm tra), nên **không biết** điện thoại `<TAILSCALE-IP>` đang online hay không.
- Task `JX-Forwarder-Tailscale`: Running, chạy lúc 15:29:29 khi đăng nhập sau reboot, `forwarder.log` ghi `KHOI DONG pid 16736` lúc 15:30:23. Forwarder tự khởi động = **đã kiểm chứng**.
- Task `JX-CDN-8080`: Running, chạy tay lúc 15:38 (tôi gọi `Start-ScheduledTask`), PID 4612, log `khoi-dong-cdn.log`. Tự khởi động sau reboot = **chưa kiểm chứng**. CDN trả 403 cho nguồn không phải điện thoại.
- LISTENING trên `<TAILSCALE-IP>`: 8080 (PID 4612), 56722 và 51189 (PID 16736, forwarder). `portproxy` rỗng.
- WinRM trên máy thật: **Running** (chủ máy chạy `bat_winrm_may_that.ps1`), `TrustedHosts=<LAN-IP>`. Chưa tắt.
- Git: chưa commit; xem mục 6.

### 1.4 `gs001` thoát (3 lần, đo hôm nay)
| Lần | Bắt đầu (console) | Quan sát |
|---|---|---|
| 1 | 16:33:23 | Treo ở "Start loading script:0", cửa sổ biến mất sau khoảng 1 đến 2 phút, cổng 51189 đóng. |
| 2 | 16:37:33 | Cùng chỗ; sống khoảng 2 phút (còn 51189 mở lúc 16:39), rồi biến mất. |
| 3 | khoảng 16:43 | Sống tới "Loaded (23) Map OK ID: 24", 51189 mở, rồi biến mất trong vòng khoảng 1 phút. |

- Dòng lỗi trên console nhưng đã biết từ trước: không mở được `E:/_bin_v2_/gs/Logs/script_errors.txt` (ổ E: không tồn tại), script NPC `5石?对话.lua` nạp lỗi.
- Không có dòng báo lỗi hay thoát nào trên console trước khi cửa sổ đóng (tôi không bắt được khung hình cuối). `gameser_log` 1 byte, các file `gw\*_log` rỗng theo kiểm tra lúc đó.
- Không có sự kiện Application Error của `gs001.exe`. **Nguyên nhân chưa tìm ra.**

## 2. Thông tin lấy từ báo cáo cũ (chưa kiểm lại hôm nay)

### 2.1 Mục tiêu và kiến trúc (CLAUDE.md, báo cáo 00, 07, 16, 22)
- Dựng và vận hành server game JX cũ từ gói không rõ nguồn gốc, chạy trong VM VirtualBox bridged (IP `<LAN-IP>`), thử bằng client Android (Cocos2d-x) từ điện thoại của chủ máy qua Tailscale; sau đó làm bot AI.
- Thứ tự khởi động: SQL Server, `Sword3PaySys` (5002), `Goddess` (5001, bấm Start), `S3Relay` (5003 đến 5005, 7776, login root), `Bishop` (56722, 56732, Login rồi Startup), `gs001` (51189). `S3RelayServer.exe` chưa được duyệt, không chạy.
- Đường vào từ điện thoại: CDN `<TAILSCALE-IP>:8080` (cổng 80 do `ReportServer` giữ, cấm dừng) và `tcp_forwarder.py` cho 56722 và 51189; chỉ nhận `<TAILSCALE-IP>`.
- `gs001_cfg.ini`: `Ip` và `localIp` đặt `<TAILSCALE-IP>` (báo cáo 12).

### 2.2 Phương án VM đã chọn
- Từ 2026-11-11, VM dùng là `JX-Server-D` (báo cáo 17, 22, BAI_HOC mục "Nhân bản VM sang ổ D"). `JX-Server-D` được tạo bằng `clonevm --mode machine` từ `JX-Server` lúc 08:36 đến 08:42 (6 phút) và giữ MAC.
- VM cũ giữ làm bản hoàn tác; sao lưu bằng robocopy (1.090 file, <IP> byte, băm SHA256 hai phía khớp), `unregistervm` và `registervm` lại trên D, rồi xóa bản ở C (báo cáo 23 đến 25).

### 2.3 Đã hoàn thành (theo báo cáo)
- SQL Server, DB `account`, tài khoản thử `<test-account>` (đủ `Account_Info`, `Account_Habitus`), xóa 672 tài khoản thật khỏi DB (báo cáo 01, 02, 09, 10).
- Đổi IP `gs001` sang Tailscale, thay `roledb` rỗng (báo cáo 12).
- Dựng APK debug arm64 (báo cáo 13, 18); điện thoại tải dữ liệu, đăng nhập `<test-account>` và chơi khoảng 5 phút (báo cáo 15); chơi lại qua forwarder, ping khoảng 150 ms (báo cáo 19).
- Sao lưu và chuyển VM cũ, giải phóng ổ C (báo cáo 23 đến 26).
- Khảo sát bot AI (báo cáo 16, chỉ đọc mã nguồn).
- Tự khởi động forwarder (báo cáo 21), script khôi phục phiên Claude (báo cáo 26).

### 2.4 Chưa hoàn thành (theo báo cáo)
- Dọn cuối: dừng CDN/forwarder, tắt WinRM, xóa `TrustedHosts`, xóa dữ liệu thật và lịch sử git chứa `account.sql` (báo cáo 06, 22).
- `JX-UI` đổi hành động nhiều lần, cần đặt về trung tính rồi xóa `ui*.ps1` (báo cáo 19 mục 4).
- Các điểm chưa rõ: 28 bản đồ thiếu `.wor`, cổng 7777 của `S3Relay`, script NPC `5石?对话.lua`, lỗi chiến đấu ở Ba Lăng Huyện, hai kết nối đóng sau 0,2 s, nguồn chữ "XÁC NHẬN TÊN TÀI KHOẢN", `roledb` còn 8192 byte nên chưa chắc nhân vật được lưu, VirusTotal theo hash.
- Bot: chưa triển khai.

### 2.5 Quyết định quan trọng không được tự đổi (chủ máy đã nêu)
- Hỏi chủ máy trước khi chạy từng exe server; không bao giờ chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe`, `S3RelayServer.exe`.
- Không dừng hay đổi `ReportServer`; không tự sửa `iphlpsvc`; không đổi Firewall, `portproxy`, SQL, cấu hình VirtualBox hay mạng VM khi chưa được duyệt.
- Không bật hai VM cùng lúc, không nối mạng VM thứ hai do trùng MAC.
- Không tạo snapshot khi VM đang chạy (live snapshot từng làm `VBoxSVC` crash); không xóa snapshot.
- Truy cập từ xa chỉ qua Tailscale, đúng điện thoại, TCP 56722, 51189 và CDN 8080.
- Không ghi mật khẩu vào file, git hay báo cáo; không push; không commit khi chưa được duyệt; một lỗi thử tối đa 3 lần rồi báo cáo.
- Lệnh cần Admin trên máy thật do chủ máy chạy.

## 3. Điều chưa xác minh
1. Vì sao `gs001` thoát trên `JX-Server`. Giả thuyết chưa kiểm: (a) trạng thái đĩa archive khác `JX-Server-D`: hai VM giống nhau tới thời điểm clone 08:36, sau đó `JX-Server-D` chạy 5 exe, ghi dữ liệu và có thêm vài thay đổi; (b) thiếu bộ nhớ khi nạp (VM 6 GB, `gs001` cần khoảng 2,2 GB và nạp mất khoảng 7 phút theo `BAI_HOC.md`); (c) tương tác với các tiến trình khác khi khởi động. Chưa có bằng chứng cho cái nào.
2. Điện thoại và Tailscale ACL: không biết hiện trạng online; luật `Tailscale-In` chưa đọc lại.
3. `JX-Server` có đúng trạng thái đĩa như lúc clone hay đã đổi sau lần khởi động thử hôm nay (đĩa hiện tại `fc58d1dc` có ghi dữ liệu khi VM chạy).
4. CDN tự khởi động sau reboot (task đã đăng ký, chưa thử).
5. Nguyên nhân gốc `portproxy` không nghe sau reboot (không còn gặp hôm nay vì forwarder chiếm cổng trước; `portproxy` hiện rỗng).
6. VM có tự khởi động exe sau reboot: 6 task `JX-*` không có trigger (báo cáo 26), nên **không tự lên**; chưa thử thực tế.
7. Ổ C còn trống bao nhiêu hôm nay, WinRM trong VM còn bật không, trạng thái snapshot `.sav` của archive.
8. Nội dung hộp thoại nhỏ (nút OK) nằm sau hộp Login của `Bishop`: tôi đã bấm bỏ khi cố tới được hộp Login; có thể là thông báo của `Sword3PaySys`, chưa đọc nội dung.

## 4. Mâu thuẫn và điểm lỗi thời cần giải quyết
1. **CLAUDE.md** còn ghi "VM cũ `JX-Server` và 24 snapshot trên ổ C vẫn giữ" và "Chưa thử khởi động lại máy thật". Thực tế: bản ở C đã xóa, `JX-Server` nay nằm ở `D:\VMs\Backup\JX-Server-archive\JX-Server`; reboot máy thật đã thử hôm nay (forwarder tự lên). Báo cáo 22 cũng lỗi thời ở các điểm này.
2. **Chủ máy gọi** "JX-Server trên ổ D" và "JX-Server (archive)" như hai thứ khác nhau. Dữ kiện: chỉ có một VM tên `JX-Server`, và nó chính là archive.
3. Báo cáo 22 ghi CDN PID 18284 và forwarder PID 18888; nay là CDN 4612 (task `JX-CDN-8080`) và forwarder 16736 (task). Hai tiến trình cũ đã mất sau reboot.
4. `BAI_HOC.md` ghi "Từ nay VM dùng là `JX-Server-D`" nhưng yêu cầu hôm nay chạy server trên `JX-Server`. Hai VM không được cùng nối mạng.
5. Báo cáo 22 mục 9 ghi trigger 6 task `JX-*` chưa rõ; báo cáo 26 đã giải quyết (không có trigger). `BAI_HOC.md` dòng cuối mục `portproxy` vẫn ghi "mâu thuẫn" cũ.
6. `JX-Server-D` đang có cáp mạng `on` trong cấu hình: bật nó khi `JX-Server` đang chạy sẽ trùng MAC và IP.
7. Chủ máy chưa nêu kế hoạch Unity trong repo (xem mục 5.4).

## 5. Source và công việc phát triển

### 5.1 Cấu trúc (đã kiểm hôm nay)
- Repo `C:\Jx1CocoV3`: `Folder\Client2912-…\Client2912\Client\Classes` (client Cocos2d-x: `engine`, `gamecore`, `gamescene`, `gameui`, `ImageStore`, `manager`, `network`, `tools`, `vn`), `Folder\ServerNew-…` (gói server), `SwordOnline\SwordOnline` (mã nguồn server, chưa dựng lại từ nguồn lần nào), `data_cdn` (44 file `.pak`, khoảng 3.295 MB, gốc CDN), `docs-analysis` (báo cáo, script, công cụ PAK), `BaoCao` (các bản quét cũ dạng `.txt`).
- Công cụ PAK trong `docs-analysis/tools`: `pak_extract.py`, `pak_extract_one.py`, `pak_index_scan.py`, `pak_replace.py`, `pak_verify.py`, `simply_crypt.py`, `xfsverjx_compare.py`.
- Bản copy build Android ở `D:\Android\b\Client`; APK hiện dùng: `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` (78.901.355 byte).

### 5.2 Đã nghiên cứu (theo báo cáo và `CLAUDE.md`)
- Đăng nhập, vào game, danh sách máy chủ (`KSelPlayer.cpp`, `Klogin.cpp`, `Bishop/GameServer.cpp`).
- Giao thức: khung gói, mã hóa XOR khóa xoay, khóa từ gói `ACCOUNT_BEGIN` 0x20, mật khẩu MD5 (báo cáo 16).
- Tải dữ liệu qua CDN, `paklist.ini`, `package.ini` (`down=` mã hóa), Range (báo cáo 08, 18).
- Chiến đấu: `mianSkillCallback`, `mainSkillattack`, cờ `0x02`; trap; bản đồ `.wor`; PAK server.
- Lưu nhân vật `Goddess`/`roledb`; bang hội `S3Relay`.
- Khảo sát bot: bot tổ đội bằng client Python không giao diện; bot Tống Kim bằng NPC Lua phía server.

### 5.3 Chưa nghiên cứu hoặc chưa có tài liệu
- Định dạng nội bộ từng loại asset (sprite, anim, âm thanh, bản đồ) ngoài lớp PAK; không có báo cáo nào mô tả chúng (chưa kiểm tra thêm file ngoài danh sách báo cáo).
- Phần render, UI, giao diện tiếng Việt, tài nguyên 23 bản đồ không có ở đâu.
- Các lỗi/điểm đang treo: Ba Lăng Huyện (chiến đấu), 28 bản đồ thiếu `.wor`, cổng 7777, `5石?对话.lua`, nguồn chữ "XÁC NHẬN TÊN TÀI KHOẢN".

### 5.4 Thay đổi code chưa commit và kế hoạch Unity
- `git status`: chỉ `docs-analysis/BAI_HOC.md` (sửa) và các file mới trong `docs-analysis` (báo cáo 24, 25, 26, 28 sau khi viết; script CDN, WinRM, khôi phục phiên; `robocopy-ketqua.txt`). **`Folder` và `SwordOnline` không đổi** (0 dòng trong `git status`). Mọi thay đổi client nằm ở bản copy `D:\Android\b\Client`, ngoài repo.
- **Kế hoạch chuyển client sang Unity: không tìm thấy** (không file `.md` trong repo nào chứa chữ "Unity"). Điều kiện đầu vào hiện có: giao thức và mã hóa đã khảo sát, công cụ PAK, server chạy được trong VM (khi `gs001` ổn). Dữ liệu chưa có: định dạng asset, đặc tả giao thức đầy đủ (danh sách mã lệnh), đặc tả bản đồ và NPC.
- Thiết kế server và bot: mới ở mức khảo sát (báo cáo 16), chưa có thiết kế chi tiết hay mã.

## 6. Git và an toàn
- Chưa commit từ `ff0837c`. Quét bí mật các file mới trước đây: không có mật khẩu. File `robocopy-ketqua.txt` nên không commit.
- Dữ liệu thật vẫn còn trong lịch sử git (`account.sql`), chưa dọn.
- WinRM máy thật đang bật; `tat_winrm_may_that.ps1` (Admin, chủ máy chạy) sẽ tắt và xóa `TrustedHosts`.

## 7. Thao tác của phiên này trong VM (để truy vết)
- Bật `JX-Server` (headless), nối cáp mạng sau khi xác nhận `JX-Server-D` poweroff và `<LAN-IP>` không ai trả lời.
- Khởi động qua task `JX-*` và hộp thoại: `Sword3PaySys`, `Goddess` (phím Space), `S3Relay` (điền `<service-account>`), `Bishop` (điền `<service-account>` rồi Startup), `gs001` 3 lần. Bấm bỏ một hộp thoại nhỏ phía sau hộp Login. Không đổi cấu hình, không xóa, không snapshot, không chạy `S3RelayServer.exe`.
- Mật khẩu dịch vụ `<service-account>` hiện trong ảnh chụp màn hình tôi đã xem (để gõ vào hộp thoại); không ghi vào file nào. Chủ máy nên xem đó là đã lộ trong phiên.

## 8. Kết luận ngắn
- **VM chính xác nên dùng:** `JX-Server-D` (`D:\VMs\JX-Server-D`). Lý do: là VM đã chạy đủ 6 thành phần và được điện thoại chơi thật sáng nay; `JX-Server` (archive) là bản lưu trữ duy nhất của VM cũ và `gs001` trên đó đang lỗi. Đây là khuyến nghị theo dữ kiện, **không tự chuyển**.
- **Server hiện tại:** `JX-Server` chạy, 5 trên 6 thành phần OK, `gs001` không chạy; `JX-Server-D` tắt. Máy thật: CDN và forwarder chạy.
- **`gs001`:** thoát im lặng khi nạp, không sự kiện lỗi, nguyên nhân chưa tìm ra (mục 1.4, 3).
- **Ưu tiên tiếp theo:** (1) chủ máy chọn VM chính; (2) nếu chọn `JX-Server-D`: tắt `JX-Server` bằng ACPI trước, rồi mới bật `JX-Server-D`; (3) nếu muốn điều tra `gs001` trên `JX-Server`: chụp console mỗi 2 đến 3 giây và so cấu hình với `JX-Server-D`; (4) chơi thử điện thoại; (5) thử reboot để kiểm task CDN; (6) viết bài học, ghi nhận mâu thuẫn mục 4 vào `CLAUDE.md`/báo cáo 22 (khi chủ máy đồng ý sửa).

## 9. Cần quyết định
**Cần tôi quyết định: có.** Chủ máy chọn VM chính (`JX-Server-D` hay `JX-Server`) và có cho điều tra `gs001` trên `JX-Server` hay không. Chưa làm gì cho tới khi có trả lời.
