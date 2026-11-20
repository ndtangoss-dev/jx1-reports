# LOADSCRIPT — nạp lại Lua nóng trên gs001 đang chạy (không restart)

Điều tra #306/#306b, Sonnet A, 20/11/2026, Test-36 (gs001 192.168.56.150).
ĐÃ TRA ĐỒ THỊ (graphify server) / ĐÃ ĐỌC KIẾN THỨC (HIEU-GAME/08-giao-dien).

## Kết luận
Lua trên gs001 **nạp lại được khi server đang chạy**, không cần khởi động lại (tiết kiệm ~8–10 phút/lần). Hai cách, đều ĐÃ KIỂM trong game:

| Cách | Cơ chế | Hiệu lực | Đo thật |
|---|---|---|---|
| (a) `dofile` đầu `main` của script vật phẩm | file đọc lại từ đĩa MỖI LẦN dùng vật phẩm | Lần dùng KẾ TIẾP (lần đang dùng vẫn chạy main cũ) | sửa file → dùng thẻ 2 lần ≈ 30 s |
| (b) nút "ReloadScript GM" (`tb_LocalScript`, gmroleitem.lua:1552) gọi `LocalScript(đường dẫn)` | `LuaLocalScript` ScriptFuns.cpp:20470 → `ReLoadScript` KSortScript.cpp:444 (UnLoadScript + nạp lại, trả id script, vd 4474/4475) | Ngay lần gọi kế sau nút; mọi người chơi dùng bản mới | 2 giây, không restart |

Chuỗi dùng thực tế (đã chạy 16:44–16:46): sửa file trên VM → vào game → Lệnh bài GM → nút ReloadScript (thông báo `LocalScript ... =4476 ... =4477`) → mở vật phẩm lần 1 (còn mục cũ) → lần 2 thấy mục mới → bấm mục mới mở menu `qhbv_menu`. Ảnh: `DESIGN/ANH-NGHIEM-THU/q306-b3/b5/b6.png`.

## #306b: "chỉ hiệu lực sau đăng nhập lại"?
- Trong phiên: ĐÃ KIỂM, có hiệu lực không cần đăng nhập lại (đo trên).
- Sau đăng nhập lại: CHƯA KIỂM bằng thao tác thật (chưa đăng xuất LD). Suy luận từ mã: nạp script là trạng thái toàn gs001 (không gắn phiên người chơi), nên đăng nhập lại chỉ gặp cùng bản đã nạp; cách (a) luôn đọc đĩa nên chắc chắn thấy bản mới.

## Cách dùng (cho A/B)
1. Sửa file Lua theo byte trên VM (có `.bak`; đường dẫn dùng `\\`).
2. Nhân vật `atest*` dùng Lệnh bài GM (cần `CHECKGM()`), bấm ReloadScript, rồi dùng vật phẩm 2 lần.
3. Muốn nút nạp đúng file: sửa danh sách `LocalScript("\\script\\...")` trong `tb_LocalScript` (hiện nạp baowubox.lua và qh_bothu.lua; bản gốc ở `gmroleitem.lua.bak-q306`).

## Giới hạn
- Chỉ Lua (script, \script\...). KHÔNG nạp được C++/exe (gs001.exe vẫn phải restart khi B đưa bản exe mới).
- Hiệu lực từ lần dùng kế; hàm toàn cục cũ bị thay bằng hàm mới (biến toàn cục giữ nguyên nếu file không gán lại).
- Item client coi là không dùng được (vd 6,1,0 "Thương Long Văn Cương Giáp") thì không mở được script: dùng sách Tân thủ hoặc Lệnh bài GM.

## Rủi ro
- Lỗi cú pháp trong file nạp lại ảnh hưởng MỌI người chơi trên gs001 (hàm hỏng); nạp trên Test-36 trước, luôn có `.bak`.
- LocalScript không tự kiểm GM; chỉ an toàn vì menu thẻ GM bị CHECKGM chặn.
- Chỉ dùng trên Test-36. Main VM theo Q-18, không đụng.

Khuyến nghị: từ nay sửa Lua (qianghua.lua, qh_bothu.lua, opensysui.lua) thì nạp nóng thay vì restart gs001.
