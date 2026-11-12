# INTEGRATION_PLAN — Điều phối thực thi liên phòng ban

## Mục đích
Quy trình bắt buộc trước các đợt Claude Code thực hiện nhiều nhiệm vụ hoặc nhiệm vụ có khả năng chạm cùng source/API/dữ liệu. Mục tiêu: tránh sửa chồng chéo, hồi quy dây chuyền, vòng lặp code–sửa vô hạn và bảo đảm mỗi phòng nhận đúng kết quả cùng bằng chứng.

## Vai trò
- Các phòng ban: phân tích chuyên môn, gửi task, phụ thuộc, phạm vi dự kiến, tiêu chí nghiệm thu và báo cáo.
- CTRL (ChatGPT hiện tại): tổng hợp; kiểm tra baseline; lập bản đồ phụ thuộc/xung đột; sắp thứ tự; soạn gói thực thi; theo dõi checkpoint; phân phối kết quả.
- Claude Code: coder/executor dùng chung. Chỉ code theo một gói thực thi đã duyệt, không nhận chỉ thị code rời rạc từ nhiều phòng.
- QA và phòng chuyên môn: kiểm tra độc lập theo tiêu chí đã thống nhất.
- Chủ dự án: duyệt kế hoạch và thay đổi thuộc diện phải duyệt.

## Khi nào phải lập đợt tích hợp?
Bắt buộc khi:
1. Có từ hai task/phòng ban trở lên cần Claude code trong cùng giai đoạn.
2. Nhiệm vụ có thể sửa file, module, API, protocol, schema, cấu hình hoặc tài nguyên mà nhiệm vụ khác sử dụng.
3. Sửa lỗi có nguy cơ ảnh hưởng tính năng đã hoàn thành.
4. Có thay đổi nền tảng/chung như build, render, network, database hoặc gameplay core.
Task đơn lẻ, cô lập vẫn phải kiểm tra phạm vi và baseline; CTRL có thể dùng luồng task đơn nếu không có phụ thuộc đáng kể.

## Chu trình chuẩn

### 1. Thu thập đầu vào
CTRL thu thập từ tất cả phòng:
- Task ID, mục tiêu, mức ưu tiên, trạng thái và link TASK/REPORT/bằng chứng.
- File/module/API/dữ liệu dự kiến bị tác động (nếu đã biết).
- Phụ thuộc, giả định, ràng buộc và điều không được thay đổi.
- Tiêu chí nghiệm thu, test cần chạy và kết quả mong đợi.
- Mức độ khẩn cấp, rủi ro, blocker.

Không coi đề xuất chưa có bằng chứng là sự thật đã xác nhận. Phòng chưa báo cáo ghi CHƯA CÓ BÁO CÁO.

### 2. Kiểm tra baseline và tác động
Trước khi code, Claude/nguồn kỹ thuật chỉ đọc để kiểm tra:
- Branch, commit baseline, trạng thái working tree và thay đổi chưa commit.
- File/module liên quan, lịch sử thay đổi gần đây và test hiện có.
- Danh sách file dự kiến sửa, file dùng chung và giao diện liên quan.
- Tương thích ngược và vùng chức năng có nguy cơ hồi quy.

Không ghi đè thay đổi chưa commit của người dùng. Nếu working tree không sạch hoặc baseline không rõ, dừng và làm rõ; không tự reset, clean, checkout phá hủy hoặc stash thay đổi của người dùng.

### 3. Bản đồ phụ thuộc và xung đột
CTRL lập ma trận:
- Task nào đọc/ghi cùng file hoặc module?
- Task nào phụ thuộc API, dữ liệu, protocol hoặc kết quả task khác?
- Task nào có thể làm thay đổi hành vi đã được QA xác nhận?
- Task nào có thể tách biệt thực sự?
- Thứ tự nào giảm sửa lại và phạm vi hồi quy?

Phân loại:
- CONFLICT: cùng vùng code hoặc thay đổi có thể phủ định nhau — không chạy đồng thời.
- DEPENDENCY: task B cần kết quả task A — A phải hoàn tất/checkpoint trước B.
- SHARED CONTRACT: cùng phụ thuộc API/schema/protocol — thống nhất hợp đồng trước khi code.
- ISOLATED: không có vùng ghi chung đã xác định — vẫn thực thi tuần tự bởi một Claude Code.

### 4. Lập gói thực thi thống nhất
Mỗi đợt có mã INT-YYYYMMDD-01 và ghi:
- Baseline branch/commit.
- Task gốc và phòng nhận kết quả.
- Phạm vi in-scope/out-of-scope.
- Sơ đồ phụ thuộc, xung đột và thứ tự thực hiện.
- File/module dự kiến sửa theo từng bước.
- Hợp đồng API/schema/protocol cần giữ.
- Lệnh build/test, tiêu chí pass/fail.
- Rủi ro, rollback và điều kiện dừng.
- Cách ánh xạ commit/test/report về task từng phòng.

Không gom task chỉ vì cùng thời điểm. Chỉ gom khi có lợi ích tích hợp hoặc cần kiểm soát xung đột.

