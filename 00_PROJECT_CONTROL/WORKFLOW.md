# WORKFLOW — Quy trình thống nhất

1. Chủ dự án nói mục tiêu; CTRL tự phân loại, chọn một Primary Owner và tạo mã task (ENG-001, VIS-001, GAME-001, SRV-001, QA-001, AST-001, REL-001, SEC-001).
2. Phòng chuyên môn nghiên cứu/đề xuất; nếu chưa rõ, hỏi một câu trọng yếu. Không tự giao Claude.
3. CTRL kiểm tra xung đột, phạm vi, rủi ro và điều kiện duyệt.
4. Chủ dự án phê duyệt thay đổi cần duyệt. CTRL đưa task vào TASKS của phòng.
5. Claude Code thực thi khi có chỉ thị rõ ràng, đúng task/phạm vi; ghi diff, lệnh, test, log, rollback.
6. QA/phòng độc lập kiểm tra khi phù hợp.
7. Phòng cập nhật REPORTS; CTRL cập nhật MASTER_TASK_BOARD, DECISION_LOG và DAILY_WORK_LOG.

## Trạng thái
INTAKE · PROPOSED · APPROVED · IN_PROGRESS · BLOCKED · REVIEW · DONE_VERIFIED · DONE_UNVERIFIED · NOT_DONE · DEFERRED.

## Độ tin cậy
VERIFIED = có kiểm chứng trực tiếp; PROBABLE = có cơ sở nhưng chưa đủ; UNKNOWN = chưa rõ; BLOCKED = bị chặn; NOT TESTED = chưa chạy test.

## Chống chồng chéo
Một task có một Primary Owner. Chỉ một executor sửa một vùng source tại một thời điểm. Nếu phát hiện xung đột, dừng phần thay đổi chưa commit và báo CTRL; không ghi đè. Mọi báo cáo nêu task ID, phạm vi, file, phương pháp, bằng chứng, kết quả, phần chưa làm, blocker và đề xuất tiếp theo.
