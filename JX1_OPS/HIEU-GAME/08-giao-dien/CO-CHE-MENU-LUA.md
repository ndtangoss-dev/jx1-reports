# CƠ CHẾ MENU LUA (nút → opensysui → Lua → Say/SelectUI)

Sonnet A, 20/11/2026, #305. ĐÃ TRA ĐỒ THỊ (graphify client+server) / ĐÃ ĐỌC KIẾN THỨC (BAN-DO-CHUOI-CUONG-HOA.md). Điều đã chạy thật trên Test-36 ghi ĐÃ KIỂM; còn lại CHƯA KIỂM.

## Luồng
1. Nút trên màn chính (vd nút lửa Cường hóa) gọi `__opensysui(kind, a, b)` ở client → gói lên gs001.
2. gs001 chạy Lua `opensysui(inKind, inVala, ...)` (System\opensysui.lua). Ví dụ `(2,1)` → `Give(...)` mở UI Giao gốc. ĐÃ KIỂM.
3. Menu chọn: Lua gọi `Say(văn bản, số mục, bảng "tên/hàm")` (chuỗi `"Tên mục/tên_hàm"`) → client vẽ hộp thoại các nút (nhiều nút xếp 3 cột, ĐÃ KIỂM q306-b6.png).
4. Bấm nút: client gửi chỉ số mục → server gọi đúng hàm Lua đã đặt tên (Lua toàn cục); hàm chạy xong, hộp thoại đóng. Muốn tiếp phải `Say` lại (menu lồng).
5. Vật phẩm dùng được (sách, thẻ GM): "Sử dụng" → script `main` của vật phẩm → thường `Say(...)`. ĐÃ KIỂM với Tân thủ lục và Lệnh bài GM.

## Giới hạn
- Mục tối đa hiển thị: 9–11 nút/lần (ĐÃ KIỂM 10 nút, bố cục 3 cột); văn bản nút dài bị xuống dòng.
- Tên hàm trong chuỗi mục phải là hàm toàn cục đã nạp; không truyền tham số (dùng biến toàn cục/hàm riêng).
- Vật phẩm mà client coi không dùng được (vd 6,1,0) không có nút "Sử dụng" → không mở được menu (ĐÃ KIỂM q306-t4..t6).
- Gõ chữ có dấu: file Lua GBK; để an toàn dùng ASCII không dấu trong chuỗi mới.

## Cần client mới khi nào
- Thêm nút hay giao diện mới (ảnh/sprite, cửa sổ tùy biến): cần APK mới.
- Chỉ đổi nội dung menu, hàm, vật phẩm, tiền, thuộc tính: chỉ Lua, nạp nóng được (xem 09-cong-cu-gm/LOADSCRIPT-NAP-LUA-NONG.md).
