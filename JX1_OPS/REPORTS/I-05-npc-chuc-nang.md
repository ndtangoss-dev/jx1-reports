TÓM TẮT 1/5: PARTIAL — khảo sát tĩnh dữ liệu gốc và source cục bộ; không dùng mạng, VM, exe, build hoặc runtime.
TÓM TẮT 2/5: `Settings/Npcs.txt` có 2.435 template, trong đó 958 Kind=3; cả 958 dòng đều để trống `ActionScript`.
TÓM TẮT 3/5: ID template là chỉ số 0-based; template 2078 là lửa trại, tạo động ở map 53, MPS (51717,102750), ô (202,200).
TÓM TẮT 4/5: Đã xác minh các đường script hệ thống cho chuyển map, cường hóa/ghép và lửa trại; chưa ánh xạ được NPC thường trú tới ID/map/tọa độ.
TÓM TẮT 5/5: Bảng vị trí NPC nằm trong dữ liệu vùng/map nhị phân; hảo hữu và NPC kho cụ thể chưa xác minh; kèm ca thu thập cho TESTER.

# I-05 — NPC chức năng

## Phạm vi và nguồn

- Task: `JX1_OPS/TASKS/I-05.md`; workspace `D:\JX-wt\I-05`, branch `task/I-05` đã khớp khi kiểm tra ban đầu. File task đã có local/untracked trước khi khảo sát; không ghi đè nội dung đó.
- `GS` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs`.
- `SV` = `D:\JX-source\server\jxOnline`; `CORE` = `SV\gameserver\Sources\Core\Src`.
- `CLIENT` = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client`.
- Không sao chép source, bảng dài, dữ liệu tài khoản hoặc bí mật vào báo cáo. Python chỉ dùng `python -I -`, đọc trực tiếp, không tạo parser/script phụ.
- Task I-05 không có trong bản `TASKS/BACKLOG.md` hiện tại; tiếp tục theo chỉ định trực tiếp của chủ dự án. Chỉ ghi report theo vùng file; yêu cầu thêm `## Kết quả` vào task được coi là cho phép riêng đúng file task này.

## ĐÃ XÁC MINH

### ID và loại thực thể

- [NGUỒN] `CORE\KNpcTemplate.cpp:642` dùng `nNpcTemplateId + 2` làm số dòng; `:654` đọc `Kind`, `:759` đọc `ActionScript`. Không lấy STT làm ID template.
- [NGUỒN] `SV\header\GameDataDef.h:362` khai báo `kind_normal=0`, player=1, partner=2, dialoger=3, bird=4, mouse=5.
- [XÁC MINH] `GS\Settings\Npcs.txt:2080` là template ID 2078, STT 2079, tên GBK `篝火`, Kind=3, resource `passerby370`, ActionScript trống. STT 2078 ở dòng trước là cây `木薯树`, không phải lửa trại.

| Bảng gốc | Cách đếm | Kết quả |
|---|---|---:|
| Settings/Npcs.txt | Dòng dữ liệu không trắng sau header | 2.435 |
| Npcs.txt | Kind=0 | 1.412 |
| Npcs.txt | Kind=3 | 958 |
| Npcs.txt | Kind=4 / Kind=5 | 23 / 23 |
| Npcs.txt | Kind trống (không tự gán loại) | 19 |
| Settings/buysell.txt | Dòng dữ liệu không trắng sau header | 105 |
| Settings/buysell.txt | Mã hàng không rỗng / mã hàng duy nhất | 2.649 / 479 |
| Settings/goods.txt | Dòng sau header | 1.464 |
| Settings/Station.txt | Dòng sau header | 16 |

Lượng `Kind=3` tính từ cột `Kind`, không phải số đối tượng đang spawn. `buysell.txt` là ma trận mã hàng nên số hàng vật lý khác số ô/mã hàng. Không coi `Station.txt` là danh sách NPC; nó mô tả điểm/nhóm trạm di chuyển.

### Nhóm chức năng và đường tương tác

