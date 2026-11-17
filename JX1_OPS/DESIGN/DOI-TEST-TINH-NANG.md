# Đội test tính năng game (chủ giao 18/11 00:3x)

Mục tiêu: chạy nhiều vòng test, mỗi vòng thu số liệu thật (trang bị có dòng thuộc tính nào, mặc vào chỉ số nhân vật đổi ra sao, vũ khí đổi gì, sát thương lên quái đổi ra sao) để hiểu game bằng số đo, không chỉ bằng đọc mã.

## Cơ cấu
- Tổng quản (dispatcher) giao việc, thu kết quả, báo qua `STATE/TRANG-THAI.md` và hòm thư. Mỗi vòng = một task nhỏ <= 30 phút, độc lập.
- Quản lý (Sonnet) nhận bảng số, đối chiếu "dự đoán từ dữ liệu" với "đo thật", ghi chênh lệch, đẩy vào MUC-LUC-TRI-THUC.
- Bốn tầng, làm theo thứ tự:
  1. **T-01 Dự đoán từ dữ liệu (chỉ đọc, chạy ngay):** từ bảng trang bị/magic/kỹ năng + Lua tính ra: mỗi món có dòng thuộc tính nào (tên đã giải mã TCVN3), giá trị theo cấp/dòng, công thức sát thương (Core `KNpc`/`KItem`). Ra `REPORTS/T-01-*.md` + `TEST/DU-DOAN/<mon>.tsv`.
  2. **T-02 Khung đo (cần VM thử):** trên JX-Test-36 tạo nhân vật test, cấp trang bị bằng Lua/GM, mặc, đọc chỉ số trước/sau (log Lua hoặc gói đồng bộ qua Bot). Cần chủ duyệt tạo tài khoản/nhân vật test (Q-18/Q-19 cho chuỗi server, chưa cho DB).
  3. **T-03 Vòng đo trang bị:** mỗi vòng 1 nhóm (bộ An Bang, vũ khí 5 hệ, phi phong...). Ra bảng: dòng thuộc tính hiển thị | chỉ số nhân vật trước | sau | chênh lệch | khớp dự đoán?
  4. **T-04 Vòng đo sát thương:** nhân vật đánh quái mẫu (heo trắng Ba Lăng Huyện...), ghi sát thương nhiều lần/đổi vũ khí/ngũ hành, tính trung bình, so công thức.
- Mỗi vòng tăng độ phủ; bảng chênh lệch giữa dự đoán và đo là nguồn phát hiện hiểu sai.

## An toàn
Chỉ chạy trên VM thử; không đụng Main VM trừ Q-18; DB test cô lập, có ghi chú hoàn tác; không đưa tài khoản thật vào báo cáo; không push; mỗi task báo theo `DESIGN/CHUAN-BAO-CAO.md`.

## Tình trạng
T-01 sẵn sàng giao. T-02..T-04 chờ T-01 và duyệt tài khoản test. Công cụ có sẵn: client không giao diện `BOT/` (đăng nhập, worldsync; chưa đủ gói vào thế giới thật, xem E-01b).
