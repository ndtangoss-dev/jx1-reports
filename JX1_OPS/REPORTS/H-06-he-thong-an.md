TÓM TẮT 5 DÒNG
1. [NGUỒN] Ấn là trang bị `equip_yinjian` (DetailType 13), có ô đeo riêng; server và Coco đều có mã hỗ trợ.
2. [NGUỒN] `Settings/item/004/YinJian.txt` chứa 13 dòng dữ liệu; đã thấy script cấp ấn tân thủ và ấn kích hoạt.
3. [NGUỒN] Server và Coco khác số liên kết kích hoạt ngũ hành; cần kiểm thử đối chiếu trước khi coi là tương đương.
4. [NGUỒN] Đã lần luồng cường hóa chung; chưa thấy công thức ghép nâng bậc ấn đáng tin cậy; dữ liệu/script có dấu hiệu khác phiên bản.
5. DONE trong phạm vi khảo sát tĩnh ngày 2026-11-17; chưa xác minh runtime/build/PAK; không sửa mã, không mạng/VM, không chạy game/server.

# H-06 — Hệ thống ấn

Loại: khảo sát
Chủ đề: Định nghĩa, dữ liệu, đeo, kích hoạt và cường hóa ấn giữa server và Coco.
Từ khóa: ấn, YinJian, equip_yinjian, DetailType 13, ngũ hành, DropZhiDingItem, cường hóa, Coco
Trạng thái: DONE — khảo sát tĩnh; chưa xác minh runtime, PAK hoặc binary đang dùng.
Độ phủ: đã liệt kê 7/7 phần tử; đối chiếu trực tiếp 4/7 tại root task, 0/12 ca đề xuất đã chạy.
Liên quan: H-05-ui-cuong-hoa.md; H-07-trang-suc-mat-na-phi-phong.md; H-09.md; DESIGN/MUC-LUC-TRI-THUC.md
Cần tôi quyết định: không

```mermaid
flowchart LR
  A[YinJian.txt] --> B[Loader và ItemGenerator]
  B --> C[Slot 13 / equip_yinjian]
  C --> D[Đeo và kích hoạt thuộc tính]
  D --> E[Cường hóa +N]
  E --> F[Đồng bộ client/server]
```

## Phạm vi và độ phủ

| Phần tử phạm vi | Độ phủ | Bằng chứng |
|---|---|---|
| Định nghĩa loại, slot và bảng YinJian | Đã phủ trực tiếp bảng; client enum đã kiểm | `G/Settings/item/004/YinJian.txt:1`; `D:/JX-build/qh9A/Classes/gamecore/KItem.h:67` |
| Nguồn nhận và script cấp ấn | Đã xác minh tĩnh tại gói được giao | `G/script/Utf8Script/npc/newplayer_get.lua:489`; `:506`; `:512` |
| Đeo/tháo và thuộc tính kích hoạt | Client A đối chiếu được; server C++ chưa có trong gói gs | `D:/JX-build/qh9A/Classes/gamecore/KItemList.cpp:1323`; `:1091` |
| Cường hóa +N và giới hạn | Script Lua trong gói; server C++ chưa có trong gói gs | `G/script/system/qianghua.lua:159`; `:170` |
| Ghép/nâng bậc và dữ liệu lệch | Giữ kết luận báo cáo cũ; chưa tái đối chiếu mã server trong root task | `H-06-he-thong-an.md:141` |
| Đối chiếu server/Coco và UI | Giữ nội dung báo cáo cũ; chưa tái đối chiếu server C++ trong root task | `H-06-he-thong-an.md:145` |
| Runtime, PAK, binary và ca test | Chưa phủ | `H-06-he-thong-an.md:186` |

## Phạm vi, cách đọc bằng chứng

- Trạng thái: **DONE — khảo sát tĩnh**, không phải xác nhận tính năng chạy được. Bản nháp đã được lưu trong cùng file trước khi hoàn thiện.
- Đúng worktree `D:\JX-wt\H-06`, nhánh `task/H-06`; H-06 có trong backlog dòng 89. File task có sẵn, chưa được Git theo dõi.
- Tiêu chí task: định nghĩa/nguồn nhận/đeo/nâng/ghép/thuộc tính/công thức/TXT/server/client/UI; đối chiếu Coco; bảng số liệu, `file:dòng`, ca test. Các điểm không chứng minh được được ghi ở mục CHƯA XÁC MINH.
- Bước tiếp theo cho PM/TESTER: xác nhận bộ dữ liệu thực sự được nạp và phiên bản API `DropZhiDingItem`, sau đó chạy T01–T12 trong môi trường thử được cấp quyền riêng.
- Công cụ: `rg` không có; dùng PowerShell và Python nội tuyến với `python -I`. Lần tìm đầu chứa ký tự Trung Quốc bị PowerShell đổi thành `?`, gây `re.error: nothing to repeat at position 0`; đã khắc phục bằng Unicode escape, không tạo script phụ.

