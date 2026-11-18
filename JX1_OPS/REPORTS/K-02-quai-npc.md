TÓM TẮT 1/5: [NGUỒN] PARTIAL — đã kiểm kê tệp rời, chỉ mục gói server và đường đọc sprite quái/NPC ở client bản A.
TÓM TẮT 2/5: [NGUỒN] 2.412/2.435 mẫu server (99,06%) nối được tới bảng có đường dẫn SPR, cho 3.010 đường dẫn khác nhau.
TÓM TẮT 3/5: [NGUỒN] Client có 34 tên PAK được khai báo và 0 tệp PAK/SPR trong vùng quét. Không có ID khớp cho 3.010 đường dẫn SPR khi tra chỉ mục 4 PAK server.
TÓM TẮT 4/5: [CHƯA KIỂM] Chưa kiểm byte ảnh client, mục nén trong PAK server và quan hệ quái/NPC theo các bản đồ còn lại.
TÓM TẮT 5/5: [NGUỒN] Chỉ đọc dữ liệu và mã. Chưa chạy build, exe game, VM, mạng hoặc kiểm thử game. Tổng quan nhận tài liệu để commit.

# K-02b — Kiểm kê sprite quái và NPC

Loại: khảo sát\
Chủ đề: Kiểm kê sprite quái và NPC từ bảng ngoại hình, gói tài nguyên và mã đọc.\
Từ khóa: quái, NPC, sprite, SPR, PAK, NpcResType, 普通npc资源, Kiếm Môn Quan, K-02b\
Trạng thái: PARTIAL — thiếu tệp PAK/SPR của client bản A để xác minh ảnh.\
Độ phủ: đã đối chiếu 2.435/2.435 mẫu server, đọc chỉ mục 4/4 PAK server và kiểm mục NPC của 479/479 tệp vùng rời.\
Liên quan: [K-02](../TASKS/K-02.md), [K-03b](K-03b.md), [K-03c](K-03c.md), [Chuẩn báo cáo](../DESIGN/CHUAN-BAO-CAO.md).\
Cần tôi quyết định: không

```mermaid
flowchart LR
    M["MapList và tệp vùng"] -. "vùng rời map 995 thiếu mục NPC" .-> T["ID mẫu NPC"]
    T --> N["Npcs.txt → NpcResType"]
    N --> R["NpcRes → thư mục và tên theo động tác"]
    R --> S["Trình đọc SPR của client"]
    P["PAK khai báo ở client"] -. "vắng tệp trong vùng quét" .-> S
    S --> F["Bảng màu và khung hình"]
```

## Phạm vi và độ phủ

`G` là gốc dữ liệu server `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs`. `Q` là client bản A `D:/JX-build/qh9A`. Các dòng nguồn bên dưới tính từ 1 theo dòng vật lý. Đối với PAK/DAT, dẫn vị trí byte hoặc cấu trúc thay cho số dòng.

| Phần tử | Độ phủ | Dữ liệu và giới hạn |
|---|---|---|
| Tệp rời client bản A | Đã phủ các thư mục nguồn và tài nguyên liệt kê bên dưới | 0 SPR, 0 PAK, 0 WOR. Chưa kiểm tra bản cài hoặc hiện trạng thiết bị. |
| Khai báo gói client | Đã phủ 4/4 tệp INI liệt kê | 34 tên PAK khác nhau. `Q/Resources/package.ini:4–37`, `Q/data/data/package.ini:7–38` và hai `paklist.ini:2`. |
| Sprite rời và chỉ mục PAK server | Đã phủ các thư mục tài nguyên liệt kê và 4/4 PAK | 0 SPR rời, 88.875 mục chỉ mục. Tra 3.010 đường dẫn SPR, không có ID khớp. Chưa giải nén 88.823 mục có cờ nén. |
| Quái/động vật, `Kind=0` | Đã phủ 1.412/1.412 mẫu về tham chiếu | 1.407 nối tới bảng tên SPR, 5 thiếu khóa trong bảng loại. `G/Settings/Npcs.txt:1–2436`. |
| NPC đối thoại, `Kind=3` | Đã phủ 958/958 mẫu về tham chiếu | 953 có đường dẫn SPR, 4 thiếu khóa trong bảng loại, 1 ô khóa trống. Cùng nguồn trên. |
| NPC loại chim, `Kind=4` | Đã phủ 23/23 mẫu về tham chiếu | 23 có đường dẫn SPR. Cùng nguồn trên. |
| NPC loại chuột, `Kind=5` | Đã phủ 23/23 mẫu về tham chiếu | 12 có đường dẫn SPR, 11 thiếu khóa trong bảng loại. Cùng nguồn trên. |
| Mẫu có `Kind` trống | Đã phủ 19/19 mẫu về tham chiếu | 17 có đường dẫn SPR, 2 ô khóa trống. Giữ riêng nhóm trong bảng gốc. |
| Bản đồ và vị trí NPC | Đã phủ phần đầu mục NPC của 479/479 tệp vùng rời | 1/993 khóa trong `G/Settings/MapList.ini` khớp WOR rời tại ID 995. Tra chỉ mục PAK thấy ID WOR ứng viên cho 955/993 khóa. Chưa kiểm tra vị trí NPC trong gói hoặc do Lua tạo. |
| Định dạng và mã đọc | Đã phủ luồng chọn tên, mở PAK/SPR và lấy khung trong mã bản A | `Q/Classes/gamecore/KNpcResNode.cpp:420–465`, `Q/Classes/engine/KPakFile.cpp:37–125`, `Q/Classes/ImageStore/KImageStore2.cpp:253–289`. |
| Byte ảnh client | Chưa phủ | 0/3.010 đường dẫn tham chiếu server đã được đối chiếu với byte ảnh client. |

