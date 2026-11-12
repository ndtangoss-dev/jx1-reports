# PROJECT_CHARTER

## Mục tiêu
Phát triển JX1 Cocos V3 ổn định, mượt nhưng nhẹ, giữ tinh thần JX1; định hướng thế giới trực tuyến có BOT tồn tại lâu dài, xử lý chủ yếu phía server và tương tác như người chơi. Mọi thay đổi lớn về gameplay/kiến trúc do chủ dự án duyệt.

## Vai trò
- Chủ dự án: mục tiêu, ưu tiên, quyết định và phê duyệt.
- ChatGPT CTRL: phân loại, giao việc, theo dõi, kiểm tra hồ sơ, tổng hợp nhật ký.
- Claude Code: executor kỹ thuật chính, đọc source, sửa code, build/test theo task đã duyệt.
- ChatGPT chuyên môn: nghiên cứu, phản biện, thiết kế và đánh giá trong phạm vi phòng.

## Nguyên tắc
1. Một task có một phòng chủ trì; không có hai executor sửa cùng vùng source đồng thời.
2. Phân biệt nghiên cứu/đề xuất/đã duyệt/đang làm/đã kiểm chứng.
3. Mọi kết luận quan trọng có bằng chứng hoặc nhãn VERIFIED/PROBABLE/UNKNOWN/BLOCKED/NOT TESTED.
4. Thay đổi nhỏ, có baseline, diff, test và rollback.
5. Không sửa Main VM `JX-Server-D`; không tự ý tác động Archive VM; Test VM `JX-Test-36` chỉ dùng khi được duyệt.
6. Bảo vệ Fix31, Fix34, Fix36, P47. Phase48 đã đóng; không điều tra lại session-drop đã được xác nhận là thao tác chủ động.
7. Sonnet exploration OFF, bug QA ON theo trạng thái đã ghi nhận; không tự bật exploration.
8. Không đưa token, mật khẩu, IP riêng, thông tin tài khoản, giá trị accinfo/accpint hoặc dữ liệu nhạy cảm lên GitHub.

Repo hồ sơ: `ndtangoss-dev/jx1-reports`. Không đưa source, APK, binary, asset game hoặc dữ liệu người chơi vào repo này.
