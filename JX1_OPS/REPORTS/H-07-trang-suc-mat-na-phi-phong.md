TÓM TẮT 5 DÒNG
1. DONE — hoàn tất khảo sát tĩnh H-07; không sửa mã, không mạng/VM, không chạy game hay build.
2. [NGUỒN] Trang sức thường có Detail 3/4/9; mặt nạ 11, phi phong 12, sức phẩm riêng 14; server/Coco cùng 15 ô trang bị.
3. [NGUỒN] Bảng gốc có 10 nhẫn, 20 dây chuyền, 20 ngọc bội, 967 dòng mặt nạ, 14 phi phong và 260 sức phẩm; đây là số dòng dữ liệu, không phải số item đang phát hành.
4. [NGUỒN] Phát hiện Mask.txt thiếu tiêu đề so với loader và phần tử kích hoạt thứ ba của Coco mặc định thành ô đầu; cần TESTER xác minh ảnh hưởng.
5. [CHƯA BIẾT] Chưa xác minh runtime/APK/PAK, xác suất nhận/nâng cấp hoặc NPC đang bật; báo cáo có bằng chứng file:dòng và 12 ca test đề xuất.

## Phạm vi, nguồn và cách đọc bằng chứng

- Task H-07; worktree `D:\JX-wt\H-07`, nhánh `task/H-07` đã xác nhận trước khi ghi.
- Chỉ đọc source, bảng cấu hình và script; không sửa mã, không build/test runtime, không mạng/VM/exe.
- Quy ước `S:` = `D:\JX-source\server\jxOnline`; `C:` = `D:\JX-source\client\Classes`; `SC:` = `S:/gameserver/Sources/Core/Src` (tiền tố báo cáo, không phải ổ đĩa).
- `G:` = gói gốc `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs`; `O:` = client gốc `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client`.
- [NGUỒN] = đã đọc trực tiếp source/bảng/script trên đĩa; [XÁC MINH] chỉ dùng cho phép kiểm tra tĩnh thực sự đã thực hiện. Không đồng nhất source với binary đang chạy.
- Số dòng là dòng vật lý tính từ 1; chỉ mục record của loader tính từ 0. Tên Việt trong dữ liệu gốc dùng bảng mã cũ, tên trong bảng dưới được trình bày lại dễ đọc; số, symbol và đường dẫn giữ nguyên.

## ĐÃ XÁC MINH

### 1. Loại item và ô trang bị

[NGUỒN] `SC:KItem.h:85`, `C:gamecore/KItem.h:52`, `S:header/GameDataDef.h:209`, `C:gamecore/GameDataDef.h:211` xác định các enum sau. Tất cả nhóm này có `Genre=0` (`item_equip`). `DetailType` không phải `ITEM_PART`.

| Nhóm | DetailType | Particular có trong bảng thường gốc | ITEM_PART | Tên ô UI Coco |
|---|---:|---|---|---|
| Nhẫn | 3 `equip_ring` | 0 | 7 `ring1`, 8 `ring2` | Ring1, Ring2 |
| Dây chuyền/hộ thân phù | 4 `equip_amulet` | 0, 1 | 6 `amulet` | Necklace |
| Hương nang/ngọc bội | 9 `equip_pendant` | 0, 1 | 9 `pendant` | Pendant |
| Mặt nạ | 11 `equip_mask` | 0–966 | 11 `mask` | Mask |
| Phi phong | 12 `equip_pifeng` | 0 | 12 `pifeng` | Mantle |
| Sức phẩm/trang sức riêng | 14 `equip_shiping` | 0–25 | 14 `shiping` | Shipin |

`equip_shiping` là nhóm riêng bên cạnh trang sức thường; không gộp nó với nhẫn/dây chuyền/ngọc bội. Ấn (`Detail=13`, `ITEM_PART=13`) chỉ dẫn ra để tránh nhầm, không khảo sát sâu H-06.

[NGUỒN] Server `SC:KItemList.cpp:2462` và Coco `C:gamecore/KItemList.cpp:1852` ánh xạ loại sang ô; nhẫn mặc định trả ring1. `C:gamecore/KItemList.cpp:1904` (`Fit`) cho phép đặt nhẫn ở ring1 hoặc ring2. `SC:KItemList.cpp:1153` (`CanEquip`) kiểm tra Genre, đúng ô và từng `GetRequirement` qua `EnoughAttrib`; không thể chỉ dựa vào icon để kết luận mặc được.

