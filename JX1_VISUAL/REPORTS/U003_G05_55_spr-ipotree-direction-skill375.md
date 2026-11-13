# 55 – U003 G0.5: xác minh SPR, KIpoTree, ánh xạ hướng, luồng thời gian skill 375

Phạm vi: CHỈ ĐỌC. Không tạo Unity project/APK, không cài package/model, không sửa PAK/source/server/DB/VM/cấu hình/EXE, không đụng Goddess, U001/U002, không push. Không chạy lại inventory G0.
Việc đã chạy (đều đọc-ghi trong `D:\JX1_U003_work`, không ghi vào PAK/repo): giải mã SPR bằng script Python mới (`tools/spr_probe.py`, `spr_probe2.py`, `spr_scan.py`, `dir_map.py`, `dir_sheet.py`) và ảnh kiểm tra trong `g05_out/` (không đưa vào git).
Nhãn: **CONFIRMED** (đọc code, có file:dòng) · **TESTED** (đã chạy/đo/xem ảnh) · **HYPOTHESIS** · **UNKNOWN**. Đường dẫn code tính từ `Client2912/Client/Classes/`.

## TÓM TẮT 5 DÒNG
1. SPR giải mã được trọn vẹn: header 32 byte + bảng màu 24-bit + bảng offset + RLE (đếm, alpha) – TESTED 257/257 entry `skills.pak` và 6 sprite ani001; có THÊM chế độ lưu "TYPE_FRAME" (từng khung nén riêng) mà `pak_extract.py` hiện chưa xử lý (66 entry trong spr+skills) – đã tự cài và kiểm chứng.
2. `interval` KHÔNG thống nhất một đơn vị: vật thể cảnh dùng mili-giây thật (`IR_NextFrame`), quái/người KHÔNG dùng interval mà kéo giãn khung theo số khung logic của hành động; đạn dùng cột `nInterval` của Missles.txt theo khung game.
3. KIpoTree đọc xong các hàm `SM_*` và `Clone`: quy tắc cắt, vẽ, chèn lại khi di chuyển đã rõ; có các giới hạn/ngoại lệ cần giữ khi port (mục B7).
4. Hướng: 64-hướng → hướng sprite bằng `(d + 32/N) / (64/N)`; bảng sắp xếp bộ phận tra bằng CHỈ SỐ HƯỚNG SPRITE (0-based) = `DirN`−1, và `LineN` khớp SỐ KHUNG TUYỆT ĐỐI (đã cộng offset hướng).
5. SỬA SAI báo cáo 52–54: skill 375 sinh 4×4 = 16 đạn 181 (không phải 4), rải lệch thời gian ngẫu nhiên; tâm nổ 193 = vị trí đạn 181 vừa chạm.

Cần tôi quyết định: có (xem mục 3 và 4 cuối báo cáo).

---
## A. SPR loader

### A1. Luồng từ PAK đến khung hình [CONFIRMED + TESTED]
1. Tên file → id băm → `g_pPakList->pGetFilePath` (`engine/KPakFile.cpp:54`, `KPakList.cpp:66-77`).
2. `SprGetHeader` → `XPackFile::GetSprHeader` (`engine/XPackFile.cpp:597-668`). Hai chế độ theo cờ `lCompressSizeFlag & TYPE_FRAME(0x10000000)`:
   - **Không cờ** (đa số, byte cao của cờ `0x01`): đọc cả file đã giải nén (`ReadElemFile`), `pOffsetTable = pSpr + 32 + Colors*3` (`:617-624`).
   - **Có cờ** (byte cao `0x11`): header + bảng màu + `Frames × XPackSprFrameInfo{lCompressSize, lSize}` đọc thẳng ở `uOffset` (`:629-642`); mỗi khung nén riêng: `lSize<0` = lưu thô `|lSize|` byte, ngược lại giải nén UCL (`GetSprFrame`, `:670-741`, `lCompressType &= TYPE_METHOD_FILTER_OLD`).
3. `KImageStore2::LoadImage` (`ImageStore/KImageStore2.cpp:655-724`): khung `n` nằm ở `pOffsTable + sizeof(SPROFFS)*Frames + pOffsTable[n].Offset`, độ dài `pOffsTable[n].Length` (`:683-684`).
4. Giải RLE → RGBA tại `engine/Kgetinidata.cpp:240-371` (`findinidata_one`), tạo texture từ buffer `W*H*4` (`:375`).

### A2. Cấu trúc [CONFIRMED, khớp đọc thực tế TESTED]
- Header `SPRHEAD` 32 byte (`engine/KbugInfo.h:238-250`): `'SPR\0'`, Width, Height, CenterX, CenterY, Frames, Colors, Directions, nInterval, Reserved[6]. Lưu ý chú thích mã nói "interval theo khung game" nhưng xem A5.
- Bảng màu: `Colors` × 3 byte **R,G,B** (`KPAL24`, `Kgetinidata.cpp:173,181`), ngay sau header (offset 32).
- Bảng offset: `Frames × {uint32 Offset, uint32 Length}` (`SPROFFS`, `KbugInfo.h:255-259`), `Offset` tính từ đầu vùng dữ liệu khung (sau bảng offset).
- Khung `SPRFRAME` (`KbugInfo.h:262-269`): `Width, Height, OffsetX, OffsetY` (4×uint16, 8 byte), rồi dữ liệu RLE; `Length` bao gồm 8 byte này (`nFrameLen = datalength-8`, `Kgetinidata.cpp:234`).
- RLE (`Kgetinidata.cpp:240-371`): lặp cặp `(count, alpha)`: `alpha==0` → `count` điểm trong suốt (không có dữ liệu màu); ngược lại theo sau `count` byte chỉ số bảng màu, mỗi điểm có cùng `alpha` (1..255). Điểm ảnh chạy liên tục theo hàng (không có mã xuống dòng), dừng khi số byte đã dùng ≥ `Length-8`. Kết quả RGBA không nhân alpha: `(R,G,B,alpha)`.
- Vị trí khung trong canvas `Width×Height` của header: góc trái-trên tại `(OffsetX, OffsetY)` của khung.

