TÓM TẮT 1/5 — A-17: đã khảo sát tĩnh dữ liệu gốc, mã server và client gốc; trạng thái hoàn tất khảo sát: DONE.
TÓM TẮT 2/5 — Có 201 INI rơi đồ, 194 có Count > 0; 59 đường dẫn chứa BOSS, không tương đương số boss hoạt động.
TÓM TẮT 3/5 — Npcs.txt có 2.435 mục; loader bỏ qua DropRateFile; boss_tieu truyền .lua vào hàm chỉ nhận .ini.
TÓM TẮT 4/5 — 15 bảng trang bị thường có 2.235 mục; tách cấp vật phẩm, điều kiện cấp nhân vật và giới 0 nam/1 nữ.
TÓM TẮT 5/5 — Chỉ đọc dữ liệu/source; không chạy game, build, mạng hoặc VM; chưa kiểm chứng runtime.

# A-17 — Rơi đồ boss và trang bị theo cấp/giới

Trạng thái: **DONE — hoàn tất phạm vi khảo sát tĩnh**, không xác nhận chức năng runtime. Ngày khảo sát: 17/11/2026. Tiếp tục từ báo cáo nháp có sẵn; các ghi nhận ban đầu được giữ và bổ sung bằng đối chiếu dưới đây.

## ĐÃ XÁC MINH

- Nhánh `task/A-17`, worktree `D:\JX-wt\A-17` đúng task; file task đã có sẵn ở trạng thái untracked, giữ nguyên nội dung gốc.
- `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src\KNpcTemplate.cpp:138` đọc Main.Count; dòng 192–198 nạp section 1..Count.
- `KNpc.cpp:12897` là hàm LoseSingleItem hiện hành; phiên bản phía trước tại dòng 12449 nằm trong block comment, không dùng làm bằng chứng hành vi hiện hành.
- `KItemList.cpp:1253` kiểm tra cấp nhân vật; dòng 1275 kiểm tra giới tính bằng phép so sánh bằng.

## CHƯA XÁC MINH

- Source có khớp binary và dữ liệu đang triển khai hay không; bảng nào được boss đang chạy sử dụng.
- Kết quả rơi đồ thực tế, tỉ lệ runtime, thao tác mặc trang bị và hiển thị trên client.

## Nguồn và phương pháp đếm

Chỉ đọc ZIP bằng thư viện chuẩn `zipfile`, đọc source và xử lý số/cột tab trong bộ nhớ qua `python -I`; không giải nén hay ghi vào nguồn gốc, không tạo script phụ. Không đọc cấu hình kết nối, không chạy binary, build, game, VM hay mạng. Chỉ ghi báo cáo này và phần kết quả mà task yêu cầu ở cuối `JX1_OPS/TASKS/A-17.md`.

Để dẫn nguồn ngắn gọn, các tiền tố sau được dùng trong toàn báo cáo. `:dòng` là dòng vật lý, bắt đầu từ 1; `!` chỉ một entry nằm trong ZIP, không phải đường dẫn đã giải nén.

