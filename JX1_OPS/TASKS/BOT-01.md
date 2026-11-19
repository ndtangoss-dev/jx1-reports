---
id: BOT-01
title: Bot GĐ1 (bán đồ): đọc bảng giá và tính giá bán, chạy offline
status: running
owner: B
level: L2
agent: codex
branch: task/BOT-01-gia-ban
worktree: D:\JX-wt\BOT-01
depends_on: []
vung_file: [JX1_OPS/BOT/gia_ban.py, JX1_OPS/BOT/test_gia_ban.py, JX1_OPS/REPORTS/BOT-01-*.md]
tai_nguyen: [không]
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K4"
---
## Worker kiểm tra trước khi làm (bắt buộc)
- Thư mục hiện tại = `worktree`, nhánh = `branch`. Sai thì dừng, `blocked`. Chỉ sửa trong `vung_file`. Không chạy exe, không kết nối server, không ghi mật khẩu/khóa.
- Đọc trước: `JX1_OPS/STATE/BOT/gia-vat-pham.csv`, `gia-vat-pham-README.md`, `JX1_OPS/DESIGN/BOT/*`.
## Mục tiêu
Mô-đun Python chuẩn (`python -I`) đọc `gia-vat-pham.csv` (cột `ma_mon, gia_goc, he_so_ban, gia_san_mac_ca, ten_unicode`), trả giá bán = `max(gia_goc*he_so_ban, gia_san_mac_ca)` (đã có cột sẵn; không đoán hệ số, đọc từ file), tra theo `ma_mon` và theo tên có dấu (không phân biệt hoa thường), báo rõ món thiếu giá.
## Tiêu chí xong
Test offline pass: ít nhất 8 món mẫu khớp bảng; tên lỗi (GBK) không làm hỏng; báo cáo ghi lệnh test và kết quả. Chưa có Bot thật: ghi "chưa kiểm".
## Lệnh build và test
`python -I -m unittest JX1_OPS.BOT.test_gia_ban -v`
---