### A3. Kết quả kiểm chứng giải mã [TESTED]
- Script `spr_probe.py`: ani001 (6 sprite st/pst/wlk/bat/die/at, spr.pak) – mọi khung giải được, tổng điểm = `W*H` mỗi khung, chỉ số màu tối đa 251–254 (< 256), 0 lỗi. Missile 181, cast `kl_16`, nổ `Bz_dian3`, missile 193, icon 375: 0 lỗi. Ảnh dựng lại xem bằng mắt đúng (hổ ani001 hướng 0 quay mặt vào camera; hiệu ứng vàng đúng hình).
- `spr_scan.py skills`: **257/257 entry giải được** (234 nguyên file + 23 chế độ khung), 0 lỗi, `Reserved[1]=0` ở cả 257. 
- Entry `kl_02_疾电法b.spr` (id lỗi "lookbehind overrun" ở các báo cáo trước): thực ra là chế độ TYPE_FRAME (cờ `0x11093766`); giải đúng bằng đường khung: 160 khung, 16 hướng, 0 lỗi, vị trí cuối khớp `off + csize`.
- spr.pak: LẤY MẪU 2500 entry đầu (không phải toàn bộ 14616): 2495 nguyên file + 5 chế độ khung giải đúng, 0 lỗi RLE/kích thước; 6 entry không phải SPR (bỏ qua); `Reserved[1]=0` ở cả 2500. 12116 entry còn lại CHƯA kiểm. Cột `interval` phổ biến: 1 (2048), 100, 80, 120.

### A4. Palette / alpha / định dạng đặc biệt
- Palette 24-bit, không có điểm "màu khóa" – trong suốt hoàn toàn do `alpha==0` [CONFIRMED]. Alpha trung gian có thật (hàng chục nghìn điểm/ khung lớn), nên Unity phải dùng alpha thẳng (straight alpha) hoặc nhân sẵn khi blend [TESTED qua thống kê alpha].
- Cờ đặc biệt: `Reserved[1]==1 || 2` và đường dẫn không chứa "游戏资源" ⇒ client chuyển sang chế độ "xóa viền": alpha = `min(alpha, max(R,G,B))` và nhân sẵn RGB theo alpha (`Kgetinidata.cpp:130-139,265-300`) [CONFIRMED trong code]. Trong tất cả sprite U003 đã kiểm, `Reserved[1]=0` ⇒ chế độ này **không áp dụng** [TESTED cho 257 entry skills + 13 sprite U003]. Với tài nguyên khác chưa kiểm hết (xem A3 spr.pak).
- `Reserved[0]` và `Reserved[2..3]` bị client ghi đè lúc nạp (chỉ số pak, chỉ số node; `KPakFile.cpp:58`, `XPackFile.cpp:652`) – không có ý nghĩa trong file gốc.
- Kiểu trộn (blend) khi vẽ (`IMAGE_RENDER_STYLE_3LEVEL/ALPHA/BORDER`, `KIpotLeaf.cpp:136-147`; `GL::blendFunc` ở `KgameWorld.cpp:14860`): **UNKNOWN** cách `3LEVEL`/hiệu ứng skill được pha (cộng hay alpha thường). Cần đối chiếu ảnh thật trước khi chọn shader hiệu ứng.

### A5. Số khung, thời lượng, đơn vị `interval`
- Số khung/hướng = `Frames / Directions` (`KSprControl::GetOneDirFrames`, `KSprControl.cpp:192`); khung thuộc hướng `d` bắt đầu ở `d * (Frames/Directions)` (`KSprControl.cpp:114-122,154`) [CONFIRMED]. TESTED: ani001_st 96 khung/8 hướng = 12/hướng.
- **Vật thể cảnh (cây/nhà có hoạt ảnh)** [CONFIRMED]: `BuildinObjNextFrame` (`KIpotLeaf.cpp:304-337`) lấy `nAniSpeed = header.nInterval` (tối thiểu 20), `IR_NextFrame` đếm bằng `l_Time` = **mili-giây thật** (`gamecore/ImgRef.cpp:17-22,44-59`). ⇒ ở đây `interval` = ms. (Chú thích "khung game" trong `KbugInfo.h:248` không đúng cho nhánh này.)
- **Quái/NPC/nhân vật** [CONFIRMED]: `KNpcRes::Draw` (`KNpcRes.cpp:255-287`): `frame = dir*(Frames/Dirs) + (Frames/Dirs) * nCurFrame / nAllFrame` với `nCurFrame/nAllFrame` là khung logic của hành động (`m_Frames`). `nInterval` KHÔNG được dùng cho NPC. Tức hoạt ảnh được kéo giãn/ép vào số khung logic của hành động; tốc độ phụ thuộc `AttackFrame/CastFrame/WalkFrame…` (khung logic), xem KNpc.cpp:2381,2399.
- **Đạn/hiệu ứng skill** [CONFIRMED]: `KMissleRes::Draw` (`gamecore/KMissleRes.cpp:141-215`): lặp `nFrame = (nCurLifeFrame / nInterval) % nTotalFrame` với `nInterval` lấy từ cột `AnimFileInfoN` của Missles.txt (`KMissle.cpp:274,302`); nếu `LoopPlay=0` thì `nFrame = nTotalFrame * nCurLifeFrame / nAllFrame` (kéo giãn suốt đời đạn, `:197`). `nCurLifeFrame` tăng 1 mỗi nhịp logic (`KMissle.cpp:526`).
- Hướng đạn: `nImageDir = nDir / (64/nSprDir)` làm tròn lên khi phần dư ≥ `32/nSprDir`, quay vòng (`KMissleRes.cpp:160-165`); đạn 181/193 chỉ 1 hướng.
- Bảng tổng hợp (đơn vị thời gian của từng nhóm): vật thể cảnh = ms thật; quái/người = khung logic hành động (≈ 1/18 s nếu logic 18 Hz — số 18 Hz lấy từ báo cáo 30/41, **HYPOTHESIS cho client**, chưa đo lại ở đây); đạn = khung logic.
- Ánh xạ cho Unity: animation quái/người/đạn phải chạy theo "đồng hồ logic" (số nhịp), không theo `interval` của header. Số liệu `interval` đã ghi ở báo cáo 52/54 (ani001 st116…) **không dùng** cho quái.

