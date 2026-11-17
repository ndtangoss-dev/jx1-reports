# TRẠNG THÁI DỰ ÁN

Cập nhật: 2026-11-16 – Sonnet PM (bắt đầu giai đoạn 0). Sonnet cập nhật file này ở mỗi điểm lưu.

## Dự án đang ở đâu
- Giai đoạn: **0 – Dựng đội, đang làm.** Kế hoạch đã duyệt; D1–D6 đã chốt (Q-10…Q-16).
- 0-01: **xong.** Đã chép 3 lệnh và áp `.claude/settings.json` (chủ dự án cho phép); `/tiep-tuc`, `/ket-thuc-ca`, `/bao-cao` hiện trong danh sách kỹ năng.
- 0-02: **xong phần kiểm kê** (xem `ENVIRONMENT.md`). `JX-Test-36` bridged là chủ ý (báo cáo 42), IP `.150`, không phải sai lệch. Bước tiếp: 0-02b bật VM thử và kiểm server 36 Hz; 0-03 thử `codex exec` (Codex ở `C:\Users\PC\.codex\.sandbox-bin\codex.exe`, không có trong PATH).
- 0-02b: chuỗi server trên `JX-Test-36` đã khởi động được (PaySys, Goddess, S3Relay, Bishop, gs001 `A2T2`; gs001 nối đủ 5001, 5003–5005, 56732). `gs001-A2` (exe tự build) vẫn thoát mã 0xC0000005, đúng như báo cáo 44. Gõ phím qua `VBoxManage` hoạt động. "36 Hz" **chưa kiểm** (A2T2 là nhánh CmdLane).
- **Sự cố mạng nhà tối 16/11 (Q-17):** `JX-Test-36` đã chuyển Host-only, IP `192.168.56.150`, không gateway/DNS ngoài. `JX-Server-D` ở trạng thái aborted từ 20:13 (không do PM). Chi tiết và nguyên nhân [CHƯA XÁC ĐỊNH] ở `ENVIRONMENT.md`.
- WinRM từ máy thật tới `192.168.56.150` đang bị chặn vì TrustedHosts chưa có IP này; cần chủ dự án chạy `docs-analysis/scripts/themTrustedHost_vm_thu_56.ps1` (Admin, có `-Undo`). Chưa chạy.
- Lúc lưu 2026-11-16 21:00: `JX-Server-D` aborted; `JX-Test-36` đang chạy (Host-only); LDPlayer chạy; worker Codex 0-03 (PID 135400) chạy lâu chưa có kết quả.
- Đang chạy được [BÁO CÁO, chưa kiểm lại]: client Cocos P46/P47 trên LDPlayer; server tự dựng 36 Hz trên VM thử `JX-Test-36`; APK mới nhất P46.
- **Main VM `JX-Server-D` (bật headless 21:02, Q-18):** Windows lên tới desktop, ping và ARP đúng MAC `08:00:27:AD:6D:3F` [XÁC MINH 21:13]; có hộp lỗi "VMware Tools Error 0xc0000096" (VM gốc từ VMware, chưa động tới). WinRM 5985, 1433, 80, 445, 135 đều đóng [XÁC MINH]; **Cập nhật 21:25:** đã khởi động chuỗi qua console VM (Q-18/Q-19): PaySys, Goddess, S3Relay, Bishop, gs001 đều lên; gs001 in "Server start succeeded" và nối đủ 5001/5003/5004/5005/56732 [XÁC MINH bằng ảnh chụp]. Từ máy thật vẫn không vào được 5985/1433/5002 (host nay là 192.168.1.12, CLAUDE.md ghi .8): nghi tường lửa VM chỉ cho IP cũ [GIẢ THUYẾT, chưa đọc luật tường lửa]. Profile mạng đã Private. **21:33 (Q-20):** đã thêm luật tường lửa chỉ cho 192.168.1.12; từ máy thật 5985 và 1433 vào được, 5002 vẫn chặn chủ ý (xem ENVIRONMENT.md, có lệnh hoàn tác) [XÁC MINH]. Đọc được tiến trình/cổng qua WinRM: cả 6 tiến trình và các cổng 5001-5005, 7776, 56722, 56732 đang nghe. Lỡ thăm dò cổng 51189 lúc 21:25 khi gs001 vừa nạp xong (không kết nối được, không thấy hậu quả).
- Q-18, Q-19 đã ghi; luật cấm cụ thể cho Main VM đã vào `.claude/settings.json` (thử: `echo` chuỗi poweroff bị chặn, `showvminfo` chạy được). Script `docs-analysis/scripts/jx_mainvm_ensure.ps1` mới (bật VM + chờ chuỗi, chỉ đọc).
- **Windows Terminal (22:35):** `winget install` lỗi 0x80070422 (một dịch vụ Windows bị tắt; chưa tìm ra dịch vụ nào, không đổi cấu hình hệ thống). Thử giải nén gói msix đã xác thực chữ ký thành bản portable: `WindowsTerminal.exe` crash (0xC0000409, sau khi thêm Microsoft.UI.Xaml.dll thì 0xC000027B). Đã thử 3 lần, dừng; đã gỡ bản giải nén. JX Wall dùng nhánh dự phòng (cửa sổ PowerShell xếp lưới). Nhánh `wt` trong script giữ nguyên, [CHƯA KIỂM] vì không có wt chạy được. Muốn có WT thật: chủ máy cài từ Microsoft Store hoặc cho tôi tìm dịch vụ đang tắt.
- **0-05 xong (22:30):** chủ dự án tạo repo private `jx1-source`, đã đẩy `main` và tag `baseline-20261116` lên `ndtangoss-dev/jx1-source` [XÁC MINH: push thành công; chưa kiểm cờ private bằng API].
- **JX Wall (22:15):** `docs-analysis/scripts/jx_wall.ps1` + shortcut Desktop `JX Wall` (chỉ đọc). Mỗi worker có log `D:\JX-wt\<ID>.codex*.log` ghi trong 20 phút gần đây = 1 ô (`Get-Content -Wait -Tail 30`), thêm ô TRANG-THAI.md (vẽ lại khi file đổi) và ô VM/server (`chain_up.log` của JX-Test-36 qua WinRM + `forwarder.log`); lưới tự co theo số ô (tham số `-ActiveMin`, `-MaxWorkers`, `-DryRun`). **Máy chưa có Windows Terminal** (không có `wt.exe`): script tự xếp cửa sổ PowerShell thành lưới toàn màn hình [XÁC MINH: đã chạy thử, 3 ô đúng tiêu đề]; nhánh dùng `wt` toàn màn hình [CHƯA KIỂM, chưa có wt]. Cài bằng `winget install Microsoft.WindowsTerminal` nếu muốn.
- **0-05 làm xong phần cục bộ (22:00):** `D:\JX-source` (nhánh `main`, commit `18c6f18`, tag `baseline-20261116`): 3.432 file, 47,5 MB, chỉ mã nguồn (server `src18` + client `Classes`); `.gitignore` chặn nhị phân, `.ini`, `.sql`, log, `graphify-out` [XÁC MINH]. Quét bí mật: không thấy mật khẩu của máy; chỉ có một chuỗi `gamePass` mặc định trong mã gốc (`CoreServerShell.h:295`), nằm trong mã gốc của game. **Chưa đẩy lên GitHub:** máy không có `gh`; tạo repo riêng tư `jx1-source` cần chủ dự án tạo trống hoặc cho phép dùng token GCM qua API [CHỜ CHỦ DỰ ÁN, không chặn việc khác].
- **0-04 gần xong (21:50):** Graphify dựng được đồ thị server (51.690 nút) và client (20.871 nút); kết quả trong `TOOLS/CONG-CU.md`. Chưa cài hook (`graphify install`).
- **0-07 thử nguội đạt (21:40):** `docs-analysis/scripts/jx_chain_up.ps1` chạy trong `JX-Test-36` qua task `JX-ChainUp` (MU1, Highest): PaySys 21:36:57, Goddess :37:02, S3Relay :37:11, Bishop :37:15, gs001 nối đủ 5001/5003/5004/5005/56732 lúc 21:40:41 (~4 phút) [XÁC MINH bằng `chain_up.log`]. Thiếu: thử qua một lần tắt bật VM, nối `jx_mainvm_ensure.ps1`, đổi tên máy VM thử (trùng tên với Main VM).
- Codex 0-03 **xong** (21:24, gộp vào `jx1-ops`): gọi y như Dispatcher cũ (xem ENVIRONMENT.md). Lỗi cũ do gọi sai model (`gpt-6-luna`), không phải tài khoản [XÁC MINH]. Worker thoát lúc ghi Kết quả (lỗi sandbox 1223 ở lệnh đầu), PM tự commit `1e1beef`.
- Worker đang chạy: không có.

