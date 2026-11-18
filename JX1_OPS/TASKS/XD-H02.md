---
id: XD-H02
title: Mục lục các sổ tay và bảng thuật ngữ
status: ready
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-H02
worktree: D:\JX-wt\XD-H02
depends_on: []
backlog_ref: "việc phụ đóng việc cha (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-H02.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao 03:35"
---

## Mục tiêu và tiêu chí xong
Lập mục lục mọi `DESIGN/SO-TAY-*.md` và `HIEU-*.md` (một dòng mỗi tệp: nội dung, nhãn đáng tin) và bảng thuật ngữ Việt–Anh–tên hàm cho 30 thuật ngữ hay gặp. Chỉ đọc tệp có sẵn.
Đầu ra: `JX1_OPS/REPORTS/XD-H02.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và mỗi vế của tiêu chí có bằng chứng hoặc ghi rõ thiếu gì; kết luận cuối một dòng "ĐẠT" hoặc "CHƯA ĐẠT vì …".

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra.
- Worktree có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- [THẤY] Báo cáo `JX1_OPS/REPORTS/XD-H02.md` có mục lục 46/46 tệp (28 sổ tay, 18 bài “Hiểu”) tại mốc chốt 03:49:56 ngày 19/11/2026 (UTC+7) và 30/30 thuật ngữ Việt–Anh–tên hàm; lượt tiếp tục bổ sung `SO-TAY-BAN-BE-ONLINE.md`, `SO-TAY-AI-QUAI.md` từ kho chỉ đọc.
- [CHƯA KIỂM] Chỉ đọc tĩnh và kiểm tài liệu. Chưa build, chạy game/exe, VM hay mạng.
- [THẤY] Trạng thái bàn giao PARTIAL do bị từ chối ghi `D:\JX-wt\XD-H02.nhip` ở ba mốc. Tổng quan thực hiện commit.
- ĐẠT — đã hoàn tất tiêu chí nội dung trong mục Mục tiêu và tiêu chí xong.
