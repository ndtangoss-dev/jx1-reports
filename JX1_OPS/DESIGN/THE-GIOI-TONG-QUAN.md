# Thế giới game JX1 — tổng quan I-06

Ngày tổng hợp: 17/11/2026. I-06 **DONE trong phạm vi tổng hợp tài liệu hiện có**; cập nhật I-06b **PARTIAL về độ phủ J-01..J-06 do thiếu báo cáo J-06**. Các khoảng trống khảo sát và runtime bên dưới vẫn chưa được xác minh.

## Phạm vi và cách đọc bằng chứng

Chỉ tổng hợp báo cáo trong `JX1_OPS`; không đọc lại source, cấu hình hoặc dữ liệu game gốc. Mọi số liệu kỹ thuật là **dẫn lại kết quả tĩnh của báo cáo nguồn**, không phải phép đo mới của I-06/I-06b. I-06b cập nhật Animation và độ phủ ngày 17/11/2026; đã có J-01..J-05 và L-01, chưa tìm thấy báo cáo J-06 trong worktree. Tên file/symbol/vị trí source được giữ để truy vết; đường dẫn đầy đủ và dấu vân tay dữ liệu xem tại nguồn. Không dùng Main VM, mạng, binary game/server, build hay test runtime.

| Phần | Nguồn trong worktree | Độ hoàn tất/giới hạn của nguồn |
|---|---|---|
| I-01: điểm nhân vật | [Các loại điểm](../REPORTS/I-01-cac-loai-diem.md) | Khảo sát tĩnh hoàn tất; HuoYueDu, dữ liệu EXP cấp cao, reset và runtime còn thiếu |
| I-02: cửa hàng | [Vật phẩm bán](../REPORTS/I-02-vat-pham-ban.md) | DONE tĩnh; chưa đối chiếu dữ liệu client đóng gói và giao dịch runtime |
| I-03: quái/spawn | [Quái vật](../REPORTS/I-03-khao-sat-quai-vat.md) | DONE tĩnh với độ phủ PAK hữu hạn; chưa bao gồm mọi spawn động |
| I-04: map | [Map](../REPORTS/I-04-khao-sat-map.md) | PARTIAL; thiếu ma trận quy tắc, trap/Lua và kiểm chứng bản nạp |
| I-05: NPC chức năng | [NPC chức năng](../REPORTS/I-05-npc-chuc-nang.md) | PARTIAL; chưa nối đầy đủ template → instance/map → script/menu |
| I-07: tiền tệ | [Các loại tiền tệ](../REPORTS/I-07-cac-loai-tien-te.md) | Nguồn ghi BLOCKED do điều kiện backlog; có kết quả tĩnh nhưng chưa hoàn tất khảo sát |
| I-08: nhiệm vụ | [Hệ thống nhiệm vụ](../REPORTS/I-08-he-thong-nhiem-vu.md) | DONE tĩnh; chưa chứng minh TASKSYS/binding và lưu DB thực tế |
| J-01: nhân vật trần | [Animation nhân vật](../REPORTS/J-01-animation-nhan-vat-tran.md) | PARTIAL; chưa có cặp asset gốc/Coco có nguồn gốc rõ |
| J-02: quái/NPC | [Animation quái/NPC](../REPORTS/J-02-animation-quai-npc.md) | Bản nháp PARTIAL; số liệu metadata, chưa đọc SPR thực |
| J-03: kỹ năng | [Hoạt ảnh kỹ năng](../REPORTS/J-03-hoat-anh-ky-nang.md) | PARTIAL; bảy nhóm, mẫu data và vòng đời source; thiếu header SPR/Settings client thực nạp và thời lượng thực |
| J-04: lớp nhân vật | [Lớp chồng nhân vật](../REPORTS/J-04-lop-chong-nhan-vat.md) | PARTIAL; đã phân biệt sức chứa/nhánh cập nhật, sort và appearance override; thiếu asset/SORT từng hướng và runtime |
| J-05: chọn/cắt khung | [Cắt khung animation](../REPORTS/J-05-cat-khung-animation.md) | Có kết quả tĩnh; chưa có tỷ lệ mất khung đo được |
| J-06: làm mượt animation | Chưa tìm thấy báo cáo `J-06-*.md` trong `REPORTS` | [Task J-06](../TASKS/J-06.md) ghi `done`, nhưng chưa có đầu ra để chốt thêm khung giữa, dung lượng hoặc công sức; độ phủ J-01..J-06 còn PARTIAL |
| L-01: làm mượt hình ảnh | [Làm mượt hình ảnh](../REPORTS/L-01-lam-muot-hinh-anh.md) | DONE giai đoạn 1 tĩnh; A/B là thiết kế thử, chưa patch/build/chụp ảnh/đo FPS-RAM; không thay kết quả J-06 |

Trạng thái BLOCKED của I-07 là lịch sử của nguồn, không phải blocker giao việc I-06: người dùng đã giao trực tiếp việc tổng hợp tài liệu hiện có. Không sửa trạng thái task/báo cáo nguồn và không coi phần khảo sát còn thiếu đã hoàn tất.

## Bức tranh thế giới và vòng chơi

