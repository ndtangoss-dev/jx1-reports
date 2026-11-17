---
name: jx1-parameters
description: Ghi sổ thông số trong báo cáo khảo sát JX1 với giá trị, đơn vị, nguồn và mức đổi an toàn; không sửa cấu hình hoặc mã game.
---
# Ghi sổ thông số JX1
Thêm vào đúng báo cáo task, không tự tạo sổ/file khác:
## MUC SO THONG SO
| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn (CÓ/CẨN THẬN/KHÔNG) | Nguồn đo |
|---|---|---|---|---|---|---|---|
- Chỉ ghi thông số liên quan; kiểm file thật/dòng hiện tại mà map/tóm tắt dẫn tới.
  Thiếu file/quyền thì ghi nguồn gián tiếp, CHUA XAC MINH, không đoán.
- Tách mặc định source/cấu hình/dữ liệu mẫu/số đo runtime. Nguồn đo ghi đọc tĩnh hoặc
  lệnh/điều kiện đo thực chạy; chưa đo ghi chưa đo, không dùng 0 thay dữ liệu thiếu.
- Giữ đơn vị/phạm vi/version; suy đổi ghi công thức và giả định (tick sang giây…).
- CÓ cần bằng chứng giới hạn và kiểm an toàn; chưa đủ dùng CẨN THẬN.
  Đánh giá không cấp quyền sửa/chạy; không ghi khóa/mật khẩu/truy cập nội bộ.