## Giải mã tên

Các dạng tên Hán bên dưới giữ tên tệp đúng như thấy trên đĩa, rồi đọc lại byte tên theo GBK. Ba tên trong dữ liệu Việt đã đối chiếu dạng gốc với bảng tra K-03. Các khóa kỹ thuật ASCII giữ nguyên.

| Tên gốc | Mã hóa | Chữ đúng UTF-8 | Nguồn file:dòng |
|---|---|---|---|
| `KiÕm M«n Quan` | TCVN3 | Kiếm Môn Quan (ID 995). Chữ Hán cho ID này chưa kiểm tra. | `G/Settings/MapList.ini:6684–6685` và [K-03c.tsv](_CHIMUC/K-03c.tsv). |
| `Tr­¬ng T«ng ChÝnh` | TCVN3 | Trương Tông Chính (张宗正), ID 511 | `G/Settings/Npcs.txt:513`, `G/Settings/Npcs_.txt:513` và [K-03b.tsv](_CHIMUC/K-03b.tsv). |
| `Tèng Quan viªn 1` | TCVN3 | Tống Quan viên 1 (南宋官员1), ID 47 | `G/Settings/Npcs.txt:49`, `G/Settings/Npcs_.txt:49` và [K-03b.tsv](_CHIMUC/K-03b.tsv). |
| `ÈËÎïÀàÐÍ.txt` | GBK | `人物类型.txt`, bảng loại ngoại hình | `G/Settings/NpcRes/ÈËÎïÀàÐÍ.txt:1`, `Q/Classes/gamecore/CoreUseNameDef.h:30`. |
| `ÆÕÍ¨npc×ÊÔ´.txt` | GBK | `普通npc资源.txt`, bảng tên sprite của nhóm ngoại hình thường | `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´.txt:1`, `Q/Classes/gamecore/CoreUseNameDef.h:41`. |
| `ÆÕÍ¨npc×ÊÔ´ÐÅÏ¢.txt` | GBK | `普通npc资源信息.txt`, bảng thông tin khung/hướng | `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´ÐÅÏ¢.txt:1`, `Q/Classes/gamecore/KNpcResNode.cpp:447`. |
| `enemy003`, `enemy003_st.spr`, `NormalStand1` | ASCII | `enemy003`, `enemy003_st.spr`, `NormalStand1` | `G/Settings/NpcRes/ÈËÎïÀàÐÍ.txt:4`, `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´.txt:1–2`. |

## Sắp theo cấu trúc game

