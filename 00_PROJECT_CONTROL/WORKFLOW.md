# WORKFLOW — QUY TRÌNH ĐIỀU PHỐI JX1

Đối với JX1, quy trình thực thi hiện hành là **Codex Direct CLI**, theo [WORKFLOW_JX1.md](../WORKFLOW_JX1.md) và [CODEX_DIRECT_CLI_RULES.md](../PROMPTS/CODEX_DIRECT_CLI_RULES.md). Tài liệu này thay thế quy định cũ giao Claude Code làm coder dùng chung cho JX1.

1. Người dùng nêu mục tiêu và quyết định ưu tiên.
2. CTRL/ChatGPT xác định một Primary Owner, phạm vi, rủi ro và tiêu chí nghiệm thu.
3. ChatGPT kiểm tra đúng các báo cáo nền liên quan; không yêu cầu kiểm kê/lặp lại việc đã hoàn thành.
4. ChatGPT soạn một prompt có đường dẫn cụ thể, đầu ra duy nhất, quyền, kiểm chứng thiết yếu và điều kiện dừng; người dùng duyệt.
5. ChatGPT đưa prompt lên GitHub và cung cấp commit SHA cùng chỉ thị kích hoạt ngắn.
6. Người dùng kích hoạt Codex CLI trực tiếp. Một task, một executor, không chạy Dispatcher/queue trong quy trình hiện tại.
7. Codex làm trong phạm vi, tạo báo cáo cuối, kiểm tra và commit/push báo cáo nếu có quyền.
8. ChatGPT đọc báo cáo, phản biện bằng chứng, cập nhật quyết định và đề xuất bước tiếp theo.

## Vai trò

- CTRL: điều phối tổng thể và kiểm soát phạm vi.
- Phòng chuyên môn: phân tích/đề xuất trong lĩnh vực phụ trách.
- Codex CLI: executor JX1 mặc định khi được kích hoạt trực tiếp.
- Claude hoặc agent khác: chỉ QA/review/nhiệm vụ riêng khi được giao rõ; không sửa chồng chéo.

## Trạng thái và độ tin cậy

INTAKE · PROPOSED · APPROVED · IN_PROGRESS · BLOCKED · REVIEW · DONE · PARTIAL · FAILED · DEFERRED.

VERIFIED = có bằng chứng trực tiếp; PROBABLE = có cơ sở nhưng chưa đủ; UNKNOWN = chưa rõ; NOT TESTED = chưa chạy; BLOCKED = bị chặn.

## Chống chồng chéo và vòng lặp

- Một task có một Primary Owner và một executor.
- Không sửa trực tiếp main nếu prompt không cho phép; không reset/clean/ghi đè thay đổi người dùng.
- Mỗi lỗi tối đa 2 vòng sửa có kiểm soát; sau đó dừng, báo blocker và đề xuất quyết định.
- Không lặp kiểm tra chuẩn bị, không đọc lại toàn bộ tài liệu và không mở rộng nghiên cứu vô hạn.
- Báo cáo nêu task, phạm vi, file/symbol/line, kiểm tra/bằng chứng, kết quả, phần chưa làm và blocker.