Người chơi vào map, tương tác NPC hoặc nhận mục tiêu, đánh quái/thu thập/hoàn thành hoạt động, nhận EXP/điểm/tiền/đồ rồi mua sắm hoặc phát triển nhân vật. Đây là cấu trúc tổng hợp từ dữ liệu và các đường xử lý được báo cáo; chưa phải một vòng chơi đã chạy thành công.

| Liên kết | Thành phần phải nối | Bằng chứng hiện có và phần thiếu |
|---|---|---|
| Map → quái | Catalog/world nạp → region spawn → template → cấp/ngũ hành override → chỉ số Lua | I-03 có kiểm kê PAK; I-04 có Count/vòng tải; chưa có tập instance đang sống |
| NPC → dịch vụ | Instance/region hoặc AddNpc → script → callback → shop/kho/nhiệm vụ | I-05 có các đường script; chưa ánh xạ đủ NPC thường trú |
| Hạ quái → EXP/đồ | EXP cơ sở → hệ số/chia đội/chênh cấp; bảng rơi map/spawn/golden | I-03 bổ sung đầu vào cho I-01; không lấy EXP bảng quái làm EXP cuối |
| Nhiệm vụ → kinh tế | Điều kiện/state → tiến độ → trừ vật phẩm → thưởng → lưu/đồng bộ | I-08 có luồng mẫu; tính nguyên tử, reset và binding thực chưa kiểm |
| Shop → phát triển | Goods/template → giá/thuế → đúng ví → hành trang → item | I-02/I-07 khớp mapping tiền; chưa thử mua và khôi phục phiên |
| Trạng thái → hình ảnh | Action/tick/hướng → resource/SPR → frame/lớp vẽ → vòng đời effect/sampler | J-01..J-05 có source/metadata; L-01 bổ sung lọc ảnh/phép chiếu; thiếu J-06, chưa xác nhận chất lượng hình hoặc FPS thật |

Hảo hữu chưa có đủ bằng chứng để nối thành vòng chơi riêng: không suy thêm bạn sẽ tăng EXP, cho chuyển đồ ràng buộc, mở NPC đồng bạn hoặc hoàn tất nhiệm vụ đồng bạn. Những liên kết này phải có dữ liệu/binding và kết quả kiểm chứng riêng.

## Điểm và phát triển nhân vật — I-01

- EXP: bảng rời có **200 cấp**, trong khi `MAX_LEVEL=500`; cấu hình `PlayerMaxLevel=200` chưa chứng minh mọi đường cộng EXP đều tuân theo. Cấp 1 cần 100, cấp 50 cần 2.000.000; từ 99 đến 200 là 2.000.000.000 theo bảng nguồn.
- Lên cấp thông thường tăng đúng một cấp, đặt EXP về 0, cộng **5 tiềm năng + 1 kỹ năng**. EXP luyện kỹ năng là dữ liệu riêng với điểm kỹ năng chưa phân phối.
- EXP đội chỉ chia người cùng subworld và trong cự ly **768**; N≥2 dùng hệ số `100+15N`, chia theo cấp. Đội hai người cùng cấp nhận 65% E/người trước các hệ số tiếp theo. Nhánh chỉ một người đủ điều kiện giữ nguyên E; không áp bonus đội cho trường hợp này.
- `ServerExp=1`, `ServerExpLimit=10.000.000` trong cấu hình được I-01 đọc. Đường `AddSelfExp`, `DirectAddExp` và nguồn lửa trại không cùng guard/hệ số. Reset task 170 theo login và ngày trong tháng còn rủi ro; chưa biết reset online qua nửa đêm.
- Danh vọng được chặn **0..100.000**, có **11 mốc cấp 0..10**; mốc cấp 10 là 36.000, không phải trần số dư. I-01 đọc được thân Lua AddRepute và cảnh báo wrapper Repute_Set; đây là phần bổ sung cho I-07 vốn chưa đọc đủ.
- HuoYueDu có một lời gọi không comment nhưng thiếu script đích; chưa xác định số dư, nguồn nhận, cách tiêu hoặc hạn ngày/tuần. Không gộp các task hoạt động cũ thành một hệ điểm chung.

Truy vết: I-01 mục Kinh nghiệm, Kỹ năng và tiềm năng, Danh vọng, Điểm hoạt động; `KPlayer.cpp:2936,3099,3264`, `KPlayerSet.h:6`, `KPlayerRepute.cpp:44,67` theo nguồn.

## Vật phẩm bán và tiền tệ — I-02/I-07

I-02 phân biệt **1.464 dòng goods**, **160 dòng shop vật lý** (105 có nội dung), **2.644 ô ID dương** và **474 goods ID khác nhau được tham chiếu**. Trong số đó 312 goods có Price trống; giá có thể kế thừa template, còn nhánh mua kiểm giá dương. Không diễn giải thành hàng miễn phí.

Kỳ Trân/DynamicShop dùng bốn danh mục trong `type.txt`, tổng **62 goods ID**, đều cấu hình loại tiền 2 (Xu): Kỳ Trân 22, Hoạt Động 10, Thư Tịch 29, Chiến Mã 1. Nhãn tab không xác định chính xác công dụng item: mục Chiến Mã hiện là genre mine. `Sale(n)` trừ 1 để ra shop nội bộ, còn DynamicShop dùng trực tiếp `shopid`; cần giữ riêng hai cách đánh số.

