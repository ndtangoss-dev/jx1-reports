# CODEX-01 — ĐỒNG BỘ QUY TẮC LÀM VIỆC NHANH 5–10 PHÚT

Task ID: CODEX-01-LEAN-RULES-20261115
Trạng thái: READY_FOR_DIRECT_CLI
Executor: Codex CLI — giữ nguyên model/provider/effort hiện tại của người dùng: **Sol Max**. Không thay đổi model, provider, reasoning, CODEX_HOME hay cấu hình CLI.

## Mục tiêu

Đồng bộ hướng dẫn làm việc tại workspace JX1 với quy trình Direct CLI mới trên GitHub, loại bỏ các chỉ thị cũ gây lặp thao tác, nhưng không làm mất các rào chắn an toàn và không làm gián đoạn công việc đang dở.

## Phạm vi

Workspace: `C:\Jx1CocoV3`

- Đọc `AGENTS.md` ở root.
- Chỉ đọc thêm file hướng dẫn khác nếu AGENTS.md dẫn chiếu trực tiếp và cần thiết để sửa mâu thuẫn.
- Đối chiếu với bản chuẩn trên GitHub:
  - `PROMPTS/CODEX_DIRECT_CLI_RULES.md`
  - `WORKFLOW_JX1.md`
  - `PROMPTS/00_CODEX_START_HERE.md`

Nguồn chuẩn: repository `ndtangoss-dev/jx1-reports`, nhánh `main`.

## Yêu cầu bắt buộc

1. Giữ nguyên model Sol Max đang sử dụng. Không chạy kiểm tra model/config, không đổi model/provider/reasoning, không sửa config CLI.
2. Cập nhật `AGENTS.md` để phản ánh đúng quy trình Direct CLI:
   - Người dùng kích hoạt Codex trực tiếp; không Dispatcher, không polling queue.
   - Không đọc lại toàn bộ báo cáo/workflow mỗi task.
   - Không preflight hoặc kiểm tra lặp cấu hình/remote/workspace khi phiên đã xác nhận.
   - Chỉ đọc file cần thiết cho task; không tự khám phá toàn repo.
   - Không tạo báo cáo tiến độ/trung gian; một báo cáo cuối.
   - Không lặp thao tác đã hoàn thành; nếu tiếp tục phiên đang dở thì resume từ checkpoint, không chạy lại từ đầu.
   - Trao đổi và báo cáo tiếng Việt.
3. Bổ sung nguyên tắc timebox: mỗi đơn vị công việc phải được thiết kế để hoàn thành trong khoảng 5–10 phút. Một đơn vị phải có đầu ra kiểm chứng được, không dừng ở việc lập kế hoạch hoặc chỉ báo đang làm.
4. Nếu yêu cầu lớn hơn 10 phút, tự chia thành các đơn vị nhỏ có thể hoàn tất độc lập. Mỗi lượt chỉ xử lý một đơn vị, hoàn tất và bàn giao kết quả rồi mới nhận đơn vị kế tiếp. Không bỏ dở một đơn vị giữa chừng chỉ để chuyển sang việc khác.
5. Nếu phát hiện công việc đang dở từ task trước:
   - Không xóa, reset, ghi đè hoặc khởi động lại.
   - Kiểm tra checkpoint và trạng thái hiện có đúng một lần.
   - Nếu thuộc phạm vi và có thể hoàn thành an toàn trong 5–10 phút, hoàn tất phần đang dở trước.
   - Nếu lớn hơn hoặc không rõ trạng thái, giữ nguyên, ghi rõ điểm tiếp tục và báo người dùng; không tự ý tiếp tục một thay đổi rủi ro.
6. Giữ nguyên các rào chắn:
   - Không tác động Main VM/server production nếu chưa được duyệt.
   - Không sửa Cocos canonical nếu chưa được duyệt.
   - Không xóa/ghi đè dữ liệu không thể khôi phục.
   - Không reset/clean thay đổi local của người dùng.
   - Không lộ secret/credential.
   - Không bypass sandbox/approval.
7. Không thay đổi source game, server, build, APK, VM, Dispatcher, Task Scheduler hoặc dữ liệu dự án trong task này. Chỉ sửa `AGENTS.md` và tạo báo cáo cuối.
8. Không sửa các file hướng dẫn trên GitHub nếu chúng đã khớp; chỉ cập nhật file thật sự mâu thuẫn và nằm trong phạm vi được nêu. Không thay đổi prompt AMOLX-02 đã ghim.
9. Trước khi ghi, kiểm tra Git status một lần. Giữ nguyên mọi thay đổi có sẵn. Sau khi sửa, xem diff một lần và chỉ stage/commit đúng file thuộc task.
10. Tạo báo cáo duy nhất:
   `TEST_RESULTS/CODEX-01-LEAN-RULES-20261115.md`

## Điều kiện kết thúc

- Hoàn tất trong 5–10 phút nếu môi trường cho phép.
- Nếu có blocker, không tìm cách vòng qua; ghi chính xác blocker và hoàn tất báo cáo trong cùng lượt.
- Báo cáo nêu nội dung AGENTS.md đã cập nhật, các quy tắc cũ đã loại bỏ, rào chắn được giữ, file/diff, trạng thái Git và commit/link.
- Commit/push chỉ thay đổi được phép. Nếu không push được, ghi rõ `BỊ CHẶN – CHƯA PUSH`; không đổi credential/config để vượt lỗi.

## Không làm

- Không đọc lại toàn bộ lịch sử hoặc báo cáo JX1.
- Không chạy preflight, config check, model check, CLI help, Dispatcher hoặc Scheduler.
- Không tạo thêm kế hoạch, checklist dài hay báo cáo trung gian.
- Không sửa bất kỳ source code/gameplay/server nào.
- Không tuyên bố hoàn thành nếu chưa có diff và bằng chứng.
