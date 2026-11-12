# WORKFLOW — Quy trình thống nhất

1. Chủ dự án nêu mục tiêu; CTRL tự phân loại, chọn một Primary Owner và tạo mã task (ENG-001, VIS-001, GAME-001, SRV-001, QA-001, AST-001, REL-001, SEC-001).
2. Phòng chuyên môn nghiên cứu/đề xuất; nếu chưa rõ, hỏi một câu trọng yếu. Không tự giao Claude.
3. CTRL kiểm tra xung đột, phạm vi, rủi ro và điều kiện duyệt.
4. Khi có nhiều task hoặc vùng code dùng chung, CTRL bắt buộc lập đợt tích hợp theo INTEGRATION_PLAN.md: tổng hợp yêu cầu, kiểm tra baseline, lập bản đồ phụ thuộc/xung đột, sắp thứ tự và tạo gói thực thi thống nhất.
5. Chủ dự án phê duyệt thay đổi cần duyệt. CTRL đưa task vào TASKS của phòng và chỉ chuyển gói thực thi sang APPROVED sau khi đủ điều kiện.
6. Claude Code là coder dùng chung; chỉ thực thi một gói đã duyệt, tuần tự từng bước trên branch/worktree tích hợp riêng, có checkpoint/commit và test sau từng bước. Không nhận lệnh code chen ngang từ các phòng.
7. QA/phòng độc lập kiểm tra; chạy test mục tiêu, tích hợp và hồi quy theo kế hoạch.
8. CTRL phân phối báo cáo theo từng task/phòng; cập nhật MASTER_TASK_BOARD, DECISION_LOG, BLOCKERS_AND_RISKS và DAILY_WORK_LOG.

## Trạng thái
INTAKE · PROPOSED · APPROVED · IN_PROGRESS · BLOCKED · REVIEW · DONE_VERIFIED · DONE_UNVERIFIED · NOT_DONE · DEFERRED.

## Độ tin cậy
VERIFIED = có kiểm chứng trực tiếp; PROBABLE = có cơ sở nhưng chưa đủ; UNKNOWN = chưa rõ; BLOCKED = bị chặn; NOT TESTED = chưa chạy test.

## Chống chồng chéo và vòng lặp
- Một task có một Primary Owner. Một vùng source chỉ một executor sửa tại một thời điểm.
- Không code trực tiếp trên main; mỗi đợt có baseline và branch/worktree riêng. Không reset/clean/ghi đè thay đổi chưa commit của người dùng.
- Mỗi lỗi tối đa 2 vòng sửa có kiểm soát trong một đợt. Sau đó dừng và báo CTRL, không lặp vô hạn.
- Phát hiện xung đột: dừng phần thay đổi liên quan, không ghi đè; báo CTRL đánh giá.
- Mọi báo cáo nêu task ID, phạm vi, file, commit, phương pháp, test/bằng chứng, kết quả, phần chưa làm, blocker và đề xuất tiếp theo.