[NGUỒN] Hai giao diện đều có đầy đủ ô. Bản VN `C:vn/gameui/KuiRoleStateVN.cpp:29` đặt Necklace (201,60), Ring1 (14,150), Ring2 (14,190), Pendant (14,237), Mask (14,21), Mantle (14,339), Shipin (241,339). Đây là offset trong panel, không phải tọa độ màn hình. Bản thường có cùng tên ô, tọa độ khác ở `C:gameui/KuiRoleState.cpp:52`.

### 2. Bảng dữ liệu, chỉ mục và thuộc tính

[NGUỒN] `SC:KBasPropTbl.CPP:16` chọn `\settings\item\004`; Coco chọn `\update10\settings\item\004` ở `C:gamecore/KBasPropTbl.cpp:16`. Vì vậy bảng server rời dưới `G:` chưa chứng minh bằng với dữ liệu mà Coco nạp. Không đọc thay thế các bản trùng tên trong `Settings/vn` hoặc `Settings/item` rồi coi là bảng đang dùng.

| Bảng dưới G:Settings/item/004 | Dòng dữ liệu trên đĩa | Level có trong bảng | Bằng chứng dòng |
|---|---:|---|---|
| ring.txt | 10 | 1–10 | 2–11 |
| amulet.txt | 20 | 1–10 | 2–21 |
| pendant.txt | 20 | 1–10 | 2–21 |
| Mask.txt | 967, **không có dòng tiêu đề** | 1–10 | 1–967 |
| PiFeng.txt | 14 | 1–14 | 2–15 |
| ShiPin.txt | 260 | 1–10 | 2–261 |

[XÁC MINH] Đếm trực tiếp byte/dòng với `python -I`; nhận diện dòng dữ liệu bằng các cột Genre/Detail/Particular dạng số. Số dòng vật lý tương ứng: 11, 21, 21, 967, 15, 261. Không diễn giải thành số record đã nạp thành công.

[NGUỒN] `SC:KItemGenerator.CPP:628` (`Gen_Equipment`), công thức tại dòng 662 và ngoại lệ dòng 666; Coco cùng công thức ở `C:gamecore/KItemGenerator.CPP:775`:

- Thường: `record = Particular*10 + Level - 1`.
- Mặt nạ: `record = Particular`, không nhân 10 theo Level.
- `SC:KBasPropTbl.CPP:810` tính `height-1`; `LoadRecord` dòng 95 cộng 2 để bỏ tiêu đề. Với bảng có header, record 0 → dòng vật lý 2.
- **Bất nhất mặt nạ:** `G:Settings/item/004/Mask.txt:1` đã là item Particular=0, giá trị biến hình đầu=54; dòng 2 là Particular=1, giá trị=56. Nếu nạp đúng file này bằng loader đã đọc, record 0 lấy dòng 2; Particular 966 vượt 966 record có thể nạp. Đây là kết luận điều kiện từ source và file rời, chưa chứng minh gói runtime dùng file này.

[NGUỒN] Cột cơ bản/nhu cầu được ánh xạ tuần tự trong `SC:KBasPropTbl.CPP:1351`: 7 bộ thuộc tính cơ bản (type,min,max), 6 bộ yêu cầu (type,value), rồi trường ẩn/rèn/ngoại hình mở rộng. Enum `SC:KMagicAttrib.h:49`, `:51`, `:100`, `:104` tương ứng ID 36=cấp nhân vật, 38=giới tính, 85=sinh lực tối đa, 89=nội lực tối đa. Các số dưới đây là **min–max cấu hình**, không phải giá trị đã roll.