| Loại/đơn vị shop | Số dư/ý nghĩa được báo cáo | Giới hạn khi dùng |
|---|---|---|
| 0/1: bạc | Túi `iservermon`, rương `isavemoney`; hai room cùng loại tiền | `GetMoney` cộng túi+rương, `Pay` thường chỉ trừ túi; chưa thấy ví bạc khóa riêng |
| 2: Xu | `iclientx`, khác điểm nạp | Có `EarnXu/PayXu`; chưa chốt trần nghiệp vụ hay chuyển trực tiếp giữa người chơi |
| 3: phúc duyên | Ví phúc duyên | Nguồn nhận, trần, UI và persistence chưa đủ |
| 4: danh vọng | `ireputevalue` | I-01 bổ sung trần 100.000 và nguồn mẫu; chưa kiểm runtime |
| 5: vinh dự | Task **2051** trong nhánh shop/đấu giá | Tên enum `moneyunit_expoint` không có nghĩa tiêu `ExtPoint` |
| 6: Tống Kim | Task **192** trong nhánh shop/đấu giá | Phải kiểm tập script nạp vì I-08 cũng thấy 192 dùng làm bit thưởng phụ tuyến |
| Điểm nạp `ExtPoint` | Số dư riêng với Xu; script tiền trang đổi sang Xu | Persistence/PaySys và tính nguyên tử chưa xác minh; không gọi là một ví Xu khác |
| Vé/lệnh bài | Vật phẩm, tùy template/script | Không mặc định là tiền; cần kiểm tiêu stack, hạn và ràng buộc |

Trong 474 goods ID được tham chiếu: 334 dùng loại 0, 115 loại 2, 25 loại 6. I-07 chưa đối chiếu I-02 lúc khảo sát; I-06 đối chiếu được mapping nêu trên ở cấp báo cáo. Bạc có đường trade; quan hệ bạn bè không tự cấp ngoại lệ chuyển đồ ràng buộc. Tính nguyên tử đổi điểm nạp/Xu, `PrePayXu` gọi `Pay`, tiêu Kim Nguyên Bảo và tràn số nguyên là ứng viên review, chưa phải lỗi runtime đã tái hiện.

Truy vết: I-02 mục Số liệu, Bảo vật/Kỳ Trân, Điều kiện mở/mua; I-07 mục Ma trận số dư, Tiền trang, Giao dịch; `KBuySell.cpp:392,512`, `KPlayerDBFuns.cpp:685,693,701`, `KPlayer.cpp:7365` theo nguồn.

## Quái, boss, map và NPC — I-03/I-04/I-05

Catalog `Npcs.txt` có **2.435 template × 106 cột**: Kind=0 tường minh 1.412, Kind=3 đối thoại 958, Kind=4 và 5 mỗi loại 23, Kind trống 19. **ID template = STT−1 = dòng vật lý−2**. Không dùng STT, ID instance hoặc tên hiển thị thay nhau. Kind trống có default 0 trong loader nên không tự gán 19 hàng thành “không dùng”.

HP/EXP/chỉ số phụ thuộc template, Lua, cấp/ngũ hành của instance và override map. Ví dụ hai mẫu animal/standard ở cấp 30 có HP suy ra 570/2.850, cùng EXP cơ sở 290; đây là phép thế nguồn, không phải kết quả đánh quái. Có **16 hàng golden**, khác giới hạn source 30 và khác các type resource tên `boss*`. DropRateFile trống không chứng minh không rơi đồ: còn bảng rơi map/spawn/golden. AI mode 7..10 có 97 template nhưng nhánh switch được báo cáo nằm trong comment; chưa kết luận hành vi runtime.

| Tầng map/spawn | Kết quả báo cáo | Không được suy thành |
|---|---|---|
| Catalog gốc / bản `Settings/vn` | 993 / 1.020 ID | Hai bộ dữ liệu cộng lại hoặc tự bổ sung lẫn nhau |
| WorldSet gs001 | 872 mục, Count=800; source xét 800 mục đầu | 872 map đang nạp hoặc 800 map đã nạp thành công |
| MapType gốc | 204 có loại, 789 thiếu | Thiếu loại tức map không tồn tại; City tức an toàn toàn map |
| NPC auto-level | 131 cặp Min=Max, cấp 15..95 | Cấp yêu cầu của nhân vật |
| PAK server theo I-03 | 955/993 map đọc được `.wor`; 38 chưa khớp | Map chưa khớp có 0 quái |
| Bản ghi spawn | 95.952 NPC = 94.098 shKind=0 + 1.854 shKind=3; 195 map có shKind=0, 172 template quái | Số NPC/quái sống hoặc số NPC chức năng duy nhất; region dùng lại được tính theo từng ID map |
| MapTraffic | 493 điểm Type0 → 342 cặp có hướng trên 156 ID | Graph trap/Lua server đầy đủ hoặc cổng đã hoạt động |

I-03 bổ sung một phần khoảng trống PAK của I-04/I-05, nhưng chưa lập ánh xạ đầy đủ NPC chức năng → script/menu; chưa gồm mọi Lua spawn động, fallback file rời và world thực nạp. PK/chiến đấu/giao dịch phụ thuộc vùng, cờ nhân vật và script. Map 53 có đường đổi FightState trong/ngoài cổng; cấm cưỡi chưa đủ bằng chứng. Không coi 36 hàng `ForbititMap.txt` là 36 map với toàn bộ thuộc tính theo hàng: consumer quét từng cột riêng.

