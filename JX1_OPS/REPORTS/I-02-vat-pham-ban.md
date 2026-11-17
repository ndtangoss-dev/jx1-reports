TÓM TẮT 5 DÒNG
1. Khảo sát tĩnh I-02 ngày 17/11/2026; chỉ đọc source và dữ liệu gốc, không chạy game/server, VM hay kết nối mạng.
2. Bảng gốc có 1.464 dòng goods, 160 dòng shop, 2.644 ô tham chiếu dương và 474 goods ID khác nhau được tham chiếu.
3. Bảo vật/Kỳ Trân có 4 danh mục, 62 goods ID; cả 62 cấu hình tiền Xu, nhưng chưa xác nhận settings đóng gói của client trùng server.
4. Có 312 goods được tham chiếu có Price trống và 5 ô chữ trong bảng ID shop; giá trống không đồng nghĩa mua miễn phí.
5. DONE trong phạm vi khảo sát tĩnh; đã đối chiếu bảng boss và soạn ca test, chưa kiểm chứng runtime; không commit/push.

## Phạm vi và quy ước

- Chỉ ghi báo cáo này theo `vung_file: [none, JX1_OPS/REPORTS/I-02-*.md]`. Yêu cầu thêm `## Kết quả` vào task mâu thuẫn vùng ghi, nên kết quả đặt cuối báo cáo; giữ nguyên task local có sẵn.
- `S` = `D:\JX-source\server\jxOnline`; `G` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs`; `C` = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client`.
- Số dòng tính cả header. Goods ID = số dòng goods trừ 1; shop nội bộ = số dòng buysell trừ 2. Dòng boss tính theo LF, bỏ CR thừa, vì một số INI có CR-CR-LF. Đếm tham chiếu bảng, chưa chứng minh mọi dòng đang được NPC/runtime sử dụng.
- Không xuất bảng đầy đủ hoặc dữ liệu nhạy cảm. Không tạo file tại `D:\JX-reports-private` vì ngoài vùng ghi của lượt này.

## ĐÃ XÁC MINH

- `S/header/CoreUseNameDef.h:123` và `:124` chọn `buysell.txt`, `goods.txt`, không chọn `goods_.txt`.
- `S/gameserver/Sources/Core/Src/KBuySell.cpp:118` nạp giá với mặc định 0; `:383` chặn giá sau sinh/thuế không dương.
- `S/gameserver/Sources/Core/Src/KItemGenerator.cpp:172` sao chép template thuốc; `:175` chỉ ghi đè giá khi dương. Quest (`:3637`, `:3645`) và mine (`:3826`, `:3833`) cũng giữ giá template khi override không dương.
- `S/gameserver/Sources/Core/Src/ScriptFuns.cpp:5427`: `Sale(n)` gọi `OpenSSale(n-1)`.

### Số liệu và cách đếm

Đọc TAB trực tiếp bằng Python inline `python -I -`, bỏ header; đếm ô số dương riêng với ô chữ. Không lưu parser hoặc bảng trích xuất. Với goods, mỗi dòng dữ liệu là một ID, kể cả nội dung trùng. Với shop, dòng trống vẫn được giữ trong chỉ số vật lý.

| Chỉ tiêu | Số lượng | Bằng chứng/phạm vi |
|---|---:|---|
| Dòng goods | 1.464 | `G/Settings/goods.txt:2`, cuối `:1465` |
| Dòng shop, kể cả trống | 160 | `G/Settings/buysell.txt:2`, cuối `:161` |
| Dòng shop có nội dung | 105 | Đếm dòng có ô khác rỗng/-1; 55 dòng còn lại trống |
| Ô ID số dương / goods ID khác nhau được tham chiếu | 2.644 / 474 | Toàn bộ `buysell.txt`; không cộng 5 ô chữ |
| ID số dương ngoài khoảng 1–1.464 / ID số 0 | 0 / 0 | Kiểm tra tất cả ô số trong buysell |
| Ô không rỗng không phải số nguyên | 5 | Chi tiết bên dưới |
| Price trống trong toàn goods | 1.107 | Cột 6; không có ô ghi số 0 hoặc giá âm |
| Goods được tham chiếu có Price trống | 312 | 292 trang bị + 20 thuốc; không phải 312 giao dịch miễn phí |
| Tiền tệ của 474 ID | 334 loại 0; 115 loại 2; 25 loại 6 | Cột 8, ô trống mặc định 0 |
| Template thuốc/mine/quest có kiểm tra chỉ số | 147/147 có dòng tên không rỗng | 20 thuốc + 121 mine + 6 quest; không phải kiểm thử sinh item |