| Nhóm/mẫu | Thuộc tính và điều kiện trong bảng thường | Bằng chứng |
|---|---|---|
| Nhẫn Particular=0, Level=1/10 | Không có type cơ bản; yêu cầu cấp 1/60; giá 360/8840 | ring.txt:2, :11 |
| Dây chuyền Particular=0, Level=1/10 | Không có type cơ bản; cấp 1/60, yêu cầu sex=1 | amulet.txt:2, :11 |
| Hộ thân phù Particular=1, Level=1 | Cấp 1, sex=0 | amulet.txt:12 |
| Hương nang Particular=0, Level=1/10 | Không có type cơ bản; cấp 1/60, sex=1 | pendant.txt:2, :11 |
| Ngọc bội Particular=1, Level=1 | Cấp 1, sex=0 | pendant.txt:12 |
| Mặt nạ Particular=0 khai báo ở dòng đầu | Base[0] type trống, value 54–54 dùng cho biến hình; 85=100, 89=50; Level=1 | Mask.txt:1 |
| Sức phẩm Particular=0, Level=1/10 | 85 và 89 cùng 10–20 / 800–1000; yêu cầu cấp 10 | ShiPin.txt:2, :11 |
| Sức phẩm Particular=1, Level=1 | Type 126=100, 121=50, 227=100, 168=50; cấp 10, type yêu cầu 47=53 (giữ ID, chưa diễn giải điều kiện đầy đủ) | ShiPin.txt:12 |

Không có type cơ bản ở nhẫn/dây chuyền/ngọc bội thường **không có nghĩa** các bản xanh/vàng/bạch kim không có chỉ số: sáu magic attr được sinh riêng; `SC:KItem.cpp:148` áp base attr, dòng 159 xử lý magic attr, các slot chỉ số lẻ phụ thuộc `nMagicActive`. Bảng `GoldItem.txt` là dữ liệu khác, không lấy số trong PiFeng.txt gán cho phi phong vàng.

| Level phi phong (Particular=0) | Tên trong PiFeng.txt | Sinh lực tối đa **và** nội lực tối đa, mỗi loại | Dòng |
|---:|---|---|---:|
| 1 | Lăng Vân | 50–100 | 2 |
| 2 | Tuyệt Thế | 100–150 | 3 |
| 3 | Phá Quân | 150–200 | 4 |
| 4 | Ngạo Tuyết | 200–300 | 5 |
| 5 | Kình Lôi | 300–500 | 6 |
| 6 | Ngự Phong | 500–700 | 7 |
| 7 | Phệ Quang | 700–900 | 8 |
| 8 | Khấp Thần | 900–1100 | 9 |
| 9 | Kình Thiên | 1100–1300 | 10 |
| 10 | Vô Cực | 1300–1500 | 11 |
| 11 | Cao cấp | 13000–15000 | 12 |
| 12 | Tân thủ | 1000–1500 | 13 |
| 13 | VIP | 15000 | 14 |
| 14 | JXGM chuyên dụng | 600000 | 15 |

Tất cả dòng phi phong trên yêu cầu cấp nhân vật 10; có các type cơ bản bổ sung 209–212 trên một số dòng nên bảng chỉ tách hai chỉ số 85/89 để so sánh. Level item 11–14 là dữ liệu trong gói, không phải mức cường hóa +11…+14 và chưa xác minh có được phát cho người chơi thông thường.

### 3. Kích hoạt thuộc tính: khác biệt server/Coco

[NGUỒN] `SC:KItemList.h:6` và `C:gamecore/KItemList.h:6` đều `MAX_ITEM_ACTIVE=3`. Server khai báo đủ ba phần tử mỗi hàng ở `SC:KItemList.cpp:54`; Coco chỉ khởi tạo hai phần tử, phần tử thứ ba mặc định `0 = itempart_head`, ở `C:gamecore/KItemList.cpp:51`. Đây **không phải** danh sách hai phần tử an toàn bỏ qua phần tử thứ ba.

| Ô được kích hoạt | Ba ô nguồn theo server (`ms_ActivedEquip`) | Ba ô nguồn thực tế từ initializer Coco |
|---|---|---|
| amulet | belt, ring2, ring1 | belt, ring2, head |
| ring1 | weapon, head, belt | weapon, head, head |
| ring2 | cuff, pendant, amulet | cuff, pendant, head |
| pendant | foot, ring1, mask | foot, ring1, head |
| mask | yinjian, shiping, pifeng | yinjian, shiping, head |
| pifeng | horse, mask, pendant | horse, mask, head |
| shiping | horse, pifeng, yinjian | horse, pifeng, head |

