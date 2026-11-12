# CLAUDE – ĐIỂM BẮT ĐẦU / KIỂM TRA NHIỆM VỤ MỚI

Repository: `ndtangoss-dev/jx1-reports`
Quy trình chính: [WORKFLOW_JX1.md](../WORKFLOW_JX1.md)
Trạng thái dự án: [00_LATEST_STATUS.md](../00_LATEST_STATUS.md)

## Khi được người dùng kích hoạt hoặc khi bắt đầu một phiên làm việc

1. Đọc `WORKFLOW_JX1.md` và `00_LATEST_STATUS.md`.
2. Kiểm tra thư mục `PROMPTS/` để tìm chỉ thị có trạng thái ĐƯỢC DUYỆT / BẮT ĐẦU THỰC HIỆN.
3. Đọc đầy đủ prompt nhiệm vụ được chỉ định trong chỉ thị. Không tự thực hiện prompt còn là bản nháp/chưa được duyệt.
4. Nếu có `CLAUDE_EXECUTE_PHASE_46.md`, đọc file này và prompt Phase 46 tương ứng; đây là nhiệm vụ đã được người dùng duyệt.
5. Xác minh môi trường, quyền truy cập, đúng source và đúng VM thử nghiệm trước khi thao tác. Không can thiệp Main VM.
6. Xác nhận ngắn gọn đã đọc nhiệm vụ, liệt kê các bước đầu tiên và bắt đầu thực hiện; không chờ người dùng duyệt lại các bước đã được ủy quyền.
7. Nếu không có nhiệm vụ mới, báo không có nhiệm vụ đã duyệt đang chờ.

## Cách nhận lệnh

GitHub không tự động đánh thức phiên Claude Code. Mặc định, người dùng cần mở Claude Code và gửi:

> Đọc `PROMPTS/00_CLAUDE_START_HERE.md` trong `ndtangoss-dev/jx1-reports`, kiểm tra nhiệm vụ mới đã được duyệt và thực hiện theo quy trình.

Chỉ được chạy tự động khi đã cấu hình và kiểm thử một watcher/automation riêng. Không được giả định rằng chỉ vì prompt đã được push lên GitHub thì Claude đã nhận hoặc chạy.