### 5. Duyệt trước khi code
CTRL trình chủ dự án bản tóm tắt dễ hiểu: sẽ sửa gì, vì sao, ảnh hưởng gì, test ra sao và rủi ro nào. Chỉ chuyển APPROVED khi đủ phê duyệt theo APPROVAL_RULES. Claude không code khi kế hoạch còn PROPOSED hoặc BLOCKED.

### 6. Thực thi có cô lập và checkpoint
- Claude dùng branch/worktree tích hợp riêng cho mỗi đợt, bắt đầu từ baseline đã ghi nhận; không code trực tiếp trên main.
- Một coder dùng chung, thực hiện tuần tự từng bước; không nhận task code chen ngang từ các phòng.
- Mỗi bước là thay đổi nhỏ, có commit/checkpoint riêng với mã INT và Task ID.
- Sau mỗi bước: xem diff, chạy test liên quan, ghi kết quả; chỉ đi tiếp khi checkpoint đạt tiêu chí.
- Không tự ý sửa ngoài phạm vi. Nếu cần mở rộng, dừng và báo CTRL để đánh giá/ xin duyệt.
- Không sửa đồng thời cùng file/module từ nhiều phiên Claude hoặc nhiều nhánh chưa tích hợp.

### 7. Kiểm thử tích hợp và hồi quy
Sau các bước:
1. Chạy unit/test mục tiêu cho từng task.
2. Chạy test tích hợp cho giao diện giữa các task.
3. Chạy regression cho luồng cũ có nguy cơ bị ảnh hưởng.
4. Build đúng cấu hình/môi trường mục tiêu nếu có thể.
5. QA độc lập xác nhận theo tiêu chí; ghi rõ test không chạy được.

Build thành công không đồng nghĩa toàn bộ chức năng đã đúng. Không tuyên bố DONE_VERIFIED nếu thiếu bằng chứng.

### 8. Báo cáo về từng phòng
CTRL tạo báo cáo tổng và bản tóm tắt riêng cho từng task/phòng:
- Task ID và kết quả thực tế.
- Commit/hash và file thay đổi.
- Test đã chạy, kết quả/log/bằng chứng.
- Ảnh hưởng phát hiện tới task/phòng khác.
- Phần chưa làm, sai khác so với yêu cầu, blocker.
- Trạng thái VERIFIED/PROBABLE/UNKNOWN/NOT TESTED.

Mỗi phòng chỉ nhận kết luận liên quan nhiệm vụ của mình; không báo hoàn thành nếu tiêu chí phòng đó chưa được kiểm chứng.

## Chống vòng lặp sửa lỗi
- Mỗi lỗi phải có mô tả tái hiện, điều kiện xảy ra, bằng chứng và tiêu chí xác nhận đã sửa.
- Tối đa 2 vòng sửa có kiểm soát cho cùng một lỗi trong cùng đợt. Một vòng gồm: xác định nguyên nhân → sửa → chạy test tái hiện → regression liên quan.
- Nếu sau 2 vòng vẫn lỗi, lỗi tái xuất hiện hoặc mỗi lần sửa tạo lỗi mới ở vùng khác: dừng, giữ checkpoint gần nhất còn tốt, chuyển BLOCKED và báo CTRL.
- Không lặp lại cùng cách sửa, không mở rộng phạm vi hoặc đổi kiến trúc để né lỗi khi chưa được duyệt.
- CTRL phân tích lại nguyên nhân, cập nhật kế hoạch hoặc tách task/đợt mới; chủ dự án duyệt nếu thay đổi vượt phạm vi ban đầu.

## Rollback và bảo vệ
- Ưu tiên revert đúng commit gây hồi quy hoặc sửa forward theo kế hoạch được duyệt; không rollback mù toàn bộ đợt.
- Trước rollback phải xác định commit, tác động phụ thuộc và dữ liệu có thể bị ảnh hưởng.
- Không chạy lệnh phá hủy, xóa dữ liệu, reset VM, thay đổi Main VM hoặc triển khai production khi chưa được duyệt.
- Nếu phát hiện lỗi sau checkpoint đã xác nhận, mở incident/task liên quan và báo CTRL; không tự sửa chồng lên task khác.

## Điều kiện đóng đợt
- Tất cả task được ánh xạ về kết quả rõ ràng.
- Diff/commit và bằng chứng test được lưu.
- QA và phòng liên quan đã nhận báo cáo.
- Task chưa đạt giữ BLOCKED/NOT_DONE/DEFERRED.
- CTRL cập nhật MASTER_TASK_BOARD, DECISION_LOG, BLOCKERS_AND_RISKS và DAILY_WORK_LOG.

## Mẫu tóm tắt đợt
- Batch ID:
- Baseline branch/commit:
- Task/phòng tham gia:
- Xung đột và phụ thuộc:
- Thứ tự thực thi:
- File/module có thể sửa:
- Ngoài phạm vi:
- Kế hoạch test:
- Số vòng sửa lỗi đã dùng:
- Checkpoint/commit:
- Kết quả theo từng task:
- Rủi ro còn lại/rollback:
- Phê duyệt:
