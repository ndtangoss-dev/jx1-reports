# Yêu cầu bắt buộc của chủ dự án – 2026-11-16 (nguyên văn)

BỔ SUNG YÊU CẦU BẮT BUỘC: BÀN GIAO VÀ THAY THẾ PROJECT MANAGER / AI MODEL

Tôi có thể hết hạn mức tài khoản Claude hiện tại và chuyển sang tài khoản Claude cũ. Opus hiện tại cũng có thể hết quota, không còn khả dụng hoặc được thay bằng một Opus khác, Sonnet, Codex hay AI khác.

Vì vậy, dự án phải được thiết kế để thay thế Project Manager và AI worker bất cứ lúc nào mà không mất tiến độ, kiến thức hoặc phải làm lại từ đầu.

Các yêu cầu:

1. Bộ nhớ dự án độc lập với tài khoản và cuộc trò chuyện:

- Mọi thông tin quan trọng phải được lưu trong các file của dự án và GitHub.
- Không phụ thuộc vào Memory của ChatGPT, Claude hay lịch sử chat của bất kỳ tài khoản nào.
- AI kế nhiệm phải có thể tiếp quản chỉ bằng cách truy cập repository và tài liệu bàn giao.

2. Opus phải lưu lại liên tục:

- Mục tiêu và định hướng dự án.
- Các quyết định đã chốt và lý do.
- Kiến trúc và trạng thái thực tế của hệ thống.
- Công việc đã hoàn thành, kết quả kiểm thử và bằng chứng.
- Lỗi đã gặp, cách xử lý và lỗi chưa giải quyết.
- Công việc đang thực hiện, tiến độ hiện tại và bước tiếp theo.
- Những điều tuyệt đối không được thay đổi hoặc làm lại tùy tiện.
- Các thông tin còn thiếu cần chủ dự án quyết định.

3. Bàn giao khi thay Project Manager:

- Opus cũ phải tạo bản bàn giao đầy đủ trước khi hết hạn mức nếu có thể dự đoán.
- AI mới phải đọc Master Prompt, quy định vận hành, Project Memory, quyết định, trạng thái task, báo cáo gần nhất và hồ sơ bàn giao.
- AI mới phải tự kiểm tra repository, môi trường và kết quả thực tế để xác nhận nội dung bàn giao.
- Sau đó tiếp tục đúng công việc còn dang dở, không tự ý thay đổi định hướng và không bắt chủ dự án kể lại từ đầu.

4. Bàn giao khi bị ngắt đột ngột:

- Phải có cơ chế lưu trạng thái thường xuyên, không chỉ lưu vào cuối ngày.
- Mọi công việc đang làm phải có trạng thái đủ để AI khác tiếp tục.
- Nếu chưa có bản bàn giao cuối cùng, AI mới phải phục hồi từ lần lưu trạng thái gần nhất và kiểm tra lại những thay đổi chưa được xác nhận.

5. Thay đổi tài khoản hoặc nhà cung cấp:

- Việc chuyển từ tài khoản Claude hiện tại sang tài khoản Claude cũ không được làm mất dữ liệu dự án.
- Không phụ thuộc vào một model hoặc một nhà cung cấp duy nhất.
- Có bảng phân công và quy trình để AI mới tiếp quản vai trò Project Manager.
- AI kế nhiệm phải được hướng dẫn sử dụng công cụ và môi trường hiện có trước khi thực hiện công việc.

6. Không tạo thủ tục thừa:

- Không yêu cầu Opus viết báo cáo riêng sau mỗi thao tác.
- Tự động cập nhật trạng thái và lưu bằng chứng cần thiết.
- Chỉ tạo một bộ hồ sơ bàn giao có cấu trúc, dễ đọc, đủ để AI mới tiếp tục.
- Chủ dự án chỉ nhận thông báo khi cần quyết định hoặc khi bàn giao đã sẵn sàng.

Đây là yêu cầu bắt buộc của kiến trúc vận hành dự án, không phải đề xuất tùy chọn.

Hãy tích hợp vào tài liệu v0.3 và bảo đảm Opus kế nhiệm có thể tiếp tục công việc của Opus tiền nhiệm mà không cần chủ dự án giải thích lại.
