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

## Ngân sách Codex
- Tổng: khoảng 2.000 USD (chủ dự án cho biết; Sonnet xác minh loại hạn mức ở task 0-10)
- Đã dùng: chưa có dữ liệu
- Trần ngày: chưa đặt (task 0-10)
- Số worker hiện tại: 0 (bậc khởi đầu: 3)

## Môi trường đang bật lúc lưu
(Sonnet ghi: VM nào đang chạy, server nào đang lên, LDPlayer, worker.)
