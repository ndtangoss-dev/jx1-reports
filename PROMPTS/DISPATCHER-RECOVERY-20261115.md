---
task_id: DISPATCHER-RECOVERY-20261115-01
status: APPROVED
scope: Repair JX1 Task Dispatcher reliability and safe autonomy so routine approved tasks run without repeated user popups. Preserve explicit boundaries for destructive/production actions.
allowed_paths:
  - docs-analysis/scripts/jx1_task_dispatcher.py
  - docs-analysis/scripts/install_jx1_task_dispatcher.ps1
  - docs-analysis/scripts/status_jx1_task_dispatcher.ps1
  - docs-analysis/scripts/enable_jx1_task_dispatcher.ps1
  - docs-analysis/scripts/disable_jx1_task_dispatcher.ps1
  - docs-analysis/scripts/test_jx1_task_dispatcher.py
  - TEST_RESULTS/DISPATCHER-RECOVERY-20261115.md
---

# DISPATCHER-RECOVERY-20261115-01 — Khắc phục Dispatcher và tự động hóa an toàn

Người dùng đã ủy quyền rõ ràng để Codex tự thực hiện các thao tác kỹ thuật thông thường trong phạm vi JX1, không hỏi duyệt từng bước nhỏ. Mục tiêu là giảm tối đa hộp thoại và thao tác thủ công, tăng tốc công việc JX1.

## 0. Điều kiện đầu tiên
- Làm việc trong `C:\Jx1CocoV3`.
- Đọc `AGENTS.md`, workflow và báo cáo Dispatcher hiện có.
- Xác minh Git status và giữ nguyên mọi thay đổi có sẵn của người dùng.
- Kiểm tra đúng các script local hiện đang được cài; không giả định repo GitHub chứa script nếu không có.
- Không tự ý thay đổi quyền sandbox toàn cục, Windows policy, firewall, credential hoặc config tài khoản ngoài phạm vi.
- Nếu script đang chạy, không ghi đè file đang được process sử dụng theo cách làm hỏng tiến trình; tạo bản sao backup và áp dụng an toàn.

## 1. Sửa lỗi polling GitHub trước tiên
Ảnh/log gần nhất ghi `github_poll_failed`, `HTTPError`, và `Test-NetConnection api.github.com:443` thất bại từ sandbox. Hãy phân biệt rõ:
- DNS/TCP/connectivity lỗi.
- HTTP 401/403/404/429/5xx.
- Rate limit và secondary rate limit.
- ETag/304.
- Credential không có hoặc không hợp lệ.

Yêu cầu:
- Polling từ host process dùng Git Credential Manager hoặc credential store hiện có, không in token và không ghi token vào log.
- Không gọi API GitHub unauthenticated nếu có credential an toàn sẵn có.
- Xử lý 401/403/429/5xx bằng exponential backoff có jitter và log nguyên nhân/status code; không spam popup.
- Với lỗi mạng tạm thời: tiếp tục chạy nền, retry theo backoff, không chuyển task đã APPROVED thành BLOCKED chỉ vì một lần poll lỗi.
- Không hiện MessageBox lặp. Chỉ log; thông báo người dùng tối đa một lần cho một sự cố mới, hoặc dùng Windows notification nếu đã có cơ chế an toàn. Mặc định không chiếm foreground.
- Không tải nội dung queue không xác thực hoặc bỏ qua SHA pin.

## 2. Cơ chế tự chủ và approval
- Bỏ yêu cầu người dùng xác nhận cho thao tác kỹ thuật thông thường nằm trong prompt đã APPROVED: đọc/ghi trong allowed paths, chạy test, build thử, ADB/LDPlayer test, lấy log, tạo backup và báo cáo.
- Cấu hình Codex exec không tương tác phù hợp để không bật hộp thoại hỏi user cho mỗi lệnh thường lệ; chỉ tự thực hiện trong sandbox và phạm vi task.
- Không dùng `danger-full-access`, `--yolo`, `--dangerously-bypass-approvals-and-sandbox`, không tắt sandbox, không cấp quyền admin rộng.
- Nếu Codex gặp thao tác bị sandbox chặn, không bật hộp thoại liên tục và không tự nâng quyền. Ghi trạng thái BLOCKED với một lý do cụ thể, giữ log, tiếp tục polling các task độc lập nếu an toàn.
- Không hỏi duyệt lại từng bước đã được user ủy quyền trong prompt.
- Người dùng đã ủy quyền thao tác thông thường, nhưng vẫn giữ chốt an toàn bắt buộc cho: xóa/ghi đè không thể khôi phục, Main VM/server production, dữ liệu tài khoản, firewall/security/credentials, thay đổi kiến trúc/gameplay lớn, hoặc hành động ngoài phạm vi đã duyệt. Với các trường hợp này, dừng đúng một lần, ghi BLOCKED và nêu lựa chọn tối thiểu.

