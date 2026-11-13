# 54 – U003 Thiết kế kiến trúc (sau G0)

Phạm vi: CHỈ tài liệu thiết kế. Chưa tạo Unity project, không build APK, không cài package, không sửa source/PAK/server/DB/VM, không đụng Goddess/EXE, không đụng U001/U002, không push.
Nguồn: báo cáo 51, 52, 53, `BAI_HOC.md`, cộng một lần đọc thêm `gamecore/KSubWorld.cpp` (mục C2).
Nhãn: **CONFIRMED** (đã đọc code/dữ liệu, có bằng chứng) · **DESIGN DECISION** (đã duyệt hoặc đề xuất thiết kế, không phải sự thật của game gốc) · **HYPOTHESIS** (suy luận chưa kiểm) · **UNKNOWN** (chưa biết). Đường dẫn code tính từ `Client2912/Client/Classes/`.

## TÓM TẮT 5 DÒNG
1. Kiến trúc 5 khối: AssetPipeline (offline, giữ nguyên gốc) → AnimationSystem → MapRenderer (port KIpoTree sang C#) → CombatSystem (mô phỏng theo giây, độc lập FPS) → UI.
2. Port KIpoTree theo đúng quy tắc gốc; điểm chân y+6 tính trong toạ độ MPS (y gấp đôi y màn hình), đã xác minh công thức đổi ở mục C2.
3. Mọi timer dùng đồng hồ mô phỏng tính bằng giây (accumulator, bước cố định), không đếm khung hình.
4. Còn nhiều chỗ UNKNOWN chặn việc triển khai: giải mã khung SPR, ánh xạ hướng→Dir1..16, nhịp animation, vị trí 15 spawn, ngữ nghĩa sát thương skill 375. Xem mục G.
5. Chưa có phần nào được TESTED bằng chạy thật; mọi test nằm ở kế hoạch (mục F).

Cần tôi quyết định: có (danh sách ở mục G).

## 0. Quyết định đã duyệt (DESIGN DECISION)
| # | Quyết định |
|---|---|
| 1 | Quái đầu tiên: ani001 |
| 2 | Port quy tắc thuật toán cây KIpoTree sang Unity; Y-sort đơn giản không phải giải pháp cuối |
| 3 | Giữ điểm chân y+6 theo logic gốc, phải xác minh quy đổi toạ độ |
| 4 | Cơ sở asset: `Resources/package.ini` (bản A); CHƯA kiểm tra file trên điện thoại |
| 5 | Skill 375 dùng chuỗi hiệu ứng gốc đã xác minh |
| 6 | Cooldown U003 = 1 s, thiết kế riêng, KHÔNG phải cooldown gốc của 375 (gốc `TimePerCast=0`) |
| 7 | Tick 20 sát thương / 500 ms là luật chiến đấu riêng của U003 |
Còn lại đã chốt từ trước: tên "JX1 Unity U003 – Idle Combat World"; bảng thứ tự vẽ lấy từ `updata02.pak`; map 45 là ứng viên (chưa xác nhận chính thức).

## A. Asset pipeline

### A1. Sự thật đã biết
- **CONFIRMED** Client nạp `data/package.ini` (`gamescene/KUpdateLayer.cpp:831`, `copyData :217,629`); PAK đứng trước trong danh sách thắng khi trùng id (`KPakList.cpp:66-77`); khoá đọc "0","1",… (`:171-200`); id = hash tên GBK chữ thường.
- **CONFIRMED** md5 `package.ini` trong 7 APK (fix33–36, p46, p47, tick) = `Resources/package.ini` (bản A). Bản B (`data/data/package.ini`) và `jxmobile.apk` gốc khác. **UNKNOWN**: file thực tế trên điện thoại.
- **CONFIRMED** Công cụ đọc PAK: `docs-analysis/tools/pak_extract.py` (`read_pak`/`extract`). Workspace trích: `D:\JX1_U003_work\extract\<id>__<pak>.bin` + `_index.tsv`, bảng người thắng `pak_winner.tsv`.
- **CONFIRMED** Header SPR: `<HHHHHHHH>` tại offset 4 = (W, H, cx, cy, frames, colors, dirs, interval) (báo cáo 52).
- **UNKNOWN** Định dạng khung/RLE/bảng màu của SPR chưa được đọc (mới đọc header). Phải đọc `engine/` (loader SPR) trước khi viết decoder.
- **CONFIRMED** Một entry (`kl_02_疾电法b.spr`) lỗi giải nén UCL; không thuộc skill 375.

### A2. Thiết kế
1. **Hai tầng tách biệt**: (a) *Nguồn gốc* chỉ đọc – PAK trong `data_cdn`, không sửa; (b) *Bản trích* – sinh ra một lần bởi công cụ offline, nằm ngoài dự án Unity.
2. **Công cụ offline (Python, chạy `-I`)** tạo bản trích tối thiểu cho U003, KHÔNG nhét PAK nguyên vào APK:
   - Đọc `package.ini` bản A → dựng chỉ mục id→(pak, offset) theo luật "PAK đầu thắng".
   - Danh sách yêu cầu (manifest) liệt kê đường dẫn gốc cần dùng; công cụ ghi lại: đường dẫn gốc, id hash, pak thắng, kích thước, SHA256 của bytes giải nén.
   - Mỗi SPR → (1) giữ file `.spr` nguyên bytes, (2) sinh atlas PNG + JSON siêu dữ liệu (W,H,cx,cy,frames,dirs,interval, bảng offset khung). Sinh PNG là dẫn xuất, luôn tái tạo được từ `.spr`.
3. **Nguyên tắc giữ dữ liệu gốc**: không đổi tên đường dẫn gốc (giữ nguyên chuỗi GBK dạng UTF-8 trong manifest); mọi giá trị bảng (NpcS, Skills, Missles, sort table) xuất sang JSON kèm `source_file`, `source_line`; mọi chỉnh sửa/đặt giá trị riêng của U003 nằm ở file cấu hình U003 riêng, tách khỏi dữ liệu gốc.
4. **Kiểm chứng**: sau khi dựng decoder, so khớp số khung × kích thước với header cho 100% entry trong manifest; lưu báo cáo kiểm; hash từng PNG sinh ra để phát hiện thay đổi ngoài ý muốn.
5. **Nạp animation 8 hướng**: JSON mô tả `dirs`, `frames/dir`, `interval`; khung sắp theo hướng-chính (frame = dir × framesPerDir + i) – **HYPOTHESIS** (cần đọc loader để xác nhận thứ tự khung trong file).
6. **Pháp lý/an toàn**: asset gốc đã trích không đưa vào git/GitHub; chỉ văn bản đã lọc lên repo báo cáo.

### A3. Danh sách asset tối thiểu (CONFIRMED tồn tại, báo cáo 52)
ani001 (6 sprite st/pst/wlk/bat/die/at, 320×320, 8 hướng, ~1895 KB); icon `\spr\Ui\skill\雷动九天.spr` (36×36); cast `\spr\skill\昆仑\kl_16_魔法施放.spr` (260×260, 10 khung, interval 50); missile 181 `\spr\skill\kl\雷动九天.spr` (400×400, 6 khung); nổ `\spr\skill\昆仑\Bz_dian3_爆炸.spr` (320×320, 8 khung, interval 40); missile 193 `\spr\skill\tm\雷击术.spr` (27 khung); âm thanh `\sound\skill\五雷正法m.wav/f.wav`; nhãn auto `\spr\Ui3\剑侠助手\state_autofight.spr`; HP cầu `\ui\main\life\hongbanqiu_NN.png`; font số `fonts/number_16_r.fnt`/`_w.fnt` (có ở `Resources/fonts`, không trong PAK); joystick `yaoganz.png`/`yaoganx.png`; mặt nạ `mainskillmix.png`.

## B. Animation system

### B1. Nhân vật nhiều bộ phận
- **CONFIRMED** Slot theo `nhóm*4+phần` (MAX_BODY_PART=6, SECT=4; `KNpcResNode.h:23-24`); 12 slot dùng trong bảng MainMan: 0 head, 1 hair, 4 shoulder, 5 body, 6 left_hand, 7 right_hand, 8 left_weapon, 9 right_weapon, 12/13/14 horse front/mid/rear, 16 cape; không có cánh (slot 20) trong bảng thắng.
- **CONFIRMED** Bảng thứ tự vẽ: `男主角贴图顺序表.txt` bản `updata02.pak` (44 section, 148 Dir + 301 Line); [DEFAULT] UnitNum=14, DirNum=18, Dir1..16 khoá đầu −1; Line khoá đầu = số khung. Đã đối chiếu 495/495 dòng với JSON (`json/sort_table_MainMan.json`). Dùng ở `KNpcRes.cpp:422,665-679`.
- **DESIGN DECISION** Lớp `PartStack`: mỗi (hành động, hướng, khung) tra bảng → danh sách slot theo thứ tự vẽ → vẽ lần lượt thành các `SpriteRenderer` con (sortingOrder cục bộ tăng dần) của một nhân vật. Bảng nạp từ JSON, không hard-code.
- **UNKNOWN** Ánh xạ hướng game (8 hướng của sprite / 64 hướng logic) → khoá Dir1..16 và `DirNum=18`. Phải đọc `KNpcRes.cpp:665-679` + `CSortTable::GetSort :1390` và lập bảng quy đổi trước khi làm B1. Cách chọn sprite bộ phận cho từng trang bị: ngoài phạm vi U003 (nhân vật mặc cố định, **cần quyết định bộ trang bị** – mục G).
- **UNKNOWN** Tên hành động ↔ khóa section trong bảng (ví dụ đứng/chạy/đánh/cast) chưa lập bảng đối chiếu.

### B2. Quái ani001
- **CONFIRMED** 2 hàng NpcS đều Kind=0; 6 sprite st/pst/wlk/bat/die/at đủ; 8 hướng; khung/hướng: st12 wlk15 bat8 die10 at12; interval header: st116 wlk84 bat75 die100 at80; AttackSpeed=18; ReviveFrame=810.
- **DESIGN DECISION** Quái là 1 sprite (không nhiều bộ phận), máy trạng thái: Idle(st) → Walk(wlk) → Attack(at) → Hit/Battle(bat) → Die(die) → Respawn. Hoạt ảnh `pst` (ngồi/đứng chờ?) – **UNKNOWN** dùng khi nào; không dùng ở bản đầu.
- Quái tấn công "theo animation/config": thời điểm gây sát thương = khung cố định trong clip `at` (tham số cấu hình `hitFrame`), **DESIGN DECISION**; giá trị chưa chọn (G).

### B3. Tốc độ animation tách khỏi FPS
- **DESIGN DECISION** Mỗi clip có `frameDuration` (giây) và phát bằng `t += dt` (đồng hồ mô phỏng), `frameIndex = floor(t / frameDuration) % n` — không tăng chỉ số mỗi Update.
- **HYPOTHESIS** `interval` trong header SPR là mili-giây mỗi khung (st116 → 8.6 khung/s…); chưa xác minh đơn vị. Cách kiểm: đọc `engine/` nơi dùng `nInterval` và/hoặc quay clip gốc so với client. Đến khi xác nhận, `frameDuration` = tham số cấu hình, mặc định theo giả thuyết ms, ghi rõ là giả thuyết.
- **CONFIRMED** Gốc kéo giãn animation đánh theo `nTotalFrame = m_AttackFrame*naAttackSpeed/(nbAttackSpeed+m_CurrentAttackSpeed)` (`KNpc.cpp:2381`); `AttackSpeed` là số khung game (`KNpcTemplate.cpp:50`). Hz của client **UNKNOWN**; Hz của server 18 (TESTED ở báo cáo 41, trước đó). Do đó "tốc độ đánh ani001 = 18/18 s" chỉ là **HYPOTHESIS**; U003 đặt `attackCycleSeconds` riêng (DESIGN DECISION, giá trị ở mục G).

## C. Map renderer

### C1. Dữ liệu bản đồ (CONFIRMED, báo cáo 52)
- `\maps\<MapList path>.wor` là INI nhỏ (`KScenePlaceC.cpp:578`). Địa hình: `\maps\<path>\v_<yyy>\<xxx>_Region_C.dat` (`KScenePlaceRegionC.cpp:93`, `SceneDataDef.h:12-13`). Vùng 512×1024 px MPS, lưới 16×32 px/ô; file gộp 6 phần: obstacle (512×4 byte), trap, npc, obj, ground (gạch spr+frame, cover objects), buildin (Tree/Line/Point/Above, mỗi KBuildinObj có 4 ImgPos và `Props`). Đã parse thật 3 vùng của map 凤翔.
- Map ngoài trời nhỏ nhất: id 45 `中原北区\天忍教\天忍教室外` 14×10 vùng (ứng viên, chưa xác nhận map 45 đủ `Region_C.dat`/số cây – **UNKNOWN**).

### C2. Quy đổi toạ độ (đã xác minh công thức — mục 3 của quyết định)
- **CONFIRMED** (`gamecore/KSubWorld.cpp:188-192`, bản đang hiệu lực; bản thay thế ở `:262-277` nằm trong khối chú thích `/* … */` bắt đầu `:260`, kết thúc `:325`):
  - `screen_x = mps_x − m_nLeft`
  - `screen_y = mps_y / 2 − m_nTop − ((z * 887) >> 10)`
  - ngược lại: `mps_y = (screen_y + m_nTop + ((z*887)>>10)) * 2`.
  → MPS có trục y gấp đôi màn hình (phối cảnh 2:1), z đổi sang pixel màn hình bằng hệ số 887/1024.
- **CONFIRMED** Vùng chia bằng `x>>9`, `y>>10` trên toạ độ MPS (`KScenePlaceC.cpp:1457-1458`), tức MPS: vùng 512×1024.
- **CONFIRMED** Lá runtime lưu `oPosition = (x, y + POINT_LEAF_Y_ADJUST_VALUE)` với `POINT_LEAF_Y_ADJUST_VALUE=6` (`KIpotLeaf.h:20`; `KScenePlaceC.cpp:1415,1479`). `x,y` truyền vào `MoveObject` là toạ độ MPS (suy từ phép chia vùng ở trên; **chưa kiểm** từng nơi gọi, ví dụ `KNpcRes.cpp:215`) ⇒ +6 là +6 đơn vị MPS = +3 pixel màn hình.
- **CONFIRMED** Logic cell cơ sở 32×32 (`defLOGIC_CELL_WIDTH/HEIGHT`, `KSubWorld.cpp:28-29`); `m_nCellWidth/Height` thực tế nạp từ dữ liệu (**giá trị chưa đọc**).
- **UNKNOWN** Toạ độ (x,y) của vật thể nền trong `buildin` đã ở MPS hay ở toạ độ vùng cục bộ; phải cộng offset vùng (`regionX*512`, `regionY*1024`) – kiểm bằng cách đặt vật thể đã parse cạnh gạch ground ở cùng vùng và so sánh với ảnh client.
- **Việc cần làm trước C3**: một bài kiểm toạ độ (xem F-C0) – dựng lại 1 vùng, so từng gốc cây/nhà với ảnh chụp client.
- **DESIGN DECISION** Trong Unity giữ MPS làm hệ toạ độ thế giới của logic; chuyển sang vị trí hiển thị bằng một hàm duy nhất `MpsToWorld(x,y,z)` theo công thức trên (đơn vị: 1 px = 1/PPU). Y-trục Unity hướng lên ⇒ đảo dấu một lần ở hàm này.

### C3. Port KIpoTree sang C# (DESIGN DECISION, dựa trên CONFIRMED bên dưới)
Cấu trúc (CONFIRMED, báo cáo 53 mục A): nhánh = đường (`head`,`end`), 2 phía (0 = UP/xa, 1 = còn lại) là nhánh con hoặc danh sách lá; lá = `BuildinObj` hoặc `RuntimeObj`; `IPOT_BRANCH_FLAG` đánh dấu con là nhánh/lá.

Các lớp C#:
- `IpotLeaf` (loại, `Position`, `pBrother`, `pLChild`, `pRChild`), `IpotBuildinObj : IpotLeaf` (`EndPos`, `Props`, `AngleXY`, `NodicalY`, 4 ImgPos), `IpotRuntimeObj : IpotLeaf` (`ParentLeaf/ParentBranch`, `AheadBrother`, `LayerFlags`).
- `IpotBranch`: `AddBranch`, `AddLeafLine`, `AddLeafPoint`, `AddPointLeafToList`, `AddLineLeafToList`, `PaintObjectLayer` (trả về danh sách vẽ có thứ tự thay vì gọi vẽ trực tiếp).
- `IpoTree`: `MainBranch`, `DefaultBranch`, `PermanentLeaf`; `AddBranch/AddLeafLine/AddLeafPoint/PluckRto/StrewRtoLeafs/SetPermanentBranchPos`, `Paint(layer)`.
- `MapBuilder`: dựng cây đúng như `KScenePlaceC.cpp:1905-2063`.

Hàm cần port (bằng chứng ở báo cáo 53): `KIpotBranch.cpp:67-173` (vẽ), `:198-292` (AddAObject/AddBranch), `:381-645` (thêm lá); `KIpoTree.cpp:108-132,187-199,240-249,386,406,428`; `KIpotLeaf.cpp:19,125-276,277`; dựng cây `KScenePlaceC.cpp:1905-2063`.

Phụ thuộc chưa đọc đầy đủ (**UNKNOWN**, bắt buộc đọc trước khi viết code): `SM_Relation_PointLine`, `SM_Relation_LineLine_CheckCut`, `SM_Distance_PointLine`, `SM_IsLineLinkable` (định nghĩa, thứ tự tham số, kiểu số học, dung sai); `KIpotBranch.cpp:90-173` chi tiết cắt ảnh (`bImgPart`); `KIpotLeaf.cpp:125-276` (`PaintABuildinObject`); header `KIpotLeaf.h` (hết enum); `KIpoTree.cpp:108-132` + nơi gọi `Paint(...)` để biết phần `EnumerateObjects`.

Quy tắc port: số học dùng đúng kiểu gốc (int/float) để cùng kết quả ở biên (so sánh `>`/`>=` giữ nguyên); không tối ưu cấu trúc ở bản đầu; thêm `Dump()` in cây dạng văn bản để diff với trạng thái mong đợi.

### C4. Nhân vật và quái như đối tượng động
- **CONFIRMED** Gốc: đổi toạ độ ⇒ `PluckRto` → cập nhật `oPosition` → `AddLeafPoint`; đứng yên thì không làm gì (`KScenePlaceC.cpp:1444-1516`). Có khoá `m_ProcessCritical` (đa luồng).
- **DESIGN DECISION** `MapRenderer.MoveObject(id, mpsX, mpsY, layers)` giữ y hệt quy tắc đó, đơn luồng (không cần khoá). Mỗi frame hiển thị: lấy danh sách vẽ đã sắp từ cây và gán `sortingOrder` tăng dần cho từng mục (mỗi mục là 1 renderer/nhóm renderer của một vật thể hoặc một đối tượng động, nhân vật đi cùng PartStack).
- Lớp (CONFIRMED, `SceneDataDef.h:55-58`): COVER_GROUND 1, OBJECT 2, INFRONTOF_ALL 4, LIGHT_PROP 8. Thứ tự toàn cảnh (`KScenePlaceC.cpp:1621-1645`): ground → COVER_GROUND → OBJECT → Above (nếu không ẩn) → INFRONTOF_ALL. Missile/hiệu ứng skill: `OBJECT` (`KMissle.cpp:514,520`); tên/HP bar: lớp INFRONTOF_ALL.
- **DESIGN DECISION** Lớp INFRONTOF_ALL và UI là Unity canvas/sorting layer riêng, đứng trên cùng.

### C5. Tree / Line / Point / Above
- **CONFIRMED** (báo cáo 53 A3) Tree: gom theo `SM_IsLineLinkable`, sắp x, nhóm dài nhất lên trước, `AddBranch`; Line: sắp độ dài giảm dần, `AddLeafLine` (hộp ±7); Point: `AddLeafPoint`, nếu trong hộp một Line (±13 ngang, −3/+128 dọc) thì thành con trái/phải của Line; Above: `m_pObjsAbove` vẽ riêng `PaintAboveHeadObj_old` sau OBJECT (`KScenePlaceC.cpp:1637-1643`), có công tắc `nIsHideTreeAndBuilding`.
- **DESIGN DECISION** Giữ công tắc ẩn Above (mặc định hiện, như gốc).

### C6. Nhánh giao nhau và trường hợp đặc biệt
- **CONFIRMED** `AddBranch` dùng `SM_Relation_LineLine_CheckCut`: UP→phía 0, DOWN→phía 1, ON→cùng nhánh, CROSS→`Clone(&poi)` cắt đối tượng tại giao điểm thành 2 nửa (`KIpotBranch.cpp:235-292`, `KIpotLeaf.cpp:277`). Nửa bị cắt vẽ bằng `bImgPart` (cắt ảnh theo đoạn x) (`KIpotBranch.cpp:90-173`).
- **DESIGN DECISION** Port đúng quy tắc cắt; bản đầu `Clone` tạo 2 `IpotBuildinObj` chia sẻ cùng sprite với vùng cắt khác nhau (UV rect/`SpriteMask`); chưa tối ưu.
- **UNKNOWN** Hành vi khi nhiều nhánh cắt chéo lồng nhau; phép `Clone` trong `KIpotLeaf.cpp:277` có tính lại ImgPos thế nào; các lá `pLChild/pRChild` khi `Clone`. Phải đọc và test (F-C3).
- **CONFIRMED (báo cáo 53)** `StrewRtoLeafs` dùng `||` thay `&&` ở điều kiện giữ (`KIpoTree.cpp:443-446`): gần như luôn giữ. **DESIGN DECISION**: port đúng hành vi gốc; không "sửa".
- **CONFIRMED** `FillLineObstacle`/`RenderLightMap` chỉ cho ánh sáng; **không port** ở U003 (không dùng ánh sáng động). Vật cản đi lại dùng lớp `obstacle` của Region_C.dat.

### C7. Kiểm thử bằng ảnh đối chiếu
- Hai nguồn đối chiếu: (a) ảnh chụp client gốc ở cùng toạ độ camera (cần quy trình chụp – **UNKNOWN**, vì không được chạy client/VM mới; có thể dùng client APK sẵn có trên điện thoại, cần chủ máy chụp màn hình); (b) so sánh danh sách vẽ của cây C# với kỳ vọng tay cho cảnh đơn giản.
- Cảnh kiểm thử tổng hợp (không cần client): dựng bản đồ nhỏ tự tạo chứa 1 cây (Tree), 1 tường (Line), 1 bụi (Point), 1 mái (Above) + nhân vật đi quanh; xuất ảnh theo từng bước di chuyển và so sánh với bảng kỳ vọng. Chi tiết ở mục F.

## D. Combat system (DESIGN DECISION, trừ khi ghi khác)

### D1. Đồng hồ và quy ước
- Một `SimClock` chạy bước cố định `Δ = 1/60 s` (accumulator, tối đa 5 bước bù/khung để tránh xoắn ốc); tất cả timer là thời điểm tuyệt đối theo giây mô phỏng (`castStart`, `nextTickAt`, `cooldownEndAt`, `respawnAt`). Không có bộ đếm "khung". Pause/focus loss: đồng hồ dừng.
- Sự kiện thời gian (tick 500 ms) xử lý bằng vòng `while (now >= nextTickAt) { Tick(); nextTickAt += 0.5 }` để FPS thấp không làm mất tick.

### D2. Thông số U003 (đã duyệt)
| Tham số | Giá trị |
|---|---|
| HP nhân vật | 500 |
| HP quái | 100 |
| Respawn quái | 2 s |
| Cast skill 375 | 1 s |
| Tick sát thương | 500 ms, 20 sát thương/tick |
| Cooldown skill 375 | 1 s (thiết kế riêng, không phải gốc) |
Hệ quả số học: một lần cast đủ 1 s có tối đa 2 tick = 40 sát thương lên mỗi mục tiêu nằm trong vùng; quái 100 HP cần ≥3 lần cast nếu chỉ dùng skill. **Cần xác nhận** có tick tại t=0.5 và t=1.0 hay tại t=0, 0.5 (mục G).

### D3. Auto attack
- Máy trạng thái nhân vật: Idle → (có quái trong tầm tìm) → Chase → Attack/Cast → …; Auto bật: tự chọn quái gần nhất trong `searchRadius`, đi tới tầm `attackRange`, đánh thường; dùng skill 375 khi sẵn sàng (hết cooldown). Auto tắt: chỉ di chuyển bằng joystick, các nút bấm tay hoạt động.
- Tầm tìm, tầm đánh, sát thương đánh thường nhân vật, và thứ tự ưu tiên skill/đánh thường: **UNKNOWN/ chưa chọn** (mục G). Không suy từ gốc (`mainSkillattack` gốc phức tạp, chưa port).

### D4. Quái tấn công
- Quái: Idle/đi lang thang → thấy nhân vật trong `aggroRadius` → đuổi → tấn công. Chu kỳ tấn công `attackCycleSeconds` (config), thời điểm gây sát thương tại `hitFrame` của clip `at` (đồng bộ với animation: `hitTime = hitFrame*frameDuration`). Sát thương quái lên nhân vật và `aggroRadius`: chưa chọn (G).
- Nhân vật HP 500; khi về 0: **chưa chọn** (chết/hồi sinh/ thua) – G.

### D5. Respawn
- Quái chết ⇒ phát `die`, sau 2 s kể từ lúc chết (`respawnAt = deathTime + 2`) xuất hiện lại tại điểm spawn với HP 100. Vị trí 15 điểm spawn: dữ liệu client **không có** (UNKNOWN); U003 tự định nghĩa (G).
- Quy tắc gốc `ReviveFrame=810` của ani001 **không dùng** (khác 2 s); ghi nhận để so sánh.

### D6. Skill 375 – chuỗi hiệu ứng gốc (CONFIRMED dữ liệu; DESIGN DECISION cách dùng)
- Skill Id 375 (`Skills.txt` dòng 376): `MisslesForm=6` (hình dạng, `SkillDef.h:117-127`), `BaseSkill=1` ⇒ `CreateMissle(..., ChildSkillId)` (`KSkills.cpp:1775,1929`); ChildSkillId=375 ⇒ Missles 181 ×4; `DmgInterval=10`, `LifeTime=12`, `CollidRange=2` (đơn vị khung game); nổ `Bz_dian3_爆炸`; khi va chạm `CollidSkillId=387` ⇒ Missles 193 (`雷击术`, 27 khung, `IsRangeDmg=1`, `DmgInterval=4`). Cast animation `kl_16_魔法施放` (260×260, 10 khung, interval 50). Âm thanh `五雷正法m/f.wav`. `WaitTime` = độ trễ sinh đạn (`KSkills.cpp:3090-3120`). Server `kunlun.lua:199-239`: không có tick 500 ms (số này là luật U003).
- **DESIGN DECISION** Chuỗi trình diễn: t=0 phát cast `kl_16` trên nhân vật → sinh 4 missile 181 hướng về mục tiêu (hay vùng) → khi chạm: nổ `Bz_dian3` + sinh missile 193 tại vị trí chạm. Phần hình ảnh/âm thanh dùng nguyên chuỗi gốc; **sát thương KHÔNG** lấy từ dữ liệu gốc (80/260/470) mà từ luật U003 (20/tick).
- **UNKNOWN / cần chốt** Gắn tick 500 ms vào đâu: (i) vào missile 193 (vùng sát thương, `IsRangeDmg`), (ii) vào một vòng quanh nhân vật trong suốt 1 s cast, (iii) lên mục tiêu đã chọn. Cách 4 missile 181 chia hướng/vị trí: dữ liệu `Missles` chưa dịch ra bố cục (`MisslesForm=6` ý nghĩa hình học chưa đọc `KMissle.cpp`). Nguồn thời gian missile (`LifeTime=12`, `DmgInterval=10` đơn vị khung ⇒ giây?) phụ thuộc Hz client (UNKNOWN) – dùng thời lượng animation thay vì quy đổi khung (DESIGN DECISION).

### D7. Cooldown
- Cooldown U003 1 s bắt đầu từ lúc kết thúc cast hay từ lúc bắt đầu cast: **chưa chốt** (G). Gốc (`KNpc.cpp:2260`) `NextCastTime = now + GetDelayPerCast` với `TimePerCast=0` ⇒ không có cooldown riêng; cast liên tiếp bị giới hạn bởi hoạt ảnh. Nhắc lại: cooldown 1 s là thiết kế U003, không có tương đương gốc cho 375.

## E. UI

| Phần | Loại | Ghi chú / bằng chứng |
|---|---|---|
| HP bar quái / đầu NPC | UI gốc đã tìm | sprite trong SpriteBatchNode `ui/state/normal.png` (uinew.pak, 2842 B), tỉ lệ `m_CurrentLife/m_CurrentLifeMax` (`KgameWorld.cpp:655,9321-9323`) |
| HP nhân vật | UI gốc đã tìm | quả cầu `\ui\main\life\hongbanqiu_NN.png` (updata03.pak); U003 có thể dùng thanh đơn giản – **DESIGN DECISION chưa chốt** (G) |
| Số sát thương | Tự xây (dựa font gốc) | gốc: `CCLabelBMFont` `fonts/number_16_r.fnt`/`_w.fnt` (`KgameWorld.cpp:9259`), chỉ đặt vị trí theo NPC; không thấy hiệu ứng bay lên ⇒ U003 tự thiết kế (bay lên + mờ dần, thời lượng cấu hình) |
| Joystick | UI gốc đã tìm (asset) | `KHRocker.cpp`, `yaoganz.png`/`yaoganx.png`; logic đọc hướng cần tự xây |
| Nút Auto | UI gốc đã tìm (cơ chế) + tự xây | gốc: `autoCallback_` (`KgameWorld.cpp:1885,4291`), `startOpenAuto` bật/tắt `KuiAutoPlay::setAutoPlay` (`:2178-2203`); nhãn trạng thái `state_autofight.spr` (`:10013`). U003: nút bật/tắt 1 chạm, không dùng bảng trợ thủ |
| Nút skill 375 | Asset gốc + tự xây | icon `雷动九天.spr`; khung nút/mặt nạ tròn `mainskillmix.png` (`KgameWorld.cpp:12758`) |
| Hiển thị cast U003 | Tự xây | thanh/vòng tiến trình 1 s (ProgressTimer của `KgameWorldVN.cpp:1008-1034` là chỉ báo pin, KHÔNG dùng làm tham chiếu cooldown) |
| Hiển thị cooldown U003 | Mẫu gốc + tự xây | gốc: `timeLoopLayer` (`CCLayerColor(0,0,0,100)` cắt tròn bằng `ClippingNode`) co `scaleY` theo `(nextUseTime − now) * nPer` (`KgameWorld.cpp:5527-5540`, `:12886-12905`), `nPer=1/GetDelayPerCast` (`:5561`). U003 dùng cùng kiểu co dần, nhưng với 1 s thiết kế riêng, + chữ số giây (`cdLabel` gốc chỉ thấy tạo, chưa thấy gán chữ) |
Quy ước: UI gốc dùng lại asset (sau khi trích); mọi logic UI viết lại bằng uGUI; kích thước theo safe-area, ưu tiên điện thoại (Xiaomi 13T Pro).

## F. Kế hoạch kiểm thử
(Chưa thực hiện – TESTED hiện = không có.)

| Mã | Nội dung | Cách | Tiêu chí đạt |
|---|---|---|---|
| F-A1 | Giải mã SPR | so khung×kích thước với header cho mọi entry trong manifest; hash lặp lại | 100% khớp, 0 lỗi (entry UCL lỗi ghi riêng) |
| F-A2 | Tra id/PAK thắng | so `pak_winner.tsv` với kết quả công cụ cho mọi asset trong manifest | khớp 100% |
| F-B1 | 8 hướng | hiển thị ani001 và nhân vật đủ 8 hướng × từng clip; chụp lưới ảnh | không thiếu/đảo hướng so với client (ảnh đối chiếu) |
| F-B2 | Thứ tự bộ phận | với mỗi (hành động, hướng, khung) trong bảng MainMan: so thứ tự vẽ sinh ra với JSON; thêm chụp mẫu 5–10 ca | 495/495 dòng khớp danh sách; mẫu ảnh đúng |
| F-B3 | Nhịp animation | ghi thời lượng chu kỳ thật ở 30/60/120 FPS giả lập | sai lệch < 1 khung giữa các FPS |
| F-C0 | Toạ độ | dựng lại 1 vùng map; so gốc cây/nhà với ảnh client; kiểm công thức `MpsToWorld` (z, 2:1) | lệch ≤ 1 px |
| F-C1 | Đi trước/sau cây | cảnh tổng hợp: nhân vật đi vòng 1 cây ở 8 hướng, bước nhỏ | thứ tự vẽ đổi đúng tại đường nhánh; đối chiếu ảnh |
| F-C2 | Tree/Line/Point/Above | cảnh tổng hợp 4 loại + công tắc ẩn Above | đúng thứ tự lớp (mục C4) |
| F-C3 | Hai nhánh giao nhau | cảnh có 2 Tree cắt chéo, nhân vật đi qua giao điểm; kiểm `Clone` hai nửa | không nhấp nháy/nhảy lớp; hai nửa liền ảnh |
| F-C4 | Dump cây | `Dump()` so với kỳ vọng tay cho cảnh nhỏ | khớp |
| F-D1 | Damage tick khi FPS đổi | chạy giả lập 15/30/60/144 FPS (khóa FPS giả và khung dài ngẫu nhiên) với cast 1 s | số tick và sát thương cuối cùng đồng nhất: 40 (hoặc theo quy tắc chốt) ở mọi FPS |
| F-D2 | Timer khác | cooldown 1 s, respawn 2 s, chu kỳ đánh | sai lệch ≤ 1 bước mô phỏng (1/60 s) |
| F-D3 | Auto | quái ở nhiều vị trí; auto bật/tắt | luôn chọn mục tiêu gần nhất hợp lệ; không kẹt |
| F-E1 | UI | HP bar, damage number, nút cooldown ở nhiều độ phân giải/ safe-area | không bị cắt, đúng tỷ lệ |
| F-S1 | 15 điểm spawn | sinh/respawn 15 quái ở 15 điểm | mỗi điểm hoạt động; không chồng nhau ngoài thiết kế |
| F-P1 | Test trên điện thoại | APK thử trên Xiaomi 13T Pro | chạy ổn định ≥ 10 phút |
| F-P2 | Hiệu năng 15 quái | đo FPS, frame time, bộ nhớ, thời gian dựng/ cập nhật cây khi 15 quái + nhân vật di chuyển | **ngưỡng cần chốt (G)**; số liệu đo ghi vào báo cáo |

Ghi chú: kiểm F-P1/P2 cần build APK – chỉ sau khi được duyệt giai đoạn triển khai.

## G. Vấn đề còn cần quyết định trước khi triển khai
1. **Nguồn đối chiếu hình ảnh**: ai chụp ảnh client gốc (điện thoại) cho F-B1/F-C0/F-C1, hay chỉ dùng cảnh tổng hợp?
2. **Map thử**: chốt map 45 chính thức sau khi kiểm đủ `Region_C.dat` và có cây (kiểm chỉ-đọc trước), hay map khác?
3. **15 điểm spawn**: dữ liệu không có trong client – tự đặt (cách đặt: lưới/vòng tròn quanh điểm vào?) và bán kính chồng.
4. **Skill 375**: tick 500 ms áp lên đâu (missile 193 vùng / quanh nhân vật / mục tiêu chọn)? tick tại 0.5 & 1.0 hay 0, 0.5? Bố cục 4 missile 181.
5. **Cooldown 1 s** tính từ đầu cast hay cuối cast; có chặn đánh thường trong lúc cast không.
6. **Nhân vật**: bộ trang bị cố định (head/hair/body/weapon…) dùng ID nào; có ngựa/áo choàng không (slot 12–16).
7. **Chiến đấu cơ bản**: tầm tìm, tầm đánh, sát thương đánh thường của nhân vật, sát thương quái, chu kỳ tấn công quái, `hitFrame`, `aggroRadius`.
8. **Chết của nhân vật** (HP 500 về 0): hồi sinh ngay/hồi sinh chỗ cũ/ kết thúc thử.
9. **Nhịp animation**: chấp nhận giả thuyết "interval = ms" tạm thời để làm prototype, hay xác minh trước bằng đọc loader `engine/` (khuyến nghị xác minh trước, ít tốn công)?
10. **Giai đoạn đọc code bổ sung (chỉ đọc)** trước khi viết code: loader SPR (RLE/palette), `SM_*` hình học, `KIpotLeaf::PaintABuildinObject`/`Clone`, ánh xạ hướng→Dir1..16, `KMissle`/`MisslesForm=6`. Có cho phép làm thành G1 không?
11. **Ngưỡng hiệu năng** cho F-P2 (FPS tối thiểu, bộ nhớ tối đa) và thiết bị mục tiêu duy nhất hay thêm máy thấp.
12. **Quản lý asset đã trích**: thư mục lưu ngoài repo (đề xuất `D:\JX1_U003_assets`), chính sách không đưa vào git; đồng ý?
13. **Bản package.ini**: giữ bản A, thêm bước kiểm file trên điện thoại (cần chủ máy lấy file hoặc băm md5 qua adb) – có thực hiện trước triển khai không?
14. Cho phép đọc thêm `Missles`/`Skills` chi tiết hay chỉ dùng chuỗi đã xác minh ở mục D6?

## H. Điểm chưa xác minh (tổng hợp)
- Mọi mục F: chưa chạy (TESTED = không có).
- Định dạng khung SPR; thứ tự khung trong file; đơn vị `interval`.
- Ánh xạ hướng → Dir1..16/DirNum=18; tên hành động ↔ section bảng.
- `x,y` truyền vào `MoveObject` ở mọi nơi gọi có phải MPS hay không (suy luận); toạ độ buildin tuyệt đối hay cục bộ vùng.
- Hành vi nhánh giao nhau phức tạp; chi tiết `Clone`.
- Hz logic của client; `m_nCellWidth/Height` thực tế.
- File `package.ini` trên điện thoại.