- [XÁC MINH] `GS\script\System\sysshop.lua:25-38,44-61,72-115` nhận `nKind`: nhánh 1 gọi `NewWorld` theo tham số map/tọa độ; nhánh 2 vào map bang hội; nhánh 3 dùng `recommendmap.ini`; nhánh 5 gọi callback hoạt động. Tên file không đủ chứng minh đây là script shop của một NPC cụ thể.
- [XÁC MINH] `GS\script\System\opensysui.lua:22-30` với `inKind==2`, `inVala==1` mở luồng `sysqiang` (cường hóa).
- [XÁC MINH] `GS\script\System\qianghua.lua:10,26-45` xử lý đầu vào cường hóa và kiểm tra tiền/đầu vào. `GS\script\System\fusioncomp.lua:33,212-240` xử lý ghép/vô cực và các hàm ghép liên quan. Đây là đường xử lý hệ thống; chưa xác định NPC đứng tại map nào mở các luồng này.
- [XÁC MINH] Ví dụ shop: `GS\script\global\npcchucnang\thoren.lua:73-81` tạo cửa hàng, thêm các nhóm hàng 174/179/93/98/146/173 rồi gọi `OpenStores()`. Ví dụ kho: `GS\script\tnlteam\npc\ruongchuado.lua:3-13` gọi `OpenBox()` trong map ID 242–248. Hai ví dụ chứng minh loại Lua tương tác có trong gói, nhưng chưa chứng minh NPC/template/map spawn nào gọi chúng.
- [XÁC MINH] `GS\script\System\activity.lua:28-36` có entry point `main`/`main11`; `sysshop.lua:111-115` có nhánh gọi callback hoạt động. Liên kết menu tới NPC cụ thể chưa xác minh.
- [XÁC MINH] `Settings\buysell.txt` có 479 mã hàng duy nhất và `Settings\goods.txt` có 1.464 bản ghi dữ liệu; hai bảng không chứa bằng chứng đủ để nối mã hàng với một template NPC cụ thể.
- [CHƯA XÁC MINH] Nhiệm vụ và hảo hữu: chưa tìm được ánh xạ đáng tin cậy từ một ID NPC thường trú tới menu/script tương ứng. Kho có script `ruongchuado.lua` nêu trên, nhưng template/map spawn vẫn chưa biết. Không gán một script cùng tên chức năng cho NPC nếu thiếu liên kết trong dữ liệu vùng.
- [NGUỒN] `CORE\KRegion.cpp:654,725` đọc bản ghi NPC và script từ dữ liệu region; `:761-764` có nhánh đặt script map khi Kind khác 3 và script trống. `KNpcTemplate.cpp:642,654,759` xác nhận chỉ số template, Kind và cột `ActionScript` là ba khái niệm riêng.

### Lửa trại tạo động

- [NGUỒN] `GS\script\task\gouhuo.lua:14` tính tọa độ hiển thị; `:16` chọn template 2078; `:21` chọn map 53; `:27` AddNpc ở MPS `(51717,102750)`, tương đương ô hiển thị `(202,200)` theo phép chia trong script; `:29` lifetime 3600; `:31` skill 1705 level 30; `:32` gán script `\\script\\两湖区\\npc\\篝火.lua`.
- [NGUỒN] `GS\script\task\dahuo.lua:16` cũng map 53; `:22` cùng tọa độ; `:25` lifetime 3600; `:27` skill 1705 level 50.
- [NGUỒN] `GS\script\item\huozhong.lua:35` chặn state 1705, `:40` chặn 1706; `:47` kiểm tra khoảng cách với NPC hỗ trợ ở map 53; `:62` chặn bản đồ/FightState; `:71` template 2078; `:76` tạo tại vị trí người dùng tính lại; `:79` lifetime 1800; `:83` gán script lửa trại. Đây là vị trí động, không phải điểm spawn cố định.

## CHƯA XÁC MINH

