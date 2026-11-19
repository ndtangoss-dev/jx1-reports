---
id: BOT-02
title: Bot: kiểm tên vai hợp lệ và không trùng trước khi tạo (offline)
status: running
owner: B
level: L2
agent: codex
branch: task/BOT-02-ten-vai
worktree: D:\JX-wt\BOT-02
depends_on: []
vung_file: [JX1_OPS/BOT/ten_vai.py, JX1_OPS/BOT/test_ten_vai.py, JX1_OPS/REPORTS/BOT-02-*.md]
tai_nguyen: [không]
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---
## Worker kiểm tra trước khi làm (bắt buộc)
- Thư mục hiện tại = `worktree`, nhánh = `branch`. Chỉ sửa trong `vung_file`. Không kết nối server, không ghi bí mật.
- Đọc: `JX1_OPS/STATE/TESTER/KIEN-THUC/tao-nhan-vat/NUT-GIAO-DIEN.md` (luật tên), `JX1_OPS/TOOLS/bot_tao_role.py`.
## Mục tiêu
Hàm `kiem_ten(ten, da_co)` theo luật client: độ dài 6..16 byte, chỉ chữ cái ASCII (không dấu cách, số, ký hiệu; không khoảng trắng đầu/cuối), không trùng (không phân biệt hoa thường) với danh sách `da_co`; sinh tên Bot không trùng `gen_ten(prefix, n, da_co)`. Trả lý do lỗi tiếng Việt ngắn.
## Tiêu chí xong
Test offline pass: `Cctesterone` hợp lệ; `T36nv2`, `Ts baone`, `abc`, tên có dấu cách cuối bị từ chối; trùng bị từ chối; báo cáo ghi lệnh và kết quả.
## Lệnh build và test
`python -I -m unittest JX1_OPS.BOT.test_ten_vai -v`
---
