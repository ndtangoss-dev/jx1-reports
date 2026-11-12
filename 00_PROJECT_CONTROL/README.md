# 00_PROJECT_CONTROL — Bàn làm việc điều phối JX1

Đây là khu vực của ChatGPT điều phối tổng thể, không chứa source/binary/asset/dữ liệu người chơi.

- [PROJECT_CHARTER](PROJECT_CHARTER.md): mục tiêu và nguyên tắc.
- [TEAM_ROLES](TEAM_ROLES.md): phòng ban và AI phụ trách.
- [WORKFLOW](WORKFLOW.md): nhận việc, giao việc, bàn giao.
- [INTEGRATION_PLAN](INTEGRATION_PLAN.md): tổng hợp task, phân tích phụ thuộc/xung đột và lập đợt code/test thống nhất cho Claude.
- [APPROVAL_RULES](APPROVAL_RULES.md): quyền hạn và việc cần duyệt.
- [MASTER_TASK_BOARD](MASTER_TASK_BOARD.md): bảng nhiệm vụ.
- [DECISION_LOG](DECISION_LOG.md): quyết định đã duyệt.
- [BLOCKERS_AND_RISKS](BLOCKERS_AND_RISKS.md): việc tắc/rủi ro.
- [CHAT_WINDOWS_SETUP](CHAT_WINDOWS_SETUP.md): tạo các chat phòng ban.
- [DAILY_WORK_LOG](DAILY_WORK_LOG/README.md): nhật ký từng ngày.

Mọi yêu cầu của chủ dự án được CTRL phân loại; chủ dự án không phải tự chọn phòng ban. GitHub là hồ sơ chung. Không có báo cáo/bằng chứng thì không tự ghi nhận hoàn thành.

## Nguyên tắc điều phối code
Claude Code là coder dùng chung, không nhận chỉ thị code độc lập từ nhiều phòng. CTRL tổng hợp yêu cầu liên quan thành gói thực thi tích hợp đã duyệt, tổ chức code tuần tự theo checkpoint, kiểm thử hồi quy và trả kết quả về từng phòng.
