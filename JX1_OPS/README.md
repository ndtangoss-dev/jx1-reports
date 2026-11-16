# JX1_OPS – ĐIỂM BẮT ĐẦU CHO MỌI AI

Nhánh `jx1-ops` của `ndtangoss-dev/jx1-reports` là **nơi duy nhất** giữ quy trình, kế hoạch, trạng thái và tiến độ của đội AI JX1. Không dựa vào lịch sử chat hay Memory của bất kỳ tài khoản nào. Không hỏi chủ dự án kể lại dự án.

## Bạn là ai?
- **PM (mặc định Claude Sonnet) hoặc PM kế nhiệm:** đọc theo thứ tự dưới đây, rồi làm theo mục "/tiep-tuc" trong `QUY-TAC-VAN-HANH.md` mục 7.
- **Worker (Codex, agent con):** chỉ đọc `QUY-TAC-VAN-HANH.md` mục 3–5, mục 12.1 và file task được giao; làm phần "Worker kiểm tra trước khi làm" trong file task trước tiên. Không đọc gì khác nếu task không yêu cầu.

## Thứ tự đọc của PM
1. `STATE/BAN-GIAO.md` – PM trước để lại gì.
2. `STATE/TRANG-THAI.md` – dự án đang ở đâu, bước tiếp theo, đường dẫn, ngân sách.
   `STATE/KHOA.md` – worker nào đang giữ vùng file, tài nguyên nào.
3. `QUY-TAC-VAN-HANH.md` – cách làm việc, quyền hạn, điểm lưu.
4. `KE-HOACH-TONG-THE.md` – kế hoạch (đọc kỹ lần đầu; các lần sau chỉ mở phần cần).
5. `TASKS/BACKLOG.md` và các file task đang `active`, `review`.
6. `STATE/QUYET-DINH.md` – điều đã chốt, không được đổi.
7. Báo cáo mới nhất trong `REPORTS/daily/`.
8. `ENVIRONMENT.md` – máy, công cụ, lệnh (Sonnet tạo ở task 0-02).

## Văn bản của chủ dự án (thứ tự ưu tiên: số lớn hơn thắng)
- `FABLE_HANDOVER_v0.3/docs/owner-inputs/01…04` (Master Prompt gốc và các yêu cầu sau đó)
- `owner-inputs/05` – cập nhật định hướng ngày 16/11 (dùng lại client, server gốc; Sonnet PM)
- `owner-inputs/06` – chỉ thị vận hành ngày 16/11 (bỏ ChatGPT, phòng ban, Dispatcher; nhánh riêng; tự động tối đa)

## Không được làm
Xem `QUY-TAC-VAN-HANH.md` mục 3 (vùng Đỏ và rào chắn) và `STATE/QUYET-DINH.md`.

## Nhánh `main`
Chứa lịch sử báo cáo (FIX_HISTORY, TEST_RESULTS, SERVER, CLIENT, knowledge…) – đọc để tra cứu. Quy tắc trên `main` (AGENTS.md, WORKFLOW_JX1.md, PROMPTS/*, 00_PROJECT_CONTROL/*) **đã hết hiệu lực**.