### A6. Neo (anchor) và độ lệch [CONFIRMED trong 1 hàm, áp dụng cho NPC = HYPOTHESIS]
`KgameWorld::ccgetTxtData` (`gamescene/KgameWorld.cpp:8029-8057`): vị trí màn hình = `GetLocalPositionByMps(mpsX, mpsY, z)`; nếu cờ `RUIMAGE_RENDER_FLAG_REF_SPOT`: trừ `(CenterX, CenterY)` của header; nếu cả hai bằng 0 và `Width > 160` thì trừ mặc định `(160, 192)` (`#define CENTERX 160, CENTERY 192`); nếu không có cờ `FRAME_DRAW`: cộng `(OffsetX, OffsetY)` của khung. Phiên bản `_p` (`:8089-8105`) bỏ nhánh mặc định (160,192). ani001 có `Center=(0,0)`, `Width=320` ⇒ neo mặc định (160,192) (khớp tâm các sprite hiệu ứng 160/192). Chưa xác định NPC dùng biến thể nào và cờ nào ⇒ phải kiểm bằng ảnh đối chiếu (F-A6).

### A7. Khung lỗi / thiếu dữ liệu [CONFIRMED]
- Thiếu header/khung → `findinidata_one` trả `NULL` (`Kgetinidata.cpp:120-124,187-197`) ⇒ khung không vẽ, không báo lỗi; `GetSprFrame` gặp lỗi giải nén thì hiện hộp thoại "GetSprFrame--filed" (`XPackFile.cpp:720-738`).
- Vòng RLE gốc KHÔNG kiểm biên (đọc quá buffer nếu dữ liệu hỏng); ở bản port phải kiểm biên (quy tắc DESIGN).

### A8. Có tái tạo chính xác hình ảnh gốc trong Unity được không?
- **Điểm ảnh/alpha/vị trí khung: CÓ** (TESTED trên 257 entry + tài nguyên U003; công thức đầy đủ ở A2).
- **Chưa đủ**: kiểu pha trộn khi vẽ (A4), biến thể neo cho NPC (A6), và phần spr.pak ngoài mẫu đã quét (A3).
- Công cụ trích hiện có (`pak_extract.py`) phải thêm đường TYPE_FRAME trước khi dùng cho pipeline (66 entry bị ảnh hưởng ở spr+skills; entry cần cho U003 ngoài `kl_02` thì không).

---
## B. KIpoTree – hình học và Clone

### B1. Hàm hình học (`gamescene/SceneMath.cpp`, `SceneMath.h`) [CONFIRMED]
- Enum `RELATION_UP=0, ON=1, DOWN=2, CROSS=3` (`SceneMath.h:15-21`). Trục y hướng xuống (toạ độ MPS).
- `SM_Relation_PointLine(P, A, B)` (`:342-381`): đặt `p1=A-P`, `p2=B-P`; nếu `|p1|²≤10` hoặc `|p2|²≤10` (cả hai thành phần `x²≤10` và `y²≤10`, **kiểm riêng từng thành phần**: `p.x*p.x<=10 && p.y*p.y<=10`) ⇒ ON; đổi chỗ để `p1.x ≤ p2.x`; `f = p1.x*p2.y − p2.x*p1.y` (tích có hướng, KHÔNG chia độ dài); `|f|≤10` ⇒ ON; `f<0` ⇒ UP, ngược lại DOWN. UP = điểm nằm phía trên đường (y nhỏ hơn) với đường không thẳng đứng. Hệ quả: ngưỡng ON tính theo "tích" nên càng dài đường càng hẹp (≈ 10/độ dài px).
- `SM_Distance_PointLine` (`:324-339`): `|x1*y2 − x2*y1| / qsqrt((x2-x1)²+(y2-y1)²)`, số nguyên cắt cụt (`qsqrt` là hàm căn nhanh của dự án, định nghĩa chưa đọc ⇒ sai số nhỏ UNKNOWN).
- `SM_Relation_PointLine_New` (`:384-424`) giống nhưng ngưỡng điểm trùng 3 px; **không được dùng** (`KIpotBranch.cpp:411-412` dòng gọi bị chú thích). Chỉ bản không-`_New` hoạt động.
- `SM_IsLineLinkable(s1,n1,s2,n2)` (`SceneMath.h:34-36`): `|s1−s2|<0.01 && |n1−n2|<16.0` (`LINE_LINKABLE_SLOPE_RANGE 0.01`, `LINE_LINKABLE_NODICALY_RANGE 16.0`). `fAngleXY` (độ dốc) và `fNodicalY` (giao điểm y) là **dữ liệu có sẵn trong file** (`KBuildinObj`, `SceneDataDef.h:176-177`), không tính lại ở client; công thức của công cụ dựng map: UNKNOWN.
- `SM_Relation_LineLine_CheckCut(L1a,L1b,L2a,L2b,POI)` (`:470-541`): `r1 = Rel(L1a, L2)`, `r2 = Rel(L1b, L2)`; `r1==r2` ⇒ trả `r1`; một trong hai ON ⇒ trả cái còn lại; ngược chiều ⇒ **CROSS** và tính giao điểm `POI` bằng số nguyên với các nhánh riêng cho đường thẳng đứng/nằm ngang (`:500-534`), chia số nguyên cắt cụt, cộng lại offset = `L1a`.

### B2. Tree / Line / Point [CONFIRMED]
- Dựng: `KScenePlaceC.cpp:1905-2063`. **Tree**: gom theo `SM_IsLineLinkable` thành "tập tuyến" (nhánh dài nhất lên trước, `:1980-1991`), trong tập sắp theo x (`:1943-1961`); từng vật thể `m_ObjectsTree.AddBranch` (`:1994-2004`). **Line**: sắp độ dài² giảm dần (`:2007-2047`), `AddLeafLine`. **Point**: `AddLeafPoint` (`:2056-2063`).
- `KIpotBranch::AddBranch` (`KIpotBranch.cpp:235-292`): cùng `fAngleXY` và `fNodicalY` (so `==` chính xác) ⇒ ON (cùng nhánh, `AddAObject :198-232`, mở rộng `m_oHeadPoint/m_oEndPoint` theo x); khác ⇒ `SM_Relation_LineLine_CheckCut(vật thể, đường nhánh)`: UP→con 0, DOWN→con 1, ON→cùng nhánh, CROSS→cắt (B3).
- `AddLeafLine` (`:381-402`): quan hệ lấy theo đầu mút **xa đường hơn** (so `SM_Distance_PointLine` hai đầu), ON/DOWN→phía 1, UP→phía 0 ⇒ Line KHÔNG bị cắt dù vắt ngang nhánh (xếp trọn vào một phía).
- `AddLeafPoint` (`:405-420`): `SM_Relation_PointLine(P, đường nhánh)`; chỉ UP→phía 0, còn lại (kể cả ON)→phía 1.
- Trong danh sách lá của một phía: `AddPointLeafToList` (`:422-549`) – trước hết tìm Line trong danh sách mà điểm nằm trong hộp (±13 ngang; trên −3, dưới +128 khi điểm không ở phía UP): nếu có ⇒ lồng vào con của Line đó (DOWN→`pRChild`, UP/ON→`pLChild`); nếu không ⇒ chèn vào danh sách theo `y` tăng dần (`:516-530`). `AddLineLeafToList` (`:551-645`): tương tự cho Line trong hộp ±7; không thì chèn theo `min(y)`.
- Vẽ lớp OBJECT: nhánh = phía 0 → các vật thể nằm trên đường nhánh → phía 1 (`PaintObjectLayer :67-88`); trong danh sách lá: `pLChild` → lá → `pRChild` → anh em kế (`KIpotLeaf_PaintObjectLayer`, `KIpotLeaf.cpp:68-98`). Đối tượng động vẽ qua `CoreDrawGameObj` nếu nằm trong vùng hiển thị (`:79-86`).

