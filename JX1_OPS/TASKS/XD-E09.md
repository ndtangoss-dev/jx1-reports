---
id: XD-E09
title: Đóng E-09: kiểm bot allowlist
status: done
level: L3
agent: codex
effort: high
priority: 1
branch: task/XD-E09
worktree: D:\JX-wt\XD-E09
depends_on: []
backlog_ref: "đóng việc cha E-09 (không vào BACKLOG)"
vung_file: [JX1_OPS/REPORTS/XD-E09.md]
tai_nguyen: []
updated: 2026-11-19
status_note: "moi tao #209 dot 4"
---

## Mục tiêu và tiêu chí xong
Việc phụ đóng việc cha **E-09** (không vào mẫu số). Đọc `JX1_OPS/TASKS/E-09.md` (mục "Tiêu chí xong") và báo cáo `JX1_OPS/REPORTS/E-09a-real-login-allowlist.md`. Với TỪNG vế của tiêu chí: chạy lại lệnh kiểm offline (python -I, không mạng), ghi lệnh và kết quả thật; vế nào chưa đạt thì chỉ ra phần cần chạy bot thật (nếu có) và đánh dấu cần Test-36. Kết luận cuối bằng một dòng: "E-09 ĐẠT" hoặc "E-09 CHƯA ĐẠT vì …". Xong khi: mỗi vế của tiêu chí có bằng chứng (lệnh+kết quả hoặc file:dòng) hoặc ghi rõ thiếu gì.
Đầu ra: `JX1_OPS/REPORTS/XD-E09.md`. Đầu file có TÓM TẮT 5 DÒNG; mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM kèm file:dòng hoặc lệnh+kết quả. Có mục "Chưa kiểm". Xong khi: tệp tồn tại và đáp ứng đúng dòng "Xong khi" riêng của việc.

## Phạm vi và quyền đã duyệt
- Không chạy exe lạ, không VM, không mạng, không Main VM, không đọc khóa/mật khẩu/dump tài khoản. Chỉ ghi tệp đầu ra ngoài ra không sửa gì.
- Worktree của bạn có thể KHÔNG có mã nguồn game: đọc trực tiếp (chỉ đọc) client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes` và server `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources`; kho báo cáo ở D:/jx1-ops-wt/JX1_OPS (chỉ đọc).
- Mỗi lần đọc <= ~400 dòng. Cuối tệp task ghi mục "## Kết quả" (3–5 dòng).

## Kết quả
- DONE phạm vi XD-E09: báo cáo `JX1_OPS/REPORTS/XD-E09.md` đã đối chiếu 8 vế yêu cầu cha từ `JX1_OPS/TASKS/BACKLOG.md:67`; giữ nguyên kết luận E-09a.
- Đã chạy `python -I -B -` với 4 test mock có sẵn và audit hook: 4/4 đạt trong 0.012 s, 0 lỗi, 0 bỏ qua, 0 sự kiện socket/DNS/tiến trình con; không ghi credential.
- E-09 CHƯA ĐẠT: C2–C8 cần Test-36 để xác minh BOT/TESTER thật, tài khoản DB, login → role → vào game, Enabled=1 Solo bằng hai phiên + bot; C1 đạt tầng cấu hình/offline.
- Không chạy lại 3 test loopback, không build/exe game/VM/mạng; lỗi import Windows ở lượt đầu đã hết sau khi giữ bốn biến đường dẫn hệ thống trong môi trường Python con.
- Không commit/push; tệp nhịp ngoài writable root nên chưa ghi, đã thông báo giới hạn và các mốc tiến độ trong trao đổi. Tổng quan tiếp nhận commit và nghiệm thu Test-36.