ID shop trong Lua và trong UI không cùng quy ước: `Sale(151)` mở shop nội bộ 150, tức `buysell.txt:152`. Client `KuiDynamicShop` giữ nguyên `shopid` từ bảng Marketshop và gọi `GetItemIndex` trực tiếp (`C/Classes/gameui/KuiDynamicShop.cpp:212`, `:580`). Không trừ 1 lần nữa khi đối chiếu Marketshop.

### Bảo vật/Kỳ Trân: danh mục, giá và tiền

`C/Classes/gameui/KuiDynamicShop.cpp:198` nạp `\\settings\\Marketshop\\type.txt`, không phải `Newtype.txt`. Bảng rời phía server `G/Settings/Marketshop/type.txt:2` đến `:5` có bốn tên legacy, chuẩn hóa đọc là Kỳ Trân, Hoạt Động, Thư Tịch, Chiến Mã. Nội dung trong pak client chưa giải nén/đối chiếu.

| Danh mục theo type.txt | shopid nội bộ | Dòng buysell | Số ô ID dương | Price cấu hình | PriceShopType |
|---|---:|---:|---:|---:|---:|
| Kỳ Trân | 99 | 101 | 22 | 1–200 | 2: Xu |
| Hoạt Động | 100 | 102 | 10 | 1–20 | 2: Xu |
| Thư Tịch | 101 | 103 | 29 | 200 | 2: Xu |
| Chiến Mã | 102 | 104 | 1 | 300 | 2: Xu |

Tổng bốn danh mục là 62 ô, 62 ID khác nhau: 56 genre mine và 6 genre quest. Đây là danh mục dữ liệu, có điểm không khớp nhãn: shopid 102 chỉ chứa một mục genre mine, không phải trang bị ngựa theo enum; cần xác minh bằng client/tester, không tự sửa tên hoặc ID. `Newtype.txt` có 7 dòng danh mục, hai dòng cùng shopid 141 (`G/Settings/Marketshop/Newtype.txt:2`, `:3`); đây chỉ là bảng thay thế tìm thấy, chưa chứng minh đang được nạp.

Các ví dụ giới hạn đủ để kiểm tra, không chép nguyên bảng:

| Goods ID; bộ sinh item | Ví dụ theo szInfo/template | Giá cấu hình | Bằng chứng |
|---|---|---:|---|
| 1; medicine detail 0, level 1 | Kim Sáng Dược (tiểu), Price goods trống; template có Price 50 | Kế thừa template, chưa chốt số tiền runtime | `goods.txt:2`; `item/004/potion.txt:2` |
| 1299; mine particular 71, level 1 | Bạch Câu Hoàn | 3 Xu | `goods.txt:1300`; `item/004/mine.txt:73` |
| 1303; mine particular 164, level 1 | Phù vô hạn theo szInfo; thời hạn cấu hình 10 | 5 Xu | `goods.txt:1304`; `item/004/mine.txt:166` |
| 1309; quest detail 238 | Lam Thủy Tinh | 10 Xu | `goods.txt:1310`; `item/004/questkey.txt:240` |
| 1329; quest detail 489 | Lệnh bài Phong Lăng Độ | 3 Xu | `goods.txt:1330`; `item/004/questkey.txt:491` |
| 1341; mine particular 33 | Bí kíp môn phái; template Đạt Ma Độ Giang | 200 Xu | `goods.txt:1342`; `item/004/mine.txt:35` |
| 1422; mine particular 77 | Tống Kim Chiến Cổ | 1.000 điểm Tống Kim (loại 6) | `goods.txt:1423` |
| 1400; equip detail 10, particular 2, series 0, level 3 | Bạch Mã theo szInfo | 5.000 ngân lượng trước thuế | `goods.txt:1401`; shop ngựa `buysell.txt:152` |