## ĐÃ XÁC MINH

Các xác minh ở đây chỉ là đọc source/dữ liệu local, chưa là bằng chứng runtime.

- `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src\KItem.h:85`: enum `equip_yinjian` ở giá trị 13.
- `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src\KBasPropTbl.CPP:16`, `:39`: loader chỉ đến `\\settings\\item\\004` và `Yinjian.txt`.
- Bảng `YinJian.txt` có 14 dòng gồm header và 13 bản ghi, hai thuộc tính gốc 85 và 89.
- `D:\JX-source\client\Classes\gameui\KuiRoleState.cpp:59`: UI có ô `Signet`, `UIEP_YINJIAN`, kích thước 1×1, tọa độ 213,297 trong bảng layout.

### 1. Gốc nguồn và quy ước đường dẫn

| Ký hiệu | Đường dẫn tuyệt đối được đọc |
|---|---|
| S | `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src` |
| E | `D:\JX-source\server\jxOnline\gameserver\Sources\Engine\Src` |
| C | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client` |
| M | `D:\JX-source\client\Classes` |
| G | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs` |

`S/KItem.cpp:3800` đã có nhánh `[qh]` sửa công thức; vì vậy “bản gốc” trong báo cáo là **bộ nguồn/gói local được giao**, không phải khẳng định bản phát hành Kingsoft nguyên thủy. `C` chính là client Coco có trong Folder; không tìm được một client PC độc lập khác trong phạm vi task để dùng làm chuẩn thứ ba. `M` là bản nguồn tham chiếu: đã so byte tám file liên quan với `C/Classes`; `KItemList.cpp/.h`, `KGameglobalSet.cpp`, `KuiRoleState.cpp`, `KuiCompoundItem.cpp`, `KuiItem.cpp` giống; `KItem.cpp`, `KNpc.cpp` khác. Các kết luận khác biệt quan trọng bên dưới dùng trực tiếp **C**, không lấy M thay thế khi khác.

### 2. Ấn là gì, dữ liệu và chỉ số

- [NGUỒN] Đây là **trang bị**, `ItemGenre=0`, `DetailType=13`, `ParticularType=0`; ô đeo `itempart_yinjian=13`, độc lập mặt nạ 11, phi phong 12, trang sức 14. Căn cứ `S/KItem.h:85`, `C/Classes/gamecore/GameDataDef.h:211`, `:226`, `:1498` và `G/Settings/item/004/YinJian.txt:1`.
- [NGUỒN] Loader dùng tên `Yinjian.txt`, không dùng `signet.txt`: `S/KBasPropTbl.CPP:16`, `:39`, `:72`, `:160`, `:639`. `G/Settings/item/004/signet.txt:2` chỉ có một dòng tên áo tăng, hình áo 2×3 nhưng DetailType 13; không được coi đó là bảng ấn đang được loader trên chọn.
- [NGUỒN] `YinJian.txt` là TSV 53 cột, 13 bản ghi. Tất cả: 1×1, vật thể 37, giá 999, không xếp chồng, ngũ hành cột gốc 5, yêu cầu thuộc tính **36=magic_requirelevel, giá trị 10**. Hai thuộc tính gốc **85=magic_lifemax_v (sinh lực tối đa)** và **89=magic_manamax_v (nội lực tối đa)**. Đối chiếu enum `S/KMagicAttrib.h:6`, `:49`, `:100`, `:104` và mô tả bảng `G/Settings/item/004/magicattrib.txt:80`, `:83`. Giá 999 là dữ liệu bảng, chưa xác nhận giá giao dịch.
- Tên hiển thị trong bảng gốc bị trộn mã tiếng Việt; không sửa/chuẩn hóa đoán. Bảng `G/Settings/vn/YinJian.txt:2`–`:11` dùng `至尊印`, `:12` dùng `推广印鉴`, `:13` dùng `新手印鉴`, `:14` dùng `VIP印鉴`. Đây là nhãn trong bảng dịch, chưa chứng minh UI hiện các tên đó.