`GetEquipEnhance` ở `SC:KItemList.cpp:2674` / `C:gamecore/KItemList.cpp:2046` cộng tương sinh nhân vật, lặp đủ ba ô nguồn và chặn tối đa 3. `ms_ActiveEquip` (chiều lan truyền) cũng lệch phần tử thứ ba: server dòng 34 so Coco dòng 31. Cần kiểm tra cả mặc lẫn tháo một món làm đổi món khác. Nhánh Equip nhân vật dùng GetEquipEnhance (server:1727, Coco:1339); một số nhánh đồng bạn dùng hằng 3 (server:1423, Coco:1091), không được suy rộng rằng mọi nhánh đều tính ngũ hành.

### 4. Nguồn nhận và nâng cấp

| Nhóm | Đường nhận tìm thấy tĩnh | Phạm vi đã chứng minh |
|---|---|---|
| Trang sức thường | `G:script/global/gucaxia.lua:626` gọi AddItem cho Detail 4/9/3; có các lệnh Particular lớn hơn bảng thường ở :614 | Có call site tạo đồ; chưa chứng minh NPC bật hoặc tất cả đối số hợp lệ với bộ bảng hiện tại. Không xem script hỗ trợ/GM là bảng rơi boss. |
| Mặt nạ | `G:Settings/item/004/mine.txt:264` gắn túi Particular=262 vào `script/mineitem/tuimatna_tongkim.lua`; script :2 kiểm chỗ 1×1, :7 gọi `AddItem(0,11,random(0,11),1,0,0)`, :8 đặt hạn 10080 phút | 12 lựa chọn số trong code; hạn 7 ngày theo đối số và API `SC:ScriptFuns.cpp:7471`. Chưa đo phân bố hay xác minh item thực nhận do bất nhất loader. |
| Phi phong vàng | `G:script/global/npcchucnang/hotrotanthu.lua:110` có menu 11 tên; :132 trở đi gọi AddGoldItem(3465…3475), truyền series=0, Level theo lựa chọn | Các ID này dùng bảng GoldItem; `GoldItem.txt:3467` là Lăng Vân, :3477 là Cao cấp. Mỗi ID ánh xạ dòng ID+2. API nhận ID tại `SC:ScriptFuns.cpp:8691`, gọi AddGold tại :8724; `SC:KItemSet.cpp:294`, `KItemGenerator.CPP:1454` lấy record theo index. |
| Phi phong hỗ trợ/GM khác | `G:script/global/npcchucnang/hotrotanthu_gm.lua:135` kiểm 4 ô rồi AddGoldItem một đối số; `G:script/mineitem/gmroleitem.lua:2402` có AddItem(0,12,0,14,…) | Chỉ là đường tạo hiện diện trong gói; không khẳng định đã phát hành. Biến thể một đối số mặc định Level=1 theo `SC:ScriptFuns.cpp:8698`, khác bản truyền Level. |
| Sức phẩm | `G:script/Utf8Script/npc/newplayer_get.lua:430` kiểm tên và task 140; :445 gọi AddItem(0,14,0,1,random(0,4),200,959,…), :448 SetAndSycItem | Có cơ chế nhận một lần theo byte task. Task được đánh dấu ở :443 trước AddItem, nên cần test nhánh hết chỗ/tạo thất bại; chưa xác minh NPC gọi hàm. |

**Nâng bậc phi phong:** [XÁC MINH] `G:script/global/npcchucnang/nangcapphiphong.lua` có kích thước **0 byte**, không có dòng code hay công thức. Menu nhận phi phong ở các file trên tạo món mới; không có bằng chứng chúng thu món cũ/nguyên liệu rồi nâng bậc. Chưa xác định recipe, chi phí, tỷ lệ thành công, thất bại hoặc trần nâng bậc riêng cho mặt nạ/sức phẩm/trang sức trong phạm vi file đã đọc.

**Cường hóa chung, tách khỏi Level/bậc:** [NGUỒN] `SC:ScriptFuns.cpp:10913` (`LuaSetItemEnChance`) cộng delta vào mức hiện tại rồi gọi EnChance, đồng bộ nếu đối số 3≥1. `SC:KItem.cpp:3800` và `C:gamecore/KItem.cpp:3515` có nhánh mới chặn 0…30, tính lại sáu **magic attr** đủ điều kiện từ backup bằng `JxQhScale`; nhánh này return trước công thức cũ. Nó không tăng trực tiếp các base attr của PiFeng.txt/Mask.txt. Hàm scale ở `SC:KItem.cpp:3795` tính `base + (base*5*N + dấu*50)/100`, có làm tròn số nguyên. Ví dụ attr dương 100 đủ điều kiện: +1→105, +10→150, +30→250 (suy ra số học, chưa chạy test).

