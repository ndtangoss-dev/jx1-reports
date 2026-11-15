# CODEX DIRECT CLI — QUY TẮC THỰC THI JX1 (BẢN CHUẨN)

Ngày áp dụng: 15/11/2026  
Phạm vi: mọi nhiệm vụ JX1 được giao trực tiếp cho Codex CLI.  
Ưu tiên hiện hành: **Direct CLI do người dùng kích hoạt**. Không dùng Dispatcher cho quy trình này.

## 1. Nguyên tắc cốt lõi

Codex được giao **kết quả cần đạt**, không được yêu cầu tự dựng lại quy trình khám phá dự án. Làm trực tiếp trên dữ liệu đã biết; chỉ kiểm tra bổ sung khi có bằng chứng về thiếu hụt, xung đột hoặc lỗi.

Thứ tự ưu tiên:
1. Hoàn thành mục tiêu trong phạm vi.
2. Giữ an toàn source, dữ liệu và server.
3. Kiểm chứng các kết luận quan trọng bằng bằng chứng tối thiểu đủ tin cậy.
4. Báo cáo và bàn giao.
5. Tiết kiệm token, lệnh và thời gian; không tạo hoạt động chỉ để thể hiện tiến độ.

## 2. Khởi động một lần — không lặp

Khi người dùng kích hoạt task:
1. Đọc **prompt đã ghim đúng commit** một lần.
2. Dùng working directory đã được chỉ định. Kiểm tra branch và `git status --short` đúng một lần trước khi ghi file.
3. Nếu phiên/model/provider đã được người dùng xác nhận trong phiên hiện tại, **không chạy lại preflight, /status, kiểm tra config hoặc CLI help**.
4. Không đọc toàn bộ workflow, toàn bộ `00_LATEST_STATUS.md`, toàn bộ lịch sử hay toàn bộ thư mục báo cáo. Chỉ đọc đúng tài liệu mà prompt chỉ định và thực sự cần.
5. Không fetch lại prompt, status, remote, refs hoặc file đã đọc thành công, trừ khi nội dung bị mất khỏi ngữ cảnh, có lỗi truy cập, hoặc cần xác minh SHA trước khi công bố.

Nếu task được resume trong cùng session và còn session ID/kết quả trước đó: tiếp tục từ checkpoint gần nhất. **Không chạy lại prompt từ đầu.** Chỉ khi không thể phục hồi ngữ cảnh mới đọc prompt và báo cáo dở dang một lần để tiếp tục; không tái thực hiện phần đã có bằng chứng.

## 3. Làm việc theo phạm vi — không khám phá vô hạn

- Prompt phải chỉ rõ mục tiêu, đường dẫn nguồn đã biết, file đầu ra, quyền được phép và điều kiện nghiệm thu.
- Ưu tiên đọc trực tiếp các file đã chỉ định. Không tìm kiếm đệ quy toàn repo nếu không cần.
- Không lập inventory, không kiểm tra môi trường/build tools, không xem Git remote, không chạy test tổng thể nếu nhiệm vụ không yêu cầu.
- Không tạo parser/script phụ hoặc báo cáo trung gian nếu một lệnh trích xuất/đối chiếu trực tiếp đáp ứng được mục tiêu.
- Gộp lệnh có liên quan; tránh gọi nhiều lệnh nhỏ lặp cùng một việc.
- Không gửi cập nhật tiến độ cho từng thao tác. Chỉ báo khi có kết quả có ý nghĩa, blocker hoặc hoàn tất.
- Không mở rộng phạm vi để theo đuổi độ bao phủ tuyệt đối. Nội dung ngoài phạm vi ghi là chưa kiểm tra.

## 4. Giới hạn và điều kiện kết thúc

Mỗi prompt phải có ngân sách công việc phù hợp:
- Task nhỏ: mục tiêu 10–15 phút.
- Audit vừa/lớn: mục tiêu 30–45 phút.
- Nếu vượt ngân sách hoặc bị lặp thao tác: dừng khám phá, chốt kết quả đã có và hoàn thành báo cáo một phần có cấu trúc.
- Đây là ngưỡng điều hành; không được hy sinh kiểm chứng thiết yếu hoặc bịa kết quả để đạt thời gian.

Khi không thể xác minh:
- Ghi **CHƯA XÁC MINH** và lý do cụ thể.
- Nêu bằng chứng hiện có và bước tối thiểu cần thiết để xác minh sau.
- Chuyển sang mục tiếp theo; không tiếp tục tìm kiếm vô hạn.

Mọi task phải kết thúc bằng một trong các trạng thái:
- `DONE`: mục tiêu trong phạm vi đạt và có bằng chứng.
- `PARTIAL`: đã có kết quả hữu ích nhưng còn mục chưa xác minh.
- `BLOCKED`: không thể tiếp tục do quyền, môi trường hoặc phụ thuộc.
- `FAILED`: đã thử nhưng thao tác/mục tiêu thất bại.