### B3. Clone khi cắt [CONFIRMED]
`KIpotBuildinObj::Clone(POI)` (`KIpotLeaf.cpp:277-302`): nếu `POI.x == oEndPos.x` ⇒ không tạo; ngược lại sao chép (cùng `pBio`, ảnh, `fAngleXY/fNodicalY`), clone = đoạn `POI → oEndPos`, bản gốc bị **sửa tại chỗ** thành `oPosition → POI`; cả hai `bImgPart = true`, clone `bClone = true`. `AddBranch` (`KIpotBranch.cpp:267-291`): quan hệ của đầu `p1` (điểm đầu gốc) với đường nhánh: DOWN ⇒ gốc→phía 1, clone→phía 0; ngược lại gốc→phía 0, clone→phía 1. Nếu gốc có `oPosition.x == oEndPos.x` thì gốc bị bỏ (và chỉ `free` nếu là clone) – xem B7.
Vẽ mảnh cắt: `PaintABranchObject` (`KIpotBranch.cpp:112-168`) nội suy 4 điểm `ImgPos` theo tỷ lệ `(nStartPart..nEndPart)/(oPos2.x − oPos1.x)` và cắt ảnh theo cột (`oImgLTPos/oImgRBPos`), chia số nguyên cắt cụt. Với đối tượng không cắt: vẽ 4 điểm nguyên vẹn (`:114-132`).

### B4. Thứ tự vẽ khi hai nhánh cắt nhau [CONFIRMED mô tả; kết quả hình ảnh chưa TESTED]
Nhánh cắt nhau được tách bằng Clone tại giao điểm: phần nằm phía UP của đường nhánh gốc đi vào cây con 0 (vẽ trước), phần DOWN vào cây con 1 (vẽ sau). Như vậy thứ tự giữa hai mảnh của đối tượng bị cắt là nhất quán với nhánh đã cắt. Thứ tự giữa mảnh và nhân vật do vị trí chân nhân vật so với đường nhánh (B5).

### B5. Cập nhật khi đối tượng động di chuyển; nhiều đối tượng cùng điểm chân [CONFIRMED]
- `MoveObject` (`KScenePlaceC.cpp:1444-1516`): gỡ (`PluckRto` → `KIpotRuntimeObj::Pluck :19-51` cập nhật `pAheadBrother/pParentBranch/pParentLeaf`), ghi `oPosition=(x, y+6)`, `AddLeafPoint` lại từ nút gốc (`:1476-1482`). Không đổi toạ độ ⇒ bỏ qua.
- Nhiều đối tượng cùng `y` chân: khi chèn, vòng lặp dừng ở lá đầu tiên có `lp.y < pL.y` **nghiêm ngặt** (`KIpotBranch.cpp:516-527`), nên đối tượng chèn sau, cùng `y`, nằm SAU (vẽ sau, che lên) các đối tượng cùng `y` đã có; `x` không tham gia. ⇒ thứ tự phụ thuộc lịch sử chèn (đối tượng vừa di chuyển thì thành "mới nhất"). Cặp cùng chân không được xử lý ổn định theo id.
- `StrewRtoLeafs` dùng `||` nên gần như giữ mọi lá (`KIpoTree.cpp:443-446`).

### B6. Các điểm thuật toán không xử lý / ngoại lệ [CONFIRMED trừ ghi chú]
1. `CCAssert(p1.x != p2.x && m_oHeadPoint.x != m_oEndPoint.x)` (`KIpotBranch.cpp:243`): vật thể nhánh thẳng đứng bị cấm ở nhánh (trong build release assert có thể không chạy ⇒ UNKNOWN).
2. Ngưỡng ON theo tích có hướng không chuẩn hóa ⇒ kết quả nhạy với độ dài đường (B1).
3. Giao điểm tính bằng số nguyên cắt cụt ⇒ sai lệch ≤ 1 px; mảnh cắt có thể lệch 1 px.
4. Line và Point không bị cắt (chỉ Tree bị cắt); Line vắt ngang nhánh được xếp theo đầu mút xa.
5. Đối tượng cùng chân thứ tự theo lịch sử chèn (B5).
6. Vật thể cùng `fAngleXY`/`fNodicalY` so bằng `==` float; hai đường gần-song-song nhưng không bằng nhau chính xác đi qua đường `CheckCut` và có thể thành CROSS giả.
7. `Clone` bỏ qua khi `POI.x == oEndPos.x`: khi đó phần gốc giữ nguyên toàn bộ ⇒ không cắt (chấp nhận).
8. `AddSubBranch`/`Clone` dùng `malloc` thủ công; quản lý bộ nhớ không áp dụng cho C#.
9. Không có xử lý z (cao độ): sắp xếp chỉ theo (x,y) chân + 6; vật thể có độ cao (ảo ảnh) chỉ qua ImgPos 4 điểm.

