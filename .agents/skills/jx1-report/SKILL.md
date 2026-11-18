---
name: jx1-report
description: Viết báo cáo cuối task JX1 đúng đường dẫn với tóm tắt 5 dòng, mức xác minh và bàn giao commit; không tự gửi thông báo ngoài.
---
# Báo cáo cuối JX1
- Chỉ ghi đường dẫn task/prompt; không tự sửa task/BAI_HOC hoặc báo cáo từng bước.
- TOM TAT 5 DONG: đúng 5 dòng nêu (1) trạng thái/phạm vi, (2) kết quả,
  (3) đầu ra, (4) chưa xác minh/test/blocker, (5) SHA/push hoặc lý do và bước PM cần làm.
- DA XAC MINH: file:dòng, symbol/lệnh, kết quả thực; nguồn gián tiếp ghi báo cáo dẫn lại.
  Kiểm file thật tóm tắt dẫn tới trong vùng được đọc; thiếu/ngoài quyền ghi chưa đối chiếu.
- CHUA XAC MINH: giới hạn, test/build chưa chạy, lý do. Khảo sát có MUC SO THONG SO
  (jx1-parameters) và DE XUAT TOI UU. Chấp nhận tên mục có dấu tương đương ở báo cáo cũ.
- Gộp mọi lỗi/cách thử/kết quả/nguyên nhân/bước tiếp tục; tối đa 3 lần/cùng lỗi.
  Trạng thái DONE/PARTIAL/BLOCKED/FAILED đúng phạm vi đã đạt, không bịa số đo/runtime.
- Chỉ stage/commit/push khi task yêu cầu; chọn đúng file. SHA có sau commit ghi phản hồi cuối,
  không vòng amend để ghi SHA của chính báo cáo. Push cần bằng chứng GitHub.
- Git bị chặn: giữ local, ghi BỊ CHẶN – CHƯA PUSH, lỗi thật, chưa có SHA, việc PM cần làm;
  không đổi quyền/credential/config hoặc tự gửi tin ngoài.
- Bắt buộc (chủ duyệt #093): kèm 1 sơ đồ Mermaid (```mermaid) về luồng/quan hệ chính, và dòng "liên quan: <báo cáo/DESIGN/BUG>". Nếu thêm tri thức mới, ghi hàng cần thêm vào JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md trong báo cáo (PM gộp).
- Nhịp sống (#117): ở mốc lớn ghi một dòng vào `D:\JX-wt\<MA-TASK>.nhip` (nếu task có worktree). Cuối báo cáo ghi "Kỹ năng đã dùng: <tên skill hoặc không>" để PM kiểm xem Codex có nạp `.agents/skills` không (#118.8).
