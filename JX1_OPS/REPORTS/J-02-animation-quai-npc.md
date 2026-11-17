# TÓM TẮT 5 DÒNG
1. [BẢN NHÁP, XÁC MINH TĨNH] 1.412 template `Kind=0`, 379 appearance type; ghép được metadata cho 1.398 template.
2. `FightStand`: tổng frame min/trung vị/max = 1/80/192; 1.303 template có 8 hướng, 95 có 1 hướng, 14 thiếu metadata.
3. Các trạng thái khác cũng chủ yếu 8 hướng; `Die` max 352, min 1. Một frame ghi trong bảng chưa chứng minh asset/animation runtime chỉ có một hình.
4. Năm `boss160..164` (STT 2429, 2430, 2432..2434) không có hàng metadata trong hai bảng NPC resource đã đối chiếu.
5. Chưa xác minh client PAK/SPR, runtime, build/test; không mạng/VM/exe, không sửa source, Python dùng `python -I`.

## ĐÃ XÁC MINH

- Client gốc: `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client`. Server source: `D:\JX-source\server\jxOnline`. Bảng dữ liệu gốc: `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\Settings`.
- Dữ liệu xử lý tại chỗ bằng Python `-I` và CSV tab-separated, không tạo parser phụ: `Settings/Npcs.txt` có 2.435 hàng, 106 cột; 1.412 hàng `Kind=0`, 379 giá trị `NpcResType` khác nhau. `Settings/NpcRes/普通npc资源.txt` và `普通npc资源信息.txt` có 982 hàng mỗi bảng, 14 cột action; 982 type khớp nhau. Tên file hiển thị theo tên legacy trong checkout.
- Ghép `NpcResType` (khóa type tài nguyên) từ `Npcs.txt` vào metadata: 1.407/1.412 template có hàng resource; 1.398/1.412 có `FightStand` metadata đọc được; 374/379 type có hàng resource/info. 14 template thiếu hàng info; năm type thiếu gồm `boss160..164`. Mẫu theo STT `Npcs.txt`: STT 2429, 2430, 2432, 2433, 2434 (dòng lần lượt STT+1). Đây là thiếu hàng metadata, chưa chứng minh boss không có asset ở nguồn khác.
- `Settings/NpcRes/npc动作表.txt:1-15` có 14 action: `FightStand`, `NormalStand1`, `NormalStand2`, `FightWalk`, `NormalWalk`, `FightRun`, `NormalRun`, `Wound`, `Die`, `Attack1`, `Attack2`, `Magic`, `SitDown`, `JunpFly`. `Classes/gamecore/KNpc.h:104-121` có 15 enum `CLIENTACTION` kể cả `cdo_none`; không giả định enum position bằng action-table order. `KNpcResList.cpp:40-50` khởi tạo hai bảng action/resource; `KNpcResNode.cpp:592-606`: NPC thường dùng doing làm action, NPC đặc biệt tra bảng theo trang bị/ngựa.
- `Settings/NpcRes/普通npc资源信息.txt:1` khai báo mỗi action là bộ `tổng frame, tổng hướng, interval`. `KNpcResNode.cpp:447-465` đọc cho NPC thường; fallback truyền vào là `16,8,0` (không phải đo asset). `KNpcResNode.cpp:570-586` trả tổng frame/hướng; `KNpcRes.cpp:113-115` nạp sprite; `KNpcRes.cpp:261-263` lượng tử hướng 64 cấp theo số direction. C++ xác nhận cấu trúc trường, không xác nhận file SPR có tồn tại/hiển thị đúng.

### Phân bố metadata

Đếm theo template `Kind=0` (template cùng `NpcResType` được nhân trọng số), tổng frame là số trong bảng metadata, không chia cho direction. Dữ liệu mỗi action có 1.359–1.407 template với metadata parse được; thiếu gồm ô trống/lỗi parse và type không khớp.

| Action | N hợp lệ | Tổng frame min / trung vị / max | Số hướng trong mẫu |
|---|---:|---:|---|
| FightStand | 1.398 | 1 / 80 / 192 | 8: 1.303; 1: 95 |
| NormalStand1 | 1.407 | 1 / 80 / 192 | 8: 1.312; 1: 95 |
| NormalStand2 | 1.407 | 1 / 96 / 192 | 8: 1.312; 1: 95 |
| FightWalk | 1.384 | 1 / 112 / 248 | 8: 1.293; 1: 91 |
| NormalWalk | 1.393 | 1 / 112 / 248 | 8: 1.302; 1: 91 |
| FightRun | 1.380 | 1 / 112 / 248 | 8: 1.289; 1: 91 |
| NormalRun | 1.389 | 1 / 112 / 248 | 8: 1.298; 1: 91 |
| Wound | 1.376 | 1 / 48 / 128 | 8: 1.285; 1: 91 |
| Die | 1.375 | 1 / 112 / 352 | 8: 1.284; 1: 91 |
| Attack1 | 1.364 | 1 / 112 / 256 | 8: 1.281; 1: 83 |
| Attack2 | 1.360 | 1 / 112 / 256 | 8: 1.277; 1: 83 |
| Magic | 1.359 | 1 / 112 / 256 | 8: 1.276; 1: 83 |
| SitDown | 1.389 | 1 / 80 / 192 | 8: 1.298; 1: 91 |
| JunpFly | 1.380 | 1 / 112 / 248 | 8: 1.289; 1: 91 |