Đường dẫn dữ liệu trong bảng trên đều dưới `G/Settings`. Cột `Level` là tham số tạo vật phẩm, không tự động là yêu cầu cấp người mua. `ThoiGianBan` được nạp thành `nExpirePoint`, rồi cộng ngày để đặt hạn vật phẩm (`KBuySell.cpp:123`, `:464`); không có cơ sở gọi đó là lịch mở bán hoặc hạn mua theo ngày.

`S/header/GameDataDef.h:231` định nghĩa loại 0/1 = ngân lượng, 2 = Xu, 3 = phúc duyên, 4 = danh vọng, 5 = điểm vinh dự theo nhánh xử lý, 6 = điểm Tống Kim. Nhánh kiểm tra và trừ tiền ở `KBuySell.cpp:392`, `:512`: loại 5 dùng task 2051; loại 6 dùng task 192. Dữ liệu được tham chiếu chỉ có loại 0, 2, 6. `PriceXu` cột 7 được đọc rồi bị gán lại bằng `Price` cột 6 (`:120`, `:121`), nên không dùng cột 7 để suy ra giá Xu độc lập.

### Nhóm vật phẩm

Phân nhóm kỹ thuật theo `S/gameserver/Sources/Core/Src/KItem.h:61`; không đồng nhất mọi genre mine với nguyên liệu chế tạo.

| Nhóm | Toàn goods | Goods ID được shop tham chiếu | Diễn giải |
|---|---:|---:|---|
| Thuốc, genre 1 | 50 | 20 | Template `item/004/potion.txt` có 49 dòng dữ liệu; 20 chỉ số dùng bởi shop đều có dòng tên |
| Trang bị, genre 0 | 1.161 | 326 | Bao gồm ngựa/phụ kiện; chưa kiểm tra toàn bộ tổ hợp template, thuộc tính sinh ngẫu nhiên |
| Mine, genre 2 | 195 | 121 | Nguyên liệu, sách, vật phẩm tiêu hao, hỗ trợ; ví dụ phúc duyên lộ, Bạch Câu Hoàn, bí kíp; template có 321 dòng |
| Quest, genre 4 | 57 | 6 | Gồm 3 thủy tinh, Tinh Hồng Bảo Thạch, vé Phong Lăng Độ và Nhạc Vương Hồn Thạch; template có 1.326 dòng |
| Truyền tống, genre 5 | 1 | 1 | Goods 446; giá goods 500, tên szInfo là `???`, cần đối chiếu template/UI |
| Tổng | 1.464 | 474 | Đếm ID, không phải tên hoặc loại template duy nhất |

Nhóm công dụng cắt ngang enum: 3 mục đá/thủy tinh là goods 1309–1311, đều được shop nội bộ 99 tham chiếu ở cột 15–17 (`buysell.txt:101`). Template `questkey.txt:240`, `:241`, `:242` lần lượt mô tả đổi ngũ hành, nâng cấp trang bị, đổi thuộc tính. Nhóm hoạt động có 10 mục trong tab Hoạt Động, trong đó goods 1329 là vé; không suy tất cả 10 mục chỉ dùng cho hoạt động từ nhãn tab. Không có số đếm nguyên liệu chế tạo chính xác tách khỏi 121 mục mine, vì cần rà công dụng các script/template; số 121 là nhóm kỹ thuật.

### Điều kiện mở, mua và giới hạn