Không được để task chạy mãi ở trạng thái chuẩn bị/kiểm tra.

## 5. Kiểm chứng vừa đủ

- Kiểm chứng trực tiếp các kết luận ảnh hưởng đến quyết định kỹ thuật.
- Với code: nêu file, symbol và line/range cụ thể.
- Với enum: tính numeric ID thật, xét explicit/implicit assignment và điều kiện compile.
- Với packet: so sánh đúng struct/serialization liên quan; không suy diễn runtime từ source.
- Chạy test chỉ khi task yêu cầu và môi trường sẵn sàng; không build hoặc kết nối server trong task read-only.
- Không kiểm tra lại cùng kết quả nhiều lần nếu không có mâu thuẫn.
- Phân biệt rõ `ĐÃ XÁC MINH`, `CHƯA KIỂM THỬ`, `CHƯA XÁC MINH`, `GIẢ THUYẾT`, `BỊ CHẶN`.

## 6. Báo cáo và GitHub — một lần bàn giao

- Tạo **một báo cáo cuối cùng** tại đúng đường dẫn trong prompt; không tạo nhiều báo cáo tiến độ.
- Báo cáo ngắn, tập trung vào: kết luận, bằng chứng, phần chưa xác minh, rủi ro và bước tiếp theo.
- Chỉ liệt kê file đã đọc/thay đổi có liên quan; không in nhật ký mọi lệnh nếu không giúp kiểm chứng.
- Với task read-only, không sửa source; chỉ tạo file báo cáo được cho phép.
- Trước khi commit: kiểm tra diff và status đúng một lần; chỉ stage/commit file thuộc task.
- Push đúng repository/branch khi có quyền. Nếu không có remote/credential/quyền, ghi rõ **BỊ CHẶN – CHƯA PUSH**, giữ báo cáo local và cung cấp đường dẫn. Không thử sửa credential hoặc cấu hình để vượt lỗi.
- Không tuyên bố push/commit nếu chưa có SHA và URL xác nhận.

## 7. An toàn và quyền hạn

Được tự thực hiện trong phạm vi đã duyệt: đọc source, phân tích, chạy lệnh không phá hủy, tạo báo cáo, test/build trên môi trường thử nghiệm nếu prompt cho phép.

Phải hỏi người dùng trước: tác động Main VM/production, xóa hoặc ghi đè dữ liệu không thể khôi phục, thay đổi kiến trúc lớn, quyền truy cập/credential, hoặc hành động có thể gián đoạn dịch vụ.

Luôn giữ nguyên:
- Cocos client canonical không được sửa nếu chưa duyệt.
- Main VM/server production không được chạm tới nếu chưa duyệt.
- Không reset/clean/checkout phá hủy thay đổi local của người dùng.
- Không đưa secret, mật khẩu, token hoặc dữ liệu truy cập vào báo cáo/GitHub.
- Không bypass sandbox hoặc approval policy.

## 8. Mẫu bàn giao bắt buộc (ngắn)

1. Task ID và trạng thái cuối (`DONE/PARTIAL/BLOCKED/FAILED`).
2. 3–7 phát hiện quan trọng nhất, kèm file/symbol/line.
3. File đã tạo/thay đổi.
4. Kiểm chứng/test đã chạy và kết quả; ghi rõ phần không chạy.
5. Phần chưa xác minh và blocker.
6. Commit SHA + link báo cáo, hoặc lý do chưa push.

## 9. Quy định hết hiệu lực / không áp dụng cho Direct CLI

Đối với quy trình Direct CLI hiện hành, **không áp dụng** các yêu cầu cũ sau:
- Polling `PROMPTS/DISPATCH_QUEUE.json`, Task Scheduler hoặc Dispatcher.
- Chạy preflight trước mọi task dù phiên đã được xác nhận.
- Đọc toàn bộ `WORKFLOW_JX1.md`, `00_LATEST_STATUS.md` và toàn bộ tài liệu tham chiếu ở mỗi lần chạy.
- Kiểm tra lặp model/provider/config, CLI help, remote, refs và workspace.
- Tạo báo cáo trung gian hoặc cập nhật tiến độ cho từng thao tác.
- Resume bằng cách chạy lại prompt từ đầu.

Các yêu cầu an toàn, phê duyệt, bảo vệ Main VM/source canonical, bằng chứng và báo cáo cuối vẫn có hiệu lực.

## 10. Xung đột tài liệu

Tài liệu này là chuẩn thực thi Codex Direct CLI mới nhất. Nếu tài liệu cũ mô tả Dispatcher/Claude hoặc quy trình kiểm tra dài hơn, áp dụng tài liệu này cho Direct CLI JX1. Prompt riêng của task chỉ được ghi đè quy tắc này khi người dùng phê duyệt rõ ràng và prompt nêu cụ thể phần thay đổi.
