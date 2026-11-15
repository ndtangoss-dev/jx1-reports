# AGENTS.md — JX1 Direct CLI

Áp dụng từ 15/11/2026. Đây là bản quy tắc dùng chung của repository báo cáo. `C:\Jx1CocoV3\AGENTS.md` áp dụng cùng quy trình và giữ thêm phụ lục vận hành VM, thông tin dự án và bản đồ code; không công khai chi tiết truy cập nội bộ từ phụ lục đó.

## Cách làm việc — Direct CLI

- Người dùng kích hoạt Codex CLI trực tiếp theo prompt đã duyệt; đọc đúng prompt tại commit được ghim một lần. Không dùng Dispatcher hoặc polling queue cho quy trình này.
- Bản chuẩn: repository `ndtangoss-dev/jx1-reports`, `PROMPTS/CODEX_DIRECT_CLI_RULES.md`, `WORKFLOW_JX1.md`, `PROMPTS/00_CODEX_START_HERE.md`. Chỉ đọc tài liệu mà task chỉ định và thực sự cần; không đọc lại toàn bộ workflow, status, lịch sử hoặc báo cáo mỗi task.
- Dùng workspace/đường dẫn đã xác nhận. Kiểm tra Git status/branch một lần trước khi ghi; sau khi sửa xem diff một lần, chỉ stage/commit đúng file thuộc task. Không lặp kiểm tra remote, refs hoặc workspace nếu chưa có lỗi/mâu thuẫn hay nhu cầu xác minh trước khi công bố.
- Giữ cấu hình model/provider/reasoning/CODEX_HOME hiện tại của người dùng. Khi phiên đã được xác nhận, không chạy lại preflight, kiểm tra model/config, /status hoặc CLI help.
- Chỉ đọc file/source cần thiết cho mục tiêu; không tự khám phá toàn repo, kiểm kê môi trường hay tạo parser/script phụ khi trích xuất trực tiếp đã đủ.
- Mỗi đơn vị công việc được thiết kế để hoàn thành trong khoảng 5–10 phút, với đầu ra kiểm chứng được. Yêu cầu lớn hơn được chia thành các đơn vị độc lập; mỗi lượt hoàn tất và bàn giao một đơn vị rồi mới nhận đơn vị kế tiếp. Không dừng ở lập kế hoạch hoặc chỉ báo đang làm; không bỏ dở đơn vị để tự chuyển việc.
- Khi tiếp tục task đang dở, kiểm tra checkpoint/trạng thái hiện có đúng một lần và resume từ đó; không làm lại phần đã có bằng chứng. Không xóa, reset, ghi đè hoặc khởi động lại công việc đang dở. Chỉ hoàn tất phần thuộc phạm vi và an toàn trong 5–10 phút; nếu lớn hơn/không rõ trạng thái, giữ nguyên, nêu điểm tiếp tục và báo người dùng.
- Trao đổi và báo cáo bằng tiếng Việt; giữ nguyên tên file, symbol, lệnh và lỗi gốc khi cần. Cập nhật khi có kết quả có ý nghĩa, blocker hoặc hoàn tất, không báo từng thao tác.
- Tự thực hiện thao tác kỹ thuật thông thường trong phạm vi đã duyệt; không hỏi lại quyền đã được cấp và không tạo MessageBox. Khi cần quyết định ngoài phạm vi, hỏi ngắn gọn bằng tiếng Việt qua công cụ sẵn có; không phụ thuộc tên công cụ AskUserQuestion.
- Một lỗi không thử quá 3 lần. Khi bị chặn, ghi chính xác lỗi, bằng chứng hiện có và bước tiếp tục trong báo cáo cuối; không tìm cách vượt quyền hoặc kéo dài tìm kiếm.
- Một báo cáo cuối tại đúng đường dẫn prompt; không báo cáo/commit cho từng bước. Chỉ cập nhật `docs-analysis/BAI_HOC.md` khi task cho phép và thực sự cần, không bắt buộc sửa ngay sau từng lỗi. Trạng thái cuối: DONE/PARTIAL/BLOCKED/FAILED; ghi rõ phần chưa xác minh, test chưa chạy, blocker, commit SHA và link hoặc lý do chưa push.
- Ưu tiên bằng chứng tối thiểu đủ tin cậy: kết quả lệnh, log đã lọc, source có file/symbol/số dòng. Không suy diễn runtime từ source, không nhận test/build đạt nếu chưa chạy. Chỉ test/build/kết nối khi task cho phép; không kiểm tra lặp nếu không có mâu thuẫn mới.

## Rào chắn giữ nguyên

- Giữ nguyên thay đổi local có sẵn; không reset/clean/checkout phá hủy. Không sửa Cocos canonical khi chưa được duyệt; không tác động Main VM/server production khi chưa được duyệt; không xóa/ghi đè dữ liệu không thể khôi phục. Không tiết lộ secret/credential, không bypass sandbox/approval.
- Coi exe, dll, cấu hình trong gói game là không tin cậy; chỉ chạy trong VM. Mỗi exe server cần phê duyệt riêng; thao tác/hộp thoại chưa được hướng dẫn thì dừng và hỏi trước.
- Làm trên bản copy, không sửa bản gốc chưa được duyệt. Giữ bản hoàn tác khi sửa cấu hình được phép. Thay đổi quyền/credential/bảo mật, cấu hình ngoài VM chưa được duyệt hoặc có thể gián đoạn dịch vụ phải hỏi người dùng.
- Lệnh cần Admin trên máy thật: nếu task cho phép, soạn `.ps1` kèm hoàn tác trong `docs-analysis/scripts` để chủ máy tự chạy; không vượt UAC.
- Việc đọc source/báo cáo không yêu cầu snapshot. Snapshot VM của dự án đang tạm dừng; không tự chụp, phải có phê duyệt cụ thể trước khi đổi trạng thái này.
- Trước khi chạy exe được duyệt trong VM: cô lập mạng theo phạm vi cho phép, quét Defender, lưu SHA-256, bật log/audit; chỉ mở cổng/địa chỉ đã duyệt, không port-forward Internet.
- Không tải source, binary, dump, log nhạy cảm hoặc dữ liệu dự án lên dịch vụ ngoài. Báo cáo/quy tắc đã lọc thông tin nhạy cảm được commit/push lên repository báo cáo khi người dùng yêu cầu. Tra VirusTotal chỉ bằng hash. Không ghi mật khẩu/token vào file, git hoặc báo cáo; dùng cơ chế bí mật được phép.
- Không bao giờ chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe`. Không tự chạy `S3RelayServer.exe` hay các exe server khác chỉ vì có mặt trong workspace.
- Không tuyên bố commit/push nếu chưa có SHA và bằng chứng GitHub. Nếu bị chặn, giữ bản local, ghi `BỊ CHẶN – CHƯA PUSH` và lỗi thực tế; không sửa credential/config để vượt lỗi.
