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
| 0-07 | đang chạy | thử nguội đạt; còn thử qua tắt bật VM, nối ensure Main VM |
| 0-09 | đang chạy | sandbox Codex chặn ghi D:\JX-wt nhưng ghi được C:\Users\Public |
| 0-10 | chờ | |
| 0-08 | chờ | |

## Ngân sách Codex
- Tổng: khoảng 2.000 USD (chủ dự án cho biết)
- **Trần cứng của khóa xingchi** (chủ dự án báo 16/11 21:25): 50 USD / 5 giờ, 200 USD / ngày, 1.000 USD / 7 ngày [BÁO CÁO]
- Đã dùng: 20 USD / 7 ngày tính đến 21:25 ngày 16/11 [BÁO CÁO]
- **Khóa hết hạn 14/02/2027. Nhắc chủ dự án trước 7 ngày (từ 07/02/2027)**
- Quy tắc khi Codex bị từ chối vì chạm trần: coi là hết hạn mức, không phải lỗi code. Không thử lại liên tục; chuyển việc cho agent con Sonnet hoặc chờ tới khung giờ sau
- Khi tăng số worker: giữ tổng chi trong 5 giờ dưới 50 USD (mỗi lần tăng phải tính lại)
- Số worker hiện tại: 0 (bậc khởi đầu: 3)

## Môi trường đang bật lúc lưu
(Sonnet ghi: VM nào đang chạy, server nào đang lên, LDPlayer, worker.)

- **Bảng tiến độ (22:10):** `TOOLS/bang_tien_do.py` dựng `D:\JX-dash\index.html` từ BACKLOG.md, TRANG-THAI.md (bảng "Tiến độ task") và KHOA.md; tự dựng lại sau mỗi commit nhờ hook `post-commit` của kho `D:\jx1-reports` (hook nằm ngoài git). Bản Artifact riêng tư: https://claude.ai/artifact/7bUxS1STLrmZ6btueV3eiy (PM xuất bản lại khi cập nhật). Bản Tailscale (cổng 8092, kèm nút sơ đồ Graphify): `docs-analysis/scripts/dash_server_tailscale.py`, chờ Tailscale bật (máy thật báo stopped, không có địa chỉ 100.x) và chờ chủ máy chạy `mo_cong_dash_8092.ps1` bằng Admin (hoàn tác `huy_cong_dash_8092.ps1`) [CHƯA KIỂM: chưa phục vụ được].
- **Graphify install (22:05):** chủ dự án cho áp dụng; `graphify claude install` tại `C:\Jx1CocoV3`: CLAUDE.md thêm 11 dòng, `.claude/settings.json` thêm 3 hook (PreToolUse Bash|Grep, Read|Glob; SessionStart compact). Hook SessionStart cũ giữ nguyên [XÁC MINH]; sao lưu `.claude/settings.json.bak-truoc-graphify`; gỡ bằng `graphify claude uninstall`. Hook chỉ có tác dụng ở phiên mới; `/tiep-tuc` chưa chạy lại thật trong phiên mới [CHƯA KIỂM].
- **0-09 thử sandbox (22:00):** Codex `workspace-write` ghi được trong worktree, bị chặn ghi `D:\JX-wt\` ngoài worktree, nhưng ghi được `C:\Users\Public\` (đã xóa file thử) [XÁC MINH].
