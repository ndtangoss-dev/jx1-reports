---
id: KC-01b
title: Sửa 3 mệnh đề sai (A-05, N-01) và kiểm nốt 2 mục chưa xác minh từ KC-01
status: running
level: L3
agent: codex
effort: high
priority: 1
branch: task/KC-01b
worktree: D:\JX-wt\KC-01b
depends_on: []
backlog_ref: "#207 dot 3 (BACKLOG, KC-01b)"
vung_file: [JX1_OPS/REPORTS/KC-01b.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "Tong quan giao bang JX-K2"
---

## Mục tiêu và tiêu chí xong
Đọc `JX1_OPS/REPORTS/KIEM-CHEO-01.md`: với 3 mệnh đề SAI (1 A-05, 2 N-01), 2 THIẾU điều kiện và 2 CHƯA XÁC MINH, đối chiếu lại nguồn và ghi bản ĐÚNG kèm file:dòng. Sửa trực tiếp các câu sai trong báo cáo gốc A-05/N-01 (chỉ các dòng đó, thêm ghi chú "sửa theo KC-01b").
Đầu ra: `JX1_OPS/REPORTS/KC-01b.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng. Viết lời thường cho người không lập trình, ít nhất 1 sơ đồ mermaid. Xong khi: tệp tồn tại, đủ 5 dòng tóm tắt, >=10 dẫn file:dòng đúng, có mục "Chưa kiểm".

## Nguồn cần đọc
- Worktree của bạn KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`. Tra nhanh được bằng `D:/JX-tools/graphify-venv/Scripts/graphify.exe query "<câu hỏi>"` chạy trong `D:/JX-build/src18/jxOnline`.

## Phạm vi và quyền đã duyệt
- Chỉ đọc tĩnh và viết tài liệu. Chỉ được sửa tệp đầu ra ở trên và các dòng sai trong JX1_OPS/REPORTS/A-05*.md, N-01*.md.
- Không sửa mã, không chạy exe, không VM, không mạng, không đụng Main VM, không đọc khóa/mật khẩu/dump tài khoản.
- Không đọc cả thư mục lớn; mỗi lần đọc <= ~400 dòng; không đọc lại.
- Cuối tệp task này ghi mục "## Kết quả" (3–5 dòng).
