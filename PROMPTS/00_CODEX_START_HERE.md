# CODEX CLI – ĐIỂM BẮT ĐẦU / KIỂM TRA NHIỆM VỤ MỚI

Repository: `ndtangoss-dev/jx1-reports`
Quy trình chính: [WORKFLOW_JX1.md](../WORKFLOW_JX1.md)
Trạng thái dự án: [00_LATEST_STATUS.md](../00_LATEST_STATUS.md)

## Khi Dispatcher nhận task hoặc khi mở phiên thủ công

1. Dispatcher dùng `codex exec` với model `gpt-6.1-sol`, provider `xingchi`, reasoning `max`; chạy preflight chỉ đọc trước prompt. Nếu preflight không thành công/không xác minh được cấu hình thì ghi **BỊ CHẶN**.
2. Đọc đầy đủ `WORKFLOW_JX1.md`, `00_LATEST_STATUS.md`, mục tương ứng trong `PROMPTS/DISPATCH_QUEUE.json`, prompt và toàn bộ tài liệu tham chiếu được ghim SHA.
3. Chỉ nhận manifest có trạng thái `APPROVED` hoặc `ĐƯỢC DUYỆT`; bỏ qua prompt cũ đã có trước lần khởi tạo đầu.
4. Kiểm tra Task ID, commit/SHA, working directory, branch, trạng thái Git, môi trường build/test và quyền. Không ghi đè thay đổi có sẵn của người dùng; **không can thiệp Main VM**.
5. Chạy một task tại một thời điểm với sandbox `workspace-write` và approval policy `on-request`. Không bỏ qua sandbox/phê duyệt. Nếu có yêu cầu phê duyệt tương tác, dừng và ghi **BỊ CHẶN**.
6. Tạo báo cáo tiếng Việt tại `docs-analysis/reports/dispatcher-<task_id>.md`; hoàn thành, lỗi hoặc chặn đều phải có trạng thái rõ ràng. Task ID đã bắt đầu không được dispatch lại.
7. Nếu task đang chạy bị gián đoạn, chỉ resume session ID đã lưu; nếu không thể phục hồi thì **BỊ CHẶN**, không chạy prompt lần nữa.
8. Nếu không có task mới đã duyệt trong manifest, chỉ ghi trạng thái chờ; không tự chọn prompt khác.

## Dispatcher và kích hoạt thủ công

Khi Task Scheduler `JX1-Task-Dispatcher` đang bật, người dùng không cần mở terminal hay gửi prompt thủ công. Dispatcher polling `PROMPTS/DISPATCH_QUEUE.json` mỗi 60 giây.

Khi Dispatcher tắt hoặc cần xử lý sự cố, người dùng có thể mở phiên Codex CLI thủ công và gửi:

> Đọc `PROMPTS/00_CODEX_START_HERE.md` trong `ndtangoss-dev/jx1-reports`, kiểm tra `PROMPTS/DISPATCH_QUEUE.json` và thực hiện đúng task đã duyệt.

Chỉ báo Codex đã nhận/chạy sau khi có state/log phù hợp; GitHub commit đơn thuần không chứng minh task đã được thực thi.

### Manifest task được duyệt

Mỗi mục trong `PROMPTS/DISPATCH_QUEUE.json` phải có Task ID duy nhất, trạng thái `APPROVED` hoặc `ĐƯỢC DUYỆT`, phạm vi, commit ghim, blob SHA prompt, `allowed_paths` và danh sách tài liệu tham chiếu kèm SHA. Prompt tồn tại ngoài manifest không được chạy. Khi nội dung đã duyệt thay đổi, phát hành Task ID mới.

Trạng thái local: `QUEUED`, `RUNNING`, `COMPLETED`, `BLOCKED`, `FAILED`. File state, status và log nằm tại `%LOCALAPPDATA%\JX1TaskDispatcher`; không chứa token/credential. Git Credential Manager chỉ được dùng khi push báo cáo và không có credential thì báo **BỊ CHẶN – CHƯA PUSH**.

## Trong khi thực hiện

- Tuân thủ phạm vi, tiêu chí nghiệm thu và phân cấp quyền trong prompt và `WORKFLOW_JX1.md`.
- Tự đọc file, chạy lệnh và lấy log nếu có quyền; hạn chế yêu cầu người dùng thao tác thủ công vì người dùng thường điều khiển PC qua điện thoại.
- Nếu cần phê duyệt cho hành động rủi ro, dừng đúng tại bước đó và hỏi rõ.
- Không tiết lộ API Key, token, mật khẩu hoặc thông tin xác thực.
- Phân biệt rõ **ĐÃ XÁC MINH**, **CHƯA KIỂM THỬ**, **BỊ CHẶN**, **GIẢ THUYẾT**.

## Bàn giao bắt buộc

Khi hoàn tất hoặc bị chặn, phải:
1. Nêu nhiệm vụ và trạng thái cuối.
2. Liệt kê file đã đọc/thay đổi/tạo; kèm diff hoặc commit khi có.
3. Liệt kê lệnh, build, test đã chạy và kết quả thực tế.
4. Nêu phần chưa làm, lỗi còn lại, rủi ro và giả thuyết.
5. Nêu backup/rollback và artifact (APK, log, SHA256...) nếu có.
6. Cập nhật báo cáo phù hợp trong `FIX_HISTORY/`, `TEST_RESULTS/`, `CLIENT/`, `SERVER/` hoặc `PATCH_NOTES/`.
7. Cập nhật `00_LATEST_STATUS.md` nếu trạng thái dự án thay đổi.
8. Push báo cáo lên GitHub nếu có quyền và remote phù hợp. Nếu không, ghi **BỊ CHẶN – CHƯA PUSH**, lưu báo cáo cục bộ và cung cấp đường dẫn.
9. Không tuyên bố hoàn thành chỉ vì build thành công; chờ ChatGPT đối chiếu và người dùng nghiệm thu.



## Ngôn ngữ bắt buộc

- Mặc định giao tiếp, xác nhận, hỏi làm rõ, cập nhật tiến độ và bàn giao bằng **tiếng Việt**.
- Báo cáo và giải thích lỗi phải bằng tiếng Việt.
- Giữ nguyên tên code/API/model/provider, lệnh terminal và thông báo lỗi gốc bằng tiếng Anh khi cần; luôn giải thích chúng bằng tiếng Việt.
- Không trả lời toàn bộ bằng tiếng Anh trừ khi người dùng yêu cầu.