[NGUỒN] Không thấy điều kiện loại item riêng trong nhánh EnChance mới; quyền đưa từng nhóm vào quy trình cường hóa vẫn phụ thuộc caller/UI. Thưởng +1/+2 tất cả kỹ năng tại +12/+15 được giới hạn **vũ khí** ở `SC:KItem.cpp:184`, không áp cho các nhóm của H-07. Không suy ra mọi món trang sức có thể được người chơi nâng cấp chỉ từ API chung.

### 5. Ngoại hình và đối chiếu Coco

| Nhóm | Quy tắc trong source | Bằng chứng server / Coco |
|---|---|---|
| Mặt nạ | Nếu không MaskLock: ưu tiên ItemResIdx>0; nếu không lấy BaseMagic (value[0] của base attr đầu). | SC:KItemList.cpp:1661 / C:gamecore/KItemList.cpp:1280; GetBaseMagic ở C:gamecore/KItem.h:388 |
| Phi phong | Ưu tiên ItemResIdx; vàng Level≤10 lấy Level; thường Level≤10 tra GetPifengRes(Particular,Level); Level>10 dùng Level%10. | SC:KItemList.cpp:1673 / C:gamecore/KItemList.cpp:1290 |
| Sức phẩm | ItemResIdx>0 ghi m_WeaponType, có khả năng thay ngoại hình vũ khí; không phải lớp trang sức độc lập trong nhánh này. | SC:KItemList.cpp:1704 / C:gamecore/KItemList.cpp:1318 |
| Nhẫn/dây chuyền/ngọc bội | Không có case đổi ngoại hình riêng trong switch Equip đã đọc; icon và chỉ số vẫn thuộc item. | Switch kết thúc SC:KItemList.cpp:1718 / C:gamecore/KItemList.cpp:1330 |

`SC:KItemChangeRes.cpp:91` tra phi phong ở dòng `Particular*10+Level+2`; đường dẫn `S:header/CoreUseNameDef.h:136` là `settings/item/PiFengRes.txt`. `G:Settings/item/PiFengRes.txt:3` ánh xạ Level 1→ResId 1; :12 ánh xạ 10→10. Nhưng Level 11 trong Equip dùng `%10`→1, **không lấy** ResId 11 ở :13 nếu không có override. Cần test riêng 10/11/12/14 và đồ vàng một/ba đối số.

Coco `C:gamecore/KNpcRes.cpp:1028` (`SetPifeng`) nạp các bộ phận 16–19 qua res node, có nhiều layer; điều kiện `nPifengType>0` ở :1050. Có lời gọi vẽ `EQ_PART_PIFENG` tại :961. Đây là bằng chứng có tuyến render, không chứng minh SPR tồn tại hay hình hiện đúng. Sync phi phong nhận `PifengType` ở `C:gamecore/KProtocolProcess.cpp:2989`, :3129. Sync mặt nạ gán `nMaskType` có điều kiện `!nIsShowSamePlayer` tại :2651, nên tester phải kiểm tra tùy chọn gom hiển thị nhân vật.

UI VN tạo checkbox mặt nạ tại `C:vn/gameui/KuiRoleStateVN.cpp:155`; callback :960 gọi ApplySetMaskLock(false) khi chọn, true khi bỏ chọn. Có tuyến ẩn/hiện mặt nạ, chưa xác minh tương tác runtime hoặc lưu trạng thái sau đăng nhập lại.

[XÁC MINH] So byte và SHA-256 giữa `C:` và `O:Classes/`: **8/8** file sau giống hoàn toàn: gamecore/KItem.h, GameDataDef.h, KItemList.cpp, KItemGenerator.CPP, KBasPropTbl.cpp, KItemChangeRes.cpp; gameui/KuiRoleState.cpp; vn/gameui/KuiRoleStateVN.cpp. Ví dụ KItemList.cpp chung SHA-256 `82fd49a0f14b426e78bf1bff5b157a05ff56c9c0bf97b7c6da76a7f16fb5d3ba`. Vì vậy các enum/UI, công thức record và lệch initializer trên cũng hiện diện ở bản gốc đã so.

