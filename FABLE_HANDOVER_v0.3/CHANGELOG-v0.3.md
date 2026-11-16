# CHANGELOG v0.3

Ngày 2026-11-16 · Fable · Chưa bàn giao Opus, chưa triển khai source.

## 1. Bỏ Secret Vault và bảo mật phức tạp

- Xóa `docs/SECRET-VAULT.md`.
- Bỏ INV-14, PR-OWN-04, trường `secrets` trong mẫu task, bước "dựng vault" trong kế hoạch ngày 1 và M0, các rủi ro và việc xác minh liên quan trong gói bàn giao.
- Còn giữ: một dòng quy tắc thông thường (không đưa mật khẩu, token lên GitHub hay vào báo cáo), và danh sách việc phải xin phép chủ dự án lấy từ Master Prompt (trong đó có đổi credential, công khai bí mật).

## 2. Chốt quy tắc thế giới Bot

- Bot là thực thể chung trong một thế giới dùng chung.
- Tất cả người chơi thấy và tương tác với cùng một Bot.
- A giết Bot thì Bot chết với B và mọi người chơi khác.
- Trạng thái, vị trí, sinh tử, hoạt động của Bot đồng bộ thống nhất; không có bản sao riêng cho từng người.
- Người chơi thật không thấy nhau ở bản đồ thường, nhưng thế giới Bot không bị tách.

Ghi tại: INV-07, INV-08 (`docs/00`), PR-BOT-07…11 và PR-VIS-01 (`docs/01`), mục "Quyết định đã chuẩn hóa" của gói bàn giao, tiêu chí thoát M4 và M6 của roadmap. Câu hỏi Q-02 đã xóa khỏi danh sách câu hỏi mở.

## 3. Bàn giao và thay thế Project Manager / AI (yêu cầu bắt buộc, bổ sung sau)

- `AI-OPERATING-RULES.md` mục 10 viết lại hoàn toàn: phép thử tiếp quản; điểm lưu trạng thái (commit và đẩy lên GitHub theo sự kiện, tối đa 1 giờ một lần, phần lớn tự động); thay PM có báo trước; PM mới tiếp quản và tự kiểm tra; phục hồi khi bị ngắt đột ngột; đổi tài khoản hoặc nhà cung cấp; thay worker; diễn tập.
- Mới: `START-HERE.md`, điểm vào cho AI kế nhiệm.
- Mới: `docs/owner-inputs/`, nguyên văn Master Prompt và ba văn bản yêu cầu, quyết định của chủ dự án.
- Mới: `docs/ENVIRONMENT-AND-TOOLS.md`, khung hướng dẫn máy và công cụ để Opus điền.
- `docs/PROJECT-MEMORY-STRUCTURE.md`: bảng tám loại thông tin phải lưu và nơi lưu; mẫu `HANDOVER.md`.
- `docs/MODEL-ASSIGNMENT-POLICY.md` (lên v0.3): thứ tự kế nhiệm vai trò PM và giới hạn của PM tạm quyền. Thay cho câu cũ "không model nào nghiệm thu thay Opus".
- INV-11, PR-OWN-05, 08, 09 cập nhật. Câu hỏi Q-09 đã xóa vì yêu cầu này đã trả lời; còn 7 câu hỏi mở.
- Roadmap: cơ chế điểm lưu phải chạy từ ngày 1; ngày 6 là diễn tập.

## 4. Tài liệu

| Tài liệu | v0.3 |
|---|---|
| `docs/00-PROJECT-MASTER.md` | Sửa |
| `docs/01-PRODUCT-REQUIREMENTS.md` | Sửa |
| `AI-OPERATING-RULES.md` | Sửa mục 9, viết lại mục 10 |
| `tasks/TASK-TEMPLATE.md` | Bỏ một trường |
| `docs/PROJECT-MEMORY-STRUCTURE.md` | Bỏ các dòng về vault |
| `docs/ROADMAP-DRAFT.md` | Sửa |
| `project-state/HANDOVER-FABLE-TO-OPUS.md` | Sửa |
| `FABLE-MASTER-PROMPT-COMPLETENESS-REPORT.md` | Chỉnh mục 7 và số câu hỏi |
| `docs/MODEL-ASSIGNMENT-POLICY.md` | Sửa mục 6 |
| `START-HERE.md`, `docs/owner-inputs/`, `docs/ENVIRONMENT-AND-TOOLS.md` | Mới |
| `docs/SECRET-VAULT.md` | Xóa |

Bản v0.1 và v0.2 nằm trong `archive/`.