## Đang chờ chủ dự án
- D1, D2 đã quyết (Q-10, Q-11). D3–D6 có mặc định, xem kế hoạch Phần 11.

## Bước tiếp theo (theo thứ tự)
1. Chờ chủ dự án đọc báo cáo mạng trước khi bật thêm VM; không bật lại `JX-Server-D` (Main) khi chưa được phép.
2. 0-03: xử lý worker Codex PID 135400 (chạy lâu, log rỗng): kiểm tra, dừng và giao lại nếu treo.
3. Giai đoạn 0 theo backlog: 0-04 (Graphify; xác minh gói trước khi cài), 0-05, 0-06, 0-07, 0-09, 0-10, 0-08.

## Đường dẫn
| Thứ | Ở đâu |
|---|---|
| Thư mục dự án trên máy | `C:\Jx1CocoV3` |
| Bản sao làm việc của nhánh `jx1-ops` | `D:\jx1-ops-wt` (git worktree của `D:\jx1-reports`) |
| Client đã vá mới nhất | `D:\Android\b\Client\Classes` [BÁO CÁO] |
| Server source đã vá (A2, 36 Hz) | `D:\JX-build\src18` [BÁO CÁO] |
| Gói server gốc | `C:\Jx1CocoV3\Folder\ServerNew-…\ServerNew\_bin_v2_` [BÁO CÁO] |
| VM thử | `JX-Test-36` [BÁO CÁO] |
| Worktree task | `D:\JX-wt\<ID>` (đề xuất) |

## Tiến độ task
(Bảng này do PM cập nhật; `TOOLS/bang_tien_do.py` đọc để dựng Bảng tiến độ. Trạng thái: xong | đang chạy | chờ | lỗi.)

| ID | Trạng thái | Ghi chú |
|---|---|---|
| 0-01 | xong | |
| 0-02 | xong | kiểm kê môi trường |
| 0-03 | xong | Codex, gộp 13fe679 |
| 0-04 | xong | Graphify server + client |
| 0-05 | xong | jx1-source đã đẩy, tag baseline-20261116 |
| 0-06 | xong | Q-19 ghi vào CLAUDE.md và AGENTS.md |
| 0-07 | đang chạy | `jx_env_up.ps1` chạy tốt khi môi trường đã lên (exit 0, 22:14); thử qua tắt bật VM cần chủ: VM thử không tự đăng nhập mu1 (đề nghị bật AutoAdminLogon trong VM thử); Main VM không trả ping lúc 22:14 |
| 0-09 | xong | sandbox Codex chặn ghi ngoài worktree nhưng ghi được C:/Users/Public; `KHOA.md` đang dùng; hook SessionStart `compact` đã cấu hình (echo nhắc + graphify), in thật sau nén CHƯA kiểm |
| 0-10 | xong | chưa có đơn giá USD; có số token và trần tạm Q-22 |
| 0-08 | chờ | đã cập nhật BAN-GIAO; thử phiên mới bị chặn do giới hạn tuần của tài khoản Claude |
| A-01 | xong | `REPORTS/A-01-ban-do-tien-trinh.md` (tổng hợp từ BAI_HOC; chưa kiểm lại trên VM thử vì VM treo) |
| A-03 | xong (PARTIAL: tĩnh, runtime chưa kiểm) | báo cáo REPORTS/A-03-kiem-ke-cau-hinh.md, đã gộp 23:50 |
| A-06 | xong (PARTIAL, nguồn) | REPORTS/A-06-bang-goi-tin.md, gộp 00:30 |
| A-02 | xong (PARTIAL: tĩnh, runtime chưa kiểm) | báo cáo REPORTS/A-02-luong-dang-nhap.md, đã gộp 23:50 |
| A-07 | xong pha tĩnh (PARTIAL) | báo cáo REPORTS/A-07-goc-re-crash-gs001.md; pha debugger trong VM CHƯA chạy: host và VM đều chưa có cdb.exe, chưa có bản Debug có PDB (A-07b) |
| A-05 | xong (tĩnh) | REPORTS/A-05-diem-tuong-tac-gs001.md, gộp 00:40; báo Chat viết B-01 |

