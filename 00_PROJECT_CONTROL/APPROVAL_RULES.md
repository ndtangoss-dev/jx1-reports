# APPROVAL_RULES — Quyền hạn

## Có thể làm trong phạm vi nghiên cứu
Đọc tài liệu/source chỉ-đọc; phân tích; lập sơ đồ; viết test plan; review diff; báo cáo trong đúng thư mục, không chứa bí mật.

## Cần chủ dự án duyệt trước
Sửa source; đổi gameplay/protocol/schema/DB; build/cài APK hoặc triển khai có ảnh hưởng môi trường; thay config mạng/firewall/tài khoản/licensing; xóa/di chuyển/ghi đè dữ liệu; migration/reset/VM; cài tool; ký/phát hành; kiểm thử tải hoặc bảo mật có tác động; thay đổi thiết kế sản phẩm.

## Khu vực bảo vệ
- Main VM `JX-Server-D`: tuyệt đối không sửa, reboot, reset, cài đặt hay thử nghiệm.
- Archive VM: không chạy đồng thời Main VM.
- Test VM `JX-Test-36`: chỉ dùng khi được duyệt.
- Fix31/Fix34/Fix36/P47: không tự ý sửa hoặc hồi quy.
- Phase48: đã đóng.

Khi chưa rõ, dừng trước thao tác rủi ro; nêu việc định làm, ảnh hưởng, backup/rollback và chờ phê duyệt. Im lặng không phải đồng ý.
