# AI OPERATING RULES

Phiên bản v0.1 – 2026-11-16 – Fable soạn, Opus sở hữu sau bàn giao.

> `C:\Jx1CocoV3\AGENTS.md` đã tồn tại. File này **không** ghi đè lên nó. Opus đọc `AGENTS.md` hiện có, hợp nhất hai bên, rồi để `CLAUDE.md` và `CODEX.md` chỉ trỏ về `AGENTS.md` kèm phần riêng của từng công cụ.

---

## 1. Thứ tự ưu tiên khi có xung đột

1. Quyết định trực tiếp của chủ dự án.
2. Nguyên tắc bất biến INV-01…INV-12 (`docs/00-PROJECT-MASTER.md`).
3. ADR đã được chấp nhận (`docs/12-DECISIONS/`).
4. Tài liệu này.
5. Chỉ dẫn trong task.
6. Suy luận của AI.

Worker gặp xung đột ở cấp 1–3 thì dừng phần liên quan, ghi vào task, báo Opus. Không tự diễn giải lại.

## 2. Mọi AI khi bắt đầu phiên làm việc

1. Đọc `AGENTS.md`, `project-state/CURRENT-STATUS.md`, `project-state/NEXT-ACTIONS.md`.
2. Đọc file task được giao và tài liệu đầu vào ghi trong task.
3. Chạy `git status`, `git log -5`, kiểm tra đúng branch và worktree.
4. Chỉ sau đó mới sửa file.

Không dựa vào trí nhớ phiên trước hay công cụ memory làm nguồn duy nhất. Git và tài liệu dự án là nguồn chính.

## 3. Quy tắc của Project Manager (Opus)

Opus phải:

- Xác minh tài liệu Fable bàn giao với GitHub và local trước khi dùng.
- Hoàn thiện kiến trúc, viết ADR cho quyết định L4–L5.
- Chia milestone, module, task; phân tích phụ thuộc trước khi chia.
- Chốt hợp đồng API, schema, giao thức **trước** khi cho nhiều worker làm song song.
- Phân loại độ khó và chọn model cho từng task.
- Tự kiểm tra bằng chứng: đọc diff, chạy build, chạy test, xem kết quả thật. Không chỉ đọc báo cáo của worker.
- Tổ chức review, tích hợp, kiểm thử sau tích hợp.
- Cập nhật `project-state/` sau mỗi thay đổi trạng thái.
- Viết báo cáo cuối ngày.

Opus không được: đổi mục tiêu sản phẩm; tự quyết các việc ảnh hưởng lớn đến định hướng game; dành phần lớn thời gian cho việc đơn giản, lặp lại.

## 4. Quy tắc của worker

- Chỉ sửa file trong danh sách "được phép sửa" của task. Cần sửa file khác thì ghi đề nghị vào task, chờ Opus.
- Làm đến khi có kết quả kiểm chứng được. "Đã viết code" chưa phải hoàn thành.
- Trước khi chuyển task sang `review`: build thành công, test trong task chạy thật và qua, đính kèm lệnh và đầu ra.
- Không viết test giả, không tắt test để qua, không báo placeholder là xong. Phần chưa làm ghi rõ là chưa làm.
- Không merge vào nhánh chính.
- Mỗi phát biểu về hiện trạng gắn nhãn tin cậy (`[SRC]`, `[TEST]`, `[RPT]`, `[HYP]`...).
- Đổi giao thức, schema, interface dùng chung thì phải cập nhật tài liệu trong cùng commit và báo Opus.
- Bị chặn quá giới hạn thử ghi trong task thì dừng, ghi lại đã thử gì, chuyển trạng thái `blocked`.

## 5. Quyền tự chủ

Không hỏi chủ dự án cho các bước thông thường. Phân loại thao tác:

**Nhóm A – Tự động.** Thao tác đảo ngược được trong workspace thử nghiệm: đọc source, phân tích, chạy lệnh, build, test, tạo task, tạo branch, commit trên nhánh task, viết báo cáo, cập nhật tài liệu.

**Nhóm B – Tự động có kiểm soát.** Cài dependency, đổi cấu hình phát triển, tạo hoặc dọn worktree, đổi cấu hình build. Bắt buộc: ghi log vào báo cáo task (làm gì, phiên bản, cách khôi phục).

**Nhóm C – Phải xin phép chủ dự án.**
- Xóa dữ liệu không khôi phục được.
- Ghi đè source gốc.
- Đổi dữ liệu production.
- Đổi server đang vận hành.
- Đổi credential hoặc quyền bảo mật.
- Force push hoặc ghi đè lịch sử Git quan trọng.
- Công khai mã nguồn hoặc bí mật.
- Phát sinh chi phí ngoài ngân sách.