`KNpcRes.cpp` **khác**: C SHA-256 `137974c9951cfcd9a546c98541ec65f18a657db220722bccaf86e8fd1a3e95c7`, O SHA-256 `dec54b5aafa12ebcc12a5bfb8f1a3564bf22c63ad23f0b1f046a9470bca2665c`; diff có camera, glow vũ khí và tối ưu render. `KItem.cpp` cũng có thay đổi: C EnChance:3515 có nhánh scale mới; O EnChance:3490 bắt đầu công thức cũ với CheckEnChance và phép dịch bit. Không khẳng định toàn bộ client giống bản gốc; cường hóa trên C và O có thể cho tooltip khác nếu dùng nhầm bản.

## CHƯA XÁC MINH

- Chưa chạy bất kỳ build, unit test, game, APK, server, VM, kết nối mạng hay test hành vi nào. Các phát hiện là static evidence.
- Chưa chứng minh source trùng binary server/APK đang vận hành hoặc gói Settings rời là bản được nạp ưu tiên. Chưa giải nén/so PAK chứa `update10/settings/item/004` và SPR.
- Chưa xác minh NPC/menu nhận đang được gắn lên map, túi mặt nạ rơi/mua ở đâu, rate boss/shop đầy đủ, xác suất random, thao tác nâng bậc riêng và chi phí/tỷ lệ/trần.
- Chưa xác minh tooltip, chỉ số combat thật, persist sau relog, timeout 7 ngày, đổi ngoại hình phía người chơi khác; không có ảnh hay log runtime.
- Chưa xác định hậu quả thực tế của Mask.txt không header và third slot kích hoạt Coco. Không tự sửa hai điểm này trong task khảo sát.

## Ca test bàn giao TESTER — tất cả CHƯA CHẠY

Chỉ thực hiện sau khi được giao task test riêng trong môi trường thử được phép. Dùng dữ liệu giả, ghi ID/Genre/Detail/Particular/Level/EnChance, item index hợp lệ, chỉ số trước/sau và nguồn file nạp; không dùng dữ liệu tài khoản thật.

| ID | Ca kiểm | Kỳ vọng/tiêu chí đối chiếu |
|---|---|---|
| H07-T01 | Mặc/tháo Detail 3/4/9/11/12/14; nhẫn thử cả hai ô và ô sai | Hai nhẫn dùng chung Detail=3; đúng ITEM_PART; ô sai bị từ chối; đầy túi không mất món. |
| H07-T02 | Trang sức Level 1/10, Particular 0/1, nhân vật hai giới, cấp dưới/đủ yêu cầu | Đối chiếu requirement 36/38 và chỉ số server/tooltip; không coi Level item là cấp nhân vật. |
| H07-T03 | Mặt nạ Particular 0,1,11,965,966; xác định file Mask thực nạp | Record/name/BaseMagic khớp hợp đồng; phát hiện bỏ dòng đầu/lệch tên hoặc vượt biên. Không dùng bản gốc làm expected mù quáng. |
| H07-T04 | Túi mặt nạ đủ/thiếu ô; lặp mẫu; ép thất bại tạo item bằng cơ chế test có sẵn | Chỉ tiêu túi sau nhận thành công, index>0 trước đặt hạn; lựa chọn trong 0…11; hạn 10080 phút và hết hạn đúng. Không suy rate từ một mẫu. |
| H07-T05 | Mặc/tháo nón tương sinh trong khi ring1/mask/pifeng/shiping đang dùng; lần lượt đổi nguồn thứ ba server | So số dòng ẩn active server/client; đặc biệt ring1 tránh đếm head hai lần. Ghi cả chỉ số combat và tooltip. |
| H07-T06 | Phi phong thường Level 1,10,11,12,14 và override ItemResIdx | Đối chiếu ResId 1,10,1,2,4 theo source khi không override; override phải được ưu tiên. |
| H07-T07 | AddGoldItem ID 3465…3475 qua menu một đối số và ba đối số | Đúng tên/ID; Level mặc định 1 khác Level truyền; không dùng số base của PiFeng.txt so cho đồ vàng. |
| H07-T08 | Checkbox mặt nạ bật/tắt, relog, xem từ người thứ hai, tùy chọn same-player | Ngoại hình/ẩn mặt nạ và trạng thái đồng bộ nhất quán; kiểm tra đánh/cưỡi ngựa/16 hướng. |
| H07-T09 | Shipin có/không ItemResIdx, thay vũ khí rồi tháo Shipin | Xác định chủ ý override m_WeaponType; tháo không để lưu hình vũ khí sai. |
| H07-T10 | Sức phẩm tân thủ: đúng/sai tên; task chưa/đã nhận; hết chỗ/tạo thất bại | Không mất quyền nhận do SetTask trước AddItem; nhận một lần; giữ nguyên item đã có. |
| H07-T11 | Nhánh nâng bậc phi phong từ NPC thật, kiểm tra đường dẫn script được gắn | File rỗng phải được ghi nhận là thiếu triển khai nếu là script được dùng; thu nguyên liệu/chi phí/thất bại chưa có expected đã chứng minh. |
| H07-T12 | Cường hóa món có base 85/89 và magic 85/89 riêng tại +0/+1/+10/+30, hạ cấp; so C với O | C scale magic đủ điều kiện từ backup, không scale base; không nhận thưởng kỹ năng vũ khí; ghi sai khác tooltip bản gốc/copy, không khẳng định PASS trước khi chạy. |