| Tiền tố | Đường dẫn cục bộ được khảo sát |
|---|---|
| `S/` | `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src\` |
| `ZS/` | `D:\AI_JX1\02_Source_Working\Source Jx1m Cocos V3 full\File\Folder\ServerNew-20260116T043145Z-3-001.zip!ServerNew/_bin_v2_/gs/` |
| `ZC/` | `D:\AI_JX1\02_Source_Working\Source Jx1m Cocos V3 full\File\Folder\Client2912-20260116T044348Z-3-001.zip!Client2912/Client/` |

Đếm mục bảng tab bằng các dòng không rỗng trừ một dòng tiêu đề. Phân tích điều kiện bằng các cột vị trí, không dựa vào tên tiếng Trung bị lỗi mã hóa: cột 12 là cấp vật phẩm; cột 35–46 là sáu cặp loại/giá trị điều kiện. Đối chiếu với `S/KBasPropTbl.CPP:1364`, `:1388`, `:1399`. Các số này là số bản ghi, không phải số vật phẩm độc nhất sau khi sinh thuộc tính. Tên entry ZIP không ASCII được giữ theo tên do `zipfile` trả về; không tự đổi encoding của đường dẫn.

## Bảng rơi đồ boss

### Số lượng và cách gắn bảng

| Phạm vi | Kết quả tĩnh | Cách hiểu |
|---|---:|---|
| `ZS/Settings/droprate/**/*.ini` | 201 file | Bao gồm bảng thường, boss và sự kiện |
| `Main.Count > 0` / `Count = 0` | 194 / 7 file | Loader từ chối Count không dương (`S/KNpcTemplate.cpp:138`, `:140`) |
| Tổng `Main.Count` | 10.734 | Số slot khai báo; không đồng nghĩa 10.734 item hợp lệ |
| Header section số trong các INI | 11.616 lần xuất hiện | Có section thừa, thiếu và lặp; không dùng làm số item độc nhất |
| Tên đường dẫn chứa `BOSS` (không phân biệt hoa/thường) | 59 file | Chỉ tiêu lọc tên, không chứng minh danh sách boss đang chạy |
| INI có Count dương nhưng thiếu ít nhất một section trong 1..Count | 31 file | Cần kiểm tra từng bảng trước khi sửa dữ liệu |
| INI có Count dương và có section số ngoài 1..Count | 29 file | Loader duyệt 1..Count nên không nạp các section thừa qua đường này |
| INI có Count dương và lặp header section số | 4 file | Chưa xác nhận quy tắc chọn giá trị khi section trùng |
| `ZS/Settings/Npcs.txt:1` | 2.435 mục, 1 ô DropRateFile không rỗng | Mục STT 2434 tại dòng 2436 trỏ `\settings\droprate\npcdroprate20.ini` |

Các nhóm thiếu/thừa/lặp ở trên có thể giao nhau. Count=0 có thể là chủ ý tắt rơi đồ; không tự coi là lỗi. Kiểm tra cấu trúc ở mức header/Count, không tuyên bố đã validate mọi item ID hoặc mọi giá trị trong 201 bảng.

`S/ScriptFuns.cpp:26820` đăng ký `LoldDropRate` tới `LuaLoldDropRate`; tại `:1401` lấy NPC và tên file, tại `:1434` lấy template rồi `:1435` gọi `InitDropRate`. `S/KNpcTemplate.cpp:516` yêu cầu chuỗi chứa `.ini`; tại `:547` gọi `g_GenItemDropRate`, tại `:551` gán con trỏ vào NPC. Loader đọc `Main.Count`, `RandRange`, giới hạn cấp và từng section `Genre/Detail/Particular/RandRate` (`:138`, `:164`, `:173`, `:192`).

**Điểm cần lưu ý:** tại `S/KNpcTemplate.cpp:697` biến `szDropFile` được khởi tạo rỗng; lệnh đọc cột `DropRateFile` ở `:698` bị comment; nhánh `:724` gán `m_pItemDropRate=NULL`. Vì vậy ô DropRateFile trong Npcs.txt không đủ chứng minh NPC có bảng rơi. Script gắn bảng hoặc logic khác phải được kiểm tra riêng. Đây là kết luận ở source đang đọc, chưa đối chiếu binary triển khai.

### Một vài ví dụ dữ liệu

| Entry dưới `ZS/Settings/droprate/` | Count / RandRange | Min–MaxItemLevel ở Main | nTypeNum | Tổng RandRate trong 1..Count |
|---|---:|---:|---:|---:|
| `npcdroprate110.ini:2` | 52 / 1.000.000 | 5–9 | 2 | 68.000 |
| `É±ÊÖ/bosstask_lev20.ini:3` | 57 / 4.500 | 2–4 | 7 | 2.033 |
| `É±ÊÖ/bosstask_lev90.ini:3` | 57 / 4.500 | 8–10 | 7 | 2.033 |
| `ËÎ½ð±¬ÂÊ/boss_a.ini:3` | 60 / 60.000 | 8–10 | 20 | 33.790 |

Ví dụ `bosstask_lev90.ini:25`: section `[1]` chứa `(Genre, Detail, Particular)=(0,0,0)`, `RandRate=10`, Min–MaxItemLevel riêng 9–10 (`:30`). Không coi cặp này là yêu cầu nhân vật cấp 9–10: điều kiện mặc nằm trong bảng item và kiểm tra riêng.

Ví dụ sai khác Count rõ ràng: `npcdroprate110.ini:2` đặt Count=52 nhưng có `[53]` tại `:335`, chứa `(2,1,1311)`, RandRate=500. Theo vòng lặp loader 1..Count, section này không được đọc qua đường `InitDropRate` nói trên. Báo cáo không sửa Count hay bảng.

`S/KNpc.cpp:12897` là phiên bản `LoseSingleItem` đang có hiệu lực trong source; bản tại `:12449` đã bị comment tới `:12895`. Phiên bản hiện hành lấy ngẫu nhiên theo `nMaxRandRate` (`:12908`), xét khoảng cộng dồn RandRate (`:12921`, `:12927`), bỏ slot đã được đánh dấu (`:12915`) và trả về khi không tìm được slot (`:12930`). Chọn cấp vật phẩm từ giới hạn Main xuất hiện tại `:13032`, giới hạn lại 1..10 tại `:13034`; mức khởi tạo còn phụ thuộc nhánh điều kiện, không thể suy ra toàn bộ phân phối chỉ từ Min/Max. Không chuyển trực tiếp RandRate/RandRange thành tỉ lệ rơi thực tế mỗi lần giết boss.

### Ca boss_tieu: hai cơ chế cần phân biệt

`ZS/script/task/boss_tieu.lua:10` khai báo 10 mục boss cấp 90 (ví dụ NPC ID 523 tại `:11`, 513 tại `:12`). Tại `:24`, `nDROP_BOSSTIEU` trỏ `\script\tnlteam\boss_tieu\drop.lua`; tại `:48` biến này được truyền vào `LoldDropRate`. Theo điều kiện `.ini` ở `S/KNpcTemplate.cpp:516`, lời gọi đó không nạp bảng INI qua đường source đang đọc. File `ZS/script/tnlteam/boss_tieu/drop.lua:15` có hàm `DropRate`, nhưng sự tồn tại của hàm không chứng minh nó được LoldDropRate thực thi.

Đồng thời `boss_tieu.lua:23` khai báo death script và `:47` gắn qua `SetNpcScript`. `ZS/script/tnlteam/boss_tieu/death.lua:10` có `OnDeath`, gọi `PickDropItem` tại `:23`; hàm này có lời gọi `DropItem` tại `:92`. Vì có đường rơi đồ riêng qua death script, **không kết luận toàn bộ boss_tieu không rơi gì**. Chưa xác minh callback runtime, các điều kiện và chữ ký DropItem tại phiên bản binary đang triển khai.

## Trang bị theo cấp/giới

`S/KBasPropTbl.CPP:16` đặt gốc `\settings\item\004`; `:57` khai báo 15 bảng trong `TABFILE_EQUIPMENT`; `:801` ghép đường dẫn khi nạp. Thư mục item/004 trong ZIP có 66 file TXT trực tiếp (có file backup/copy và bảng phụ), không đồng nghĩa 66 bảng trang bị được nạp.

`S/KMagicAttrib.h:49` là `magic_requirelevel`, có giá trị enum **36**; `:51` là `magic_requiresex`, giá trị **38** (đã đối chiếu enum tính từ đầu). `S/KNpc.h:747` ghi mã giới 0 nam, 1 nữ. `S/KItemList.cpp:1170` duyệt điều kiện, `:1255` từ chối cấp nhân vật thấp hơn yêu cầu; `:1276` từ chối mã giới khác yêu cầu. Sự có mặt của loại 38 với giá trị 0 có nghĩa yêu cầu nam, không phải bỏ hạn chế giới.

Ngoại lệ source: `S/KItemList.cpp:1220` trả TRUE sớm cho `GetUseKind()==1 && GetUseMapIdx()>0`; không được áp dụng quy tắc cấp/giới chung mà bỏ qua nhánh này. Các thuộc tính khác như sức mạnh, thân pháp, môn phái/ngũ hành vẫn có thể chặn mặc (`:1229`, `:1261`, `:1269`).

### Số lượng mục và điều kiện

Mọi file bảng dưới đây đều thuộc `ZS/Settings/item/004/`; dòng 1 là tiêu đề, dữ liệu từ dòng 2. Khoảng yêu cầu cấp chỉ tính những cặp có loại 36; dấu “không có 38” nghĩa không có điều kiện giới trong sáu cặp đã đọc, không phải đã chứng minh mặc được trên mọi nhân vật.

| Bảng | Số mục | Cấp vật phẩm | Khoảng yêu cầu cấp (36) | Số mục có giới 0 / giới 1 |
|---|---:|---|---|---:|
| `armor.txt:2` | 290 | 1–10; mỗi cấp 29 | 1–60 | 143 / 147 |
| `helm.txt:2` | 141 | 1–10; cấp 10 có 15, còn lại 14 | 1–140 | 70 / 70 |
| `meleeweapon.txt:2` | 70 | 1–10; mỗi cấp 7 | 0–81 | không có 38 |
| `rangeweapon.txt:2` | 30 | 1–10; mỗi cấp 3 | 0–81 | không có 38 |
| `boot.txt:2` | 40 | 1–10; mỗi cấp 4 | 1–62 | 20 / 20 |
| `cuff.txt:2` | 20 | 1–10; mỗi cấp 2 | 1–60 | 10 / 10 |
| `ring.txt:2` | 10 | 1–10; mỗi cấp 1 | 1–60 | không có 38 |
| `belt.txt:2` | 20 | 1–10; mỗi cấp 2 | 1–60 | không có 38 |
| `pendant.txt:2` | 20 | 1–10; mỗi cấp 2 | 1–60 | 10 / 10 |
| `amulet.txt:2` | 20 | 1–10; mỗi cấp 2 | 1–60 | 10 / 10 |
| `horse.txt:2` | 321 | cấp 1 có 33; cấp 2–10 mỗi cấp 32 | 10–150 | không có 38 |
| `Mask.txt:2` | 966 | 1–10; cấp 1 có 947 | 50 | 1 / 1 |
| `PiFeng.txt:2` | 14 | 1–14 | 10 | không có 38 |
| `YinJian.txt:2` | 13 | 1–13, thiếu cấp 6; cấp 7 lặp 2 mục | 10 | không có 38 |
| `ShiPin.txt:2` | 260 | 1–10; cấp 6 có 25, cấp 7 có 27 | 10 | không có 38 |
| **Tổng 15 bảng thường** | **2.235** | 11 bảng đầu: 982 mục | Không cộng thành số item độc nhất | — |
| `GoldItem.txt:2` (bảng riêng) | 5.945 | 1–20 | 0–180 | 12 / 12 |
| `platinaequip.txt:2` (bảng riêng) | 5.670 | 1–11 | 0–160 | 12 / 12 |

Chỉ hai dòng cuối là thống kê bổ sung bảng đặc biệt, không gộp chúng vào 2.235. Một số mục không có loại 36 hoặc 38: ví dụ mũ đặc biệt cuối bảng không có loại 38. Không diễn giải việc thiếu điều kiện thành một giá trị 0 được lưu.

### Ví dụ định danh bằng số

Tránh suy đoán/đổi tên item tiếng Việt bị lỗi encoding; dùng `(Genre,Detail,Particular,Level)` và dòng nguồn để tái kiểm tra.

| Nguồn | Định danh / cấp vật phẩm | Điều kiện đọc từ bảng |
|---|---|---|
| `ZS/Settings/item/004/armor.txt:2` | `(0,2,0,1)` | cấp nhân vật ≥1, giới 0; còn yêu cầu loại 32 = 30 |
| `ZS/Settings/item/004/armor.txt:3` | `(0,2,0,2)` | cấp nhân vật ≥7, giới 0; loại 32 = 50 |
| `ZS/Settings/item/004/helm.txt:142` | `(0,7,14,10)` | cấp nhân vật ≥140; loại 39 = 0, không có loại 38 |
| `ZS/Settings/item/004/horse.txt:322` | `(0,10,32,1)` | cấp nhân vật ≥90; không có loại 38 |

Cặp armor dòng 2/3 và ngựa dòng 322 cho thấy cấp vật phẩm không phải cấp nhân vật bắt buộc. Mũ cấp vật phẩm 10 cũng không có một ngưỡng nhân vật chung cho mọi dòng.

## Đối chiếu client gốc

Đã đọc trực tiếp source trong Client2912 ZIP, không chỉ dùng bản client tại D:\JX-source:

- `ZC/Classes/gamecore/KBasPropTbl.CPP:16` dùng gốc **`\update10\settings\item\004`**, khác gốc server; `:830` ghép đường dẫn. Cặp điều kiện đầu ở `:1456`/`:1457`.
- `ZC/Classes/gamecore/KItemList.cpp:954`/`:955` kiểm tra cấp, `:975`/`:976` kiểm tra giới; `ZC/Classes/gamecore/KNpc.h:666` cũng ghi 0 nam/1 nữ.
- ZIP client không có entry TXT dưới thư mục `/settings/` và không có file `.pak` trực tiếp. Có `ZC/Resources/paklist.ini`, nhưng không đọc nội dung cấu hình này và không suy ra dữ liệu nào đã tải về. `ZC/data/jx50ai/equipName.txt:1` có 16 dòng từ khóa/lọc, không phải bảng định nghĩa trang bị để đối chiếu 2.235 mục.

**Chưa xác minh:** nội dung bảng item tại đường update10 thực tế, tính đồng nhất client/server, bảng trong gói dữ liệu được tải ngoài ZIP, hiển thị sprite/tên/tooltip và kết quả mặc trên client. Sự giống nhau của phép kiểm tra source không chứng minh dữ liệu hay binary giống nhau.

## Ca test cho TESTER (chưa chạy)

Chỉ là bàn giao ca thử; task A-17 không cấp quyền chạy VM/exe hay kết nối. TESTER cần môi trường và binary được duyệt riêng. Ghi rõ phiên bản source/data, NPC/item ID, log lọc và kết quả thực tế; không đưa thông tin truy cập vào báo cáo.

| ID | Ca kiểm tra trong môi trường được duyệt | Kỳ vọng/điểm cần đo |
|---|---|---|
| A17-T01 | Với một boss được xác nhận có script gọi LoldDropRate tới INI, quan sát đường dẫn bảng thực nạp và giá trị trả về | Phân biệt bảng được gắn thành công với việc file chỉ tồn tại; xác nhận Count/RandRange và NPC dùng bảng nào |
| A17-T02 | Chọn NPC chỉ có DropRateFile từ Npcs.txt, so với NPC được gắn bảng bằng script | Đối chiếu nhận định loader bỏ qua cột; không dùng việc không rơi trong vài lần giết làm bằng chứng duy nhất |
| A17-T03 | Theo dõi boss_tieu: lời gọi với .lua và death script | Theo source, đường INI từ chối .lua; đo riêng callback death/PickDropItem để biết đường rơi nào có hoạt động |
| A17-T04 | Trên bản sao được phép, bảng Count=52 có section 53 như npcdroprate110 | Ghi nhận slot 53 không được nạp qua vòng 1..Count; kiểm tra slot nạp bằng log/instrumentation được duyệt, không chỉ thống kê giết boss |
| A17-T05 | Dùng item armor dòng 3: nhân vật giới 0 ở cấp 6, 7, 8; đáp ứng đủ các yêu cầu khác | Cấp 6 bị từ chối; 7/8 vượt qua điều kiện cấp. Chọn item không thuộc nhánh ngoại lệ UseKind/UseMapIdx |
| A17-T06 | Cùng armor dòng 3, đủ cấp/thuộc tính, đổi giới 0 sang 1 | Giới 0 vượt qua điều kiện giới; giới 1 bị từ chối. Kiểm tra cả thao tác client và quyết định server |
| A17-T07 | Mũ dòng 142: thử cấp 139/140, hai giới, đáp ứng môn phái và điều kiện khác | Kiểm tra biên cấp 140; không tự phát sinh điều kiện giới nếu dữ liệu không có loại 38 |
| A17-T08 | Ngựa dòng 322: cấp nhân vật 89/90 dù Level của item là 1 | Cấp 89 bị chặn bởi yêu cầu 90; cấp 90 vượt điều kiện này |
| A17-T09 | So bảng update10 của client với bảng server cho các item thử trên | Đối chiếu tuple/cấp/requirement và tooltip; chụp bằng chứng nếu client cho phép nhưng server từ chối hoặc ngược lại |
| A17-T10 | Chỉ khi có kế hoạch riêng được duyệt: thống kê nhiều lần boss chết, giữ cố định bảng, luck, loại map, số lượt drop | Ghi cỡ mẫu và phân phối; không dùng RandRate/RandRange làm khẳng định tỉ lệ mỗi lần giết; tách death script và INI |

## Kết quả và giới hạn bàn giao

Đã hoàn thành khảo sát tĩnh, số lượng mục, ví dụ ngắn, đối chiếu đường nạp dữ liệu, giới/cấp và ca test TESTER. Phát hiện các điểm cần xác minh tiếp: loader bỏ qua DropRateFile; đường .lua/.ini của boss_tieu; Count/section không khớp; client dùng gốc update10 khác server. Không sửa mã hay dữ liệu để xử lý các điểm này trong A-17.

Không có blocker cho phạm vi đọc tĩnh. Toàn bộ test runtime/build chưa chạy đúng chỉ thị; bản dữ liệu client triển khai và sự khớp binary/source còn chưa xác minh. Không báo cáo đạt chức năng runtime. Chưa có commit SHA vì task không yêu cầu commit; chưa push vì người dùng cấm mạng.

## Ghi nhận công cụ

- `rg` không có trong PATH (`CommandNotFoundException`); chuyển sang đọc tệp có mục tiêu bằng PowerShell/Python, không cài thêm công cụ.
- Đầu ra Python ban đầu lỗi `UnicodeEncodeError` vì stdout cp1252; đặt `sys.stdout.reconfigure(encoding='utf-8')`, đọc lại thành công. Mọi Python đều chạy `python -I`.
- Tiếp tục khảo sát gặp `TypeError: 'bool' object is not subscriptable` hai lần do đặt phép cắt chuỗi sai vị trí trong generator; đã bỏ phép cắt tại biểu thức điều kiện, lần thứ ba đọc được ZIP. Không thay đổi dữ liệu hay cài công cụ để khắc phục.
- `Get-Content` theo encoding mặc định hiển thị sai dấu tiếng Việt; đọc UTF-8 bằng Python xác nhận nội dung task/báo cáo vẫn đúng. Dữ liệu tab chứa tên/tiêu đề legacy nên thống kê số trực tiếp bằng byte/cột tab, không đoán tên item.
- Khi ghi phần kết quả task qua pipeline PowerShell sang Python, ký tự tiếng Việt bị đổi thành `?`; kiểm tra sau ghi đã phát hiện, sửa đúng phần vừa thêm bằng apply_patch và xác nhận lại UTF-8. Nội dung task ban đầu không bị thay đổi.
- Chưa commit, chưa push; không dùng mạng theo chỉ thị người dùng.
