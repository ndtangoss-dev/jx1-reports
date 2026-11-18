---
id: XD-A07c
title: Đóng A-07c: kiểm sản phẩm build
status: done
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-A07c
worktree: D:\JX-wt\XD-A07c
depends_on: []
backlog_ref: "đóng việc cha A-07c (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-A07c.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao #209 dot 4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **A-07c** (không vào mẫu số). Đọc `JX1_OPS/TASKS/A-07c.md` và `REPORTS/A-07c-link-gs001.md`. Kiểm bằng lệnh đọc (Get-FileHash, dir) rằng gs001.exe x64 nêu trong báo cáo có tồn tại, SHA-256 khớp báo cáo, chưa đè bản đang chạy; KHÔNG chạy exe. Kết luận ĐẠT/CHƯA ĐẠT từng vế.
Đầu ra: `JX1_OPS/REPORTS/XD-A07c.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- PARTIAL — báo cáo: `JX1_OPS/REPORTS/XD-A07c.md`; đã kiểm tra tĩnh artifact ngày 19/11/2026.
- THẤY: gs001.exe tồn tại, 1.346.560 byte, PE x64; SHA-256 khớp đủ báo cáo A-07c. TÀI LIỆU: log năm project mã 0, build_errors rỗng.
- CHƯA KIỂM: chưa đủ bằng chứng không đè bản đang chạy; không build/chạy exe, VM hoặc mạng, không sửa kết luận cũ.
- Không commit/push; Tổng quan commit hộ. Tệp nhịp `D:\JX-wt\XD-A07c.nhip` ngoài vùng sandbox cho phép ghi nên không được tạo.
