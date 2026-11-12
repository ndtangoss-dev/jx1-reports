# 04_SERVER_BACKEND — Server & Backend

**Mã:** SRV  
**AI chính:** ChatGPT Server  
**Executor dùng chung:** Claude Code (chỉ khi task rõ ràng được duyệt).

## Chức năng
Server processes, protocol, database, network, persistence, concurrency, BOT server-side, scaling và deployment design.

## Giới hạn
Không đổi protocol/schema/DB/config/firewall/licensing hoặc triển khai nếu chưa duyệt. Không test tải trên Main VM. Không giả định mỗi BOT là một client connection. Phân biệt số đo thật với giả định.

## Hồ sơ
- `CHAT_START_HERE.md`: nội dung khởi tạo cửa sổ chat.
- `TASKS/`: nhiệm vụ đã duyệt.
- `REPORTS/`: báo cáo kết quả.
- `HISTORY/`: lịch sử.
- `REFERENCES/`: tài liệu tham khảo.

Mỗi task có mã SRV-NNN, một Primary Owner. Gửi đề xuất qua CTRL; không tự giao Claude hoặc phòng khác. Trạng thái phải rõ: VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
