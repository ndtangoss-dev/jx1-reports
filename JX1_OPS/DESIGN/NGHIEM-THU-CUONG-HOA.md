# DANH SÁCH NGHIỆM THU CHO CHỦ — Cường hóa / Tài phú / Phi phong (B soạn 20/11, #B-038)
Môi trường: Test-36 (192.168.56.150), tài khoản test riêng; KHÔNG Server D. Đánh dấu ☐ → ✔ khi xong. Giá trị mong đợi lấy từ `DESIGN/BANG-CUONG-HOA-BAO-CAO.md`. Tất cả mục là KỲ VỌNG theo đọc mã, chưa chạy.

## A. Cường hóa +1..+15
1. ☐ Mở cửa sổ cường hóa: đủ 10 ô (mũ, áo, đai, vũ khí, giày, tay, dây chuyền?, nhẫn 1, nhẫn 2, phi... theo `QH_PARTS` 0..9); ô trống báo "ô không hợp lệ".
2. ☐ +1 → +2 → ...: giá hiển thị = bảng (thủy tinh mỗi loại 1,2,4..512, từ +11 là 1000; bạc 200 vạn x2 mỗi cấp, kẹp 20 ức từ +11). Thiếu thủy tinh/bạc báo đúng, không trừ.
3. ☐ Tỉ lệ: +1 luôn thành công (100%); từ +2 thử nhiều lần, thất bại GIỮ cấp, vẫn mất nguyên liệu + bạc. Tỉ lệ +15 = 30%.
4. ☐ Đã +15: bấm tiếp báo "đã tối đa".
5. ☐ Chỉ số: một món có dòng gốc ≥ 20 ở +0/+5/+10/+15 tăng 0/25/50/75% (làm tròn xuống; gốc nhỏ <20 có thể đứng yên).
6. ☐ +14: vũ khí có thêm "+1 tất cả kỹ năng"; +15: "+2". Kiểm cấp kỹ năng thật tăng trong bảng kỹ năng. Món không phải vũ khí KHÔNG có dòng này.
7. ☐ Lưu: cường hóa +3, thoát game bằng nút thoát, đăng nhập lại: vẫn +3. Thử tắt cưỡng bức client: vẫn giữ (nếu không, báo lỗi lưu).
8. ☐ Tháo ra mặc lại: giữ nguyên +N.
9. ☐ Tiền: bạc ≥ 21,47 ức không bị tràn (kẹp 20 ức); số bạc hiển thị đúng đơn vị vạn/ức.

## B. Điểm tài phú
1. ☐ Tài phú = 100 × tổng +N 10 ô đang mặc (nhẫn tính 2 ô). Mặc bộ +6 đủ 10 món → 6000.
2. ☐ Mỗi món có điểm riêng trên tooltip = 100 × +N; khung nhân vật hiện tổng; tổng server (`[QH]|W|`) = tổng client. LỆCH → lấy server làm chuẩn, báo lỗi.
3. ☐ Tháo một món +N → tổng giảm đúng 100×N ngay lập tức; mặc lại tăng lại.
4. ☐ Đồ trong túi KHÔNG tính.
5. ☐ (Q-90) Tài phú là thuộc tính nhân vật: mặc món +N tăng đúng 100×N, tháo giảm đúng, cường hóa món đang mặc +1 → tăng 100 ngay; đăng nhập lại vẫn đúng (tính lại từ đồ đang mặc). Tooltip món có dòng "Điểm tài phú +M".
6. ☐ (Q-90) Tooltip phi phong có "Yêu cầu tài phú: X" (đỏ nếu thiếu); mặc khi thiếu bị chặn bằng cơ chế yêu cầu chuẩn. Cần bản gs001 B-039 (SHA256-b039.txt).

## C. Phi phong 11 cấp
1. ☐ Cấp k cần tài phú ≥ 6000+900(k−1): 6000, 6900, ..., 15000. Thử đúng ngưỡng (mặc được) và dưới 1 điểm (bị chặn, có thông báo).
2. ☐ Mặc phi phong cấp k rồi tháo món làm tài phú giảm dưới ngưỡng: phi phong tự tháo (pf3) và có thông báo.
3. ☐ Chỉ số phi phong tăng dần theo cấp: sinh lực/nội lực 200→2200, thể lực 100→1100, kháng tất cả 4→44, tốc chạy 5→55 (bảng; các giá trị này là thiết kế, cần kiểm trong game xem dòng có hiện đúng).
4. ☐ Phi phong vàng không cộng tài phú.

## D. Hiển thị / khác
1. ☐ Số lớn hiển thị đơn vị vạn/ức; tooltip +N đúng màu/tiêu đề.
2. ☐ Đánh thường (nút đánh): bấm gần/xa quái đều đánh được, không "chỉ chạy sát quái"; quái hiện đúng tầm khi chạy tới.
3. ☐ Reset trước khi giao chủ: bỏ hook test `atestvaihero` trong qhcuonghoa.lua (dòng 44-52), bỏ phát đồ +15 thử, đặt tài khoản test về +0.
