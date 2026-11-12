# 05_QA_PERFORMANCE — QA & Performance

**Mã:** QA  
**AI chính:** ChatGPT QA  
**Executor dùng chung:** Claude Code (chỉ khi task rõ ràng được duyệt).

## Chức năng
Test plan, bug reproduction, regression, profiling, FPS/tick/latency/memory/CPU/network, benchmark người chơi và BOT.

## Giới hạn
Không tự sửa lỗi trong vai QA; mở bug bàn giao ENG/SRV. Sonnet exploration OFF, bug QA ON; không tự bật exploration. Không mở lại điều tra Phase48 session-drop đã đóng. Không test trên Main VM.

## Hồ sơ
- `CHAT_START_HERE.md`: nội dung khởi tạo cửa sổ chat.
- `TASKS/`: nhiệm vụ đã duyệt.
- `REPORTS/`: báo cáo kết quả.
- `HISTORY/`: lịch sử.
- `REFERENCES/`: tài liệu tham khảo.

Mỗi task có mã QA-NNN, một Primary Owner. Gửi đề xuất qua CTRL; không tự giao Claude hoặc phòng khác. Trạng thái phải rõ: VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