- **Bản đồ 995 → vùng → vị trí quái/NPC.** Tên và đường dẫn khớp `G/Settings/MapList.ini:6684–6685`, trỏ tới `G/maps/fongkieu/kiem_mon_quan.wor:4`. Bản đồ này có 479 tệp `*_Region_C.dat` rời. Tất cả có mục NPC dài 0 byte khi đọc cấu trúc vùng. Chưa có bản ghi để gán mẫu NPC vào bản đồ này. Client ghép đường dẫn WOR từ khóa bản đồ ở `Q/Classes/gamescene/KScenePlaceC.cpp:583` và đọc hình chữ nhật vùng ở `:602`.
- **Chưa gán bản đồ → nhóm trong game → mẫu → ngoại hình → động tác.** Bảng phạm vi đi theo `Kind` của bảng server, đối chiếu định nghĩa ở `Q/Classes/gamecore/GameDataDef.h:363–370`. Ví dụ quái ID 511 và NPC đối thoại ID 47 cùng dùng khóa `enemy003`. Động tác đứng `NormalStand1` của khóa đó trỏ tới `\spr\npcres\enemy\enemy003\enemy003_st.spr`. Hai mẫu giữ ID riêng. Chưa kiểm tra chúng xuất hiện ở bản đồ nào. `G/Settings/Npcs.txt:49,513`, `G/Settings/NpcRes/ÈËÎïÀàÐÍ.txt:4`, `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´.txt:1–2`.

## Kiểm kê tệp và dung lượng

**[NGUỒN]** Đếm tệp rời theo phần mở rộng, gồm tệp ẩn trong phạm vi liệt kê. Dung lượng là tổng thuộc tính `Length` theo byte. PowerShell `Get-ChildItem -File -Recurse -Force` và `Measure-Object Length -Sum` chạy trên các thư mục tài nguyên. Số 0 chỉ áp dụng cho phần mở rộng, đường dẫn và lớp tệp được ghi trong bảng.

| Gốc và thư mục | Phần mở rộng | Số tệp | Byte | Ghi chú |
|---|---|---:|---:|---|
| Q/Resources | SPR / PAK / WOR | 0 / 0 / 0 | 0 / 0 / 0 | Gốc tài nguyên Android được khai báo ở `Q/proj.android/app/build.gradle:63`. |
| Q/data | SPR / PAK / WOR | 0 / 0 / 0 | 0 / 0 / 0 | `data/data` có cấu hình gói. |
| Q/Classes | SPR / PAK / WOR | 0 / 0 / 0 | 0 / 0 / 0 | Có mã đọc. |
| Q/proj.android, Q/proj.ios_mac, Q/L02 | SPR / PAK / WOR | 0 / 0 / 0 ở mỗi thư mục | 0 / 0 / 0 | Kiểm tên tệp rời, không mở gói cài đặt. |
| Q/cocos2d, Q/fmod, Q/Up testflight | SPR / PAK / WOR | 0 / 0 / 0 ở mỗi thư mục | 0 / 0 / 0 | Đối chiếu bổ sung tên tệp rời. |
| G/pak | PAK | 4 | 15.610.628 | Chỉ đọc đầu gói, chỉ mục và dấu đầu mục. |
| G/maps | WOR | 1 | 111 | `fongkieu/kiem_mon_quan.wor`. |
| G/maps | DAT | 479 | 2.551.187 | Tất cả là `*_Region_C.dat` cùng bản đồ 995. |
| G/pak, G/maps, G/Settings, G/script, G/Msg, G/TongSet, G/GameData, G/DataFiles | SPR | 0 | 0 | Đếm tệp rời. |
| G/gs.zip | ZIP | 1 | 9.158.622 | Đọc danh mục tên. Có 0 mục mang đuôi SPR, PAK hoặc WOR. |
| G/Settings/NpcRes | TXT / INI | 91 / 2 | 2.786.458 / 18.931 | Tổng thư mục có cả bảng ngoại hình ngoài nhóm quái/NPC. |
| G/Settings | TXT | 2 | 1.488.380 | `Npcs.txt` 753.810 byte và `Npcs_.txt` 734.570 byte. |
| G/Settings/vn | TXT | 1 | 20.147 | Riêng tệp `npc.txt`, đã đếm kích thước, chưa đối chiếu nội dung. |
| G/Settings/npc | TXT / INI | 10 / 4 | 36.393 / 910 | Đã đếm tệp đi kèm, ngoài phép nối ngoại hình. |
| G/Settings/maps | TXT | 518 | 1.046.612 | Đã đếm tệp đi kèm, chưa phân tích quan hệ xuất hiện. |

Không thấy SPR/PAK/WOR ngay tại gốc `G` hoặc `Q`. Các tệp cấu hình client có khai báo tên gói như sau.

| Tệp cấu hình | Byte | Tên PAK trong tệp | Tên có tệp trùng trong vùng quét | Dòng khai báo `spr.pak` |
|---|---:|---:|---:|---|
| `Q/Resources/package.ini` | 591 | 34 | 0 | `:24` |
| `Q/data/data/package.ini` | 661 | 32 | 0 | `:26` |
| `Q/Resources/paklist.ini` | 1.305 | 32 | 0 | `:50` |
| `Q/data/data/paklist.ini` | 1.305 | 32 | 0 | `:50` |