## Ngân sách Codex
- Tổng: khoảng 2.000 USD (chủ dự án cho biết)
- **Trần cứng của khóa xingchi** (chủ dự án báo 16/11 21:25): 50 USD / 5 giờ, 200 USD / ngày, 1.000 USD / 7 ngày [BÁO CÁO]
- Đã dùng: 20 USD / 7 ngày tính đến 21:25 ngày 16/11 [BÁO CÁO]
- **Khóa hết hạn 14/02/2027. Nhắc chủ dự án trước 7 ngày (từ 07/02/2027)**
- Quy tắc khi Codex bị từ chối vì chạm trần: coi là hết hạn mức, không phải lỗi code. Không thử lại liên tục; chuyển việc cho agent con Sonnet hoặc chờ tới khung giờ sau
- Khi tăng số worker: giữ tổng chi trong 5 giờ dưới 50 USD (mỗi lần tăng phải tính lại)
- **Đo token Codex (0-10, 22:30) [XÁC MINH từ log `D:\JX-wt\*.codex*.log`, dòng `turn.completed`]:**
  - 0-03 lần 4 (task nhỏ có ích, đọc nhiều file): đầu vào 1.248.292 token (cache 1.173.120), đầu ra 12.860 (suy luận 8.380).
  - 0-09 lần 1 (thử sandbox, 1 lượt ngắn): đầu vào 280.808 (cache 148.480), đầu ra 436.
  - 0-03 lần 3: log không có dòng usage (lỗi sớm).
  - **Không có đơn giá USD** cho nhà cung cấp xingchi / gpt-6.1-sol trong máy này, nên chưa quy ra USD [CHƯA KIỂM]. Cách đo tiền thật: chủ dự án đọc "Đã dùng" ở bảng điều khiển khóa trước và sau một đợt chạy; số trên cho biết tỉ lệ: một task vừa ~1,2 triệu token đầu vào, 90% là cache.
- **Trần tạm của PM (Q-22):** tối đa 3 worker song song; một lượt giao việc không quá 2 task L2 cùng lúc; PM tự dừng giao Codex khi `Đã dùng` 7 ngày ≥ 700 USD hoặc trong ngày tăng ≥ 150 USD (75% trần cứng 200). Cập nhật dòng `Hôm nay: N USD` ở mục này khi chủ dự án báo số mới; hook Stop dùng dòng đó.
- Số worker hiện tại: 0 (bậc khởi đầu: 3)

## Môi trường đang bật lúc lưu
(Sonnet ghi: VM nào đang chạy, server nào đang lên, LDPlayer, worker.)

- **Bảng tiến độ (22:10):** `TOOLS/bang_tien_do.py` dựng `D:\JX-dash\index.html` từ BACKLOG.md, TRANG-THAI.md (bảng "Tiến độ task") và KHOA.md; tự dựng lại sau mỗi commit nhờ hook `post-commit` của kho `D:\jx1-reports` (hook nằm ngoài git). Bản Artifact riêng tư: https://claude.ai/artifact/7bUxS1STLrmZ6btueV3eiy (PM xuất bản lại khi cập nhật). Bản Tailscale (cổng 8092, kèm nút sơ đồ Graphify): `docs-analysis/scripts/dash_server_tailscale.py`, chờ Tailscale bật (máy thật báo stopped, không có địa chỉ 100.x) và chờ chủ máy chạy `mo_cong_dash_8092.ps1` bằng Admin (hoàn tác `huy_cong_dash_8092.ps1`) [CHƯA KIỂM: chưa phục vụ được].
- **Graphify install (22:05):** chủ dự án cho áp dụng; `graphify claude install` tại `C:\Jx1CocoV3`: CLAUDE.md thêm 11 dòng, `.claude/settings.json` thêm 3 hook (PreToolUse Bash|Grep, Read|Glob; SessionStart compact). Hook SessionStart cũ giữ nguyên [XÁC MINH]; sao lưu `.claude/settings.json.bak-truoc-graphify`; gỡ bằng `graphify claude uninstall`. Hook chỉ có tác dụng ở phiên mới; `/tiep-tuc` chưa chạy lại thật trong phiên mới [CHƯA KIỂM].
- **0-09 thử sandbox (22:00):** Codex `workspace-write` ghi được trong worktree, bị chặn ghi `D:\JX-wt\` ngoài worktree, nhưng ghi được `C:\Users\Public\` (đã xóa file thử) [XÁC MINH].
- **Hook Stop + Q-21 (22:25):** `TOOLS/stop_guard.py` khai báo trong `C:\Jx1CocoV3\.claude\settings.json` (mục `hooks.Stop`). Đã thử bằng dữ liệu giả: còn task → chặn kèm task kế tiếp (0-07); có `/ket-thuc-ca`, thẻ `[DUNG-CAN-CHU]` còn hiệu lực, hoặc `Hôm nay: 210 USD` → im lặng cho dừng [XÁC MINH]. Chưa thử trong phiên Claude Code thật sau khi khai báo [CHƯA KIỂM]; mục lỗi 3 lần chưa thử riêng. Gỡ: xóa khóa `Stop` trong settings.json.
- **Giới hạn tuần Claude (22:50):** thử mở phiên mới không đầu (`claude -p`, bước đọc BAN-GIAO của 0-08) trả về "You've hit your weekly limit · resets Nov 19, 1am (Asia/Bangkok)" [XÁC MINH, nguyên văn thông báo]. Nghĩa là phiên PM có thể không chạy được cho tới 19/11 01:00 (giờ Bangkok). 0-08 và `/tiep-tuc` trong phiên thật CHƯA thử.

- **0-07 vòng tắt bật VM thử (22:40):** AutoAdminLogon mu1 trên JX-Test-36 đã bật (mật khẩu trống; sao lưu giá trị cũ ở `C:\JX\winlogon.bak.json` trong VM). Thẻ `[DUNG-CAN-CHU]` đã xóa. Sau `Restart-Computer` VM không lên lại (màn hình đen, không ping/WinRM); `controlvm reset` không cứu; `poweroff` kẹt ở trạng thái `stopping`, tiến trình `VBoxHeadless` PID 132960 không giết được (Stop-Process bị từ chối, taskkill báo Not found), `VBox.log` của VM đứng từ 20:48. Cần chủ máy chạy Admin: dừng/khởi động lại dịch vụ VBox hoặc tắt hẳn tiến trình, bật lại `JX-Test-36` [CHƯA KIỂM: chưa biết nguyên nhân gốc; đã loại ổ đĩa đầy, D: còn 1,38 TB].
- **Main VM 192.168.1.50 (22:40):** hiện trả ping bình thường (đã đo lại, chỉ đọc theo Q-18). Máy thật đang là 192.168.1.12 (không phải .8), cùng lớp mạng. Log VBox của Main VM chỉ ghi đến 21:13 rồi đứng (`AHCI#0 Port 0 reset`, `Cancelling all active requests`), tức có một lần đĩa ảo/ổ D: bị đứng khoảng 21:13, trùng thời điểm log VM thử đứng; lúc 22:14 mất ping là khớp với đợt đứng này [SUY LUẬN, chưa chứng minh]. Không có lỗi đĩa trong nhật ký System 4 giờ qua.
- **Worker Codex tách phiên (22:45, Q-23):** shell của Claude Code nằm trong Job Object và tiến trình con cùng job (đã đo); có bị giết khi đóng phiên không CHƯA kiểm. Đã làm `TOOLS/chay_codex.ps1` giao qua Task Scheduler (thử với worker giả: chạy xong, ghi log và cờ `.done`); chưa thử với codex thật. Quy tắc giao sẵn hàng đợi khi hạn mức phiên >80% ghi ở QUY-TAC mục 13 và Q-23.
- **Codex lỗi model (22:58):** A-03 và A-06 thoát `exit=1` ngay: `404 Model "gpt-6-luna" is not supported by any configured account in this group` (xingchiapi.com). `~/.codex/config.toml` dòng 1 đang đặt `gpt-6-luna`. Theo quy tắc không đổi model/cấu hình Codex nên tôi không sửa; chủ dự án cần kiểm tài khoản/nhóm xingchi hoặc cho biết model đúng. Tăng worker (Q-24) vô ích khi Codex chưa gọi được. Launcher tách phiên chạy đúng (log, cờ `.done`). Trong lúc đó PM tự làm việc Sonnet được (A-01).
- **Codex khôi phục (22:56):** model cố định `gpt-6.1-sol` + reasoning max (Q-25); A-02, A-03, A-06, A-07 chạy tách phiên (4/6 worker; 5/6 từ 23:19 khi thêm A-05). Lỗi 404 cũ coi như xong. Hướng Bot (a), mốc đầu, trần 100, nhịp 18 Hz: Q-26, Q-27.