NPC chức năng có các script kho, shop, cường hóa, ghép và chuyển map; chưa chốt NPC thường trú nào mở chúng. Lửa trại là ví dụ nối được bằng script: **template 2078**, map 53, MPS `(51717,102750)`, ô hiển thị `(202,200)` ở nhánh lịch; item tạo tại vị trí động. Lifetime cấu hình 3.600 hoặc 1.800 chưa quy thành giây. Script gọi skill 1705/1706 nhưng I-01 không thấy hai SkillId trong bảng Skills rời được đọc; cần đúng overlay/PAK trước khi kết luận hoạt động hỏng.

Truy vết: I-03 mục Template, Chỉ số theo cấp, Golden, Kiểm kê spawn PAK; I-04 mục Catalog, Truyền tống, PK; I-05 mục ID, Đường tương tác, Lửa trại. Vị trí nguồn tiêu biểu: `KNpcTemplate.cpp:642,654`, `KSubWorldSet.cpp:448,458`, `KRegion.cpp:657`, `gouhuo.lua:16,21,27`.

## Nhiệm vụ và trạng thái dùng chung — I-08

- Kho task có key **0..9999**, dùng cả nhiệm vụ, tiền/điểm, timer và gameplay khác; không tương đương 10.000 nhiệm vụ. Key task, mã/tên TASKSYS, khóa mission/timer và TaskId UI là các loại mã riêng.
- I-08 đếm 3 tuyến trạng thái chính, 36 cổng thưởng phụ tuyến; daily kill có 17 mẫu nhưng nhánh chọn chỉ 1..16; random có 117 tên entity và 107 tên bảng chọn; 33 khóa mission và 47 khóa timer. Không cộng các số này thành tổng nhiệm vụ đang mở.
- TASKSYS mẫu có state 0 → 1 START → 2 FINISH → 3 AWARD; chính tuyến/daily/random dùng các biến và quy ước khác. Không áp state chung cho mọi quest.
- `nTaskCount` là **BYTE**; save đếm mọi biến khác 0 rồi thu hẹp. Biên 255/256 là rủi ro persistence suy ra từ source, chưa tái hiện mất DB. Buffer role 128 KiB không tự giải quyết count 8 bit; tăng key hoặc nhét thêm dữ liệu hảo hữu cần đánh giá hợp đồng lưu trữ.
- IncludeLib trong source được báo cáo là no-op; binding TASKSYS, 16 đường script guide thiếu file rời, nhãn random không khớp và nhận/thưởng lặp còn chưa xác minh. Coco có panel/trace/gói task không chứng minh toàn bộ quest chạy được. Bot chưa có nhận/trả quest hoàn chỉnh theo nguồn.

Truy vết: I-08 mục Bảng số liệu, Cấu trúc, Trạng thái, Điểm không khớp; `KPlayerTask.h:13`, `S3DBInterface.h:193`, `KPlayerDBFuns.cpp:1844,1862`, `ScriptFuns.cpp:3842` theo nguồn.

## Animation — J-01..J-06 và L-01

Độ phủ hiện có là **J-01..J-05 và L-01**; J-06 còn thiếu báo cáo. Các kết quả dưới đây được kiểm ở cấp tài liệu, không xác minh lại source hay binary. Đặc biệt phải tách số ảnh asset, số bước logic, số lần draw và chất lượng lấy mẫu texture; mỗi tầng có thể tạo triệu chứng hình ảnh khác nhau.

### Nhân vật trần và quái/NPC — J-01/J-02

J-01 xác nhận loader SPR có metadata tổng frame, hướng, interval, kích thước/offset từng frame. Đường VN dùng `KNpcResVN`; một số file gốc/Coco khác hash, nên không xem hai cây source là cùng bản. Header bốn PAK local đã được nguồn kiểm tra nhưng chưa có manifest/cặp asset trước–sau để chốt số khung nhân vật trần, giới tính, kích thước hoặc độ đủ khung chuyển đổi.

J-02 ghép 1.412 template Kind=0 với **379 appearance type**; `FightStand` có metadata hợp lệ cho **1.398 template**, min/trung vị/max tổng frame **1/80/192**. Trong mẫu hợp lệ, 1.303 template có 8 hướng, 95 có 1 hướng; 14 template thiếu metadata. Năm type `boss160..164` thiếu hàng resource/info. Đây là mẫu theo template, không phải thống kê SPR duy nhất và không xác nhận quái di động một frame. 16 loại golden, 135 type `boss*` và số boss runtime là ba đại lượng khác nhau.

Truy vết báo cáo: `J-01-animation-nhan-vat-tran.md:24` (metadata), `:27` (đường VN), `:48` (thời lượng logic), `:54` (PAK); `J-02-animation-quai-npc.md:11` (ghép template), `:18` (phân bố), `:48` (metadata không chia hết hướng). Nguồn tiêu biểu theo báo cáo: `KbugInfo.h:238`, `KNpcResVN.cpp:28`, `KNpcResNode.cpp:447`.

### Kỹ năng và vòng đời hiệu ứng — J-03