### Chỉ mục PAK server

**[NGUỒN]** Cả bốn gói có chữ ký `PACK`. Đọc số mục và độ dời chỉ mục kiểu little-endian, rồi duyệt bản ghi 16 byte có ID, độ dời, cỡ gốc và cờ/cỡ lưu. Cuối chỉ mục bằng cuối tệp ở cả bốn gói. Không có mục vượt giới hạn vùng dữ liệu khi tách 24 bit cỡ lưu theo mã đọc. `Q/Classes/engine/KbugInfo.h:273–291,313`, `Q/Classes/engine/XPackFile.cpp:94–125,439–447`.

| Gói vật lý | Byte | Mục | Mục có cờ nén | Dòng trong cấu hình G |
|---|---:|---:|---:|---|
| `G/pak/maps01.pak` | 626.551 | 706 | 706 | `G/package.ini:3` |
| `G/pak/maps.pak` | 14.542.936 | 87.245 | 87.193 | `G/package.ini:4` |
| `G/pak/script.pak` | 91.771 | 425 | 425 | `G/package.ini:8`, dòng chú thích |
| `G/pak/skill.pak` | 349.370 | 499 | 499 | Hiện diện vật lý |
| **Tổng** | **15.610.628** | **88.875** | **88.823** | |

Không thấy dấu `SPR\0` ngay đầu mục lưu, kể cả trong 52 mục không nén. Nội dung sau giải nén của 88.823 mục chưa kiểm tra. Chỉ mục lưu ID số nên số mục là số bản ghi PAK, còn phần mở rộng và nguồn gốc từng bản ghi nén chưa xác định. `Q/Classes/engine/KbugInfo.h:240,252,286–291`.

Đối chiếu 3.010 đường dẫn SPR của bảng mẫu bằng ID 32 bit trên cả bốn chỉ mục, không có ID khớp. Với 16 đường dẫn có byte ngoài ASCII, đã thử cả byte gốc và dạng đổi GBK sang UTF-8, với hai cách diễn giải byte có dấu và không dấu. Phép đối chứng trên 993 khóa đường dẫn WOR từ `MapList.ini` tìm thấy ID ứng viên cho 955 khóa, gồm 948 khớp ở `maps.pak` và 7 ở `maps01.pak`. Đây là kết quả tra ID theo các dạng đường dẫn đã thử. Chưa mở nội dung WOR nén để xác nhận tệp tương ứng. `Q/Classes/engine/KFilePath.cpp:282–298,484–495,567–590`, `Q/Classes/engine/KPakList.cpp:247–265`.

### Tỷ lệ hiểu dữ liệu

**[NGUỒN]** Đã đọc 2.435/2.435 dòng có STT trong `G/Settings/Npcs.txt:2–2436`. Nối `NpcResType` ở cột 13 với khóa ở cột đầu của bảng loại và bảng tên SPR. Có 2.412 dòng nối được tới khóa có ít nhất một ô `.spr`, tức `2.412 ÷ 2.435 × 100 = 99,06%`. Còn 20 dòng khóa có giá trị nhưng thiếu trong bảng loại và 3 dòng trống. Phép nối giữ nguyên giá trị trong tệp. Mã client có giá trị dự phòng khi đọc `NpcResType`. `G/Settings/Npcs.txt:1`, `Q/Classes/gamecore/KNpc.cpp:3897–3900`.

Đã đọc 982/982 hàng dữ liệu của bảng tên SPR. Có 8.077 ô kết thúc bằng `.spr` và cả 982 khóa ở đúng vị trí tương ứng trong bảng thông tin khung. Với các khóa được nối từ mẫu server, sau khi ghép thư mục với tên theo động tác và gộp đường dẫn trùng không phân biệt hoa thường, còn 3.010 đường dẫn. Số liệu chỉ đếm tham chiếu có trong bảng. Bóng `b.spr` do mã ghép tên chưa nằm trong phép đếm. `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´.txt:1–983`, `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´ÐÅÏ¢.txt:1–983`, `Q/Classes/gamecore/KNpcResNode.cpp:456–472,494–529,664`.

**[CHƯA KIỂM]** Độ phủ xác minh byte ảnh của client là 0/3.010 tham chiếu đối chiếu. Tổng số sprite quái/NPC trong bản phân phối client và tỷ lệ ảnh thực tế đọc được chưa đếm được vì thiếu gói trong cây dữ liệu bàn giao.

