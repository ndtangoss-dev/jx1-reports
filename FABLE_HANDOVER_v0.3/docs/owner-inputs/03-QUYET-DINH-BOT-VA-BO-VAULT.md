# Quyết định của chủ dự án – 2026-11-16 (nguyên văn)

Cập nhật bộ tài liệu JX1 v0.2 theo các quyết định đã chốt:

1. Bỏ toàn bộ yêu cầu Secret Vault và các nội dung triển khai bảo mật phức tạp. Không tiếp tục dành thời gian cho phần này.

2. Làm rõ quy tắc thế giới Bot:

- Bot là thực thể chung, tồn tại trong một thế giới dùng chung.
- Tất cả người chơi đều nhìn thấy và tương tác với cùng một Bot.
- Nếu người chơi A giết Bot thì Bot phải chết đối với người chơi B và tất cả người chơi khác.
- Trạng thái, vị trí, sinh tử và hoạt động của Bot phải được đồng bộ thống nhất, không tạo bản sao Bot riêng cho từng người.
- Người chơi thật không nhìn thấy nhau ở bản đồ thông thường, nhưng điều đó tuyệt đối không có nghĩa là thế giới Bot bị tách riêng.

Đây là quyết định đã chốt, không phải câu hỏi mở. Không đưa nội dung này vào danh sách câu hỏi để Opus hỏi lại.

Giữ nguyên các nội dung khác của v0.2. Chỉ cập nhật những tài liệu liên quan, xuất ZIP v0.3 và báo cáo ngắn các thay đổi. Chưa bàn giao Opus và chưa triển khai source.