J-03 lần ra mục tiêu **18 tick logic/giây** ở đường gọi `g_pCoreShell->Breathe()` trong `KgameWorld.cpp`, khác render mục tiêu 60 Hz; chưa đo cadence hoặc đồng bộ client/server. Với N tổng frame, D hướng, F=floor(N/D), I interval, c tuổi bay và L thời gian bay logic, nhánh missile loop chọn `floor(c/I)%F`, non-loop chọn `floor(F*c/L)`. Interval có tác dụng khác nhau theo đường phát, không thể dùng một công thức FPS cho mọi SPR. Mẫu metadata server missile 68/6/412 có F=4/3/5 và chu kỳ loop tính được 4/3/10 tick; chưa đối chiếu header SPR hoặc Settings client thực nạp.

| Nhóm hiệu ứng đã khảo sát | Kết quả tĩnh và giới hạn |
|---|---|
| Niệm/tiền chiêu | `PreCastSpr` riêng với action cast; thiếu header để chốt số ảnh và thời lượng nhìn thấy |
| Bay/đạn | Chọn frame theo tuổi bay ở nhánh loop/non-loop; lifetime không bảo đảm mọi frame đã được vẽ |
| Trúng/va chạm/biến mất | Deadline `begin + I*N/D` khác nhịp tiến ảnh; điều kiện damage/event và hình có thể khác nhau |
| Vùng đất | Đường Zone phát missile con theo lưới/lọc tròn; chưa thấy renderer mặt đất riêng trong đường đã khảo sát |
| Aura/buff | State hình riêng với thời hạn buff; caller GetInfo truyền trùng biến D/I và tọa độ, nên chưa dùng metadata để suy tốc độ hiệu dụng |
| Chém/vệt vũ khí | Phân biệt part vũ khí, blur và missile hình chém; chưa có số frame/duration chung theo phái/ngũ hành |
| Hiệu ứng treo | Có đường bám target match-ID và slot NPC đơn; cùng tên SPR không restart, tên khác có thể thay ảnh |

J-03 chỉ ra thứ tự **tiến frame → CheckEnd/release → draw**, nguy cơ frame cuối bị giải phóng trước vẽ; effect thuộc list missile cũng có đường bị xóa khi owner bị remove. Đây là nghi vấn từ thứ tự câu lệnh, chưa phải lỗi trong game đã tái hiện. Không kéo dài LifeTime, đổi damage/cooldown hoặc thêm khung chỉ để che triệu chứng này.

Truy vết: `J-03-hoat-anh-ky-nang.md:28` (18 tick), `:34` (missile), `:43` (bảy nhóm), `:57` (release/owner), `:61` (alias state), `:71` (mẫu data), `:115` (giới hạn). Nguồn theo J-03: `KgameWorld.cpp:5624`, `KMissleRes.cpp:154`, `KNpcResVN.cpp:176`, `KNpcRes.cpp:2143`.

### Lớp ghép nhân vật và thứ tự che — J-04

Sức chứa legacy là **24 section/6 nhóm**, hai layer `BASE/EFFECT`; nhánh `ChangeFeature` được báo cáo chỉ cập nhật BASE của **5 nhóm** đầu/áo/vũ khí/ngựa/Phi Phong. Không coi sức chứa là số lớp đang hiển thị hoặc bằng chứng cánh/EFFECT đã hoạt động. `shiping` thay appearance vũ khí, `yinjian` thay appearance áo trong nhánh Equip; chúng không thêm section độc lập ở đường này. Nhãn UI Phi Phong cũng khác sprite áo choàng.

Mỗi part/layer nhận tiến độ action chung nhưng có N/D riêng, nên có thể chọn index khác nhau. Sort tra theo **action × hướng × frame**, không có thứ tự che cố định cho mọi tư thế; khóa hướng/frame đưa vào sort còn phụ thuộc vòng lặp part/layer. Cần metadata và bảng SORT thực nạp để kết luận lệch lớp hay che vũ khí. J-04 phân biệt source gốc với mirror có glow/sét tùy biến: đường mirror vẽ lại ảnh weapon đã chọn, không chứng minh glow là SPR có cùng action riêng.

Truy vết: `J-04-lop-chong-nhan-vat.md:22` (section), `:33` (nhánh hiện hành), `:39` (appearance), `:56` (frame), `:62` (sort), `:66` (mirror), `:72` (chưa xác minh). Nguồn theo J-04: `KNpcResNode.h:23`, `KNpcRes.cpp:1703`, `KItemList.cpp:1318`, `KNpcResVN.cpp:439`.

### Chọn/cắt khung và nhịp phát — J-05 đối chiếu J-03/J-04

J-05 xác nhận ánh xạ frame bằng chia nguyên và bộ đếm tick; khi số ảnh mỗi hướng lớn hơn số bước logic, có thể bỏ mẫu; ít hơn thì lặp khung. Nhánh `GetNextFrame` chỉ tăng một khung khi tick engine đổi, không gate theo interval và không bù nhiều tick đã trễ; nhánh `ChangeCurFrame` có xử lý elapsed khác. J-03/J-04 bổ sung đường VN thực được khai báo, tránh lấy mọi kết quả renderer base làm hành vi VN. `setAnimationInterval(1/60)` là nhịp render mục tiêu, không phải FPS đo được; interval SPR không mặc định có đơn vị millisecond. Tốc độ đánh/niệm đổi thời lượng logic, không chứng minh client mất asset.