## Định dạng và mã đọc

| Bước | Mã đọc bản A | Nội dung đã xác minh tĩnh |
|---|---|---|
| Nạp mẫu và chọn khóa ngoại hình | `Q/Classes/gamecore/KCore.cpp:398`, `Q/Classes/gamecore/CoreUseNameDef.h:133`, `Q/Classes/gamecore/KNpcTemplate.cpp:24–37`, `Q/Classes/gamecore/KNpc.cpp:3897` | Nạp bảng `NpcS.txt`, tìm mẫu ở dòng `ID + 2` và đọc `NpcResType`. |
| Chọn đường dẫn theo động tác | `Q/Classes/gamecore/KNpcSet.cpp:603`, `Q/Classes/gamecore/KNpcRes.cpp:64–75,111–118`, `Q/Classes/gamecore/KNpcResNode.cpp:48–70,420–465` | Khởi tạo ngoại hình bằng khóa. Nhánh thường ghép một phần thân cơ sở từ thư mục và tên tệp theo động tác, đồng thời đọc tổng khung, số hướng và khoảng khung từ bảng. |
| Chọn gói và tìm mục | `Q/Classes/gamescene/KUpdateLayer.cpp:821–831`, `Q/Classes/engine/KPakList.cpp:136–184,247–265` | Mở `package.ini`, lấy tên gói theo khóa số. Chuẩn hóa đường dẫn, tra theo ID và có nhánh thử đổi GBK/UTF-8. |
| Mở SPR và đọc khung | `Q/Classes/engine/KPakFile.cpp:37–125`, `Q/Classes/engine/XPackFile.cpp:597–638,681–716`, `Q/Classes/ImageStore/KImageStore2.cpp:253–289,655–683` | Thử tra gói trước rồi có nhánh mở tệp. Đọc `SPRHEAD`, bảng màu 3 byte mỗi màu và bảng `SPROFFS`. Nhánh nén riêng từng khung dùng chỉ mục `XPackSprFrameInfo`. |
| Cấu trúc ảnh | `Q/Classes/engine/KbugInfo.h:238–269,299–303`, `Q/Classes/engine/XPackFile.cpp:300–344` | Đầu SPR chứa chiều rộng/cao, tâm, tổng khung, số màu, hướng và khoảng khung. `SPRFRAME` có cỡ khung, độ lệch và dữ liệu ảnh RLE. Mã đọc gói có các nhánh giải nén UCL. |
| Tham chiếu lúc vẽ và dữ liệu vùng | `Q/Classes/gamecore/KNpcRes.cpp:949–961`, `Q/Classes/gamescene/KgameWorld.cpp:11476,11537`, `Q/Classes/gamecore/KRegion.cpp:142–165,239–241` | Luồng vẽ chuyển tên và chỉ số khung cho hàm lấy texture. `Region_C.dat` có vị trí dành cho mục NPC, và `LoadClientNpc` trong mã hiện tại trả `FALSE` ngay đầu hàm. |

Trình đọc có sẵn trong mã client là `KPakList`, `XPackFile`, `SprGetHeader` và `KImageStore2`. Chưa thấy tiện ích SPR/PAK riêng theo tên trong các thư mục công cụ đã kiểm. Gốc server được giao có dữ liệu `gs`. Dẫn chứng về mã đọc ở trên lấy từ bản A. Phần hướng dẫn và Graphify chỉ dùng định vị, với mốc gốc `.` trong `Q/Classes/graphify-out/.graphify_root:1`.

## Mục sổ thông số

| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Mẫu | Dòng đọc ID | `Q/Classes/gamecore/KNpcTemplate.cpp:24` | `ID + 2` | dòng | Định vị mẫu | KHÔNG | Mã tĩnh |
| Ngoại hình | Giá trị dự phòng `NpcResType` | `Q/Classes/gamecore/KNpc.cpp:3897` | `enemy003` | khóa | Giá trị truyền vào khi đọc bảng | KHÔNG | Mặc định của mã |
| Động tác | Bộ `nTotalFrames,nTotalDirs,nInterval` | `Q/Classes/gamecore/KNpcResNode.cpp:458–465` | `16,8,0` | khung, hướng, khoảng khung | Dự phòng khi đọc thông tin động tác | KHÔNG | Mặc định của mã |
| Động tác | `enemy003 / NormalStand1` | `G/Settings/NpcRes/ÆÕÍ¨npc×ÊÔ´ÐÅÏ¢.txt:2` | `48,8,200` | khung, hướng, khoảng khung | Tham số mẫu của động tác đứng | KHÔNG | Giá trị bảng, đơn vị thời gian của số 200 chưa kiểm tra |
| Định dạng | Bảng màu SPR | `Q/Classes/engine/KPakFile.cpp:73,86` | tối đa 256 ở nhánh tệp rời, 3 byte/màu | màu, byte | Xác định vị trí chỉ mục khung | KHÔNG | Mã tĩnh |
| Gói | `MAX_PAK` | `Q/Classes/engine/KPakList.h:44` | 50 | gói | Giới hạn vòng đọc khóa số | KHÔNG | Hằng số mã |
| Bản đồ | `MAIN.rect` bản đồ 995 | `G/maps/fongkieu/kiem_mon_quan.wor:4` | `96,96,118,117` | tọa độ vùng | Phạm vi vùng của tệp WOR rời | KHÔNG | Đọc tĩnh INI, chưa kiểm chạy |

## Đã xác minh / Chưa xác minh

- **Đã xác minh.** Đếm tệp và dung lượng bằng PowerShell. Đọc chỉ mục 4 PAK và kiểm vị trí/cỡ mục bằng `BinaryReader` ở chế độ đọc. Phép kiểm tệp vùng dùng `count` đầu tệp và cặp `offset,length` ở mục NPC số 2. Mục này dài 0 ở cả 479 tệp. `Q/Classes/gamescene/SceneDataDef.h:20–35`, `Q/Classes/gamecore/KRegion.cpp:149–165`.
- **Đã xác minh.** Nối các bảng theo khóa ngoại hình, kiểm số dòng, cột động tác, đối chiếu hai tên mẫu với K-03b và kiểm tên bản đồ với K-03c. Đọc mã client theo các dòng trong bảng mã đọc.
- **Chưa xác minh.** Byte ảnh, giải nén/hiển thị khung, gói được nạp trên thiết bị, vị trí quái/NPC từ gói hoặc Lua, và hành vi runtime. Chưa chạy build, exe game/server, VM, mạng hoặc test game theo phạm vi chỉ đọc.
- **Lỗi và cách xử lý.** Máy không có `rg`. Đã tra bằng `Select-String` và `Get-ChildItem`. Một lệnh trích mã tra ID lấy quá dòng cuối, đã đối chiếu lại trong đoạn có thật và chạy phép đối chứng WOR. Quyền ghi giới hạn trong worktree, nên `D:/JX-wt/K-02b.nhip` chưa ghi được. Các mốc bắt đầu, kiểm đếm, đối chiếu và gần hoàn tất đã cập nhật trong trao đổi.

## Đề xuất tối ưu tra cứu

Dùng `template_id → NpcResType → thư mục + tệp theo động tác` làm khóa tra chung. Khi có bản sao gói của client bản A, ưu tiên đối chiếu một đường dẫn đã biết như `enemy003_st.spr` với chỉ mục và `SPRHEAD`, rồi mở rộng theo 3.010 tham chiếu. Với bản đồ, cần dữ liệu vị trí NPC có bản ghi để nối ID mẫu và map.

Hàng đề xuất cho `JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md`.

| Chủ đề | Báo cáo | File, hàm chính | Độ chắc |
|---|---|---|---|
| Sprite quái và NPC | `REPORTS/K-02b.md` | `Npcs.txt`, `NpcRes`, `KNpcResNode::Init`, `SprGetHeader` | Khảo sát tĩnh, chưa kiểm byte ảnh client |

## Bàn giao

Báo cáo và mục Kết quả đã để tại worktree để Tổng quan commit. Chưa có SHA và chưa push. Đường dẫn trong `vung_file` là [trang dẫn theo task](K-02-quai-npc.md). Hàng chỉ mục được gói trong báo cáo vì phạm vi ghi chỉ gồm các tệp giao trực tiếp.

```tsv
file	loại	chủ đề	từ khóa	trạng thái	độ phủ	liên quan
JX1_OPS/REPORTS/K-02b.md	khảo sát	Kiểm kê sprite quái và NPC	quái, NPC, sprite, SPR, PAK, NpcResType, 普通npc资源, Kiếm Môn Quan, K-02b	PARTIAL	2.435/2.435 mẫu đã tra, 2.412 có đường SPR, 4/4 PAK server đã đọc chỉ mục	K-02, K-03b, K-03c
```

Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report.