| Prefix `NpcResType` | Số type | Số template | FightStand min / trung vị / max |
|---|---:|---:|---|
| `enemy` | 158 | 797 | 1 / 80 / 168 |
| `boss` | 135 | 411 | 8 / 80 / 192 |
| `ani` | 49 | 123 | 48 / 96 / 120 |
| `passerby` | 25 | 59 | 1 / 64 / 128 |
| `npc` | 7 | 7 | 64 / 64 / 64 |
| `passerby_*` elemental | 5 | 15 | 1 / 1 / 1 |

Min 1 frame xuất hiện ở nhiều action, trong đó có fixture/passersby; đây là metadata cấu hình, không đủ để kết luận lỗi animation. Mẫu `enemy181` (Npcs STT 447, info line 157) khai 1 frame/1 hướng cho mọi action và tên SPR được tham chiếu nhưng chưa kiểm SPR; đây là ứng viên ít khung nhất trên metadata, chưa xác nhận là quái di động. `enemy178` (`FightStand` 1 frame; Npcs STT 414/586) và `enemy179` (STT 1606/1612/2251) cũng là các type có stand 1 frame nhưng Wound/Die 6–7 frame. Median tổng frame `FightStand` 80 với 8 hướng thường tương ứng 10 frame/hướng nếu chia đều; là phép chia dẫn xuất, chưa phải số hình quan sát được.

Kiểm tính nhất quán: 14 ô metadata có tổng frame không chia hết cho số hướng; phần lớn là boss type (ví dụ `boss014`, `boss015`, `boss017`, `boss025`, `boss016`, `boss149`). Ba template ở hai type `Magic` có số metadata nhưng tên SPR trống (`enemy044`: 2; `enemy046`: 1); loader có thể giữ metadata dù không có tên file. Đây là các mục cần đối chiếu asset/loader, không tự kết luận lỗi.

### Boss và liên hệ

- `Settings/npc/NpcGoldTemplate.txt:2-17` có 16 hàng golden; đây là tầng chỉ số/loại golden, không phải bảng animation. Không gộp 16 loại này với 135 `boss*` type resource.
- Năm type `boss160..164` trong Npcs STT 2429,2430,2432,2433,2434 thiếu hàng ở resource và info table. Bốn STT 2429,2430,2432,2433 dùng LevelScript `makeboss.lua`; STT 2434 `boss162` dùng `animal.lua`. Không suy diễn bốn boss mùa vụ có animation/asset riêng từ tên hoặc script.
- Liên hệ H-14: frame interval/action SPR là đầu vào animation, còn FPS/hiệu ứng và chi phí render cần kiểm runtime; không tối ưu bằng cách giảm số frame metadata đơn lẻ. Không tìm thấy `JX1_OPS/TASKS/J-05.md` hoặc báo cáo J-05 trong danh sách task/report hiện có để đối chiếu thêm.

## CHƯA XÁC MINH

- Client checkout không có `.pak` trong cây client, còn `Resources` không chứa SPR NPC. Config gốc tham chiếu `data/spr.pak` và resource package; không thể kiểm asset/frame decoded hay đối chiếu bản server metadata với client runtime.
- Chưa xác định `Kind=0` nào là sinh vật di động hay fixture/static; không đánh dấu nhóm min-1 là lỗi. `enemy181` (STT 447, mọi action khai 1 frame/1 hướng) là ứng viên thấp nhất theo metadata, chưa xác nhận là quái di động.
- Chưa xác minh action fallback khi thiếu tên/cột, loop/hold/direction ở engine, boss spawn runtime, chất lượng hình, FPS/chi phí; không build/test/game/exe, mạng hay VM.
- Trạng thái bản nháp: **PARTIAL**. Chưa ghi `## Kết quả` vào file task vì vùng ghi khai báo `vung_file: [none, JX1_OPS/REPORTS/J-02-*.md]`; chỉ báo cáo này nằm trong phạm vi được phép sửa.

## ĐỀ XUẤT TỐI ƯU

- Trước khi tối ưu, cung cấp/bảo toàn đúng client `spr.pak` và các bảng `Settings/NpcRes`; kiểm hash/phiên bản client-server rồi xác minh nhóm một-frame và năm boss thiếu metadata.
- Với H-14/J-05, đo cùng mẫu SPR ở đủ hướng/action: số frame thực, interval, frame giữ/chuyển, hướng lượng tử, FPS và chi phí render. Không sửa số metadata để che thiếu sprite hoặc lệch chỉ số trước khi đo.
- Giữ nguyên source trong khảo sát này. Chưa có thay đổi mã được đề xuất; cần kết quả asset/runtime trước khi xác định tối ưu.

## MỤC SỔ THÔNG SỐ

| Nhóm | Tên/hằng số | file:line | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Metadata | fallback `NormalNpcSprInfo` | `Classes/gamecore/KNpcResNode.cpp:458` | `16,8,0` | tổng frame, hướng, interval | giá trị dùng khi thiếu ô metadata; có thể làm thiếu asset trông như animation 16×8 | CẨN THẬN | SOURCE, chưa đo SPR |
| Cấu trúc | `MAX_ACTION` | `Classes/gamecore/KNpcResNode.h:27` | 128 | action tối đa | cap bảng action; tăng/giảm có thể ảnh hưởng index/tải dữ liệu | KHÔNG | SOURCE |
| Cấu trúc | `MAX_PART` | `Classes/gamecore/KNpcResNode.h:23-25` | 24 | part slot | kích thước bảng resource/sort | KHÔNG | SOURCE |