| Dòng YinJian.txt | Level lưu trong dòng | HP tối đa cộng | MP tối đa cộng | 基础兵甲值 | Hình |
|---:|---:|---:|---:|---:|---|
| 2 | 1 | 50–100 | 50–100 | 500 | `wuxingyin_1.spr` |
| 3 | 2 | 100–150 | 100–150 | 600 | `wuxingyin_2.spr` |
| 4 | 3 | 150–200 | 150–200 | 700 | `wuxingyin_2.spr` |
| 5 | 4 | 200–300 | 200–300 | 1000 | `wuxingyin_3.spr` |
| 6 | 5 | 300–500 | 300–500 | 1100 | `wuxingyin_3.spr` |
| 7 | **7** | 500–700 | 500–700 | 1200 | `tianziyuxi.spr` |
| 8 | **7** | 700–900 | 700–900 | 1300 | `tianziyuxi.spr` |
| 9 | 8 | 900–1100 | 900–1100 | 1400 | `tianziyuxi.spr` |
| 10 | 9 | 1100–1300 | 1100–1300 | 1600 | `tianziyuxi.spr` |
| 11 | 10 | 1300–1500 | 1300–1500 | 1700 | `tianziyuxi.spr` |
| 12 | 11 | 13000–15000 | 13000–15000 | 1800 | `tianziyuxi.spr` |
| 13 | 12 | 1000–1500 | 1000–1500 | 1900 | `tianziyuxi.spr` |
| 14 | 13 | 20000 | 20000 | 2000 | `tianziyuxi.spr` |