- NPC: `G/script/global/npcchucnang/shop_datau.lua:172` nhận shop qua callback rồi `Sale(nIDShop)` tại `:174`; ví dụ `:179` gọi `Sale(151)`, ứng với shop nội bộ 150, có 7 ô ID số dương. Callback này chưa đủ chứng minh NPC đã được map gán đúng script.
- Đường mở SuperShop cũ: `G/script/System/player/script_protocol.lua:69` kiểm tra trạng thái chiến đấu và `IsShopMap`; `:74` gọi `NewSale(0,1,5,97,98,99,100,101)`. Các dòng shop nội bộ 97/98 trong dữ liệu hiện có trống. Chưa tìm thấy binding `NewSale` trong `ScriptFuns.cpp` đã đọc; chưa chứng minh đường này đang hoạt động. Không trộn danh sách này với bốn tab DynamicShop.
- Mua hàng theo source: shop phải khớp trạng thái người chơi (`KBuySell.cpp:292`), chỉ số item phải trỏ vào goods hợp lệ (`:316`), mua nhiều phải là item xếp chồng (`:334`), tiền phải đủ, có chỗ hành trang (`:487`), giá đơn và tổng phải dương (`:383`, `:456`). Giá có cộng/trừ thuế thành viên bang ở `:348`.
- DynamicShop hiện đặt `nCount=1`, khối đọc số lượng bị comment (`C/Classes/gameui/KuiDynamicShop.cpp:438`, `:484`, `:500`). `KuiShop.cpp:345` chặn trên UI ở 150; `KuiSuperShop.cpp:357` chặn ở 30. Đây là ba đường UI khác nhau, không phải ba hạn mức server đã xác minh.
- Header goods không có trường tồn kho, hạn mức tài khoản/ngày hoặc cấp tối thiểu người mua. Chưa thấy hạn mức theo ngày trong `KBuySell::Buy` đã đọc. Chưa kiểm tra toàn bộ đường protocol/script nên không kết luận toàn hệ thống không có giới hạn.

### Đối chiếu boss

Đọc trực tiếp 59 file `.ini` dưới `G/Settings/droprate` có `boss` trong đường dẫn/tên, không phân biệt hoa thường. Đây là tập được chọn theo tên, không phải khẳng định đủ mọi boss. Đếm block số có `Genre`, `Detail`, `Particular`, với số section không vượt `Main/Count`: có 3.458 block thô (3.036 equip, 362 quest, 57 mine, 3 medicine). Số này vẫn chứa block trùng tên section, không phải số kết quả rơi hiệu lực.

Đối chiếu sơ bộ shop theo bộ ba genre/detail/particular có 259 goods ID trùng trong tập block; lọc thêm RandRate dương và level nằm trong min/max section hoặc phạm vi Main khi thiếu section cho 256 ứng viên, đều genre equip. Bộ lọc Main chỉ là sàng lọc tĩnh: source còn tính theo cấp NPC và scale (`S/gameserver/Sources/Core/Src/KNpc.cpp:12585`). Không gọi 256 ứng viên này là vật phẩm chắc chắn rơi hoặc cùng chất lượng với hàng bán; chưa so series, Quality, magic, bind, expiry và script phát thưởng.

Ví dụ tái kiểm tra: goods 26 ở `goods.txt:27` là equip `(0,0,0)`, series 4, level 1; `G/Settings/droprate/BOSSÕÙ»½/putong.ini:24` có section `[1]`, `Genre=0`, `Detail=0`, `Particular=0`, `RandRate=10`. Đây là trùng loại cơ sở, không phải đối chiếu theo goods ID; file drop không dùng chỉ số dòng goods. Tên thư mục trên giữ đúng ký tự đang lưu trên đĩa.

Bốn tab Marketshop không có ID nào trong tập 256 ứng viên equip, vì 62 ID ở đây đều mine/quest. Không suy ra Bảo vật độc quyền, hoặc không thể rơi từ boss: script, loại drop khác, cấp và cách xử lý mine/quest chưa được đối chiếu đầy đủ.

Chất lượng bảng drop cần chú ý: có 125 block số nằm ngoài `Count`; 2 file có tên section lặp, gồm `G/Settings/droprate/ÊÀ½çBOSS/°×Ó¨Ó¨.ini` (section 55 lặp) và `.../µÀÇåÕæÈË.ini` (1–56 lặp). Chưa mô phỏng chính xác lựa chọn section trùng của loader; do đó chỉ dùng số liệu thô và ví dụ, không công bố xác suất rơi. Ca tester phải gắn đúng boss/NPC và bảng thực sự được nạp.

### Bất thường và mức chắc chắn

