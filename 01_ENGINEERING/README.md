# 01_ENGINEERING — Engineering

**Mã:** ENG  
**AI chính:** Claude Code  
**Executor dùng chung:** Claude Code (chỉ khi task rõ ràng được duyệt).

## Chức năng
Phòng chịu trách nhiệm source client/server C/C++, sửa lỗi, tối ưu, refactor và tích hợp. ChatGPT ENG phân tích, review và đề xuất.

## Giới hạn
Đọc source chỉ-đọc khi chưa có task sửa. Chỉ sửa đúng phạm vi task đã duyệt; tạo diff/backup, chạy test, nêu rollback. Không tự đổi gameplay/protocol/schema hoặc triển khai. Không commit source main nếu chưa được chỉ thị. Bảo vệ Fix31/Fix34/Fix36/P47; không chạm Main VM.

## Hồ sơ
- `CHAT_START_HERE.md`: nội dung khởi tạo cửa sổ chat.
- `TASKS/`: nhiệm vụ đã duyệt.
- `REPORTS/`: báo cáo kết quả.
- `HISTORY/`: lịch sử.
- `REFERENCES/`: tài liệu tham khảo.

Mỗi task có mã ENG-NNN, một Primary Owner. Gửi đề xuất qua CTRL; không tự giao Claude hoặc phòng khác. Trạng thái phải rõ: VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