Hình đầu thuộc `\spr\item\script\`, hình `tianziyuxi` thuộc `\spr\item\`. Các dòng có `可熔炼属性数量=6`, `可熔炼纹钢品质=10`; đó là sức chứa/phẩm chất dữ liệu cho hệ luyện chung, **không phải** công thức “6 ấn ghép 1”. Header/loader: `S/KBasPropTbl.CPP:1401`–`:1405`.

**Bất thường dữ liệu:** thiếu Level 6, trùng Level 7 ở dòng 7/8; HP/MP không tăng đơn điệu ở Level 11→12. Generator lấy **chỉ số vị trí** `i=ParticularType*10+Level-1`, rồi `GetYinjianRecord(i)`, không tra cột Level: `S/KItemGenerator.CPP:2275`, `:2326`; `S/KBasPropTbl.CPP:95`, `:1420`. Với `(Particular=0,Level yêu cầu=6)` nó chọn dòng 7 chứa Level=7; yêu cầu Level 7 chọn dòng 8 cũng chứa Level=7. Đây là mâu thuẫn source/dữ liệu cần thử, chưa tự sửa hay kết luận chủ ý.

### 3. Nguồn nhận — phân biệt lệnh cấp thực sự và script có vẻ rơi ấn

| Nguồn local | Bằng chứng | Điều có thể kết luận |
|---|---|---|
| Quà/kích hoạt tân thủ | `G/script/Utf8Script/npc/newplayer_get.lua:479`, `:489`, `:506`, `:508`, `:512` | Kiểm tra tên nhân vật; kiểm tra byte 2 của Task 140; gọi `AddItem(0,13,0,2,random(0,4),200,1040,959,0,0,0,0,1,0,7,...)`; bind/sync khi index>0; ghi cờ đã nhận. Chưa xác nhận NPC gọi được từ game. |
| Bản script NPC cũ | `G/script/Á½ºþÇø/npc/ÐÂÊÖ½Ó´ý.lua:1126` | Có cùng lệnh cấp ấn Level 2. Không tính là hai lần thưởng độc lập khi chưa biết script nào được gán. |
| Ấn kích hoạt Level 10 | `G/script/item/ÒÆ¶¯»ØÊÕ.lua:147`, `:153`, `:155`; `G/script/Á½ºþÇø/°ÍÁêÏØ/npc/½ðÉ½ÕÆÃÅÈË.lua:178` | `AddItem(0,13,0,10,3,200,1205,1233,1245,0,0,0,1,0,7)`; script item dùng toàn bộ Task 140, đặt cờ **trước khi** biết AddItem thành công. |
| Script chết sự kiện | `G/script/deadth/»î¶¯/deadth.lua:1`, `:23`, `:57`, `:62` | Có lời gọi mang ý định rơi ấn, chọn một trong 30 mảng thuộc tính. **Không thể coi là nguồn rơi hợp lệ với source hiện có**, xem lệch API bên dưới. |
| GM | `G/script/item/gm.lua:4734`; `gm(¿ª·þ).lua:3499` | Có lệnh tương tự sự kiện, không chứng minh drop tự nhiên. |
| Script nhiệm vụ cũ | `G/script/Á½ºþÇø/npc/²Ø±¦Í¼ÈÎÎñ/Â·ÈË_¸µÀ×Êé.lua:48` | Có `DropItem(...,0,13,...)`; chưa lần hết API/gán NPC, không khẳng định tỷ lệ hay điều kiện thưởng. |

`AddItem` được đăng ký tại `S/ScriptFuns.cpp:25955`; tham số 1–6 là Genre/Detail/Particular/Level/Series/Luck (`:8995`), 7–12 là sáu **số dòng thuộc tính**, 13 stack, 14 cường hóa, 15 Point (`:9013`). Với Point=7, generator đọc trực tiếp số dòng TSV (`S/KItemGenerator.CPP:2428`, `:2449`). Chuỗi cấp: `LuaAddItem` → `ItemSet.AddOther` (`S/ScriptFuns.cpp:9054`) → `Gen_EquipmentRong` (`S/KItemSet.cpp:389`) → bảng ấn/thuộc tính. `LuaAddItem` kiểm tra chỗ trống, trả 0 nếu thất bại (`S/ScriptFuns.cpp:9092`).

**Rủi ro mất lượt nhận:** tân thủ ghi byte đã nhận ở `:512` kể cả khi `nIndex<=0`; script item ghi Task 140 trước cấp ở `:153`. Bằng chứng tĩnh về thứ tự thao tác; chưa thử hành trang đầy. Hai script dùng hai cách lưu cờ khác nhau trên Task 140, cần kiểm tra ảnh hưởng chéo.

**Lệch API drop nghiêm trọng:** source `S/ScriptFuns.cpp:9646` yêu cầu **tham số 1 là NPC index >0**, tham số 2 Genre, 3 Detail, 4 Particular, 5 Rate, 6/7 Min/MaxLevel; các script sự kiện/GM trên lại bắt đầu `DropZhiDingItem(0,13,0,500,...)` theo API cũ trong comment. Nếu chạy đúng source này, `:9658`–`:9662` trả 0 ngay; không thể lấy `500` làm tỷ lệ rơi thực tế. Tham số `nRate` trong source cũng chỉ kiểm tra khác 0 (`:9740`), không thấy truyền vào `GiveZhiDingItem` ở `:9753`. Chưa biết exe gói dùng API cũ hay mới.

**Không nhầm “signet” khác hệ:** `G/script/battles/bossdeath.lua:1` include `script/global/signet_head.lua` (không có file rời ở vị trí này), nhưng `:18` thả item **Genre 6, Detail 1, Particular 1094**, không phải `0/13/0`; `SIGNET_DROPCOUNT=4` không phải bằng chứng boss rơi bốn ấn đeo.

### 4. Đeo/tháo, dòng hiện/ẩn, kích hoạt

- Mapping loại 13 → slot 13: `S/KItemList.cpp:2504`, `:2580`; Coco tương ứng `C/Classes/gamecore/KItemList.cpp:1892`, `:1968`. `CanEquip` duyệt yêu cầu, kiểm tra Level tại `S/KItemList.cpp:1183`, `:1253`; bảng ấn yêu cầu nhân vật Level 10, không phải Level của món.
- `Equip` ghi vị trí, tính `GetEquipEnhance`, áp thuộc tính khi `GetIsCanUse()==1`, cập nhật người chơi: `S/KItemList.cpp:1525`, `:1722`, `:1727`, `:1755`, `:1782`. Tháo gọi `RemoveMagicAttribFromNPC`, cập nhật vật liên quan (`:2094`, `:2114`). Khi `ItemResIdx>0`, ấn có thể ghi đè `m_ArmorType` (`:1710`); tháo ấn khôi phục ngoại hình áo (`:2178`). Chưa có bằng chứng ấn ở bảng hiện tại luôn có ngoại hình thay thế.
- Thuộc tính gốc luôn được áp; sáu dòng phép có index 0/2/4 áp trực tiếp, 1/3/5 cần lượt kích hoạt, mỗi lượt tiêu hao một: `S/KItem.cpp:140`, `:148`, `:159`. Không gọi mọi dòng ấn là “ngũ hành công/kháng”; dữ liệu gốc đang là HP/MP, dòng phép tùy bảng tham chiếu.
- Công thức kích hoạt chung: `nActive=min(3, I[ngũ hành nhân vật sinh ngũ hành món] + Σ I[món ở slot kích hoạt có hệ tương sinh])`, `S/KItemList.cpp:2674`–`:2706`. Đây là số dòng phép ẩn được mở, không phải cấp cường hóa.
- Server: ấn **được kích hoạt bởi phi phong, trang sức, áo** (`S/KItemList.cpp:69`) và **kích hoạt mặt nạ, ngựa, trang sức** (`:49`). Coco chỉ khởi tạo hai slot đầu của mỗi hàng (`C/Classes/gamecore/KItemList.cpp:46`, `:66`), trong khi `MAX_ITEM_ACTIVE=3` (`KItemList.h:6`). Theo quy tắc C++ phần tử thứ ba =0, tức `itempart_head`; vòng tính vẫn duyệt ba (`KItemList.cpp:2062`). Vì vậy Coco có thể dùng **nón** thay cho **áo** khi tính kích hoạt ấn; phải kiểm runtime, không chỉ nói “thiếu liên kết thứ ba”.
- Toàn thân: `magic_alljihuo_v` cộng `m_CurrentAllJiHuo` (`S/KNpcAttribModify.cpp:199`, `:3154`). Server nhánh đồ xanh cần cờ >0 và kiểm slot theo `nEquipAllActive` (`S/KItemList.cpp:9625`); không phải cứ đeo bất kỳ ấn nào là kích toàn bộ. Config rời `G/Settings/gamesetting.ini:60` đặt EquipAllActive=13, GoldAllActive=14. Coco **đảo hai biến**: đồ xanh đọc `nGoldAllActive` (`C/Classes/gamecore/KItemList.cpp:4770`), đồ vàng đọc `nEquipAllActive` (`:4784`), khác server `:9629`, `:9648`.

### 5. Nâng, ghép và công thức — điều có thật trong source

**Cường hóa +N dùng hệ chung:** không thấy cấm riêng DetailType 13 trong `S/KItemList.cpp:5393`; điều kiện là trang bị xanh/tím/vàng (`:5397`). `G/script/system/qianghua.lua:99` phân loại đồ xanh, chọn đá Detail 403/404/405 (`:88`), gọi `ItemQiangHua` (`:160`–`:165`), kiểm 200000 tiền (`:26`) và `Pay(200000)` **sau lời gọi**, không kiểm `nGong>0` (`:170`). Đường xử lý: `S/KProtocolProcess.cpp:9318` → Lua `sysqianghua` → đăng ký `S/ScriptFuns.cpp:26835` → `KItemList::QiangHua`.

| Công thức/giới hạn | Bằng chứng | Ý nghĩa và giới hạn |
|---|---|---|
| Bản ghi nền `i=Particular*10+Level-1` | `S/KItemGenerator.CPP:2275`, `:2326` | Lấy theo thứ tự dòng, có bất thường Level nêu trên. |
| Base HP/MP chọn `GetRandomNumber(min,max)` | `S/KItem.cpp:524`, `:534` | Chưa xác nhận hàm RNG lấy cận cuối inclusive/exclusive. |
| Point=7 lấy sáu row index và random từng min/max | `S/KItemGenerator.CPP:2428`, `:2449`, `:2454` | Không mặc định các ID 1040/959 là enum chỉ số; đó là dòng trong bảng. |
| `N=clamp(N,0,30)`; `v=base+(base*5*N+(base>=0?50:-50))/100` với chia số nguyên C++ | `S/KItem.cpp:3782`, `:3795`, `:3800` | Nhánh `[qh]` hiện tại, áp các loại trong whitelist vào **m_aryMagicAttrib**; không tự nhân base HP/MP trong `m_aryBaseAttrib`. Ví dụ phép HP base 100, N=5 →125. |
| Coco cũ lặp `v += v>>2`; nếu phần dư của v sau cập nhật >2 thì +1 | `C/Classes/gamecore/KItem.cpp:3490`, `:3503`; `KItem.h:37` | Chỉ loại được `CheckEnChance("ForBitEn",type)` cho phép và giá trị hiện tại ≥4; khác nhánh server tuyến tính 5%. Không coi Coco đã đồng bộ công thức. |
| Trần thực hiện +N đọc `QiangHuaRank[2]`; thất bại nếu `N>=2 && g_Random(A+rank)<g_Random(B)` | `S/KItemList.cpp:5427`, `:5441` | N<2 không vào nhánh thất bại; khi 2≤N<QiangHuaSet, trừ 2 rồi áp N+1 (giảm ròng 1); khi N≥ngưỡng, có nhánh giữ cấp và mất đá. |
| Config rời: gamesetting `20000,40000,5`, gs001 `1000,2000,5`; QiangHuaSet=10 | `G/Settings/gamesetting.ini:460`, `:462`; `gamesetting_gs001.ini:478`, `:480` | Cả hai trần +5, chưa xác nhận file thực sự được server nạp. Không gán tỷ lệ % từ so sánh hai RNG. |

Không cộng +1/+2 mọi kỹ năng cho ấn ở +12/+15: nhánh này chỉ vũ khí cận/xa (`S/KItem.cpp:184`). Có `EnChanceRong` và `EnChanceBao` riêng; không khái quát công thức `[qh]` cho mọi dạng luyện/khảm.

**Ghép/nâng bậc ấn:** chưa tìm thấy recipe “N ấn thấp → 1 ấn cao”, chi phí hoặc xác suất riêng đáng tin cậy trong các script có 0/13/0 và bảng ghép đã đọc. `KuiCompoundItem` có ghép/tách/rèn/khảm/đồ phổ chung (`C/Classes/gameui/KuiCompoundItem.cpp:1029`, `:1064`, `:1085`, `:1104`, `:1128`). Trang HECHENG_A chỉ nhận Detail 3/4/9 (`:1480`, `:1491`, `:1502`), **không nhận ấn 13 ở trang này**; không suy ra mọi trang đều cấm ấn.

`G/Settings/item/other_compound.txt:2` liệt kê loại 0–14 cho ô lớn, nên cũng không được nói UI luyện chung hoàn toàn không biết ấn. Hai bảng `Settings/item/004/atlas_compound.txt` (204 dòng) và `Settings/item/atlas_compound.txt` (154 dòng) có đúng một row `DES_DETAILTYPE=13` ở **dòng 14**, nhưng tên kết quả là **四空之护法腰带 (đai)**, `DES_PARTICULAR`, `DES_LEVEL`, `DES_SERIES` trống. Đây là row **mâu thuẫn tên/loại**, không đủ để công bố recipe ấn. Sự hiện diện 13 cấp trong YinJian cũng không chứng minh tồn tại luồng nâng liên tiếp.

**Công thức “ngũ hành ấn” không được nhận nhầm:** `S/KGameglobalSet.h:77` và `KGameglobalSet.cpp:196` khai báo/nạp SeriesTrimMax/Param1–5. Tham chiếu tính toán tìm được nằm trong **comment của `KNpc_backup.cpp:5165`, `:5180`, `:5217`**, không phải bằng chứng công thức chạy. `S/KNpc.cpp:5100` hiện tính ngũ hành theo cặp attacker→defender `(0,1),(1,4),(2,3),(3,0),(4,2)`, trừ `nSeriesDamage` vào kháng rồi cộng/giới hạn kháng loại (`:5156`); `:6206` chỉ chép thuộc tính kỹ năng `magic_seriesdamage_p`. Coco lại cộng `m_CurrentSerisesEnhance` cho bIsPhysical tại `C/Classes/gamecore/KNpc.cpp:3243`–`:3251`. Chưa chứng minh HP/MP của ấn hiện tại đóng góp vào công thức ngũ hành đó.

### 6. Dữ liệu thiếu/lệch và phần Coco hiện có

| Hạng mục | Có trong Coco/source | Thiếu/lệch đã thấy hoặc cần xác minh |
|---|---|---|
| Loại, slot, bảng ấn | `C/Classes/gamecore/KItem.h:67`; `KBasPropTbl.CPP:39`, `:662`; `GameDataDef.h:1498` | Có mã nền, chưa chứng minh dữ liệu client được nạp thành công. |
| Ô nhân vật và xem người khác | `C/Classes/gameui/KuiRoleState.cpp:59`; `KuiViewRoleState.cpp:56`; `KgameWorld.cpp:2714`, `:14125` | Không phải thiếu hoàn toàn UI ấn. Chưa kiểm ảnh, chạm, màn hình VN thực tế. |
| Hiển thị/tooltip/cập nhật | `KuiRoleState.cpp:2213`, `:2351`, `:2991`; `KItem.cpp:1852` | Dùng item description chung; chưa thấy cửa sổ nâng ấn chuyên biệt trong phạm vi tìm. |
| So sánh ấn đang đeo | `C/Classes/gameui/KuiItem.cpp:1517`; `KuiItem_New.cpp:633` | Có mapping, chưa chạy thao tác. |
| Đồng bộ item chung | `C/Classes/gamecore/KProtocolProcess.cpp:1707`, `:1714`, `:1730`, `:1734`, `:1736` | Nhận Detail/Level/seed/sáu dòng phép/+N; không thấy cần packet riêng chỉ để biểu diễn ấn. Chưa kiểm tương thích byte với exe. |
| Kích hoạt theo slot | `KItemList.cpp:46`, `:66`, `:2062` | Phần tử 3 bằng 0 thay slot thứ ba của server. |
| Kích hoạt toàn thân | `KItemList.cpp:4770`, `:4784` | Hai biến config bị đảo so với server. |
| Cường hóa | `KItem.cpp:3490` | Công thức Coco canonical cũ khác nhánh `[qh]` trong server tham chiếu. |
| Thuộc tính phát ấn | Script Point=7, row 959/1040/1205/1233/1245 | **Bảng rời đúng đường dẫn macro chỉ 370 dòng**: không đủ các row đó. `S/KItem.h:39`, `S/KItemGenerator.CPP:2449`; `E/KTabFile.cpp:393`, `:856` cho thấy đọc vượt bảng thất bại và dùng default, nên có nguy cơ mất dòng phép nếu đúng bảng này được nạp. |
| Ảnh và TXT client | Tìm tên YinJian/Signet/wuxingyin/tianziyuxi và .pak trong `C/data`, `C/Resources`: không thấy file rời/PAK tương ứng | Chưa khảo sát nơi tải dữ liệu ngoài hai cây này; không kết luận asset vắng khỏi toàn máy hay thiếu trong bản cài chạy. Không mở cấu hình tài khoản. |

Hash định danh hai bảng đã đọc (để PM so với bản nạp; không phải hash exe):

| File dưới G | Số dòng vật lý theo splitlines | SHA-256 |
|---|---:|---|
| `Settings/item/004/YinJian.txt` | 14 | `d141ac617a22bf84adeebb7a7dcdd41f29dc166d02f1639ea87c525096e310c9` |
| `Settings/item/004/magicattrib.txt` | 370 | `7df578b0999a7fca8722f62df4cfeabb3aba9667f078bfb431c151903b827938` |

## Ca test cho TESTER (đề xuất, CHƯA CHẠY)

Chỉ chạy sau khi có quyền môi trường thử riêng; không dùng dữ liệu thật. Giữ bằng chứng item ID/row/config, HP/MP trước–sau, ảnh tooltip và log đã lọc; không ghi tài khoản/IP/khóa. Các kết quả dưới là điều cần kiểm tra, không phải PASS đã đạt.

| ID | Thao tác | Tiêu chí kiểm/điểm cần phân xử |
|---|---|---|
| T01 | Định danh dữ liệu nạp, API drop, hash bản server/client test | Khớp đúng TXT/PAK và source hay ghi rõ phiên bản khác; xác nhận row phép >370 có tồn tại trong dữ liệu nạp. Đây là điều kiện trước các ca khác. |
| T02 | Cấp ấn 0/13/0 Level 1,2,5,6,7,10,11,12,13 qua công cụ thử được duyệt | Đúng slot/1×1/tên/hình; ghi row thực tế, HP/MP trong khoảng bảng; đặc biệt 6/7 và bước 11→12. Không lấy Level cột làm mặc định khóa tra. |
| T03 | Nhân vật Level 9 và 10 đeo/tháo ấn | Level 9 bị yêu cầu 10 chặn; Level 10 đeo được khi điều kiện khác đủ; đúng slot, HP/MP cộng/trừ đúng, tháo không cộng lặp, ngoại hình áo được khôi phục nếu ấn có ItemResIdx. |
| T04 | Quà tân thủ lần đầu/lần hai; hành trang đầy; sai tên; AddItem trả 0 | Không mất lượt khi cấp thất bại là tiêu chí mong muốn; source có nguy cơ vẫn ghi cờ. Kiểm byte 2 Task 140 và tương tác với script ghi cả Task. |
| T05 | Ấn có 6 dòng phép đã biết; bật/tắt từng nguồn tương sinh nhân vật/phi phong/trang sức/áo/nón | So số dòng ẩn và chỉ số server/Coco; nón không được thay áo chỉ vì ô thứ ba mặc định 0. Ghi bất đồng, không tự sửa kỳ vọng theo client. |
| T06 | Ấn xanh có/không alljihuo, thay riêng slot 13/14; đồ vàng tương ứng | Xác nhận điều kiện cờ >0; phát hiện việc Coco đảo nEquipAllActive/nGoldAllActive; tháo không để lại chỉ số. |
| T07 | Kích hoạt drop sự kiện/GM bằng harness được duyệt, không sửa source production | Kiểm chữ ký NPC index; lời gọi bắt đầu 0 có bị trả 0 như source không; không gọi “rate=500” khi chưa giải thích khác phiên bản. |
| T08 | Cường hóa ấn xanh thường +0→+1→+2→+5; thiếu/đúng đá 403/404/405; chạm trần | Ghi tiền/đá/+N trước–sau, không tăng Level món do nhầm với +N; kiểm phí khi nGong=0; config +5 không bị UI cho vượt. |
| T09 | Cùng ấn seed cố định, một dòng phép HP=100, +0 và +5; đăng nhập lại/tháo đeo | Server `[qh]` phép HP 125 tại +5, base HP không bị nhân chung; so tooltip Coco cũ. Ghi khác biệt EnChanceRong nếu là đồ đã luyện/định danh. |
| T10 | Mở từng tab ghép/tách/rèn/khảm/đồ phổ; thử đặt ấn | HECHENG_A phải từ chối 13 theo source; các tab khác theo bảng thật. Row đồ phổ tên đai nhưng Detail13 phải bị phân xử trước khi thử tiêu hao. Chưa có recipe nâng bậc ấn để đặt kỳ vọng thành công. |
| T11 | Xem người khác, tooltip, thay ấn nhanh, mở/đóng UI, bản VN, relog | Icon/tên/dòng hiện–ẩn và item ID nhất quán; không nhân bản, mất item hoặc dư thuộc tính; kiểm nhận packet item chung. |
| T12 | Nếu sản phẩm yêu cầu công/kháng ngũ hành ấn: đấu thử các cặp hệ, giữ kỹ năng/kháng cố định, chỉ đổi ấn | Đo server quyết định sát thương; xác định có tiêu thụ SerisesEnhance/SeriesTrim thật hay chỉ comment/hiển thị Coco. Không dùng riêng tooltip để chứng minh công thức. |

## CHƯA XÁC MINH

- Chưa chạy build/test/runtime theo giới hạn task.
- Chưa chứng minh server exe khớp source; chưa kiểm tra PAK client hoặc UI hiển thị thực tế.
- Chưa kết luận công thức trong file backup/comment là logic đang chạy.
- Chưa xác nhận nơi gọi/gán NPC của từng script nhận, tỷ lệ rơi tự nhiên, cửa hàng, sự kiện đang mở; API rơi ấn khác source là blocker đối với kết luận runtime.
- Chưa xác nhận bộ nạp chọn TXT rời hay dữ liệu đóng gói, file gamesetting nào có hiệu lực; chưa giải mã/mở PAK ngoài phạm vi đã đọc.
- Chưa có bằng chứng recipe nâng cấp ấn theo bậc, tỷ lệ thành công, nguyên liệu/chi phí riêng. Các bảng/ảnh/logic riêng của một phiên bản thương mại khác không được suy diễn vào bản local.
- Chưa sửa bất kỳ lỗi nghi vấn nào; cần task sửa riêng sau review L3 của PM. Ưu tiên: dữ liệu phép/API drop → kích hoạt slot/config → đồng bộ công thức/+N/UI.

## Kiểm tra và lỗi công cụ trong task

- Đã đọc source và TSV/INI/Lua bằng công cụ đọc local; các lệnh Python đều dùng `python -I`, chạy nội tuyến, không tạo parser/script file phụ. Có đếm dòng, so byte các file Coco liên quan, xác nhận row/column bằng header và SHA-256 hai bảng.
- `rg` không được nhận diện (`The term 'rg' is not recognized...`); chuyển PowerShell/Python, không cài công cụ. Hai lệnh độc lập ban đầu cùng gặp lỗi này, không tiếp tục thử rg.
- Một lần tìm bằng ký tự Trung Quốc trong pipe PowerShell gây `re.error: nothing to repeat at position 0`; đổi Unicode escape `\u5370`, đọc lại thành công. Chuỗi văn bản cũ có trộn mã; giữ nguyên tên file và chỉ báo cáo giá trị số/identifier chắc chắn, không sửa dữ liệu.
- Build/test/runtime: **không chạy theo yêu cầu**. Không truy cập mạng thật, VM, không chạy exe game/server hay tool gói; không đọc dump/SQL/log người dùng, không ghi bí mật. Không kiểm thử bằng UI hay MessageBox.

## Lưu Git

- **Chưa commit, không có commit SHA**: `git add -- JX1_OPS/TASKS/H-06.md JX1_OPS/REPORTS/H-06-he-thong-an.md` thất bại với `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/H-06/index.lock': Permission denied`. Metadata worktree nằm ngoài vùng được ghi; không sửa quyền, không vượt sandbox, không thử lặp. Hai file kết quả còn nguyên trong worktree.
- **BỊ CHẶN – CHƯA PUSH**: chưa có commit và task cấm mạng; không thử kết nối/đổi credential. Bước lưu tiếp theo cho PM ở phiên có quyền Git: review hai file, stage/commit với tiền tố H-06; chỉ push khi được cấp phạm vi mạng riêng.

## Phát hiện khi chuẩn hóa

- Báo cáo thiếu tiêu đề chuẩn, khối thông tin, sơ đồ Mermaid, bảng phạm vi và mục phát hiện chuẩn hóa. Đã thêm tiêu đề và cấu trúc; tóm tắt, số liệu, phát hiện và kết luận trước đó được giữ nguyên.
