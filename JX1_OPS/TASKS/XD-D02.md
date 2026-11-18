---
id: XD-D02
title: Chuẩn bị D-02: danh sách thử hoạt động bằng GM
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-D02
worktree: D:\JX-wt\XD-D02
depends_on: []
backlog_ref: "việc phụ (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-D02.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao"
---

## Mục tiêu và tiêu chí xong
Việc chuẩn bị cho **D-02**. Đọc D-01 và báo cáo hoạt động; lập danh sách từng hoạt động: lệnh GM cần (dẫn gmroleitem.lua dòng nếu có), điều kiện bản đồ, kết quả mong đợi, cách chụp bằng chứng; chỉ kế hoạch.
Đầu ra: `JX1_OPS/REPORTS/XD-D02.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "## Chưa kiểm". Xong khi: tệp tồn tại và đúng phạm vi, mỗi nhận định có bằng chứng hoặc nhãn CHƯA KIỂM.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả

- **DONE** — `JX1_OPS/REPORTS/XD-D02.md` lập kế hoạch cho đủ 27 nhánh D-01, có điều kiện bản đồ, kết quả mong đợi và bằng chứng cần thu.
- Đối chiếu tĩnh sáu mục mở hoạt động trong `gmroleitem.lua`. Các mục GM hoặc điều kiện còn thiếu bằng chứng được ghi **CHƯA KIỂM**.
- Chỉ kiểm tài liệu và đọc nguồn. Chưa build, chạy lệnh GM, exe, VM hay mạng. Tổng quan phụ trách commit.
- Tệp `.nhip` nằm ngoài vùng ghi của phiên. Tiến độ được báo trong hội thoại.
