# START HERE – DÀNH CHO AI VỪA TIẾP QUẢN

Bạn là AI mới của dự án JX1, có thể là Project Manager kế nhiệm hoặc một worker. Mọi thứ bạn cần nằm trong repository này. **Không hỏi chủ dự án kể lại dự án.** Chủ dự án không lập trình; chỉ hỏi khi cần một quyết định thuộc quyền của họ.

Không dựa vào Memory của Claude, ChatGPT, Codex hay lịch sử chat của bất kỳ tài khoản nào. Nếu bạn "nhớ" điều gì mà repository không ghi, coi như chưa xác minh.

## 1. Đọc theo thứ tự

| # | Đọc | Để biết |
|---|---|---|
| 1 | `docs/owner-inputs/` (README trước) | Chủ dự án thực sự yêu cầu gì, nguyên văn |
| 2 | `docs/00-PROJECT-MASTER.md` | Mục tiêu, nguyên tắc bất biến, vai trò |
| 3 | `AGENTS.md` (trước khi có thì `AI-OPERATING-RULES.md`) | Cách đội AI làm việc |
| 4 | `project-state/HANDOVER.md` | PM trước để lại gì cho bạn |
| 5 | `project-state/CURRENT-STATUS.md`, `NEXT-ACTIONS.md`, `RISKS.md` | Dự án đang ở đâu, làm gì tiếp |
| 6 | `docs/12-DECISIONS/` | Quyết định đã chốt và lý do |
| 7 | `project-state/ACTIVE-TASKS.md`, `BLOCKED-TASKS.md` và các file trong `tasks/active/`, `tasks/review/` | Việc đang dang dở |
| 8 | Báo cáo mới nhất trong `reports/DAILY-REPORTS/` | Chủ dự án đã được báo gì |
| 9 | `docs/ENVIRONMENT-AND-TOOLS.md` | Máy, công cụ, cách build, test, chạy game |

Worker chỉ cần mục 3, 9 và file task của mình.

## 2. Tự kiểm tra trước khi tin

Tài liệu bàn giao là lời khai, chưa phải sự thật. Trước khi làm tiếp, PM mới tự xác nhận:

- [ ] `git status`, `git log`, danh sách branch và worktree khớp với `CURRENT-STATUS.md`.
- [ ] Local và GitHub đồng bộ; không có commit chưa đẩy lên hoặc thay đổi chưa commit bị bỏ quên.
- [ ] Nhánh tích hợp build được và bộ test chạy ra kết quả như tài liệu ghi.
- [ ] Thứ được ghi là "đã chạy được" thì mở lên chạy thử thật.
- [ ] Mỗi task ở `active` và `review`: trạng thái ghi trong file khớp với code trên branch của nó.
- [ ] Công cụ trong `ENVIRONMENT-AND-TOOLS.md` còn hoạt động với tài khoản và model hiện tại.

Chỗ nào không khớp: tin thực tế, sửa tài liệu, ghi một dòng vào `HANDOVER.md`.

## 3. Nếu không có bản bàn giao cuối (PM trước bị ngắt đột ngột)

1. Tìm lần lưu trạng thái gần nhất: commit mới nhất có sửa `project-state/`.
2. Liệt kê mọi thứ xảy ra **sau** thời điểm đó: commit mới hơn, thay đổi chưa commit trong các worktree, task đang `active` mà chưa có mục "Kết quả".
3. Coi tất cả những thứ đó là **chưa xác nhận**. Với từng cái: build và test; đạt thì commit và cập nhật task; không đạt hoặc không hiểu được thì cất sang một branch `wip/` kèm ghi chú, không xóa.
4. Viết lại `CURRENT-STATUS.md` theo thực tế, rồi làm tiếp từ `NEXT-ACTIONS.md`.

## 4. Không được thay đổi hoặc làm lại tùy tiện

- Nguyên tắc bất biến INV-01…INV-16 trong `docs/00-PROJECT-MASTER.md`. Đặc biệt: client Axmol, không Unity; server riêng; **thế giới Bot dùng chung** (mọi người chơi thấy cùng một Bot, A giết thì chết với tất cả); người chơi thật chỉ thấy nhau trong hoạt động có giới hạn.
- Quyết định đã chấp nhận trong `docs/12-DECISIONS/`. Muốn đổi phải viết quyết định mới nêu lý do; chạm định hướng game thì chủ dự án quyết.
- Việc đã hoàn thành và đã nghiệm thu. Không viết lại vì "tôi sẽ làm khác". Chỉ làm lại khi có lỗi được chứng minh bằng test.
- Các điểm gameplay còn bỏ ngỏ (mục H của `docs/01-PRODUCT-REQUIREMENTS.md`): không tự quyết.
- Danh sách bổ sung do PM duy trì:
  - *(PM ghi thêm tại đây: thứ đã thử và thất bại không nên thử lại, thứ dễ bị làm hỏng…)*

## 5. Sau khi tiếp quản

- Ghi vào `project-state/HANDOVER.md` một dòng: ngày giờ, bạn là model nào, tài khoản loại nào, kết quả kiểm tra ở mục 2.
- Cập nhật `agents/registry/`.
- Gửi chủ dự án **một** thông báo ngắn: đã tiếp quản, trạng thái đã xác nhận, đang làm tiếp việc gì, có cần quyết định gì không.
- Làm tiếp đúng việc còn dang dở. Không đổi định hướng.