- Chưa chạy client/server, chưa kết nối VM; mọi điều kiện runtime và việc NPC thực sự xuất hiện đều chưa kiểm.
- Dữ liệu vùng/map dạng nhị phân không được giải mã trong khảo sát này, nên chưa có danh sách đầy đủ NPC thường trú, ID-template/map/tọa độ, script hội thoại và loại tương tác theo từng NPC. Client gốc đã được xác nhận ở đường dẫn nhưng chưa trích xuất dữ liệu map nhị phân.
- Chưa xác minh được template/map spawn của NPC kho, NPC hảo hữu hoặc tương tác hảo hữu với lửa trại. Không có căn cứ để kết luận template 2078 là NPC hảo hữu; bằng chứng hiện có chỉ cho thấy template được tạo làm lửa trại có thời hạn và gán script lửa trại.
- Các hàm Lua được kiểm tra chỉ chứng minh nhánh xử lý trong source; điều kiện gọi, NPC có xuất hiện hay không, và hành vi thực tế cần tester kiểm tra trong môi trường được duyệt.

## Ca kiểm tra cho TESTER

Mỗi ca ghi lại: tên hiển thị, map ID/tên map, tọa độ ô, template ID (không dùng STT thay thế), script đầy đủ, loại menu và kết quả; không ghi thông tin tài khoản thật.

1. Mở lần lượt NPC bán hàng ở thành/trạm; kiểm tra menu, mua/bán và đối chiếu item ID với `buysell.txt`/`goods.txt`.
2. Nói chuyện với NPC nhiệm vụ; ghi ID/map/tọa độ/script và kiểm tra mở/nhận/trả nhiệm vụ bằng nhân vật thử.
3. Nói chuyện với NPC truyền tống; đối chiếu lựa chọn map/điểm đến với `Station.txt` hoặc `recommendmap.ini`, rồi kiểm tra cả map cho phép và map bị chặn.
4. Mở NPC/chức năng cường hóa và ghép; kiểm tra luồng UI, điều kiện tiền/vật phẩm và kết quả với vật phẩm thử không có giá trị.
5. Mở kho và mục hảo hữu; xác định NPC hay UI hệ thống, script/giao thức mở ra, phạm vi lưu trữ và hành vi thêm/xóa bạn trên tài khoản thử.
6. Tạo lửa trại theo luồng được phép; xác nhận template 2078, map/ô, script, thời hạn, tương tác hảo hữu và việc NPC hết hạn. Không coi mã nguồn là bằng chứng runtime.

## Lỗi công cụ và cách xử lý

- `rg` không có trong PATH (`The term 'rg' is not recognized`); dùng đọc trực tiếp và tìm trong phạm vi thư mục bằng `python -I -`, không cài công cụ.
- PowerShell hiển thị sai một số ký tự legacy; đọc Markdown UTF-8 và dùng Python `errors='backslashreplace'` khi in. Bảng gốc có dữ liệu legacy; tên Hán/Việt hiển thị qua GBK không được dùng làm căn cứ nếu chưa kiểm encoding.
- Một lượt trích mẫu bị `UnicodeEncodeError` do ký tự không biểu diễn được ở console; cấu hình stdout UTF-8/backslashreplace khắc phục.
- Một lượt truy cập `Client\\data` bị `FileNotFoundError`; dừng dò thư mục giả định, không thử quét toàn client. Vì vậy không xác minh dữ liệu map phía client.
- Số `buysell` 160 ở checkpoint trước sai định nghĩa/không tái lập; đếm trực tiếp xác nhận 105 dòng dữ liệu, 2.649 ô mã và 479 mã duy nhất. Bảng thống kê trong báo cáo đã sửa theo cách đếm nêu rõ.

## Trạng thái bàn giao

PARTIAL. Báo cáo chỉ chứa kết quả khảo sát tĩnh và giới hạn bằng chứng. Chưa commit/push; task yêu cầu không mạng. Chưa chạy test/build/runtime, không kết nối VM và không chạy exe. Bước tiếp theo: tester đối chiếu NPC thường trú trong client/server thử nghiệm được duyệt, ghi template/map/tọa độ/script để hoàn thiện các nhóm còn thiếu.
