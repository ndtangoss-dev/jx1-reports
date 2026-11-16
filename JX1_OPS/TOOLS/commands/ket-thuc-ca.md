---
description: Dừng ca làm việc an toàn để chủ dự án tắt máy
---
Chủ dự án sắp tắt máy. Làm đúng các bước "/ket-thuc-ca" trong `JX1_OPS/QUY-TAC-VAN-HANH.md` mục 7:

1. Không giao việc mới.
2. Worker đang chạy: chờ tới điểm dừng an toàn, tối đa 10 phút; quá thì dừng, commit phần dở thành WIP trên branch task, ghi "Bước tiếp theo" trong file task.
3. Server trong VM thử: để chạy hoặc dừng đúng thứ tự; ghi lại trong TRANG-THAI.md đã làm gì.
4. Cập nhật `STATE/TRANG-THAI.md` và `STATE/BAN-GIAO.md`.
5. Viết báo cáo ngày `REPORTS/daily/YYYY-MM-DD.md` theo 7 câu (nếu hôm nay đã có thì bổ sung).
6. Commit, đẩy nhánh `jx1-ops` và các branch task lên. Kiểm tra commit đã có trên GitHub.
7. Trả lời chủ dự án: tóm tắt báo cáo ngày trong tối đa 6 dòng, rồi dòng cuối "Đã lưu. Có thể tắt máy." Nếu đẩy lên GitHub thất bại thì nói rõ và KHÔNG nói có thể tắt máy.

$ARGUMENTS