### B7. Đề xuất port sang C# (chưa viết code)
- Giữ nguyên **đúng thứ tự phép toán và kiểu số** (int 32-bit, chia cắt cụt về 0 như C — `int` chia trong C# cũng cắt cụt) cho `SM_*`; không thay bằng `float`/`Math.Sign`.
- Cấu trúc: `IpotLeaf`, `IpotBuildinObj`, `IpotRuntimeObj`, `IpotBranch`, `IpoTree` như mô tả ở báo cáo 54 mục C3, nhưng danh sách lá dùng liên kết đơn như gốc (để giữ quy tắc chèn "sau cùng y").
- `IpotBranch.PaintObjectLayer` trả `IEnumerable<DrawItem>` theo đúng thứ tự (phía 0 → trên đường → phía 1; `LChild → lá → RChild → anh em`); Unity gán `sortingOrder` tăng dần theo thứ tự này mỗi khung đã thay đổi (chỉ tính lại khi cây đổi).
- Bộ dựng cây theo `KScenePlaceC.cpp:1905-2063` (nhóm theo `IsLineLinkable`, sắp theo nhóm dài nhất, sắp x trong nhóm) – cần làm chính xác vì cây phụ thuộc thứ tự thêm.
- Test tương đương: một trình **tham chiếu C++ chỉ-đọc** (biên dịch riêng ngoài dự án, không sửa nguồn) hoặc dump thứ tự vẽ từ client gốc trên map thử; hoặc bộ trường hợp tay (TESTED bởi người), để so khớp thứ tự lá C#. Chưa có mô hình tham chiếu ⇒ ghi nhận F-C.
- Không port: `RenderLightMap`, `FillLineObstacle`, `CanLighting` (chỉ ánh sáng).

---
## C. Ánh xạ hướng

### C1. Hướng logic 64 → hướng sprite [CONFIRMED + TESTED]
- Hướng logic = chỉ số 0..63 từ `g_GetDirIndex(x1,y1,x2,y2)` = `g_GetNewDirIndex(dx,dy)` (`gamecore/KMath.h:221-256,329-333`), bảng sin `g_nSinBuffer[64]` (`KMath.cpp:6-16`). Quy ước đã suy ra và kiểm bằng cài lại hàm: **0 = hướng xuống (y+)**, **16 = trái**, **32 = lên**, **48 = phải**; tăng dần theo chiều kim đồng hồ trên màn hình (xuống→trái→lên→phải). Điểm chuyển chẵn (dx≥0 và `nRet!=0`) lấy `64−nRet`. Không có giá trị 64 (tối đa 63); `−1` khi `dx=dy=0` (`:225-226,230`). Hàm cài lại `tools/dir_map.py` cho 3600 góc: sinh đủ 64 giá trị 0..63 [TESTED].
- Hướng sprite `N` hướng (`N = Directions` của sprite): `idx = (dir64 + 32/N) / (64/N)`, nếu `idx ≥ N` thì `idx −= N` (`KSprControl.cpp:162-179`, `KNpcRes.cpp:282-284`) [CONFIRMED].
- Bảng cụ thể (TESTED bằng `dir_map.py`):

| dir64 | 0 | 8 | 16 | 24 | 32 | 40 | 48 | 56 |
|---|---|---|---|---|---|---|---|---|
| hướng màn hình | xuống | xuống-trái | trái | lên-trái | lên | lên-phải | phải | xuống-phải |
| sprite 8 hướng | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| sprite 16 hướng | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 |

Bảng đầy đủ 64 dòng: sprite8: `0-3→0, 4-11→1, 12-19→2, 20-27→3, 28-35→4, 36-43→5, 44-51→6, 52-59→7, 60-63→0`; sprite16: `0-1→0, 2-5→1, 6-9→2, … , 58-61→15? ` (chính xác: `idx = (d+2)/4 mod 16`; xem `g05_dirmap.txt`).
- Kiểm bằng ảnh [TESTED, 1 sprite]: sheet 8 khung đầu mỗi hướng của `ani001_st`: hướng 0 hổ quay mặt vào camera, 1 chếch trái-dưới, 2 hướng trái, 3 chếch lên-trái (nhìn lưng), 4 lưng, 5 chếch lên-phải, 6 hướng phải, 7 chếch xuống-phải ⇒ đúng thứ tự bảng. (Ảnh: `g05_out/ani001_dirs_sheet.png`.)
- Điểm giữa hai hướng: số nguyên chia cắt cụt ⇒ ranh `dir64 = 4 (mod 8)` thuộc về hướng sprite **cao hơn** (làm tròn lên), ví dụ 4→1, 12→2; riêng 60..63 quay về 0 [CONFIRMED + TESTED].
- Không gian toạ độ khi tính `dx,dy` (MPS với y gấp đôi, hay màn hình): `g_GetDirIndex` được gọi với toạ độ MPS ở `KNpc.cpp:2332` (`NewMap2Mps`) ⇒ trục y bị gấp đôi trước khi lấy hướng; các điểm chéo trên màn hình 45° khi đó rơi ở dir64 ≈ 5/27/37/59 thay vì 8/24/40/56 (đã tính, `g05_dirmap.txt`). Joystick/AI nhập vector thế nào: **UNKNOWN** (chưa đọc `KHRocker`/`KNpcAI` ở bước này).

### C2. Bảng sắp xếp bộ phận (Dir/Line) [CONFIRMED]
- Chỉ dùng với nhân vật nhiều bộ phận. Với quái `NPC_RES_NORMAL` (ani001): `GetnSort` bỏ qua bảng và trả đúng một bộ phận `NORMAL_NPC_PART_NO=6` (`KNpcResNode.cpp:614-624`, `GameDataDef.h:640`) ⇒ **ani001 không cần bảng sắp xếp**.
- Nạp bảng (`CSortTable::GetkTable`, `KNpcResNode.cpp:1219-1378`): bảng gồm tối đa 16 dòng `Dir1..Dir16` mặc định của `[DEFAULT]` (`MAX_SORT_DIR=16`), rồi mỗi hành động: tùy chọn `Dir1..16` riêng (khuyết ⇒ chép từ dòng mặc định, `:1352-1355`), và các `LineN` đặc biệt. `DirNum`/`UnitNum` trong `[DEFAULT]` **không được đọc** (dòng đọc `DirNum` bị chú thích, `:1317`).
- Tra (`CSortTable::GetSort`, `:1390-1480`): chỉ số hướng = `nDir` 0-based của **sprite** (= `DirN`−1; không phải dir64); nếu hành động có `LineN` và `nFrameNo` bằng cột đầu của một dòng ⇒ dùng dòng đó, ngược lại dùng dòng hướng. Mỗi dòng: cột đầu = khóa, các cột sau = thứ tự vẽ (chỉ số slot, −1 = bỏ qua) (`KNpcRes.cpp:663-694` vẽ lần lượt theo `m_nSortTable[i]`, mỗi slot qua các lớp `emNPCRES_PART_LAYER_COUNT`).
- `nFrameNo` truyền vào là **số khung tuyệt đối của sprite** (đã cộng `dir*(Frames/Dirs)`; `KNpcRes.cpp:286-287,422`) từ **bộ phận cuối cùng tồn tại** trong vòng lặp slot×lớp (biến bị ghi đè mỗi lượt) ⇒ khóa `LineN` là số khung tuyệt đối, khác nhau theo hướng. Bằng chứng dữ liệu: hành động `RangeWWalk` có `Line` khóa 30, 31, 44 (`json/sort_table_MainMan.json`, mục 2) — phù hợp khung tuyệt đối (30 = 2×15 + 0 nếu 15 khung/hướng) [HYPOTHESIS cho số khung/hướng của ngựa-đi bộ, vì chưa tra sprite].
- `LineN` thay đổi theo khung: **có** (chỉ các khung có khóa khớp mới dùng dòng riêng; khung khác dùng dòng hướng) [CONFIRMED].
- Đổi hướng giữa animation [CONFIRMED]: nhánh `nAllFrame>0` (hành động có khung xác định) tính lại `dirNo` từ `dir64` mỗi lần vẽ; `frame = dirNo*per + per*nCurFrame/nAllFrame` ⇒ đổi hướng giữa chừng giữ nguyên tiến trình hành động (không về khung 0). Nhánh `nAllFrame==0`: `SetCurDir64` (`KSprControl.cpp:162-179`) khi đổi hướng đặt lại khung về đầu hướng mới và `GetNextFrame` tăng 1 khung mỗi nhịp logic (`:342-374`) ⇒ khởi động lại. Hành động nào dùng nhánh nào: chưa tra đầy đủ **UNKNOWN**.
- Ánh xạ tên hành động ↔ section: `CActionName` (`GetActionName`) — danh sách tên chưa lập ⇒ UNKNOWN (chặn nhân vật nhiều bộ phận, không chặn ani001).

---
## D. Skill 375 – luồng thời gian (đơn vị: khung logic của game; quy ra giây phụ thuộc Hz, HYPOTHESIS 18 Hz theo báo cáo 30/41)

### D1. Dữ liệu gốc [CONFIRMED, đọc lại bảng thật]
- Skill 375: `MisslesForm=6` (AtTarget), `BaseSkill=1`, `ChildSkillId=181`, **`ChildSkillNum=4`**, `MslsGenerate=3` (= `SKILL_MGS_RANDONORDER`, `SkillDef.h:151-156`), `MslsGenerateData=5`, `WaitTime=2`, `CollideEvent=1`, `CollidSkillId=387`, `TimePerCast=0`, `CharAnimId=11`, `PreCastSpr=kl_16_魔法施放.spr`.
- Skill 387: `MisslesForm=6`, `ChildSkillId=193`, `ChildSkillNum=1`, `MslsGenerate=0`, `WaitTime=5`, `CollideEvent=0`.
- Missles 181: `MoveKind=0` (Stand = đứng yên, `SkillDef.h:18`), `CollidRange=2`, `IsRangeDmg=0`, `DmgRange=2`, `LifeTime=12`, `ColVanish=1`, `AutoExplode=0`, bay `AnimFile2` (6 khung, `6,1,2`), nổ `AnimFile4` (8 khung).
- Missles 193: `MoveKind=0`, `CollidRange=2`, `IsRangeDmg=1`, `DmgRange=2`, `DmgInterval=4`, `LifeTime=12`, `ColVanish=1`, `AnimFile2` = `雷击术` (27 khung), nổ `Bz_dian3`.

### D2. Chuỗi sự kiện [CONFIRMED trong code; thời gian thực chưa TESTED]
1. **Bắt đầu cast**: `KNpc::DoSkill` kiểm tra hết hồi chiêu (`NextCastTime`) và tiêu hao (`KNpc.cpp:2195-2243`); đặt `NextCastTime = now + GetDelayPerCast()` (=0 với 375) và gọi UI `setSkillNextUseTime` (`:2259-2264`); `DoOrdinSkill` đặt sprite cast sẵn `kl_16` (`:2334-2335`) và tổng khung `nTotalFrame = m_CastFrame * naAttackSpeed / (m_CurrentCastSpeed + nbAttackSpeed)` (skill nội công, `:2394-2402`); mặc định `m_CastFrame=20` (`:449`), `naAttackSpeed/nbAttackSpeed` lấy từ `_gameGlobalSet.NpcInfo` (giá trị: UNKNOWN; khởi tạo cục bộ 100/100, `:2357-2361`). Nhân vật phát động tác cast `CharAnimId=11`.
2. **Phóng skill**: `KNpc::OnSkill` gọi `pSkill->Cast` khi đạt 60% thời gian động tác (`IsReachFrame(ATTACKACTION_EFFECT_PERCENT=60)`, `KNpc.cpp:58,2576,2598`) ⇒ cast hoàn tất ≈ khung 12 trên 20; động tác kết thúc ở khung 20 (`WaitForFrame`, `:2571`).
3. **Tạo đạn**: `CastMissles` (`KSkills.cpp:1620-1677`) → `AtTarget` → `__CastFixed` (`:1433-1528`) → tọa độ đích = vị trí mục tiêu/điểm (`Param2PCoordinate`) → `CastZone` (`:1695-1837`): vì `ChildSkillNum=4`, hai vòng lặp `i,j` đều chạy 0..3 ⇒ **16 đạn 181** đặt trên lưới 4×4 ô (mỗi ô `m_nCellWidth × m_nCellHeight`, nguyên mẫu 32×32 MPS), căn quanh điểm đích: `begin = ref − N*cell/2`, đạn `(i,j)` tại `begin + (j*cellW, i*cellH)` (`:1744-1766`) (`Param1=0` ⇒ hình chữ nhật, không cắt góc tròn, `:1758-1760`).
   - **Không cùng lúc**: `m_nStartLifeTime = nWaitTime(tham số truyền) + GetMissleGenerateTime(i*N + j)` (`:1793`); với RANDONORDER: `m_nWaitTime(2) + k*5 ± ngẫu nhiên` – nửa lần `+rand(5)`, nửa lần `−rand(2)` (`:3103-3109`), `k=0..15` ⇒ độ trễ vào khoảng `2+5k−1 … 2+5k+4` khung, từ ~1–6 (k=0) đến ~76–81 (k=15). Tham số `nWaitTime` ban đầu của lần cast người chơi: mặc định chưa tra (khả năng 0, UNKNOWN). Ở 18 Hz: từ ~0,1 s đến ~4,4 s sau thời điểm phóng.
   - `m_nLifeTime += m_nStartLifeTime` (`:1794`): đạn sống đủ `LifeTime=12` khung sau lúc bắt đầu bay.
4. **Vòng đời đạn** (`KMissle::Activate`, `KMissle.cpp:405-526`): `m_nCurrentLife` tăng 1 mỗi nhịp (`:526`); khi `== m_nStartLifeTime` → `PrePareFly`+`DoFly` (`:441-455`) (đạn bắt đầu bay/xuất hiện); trong trạng thái bay mỗi nhịp `OnFly` (`:657-`) kiểm vật cản, rồi `FsCheckCollision` (`:554-650`).
5. **Va chạm đạn 181**: `CollidRange=2 ≠ 1` ⇒ "tấn công nhóm": duyệt 5×5 ô quanh đạn (`-2..2`), `FindNpc(..., m_eRelation)` tìm NPC quan hệ kẻ thù; nếu thấy: `ProcessCollision()` (hiệu ứng) rồi `DoCollision()` (`KMissle.cpp:626-648`, `1560-1600`). `DoCollision` gọi `pOrdinSkill->Collidsion(this)` (kích hoạt `CollideEvent` → skill 387) rồi, vì `ColVanish=1`, `DoVanish` (hiệu ứng nổ `Bz_dian3`). Hết đời mà chưa chạm: `AutoExplode=0` ⇒ biến mất không kích hoạt 387 (`:419-438`). Mỗi đạn 181 kích hoạt tối đa một lần.
6. **Kích hoạt 193**: `Collidsion` → cast skill 387 với bên phóng là **đạn 181** (`SKILL_SLT_Missle`) ⇒ `__CastFixed` nhánh `SKILL_SLT_Missle` (`KSkills.cpp:1511-1523`): tâm = `NewMap2Mps(vị trí hiện tại của đạn 181)` ⇒ `CastZone` với `ChildSkillNum=1` ⇒ một đạn 193 đúng tại vị trí đạn 181 (không phải vị trí con quái); trễ `WaitTime=5` khung (`:1793` + `GetMissleGenerateTime`, kiểu NULL ⇒ `m_nWaitTime=5`). Như vậy tối đa 16 đạn 193 mỗi lần cast (một cho mỗi 181 chạm kẻ thù).
7. **Đạn 193**: bắt đầu bay sau 5 khung, sống 12 khung, `IsRangeDmg=1`, vùng sát thương `DmgRange=2` ⇒ `nRangeX = DmgRange/2 = 1` ⇒ hình vuông 3×3 ô quanh đạn (`ProcessCollision`, `KMissle.cpp:1675-1760`, bo tròn bị chú thích `:1724-1726`) ≈ 96×96 MPS px (96×48 màn hình) với ô 32×32; quan hệ kẻ thù `m_eRelation`. `DmgInterval=4` (khung): nơi dùng nằm ở phía server (`#ifdef _SERVER` đã chú thích trong client, `:707-718`) — **UNKNOWN** (chưa đọc server). Ảnh 193 (27 khung, `LoopPlay=0`) được kéo giãn ra suốt đời đạn (`KMissleRes.cpp:197`).
8. **Sát thương thực**: dữ liệu `lightingdamage_v` 80/260/470 (cấp 1/15/20) ở `kunlun.lua:199-239` (báo cáo 52); client chỉ hiển thị hiệu ứng, số thực do server tính [UNKNOWN chi tiết ở đây].

### D3. Khác biệt giữa gốc và luật U003 (không sửa luật U003)
| Mục | Gốc (CONFIRMED) | U003 đã chốt |
|---|---|---|
| Số đạn 181 | 16 (4×4), trễ ngẫu nhiên ~1–81 khung | (báo cáo trước ghi 4) — cần quyết định mục 4.2 |
| Thời điểm sinh đạn | 60% động tác cast (~khung 12/20) rồi cộng trễ từng đạn | sau cast 1 s |
| Tâm AOE | vị trí đạn 181 vừa chạm kẻ thù (ô quanh mục tiêu) | tâm tại vị trí kích hoạt missile 193 — **tương thích** (193 sinh tại vị trí 181) |
| Hình AOE | vuông 3×3 ô | tự chọn khi thiết kế |
| Tick sát thương | `DmgInterval=4` khung (server, chưa đọc) | 500 ms/1000 ms sau kích hoạt, 20/tick |
| Cooldown | `TimePerCast=0` (không có) | 1 s từ lúc bắt đầu cast |
| Thời lượng cast | `m_CastFrame=20` khung (~1,1 s @18 Hz) | 1 s |

---
## 1. Đánh giá các blocker
| Blocker (báo cáo 54) | Trạng thái |
|---|---|
| Giải mã khung SPR | **ĐÃ GIẢI QUYẾT** về dữ liệu điểm ảnh (A2–A3, TESTED); còn mở: blend, neo NPC (A4, A6) |
| Thứ tự khung trong file/đơn vị `interval` | **ĐÃ GIẢI QUYẾT**: khung theo hướng liên tiếp; đơn vị từng nhóm ở A5 |
| `SM_*`/Clone | **ĐÃ GIẢI QUYẾT** (đủ để port; cần dựng test tham chiếu) |
| Ánh xạ hướng → Dir | **ĐÃ GIẢI QUYẾT cho 8/16 hướng sprite** (C1); tên hành động ↔ section còn mở (chặn nhân vật nhiều bộ phận, không chặn ani001) |
| Skill 375 – luồng thời gian | **ĐÃ GIẢI QUYẾT phần client**; tick sát thương phía server chưa đọc, nhưng U003 dùng luật riêng nên không chặn |
| Vị trí 15 spawn | **CHƯA** (dữ liệu không có trong client) |
| `package.ini` trên điện thoại | **CHƯA** |
| Toạ độ buildin tuyệt đối/cục bộ vùng | **CHƯA** |

## 2. Danh sách vấn đề còn thiếu
1. Kiểu blend khi vẽ đối tượng thường/hiệu ứng (A4).
2. Biến thể neo cho NPC/đạn và cờ `REF_SPOT` (A6).
3. Quét hết spr.pak (A3) và các pak `updata*`, `ui*` cho `Reserved[1]` khác 0.
4. Tần số logic của client (18 Hz?) – cần đo/đọc `KgameWorld` update.
5. Nhân vật nhiều bộ phận: danh sách tên hành động, hành động nào dùng nhánh `nAllFrame>0`, đối chiếu khóa `LineN` với sprite thật.
6. Cách joystick/AI tạo vector hướng (không gian MPS hay màn hình).
7. Tick sát thương/`DmgInterval` phía server; `nWaitTime` ban đầu của lần cast.
8. `_gameGlobalSet.NpcInfo.naAttackSpeed/nbAttackSpeed` (ảnh hưởng thời lượng cast).
9. Tọa độ buildin (tuyệt đối hay cục bộ vùng), map 45 có đủ Region_C.dat/cây.
10. Mô hình tham chiếu hoặc ảnh đối chiếu cho thứ tự vẽ cây (chưa TESTED).
11. 15 điểm spawn, package.ini trên điện thoại.

## 3. Đề xuất kiến trúc cuối cho Unity (DESIGN DECISION đề xuất)
- **Asset**: công cụ offline Python (thêm đường TYPE_FRAME) → bản trích `.spr` nguyên + atlas PNG RGBA (straight alpha) + JSON {W,H,cx,cy,frames,dirs,interval + bảng offset khung (ox,oy,w,h)}; không đưa vào APK PAK gốc; kiểm 100% khung bằng `spr_scan` (đã có).
- **Đồng hồ**: một `SimClock` bước cố định (đề xuất 18 Hz logic để khớp dữ liệu gốc + nội suy hiển thị 60 Hz) cho gameplay; animation quái/đạn chạy theo "khung logic" (đúng gốc) chứ không theo `interval`; vật thể cảnh động dùng ms thật (đúng gốc). Mọi timer U003 (cast 1 s, tick 500 ms, cooldown 1 s, respawn 2 s) tính bằng giây trên `SimClock`, độc lập FPS.
- **Hướng**: một hàm `Dir64FromVector(dx,dy)` port nguyên `g_GetNewDirIndex` (bảng sin 64) và `SpriteDir(d64,N)`; vector hướng tính trong không gian MPS (y gấp đôi) cho quái/nhân vật để khớp gốc.
- **Cây che khuất**: port `IpoTree` đúng quy tắc B1–B6, kiểm bằng mô hình tham chiếu/ảnh; chèn lại lá runtime khi đổi toạ độ; quy tắc "cùng y ⇒ chèn sau vẽ sau" giữ nguyên.
- **ani001**: không dùng bảng sắp xếp; 1 sprite/hành động; hoạt ảnh kéo giãn theo khung logic của hành động (đủ để ép về `attackCycle`, `walk…`); neo (160,192) tạm theo A6.
- **Skill 375**: trình diễn theo chuỗi gốc với hai mức: (a) **đúng gốc**: 16 đạn 181 trên lưới 4×4, trễ ngẫu nhiên, 193 sinh tại vị trí 181 va chạm; hoặc (b) **rút gọn U003**: số đạn ít hơn nhưng giữ cùng chuỗi hình ảnh. Luật sát thương luôn là luật U003 (AOE tại vị trí 193, tick 500/1000 ms, 20 dmg, cooldown 1 s từ đầu cast).
- **UI**: như báo cáo 54 mục E; cooldown vòng đen co `scaleY` đúng mẫu `KgameWorld.cpp:5527-5540`.

## 4. Test bắt buộc trước khi tạo project (đề xuất)
1. **T-SPR**: chạy `spr_scan` trên toàn bộ pak liên quan; đối chiếu hash từng khung ani001 + hiệu ứng 375 giữa script và bộ giải mã C# tương lai (golden hash).
2. **T-BLEND/ANCHOR**: lấy 3–5 ảnh chụp màn hình client gốc (điện thoại) của: ani001, hiệu ứng 181/193/cast, một cây; so khớp neo, blend, kích thước.
3. **T-DIR**: bảng 64 → sprite8 (C1) có test đơn vị; đối chiếu ảnh sheet 8 hướng ani001 (đã có 1 ca).
4. **T-IPOT**: dựng mô hình tham chiếu thứ tự vẽ (dump từ client gốc hoặc trường hợp tay) cho ≥ 6 cảnh: Tree đơn, Line, Point, hai Tree cắt chéo, nhiều đối tượng cùng chân, vật thể bị `Clone`; so sánh 100% thứ tự.
5. **T-CLOCK**: xác nhận Hz client (đọc/đo) và đo thời lượng cast/đạn gốc bằng quay màn hình để hiệu chỉnh quy đổi khung→giây (không bắt buộc cho luật U003, nhưng cần cho trình diễn đúng nhịp).
6. **T-COORD**: dựng 1 vùng map 45, so gốc cây/nhà với ảnh client (F-C0 của báo cáo 54).
7. **T-SK375**: mô phỏng không UI chuỗi sự kiện mục D2 (trễ ngẫu nhiên, 16 đạn, vị trí 193) và so với số liệu code; kiểm luật U003 (tick 500/1000 ms) khi FPS 15/30/60/144.
8. Điều kiện qua cổng: các test 1–4 đạt, các điểm UNKNOWN 1–6 ở mục 2 được xử lý hoặc chấp nhận bằng văn bản.

## Cần tôi quyết định: có
1. Có cho phép sửa `pak_extract.py` (công cụ dự án, không phải dữ liệu gốc) để thêm đường TYPE_FRAME không? (Hiện tôi chỉ dùng script riêng trong `D:\JX1_U003_work`.)
2. Trình diễn skill 375: giữ đúng gốc (16 đạn, trễ ngẫu nhiên) hay rút gọn (ví dụ 4 đạn) — luật U003 vẫn giữ nguyên.
3. Có cần chụp ảnh client gốc trên điện thoại cho T-BLEND/T-ANCHOR không?