Với Nhóm C: chuẩn bị xong mọi thứ, mô tả thao tác, rủi ro và cách khôi phục, đưa vào mục "Cần chủ dự án quyết" của báo cáo ngày, rồi dừng đúng phần đó và làm việc khác. Không rõ thao tác thuộc nhóm nào thì coi như nhóm cao hơn.

Bí mật (mật khẩu, token, khóa Tailscale, chuỗi kết nối DB) không đưa vào Git, task hay báo cáo.

## 6. Git và worktree

- Mỗi task một branch. Đề xuất tên: `task/<TASK-ID>-<mô-tả-ngắn>`.
- Worker chạy song song thì mỗi worker một worktree. Không hai worker sửa cùng một thư mục làm việc.
- Mọi thay đổi có commit. Thông điệp commit bắt đầu bằng Task ID.
- Review trước khi merge. Kiểm thử sau tích hợp. Mỗi lần merge phải rollback được.
- Chỉ Opus merge vào nhánh tích hợp. Chiến lược branch, đặt tên, dọn worktree do Opus quyết và ghi thành ADR.
- Thư mục chứa source JX1 gốc là chỉ đọc.

## 7. Vòng đời task

`backlog` → `active` → `review` → `completed`, nhánh phụ `blocked`.

| Chuyển trạng thái | Điều kiện |
|---|---|
| backlog → active | Đủ trường bắt buộc, phụ thuộc đã xong, đã gán agent và branch. |
| active → review | Worker đính kèm commit, lệnh build/test, đầu ra, danh sách file đã sửa, phần còn thiếu. |
| review → completed | Reviewer theo đúng cấp (xem Model Assignment Policy) xác nhận bằng chứng. |
| review → active | Reviewer ghi lỗi cụ thể, giữ nguyên Task ID. |
| bất kỳ → blocked | Ghi nguyên nhân, đã thử gì, cần gì để gỡ. |

File task di chuyển giữa `tasks/backlog|active|review|completed/`. Mẫu: `tasks/TASK-TEMPLATE.md`.

## 8. Thay thế AI

Khi đổi worker có kế hoạch, AI cũ: cập nhật task; ghi kết quả và file đã sửa; commit phần hợp lệ; ghi lỗi và các thử nghiệm thất bại; cập nhật `HANDOVER.md`. AI mới: đọc tài liệu, kiểm tra Git và worktree, tiếp tục từ trạng thái hiện tại.

Khi AI cũ mất kết nối đột ngột, AI mới dựng lại trạng thái từ file task, Git (`git log`, `git status`, `git stash list`, diff chưa commit trong worktree), báo cáo và worktree. Thay đổi chưa commit được xem xét rồi commit dạng `WIP` hoặc loại bỏ có ghi chú, không lặng lẽ xóa.

Khi đổi model do không hoàn thành được: giữ nguyên Task ID và lịch sử, đánh giá lại độ khó, tiếp tục từ kết quả đã có. Không bắt AI mới làm lại từ đầu.

Khi đổi Project Manager: PM mới đọc toàn bộ `project-state/`, báo cáo ngày gần nhất và mọi ADR trước khi giao việc.

Để việc này luôn khả thi: PM cập nhật `project-state/` và commit ít nhất một lần vào cuối mỗi phiên làm việc, không đợi cuối ngày.

## 9. Công cụ và plugin

Không cài máy móc. Trước khi cài, điền bảng: Công cụ | Giá trị | Chi phí | Rủi ro | Tương thích | Quyết định, và xếp loại: Bắt buộc, Nên cài, Có thể cài sau, Không cần thiết, Trùng chức năng, Không tương thích.

Kiểm tra xung đột: nhiều hệ thống bộ nhớ cùng ghi; nhiều lớp nén context; xung đột MCP và hooks; đổi model làm mất tương thích tool; plugin không hợp phiên bản Claude Code.

Công cụ bộ nhớ chỉ là lớp tăng tốc. Nếu gỡ nó đi mà dự án không tiếp tục được thì đang vi phạm INV-10.

Nếu Orchestrator đáp ứng nhu cầu thì dùng, chỉ tự xây phần còn thiếu.

## 10. Báo cáo cuối ngày

Lưu tại `reports/DAILY-REPORTS/YYYY-MM-DD.md`, mẫu trong `docs/PROJECT-MEMORY-STRUCTURE.md`. Viết cho chủ dự án đọc trên điện thoại: kết quả trước, chi tiết sau, phần "Cần chủ dự án quyết" đặt ngay đầu.

Phần quy định báo cáo trong Master Prompt gốc bị cắt, mẫu này là đề xuất của Fable.