## Kiểm tra tĩnh đã thực hiện

- [XÁC MINH] Cwd/nhánh khớp task; lúc bắt đầu chỉ có task H-07.md là untracked, không có báo cáo H-07 cũ để ghi đè.
- [XÁC MINH] Trích enum, ánh xạ ô, loader, công thức record, apply attr, appearance, Lua API và các script nhận nêu trên bằng PowerShell/Python chỉ đọc.
- [XÁC MINH] Đếm sáu bảng, kiểm kích thước script nâng phi phong, so byte/SHA-256 tám file Coco và kiểm diff KNpcRes/KItem cần thiết.
- Báo cáo đã được ghi nháp trong cùng file trước khi hoàn thiện; không tạo parser/script phụ, không sửa source hoặc cấu hình.

## Lỗi công cụ và xử lý trong task

- `rg` không có sẵn (`The term 'rg' is not recognized`): dùng PowerShell và Python trực tiếp, không cài công cụ.
- Lần đọc đầu PowerShell dùng encoding mặc định làm sai dấu; các lần đọc tài liệu sau dùng UTF-8.
- Python xuất Unicode qua console cp1252 gặp `UnicodeEncodeError`; đã đặt `sys.stdout.reconfigure(encoding='utf-8')`, tiếp tục đọc được. Python luôn gọi `python -I`.
- Đường dẫn giả định `Core/Src/GameDataDef.h` không tồn tại; đã dùng header thật, không tạo file thay thế.
- Một lần tìm header dưới `gameserver/Sources/header` và một đường dẫn `header/KMagicAttrib.h` không tồn tại; đã tìm đúng `S:header/GameDataDef.h`, `SC:KMagicAttrib.h`. Không còn cản trở khảo sát.
- PowerShell Get-ChildItem kết hợp LiteralPath/Include trả danh sách rộng ngoài ý định, output bị cắt; đã chuyển sang Filter/Where-Object theo tên chính xác và trích trực tiếp. Không dùng output bị cắt để chứng minh thiếu file hay kết quả âm tính.
- Lưu Git: một lần `git add -- <hai file H-07>` thất bại với `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/H-07/index.lock': Permission denied`. Metadata Git của worktree nằm ngoài vùng được ghi. Không sửa quyền/config, không xóa lock, không thử bypass; báo cáo và task vẫn được lưu local.

## Trạng thái bàn giao và bước tiếp theo

**DONE (khảo sát tĩnh).** Không có blocker ngăn hoàn thành báo cáo. Các bất nhất và phạm vi chưa xác minh được tách rõ ở trên; bước tiếp theo là PM giao TESTER các ca H07-T01…T12, ưu tiên T03/T05 và xác định dữ liệu update10 thực nạp trước khi sửa mã.

Commit SHA: **không có — chưa commit**, do git add bị chặn quyền tạo index.lock nêu trên. **BỊ CHẶN – CHƯA PUSH**; không có link commit GitHub. Không gọi mạng theo yêu cầu user. PM có quyền ghi metadata Git có thể review rồi stage/commit đúng hai file H-07; không cần chạy lại khảo sát.
