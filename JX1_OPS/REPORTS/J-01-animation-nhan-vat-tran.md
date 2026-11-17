# J-01 — Khảo sát animation nhân vật trần

**TÓM TẮT 5 DÒNG**
1. **PARTIAL** — đã xác minh tĩnh đường nạp SPR, cấu trúc metadata, chọn hướng/khung và khác biệt mã giữa source gốc với `D:\JX-source`.
2. Hai source tree không có `.spr/.pak`; đã tìm thấy PAK local trong `data_cdn/data`, nhưng chưa có cặp asset gốc/Coco có provenance và bảng nhân vật trần để đối chiếu.
3. Vì vậy số khung, nhịp phát thực, kích thước từng frame, giới tính và độ đủ khung sau chuyển đổi đều **CHƯA XÁC MINH**.
4. Đã đọc thêm logic frame client/server và header của 4 PAK; không chạy game/exe, VM, build, mạng hoặc giải nén/chuyển đổi dữ liệu.
5. Không sửa source; báo cáo này là đầu ra duy nhất được ghi theo `vung_file` của J-01.

## Phạm vi và trạng thái

- Source gốc (O): `Folder/Client2912-20260116T044348Z-3-001/Client2912/Client`.
- Source Coco/đang đối chiếu (C): `D:\JX-source\client`. O cũng đã chứa API Cocos2d trong loader; chữ “gốc” ở đây chỉ là snapshot Folder được task chỉ định, không chứng minh đây là client PC trước chuyển đổi. Chưa xác minh C chính là artifact của lần chuyển đổi cần so sánh.
- Server (S): `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src`.
- Đã đọc các đoạn liên quan trong `KNpcRes.cpp`, `KNpcResVN.cpp`, `KNpcResNode.cpp`, `KSprControl.cpp`, `KNpc.cpp`, `KNpcSet.cpp`, `Kgetinidata.cpp`, `KImageStore2.cpp`, `KbugInfo.h`, `KFilePath.cpp`, `KPakList.cpp`; ở S chỉ đọc logic frame/giá trị cấu hình NPC tương ứng.
- Dò tĩnh source tree O và C: không thấy file `.spr` hoặc `.pak`; 8 file `.zip` tìm thấy trong O thuộc renderer/font/UI. `Resources/paklist.ini` khai báo các gói dữ liệu, nhưng các gói đó không nằm trong source tree O. Một lượt đọc cấu hình nguyên file đã trả cả trường ngoài phạm vi có dạng thông tin xác thực; không sao chép chúng vào báo cáo, file hoặc Git; các lượt sau chỉ đọc source/metadata cần thiết.
- Trạng thái Git workspace khi bắt đầu: branch `task/J-01`; `JX1_OPS/TASKS/J-01.md` là file untracked có sẵn. Không chỉnh sửa hoặc stage file này. Whitelist ghi `vung_file: [none, JX1_OPS/REPORTS/J-01-*.md]`, trong khi cuối task yêu cầu thêm `## Kết quả` vào chính file task; hai chỉ thị xung đột, nên chỉ tạo báo cáo đúng whitelist.

## ĐÃ XÁC MINH

### Đường nạp và metadata