1. **5 ô chữ trong bảng chỉ số**: `buysell.txt:150` cột 34 `Bi kiep`; `:151` cột 15 `Ma Bai`; `:155` cột 6 `Trang suc`; `:156` cột 24 `Tong kim Xu`; `:157` cột 27 `Tong Kim diem`. `S/gameserver/Sources/Engine/Src/KTabFile.cpp:681` dùng `atoi` tại `:687`, nên chuỗi này cho 0 khi đọc thành công; `KBuySell.cpp:231` chỉ trừ 1 khi giá trị dương. Theo source, chúng có nguy cơ trở thành chỉ số mảng goods 0 (goods ID 1), thay vì sentinel -1. Chưa quan sát UI/runtime. Ưu tiên xác minh; không tự sửa.
2. **Giá trống không phải giá miễn phí**: 1.107 dòng toàn bảng, 312 ID được tham chiếu có cột Price trống. Thuốc, mine/quest và nhiều nhánh trang bị giữ giá template nếu override không dương (`KItemGenerator.cpp:175`, `:388`, `:3645`, `:3833`). Ví dụ thuốc tiểu có template Price 50 ở `item/004/potion.txt:2`, khác bảng potion ngoài `004`. Nếu giá item sau sinh và thuế vẫn không dương thì source từ chối mua. Chưa tính giá hiệu lực của tất cả trang bị.
3. **Cột trưng bày không bảo đảm ẩn**: ba thủy tinh và THBT có `IsShow=0` (`goods.txt:1310` đến `:1313`) nhưng vẫn nằm trong `buysell.txt:101`. `KBuySell::Init` đọc các cột 1–11 và 14–19, không dùng cột 13 IsShow. Chưa xác minh bộ lọc UI khác; không gọi các mục này đã bị ẩn.
4. **Bản dữ liệu thay thế lệch**: `goods_.txt` khác `goods.txt` ở 5 dòng (1300, 1307, 1370, 1453, 1458), gồm khác item/giá và tên. Ví dụ `goods.txt:1300` là particular 71 giá 3, bản gạch dưới là particular 68 giá 200. Macro source chọn bản không gạch dưới; chưa xác minh binary/client chọn cùng bản.
5. **Dòng trùng**: `goods.txt:1464` và `:1465` giống nhau, nhưng vẫn là hai goods ID riêng 1463/1464; ID 1463 được shop tham chiếu, 1464 không nằm trong tập 474. Không khẳng định trùng là lỗi gameplay.
6. **Biên chỉ số source cần rà riêng**: `KBuySell.cpp:309` kiểm tra `nBuyIdx > m_Width`, chưa loại bằng m_Width hoặc âm ngay tại điều kiện này; `:851` có điều kiện biên tương tự. Đây là quan sát tĩnh, chưa chứng minh đầu vào có thể tới được; không gửi gói thử hoặc khai thác.

### Ca test cho TESTER — chỉ là thiết kế, chưa chạy

Chỉ thực thi ở môi trường thử nghiệm sau khi được phê duyệt riêng. Không dùng tài khoản/số dư thật, không kết nối production.

| Mã | Ca kiểm tra | Kết quả cần quan sát |
|---|---|---|
| I02-T01 | Mở Bảo vật ở từng đường DynamicShop/SuperShop; ghi phiên bản settings | Bốn tab 99–102 có lần lượt 22/10/29/1 ID theo dữ liệu rời; xác định đường cũ và shop 97/98 trống có được dùng không |
| I02-T02 | Mua 1 Bạch Câu Hoàn, vừa đủ/thiếu Xu | Giá cơ sở 3 Xu; ghi thuế nếu có; chỉ trừ đúng loại tiền, thiếu tiền không sinh item |
| I02-T03 | Mua thuốc ID 1 có Price trống | Xác minh kế thừa template, UI và số tiền trừ khớp; không miễn phí; không lấy giá 60 từ potion ngoài thư mục 004 |
| I02-T04 | Quan sát 5 ô chữ và ba thủy tinh IsShow=0 | Ghi nhận item thừa/ẩn hiện; đối chiếu goods ID 1; không sửa bảng gốc |
| I02-T05 | Mua item xếp chồng/không xếp chồng; thử nhập 0 và số vượt giới hạn UI | DynamicShop mua 1/lần theo source; UI thường tối đa 150, SuperShop 30; server từ chối mua nhiều item không stack; không giả định có quota ngày |
| I02-T06 | Mua khi hành trang đầy, đổi tab, đóng shop rồi mua | Thất bại phải không mất tiền/không cấp item; xác nhận shop/item khớp trạng thái |
| I02-T07 | Thử mở theo PermitSuperShop khi chiến đấu/ngoài map được phép | Đường script cũ từ chối theo điều kiện; xác định có áp dụng cho DynamicShop không |
| I02-T08 | Mua phù goods 1303 | Giá 5 Xu trước điều chỉnh; hạn vật phẩm tương ứng 10 ngày nếu source này chạy; không nhầm thành hạn mua |
| I02-T09 | Mua goods 1422 bằng điểm Tống Kim | Trừ 1.000 task 192 theo source; không trừ Xu/ngân lượng; thiếu điểm không cấp item |
| I02-T10 | Gắn đúng NPC boss và bảng drop trên bản thử nghiệm, đối chiếu `(genre,detail,particular,level,series,quality)` | Xác minh loại cơ sở có thể trùng hàng shop; kiểm tra tác động section trùng/vượt Count; không diễn giải RandRate trực tiếp thành phần trăm |
| I02-T11 | Rà biên chỉ số bằng kiểm thử nội bộ có chặn an toàn | Xác minh slot âm/bằng width và shop bằng height bị từ chối trước truy cập; không thử trên server thật |

