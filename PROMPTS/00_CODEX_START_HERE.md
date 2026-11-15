# CODEX CLI – ĐIỂM BẮT ĐẦU / KIỂM TRA NHIỆM VỤ MỚI

Repository: `ndtangoss-dev/jx1-reports`
Quy trình chính: [WORKFLOW_JX1.md](../WORKFLOW_JX1.md)
Trạng thái dự án: [00_LATEST_STATUS.md](../00_LATEST_STATUS.md)

## Khi người dùng kích hoạt hoặc bắt đầu phiên làm việc

1. Xác minh trạng thái phiên bằng `/status`: model, provider, reasoning effort và working directory.
   - Mặc định dự kiến cho phiên JX1: `gpt-6.1-sol`, provider `xingchi`, reasoning `max`.
   - Nếu sai hoặc không xác minh được, báo **BỊ CHẶN**; không âm thầm dùng provider/model khác.
2. Đọc đầy đủ `WORKFLOW_JX1.md` và `00_LATEST_STATUS.md`.
3. Kiểm tra `PROMPTS/` và các chỉ thị bắt đầu để tìm nhiệm vụ có trạng thái **ĐƯỢC DUYỆT / BẮT ĐẦU THỰC HIỆN**.
4. Đọc đầy đủ prompt nhiệm vụ được chỉ định và mọi tài liệu được prompt tham chiếu. Không tự thực hiện bản nháp/chưa được duyệt.
5. Xác minh đúng source, branch, working directory, công cụ build/test, emulator/ADB và VM thử nghiệm trước khi thao tác. **Không can thiệp Main VM.**
6. Kiểm tra trạng thái Git (branch, working tree, thay đổi chưa commit) trước khi sửa; không ghi đè thay đổi có sẵn của người dùng.
7. Xác định backup/rollback phù hợp trước thay đổi có rủi ro.
8. Xác nhận ngắn gọn nhiệm vụ, phạm vi, model/provider, môi trường và các bước đầu tiên; bắt đầu thực hiện mà không hỏi lại các bước thông thường đã được duyệt.
9. Nếu không có nhiệm vụ đã duyệt, báo rõ không có nhiệm vụ mới và không tự chọn một bản nháp để chạy.

## Lệnh kích hoạt mặc định

Người dùng mở phiên Codex CLI và gửi:

> Đọc `PROMPTS/00_CODEX_START_HERE.md` trong `ndtangoss-dev/jx1-reports`, kiểm tra nhiệm vụ mới đã được duyệt và thực hiện theo quy trình.

GitHub không tự động đánh thức phiên Codex CLI. Không được giả định rằng chỉ vì prompt đã được push lên GitHub thì Codex đã nhận hoặc chạy.

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