- O `Classes/engine/Kgetinidata.cpp:100–124`: đường `findinidata_one` yêu cầu tên có đuôi `.spr`, gọi `m_ImageStore.GetImage(..., ISI_T_SPR, ...)`, rồi dừng nếu thiếu header/frame hoặc offset table (trừ chế độ single-frame). O `KFilePath.cpp:441–456` kiểm tra file qua pak list; resource có thể được lấy từ gói thay vì file rời.
- O `Classes/engine/KbugInfo.h:238–268`: `SPRHEAD` chứa `Width`, `Height`, `CenterX/Y`, `Frames`, `Directions`, `nInterval`; `SPRFRAME` chứa kích thước, offset và pixel data của từng frame. Comment của `nInterval` ghi đơn vị là game frame, không phải millisecond.
- O `Classes/engine/Kgetinidata.cpp:142–163`: loader trả metadata header và kích thước frame đang nạp (`pFrameData->Width/Height`), do đó kích thước mỗi frame có thể khác nhau; không thể thay bằng kích thước header.
- O `Classes/gamecore/KNpcRes.cpp:261–287`: hướng resource được quy đổi từ `nDir` trong miền 64 hướng sang `m_nTotalDir` của SPR; frame lấy theo `nCurFrame/nAllFrame` trong dải frame của hướng. Mã chỉ cho biết quy tắc ánh xạ, không cho biết từng SPR có bao nhiêu hướng/khung.
- Đường hiển thị thực trong source là override VN: O `Classes/gamecore/KNpc.h:816` khai báo `KNpcResVN m_DataRes`; O `KNpc.cpp:5916` truyền `m_Frames` vào `Draw`. Phép chọn part tương ứng ở O `Classes/vn/gamecore/KNpcResVN.cpp:28–60`, C `Classes/vn/gamecore/KNpcResVN.cpp:35–67`. Các phép chọn frame dùng số nguyên: nếu thời lượng logic có ít bước hơn số ảnh/hướng, một số ảnh có thể không được chọn dù asset không mất frame. Đây là hệ quả công thức, chưa phải bằng chứng triệu chứng thực tế.
- O `Classes/gamecore/KNpcRes.cpp:1180–1226`: action suy ra từ trạng thái, loại vũ khí và cờ cưỡi; từng part được nạp với `GetFileName`, `GetTotalFrames`, `GetTotalDirs`, `GetInterval`. Cần khóa cấu hình part/equip về nhân vật trần khi đo; không lấy số mặc định `16` trong lời gọi làm bằng chứng SPR thật có 16 hướng.
- O `Classes/gamecore/KNpcResNode.cpp:547–586,592–605,982–1028`: tên file, interval, số frame và số hướng tra từ bảng action × equip × part; action NPC thường dùng `nDoing`, trường hợp nhân vật khác có bảng ánh xạ ngựa/không ngựa. Giá trị bảng cụ thể phụ thuộc dữ liệu không có trong source tree.
- O `KNpc.cpp:3763–3787` chọn `MainMan`/`MainLady` và giá trị hành vi theo giới. O `KNpcResNode.cpp:210–226` có thể chuyển `MainMan` sang đường `spr\\npcres\\woman` và ngược lại tùy trường cấu hình `nIsMa`; không phân loại giới chỉ theo tên thư mục. O `KNpcResNode.cpp:232–239` đọc metadata với fallback `16,8,1` (tổng frame, hướng, interval), không phải số đo asset. `CoreUseNameDef.h:30,35` trỏ bảng loại và bảng part dưới `settings/npcres`; cần đúng bộ bảng này khi tiếp tục.
- O `Classes/engine/KbugInfo.h:272–319`: format PAK có bảng mục và kiểu nén; SPR có thể dùng kiểu nén theo frame. Đây là mô tả format trong source, không phải kết quả đã giải mã gói.

### Đối chiếu O/C

| Tệp tương ứng | SHA-256 O | SHA-256 C | Kết quả |
|---|---|---|---|
| `Classes/gamecore/KNpcRes.cpp` | `DEC54B5AAFA12EBCC12A5BFB8F1A3564BF22C63AD23F0B1F046A9470BCA2665C` | `137974C9951CFCD9A546C98541EC65F18A657DB220722BCCAF86E8FD1A3E95C7` | Khác |
| `Classes/gamecore/KNpcResNode.cpp` | `CD748986B6D17DE50D5D9FD1D4AA3A3FBECC650DB0A441D96B7694FF796FB09E` | như O | Giống |
| `Classes/engine/Kgetinidata.cpp` | `37E5A2FEF69CE9772BB606D648BC0F122DA06FB6944F6255ECD5FA2C2ECF3A0F` | `D47795258E01947F60DEF87F7E2B84CFC32D2B5DE7EC5BCBE4B61C6339E1BE08` | Khác |
| `Classes/engine/KbugInfo.h` | `BC9195B22E9FB97C69F4DE56FFB3225978BE8E4A4C471024C0948972B809887D` | như O | Giống |
| `Classes/engine/KPakList.cpp` | `4FFB23ACA39441B025CB1C4F1B006662B6ED08B7CCC1C4A01424B4FF05912BEA` | như O | Giống |
| `Classes/engine/KPakFile.cpp` | `2710369EC788437D515CD265956E576D7EDD45F11B9B122E8996AB41B83F3C86` | như O | Giống |