- **kill-test-vm kiểm chứng (16/11 ~23:40):** JX-Test-36 aborted; jx_env_up -BoQuaMain lên chuỗi đủ 23:48 (cổng 5002,5001,5003-5005,56722,56732,51189). A-02/A-03 xong; Codex không commit được (git metadata ngoài sandbox), PM gộp tay.


- **A-07 (00:20):** pha tĩnh xong, gộp. Pha debugger bị chặn bởi thiếu cdb.exe (không thấy trong Windows Kits trên host, VM không có Internet) và chưa dựng bản Debug trong D:\JX-build\a07. Hướng thay thế không cần cdb: WER LocalDumps (script đã có) rồi đọc dump bằng công cụ có sẵn; chưa làm.


- **E-01 giao (00:30)** Codex gpt-6.1-sol, mốc đầu Bot (Q-26), offline test; chi tiết giao thức thiếu ghi vào REPORTS/E-01-thieu-giao-thuc.md.



- **D-01, C-01 giao (00:45)** Codex; cùng E-01 là 3/6 worker. A-05 xong, đã gộp.


- **C-01 xong (00:40):** TOOLS/jxadm, 22 test offline pass; chưa chạy với SQL thật (chưa kiểm). Gộp.


- **E-01 xong (00:41, PARTIAL):** JX1_OPS/BOT, 29 test offline pass; chưa chạy server thật; thiếu record đồng bộ thế giới phía nhận GS nên chưa đạt mốc 'đi, đánh' (REPORTS/E-01-thieu-giao-thuc.md).


- **D-01 xong (00:43):** REPORTS/D-01-bang-hoat-dong.md (tĩnh). Gộp. Không còn worker chạy.


- **C-03, P-02 giao (00:46)** Codex; 2/6 worker.


- **C-03 xong (00:57):** TOOLS/jxweb, 6 test offline pass, bind 127.0.0.1; chưa chạy với dữ liệu thật.


- **P-02 xong (01:03):** TOOLS/bench, test offline trên dữ liệu mẫu; chưa đo thật. Không còn worker chạy; việc kế: A-04 (Sonnet).


- **A-04 xong (01:10):** REPORTS/A-04-kien-truc-tong.md (tổng hợp, có nhãn tin cậy).