Có cờ ẩn NPC/người/đạn và pool missile 30.000, slot skill state 18/NPC; chưa có bằng chứng chắc về LOD tự động theo mật độ. Không dùng dung lượng pool làm số hiệu ứng đang vẽ. Tỷ lệ rơi khung ở đứng/đi/đông, nguyên nhân H-14/H-15 và chi phí APK/RAM/texture đều **chưa đo**; không ghi 0% hoặc ước lượng lợi ích định lượng.

Truy vết: `J-05-cat-khung-animation.md:18` (render), `:20` (hai controller), `:22` (bỏ/lặp mẫu), `:33` (ẩn/pool), `:48` (các cảnh chưa đo). Nguồn theo J-05: `KSprControl.cpp:297,342`, `KNpc.cpp:3732`, `AppDelegate.cpp:119`.

### Làm mượt hình ảnh — L-01; khoảng trống J-06

L-01 xác nhận tĩnh đường SPR giải mã từng frame sang RGBA và texture raw mặc định dùng **GL_LINEAR, một mip**; bật lại linear toàn cục chưa phải cải thiện mới. Thiết kế 1040 × 603,2, policy `EXACT_FIT`, phép chiếu world dùng int và canvas map 512 × 512 logic là các tầng khác nhau. Macro subpixel mặc định 1 không khôi phục phần lẻ đã mất upstream. Nhánh `nIsClear` có bất nhất giữa RGB đã premultiply và cờ texture alpha thẳng; chưa biết asset nào thực đi nhánh đó.

**A chỉ là đề xuất thử:** giữ sampler hiện có, thêm phép chiếu float riêng cho render và migrate đồng bộ các lớp; thử mật độ target map cao hơn cho một region, giữ footprint/crop/điểm neo, chưa đổi policy/design size toàn cục. **B chỉ là prototype dự kiến** bộ lọc cạnh 2× theo mục tiêu xBRZ, chưa có port/shader đã thẩm định hay build. Ban đầu chỉ dùng frame SPR riêng có hợp đồng alpha rõ; giữ vũ khí/glow/sét, shadow/state và font ngoài B đến khi ánh xạ đường vẽ. Map ghép có hợp đồng alpha/biên khác, phải đủ điều kiện mới thử B.

Kế hoạch L-01 so baseline/A/A+B trên nhân vật, quái, ô map, icon UI; kiểm +6/+12/+15 trên nền sáng/tối, đứng/đánh/di chuyển và đo FPS/frame-time/RAM riêng trên điện thoại và LDPlayer trong task sau được duyệt. Ví dụ target RGBA8888 ở content scale 1, không padding: 512² → 1024² tăng màu từ 1 → 4 MiB/target; đây là **phép tính điều kiện**, không phải RAM đo hoặc tăng APK do thêm frame. Chưa có ảnh, chất lượng/hiệu năng đạt hay patch áp dụng.

J-06 hiện chỉ có task `done` và yêu cầu đánh giá nhịp phát độc lập tick, nội suy vị trí, thêm khung giữa/chọn lọc và điều chỉnh thời lượng. **Chưa đủ đầu ra để kết luận cần/không cần khung giữa, số khung bổ sung, chi phí APK/RAM/texture hoặc công sức.** L-01 xử lý lấy mẫu/phép chiếu, không thay báo cáo làm mượt animation theo thời gian của J-06. Điểm tiếp tục là bổ sung đúng báo cáo J-06 vào worktree rồi đối chiếu với các tầng timing, vòng đời và lớp ghép ở trên.

Truy vết: `L-01-lam-muot-hinh-anh.md:19` (policy/sampler), `:27` (alpha), `:32` (lượng tử), `:41` (A), `:74` (target), `:82` (phép tính RAM), `:88` (B), `:158` (kế hoạch), `:170` (giới hạn); `TASKS/J-06.md:4,11,12` chỉ là trạng thái/phạm vi/đầu ra yêu cầu. Nguồn theo L-01: `CCTexture2D.cpp:641,714`, `KSubWorld.cpp:188`, `KgameWorld.cpp:7461,7665`, `Kgetinidata.cpp:289`.

## Đối chiếu và khoảng trống còn mở

