# Kiến trúc Autonomous QA – JX1 (từ Phase 47, 2026-11-12)

## Vai trò
| Vai trò | Model | Trách nhiệm |
|---|---|---|
| QA Lead + Autonomous Game Explorer | Sonnet | Tự vận hành game trên LDPlayer, tự lập kế hoạch, đo, ghi knowledge/thí nghiệm, gửi báo cáo kỹ thuật cho Opus rồi TIẾP TỤC khám phá |
| Developer + Technical Reviewer | Opus | Phân tích code/nguyên nhân, đánh giá báo cáo QA, đề xuất sửa, sửa sau khi chủ máy duyệt, build, giao bản build cho QA xác minh |
| Execution Orchestrator | Claude Code (phiên chính) | Khởi chạy/resume các agent, giữ quyền cài APK, quản lý GitHub, bảo vệ dữ liệu |
| Trợ lý tùy chọn | Haiku | Việc lặp lại đơn giản khi Sonnet giao; không phải điều kiện để QA chạy |

## Sự thật về cơ chế (đã kiểm tra trong phiên Phase 46-47)
- Sonnet/Haiku chạy dưới dạng subagent của Claude Code. Mỗi subagent có cùng bộ công cụ (PowerShell -> ADB, Read ảnh, ghi file) nên **tự thao tác LDPlayer được** (Haiku đã thao tác thật ở Phase 46; Sonnet được giao quyền thao tác từ Phase 47 – kết quả kiểm tra năng lực ghi trong TEST_RESULTS/47-autonomous-qa-log.md).
- Vì sao Haiku "đứng chờ Opus" ở Phase 46: (1) mỗi lần giao là một nhiệm vụ hữu hạn, agent chạy xong thì trả báo cáo và dừng tới khi được gọi lại (cơ chế subagent, không có vòng lặp vô hạn); (2) prompt do Opus viết có điểm dừng bắt buộc ("dừng và báo cáo", "tối đa ~60 thao tác", "dừng khi HP < 40%") và yêu cầu hỏi khi gặp quyết định; (3) không có nguồn tri thức dùng chung nên mỗi lần kẹt UI phải chờ Opus tra mã nguồn.
- Giới hạn còn lại (không thể vượt bằng cấu hình): một subagent không chạy mãi; nó kết thúc khi hoàn tất kế hoạch hoặc hết ngữ cảnh. Claude Code phải resume hoặc khởi chạy lại. Tin nhắn giữa agent chỉ được đọc ở lượt công cụ kế tiếp của bên nhận. Một thiết bị LDPlayer chỉ nên do MỘT agent điều khiển tại một thời điểm.

## Quy trình
1. Sonnet nhận nhiệm vụ dài hạn (không phải từng bước): mục tiêu, phạm vi an toàn, công cụ, tri thức sẵn có.
2. Vòng OBSERVE → UNDERSTAND → PLAN → ACT → VERIFY → RECORD → CONTINUE; ghi nhật ký liên tục vào TEST_RESULTS/<phase>-autonomous-qa-log.md.
3. Khi có bằng chứng lỗi/xác minh: gửi báo cáo ngắn cho Opus (SendMessage "main") rồi tiếp tục, không chờ.
4. Opus phân tích, đề xuất sửa -> chủ máy duyệt -> Opus sửa/build -> Claude Code cài APK (báo trước cho Sonnet) -> Sonnet ưu tiên xác minh -> quay lại khám phá.
5. Tri thức: knowledge/ (Markdown, trạng thái VERIFIED/DISCOVERED/NOT_TESTED/UNKNOWN/BLOCKED) + experiments/ (CSV/JSON số liệu thô, mã thí nghiệm, epoch, build, server).

## An toàn
Chỉ VM thử + nhân vật thử; không Main VM; không mục GM nguy hiểm (Admin, ReloadScript, Quản lý Server, Reset, SetFightState, Hủy/Dọn hành trang); không cài APK/sửa source/commit (Opus/Claude Code làm); không ghi IP/mật khẩu/tài khoản; không PASS khi chỉ có toast/ảnh không chứng minh; LDPlayer ≠ điện thoại thật.
