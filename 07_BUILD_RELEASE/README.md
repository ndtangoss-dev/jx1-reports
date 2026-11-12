# 07_BUILD_RELEASE — Build & Release

**Mã:** REL  
**AI chính:** ChatGPT Release  
**Executor dùng chung:** Claude Code (chỉ khi task rõ ràng được duyệt).

## Chức năng
Toolchain, build Android/Windows, APK/package, versioning, release checklist và bàn giao artifact.

## Giới hạn
Không tự cài tool, thay SDK/NDK/JDK, ký release, phát hành hoặc cài lên môi trường thật nếu chưa duyệt. Không đưa APK/binary vào repo báo cáo; giữ log và phương án rollback.

## Hồ sơ
- `CHAT_START_HERE.md`: nội dung khởi tạo cửa sổ chat.
- `TASKS/`: nhiệm vụ đã duyệt.
- `REPORTS/`: báo cáo kết quả.
- `HISTORY/`: lịch sử.
- `REFERENCES/`: tài liệu tham khảo.

Mỗi task có mã REL-NNN, một Primary Owner. Gửi đề xuất qua CTRL; không tự giao Claude hoặc phòng khác. Trạng thái phải rõ: VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