| Vấn đề | Cách tổng hợp I-06 | Phần cần xác minh tiếp |
|---|---|---|
| I-05: 2.649 ô/479 mã shop; I-02: 2.644/474 | I-02 tách 5 ô chữ khỏi ID nguyên dương; dùng 2.644/474 khi nói tham chiếu goods hợp lệ | Không gọi 479 là 479 ID goods số hợp lệ |
| I-04 chưa đọc PAK; I-03 đã kiểm kê hai PAK | Dẫn độ phủ 955/993 của I-03, vẫn giữ giới hạn map/rule/trap của I-04 | Không coi khảo sát map/NPC hoàn tất nhờ có tổng bản ghi |
| I-07 chưa có I-02; I-01 bổ sung danh vọng | Đối chiếu được mapping shop và trần danh vọng ở cấp báo cáo | Chưa đối chiếu byte bộ dữ liệu/binary thực nạp |
| Task 192 dùng cho Tống Kim và bit thưởng phụ tuyến | Ghi là nguy cơ dùng chung key trong các đường script | Chọn tập script nạp và kiểm tương tác; chưa kết luận collision runtime |
| J-02 chưa thấy PAK trong cây client; J-01 thấy PAK local ngoài cây | Hai phạm vi tìm khác nhau; đã có dữ liệu local nhưng chưa rõ nguồn gốc | Cần manifest và asset đúng bản, không coi thiếu file rời là mất tài nguyên |
| J-01..J-04 từng ghi chưa có J-05; J-05 hiện đã có | Đó là giới hạn thời điểm khảo sát của nguồn; I-06b đã đối chiếu báo cáo J-05 | Không lặp kết luận thiếu J-05 như trạng thái hiện tại; không sửa báo cáo nguồn |
| J-03: logic 18 tick/giây; J-05/L-01: render 60 Hz | Hai nhịp mục tiêu khác nhau, đều là source tĩnh | Đo tick/draw/frame-time thực, không suy 60 frame animation mới mỗi giây |
| J-04 có mirror glow/sét; L-01 không tìm thấy symbol tương ứng ở source gốc | Hai snapshot/phạm vi khác nhau; không ghép vị trí patch giữa chúng | Khóa đúng source/build, ánh xạ blend/alpha/sort trước thử B cho vũ khí |
| J-06 task done nhưng thiếu báo cáo | Chưa có kết quả để tổng hợp | Nhận đầu ra J-06 rồi bổ sung trong đơn vị tài liệu tiếp theo |

## MUC SO THONG SO

Sổ rút gọn dưới đây dẫn lại nguồn, chưa đo live. **CẨN THẬN** là cần phê duyệt/kiểm chứng trước thay đổi; **KHÔNG** là không coi ID, thống kê hay hợp đồng cấu trúc như núm cân bằng. I-06 không thay thông số nào.

| Nhóm | Tên/thông số | Giá trị | Đơn vị/ảnh hưởng | Đổi an toàn | Nguồn báo cáo; file:line nguồn |
|---|---|---|---|---|---|
| Phát triển | Điểm mỗi cấp | 5 tiềm năng; 1 kỹ năng | điểm/cấp; EXP dư về 0 ở LevelUp | CẨN THẬN | I-01; `KPlayer.cpp:61,62,3264` |
| EXP | Bảng / MAX_LEVEL / PlayerMaxLevel | 200 / 500 / 200 | cấp; ba phạm vi không đồng nhất | KHÔNG tự đồng bộ | I-01; `level_exp.txt:2`, `KPlayerSet.h:6`, `gamesetting.ini:448` |
| EXP | ServerExp / ServerExpLimit | 1 / 10.000.000 | hệ số / EXP đếm; tùy đường nhận | CẨN THẬN | I-01; `GameOption.ini:2,4` |
| Đội | Cự ly; hệ số N≥2 | 768; 100+15N | đơn vị nguồn; phần trăm trước chia cấp | CẨN THẬN | I-01; `KPlayer.cpp:63,2936` |
| Danh vọng | MAX_REPUTE_VALUE | 100.000 | điểm, trần số dư | CẨN THẬN | I-01; `GameDataDef.h:42` |
| Shop | Goods / dòng shop / ID tham chiếu | 1.464 / 160 / 474 | thống kê dữ liệu, không phải quota | KHÔNG | I-02; `goods.txt:2`, `buysell.txt:2` |
| Tiền | Task vinh dự / Tống Kim | 2051 / 192 | key dùng khi mua hàng | KHÔNG | I-02/I-07; `KBuySell.cpp:432,533` và mục mapping |
| Tiền trang | KM; chặn điểm rút | 0; >=21.000 | hệ số thêm Xu; miền đi được 1..20.999 | CẨN THẬN | I-07; `tientrang.lua:4,68,77` |
| NPC | Tổng / Kind=0 / Kind=3 | 2.435 / 1.412 / 958 | template tĩnh | KHÔNG | I-03/I-05; `Npcs.txt:1` và mục đếm |
| Map | WorldSet Count / số mục | 800 / 872 | số mục xét tải / mục khai báo | CẨN THẬN với Count | I-04; `WorldSet_gs001.ini:803,804`, `KSubWorldSet.cpp:448` |
| Map | Cặp auto-level Min=Max | 131 cặp, cấp 15..95 | cấp NPC, không là cấp vào map | CẨN THẬN | I-04; `KRegion.cpp:657` và mục Catalog |
| Lửa trại | Template; skill được gọi | 2078; 1705/1706 | ID; thiếu hai SkillId trong bảng rời khảo sát | KHÔNG | I-05/I-01; `Npcs.txt:2080`, `huozhong.lua:35,40` |
| Lửa trại | Lifetime lịch / item | 3.600 / 1.800 | đơn vị runtime chưa xác minh | CẨN THẬN | I-05; `gouhuo.lua:29`, `huozhong.lua:79` |
| Task | MAX_TASK / nTaskCount | 10.000 / BYTE (255) | miền ID / count record khác 0 | KHÔNG tự mở rộng | I-08; `KPlayerTask.h:13`, `S3DBInterface.h:193` |
| Task | Buffer role / lô load | 128 KiB / 20 | byte/role; record/lô | CẨN THẬN | I-08; `KPlayer.h:284`, `KPlayerDef.h:8` |
| Render | Animation interval | 1/60 | giây/khung mục tiêu, chưa đo FPS | CẨN THẬN | J-05; `AppDelegate.cpp:119` |
| Animation | FightStand hợp lệ; min/median/max | 1.398; 1/80/192 | template; tổng frame metadata | KHÔNG sửa theo thống kê | J-02; mục Phân bố metadata |
| Animation | Nhịp logic mục tiêu | 18 | tick/giây theo source, khác render 60 Hz | CẨN THẬN | J-03:28; `KgameWorld.cpp:5624` |
| Lớp nhân vật | Sức chứa / nhánh cập nhật | 24 section, 6 nhóm, 2 layer / 5 nhóm BASE | cấu trúc / ChangeFeature; không là số lớp đang hiện | KHÔNG coi là núm cân bằng | J-04:22,33,41; `KNpcResNode.h:23`, `KNpcRes.cpp:1703` |
| Lọc SPR | Sampler / số mip raw | GL_LINEAR min/mag / 1 | lấy mẫu texture, không thêm frame | CẨN THẬN | L-01:21,27; `CCTexture2D.cpp:641,714` |
| Render | Thiết kế / policy | 1040 × 603,2 / EXACT_FIT | đơn vị thiết kế; không phải framebuffer đo | CẨN THẬN | L-01:19,36; `AppDelegate.cpp:55,128` |
| Render | Subpixel Node / SpriteBatchNode | 1 / 1 mặc định | macro; không phục hồi phần lẻ đã mất | CẨN THẬN | L-01:26,32; `ccConfig.h:145,154`, `KSubWorld.cpp:188` |
| Render map | Canvas / mật độ thử A | 512 × 512 logic / q=2 dự kiến | giữ footprint; màu 1→4 MiB/target chỉ khi CSF=1, không padding | CẨN THẬN; chưa triển khai | L-01:74,82; `KgameWorld.cpp:7461,7665` |
| Lọc cạnh | Tỷ lệ thử B | 2× dự kiến | prototype shader, chưa có port xBRZ được kiểm | CẨN THẬN; chưa triển khai | L-01:88,92; hook `KgameWorld.cpp:11374,11386` |
| Render | MAX_MISSLE / MAX_SKILL_STATE | 30.000 / 18 | chỉ số pool / slot trạng thái mỗi NPC | KHÔNG coi là LOD | J-05; `KMissle.h:6`, `GameDataDef.h:132` |