### Dấu vết dữ liệu

SHA-256 đọc tại chỗ, không gửi dịch vụ ngoài:

| File dưới G | SHA-256 |
|---|---|
| `Settings/buysell.txt` | `dc424d5be9f27405e8364d9c45eccd09877c741fec8000f1aac64abcc1af92e9` |
| `Settings/goods.txt` | `e7317151e8e76572d327110d8b555d0af105a1b353113790f637adfba6e740ba` |
| `Settings/Marketshop/type.txt` | `65203330a84019f0ee92e4efc541d88e3ee1a7ad717541678a30fd2a718d7ddb` |

## CHƯA XÁC MINH

- Chưa chạy runtime/build/test; chưa xác nhận nội dung settings trong pak của client trùng dữ liệu server rời.
- Chưa chứng minh binary được build từ source đã đọc; mọi nhận định hành vi là theo source.
- Chưa kiểm tra đầy đủ template/giá hiệu lực của 326 trang bị và 1 truyền tống; 0 ID số dương thiếu dòng goods không đồng nghĩa mọi item sinh thành công.
- Chưa chia chính xác 121 mục mine theo công dụng script, xác minh quota toàn hệ thống, gán NPC/map, xác suất boss và lựa chọn section INI trùng.
- Chưa dùng dữ liệu client trong pak để đếm độc lập; các bảng số liệu là dữ liệu server gốc, source UI là client gốc. Không đọc nội dung file khóa/mật khẩu.

## Lỗi và xử lý

- `rg : The term 'rg' is not recognized as the name of a cmdlet, function, script file, or operable program.` Đã chuyển sang PowerShell và Python inline với `python -I`; không cài công cụ, không tạo parser/script phụ.
- PowerShell đọc mặc định làm sai hiển thị tiếng Việt trong prompt; đã đọc lại UTF-8. Dữ liệu legacy được đọc giữ byte qua Latin-1 cho số/cột ASCII, không suy tên tiếng Việt từ giải mã GBK.
- Kiểm tra cấu trúc lần đầu báo `AssertionError` ở ba phép so chuỗi tiếng Việt truyền qua PowerShell stdin; diff UTF-8 vẫn hiển thị đúng. Đã chuyển chuỗi kỳ vọng sang Unicode escape và kiểm tra lại, không đổi nội dung dữ liệu gốc.

## Kết quả

**DONE — khảo sát tĩnh theo phạm vi I-02.** Đã lưu bản nháp trong chính báo cáo này rồi hoàn thiện; chỉ tạo/cập nhật `JX1_OPS/REPORTS/I-02-vat-pham-ban.md`, không sửa mã, dữ liệu gốc hoặc task có sẵn. Đã chạy đọc/đếm bảng và kiểm tra chỉ số tĩnh; không chạy build, runtime, VM, exe dự án hoặc ca test trong bảng trên.

Commit SHA: không có, chưa commit. Chưa push vì người dùng yêu cầu khảo sát local và không mạng; không có bằng chứng GitHub và không tuyên bố đã công bố. Không sửa credential/config. Các giới hạn xác minh được ghi ở mục CHƯA XÁC MINH; không có blocker ngăn hoàn thành báo cáo tĩnh.
