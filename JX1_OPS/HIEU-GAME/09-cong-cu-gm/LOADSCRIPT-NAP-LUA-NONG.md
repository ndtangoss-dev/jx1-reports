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

## Cập nhật 20/11 17:20 — đã nạp nóng B-051 thật (#308)
- Nạp nóng được (không restart, đã đo): `qianghua.lua` (hàm mới `qh_wealth`, có hiệu lực ngay lần dùng kế), `opensysui.lua` (nhánh `inVala==12` gửi `[QH]|W|`), `qh_bothu.lua`. Cách: mục "[#306] Nap lai Lua nong" trong menu Hỗ trợ Thử nghiệm gọi LocalScript từng file (nạp đúng 1 lần là đủ; lần đầu sau khi sửa chính hàm `qhbv_reload` cần bấm 2 lần).
- Cần relogin: chưa gặp. C++ (EnChanceRong B-049/B-050 client) vẫn phải thay exe/APK.

## Chuỗi cấp đồ GM + điều kiện lưu DB (#311, A, 20/11 17:55 — BẢN NHÁP, còn chờ TN4/TN5)
**Chuỗi nút → script (đã thấy trên LD + mã):**
1. Túi có sách (6,1,0) → "Sử dụng" → `\script\item\baowubox.lua` → `qhbv_menu()` (qh_bothu.lua, GBK) hoặc menu Tân thủ (`lenhbaitanthu.lua`): "[TEST-36] Hỗ trợ Cường hóa", "Hỗ trợ tân thủ", "Nhận Code Tân Thủ", "Nhận Thẻ GM", "Hỗ trợ Thử Nghiệm".
2. "Nhận Thẻ GM" → script cấp "Lệnh bài GM x1" (qua AddItem). "Đồ XANH" → `qhbv_blue` → `AddItem(0,b[1],b[2],b[3],b[4],1000,6,6,6,6,6,6,1,0,0)`. Thủy tinh → `qhbv_cry` → `AddItem(4,239..240..238,...,200,0,0)`.
3. `LuaAddItem` (`gameserver/Sources/Core/Src/ScriptFuns.cpp:8978`): `ItemSet.AddOther(...)` rồi `m_ItemList.Add(nIndex,pos_equiproom,x,y,0,0,nStackNum)` (dòng 9053–9093). KHÔNG đặt cờ "tạm/không lưu" nào; item cấp bằng AddItem đi cùng đường `Add` như item nhặt/mua.
**Điều kiện lưu**: Goddess nhận đủ (log `gw\goddes_log`, cột cuối = số món: 12→5→3 khớp màn hình trước khi thoát, 20/11 17:28/17:33/17:36).
**Điều kiện nạp**: `KPlayer::LoadPlayerItemList` (`KPlayerDBFuns.cpp:818`) sinh lại từng món bằng ItemGen; món nào sinh lại thất bại bị bỏ im lặng (dòng ~1110–1115). Log chi tiết chỉ khi `showItemInfo` bật (`KGameglobalSet.cpp:52`) nhưng `gs\gameser_log` không có dòng nào.
**Kết luận hiện tại**: không có cờ GM/tạm trong LuaAddItem; mất đồ xảy ra ở bước NẠP sau đăng nhập (đã chứng minh bằng đếm 3 lần). Chưa biết vì sao món bị bỏ: kiểm tiếp bằng TN4 (restart gs001) và TN5 (nhân vật cũ).
