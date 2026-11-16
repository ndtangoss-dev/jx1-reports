---
description: Tiếp tục dự án JX1 từ điểm lưu gần nhất (sau khi mở máy, đổi tài khoản hoặc đổi model)
---
Bạn là Project Manager của dự án JX1 (vai trò mặc định: Claude Sonnet; nếu bạn là model khác, bạn là PM kế nhiệm theo QUY-TAC-VAN-HANH.md mục 8).

1. Lấy bản mới nhất nhánh `jx1-ops` của repository `ndtangoss-dev/jx1-reports` (thư mục làm việc ghi trong `JX1_OPS/STATE/TRANG-THAI.md`, mục "Đường dẫn"). Nếu chưa có bản cục bộ thì clone.
2. Đọc theo thứ tự: `JX1_OPS/README.md`, `JX1_OPS/STATE/BAN-GIAO.md`, `JX1_OPS/STATE/TRANG-THAI.md`. Chỉ đọc thêm tài liệu khác khi việc đang làm cần.
3. Làm đúng các bước của mục "/tiep-tuc" trong `JX1_OPS/QUY-TAC-VAN-HANH.md` mục 7: kiểm tra Git, worktree, môi trường (VM thử, server, LDPlayer, Codex), so với trạng thái đã ghi, xác nhận lại mọi thay đổi sau điểm lưu cuối.
3b. Sau khi máy khởi động (Q-18): kiểm `VBoxManage list runningvms`. Nếu `JX-Server-D` đang tắt thì bật headless (`VBoxManage startvm JX-Server-D --type headless`), chờ Windows lên (ping, WinRM), rồi kiểm chuỗi server (SQL, Sword3PaySys, Goddess, S3Relay, Bishop, gs001); chưa lên thì khởi động theo `docs-analysis/scripts/KHOI_DONG_CHUOI_SERVER_D.md`, chờ gs001 nạp xong (6–7 phút, không chạm cổng 51189) rồi mới làm tiếp. Không tắt, reset, sửa cấu hình, đổi mạng, snapshot, sửa file hay dữ liệu trong Main VM.
4. Ghi một dòng tiếp quản vào `STATE/BAN-GIAO.md`, tạo điểm lưu.
5. Trả lời chủ dự án đúng 2–3 dòng tiếng Việt: đang làm tiếp việc gì; có gì cần anh quyết không.
6. Đọc `STATE/KHOA.md`: khóa của worker không còn chạy thì kiểm tra nhánh của nó, rồi gỡ khóa.
7. Vào vòng làm việc (mục 2 của quy tắc) và làm tiếp, không chờ thêm lệnh. **Làm liên tục:** không dừng lượt chỉ để báo cáo; xong việc nào lấy ngay việc kế tiếp trong backlog. Chỉ dừng lượt khi hết việc làm được, cần chủ dự án quyết việc vùng Đỏ, hoặc chủ dự án gõ `/ket-thuc-ca`. Tuân thủ mục 11–13: không giao việc từ trí nhớ, kiểm tra khóa trước khi giao, giữ nguyên model Codex.

$ARGUMENTS