Ở C, đường `findinidata_one` hoạt động nằm ở `Kgetinidata.cpp:101–166`, vẫn gọi ImageStore và trả tổng frame/kích thước/interval; có thêm phép đo thời gian ở dòng 119–121. Đoạn viết lại tại `399–571` nằm trong block comment `397–572`, không được lấy làm đường chạy. Hash khác chỉ chứng minh mã khác; chưa đủ kết luận resource sau chuyển đổi còn nguyên mọi frame, palette, interval hoặc kích thước. `KNpcResNode.cpp` và cấu trúc `SPRHEAD` giống nhau theo hash ở hai bản. `KSprControl.cpp` O/C cùng SHA-256 `FDAA90A45EBD162053AB31A33C6FB90661955DF5CD5F1E94C4C6B63C63A90E25`.

### Thời lượng logic không phải số ảnh SPR

O `KNpc.cpp:443–451` khởi tạo walk=12, run/stand/death/sit=15, hurt=10, attack/cast=20, jump=40 bước logic. Đây là giá trị constructor, có thể bị thay bởi cấu hình/template; không điền chúng vào cột số frame ảnh. O `KNpcSet.cpp:101,104–110` đọc HurtFrame mặc định 12, AttackFrame 20, Walk/Run/Stand nam và nữ mặc định 15. S `KNpc.cpp:393–400` và `KNpcSet.cpp:141–151` có các giá trị tương ứng; client/server đọc cấu hình thật còn chưa xác minh. O `KNpc.cpp:3732–3739` tăng bộ đếm hành vi từng lần gọi `WaitForFrame`; `5916` chuyển bộ đếm đó sang render.

Đánh/niệm dùng tổng bước logic tỉ lệ theo tốc độ, ở O `KNpc.cpp:2380–2401` và S `KNpc.cpp:3813–3829`: `AttackFrame * a / (b + CurrentAttackSpeed)` hoặc `CastFrame * a / (b + CurrentCastSpeed)`; trường hợp mẫu số bằng 0 dùng frame cơ sở. Chưa đọc cấu hình thực của a/b hay tốc độ nhân vật, nên không có một FPS phát duy nhất cho mọi nhân vật trần.

O/C `KSprControl.cpp:37–74` lưu interval; `342–373` chỉ chuẩn hóa interval tối thiểu 1 rồi tăng **một** frame khi `SubWorld[0].m_dwCurrentTime` đổi, không dùng interval để quyết định bước ở hàm này. Trong đường `nAllFrame > 0`, renderer chọn frame theo bộ đếm logic thay vì gọi bộ tự tăng. Vì vậy lấy `1000/nInterval` làm FPS sẽ sai; chưa xác minh tick wall-clock hoặc cadence vẽ nên không suy ra millisecond.

### Gói dữ liệu local tìm được, chưa gắn provenance

Đọc trực tiếp header bằng `System.IO.BinaryReader` (không giải nén, không chạy binary) tại `C:\Jx1CocoV3\data_cdn\data`; cả 4 tệp dưới đây có magic `PACK`, data offset 32 byte và bảng index nằm trong giới hạn file theo cấu trúc 16 byte/mục ở `KbugInfo.h:286–295`:

| Gói | Dung lượng byte | Số mục header | Offset index byte |
|---|---:|---:|---:|
| `spr.pak` | 738486991 | 14616 | 738253135 |
| `resource.pak` | 238266129 | 2810 | 238221169 |
| `setting.pak` | 755491 | 325 | 750291 |
| `setting-new.pak` | 5861612 | 2074 | 5828428 |