## A/B Codex effort (Sonnet, 2026-11-17 01:12) - tom tat faction.ini, Sol, 1 lan moi muc
| Effort | Thoi gian | Token vao/ra/suy luan | Chat luong |
|---|---|---|---|
| low | 112 s | 284k / 1533 / 76 | Dung: 16 muc, co so dong |
| medium | 96 s | 359k / 2024 / 158 | Dung, day tuong tu |
| high | 89 s | 357k / 2034 / 407 | Dung, day tuong tu |
Ket luan so bo: voi viec nho doc-tom-tat, effort khong doi toc do ro (nhieu hon sai so, moi muc 1 mau); thoi gian chu yeu do doc file. Chua thu Astra, service_tier=fast, profiles (con lai #010/#011). Giu Sol; effort L1 low, L2 medium, L3 high; A-08/B-02 dang chay high.

## [ĐANG CHỜ hạn mức Codex, tiếp tục khi het 429] (Sonnet, 2026-11-17 01:27)
Codex/xingchi tra 429 Too Many Requests o moi lenh (ke ca ping 1 tu, effort low) sau khi A-08a-d xong. A-07b (da giao, max) va B-02 (da co KVisibility.cpp/.h dang do) bi ngat; worktree D:\JX-wt\A-07b va D:\JX-wt\B-02 giu nguyen. Thu lai moi ~20 phut bang AB-ping; khi OK thi chay lai A-07b, B-02 (-Effort high), dong thoi toi da 3 worker de tranh 429.

[02:18] Codex het 429; chay lai A-07b va B-02 (high), toi da 2 worker dong thoi.

[02:27] Dang chay A-07b, B-02, A-10 (high); A-09 cho slot. chay_codex them --add-dir de Codex commit duoc (thu lan dau o A-10).

[02:55] B-02, A-07b xong (build, chua chay). A-09, A-10 dang chay. Viec ke: sua link ms64.lib (A-07c), O-01 duyet B-02.

[03:06] A-07c: build tu nguon chay duoc khi tat HighEntropyVA, bat co thi crash 0xC0000005 ~40s. Can A-07d (tim cho cat con tro bang dump). VM thu dang chay ban A-07c nohe.
- [03:30] A-07: bo A-07c moi chet 0x80000003 sau ~225 s (HEVA bat/tat deu vay), chua biet dong console cuoi. VM thu da khoi phuc bo on dinh (nohe exe D41A273C0F12 + DLL goc). Tao TASKS/A-07d.
- [04:05] A-07d xong (nghi /RTC1 + 4 loi mang), A-07e xong (build khong RTC, SHA gs001 988175A7.., HEVA tat 91BC8EB67058, nhanh fix/a07c-link a52791d). Dang thu trong JX-Test-36 tu 04:02:49 (bo A-07e moi, DLL moi).
- [04:13] A-07e: bo moi song >10 phut (cu chet 225 s), nghe 51189. Dang giu chay de do on dinh; chua thu HEVA bat.
- [04:35] A-07: bo A-07e (build khong RTC, 4 loi mang sua) chay on voi HEVA BAT >10 phut (hai loi cu 0xC0000005 va 0x80000003 deu het). Chua co tai. Can giu chay lau + cho Chat duyet O-01.

## Bảng worker Codex (Chat #014.3a; từ nay ghi đủ cột khi giao/xong)
| Task | Xong | exit | Effort | Token vào/ra | Số 429 |
|---|---|---|---|---|---|
| A-02 | 0 2026-11-16T23:42:35 | | ? | chưa ghi | chưa ghi |
| A-03 | 0 2026-11-16T23:45:06 | | ? | chưa ghi | chưa ghi |
| A-05 | 0 2026-11-17T00:26:12 | | ? | chưa ghi | chưa ghi |
| A-06 | 0 2026-11-17T00:23:11 | | ? | chưa ghi | chưa ghi |
| A-07 | 0 2026-11-17T00:20:11 | | ? | chưa ghi | chưa ghi |
| A-07b | 0 2026-11-17T02:45:11 | | high | chưa ghi | chưa ghi |
| A-07c | 0 2026-11-17T03:00:35 | | high | chưa ghi | chưa ghi |
| A-07d | 0 2026-11-17T03:43:11 | | high | chưa ghi | chưa ghi |
| A-07e | 0 2026-11-17T04:02:07 | | high | chưa ghi | chưa ghi |
| A-08a | 0 2026-11-17T01:12:16 | | ? | chưa ghi | chưa ghi |
| A-08b | 0 2026-11-17T01:16:56 | | ? | chưa ghi | chưa ghi |
| A-08c | 1 2026-11-17T01:15:41 | | ? | chưa ghi | chưa ghi |
| A-08d | 0 2026-11-17T01:11:53 | | ? | chưa ghi | chưa ghi |
| A-09 | 0 2026-11-17T02:56:11 | | high | chưa ghi | chưa ghi |
| A-10 | 0 2026-11-17T02:51:19 | | high | chưa ghi | chưa ghi |
| AB-high | 0 2026-11-17T01:09:15 | | high | chưa ghi | chưa ghi |
| AB-low | 0 2026-11-17T01:09:36 | | low | chưa ghi | chưa ghi |
| AB-medium | 0 2026-11-17T01:09:21 | | medium | chưa ghi | chưa ghi |
| AB-ping | 0 2026-11-17T02:17:09 | | ? | chưa ghi | chưa ghi |
| B-02 | 0 2026-11-17T02:36:13 | | high | chưa ghi | chưa ghi |
| C-01 | 0 2026-11-17T00:39:12 | | ? | chưa ghi | chưa ghi |
| C-03 | 0 2026-11-17T00:55:56 | | ? | chưa ghi | chưa ghi |
| D-01 | 0 2026-11-17T00:42:21 | | ? | chưa ghi | chưa ghi |
| E-01 | 0 2026-11-17T00:40:30 | | ? | chưa ghi | chưa ghi |
| P-02 | 0 2026-11-17T01:01:53 | | ? | chưa ghi | chưa ghi |
- [04:37] RỦI RO (Chat #014.1): Engine đổi sang CRT tĩnh (/MT) khi bỏ /RTC1 → cấp phát qua biên DLL có thể lệch; nếu thấy crash lạ khi free thì nghi chỗ này đầu tiên. WER LocalDumps đã bật cho gs001.exe trong JX-Test-36 (C:\JX\dumps, full dump, giữ 3).
- [05:00] 429 lần nữa (B-02b, giao 04:57, chỉ 1 worker chạy): codex báo 'stream disconnected: Upstream service temporarily unavailable' rồi 'exceeded retry limit, last status: 429 Too Many Requests', request id 37959130de3cf31c83d8f18437264ba4. Không thấy Retry-After trong log. Thử lại sau ~10 phút.
- [05:11] B-02b: 429 lan 2 (giao lai 05:00, request id e6ba3a47a26c576fb07134a49f1d5371). Cho 20 phut roi thu lan 3; neu van 429 thi ghi [DANG CHO han muc] va bao trong bao cao dem.
- [05:36] B-02b: 429 lan 3 (request id 3d3e1be9...). Codex dung xong Engine+LuaLibDll roi chet. PM tu dung tiep CoreServer+GameServer (checkpoint-b02b-a07e, --resume). Khong giao lai Codex.
- [05:45] B-02b XONG: build 5/5 exit 0 (PM tu dung, Codex 429 x3). Xem REPORTS/B-02b-build-tren-a07e.md. Chua chay VM. gs001 A-07e HEVA-on van song (>4300s).
- [05:50] B-02b: da gỡ HEVA ban sao (D:\JX-build\b02b\gs001_nohe.exe), Defender may that loi lan 2. 0-08 doi chu may (can dong/mo Claude Code).
- [05:55] E-01b giao Codex (high): bo tach ban ghi dong bo the gioi cho Bot (worktree D:\JX-wt\E-01b). 0-08 cho chu may.
- [08:05] 0-10 (do chi phi Codex, 9 task xong, tu log `turn.completed`): input trung binh ~6,5 trieu token (~95% la cache), output trung binh ~31,5 nghin (min C-01 1,7M/24,7k; max A-07b 13,9M/42,4k, A-05 10,2M/49,3k). Chua co don gia/tran 5 gio tu xingchi nen KHONG tinh tien; tran tam: toi da 3 worker dong thoi (#013), 429 xuat hien khi chay lien tuc ~3 worker + retry (B-02b 3 lan 429 luc 04:59-05:34).
- [08:12] E-01b XONG (PARTIAL): worldsync.py, 41 test offline pass, chua chay server that; xem REPORTS/E-01b-thieu-giao-thuc.md. gs001 A-07e HEVA-on song 13.465s (~3h45).
- [08:25] [Q-37] B-02b dua len JX-Test-36 (bo A-07e giu *.a07e-set tren VM), Enabled=0 mac dinh; theo doi uptime. Giao A-12 (high, worktree D:\JX-wt\A-12) theo #017/#018. Con: A-11 (sol vs astra), A-13 (PM tu lam). Dang cho Codex xong A-12.
- [08:40] Ping astra qua xingchi OK (17s, 'OK', khong 429). Bat dau A-11 (sol vs astra) bang script D:\JX-wt\A11\run_ab.ps1.
- [10:25] A-12 XONG, da gop vao jx1-ops (REPORTS/A-12-hao-huu-mac-do.md, khao sat tinh). A-11 dang do: T1 sol 26s vs astra 20s, khong 429; T4 sol treo >2h (da kill, chay lai co gioi han 400s); xem REPORTS/A-11-sol-vs-astra.md. Giao E-05a (high, D:\JX-wt\E-05a). Khoa xingchi thu hai: CHUA tao (dang kiem trang).
- [10:40] Khoa xingchi #2: CHUA tao duoc. Trinh duyet trong app chua dang nhap xingchi (trang Login), Chrome extension khong co may nao ket noi; nhap mat khau la viec cam. Can chu may dang nhap xingchi trong trinh duyet trong app (hoac tu tao khoa, cat ngoai kho). Tam thoi khong 429 voi khoa cu (A-11, astra chay duoc).
- [10:55] [Q-34 so lieu tien that, bang dieu khien xingchi 10:16] 7 ngay: sol 1.968 yc, 297,0M token, tra that 34,61 USD (chuan 138,45); astra 2 yc, 126,7K token, 0,18 USD. Hom nay 17/11: tra that 14,46 USD, cache 84,8%. Ti le thuc/chuan 0,25; ~0,0176 USD/yc sol. Da dung ~3,5% tran 7 ngay, ~7% tran ngay: tien KHONG phai nut that; nut that la 429/so worker. Se tang song song toi 8 worker khi co viec doc lap. A-11 co thuc su chay astra (T1 usage ghi nhan); doi bang dieu khien tang yc astra de xac nhan.
- [10:55] Hook thu 10 phut (Q-40) da gan. Da doc den #034.
- [10:35] A-11 XONG: sol vs astra, 3 bai x 2, ca hai dung het, 0 lan 429; astra it hon ~15% token input, thoi gian lon xon (n=1). Ket luan: astra lam be thu hai cho doc/tom tat/soan task (effort low), sol cho sua ma/build. REPORTS/A-11-sol-vs-astra.md. Dang chay: E-05a, B-02c, C-02. Khoa xingchi #2 chua tao (cho chu may cai Chrome extension / dang nhap).
- [11:15] khóa #2 OK (JX K2, đã thử qua codex exec, trả lời bình thường); thêm K3 (đã thử OK), K4. Tạo trong Chrome của chủ máy, đăng nhập sẵn; không đổi cài đặt/thanh toán. Giá trị khóa chỉ lưu ở C:\Users\PC\.jx1keys (ProgramData cần Admin nên không dùng; chủ máy duyệt: không cần Admin). chay_codex.ps1 nhận JX_CODEX_KEY=<tên>, chỉ ghi tên.
- [11:15] Đã gộp C-02 (khảo sát is_bot, tĩnh) và E-05a (khung TESTER, 14 test + 41 BOT đạt, máy chủ giả). B-02c đã commit (026c628 trong jx1-source worktree), đang dựng. A-14 chạy với K2.
- [11:30] B-02c dựng xong, đã lên VM thử (gs001 sống ≥207 s, Enabled=0). Defender VM sạch. Việc tiếp: thử Enabled=1 Solo bằng 2 bot (cần E-05b/TESTER), đo B-04. Đang chạy: A-14 (K2), E-05b (K3), E-03 (K4).
- [11:35] Gộp E-03 (điều phối dân số, 53 test BOT đạt, chưa nối server).
- [11:50] Gộp E-05b (full_cycle, TESTER 18 test; bước tạo nhân vật/kill/logout BỎ QUA vì thiếu gói tin).
- [11:5x] A-14 xong, gộp vào jx1-ops. Giao E-07 (gói tạo nhân vật/logout, K2), E-08 (gói skill/NPC/kill, K3), high. A-11c còn chạy.
- [11:1x] A-11c xong: sol ~30 tok/s mọi khóa, không 429 ở tải 3; astra 503 ở mọi khóa → A-11b bị chặn tới khi xingchi bật astra. A-11b hoãn tới khi astra lên lại (Chat #040); ping astra mỗi 15 phút.
- [11:15] B-03 xong (22/22 offline, tiêu chí 3/4 TODO chờ E-07/E-08). K4 chạy tốt. Còn E-07/E-08 chạy.
- [11:16] E-08 xong (gói 69/76/77/91/92, C2S 77; killerID không có → xác nhận kill [CHƯA KIỂM]). Chờ E-07.
- [11:23] E-02 xong (BOT 65/65 offline). Chờ E-07 rồi E-09.
- [11:27] E-07 xong (gói tạo nhân vật/logout, tĩnh). Tiếp: E-09.

## Bảng hiệu quả tiểu yêu (Q: thư #041; cập nhật mỗi 30 phút)
[11:28] Nguồn: dashboard xingchi 11:25 (số Chat chụp) + log codex.
| Chỉ số | Giá trị | Mục tiêu |
|---|---|---|
| Đồng thời TB (Little: RPM/60 × 42,76 s) | ≈1,4 (lúc 11:25, gần như không worker nào chạy) | ≥6 |
| Đồng thời hiện tại | 6 worker chạy (K2:2, K3:2, K4:2) từ 11:28 | ≥6 liên tục |
| Task xong/giờ | 38 marker .done hôm nay (tính cả đo thử); 7 task thật xong từ 10:57 đến 11:27 | — |
| USD/task | 38,60 USD / 2.140 yc (tổng); hôm nay 18,25 USD cho 988 yc; mỗi task thật ≈ [CHƯA TÍNH từ dashboard] | — |
| % cache | 111,1M/134,7M ≈ 82% (hôm nay) | ≥85% |
| % token ra / tổng | 854,6K/134,7M ≈ 0,63% | cao hơn = đỡ đọc lại |
| % yêu cầu lỗi | 503 astra 100% (9 yc astra đã trả tiền hôm nay; ping 15 phút ghi D:\JX-wt\A11c\astra_ping.log); sol: chưa thấy 429 | ~0 |
| % rảnh vì chờ PM/duyệt/build | 11:16–11:24: chỉ 1–2 worker chạy (PM trễ giao việc) | <10% |
**Nút thắt hiện tại:** hàng đợi giao việc của PM, không phải model/khóa; đã giao 6 task độc lập (E-10, E-09a, B-04a, E-11, E-12, B-02d) để chạm ≥6 đồng thời. Cần thêm task khi 1 xong (giữ ≥6 sẵn sàng).
- [11:44] Tạo khóa K5 (không cần mật khẩu/2FA; lưu .jx1keys). Khóa riêng có hiệu lực (khóa giả → 401). Dashboard xingchi cập nhật usage theo khóa chậm vài phút. Giao thêm A-15a/b/c (K5). Tổng 12 worker (K2:3 K3:3 K4:3 K5:3).
- [11:45] Dựng lại monitor b55akq14o (30 phút, theo dõi mọi .done của 12 worker); monitor cũ b1mop5z3c hết hạn. Phút không có monitor: 0.
- [11:53] Merge A-15a (bốn phái đầu, khảo sát tĩnh). Giao H-01 (K5) theo #045; H-02..H-08 xếp hàng chờ chỗ trống; H-04 theo #046 là gom ghi chép cũ, không khảo sát lại.
- [11:58] Merge A-15b; giao H-02 (K5).
- [12:02] xingchiapi.com trả 522 (Cloudflare, máy chủ gốc timeout); speed.py K2 không trả lời 100s; log 9 worker đứng từ ~11:55. Nghi sự cố nhà cung cấp, đo lại sau. K6: bấm Create lúc 12:00, chưa xác nhận có tạo; chủ lệnh tạo khóa từ từ, tạm dừng.
- [12:05] H-04 (#047): PM tự làm, REPORTS/H-04-hieu-ung-vu-khi.md; qh7 sao lưu D:\JX-backup\qh7. API xingchi bình thường lại (K3 test 109s/2,9k token). Đã đọc #47.
- [12:11] Merge H-02 (magic attrib; PARTIAL do thiếu quyền commit, khảo sát tĩnh đủ). Giao H-03 (K5).
- [12:13] Chủ duyệt sao lưu: robocopy D:\Android\b\Client -> D:\JX-backup\Client-qh7 (13261 file, 2,19 GB, 0 lỗi; chỉ copy, không xóa gốc).
- [12:26] #48: bản sao D:\JX-backup\Client-qh7 có manifest SHA256 (13261 dòng, D:\JX-backup\Client-qh7.sha256.txt) và git cục bộ, tag qh7-base (KHÔNG có remote; đẩy lên repo riêng tư chưa làm vì 2,2 GB + cần chủ duyệt). So mã: KgameWorld.cpp sửa 14/11 10:48, sau APK qh7 (10:05) và trước qh8 (10:51) => mã hiện tại KHÔNG còn đúng qh7 ở file này; các file nguồn khác (KItem.cpp 13/11) không mới hơn qh7. Chưa diff chi tiết (chưa có bản qh7 của KgameWorld.cpp; bản .bak-bolt8 gần nhất, chưa so).
- [12:26] #49 F-02 (Groq/Cerebras): hoãn. [GIẢ ĐỊNH-CHỜ-CHAT] tạo tài khoản + đăng nhập cần chủ tự làm (mật khẩu/2FA, quy tắc #035); ưu tiên thấp, không chặn việc khác. Phần script đo HTTP sẽ soạn khi có khóa.
- [12:38] Monitor brxg9r2zm hết hạn; dựng lại ngay (phút hở ≈0-1, không có .done nào bị lỡ: quét lại .seen-all).
- [12:38] Merge A-15c (phái 9-cuối; A-15 xong cả 3 phần). Đọc #50. Giao H-05, H-10 (K5). Hàng chờ: H-06,H-07,H-08,H-11,H-12,H-09. Monitor bjbhhhbj9 dựng lại 12:38; A-15c .done 12:29 bị trễ ~9 phút do monitor hết hạn.
- [12:47] F-02 xong: Groq gpt-oss-120b ~550 tok/s (sol ~30). Khóa ở .jx1keys\JX-GROQ.txt, không vào kho.
- [12:51] #51: F-02 cập nhật header Groq thật (1000 yc/ngày, 8000 TPM); thêm P3 'trợ lý nhanh' vào thiết kế Tổng quản.
- [12:51] E-13, G-01, F-01: log đứng ở ~5KB suốt 70 phút từ 11:38 (trùng sự cố xingchi 522 lúc 12:00) => chạy lại (lần 1, chưa có tiến độ nào mất). Các worker khác sống, log cập nhật 12:36.
- [12:53] Nghi van nha cung cap nghen: phan lon log worker khong ghi tu ~12:36 (E-13/G-01/F-01 da chay lai). Khong giao them cho den khi log cua worker song lai; monitor bh7nuaktn dem log hoat dong moi phut (het han ~13:25).
- [13:04] #052: Groq huy, khoa .revoked, P3 danh dau huy.
- [13:05] F-01 xong (merge). Lan cuoi bi 429 Too Many Requests tren K4 (retry limit) => 429 la nguyen nhan nghen; 10 worker im tu 12:36 co the dang cho retry 429.
- [13:10] SU CO DUNG IM #2: 10 worker im 12:36-13:09 (SSE idle timeout + 429 xingchi), API da thong; chay lai het 10 (lan 1), chia lai khoa <=3/khoa. Monitor bao STALL>10min. Bang hieu qua: worker dung >10 phut = 10 luc 13:09.
- [13:16] TRANG THAI: SU CO NHA CUNG CAP xingchi (chung, theo chu du an #055) da qua; 10 worker chay lai 13:09 va dang song. Khong ha quan so. Chat dung bao dong nham.
- [13:21] E-12 thoat exit=1 do 429 (retry limit) khi chua ra ket qua => chay lai lan 2 (K4).
- [13:28] LOI MONITOR: ten worker chay lai da nam san trong .seen-all nen DONE/exit khong bao => 7 worker chet vi 429 (E-10,H-01,E-13,B-02d,B-04a,G-01,H-03; exit=1, 'exceeded retry limit 429') khong duoc phat hien 13:11-13:22. Da go ten khoi .seen-all moi lan giao, chay lai 7 worker cach nhau 20s (lan 2 cho E-13,G-01,H-03,B-02d,B-04a; lan 3 cho E-10/H-01 xem them). H-10 (exit 0) va E-09a (exit 0) da merge.
- [13:31] H-05 xong (merge); H-10, E-09a da merge.
- [13:37] E-10 xong (merge). M-01 xong (bao cao, cho chu duyet). #056: astra_loop doi 1800 s (can khoi dong lai vong ping).
- [13:40] B-02d xong (merge): review tinh B-02c = CHUA du dieu kien gop (REMOVE loi bookkeeping, thieu guard giao dich/doi/PK, chat man hinh qua relay CoreServerShell.cpp:3009, bo qua nguoi an co the lam Bot khong trung). Giao H-06,H-07,H-08,H-11 (readonly) luc 13:40; dang chay 12 worker. Monitor moi bsdo5wj3p.
- [13:41] E-13 P1 xong (merge): 11 test dat, 5 task gia done. Thieu watchdog/su co chung (#053) => giao E-13b (K2). Chua chuyen sang Tong quan (can 2 task that, Q-42). Monitor boh1f7f5f + bsdo5wj3p chong lap (khong lo ho). Dang chay: H-01,H-03,B-04a,G-01,E-11,E-12,H-06,H-07,H-08,H-11,E-13b.
- [13:42] H-03 xong (merge).
- [13:46] E-12 xong (merge).

- 17/11 14:05 Gộp H-01, B-04a, G-01, H-11, E-13b, H-08, H-06, E-11, H-07. Đang chạy: I-01..I-05, H-12, A-16, A-17 (8 worker).

- 17/11 14:12 Giao thêm H-13, H-14, I-07, I-08 (12 worker; 3/khóa). Số mục sổ sổ thông số: 0 / số đo gốc: chưa có (chờ E-05).
- 17/11 14:32 Gộp I-03 (quái vật).

- 17/11 14:53 Gộp H-13. Giao J-05 (K4). Hàng đợi: J-01..J-04, J-06, I-06, H-09.

- 17/11 15:14 Gộp H-12, H-14, H-15, I-01, I-02, I-04, I-07, I-08. Chạy lại I-05, A-17, J-05 (429). Giao J-01..J-04, J-06. Đang chạy 8 worker.

- 17/11 15:30 Sự cố nhà cung cấp lần 2: 9 worker chết 429 cùng lúc (15:12-15:18). API thăm dò 15:26 đã lên; chạy lại I-05, A-17, J-01..J-06, K-01 (cách 20 s). L-01 đang chạy.
- 17/11 15:44 Gộp J-05, J-06.
- 2026-11-17 16:05 I-05: xong (exit=0), da gop vao jx1-ops.
- 2026-11-17 16:05 J-01: xong (exit=0), da gop vao jx1-ops.
- 2026-11-17 16:05 J-02: xong (exit=0), da gop vao jx1-ops.
- 2026-11-17 16:05 J-05: xong (exit=0), da gop vao jx1-ops.
- 2026-11-17 16:16 A-17: xong (exit=0), da gop. bao cao=True
- 2026-11-17 16:16 J-04: xong (exit=0), da gop. bao cao=True
- 2026-11-17 16:16 L-01: xong (exit=0), da gop. bao cao=True
- 2026-11-17 16:16 H-09: xong (exit=0), da gop. bao cao=True
- 2026-11-17 16:16 I-06: xong (exit=0), da gop. bao cao=True
- 2026-11-17 16:16 I-06 chay khi J-03/J-04/J-06 chua co bao cao: can chay lai muc Animation (I-06b) sau khi J-03, K-01 xong. H-09/I-06 khong commit duoc trong sandbox worker (index.lock); PM da commit ho.
- 2026-11-17 16:39 #074 E-13 chay that thu: X-01/X-02 giao dung (K2,K3) nhung dispatcher thoat sau 60s nen QUEUE danh dau blocked 'dispatcher stopped' (loi do thuoc ha dat max-seconds ngan; worker van chay). Chay lai X-03/X-04 voi --until-idle --max-seconds 1500, state D:\JX-wt\_dispatcher-state2, snapshot ngan sach tam daily=0 (CHUA co so that, can doi soat). Cho ket qua 2 cap de doi chieu.
- 2026-11-17 16:39 J-03: xong (exit=0), da gop.
- 2026-11-17 16:39 M-02: xong (exit=0), da gop.
- 2026-11-17 17:04 K-01: xong (exit=0), da gop.
- 2026-11-17 17:04 L-02: xong (exit=0), da gop.
- 2026-11-17 17:04 I-06b: xong (exit=0), da gop.
- 2026-11-17 17:04 X-01: xong (exit=0), da gop.
- 2026-11-17 17:05 X-02: xong (exit=0), da gop.
- 2026-11-17 17:05 X-04: xong (exit=0), da gop.
- 2026-11-17 17:05 E-13 chay that: X-04 xong qua dispatcher dung; X-03 bi dispatcher danh dau blocked:timeout (~15 phut, log ngung 16:53), PM chay lai tay; X-01/X-02 lan dau im sau khi dispatcher thoat (state 1), chay lai tay xong. Chua du dieu kien chuyen han Q-42.
- 2026-11-17 19:04 APK-A: jx-qh9-smooth-A.apk (versionCode 18, cert a48601f7, SHA256 137691757920392e9fc9695ab963906d267b1b185a12e612f1296a9f41081116) dựng xong, phát ở D:\JX1_U003_build\serve, link http://100.95.186.86:8091/jx-qh9-smooth-A.apk; chủ yêu cầu gửi test thẳng, chưa thử LD. A0 đối chứng, APK-B và H-15 chưa làm.
