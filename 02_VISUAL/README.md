# 02_VISUAL — Visual Quality

**Mã:** VIS  
**AI chính:** ChatGPT Visual  
**Executor dùng chung:** Claude Code (chỉ khi task rõ ràng được duyệt).

## Chức năng
Render 2D, PAK/SPR pipeline, camera, animation, UI, effects, map rendering, font, hình ảnh, FPS/frametime và chi phí GPU/memory.

## Giới hạn
Chỉ nghiên cứu/review/đề xuất. Không sửa source/asset/APK, không cài tool. Claude Code chỉ đọc source hoặc đo theo task được duyệt. Mỗi thử nghiệm có ID, baseline, điều kiện và kết quả. Bảo vệ Fix31/Fix34/Fix36/P47. Tiếp tục workspace hiện hữu JX1_VISUAL, không nhân đôi báo cáo V001.

## Hồ sơ
- `CHAT_START_HERE.md`: nội dung khởi tạo cửa sổ chat.
- `TASKS/`: nhiệm vụ đã duyệt.
- `REPORTS/`: báo cáo kết quả.
- `HISTORY/`: lịch sử.
- `REFERENCES/`: tài liệu tham khảo.

Mỗi task có mã VIS-NNN, một Primary Owner. Gửi đề xuất qua CTRL; không tự giao Claude hoặc phòng khác. Trạng thái phải rõ: VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