Chỉ xác minh cấu trúc header/bounds, chưa kiểm CRC, nội dung từng mục, thứ tự override hoặc dữ liệu nén. Không có bằng chứng 4 gói này là bản gốc hay bản Coco của lần chuyển đổi cần đối chiếu. Chưa có manifest tên asset/action/trang bị trần và cặp gói trước/sau; không tự triển khai parser/giải mã hay đọc khóa cấu hình. Đây là điểm tiếp tục cụ thể, thay cho kết luận “không có dữ liệu local”.

## CHƯA XÁC MINH

`CHƯA ĐO` nghĩa là không có số liệu asset/runtime để điền. Trạng thái hướng của từng SPR cũng chưa xác định; “mọi hướng” bên dưới là yêu cầu kiểm tra theo danh sách `Directions` đọc từ từng asset, không mặc định 8 hay 16.

| Trạng thái yêu cầu | Số khung × hướng | Interval (ms)/FPS | File/format | Nam/nữ | Kích thước frame | O so với C: đủ khung? |
|---|---|---|---|---|---|---|
| Đứng | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC (SPR/PAK dự kiến theo loader) | CHƯA PHÂN LOẠI | CHƯA ĐO từng frame | CHƯA ĐỐI CHIẾU |
| Đi | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Chạy | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Đánh thường | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Niệm | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Bị đánh | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Chết | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Ngồi | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Cưỡi (người không trang bị) | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC; cần bảng OnHorse | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |
| Khác (cần liệt kê action id) | CHƯA ĐO × mọi hướng trong SPR | CHƯA ĐO | CHƯA ĐỌC | CHƯA PHÂN LOẠI | CHƯA ĐO | CHƯA ĐỐI CHIẾU |

Chưa có đủ dữ liệu để khẳng định mọi trạng thái đều tồn tại cho từng giới hoặc cùng dùng một bộ hướng. Source cho biết số frame/dir/interval có thể khác theo part/action/equip; so sánh đúng cần cùng cấu hình nhân vật trần và cùng bảng action ở O/C.

Danh sách client doing tại O `KNpc.h:105–122` phân biệt fightstand/stand/stand1, fightwalk/walk, fightrun/run, hurt, death, attack/attack1, magic, sit, jump, none. “Khác” cần ít nhất kiểm các biến thể chiến đấu và nhảy; cưỡi là cờ chọn bảng ánh xạ, không phải một action SPR duy nhất.

## ĐỀ XUẤT TỐI ƯU

1. Xác định provenance của gói local đã tìm thấy và cung cấp/định danh đúng cặp bản copy dữ liệu trước/sau chuyển đổi, gồm PAK/SPR nhân vật trần cùng bảng resource/action; không cần chạy executable để đo header.
2. Dùng extractor/decoder SPR đã được duyệt trên bản copy, chỉ đọc header, offset table và frame metadata; ghi hash input/output, kiểm `Frames`, `Directions`, `nInterval`, palette và kích thước từng frame. So sánh theo giới × action × part × hướng, không chỉ so tổng file.
3. Quy đổi `nInterval` sang thời gian/FPS bằng quy tắc tick client đã xác minh hoặc đo trong harness offline được duyệt. Không quy đổi trực tiếp game frame thành ms khi chưa biết cadence.
4. Đối chiếu các ID action thực tế với H-14/J-05. Tệp `JX1_OPS/TASKS/J-05.md` và báo cáo J-05 không có trong danh sách hiện hữu đã kiểm tra; hiện chỉ có báo cáo H-14 liên quan khung hình hiệu ứng, không phải số liệu animation nhân vật.

## H-14 liên quan

H-14 ghi rõ việc thiếu SPR/item cụ thể khiến không thể đánh số frame mất; kết quả đó phù hợp với blocker dữ liệu của J-01. Không gộp hiện tượng bolt/effect trong H-14 với animation thân nhân vật. Tham chiếu: `JX1_OPS/REPORTS/H-14-mat-khung-hieu-ung.md:67–80,131–133,186`.

## Kết quả

