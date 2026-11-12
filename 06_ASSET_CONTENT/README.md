# 06_ASSET_CONTENT — Asset & Content

**Mã:** AST  
**AI chính:** ChatGPT Asset  
**Executor dùng chung:** Claude Code (chỉ khi task rõ ràng được duyệt).

## Chức năng
Kiểm kê/coverage tài nguyên; PAK/SPR, map, texture, animation, UI, font, audio, resource naming và nội dung game.

## Giới hạn
Mặc định chỉ đọc/kiểm kê. Không giải nén/chuyển đổi/chỉnh sửa/thay asset nếu chưa duyệt. Không đưa asset/binary/dữ liệu thô lên repo. Hash chưa tìm thấy không đồng nghĩa asset thiếu.

## Hồ sơ
- `CHAT_START_HERE.md`: nội dung khởi tạo cửa sổ chat.
- `TASKS/`: nhiệm vụ đã duyệt.
- `REPORTS/`: báo cáo kết quả.
- `HISTORY/`: lịch sử.
- `REFERENCES/`: tài liệu tham khảo.

Mỗi task có mã AST-NNN, một Primary Owner. Gửi đề xuất qua CTRL; không tự giao Claude hoặc phòng khác. Trạng thái phải rõ: VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