## 3. Xử lý source nằm ngoài workspace — trường hợp AMOLX
Task AMOLX đang bị BLOCKED vì source ở:
`C:\JX1\jx1client-amol-main\jx1client-amol-main`
trong khi Codex cwd là `C:\Jx1CocoV3`.

Thiết kế một cách an toàn để Codex đọc source ngoài workspace mà không cho phép ghi:
- Ưu tiên dùng sandbox/config chính thức hỗ trợ thêm read-only root hoặc chạy audit trong một workspace read-only phù hợp.
- Báo cáo vẫn phải ghi vào repo JX1 và được commit/push.
- Không dùng `--add-dir` nếu điều đó cấp quyền ghi cho source AMOLX mà không có biện pháp read-only được xác minh.
- Nếu phiên bản CLI hiện tại không hỗ trợ read-only external root, hãy chọn phương án có thể kiểm chứng (ví dụ tạo snapshot read-only có kiểm tra hash, hoặc tách quy trình đọc/ghi), không tự ý cấp write access vào source gốc.
- Không copy toàn bộ asset lớn nếu không cần; ưu tiên đọc README, CMake, source network/login và manifest.
- Sau khi thiết kế được quyền đọc an toàn, cập nhật task AMOLX để có thể chạy mà không cần người dùng bấm popup.

## 4. Task lifecycle
- Một task lỗi không được làm chết poller.
- Không tự retry task có thể đã chạy một phần nếu chưa có session/state xác minh; giữ at-most-once và resume đúng session.
- Task BLOCKED phải có lý do ngắn, mã lỗi, bước tiếp theo; không tạo popup lặp.
- Sau khi task COMPLETED, ghi kết quả lên GitHub, verify bằng fetch và cập nhật queue đúng SHA.
- Không chạy task khác đồng thời nếu chưa có isolation/lock đã kiểm chứng.

## 5. Kiểm thử bắt buộc
- Unit tests.
- Mock các tình huống 401, 403, 429, 500, timeout, DNS/TCP failure và 304.
- Xác nhận không có MessageBox trong retry loop.
- Xác nhận lỗi polling không làm mất task APPROVED.
- Xác nhận đọc AMOLX ngoài workspace nhưng không thể ghi vào source AMOLX (nếu tính năng read-only root được hỗ trợ).
- Xác nhận các thao tác trong allowed paths chạy không cần popup tương tác.
- Không reboot Windows trong task này.
- Không kết nối Main VM/server production.
- Không thực hiện AMOLX audit trong task recovery; chỉ sửa hạ tầng và chuẩn bị điều kiện để chạy AMOLX tiếp.

## 6. Báo cáo
Tạo `TEST_RESULTS/DISPATCHER-RECOVERY-20261115.md` bằng tiếng Việt, nêu:
- Nguyên nhân gốc của HTTP errors.
- Các thay đổi và file cụ thể.
- Cách quyền đọc AMOLX được giới hạn.
- Approval/sandbox thực tế sau thay đổi.
- Test results và log.
- Những việc vẫn cần người dùng can thiệp (nếu có), chỉ nêu điều thực sự không thể tự xử lý.
- Cách rollback an toàn.
- Xác nhận Dispatcher vẫn chạy nền và không hiện popup lặp.

Không tuyên bố tự động hóa thành công nếu chỉ unit test; cần kiểm thử end-to-end trong điều kiện an toàn.