## DE XUAT TOI UU

1. **Ưu tiên hợp đồng dữ liệu trước cân bằng:** khóa manifest phiên bản source/binary/PAK/cấu hình; thống nhất đơn vị tiền, cách đánh số shop/template, tập script nạp và key task đang dùng. Đây là đề xuất cho task sau, không thay dữ liệu trong I-06.
2. **Bảo toàn tiến trình và tiền:** thiết kế kiểm biên 255/256 record khác 0, task 192, login/reset và phát thưởng lặp; kiểm mua/đổi Xu khi túi đầy, cộng thất bại, logout hoặc mất kết nối. Chưa cấp thêm hàng loạt key hảo hữu trước khi kiểm persistence/ABI.
3. **Hoàn thiện atlas chức năng có giới hạn:** nối mẫu map → region → template → script/menu cho shop, kho và quest; dùng kết quả PAK I-03 làm đầu vào, giữ riêng 38 map chưa khớp và spawn động. Không tự tăng Count hoặc sửa MapType để che khoảng trống.
4. **Đo gameplay theo chuỗi:** đối chiếu EXP cơ sở quái → EXP cuối người chơi, cấp/ngũ hành override, đội/cự ly và bảng rơi; giữ riêng các đường AddSelfExp/DirectAddExp/lửa trại. Bộ ca chỉ được chạy ở task/môi trường đã duyệt, không Main VM trong I-06.
5. **Animation: kiểm đúng tầng trước đổi tốc độ/khung:** có manifest asset đúng bản, đếm frame/hướng/action và bảng SORT; kiểm alias state, release trước draw và cleanup owner theo J-03, rồi đo tick/delta/frame index/draw/FPS/frame-time/RAM/texture/dung lượng. Với L-01, hoàn thiện bản thử A cô lập, kiểm alpha/điểm neo/footprint rồi mới cân nhắc B theo whitelist và ma trận +6/+12/+15. Nhận báo cáo J-06 trước quyết định khung giữa hay chi phí APK; không tăng FPS mục tiêu, giảm metadata hoặc đổi LifeTime để che giả thuyết H-14/H-15.

## Kiểm chứng và bàn giao

I-06 đã đối chiếu bảy phần I; I-06b cập nhật độ phủ thành năm báo cáo J-01..J-05 và L-01, giữ rõ nguồn tĩnh, trạng thái và chênh lệch phạm vi. **Độ phủ Animation J-01..J-06 còn PARTIAL do thiếu báo cáo J-06 trong worktree.** Chưa kiểm chứng độc lập source/dữ liệu gốc, chưa chạy game, build, TESTER, benchmark, DB round-trip hoặc thử nghiệm VM. Các đề xuất trên là công việc tiếp nối, không phải thay đổi đã triển khai. Bàn giao gốc tại [I-06](../REPORTS/I-06.md); phần cập nhật, kiểm tra tài liệu và giới hạn tại [I-06b](../REPORTS/I-06b.md).