- Trạng thái: **PARTIAL**. Đã khảo sát loader/schema, logic client/server, hướng/khung, nam/nữ, fallback và header gói local. Chưa đo ma trận asset, FPS/ms hoặc chứng minh đủ khung O/C vì thiếu mapping và cặp asset có provenance; không đồng nhất việc có gói local với đã giải mã nội dung.
- Không có test/build/runtime; không chạy exe, VM hoặc mạng thật theo yêu cầu.
- Chỉ tạo `JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md`. Không ghi mục kết quả vào `JX1_OPS/TASKS/J-01.md` vì `vung_file` chỉ cho phép `JX1_OPS/REPORTS/J-01-*.md`; file task untracked được giữ nguyên.
- Không stage/commit/push. Chưa có SHA commit hoặc link push.

## Lỗi, giới hạn và điểm tiếp tục

- `rg : The term 'rg' is not recognized...`: chuyển sang `Get-ChildItem/Select-String`, không cài đặt. Lượt đầu đọc prompt mặc định hiển thị sai encoding; đọc UTF-8 đã khắc phục.
- Một lượt tìm quá rộng có output bị cắt; đọc lại đúng các đoạn source có số dòng, không lấy phần bị cắt làm bằng chứng. Một pipeline dùng `-Include` không trả kết quả như mong đợi; chuyển sang đường dẫn file cụ thể. Một số bảng PowerShell trộn kiểu object chỉ in cột trống; in `FullName/Name` trực tiếp để xác định đường dẫn.
- Ban đầu bản nháp xem nhầm đoạn loader viết lại là mã hoạt động và coi cưỡi ngoài phạm vi; đã sửa sau khi kiểm tra block comment và bảng OnHorse. Tìm được gói local sau bản nháp; đã thay kết luận thiếu file rời bằng giới hạn provenance/mapping thực tế.
- Một lần gọi nhầm công cụ inventory giao diện ngoài nhu cầu khảo sát; không mở ứng dụng, không bấm/nhập, không chạy game hay VM và không dùng thông tin giao diện làm bằng chứng. Không tiếp tục công cụ đó.
- Lượt đọc cấu hình nguyên file trả trường nhạy cảm ngoài phạm vi; không đưa giá trị vào báo cáo, không tạo file chứa khóa/mật khẩu, không sửa credential. Các lần đọc tiếp theo giới hạn source và header không có trường xác thực.
- Không tạo bảng asset dài ở `D:\JX-reports-private\` vì task hiện chỉ cho ghi `JX1_OPS/REPORTS/J-01-*.md`; chưa có bảng asset đã đo để xuất. Không viết ra ngoài whitelist hoặc tự tạo extractor.
- Điểm tiếp tục: xác định cặp gói O/C và manifest `MainMan/MainLady` + part/equip trần + action/OnHorse/NoHorse. Sau đó dùng công cụ đọc SPR đã duyệt để so frame/dir/offset/kích thước/palette/interval trên bản copy; kiểm cadence trong task offline riêng nếu cần ms/FPS. Chưa có bằng chứng để kết luận “đủ khung” hay “mất khung”.

## MỤC SỔ THÔNG SỐ

`TĨNH` là đọc source, không phải giá trị cấu hình đang chạy hoặc số frame ảnh thực. Đường dẫn rút gọn dưới đây: `G` = O `Classes/gamecore`, `E` = O `Classes/engine`; S như mục phạm vi. Mỗi fallback điều chỉnh được đã trích trong báo cáo có dòng riêng. Các trường asset chưa có giá trị được liệt kê để tránh nhầm với fallback.

| Nhóm | Tên/hằng số | File:line | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn (CÓ/CẨN THẬN/KHÔNG) | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Loader | `m_nInterval` khởi tạo | E `Kgetinidata.cpp:35` | 10 | giá trị interval khởi tạo | Không chứng minh cadence từng asset | CẨN THẬN | TĨNH |
| Bảng SPR | `nTotalFrames` fallback | G `KNpcResNode.cpp:232–235` | 16 | tổng frame | Dùng khi thiếu metadata bảng | CẨN THẬN | TĨNH |
| Bảng SPR | `nTotalDirs` fallback | G `KNpcResNode.cpp:237` | 8 | hướng | Chia dải frame theo hướng | CẨN THẬN | TĨNH |
| Bảng SPR | `nInterval` fallback | G `KNpcResNode.cpp:239` | 1 | game tick theo ý nghĩa bảng | Không trực tiếp điều khiển nhánh `GetNextFrame` đã đọc | CẨN THẬN | TĨNH |
| Constructor | `m_WalkFrame` | G `KNpc.cpp:443` | 12 | bước logic | Thời lượng đi; bị cấu hình ghi đè | CẨN THẬN | TĨNH |
| Constructor | `m_RunFrame` | G `KNpc.cpp:444` | 15 | bước logic | Thời lượng chạy | CẨN THẬN | TĨNH |
| Constructor | `m_StandFrame` | G `KNpc.cpp:445` | 15 | bước logic | Thời lượng đứng | CẨN THẬN | TĨNH |
| Constructor | `m_DeathFrame` | G `KNpc.cpp:446` | 15 | bước logic | Thời lượng chết | CẨN THẬN | TĨNH |
| Constructor | `m_HurtFrame` | G `KNpc.cpp:447` | 10 | bước logic | Thời lượng bị đánh | CẨN THẬN | TĨNH |
| Constructor | `m_AttackFrame` | G `KNpc.cpp:448` | 20 | bước logic cơ sở | Đánh; còn chia theo tốc độ | CẨN THẬN | TĨNH |
| Constructor | `m_CastFrame` | G `KNpc.cpp:449` | 20 | bước logic cơ sở | Niệm; còn chia theo tốc độ | CẨN THẬN | TĨNH |
| Constructor | `m_SitFrame` | G `KNpc.cpp:450` | 15 | bước logic | Ngồi | CẨN THẬN | TĨNH |
| Constructor | `m_JumpFrame` | G `KNpc.cpp:451` | 40 | bước logic | Nhảy | CẨN THẬN | TĨNH |
| Player fallback | `Common.HurtFrame` | G `KNpcSet.cpp:101`; S `KNpcSet.cpp:141` | 12 | bước logic | Phục hồi bị đánh | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Common.AttackFrame` | G `KNpcSet.cpp:104`; S `KNpcSet.cpp:144` | 20 | bước logic cơ sở | Nhịp đánh | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Male.WalkFrame` | G `KNpcSet.cpp:105`; S `KNpcSet.cpp:146` | 15 | bước logic | Đi nam | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Female.WalkFrame` | G `KNpcSet.cpp:106`; S `KNpcSet.cpp:147` | 15 | bước logic | Đi nữ | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Male.RunFrame` | G `KNpcSet.cpp:107`; S `KNpcSet.cpp:148` | 15 | bước logic | Chạy nam | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Female.RunFrame` | G `KNpcSet.cpp:108`; S `KNpcSet.cpp:149` | 15 | bước logic | Chạy nữ | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Male.StandFrame` | G `KNpcSet.cpp:109`; S `KNpcSet.cpp:150` | 15 | bước logic | Đứng nam | CẨN THẬN | TĨNH; thiếu INI thực |
| Player fallback | `Female.StandFrame` | G `KNpcSet.cpp:110`; S `KNpcSet.cpp:151` | 15 | bước logic | Đứng nữ | CẨN THẬN | TĨNH; thiếu INI thực |
| SPR header | `Frames` | E `KbugInfo.h:245` | Theo asset, chưa đọc | frame ảnh | Tổng ảnh phải kiểm chứng | KHÔNG | TĨNH schema |
| SPR header | `Directions` | E `KbugInfo.h:247` | Theo asset, chưa đọc | hướng | Số slice; cần kiểm tổng frame chia hết | KHÔNG | TĨNH schema |
| SPR header | `nInterval` | E `KbugInfo.h:248` | Theo asset, chưa đọc | game frame | Chưa quy ra ms/FPS | CẨN THẬN | TĨNH schema |
| Hướng | Quantization | G `KNpcRes.cpp:282–287`; O `Classes/vn/gamecore/KNpcResVN.cpp:55–60` | offset `32/D`, miền `64` | đơn vị góc | Chọn direction slice | KHÔNG | TĨNH |
| Sprite control | Interval tối thiểu | G `KSprControl.cpp:350–351` | 1 | giá trị interval | Chỉ clamp biến trong hàm; không throttle bước | CẨN THẬN | TĨNH |
