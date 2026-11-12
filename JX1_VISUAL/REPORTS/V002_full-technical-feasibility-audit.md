# JX1 COCOS V3 — THẨM ĐỊNH KỸ THUẬT TOÀN DIỆN VỀ KHẢ NĂNG PHÁT TRIỂN ĐỘC LẬP

Ngày: 2026-11-12. Loại nhiệm vụ: READ-ONLY AUDIT. Không sửa source, asset, cấu hình, database, VM; không build; không chạy server; không commit/push.
Công việc chỉ ghi vào `C:\Jx1CocoV3_RESEARCH` (báo cáo này, 4 script chỉ-đọc mới trong `scripts\`, 2 file CSV mới trong `data\`).

**Nhãn độ tin cậy:** VERIFIED (kiểm chứng trực tiếp trong phiên này) · PROBABLE (có cơ sở, chưa đủ bằng chứng) · UNKNOWN · BLOCKED · NOT TESTED (chỉ phân tích, chưa thử trên máy).
**Viết tắt đường dẫn:** `CLIENT` = `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client` · `SRV` = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline` · `RUNTIME` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_` · `CDN` = `C:\Jx1CocoV3\data_cdn\data` · `DOCS` = `C:\Jx1CocoV3\docs-analysis`.

**Lưu ý phạm vi quan trọng:** mã client trong repo (`CLIENT`) là bản **gốc chưa vá**. Các bản vá độ mượt P31–P47 của dự án nằm ở bản build riêng `D:\Android\b\Client` (ngoài repo, không thẩm định lại ở đây). Mọi số dòng dưới đây là của bản trong repo.

---

## 1. EXECUTIVE SUMMARY

1. **Không tìm thấy cơ chế nào cố ý ẩn hay giảm khung hình của chiêu thức.** Cái có thật là bốn giới hạn kiến trúc: (a) toàn bộ hoạt ảnh chạy theo nhịp logic 18 lần/giây, mỗi nhịp tối đa một khung; (b) hoạt ảnh nhân vật và đạn bay chọn khung theo *tiến độ hành động*, nên hành động ngắn hơn số khung của ảnh thì khung bị nhảy cóc; (c) hiệu ứng bị cắt khi hết thời gian sống; (d) vật thể ngoài màn hình không được vẽ. (VERIFIED trong mã.)
2. **Asset có số khung khiêm tốn.** Trung vị 10–11 khung mỗi hướng cho hiệu ứng kỹ năng (280 file SPR đã đọc header), 11–18 khung mỗi hướng cho động tác nhân vật, 8 hướng, 256 màu. Phần lớn hiệu ứng **đã phát gần hết khung đang có**: hiệu ứng va chạm/tan biến phát 96–100% số khung; đạn bay phát 85% (4.342/5.116 khung theo mô hình). Muốn mượt hơn hẳn thì phải **tạo thêm khung mới**, không phải "mở khóa" khung đang bị giấu.
3. **Có thể phát đủ khung hiện có và tăng số khung**, nhưng cần sửa mã client (đổi chọn khung từ theo-nhịp sang theo-thời-gian-vẽ) và cần viết bộ mã hóa SPR. Định dạng PAK và SPR đã được giải mã đầy đủ từ mã nguồn; chưa có lần nào thay ảnh SPR rồi cho game nạp (NOT TESTED).
4. **Làm chủ asset: đạt 4/5 cấp cho dữ liệu văn bản, 2/5 cấp cho hình ảnh.** Đọc và trích xuất: có công cụ của dự án. Đóng gói lại và game nạp: đã làm với file cấu hình (`update10.pak`). Với ảnh SPR: chưa có bộ mã hóa, chưa thử.
5. **Client riêng: khả thi trên nền source này.** Có đủ mã, build được APK. Rào cản là nợ kỹ thuật (file 15 nghìn dòng, UI trùng lặp, engine Cocos đã bị sửa), không phải thiếu mã.
6. **Server riêng: khả thi bằng cách dựng từ source, không khả thi rẻ nếu viết mới.** Lưu ý quan trọng: **source server trong repo không khớp giao thức với client ở 18 struct gói tin** (VERIFIED), nên không thể "chỉ đổi IP". Dự án đã từng sửa 7 struct trên bản copy để server tự dựng chạy được với client (báo cáo dự án số 45).
7. **Khuyến nghị: CONTINUE WITH RESTRUCTURING** (Phương án 2 — kế thừa có chọn lọc). Không có trở ngại kỹ thuật nào buộc dừng. Rủi ro lớn nhất không phải kỹ thuật: **chưa có tài liệu chứng minh quyền sử dụng mã và asset** (mã ghi "Copyright Kingsoft 2003"). Tôi không kết luận pháp lý.

---

## 2. DANH SÁCH VÀ ĐÁNH GIÁ 11 BÁO CÁO ĐẦU VÀO

Đủ 11 file (VERIFIED: tồn tại, không rỗng).

| # | File | Đường dẫn | Kích thước | Nội dung và phạm vi | Mức đọc trong phiên này |
|---|---|---|---:|---|---|
| 1 | INVENTORY_MASTER.md | `C:\Jx1CocoV3_INVENTORY_REPORTS\` | 2.148.792 | Tổng số file/thư mục/byte, nhánh gốc, thống kê đuôi file, cây thư mục, thư mục rỗng, tên trùng, bất thường, giới hạn | Đọc trọn phần đầu (dòng 1–254), bất thường, ghi chú thực thi, giới hạn. Cây thư mục và danh sách tên trùng (≈9.700 dòng liệt kê) được tra bằng tìm kiếm, **không đọc từng dòng** |
| 2 | CLIENT_SOURCE_INVENTORY.md | như trên | 7.528 | Công nghệ, điểm vào, cấu hình render, mô-đun, thư viện, nạp tài nguyên của client | Đọc toàn bộ |
| 3 | SERVER_SOURCE_INVENTORY.md | như trên | 5.198 | Hai cây mã server, mô-đun, điểm vào, DB, runtime | Đọc toàn bộ |
| 4 | ASSET_INVENTORY.md | như trên | 4.354 | Asset rời, PAK/APK/archive, băm | Đọc toàn bộ |
| 5 | ASSET_REFERENCE_COVERAGE.md | như trên | 107.719 | 1.069 literal tài nguyên trong mã client; 254 khớp file rời, 815 chưa khớp | Đọc 120 dòng đầu và phần "FOUND_LOOSE"; toàn bộ nội dung được tái lập bằng script riêng (1.113 literal) |
| 6 | FILE_MANIFEST.csv | như trên | 6.858.913 | 35.211 dòng: đường dẫn, đuôi, byte, thời gian, nhóm, SHA-256 (48 file CDN) | Xử lý bằng script và tìm kiếm; **không đọc từng dòng** |
| 7 | TECHNICAL_ARCHITECTURE_REVIEW.md | `C:\Jx1CocoV3_RESEARCH\` | 14.363 | Kiến trúc client/server, chất lượng nguồn | Đọc toàn bộ (do tôi viết ở phiên trước) |
| 8 | ASSET_FORMAT_RESEARCH.md | như trên | 15.031 | Định dạng PAK, hash, nén, SPR, đối chiếu literal | Đọc toàn bộ |
| 9 | CLIENT_SERVER_DEPENDENCY_MAP.md | như trên | 12.061 | Sơ đồ thành phần, giao thức, so khớp ID | Đọc toàn bộ |
| 10 | INVENTORY_GAPS_AND_RISKS.md | như trên | 8.933 | Lỗ hổng kiểm kê, rủi ro | Đọc toàn bộ |
| 11 | PHASE_2_RESEARCH_PLAN.md | như trên | 9.815 | Kế hoạch nghiên cứu (chưa triển khai) | Đọc toàn bộ |

### 2.1 Thiếu sót, mâu thuẫn và điểm đã được sửa bởi phiên thẩm định này
| Báo cáo cũ nói | Kết quả thẩm định | Mức |
|---|---|---|
| "Cần viết trình giải nrv2b độc lập" (#11), "không có công cụ ghi PAK trong nguồn gốc" (#7) | Dự án **đã có** `DOCS\tools\pak_extract.py` (giải nén nrv2b/d/e), `pak_replace.py`, `pak_verify.py`. Báo cáo #11 bỏ sót | VERIFIED (đọc mã công cụ, đã dùng trong phiên này) |
| Cờ nén `0x11` "rơi vào nhánh mặc định nrv2b" (#8) | Sai cho SPR. Bit `0x10000000` là `TYPE_FRAME`: SPR lưu header thô + nén **từng khung** (`XPackFile::GetSprHeader`, `GetSprFrame`). 22/280 SPR kỹ năng thuộc loại này | VERIFIED |
| "Đường giải RLE → texture: UNKNOWN" (#7, #8) | Đã truy ra: `CLIENT\Classes\engine\Kgetinidata.cpp` (mục 3.4) | VERIFIED |
| "ID giao thức khớp; struct payload UNKNOWN" (#9) | **18 struct khác nhau** giữa client và source gameserver (mục 10.2) | VERIFIED (so văn bản) |
| "Thứ gì quyết định độ mượt chưa đọc" (#7) | Đã đọc: `KSprControl`, `KNpcRes::Draw`, `KMissleRes::Draw`, `KSkillSpecial` (mục 3–5) | VERIFIED |
| Kiểm kê (#2–#5) không nêu | Bảng dữ liệu client và server **khác nhau**: `Missles.txt` 91.532 byte (PAK client) vs 93.775 (server); `Skills.txt` 747.008 vs 764.878; `Npcs.txt` 742.553 vs 753.810 | VERIFIED (băm trong bộ nhớ) |
| Kiểm kê không nêu | Engine Cocos đi kèm **đã bị sửa**: `CCTextureCache::addImageWihtData` (không có trong Cocos gốc) | VERIFIED (`CLIENT\cocos2d\cocos\renderer\CCTextureCache.h`) |

---

## 3. KIẾN TRÚC ANIMATION HIỆN TẠI

Game **không dùng** hệ animation của Cocos2d-x (`Animation`/`Animate`/atlas/Spine). Nó dùng cơ chế **tùy chỉnh frame-by-frame của engine Kingsoft gốc**: mỗi đối tượng tự giữ chỉ số khung, mỗi lần vẽ yêu cầu "file SPR + số khung", khung được giải mã thành một texture riêng. (VERIFIED)

### 3.1 Đồng hồ: nhịp logic 18 lần/giây
- `CLIENT\Classes\gamecore\KSubWorld.cpp:148` — `++m_dwCurrentTime; //每秒18帧`: bộ đếm nhịp, tăng 1 mỗi lần `KSubWorld::Activate`.
- `CLIENT\Classes\gamecore\KProtocolProcess.cpp:3227` — `SubWorld[0].m_dwCurrentTime = WorldSync->Frame;`: bộ đếm được đồng bộ lại theo server.
- `CLIENT\Classes\vn\gamescence\KgameWorldVN.cpp` hàm `KgameWorldVN::draw` (dòng 1541–1544): `while (nLoopCount * 1000 <= timerStart.GetElapse() * 18 && loopCount < MAX_BREATHE_LOOP) { g_pCoreShell->Breathe(); ... }` với `MAX_BREATHE_LOOP = 128`. Tức là mỗi khung vẽ chạy bù đủ số nhịp logic còn thiếu, tốc độ 18 nhịp/giây.
- Khung vẽ yêu cầu 60/giây (`CLIENT\Classes\AppDelegate.cpp`, `setAnimationInterval(1.0f/60)`). Một trạng thái logic được vẽ lại khoảng 3,3 lần.

### 3.2 Bộ điều khiển khung `KSprControl`
File: `CLIENT\Classes\gamecore\KSprControl.h/.cpp`. Trường: `m_nTotalFrame`, `m_nCurFrame`, `m_nTotalDir`, `m_nCurDir`, `m_dwTimer`, `m_dwInterval`, tên file SPR.
- **`GetNextFrame` (dòng 342–374):** `if (SubWorld[0].m_dwCurrentTime != m_dwTimer) { m_dwTimer = ...; m_nCurFrame++; ... }`. Nghĩa là **mỗi nhịp logic tăng đúng 1 khung**, bất kể `m_dwInterval`. Hết khung của hướng hiện tại thì quay vòng (`bLoop`) hoặc dừng ở khung cuối.
- **`m_dwInterval` không được dùng** trong `GetNextFrame`. Bản gốc theo thời gian vẫn còn dưới dạng mã đã comment trong `SRV\gameserver\Sources\Core\Src\KSprControl.cpp` (`if (m_dwCurrentTime - m_dwTimer >= m_dwInterval) ... else m_nCurFrame = ... * (dt) / m_dwInterval`), và còn sống ở hàm `ChangeCurFrame` (dòng 297–335) nhưng **không nơi nào gọi** (lời gọi duy nhất ở `KNpcRes.cpp:368` đã bị comment). VERIFIED.
- `SetCurFrame` (dòng 79–109) đặt thẳng chỉ số khung; dùng cho nhân vật (3.3).

### 3.3 Ba cách chọn khung đang hoạt động
| Loại đối tượng | Hàm | Cách chọn khung | Nguồn số khung |
|---|---|---|---|
| **Thân nhân vật, NPC, quái** (mọi bộ phận: đầu, thân, tay, vũ khí, ngựa, áo choàng, cánh) | `KNpcRes::Draw(nNpcIdx, nDir, nAllFrame, nCurFrame, bInMenu)`, `CLIENT\Classes\gamecore\KNpcRes.cpp:241`; bản VN `vn\gamecore\KNpcResVN.cpp` | Khi `nAllFrame > 0` (dòng 254–289; công thức ở dòng 265 và 286): `nCurFrameNo = nCurDirNo*(nGetFrame/nGetDir) + (nGetFrame/nGetDir) * nCurFrame / nAllFrame` rồi `SetCurFrame`. Khung ảnh = **tiến độ hành động** × số khung mỗi hướng | Số khung ảnh: bảng `NpcRes\*信息.txt` ("tổngKhung,sốHướng,khoảng"). `nAllFrame`/`nCurFrame`: `m_Frames.nTotalFrame/nCurrentFrame` của NPC, tính bằng nhịp logic |
| **Đạn đang bay** (`MS_DoFly`) | `KMissleRes::Draw`, `CLIENT\Classes\gamecore\KMissleRes.cpp:128–212`; gọi từ `KMissle.cpp:1185, 1192` với `nAllFrame = m_nLifeTime - m_nStartLifeTime`, `nCurLifeFrame = m_nCurrentLife - m_nStartLifeTime` | Lặp (`LoopPlay=1`): `nFrame = (nCurLifeFrame / nInterval) % nTotalFrame` (dòng 180; có biến thể lặp đoạn con dòng 185–192). Không lặp: `nFrame = nTotalFrame * nCurLifeFrame / nAllFrame` (dòng 197). Vượt khung cuối thì không vẽ (dòng 199) | Bảng `\settings\Missles.txt`, cột `AnimFileInfoN` = "tổngKhung,sốHướng,khoảng" (`KMissle.cpp:270–274`) |
| **Hiệu ứng tức thời** (chờ, tan biến, va chạm của đạn; hiệu ứng trạng thái/buff; hiệu ứng đặc biệt trên người; vật thể rơi, xác) | `KSkillSpecial::DrawC` (`KSkillSpecial.cpp:84`), `KNpcRes::Draw` dòng 391–412, `KObj.cpp:632–722` | `GetNextFrame`: **1 khung mỗi nhịp** | Số khung lấy từ **header SPR** (`KSkillSpecial::SetFrameSpr` gọi `m_ImageStore.GetImageParam`). Thời gian sống của hiệu ứng lại lấy từ **bảng**: `KMissle.cpp:1924` `m_nEndTime = m_nBeginTime + nInterval * nTotalFrame / nDir` |

Độ dài hành động của nhân vật (đơn vị nhịp), VERIFIED:
- `\settings\npc\player\BaseValue.ini` (bản client, trong `updata02.pak`, đọc trong bộ nhớ): `AttackFrame=18, CastFrame=18, HurtFrame=10, WalkFrame=12, RunFrame=14, StandFrame=25 (nam) / 45 (nữ)`. Nạp ở `KNpcSet.cpp:95–112` (`PLAYER_BASE_VALUE`, `CoreUseNameDef.h:108`).
- Đánh thường: `m_Frames.nTotalFrame = m_AttackFrame * naAttackSpeed / (nbAttackSpeed + m_CurrentAttackSpeed)` (`KNpc.cpp:2381`); phép: tương tự với `m_CastFrame`, `m_CurrentCastSpeed` (`KNpc.cpp:2399`); `naAttackSpeed = nbAttackSpeed = 100` mặc định (`KGameglobalSet.cpp:20–21`). Chạy: `m_RunFrame * m_RunSpeed / m_CurrentRunSpeed` (`KNpc.cpp:2092`).
- NPC/quái: từ bảng `Npcs.txt` (`KNpcTemplate.cpp:47–54`).

### 3.4 Từ khung SPR tới màn hình
1. `KRUImage` (tên file + `nFrame`) → `g_GameWorld->getIniDataForGame(...)` (`CLIENT\Classes\gamescene\KgameWorld.h:117`).
2. `Kgetinidata::findinidata_one` / `findinidata_new` (`CLIENT\Classes\engine\Kgetinidata.cpp:100–390, 570–740`): lấy header và khung qua `KImageStore2` → `KPakList` → `XPackFile`.
3. Giải RLE (dòng 236–366): chuỗi cặp `(số điểm, alpha)`; `alpha == 0` là đoạn trong suốt; ngược lại theo sau là `số điểm` chỉ số màu trong bảng 256 màu RGB. Kết quả RGBA8888.
4. Tạo texture qua `CCTextureCache::addImageWihtData(key, ...)` (dòng 375, 729), khóa cache `"<id file>-<số khung>"` (dòng 157). **Mỗi khung một texture, không có atlas.**
5. Nếu tên file kết thúc `.png`/`.jpg`, `findinidata_new` nạp ảnh thường với `*mFrams = 1` (dòng 576–586): **ảnh màu thật chỉ dùng được cho hình một khung**.

### 3.5 Kết thúc, lặp, chuyển hoạt ảnh
- Nhân vật: hết `m_Frames.nTotalFrame` nhịp thì logic chuyển trạng thái (ví dụ `KNpc.cpp:1840, 1885` `WaitForFrame()`); hoạt ảnh không tự quyết.
- Hiệu ứng tức thời: `GetNextFrame(FALSE)` trả FALSE ở khung cuối rồi `Release()`; đồng thời bị xóa khi `dwCurrentTime > m_nEndTime` (`KMissleRes.cpp:223–236`).
- Đạn: hết `m_nLifeTime` hoặc va chạm thì chuyển `MS_DoVanish`/`MS_DoCollision` (`KMissle.cpp:419, 1527–1606`).

---

## 4. KẾT QUẢ ĐIỀU TRA SỐ KHUNG

Phương pháp: script chỉ-đọc `scripts\audit_missile_frames.py` và `scripts\audit_character_frames.py` đọc bảng dữ liệu, tính hash tên file, tìm trong 34 PAK theo đúng thứ tự `paklist`, đọc **header SPR trong bộ nhớ** bằng hàm của `DOCS\tools\pak_extract.py`. Không ghi file nào vào cây game. Kết quả: `data\missile_frame_audit.csv` (727 dòng), `data\character_frame_audit.csv` (2.203 dòng).

### 4.1 Hiệu ứng kỹ năng và đạn (toàn bộ bảng `Missles.txt` của client)
- 727 ô hoạt ảnh, **286 file SPR khác nhau**; 280 đọc được header, 6 không tìm thấy bằng hash (UNKNOWN, có thể khác mã hóa tên).
- Mọi SPR: 256 màu. Số khung mỗi hướng: **trung vị 11**. Tổng 11.131 khung.
- Khoảng thời gian khung ghi trong header SPR (mili giây/khung, suy từ `SetFrameSpr`: `khung × nInterval / 50`): 50 ms (87 file), 30 ms (38), 20 ms (22), 40 ms (19), 100 ms (16), 80 ms (10)… Tức là **tác giả asset đã thiết kế nhiều hiệu ứng ở 25–50 hình/giây**, nhưng engine phát tối đa 18 hình/giây.

| Nhóm | Số ô đọc được | Bảng khớp header SPR | Bảng khai ít khung hơn SPR | Bảng khai nhiều hơn SPR |
|---|---:|---:|---:|---:|
| Đạn bay (`AnimFile2`) | 369 | 309 | **19** | 41 |
| Va chạm (`AnimFile4`) | 240 | 201 | **6** | 33 |
| Tan biến (`AnimFile3`) | 42 | 39 | **3** | 0 |
| Dự phòng (`AnimFileB*`) | 66 | 50 | 0 | 16 |

"Bảng khai ít hơn SPR" = **asset có khung mà cấu hình không dùng** (trường hợp 2 của câu hỏi). Ví dụ đạn 129/131/132/133/240: bảng 20 khung, SPR có 36; đạn 259: 16 so với 43; đạn 268: 64 so với 168. Tổng 28 ô. VERIFIED.

### 4.2 Số khung thực sự được phát (mô hình theo đúng công thức mã, giả định đạn sống hết `LifeTime`)
| Nhóm | Số ô | Phát ít hơn số khung mỗi hướng | Trong đó chỉ thiếu 1 khung | Phát ≤ 50% | Khung phát / khung có |
|---|---:|---:|---:|---:|---|
| Đạn bay (bỏ 15 ô khai >200 khung/hướng) | 357 | 84 (24%) | 17 | 24 | 4.342 / 5.116 (85%) |
| Va chạm | 240 | 8 (3%) | 1 | 5 | 2.494 / 2.587 (96%) |
| Tan biến | 39 | 0 | 0 | 0 | 749 / 749 (100%) |

Ví dụ thiếu nhiều: đạn 179 `\spr\skill\kl\傲雪萧风.spr` 54 khung nhưng sống 15 nhịp → phát 15; đạn 447 `hs_龙旋气劲_被击.spr` 23 khung, sống 5 nhịp → 5; đạn 308/311/312 `mag_cy_08_冰墙_b.spr` 7 khung với khoảng 150 nhịp → thực tế đứng ở 1 khung; va chạm 377 `投石冰爆炸.spr` SPR có 27 khung, bảng khai 8 → phát 9.
Mức: PROBABLE (mô hình từ mã, **NOT TESTED** trên thiết bị; `LifeTime` có thể bị kỹ năng ghi đè, đạn có thể va chạm sớm hơn).

### 4.3 Nhân vật người chơi (thân nam 12 bộ + nữ 5 bộ, 48 động tác, 816 SPR)
- 816/816 khớp bảng. 8 hướng, khung vẽ 320×320, header `nInterval = 1`.
- Khung mỗi hướng (min/trung vị/max): đứng 8–15; đi 12/15/15; **chạy 11/11/12**; bị thương 6–12; chết 10–18; **đánh tay không 12/18/18**, đâm 13/16/16, chém 13/14/14, giáo 12–13, song đao 12–16, ám khí 12/16/16; **phép 10–16**; ngồi 9–12; cưỡi ngựa đánh 12–14.
- So với độ dài hành động: đánh 18 nhịp ở tốc độ gốc → 18 khung/18 nhịp, **phát đủ**. Khi tốc độ đánh +50%: 12 nhịp cho 18 khung → **mất 6 khung**; +100%: 9 nhịp → mất 9 khung. Chạy 14 nhịp cho 11 khung → đủ (có khung lặp), nhưng khi tốc chạy tăng thì số nhịp giảm theo `KNpc.cpp:2092`.
- Kết luận: với nhân vật, **asset và code đều có đủ khung; khung bị nhảy cóc là hệ quả trực tiếp của chỉ số tốc độ đánh/chạy** (trường hợp 3). VERIFIED công thức; NOT TESTED trên thiết bị.

### 4.4 NPC và quái (120 loại đầu bảng, 14 động tác, 1.383 SPR đọc được)
- 1.358 khớp bảng, 23 ô bảng khai ít hơn SPR, 2 nhiều hơn, 4 không tìm thấy.
- Khung mỗi hướng (min/trung vị/max): đứng 6/10/19; đi, chạy 8/15/30; bị thương 5/6/14; chết 8/15/44; đánh 11/14,5/22; phép 11/15/22.

### 4.5 Phân loại theo ba trường hợp của đề bài
| Trường hợp | Có xảy ra? | Ở đâu |
|---|---|---|
| 1. Asset chỉ có ít khung | **Có, là trường hợp phổ biến nhất.** Trung vị 10–11 khung/hướng cho hiệu ứng; 11–18 cho động tác | Toàn bộ |
| 2. Asset nhiều khung, code/cấu hình chỉ dùng một phần | Có, ít: 28 ô đạn/hiệu ứng (bảng khai thiếu), 23 ô NPC | 4.1, 4.4 |
| 3. Đủ khung nhưng không phát hết | Có: đạn bay 24% số ô; nhân vật khi tốc độ đánh/chạy cao | 4.2, 4.3 |

---

## 5. CƠ CHẾ ẨN, BỎ QUA HOẶC GIỚI HẠN KHUNG

**Kết luận: không có cơ chế cố ý giấu khung của chiêu thức.** Dưới đây là mọi cơ chế tìm được có thể làm hoạt ảnh không hiện đủ.

| # | Cơ chế | Vị trí | Điều kiện | Phạm vi | Loại | Mức |
|---|---|---|---|---|---|---|
| 1 | Lượng tử 18 Hz: tối đa 1 khung mỗi nhịp | `KSprControl.cpp:342–374`; `KSubWorld.cpp:148` | Luôn luôn | Toàn bộ hoạt ảnh | Giới hạn tốc độ phát | VERIFIED |
| 2 | Bỏ qua `m_dwInterval` (tốc độ tác giả đặt) | cùng chỗ; bản theo thời gian bị comment ở `SRV\...\KSprControl.cpp` | Luôn luôn | Hiệu ứng dùng `GetNextFrame` | Đổi tốc độ, không mất khung | VERIFIED |
| 3 | Chọn khung theo tiến độ hành động | `KNpcRes.cpp:254–289` | Số nhịp hành động < số khung mỗi hướng (tốc đánh/chạy cao) | Nhân vật, NPC, quái | **Nhảy cóc khung** | VERIFIED công thức |
| 4 | Chọn khung đạn theo tuổi thọ | `KMissleRes.cpp:180–199` | `LifeTime` ngắn hoặc `khoảng` lớn | Đạn bay | Nhảy cóc / không tới khung cuối | VERIFIED công thức |
| 5 | Cắt theo thời gian sống của hiệu ứng | `KMissle.cpp:1924`; `KMissleRes.cpp:223–236` | Bảng khai ít khung hơn SPR | Hiệu ứng chờ/tan/va chạm | Cắt đuôi | VERIFIED |
| 6 | Logic gameplay chuyển trạng thái | `KMissle.cpp:419, 1527–1606`; `KNpc.cpp` các `WaitForFrame` | Đạn va chạm, NPC chết, đổi lệnh | Tất cả | Kết thúc sớm | VERIFIED |
| 7 | Cắt theo vùng nhìn | `CoreDrawGameObj.cpp` nhánh `CGOG_MISSLE` (dòng 161): ngoài `visibleSize` thì `break` | Đạn/vật thể ngoài màn hình | Đạn, vật thể | Không vẽ (khung vẫn "chạy" theo thời gian) | VERIFIED |
| 8 | Tùy chọn ẩn đạn của người khác | `CoreDrawGameObj.cpp:164` `nIsHideMis`; đặt ở `gameui\KuiOptions.cpp:268`, `KgameWorldVN.cpp:328` | Người chơi bật trong cài đặt | Đạn không phải của mình | Ẩn toàn bộ | VERIFIED |
| 9 | Tùy chọn ẩn NPC / người chơi khác | `KNpc.cpp:5889–5895` `nIsHideNpc`, `nIsHidePlayer` | Người chơi bật | NPC, người khác | Ẩn toàn bộ | VERIFIED |
| 10 | Tự ẩn NPC/người chơi khi FPS < 10 | `KgameWorldVN.cpp` khối "TOI UU HOA" từ dòng 3813, nằm trong `/* … */` | — | — | **Đã comment, không chạy** | VERIFIED |
| 11 | `m_bIsHideMissle` | `CoreDrawGameObj.cpp:167`; khởi tạo `KNpc.cpp:268` | Không nơi nào đặt TRUE | — | Không hoạt động | VERIFIED |
| 12 | Chạy bù nhiều nhịp trong một khung vẽ | `KgameWorldVN::draw`, `MAX_BREATHE_LOOP 128` | Khung vẽ chậm (giật) | Tất cả | Hiệu ứng chỉ tăng 1 khung/lần vẽ nhưng đồng hồ nhảy nhiều nhịp → bị cắt đuôi | VERIFIED mã; tần suất NOT TESTED |
| 13 | Giới hạn số lượng | `KMissle.h:6` `MAX_MISSLE 30000`; `KNpc.h:25` 5 số sát thương cùng lúc | Vượt ngưỡng | Đạn; chữ số sát thương | Không tạo thêm | VERIFIED hằng số |

Không tìm thấy: giảm chất lượng theo cấu hình máy, giới hạn số hiệu ứng theo FPS, bỏ khung theo tải CPU/GPU (tìm theo các từ khóa `skip`, `quality`, `MaxShow`, `HideEffect`… trong toàn bộ `Classes`). Mức: VERIFIED trong phạm vi từ khóa đã tìm; không loại trừ tuyệt đối cơ chế đặt tên khác.

Phân biệt theo yêu cầu: (a) bị bỏ qua khi phát: #3, #4; (b) không được nạp: không có — khung được nạp theo nhu cầu, từng khung; (c) không tồn tại trong asset: trường hợp phổ biến (mục 4.5); (d) chạy nhưng không vẽ: #7–#9; (e) kết thúc sớm do gameplay: #5, #6, #12.

---

## 6. KHẢ NĂNG MỞ TỐI ĐA KHUNG HIỆN CÓ

| Tình huống | Cần gì | Loại can thiệp | Mức khả thi |
|---|---|---|---|
| 28 ô đạn/hiệu ứng và 23 ô NPC mà bảng khai ít khung hơn SPR | Sửa số trong `Missles.txt` / bảng `NpcRes` của client | **Chỉ đổi cấu hình** (file văn bản trong PAK; đã có công cụ thay mục PAK) | Cao. NOT TESTED |
| 8 hiệu ứng va chạm bị cắt đuôi | Như trên (tăng `khoảng × khung` trong bảng) | Cấu hình | Cao. NOT TESTED |
| Đạn bay phát thiếu khung (84 ô) | Không nên đổi `LifeTime`/`Speed` vì đó là tầm bay, do server quyết. Phải đổi **công thức chọn khung** ở `KMissleRes::Draw` | **Sửa logic phát** phía client (một hàm) | Cao về kỹ thuật. NOT TESTED |
| Nhân vật nhảy cóc khung khi tốc đánh cao | Chọn khung bằng tiến độ **có phần lẻ theo thời gian vẽ** thay vì theo nhịp nguyên: ở 60 hình/giây, đòn đánh 12 nhịp (0,67 s) có 40 lần vẽ, đủ chỗ cho 18 khung | **Sửa logic phát** ở `KNpcRes::Draw` (và bản VN) | Trung bình-cao. Dự án đã làm nội suy vị trí theo cách tương tự (báo cáo dự án 31, 34, 46). NOT TESTED |
| Hiệu ứng `GetNextFrame` | Đã phát mỗi nhịp một khung, **không có khung nào để mở thêm**. Chỉ có thể trả lại tốc độ tác giả đặt bằng cách dùng lại đường theo thời gian (`ChangeCurFrame` có sẵn, đang bỏ không) | Sửa logic (nhỏ) | Cao. Hệ quả: hiệu ứng 30 ms/khung sẽ **ngắn lại**, không mượt hơn |
| Bộ giải mã / loader | Không cần sửa để phát khung đang có | — | — |
| Giới hạn kiến trúc không vượt được | Không có, nhưng không thể hiển thị nhiều hình khác nhau hơn số khung asset có | — | VERIFIED |

Ảnh hưởng tài nguyên (ước tính, NOT TESTED): phát đủ khung hiện có **không tăng** số texture tối đa mỗi SPR, nhưng tăng số texture được giải mã trong một đòn đánh. Mỗi khung là một texture RGBA8888 không nén (`rộng × cao × 4` byte) và một lần giải RLE trên CPU ở luồng chính lần đầu dùng. Dự án đã đo thấy giải mã texture trên luồng chính gây khung chậm (báo cáo dự án 46). Trên máy yếu, rủi ro chính là giật lần đầu và bộ nhớ texture, không phải GPU.

**Phân biệt bắt buộc:** các việc trên chỉ *hiển thị đủ khung đã có*. Chúng không làm hoạt ảnh 11 khung thành 22 khung.

---

## 7. KHẢ NĂNG TẠO THÊM KHUNG VÀ NÂNG CẤP ANIMATION

| Câu hỏi | Trả lời | Bằng chứng | Mức |
|---|---|---|---|
| 1. Tăng số khung từ dữ liệu hiện có? | Chỉ bằng nội suy ảnh (sinh khung trung gian bằng công cụ ngoài). Dữ liệu gốc không chứa khung ẩn ngoài 28+23 ô ở mục 4 | Mục 4 | VERIFIED phần dữ liệu; chất lượng nội suy UNKNOWN |
| 2. Bổ sung khung mới vào animation? | **Định dạng cho phép**: `SPRHEAD.Frames` là số 16-bit; bảng khai "tổngKhung,sốHướng,khoảng" tùy ý. Cần bộ **mã hóa SPR** (chưa có) và thay mục trong PAK (đã có) | `CLIENT\Classes\engine\KbugInfo.h:238–269`; `DOCS\tools\pak_replace.py` | PROBABLE (định dạng VERIFIED, quy trình NOT TESTED) |
| 3. Thay animation cũ bằng bộ tự tạo? | Có, cùng điều kiện câu 2. Giới hạn: 256 màu mỗi file, alpha 8 bit theo đoạn, tối đa 16 MiB nén mỗi mục PAK (nén cả file) hoặc dùng nén từng khung | `Kgetinidata.cpp:236–366`; `XPackFile.cpp` `ReadElemFile`, `GetSprFrame` | PROBABLE |
| 4. Đổi FPS phát độc lập với số khung? | **Hiện không**: tốc độ gắn cứng vào nhịp 18 Hz. Làm được bằng sửa mã (chọn khung theo thời gian vẽ) | Mục 3.2 | VERIFIED hiện trạng; sửa đổi NOT TESTED |
| 5. Nâng cấp chuyển động không đổi gameplay? | Có, nếu chỉ đổi phía hiển thị client (chọn khung, số khung ảnh). Thời điểm gây sát thương do server tính theo nhịp (`ATTACKACTION_EFFECT_PERCENT 60`, theo báo cáo dự án 33) không phụ thuộc số khung ảnh | Mục 3.3; báo cáo dự án 33 | PROBABLE |
| 6. Áp dụng cho toàn bộ skill hay từng nhóm? | Sửa mã áp dụng theo **3 nhóm cơ chế** (nhân vật / đạn bay / hiệu ứng tức thời). Sản xuất khung mới phải làm **từng file SPR** (286 file hiệu ứng, hàng nghìn file nhân vật × 8 hướng) | Mục 3.3, 4 | VERIFIED |

### Quy trình đề xuất (chưa thực hiện, cần duyệt từng bước)
1. **Đo trước:** quay màn hình một kỹ năng mẫu ở 60 hình/giây, đếm số hình khác nhau thật sự hiện ra (kiểm chứng mô hình mục 4.2).
2. **Viết bộ mã hóa/giải mã SPR độc lập** (PNG ↔ SPR, cả dạng nén từng khung), kiểm bằng vòng khép kín: giải → mã hóa → so từng điểm ảnh với bản gốc.
3. **Thử thay một SPR** trong bản copy PAK phục vụ qua CDN thử, xác nhận game nạp và hiển thị (cấp độ 5 của mục 8).
4. **Sửa chọn khung theo thời gian vẽ** cho một nhóm (đề xuất: đạn bay trước), đo lại bước 1.
5. Sau đó mới sản xuất khung mới (nội suy hoặc vẽ lại) cho một kỹ năng mẫu, đo bộ nhớ texture và thời gian giải mã trên máy yếu.
6. Nếu cần vượt 256 màu: mở rộng loader để nhận chuỗi PNG/atlas nhiều khung (hiện `findinidata_new` chỉ nhận PNG một khung). Đây là thay đổi cấu trúc dữ liệu, làm sau cùng.

---

## 8. KHẢ NĂNG LÀM CHỦ ASSET

Năm cấp độ: (1) đọc được · (2) trích xuất được · (3) chỉnh sửa được · (4) đóng gói lại được · (5) game nạp và hiển thị bản đã thay.

| Nhóm | Định dạng, nơi lưu | Cách nạp | (1) | (2) | (3) | (4) | (5) | Cần công cụ riêng / sửa source |
|---|---|---|---|---|---|---|---|---|
| Nhân vật, quái, NPC | SPR 256 màu, 8 hướng, 320×320; trong `spr.pak`, `image1/2.pak`, `update.pak`… Bảng ghép bộ phận: `\settings\npcres\*.txt` | `KNpcRes` → `Kgetinidata` | VERIFIED (đọc header 2.199 file) | PROBABLE: `pak_extract.py` giải được dạng nén cả file; dạng nén từng khung (cờ `0x10`) công cụ hiện tại **chưa hỗ trợ** | NOT TESTED (chưa có bộ chuyển SPR→PNG) | NOT TESTED (chưa có bộ mã hóa SPR) | NOT TESTED | Cần bộ mã hóa SPR. Không cần sửa source nếu giữ định dạng |
| Skill, hiệu ứng, đạn | SPR; chủ yếu `skills.pak` (170 file), `update.pak` (77), `image2.pak` (32). Bảng: `Missles.txt`, `Skills.txt` | `KMissleRes`, `KSkillSpecial` | VERIFIED (280 header) | PROBABLE như trên | NOT TESTED | NOT TESTED | NOT TESTED | Như trên |
| Bảng dữ liệu và cấu hình (INI, TXT, TAB, Lua) | Văn bản GBK trong `updata*.pak`, `setting.pak`, `script*.pak` | `KIniFile`, `KTabFile`, `KLuaScript` | VERIFIED | VERIFIED (đã đọc `BaseValue.ini`, `Missles.txt` từ PAK) | VERIFIED khả năng (văn bản) | VERIFIED: `pak_replace.py` + `pak_verify.py` | **VERIFIED bởi dự án** với `FsjxClient.ini` trong `update10.pak` (báo cáo dự án 08; client đăng nhập được, theo CLAUDE.md). Không kiểm lại trong phiên này | Không |
| Map, cảnh nền | `map.pak` 67.487 mục, `mapfix.pak`; server `.wor` trong `maps*.pak` | `KSubWorld`, `KScenePlaceC` | Chỉ đếm mục | UNKNOWN (chưa đọc định dạng) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| UI | Hai nguồn: PNG rời trong `CLIENT\Resources\ui` (qua Cocos) và SPR/INI trong PAK (`\spr\Ui3\…`, `\ui\ui3_800\…`) | Cocos `TextureCache`; `Kgetinidata` | VERIFIED | VERIFIED cho PNG rời | VERIFIED khả năng cho PNG | Không cần (file rời đóng vào APK) | PROBABLE (build APK là quy trình dự án đã làm) | Không cho PNG |
| Icon | SPR trong PAK (`\spr\Ui\技能图标\…`), một phần PNG rời | như UI | VERIFIED hash | PROBABLE | NOT TESTED | NOT TESTED | NOT TESTED | Bộ mã hóa SPR, hoặc đổi tên sang `.png` một khung (loader hỗ trợ) |
| Font | 20 TTF + `.fnt` rời; `font.pak` 3 mục | Cocos `Label`; engine cũ | VERIFIED | VERIFIED (rời) | VERIFIED khả năng | Không cần | PROBABLE | Không |
| Texture | Không có định dạng texture nén (không `.pvr/.dds/.ktx`); mọi thứ giải ra RGBA8888 lúc chạy | `addImageWihtData` | VERIFIED | — | — | — | — | Muốn dùng atlas/texture nén phải sửa source |
| Âm thanh | OGG/WAV/MP3 rời (103 OGG), `sound.pak` 416 mục, `update_music.pak` 41 mục, FMOD `.bank` | FMOD / AudioEngine | Chỉ đếm | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Đánh giá pipeline asset riêng: **xây được**, vì định dạng PAK, hàm hash tên và định dạng SPR đều đã rõ từ mã (không phụ thuộc công cụ gốc `JxStudio.exe`/`str_tool.exe` — vốn bị cấm chạy). Thiếu hai mảnh: bộ mã hóa SPR và hỗ trợ SPR nén từng khung trong công cụ giải. Việc quan trọng nhất chưa làm là **một lần thay ảnh SPR thật và thấy nó trong game**.

Giới hạn chất lượng hình ảnh của định dạng hiện tại (VERIFIED): 256 màu mỗi file; mỗi khung một texture; khung nhân vật 320×320; thiết kế 2D kéo giãn `EXACT_FIT`.

---

## 9. KHẢ NĂNG PHÁT TRIỂN CLIENT RIÊNG

Phân loại: A giữ nguyên · B chỉnh sửa/mở rộng · C viết lại một phần · D thay hoàn toàn · E chưa đủ bằng chứng.

| Thành phần | Bằng chứng | Loại | Ghi chú |
|---|---|---|---|
| Cocos2d-x 3.17.2 (đi kèm, **đã sửa**) | `CLIENT\cocos2d\CHANGELOG`; `addImageWihtData` | B | Bản sửa khiến nâng cấp engine không còn là thay thư mục. Số chỗ sửa khác: UNKNOWN |
| Hệ build Android (Gradle + CMake 3.30.5, NDK 25.2) | `proj.android\gradle.properties` `PROP_BUILD_TYPE=cmake`; `app\build.gradle:39–48` | A/B | Dự án đã build APK nhiều lần (báo cáo dự án 13, 18, 33…) |
| Đọc PAK, hash, giải nén (`engine\XPackFile`, `KPakList`, `ucl`) | báo cáo #8 | B | Cần vá: giải nén không giới hạn đầu ra, không kiểm CRC |
| Giải mã SPR → texture (`engine\Kgetinidata.cpp`, `ImageStore`) | mục 3.4 | C | Mỗi khung một texture, giải trên luồng chính; nên có atlas/cache và nạp nền |
| Hệ animation (`KSprControl`, `KNpcRes`, `KMissleRes`, `KSkillSpecial`) | mục 3 | C | Gắn cứng nhịp 18 Hz; cần lớp chọn khung theo thời gian |
| Dựng cảnh và vẽ thế giới (`gamescene\KScenePlaceC`, `CoreDrawGameObj`) | báo cáo #7; báo cáo dự án 47 | C | Cây đối tượng riêng, từng gây nhấp nháy khi đổi vùng |
| Lõi gameplay client (`gamecore`: `KNpc` 11.385 dòng, `KPlayer`, `KSkills`, `KItem`…) | báo cáo #7 | B | Là bản sao rút gọn của logic server; đổi gameplay phải đổi **cả hai phía** và bảng dữ liệu |
| UI (`gameui` 174 file + `vn` 131 file) | báo cáo #2 | C/D | Hai bộ song song; `KgameWorld.cpp` 15.397 dòng |
| Mạng (`network\SocketClient`, `KSG_EncodeDecode`) | báo cáo #9 | B | XOR cuốn, không bảo mật |
| Giao thức (`gamecore\KProtocol.h`, `KProtocolDef.h`) | mục 10.2 | B | Phải giữ đồng bộ tay với server |
| Đăng nhập, chọn server, chọn nhân vật (`gameui\Klogin*`, `KuiSelserver`, `KSelPlayer`) | CLAUDE.md; báo cáo dự án 16 | B | Phụ thuộc chuỗi Bishop → Goddess → gs |
| Tải và cập nhật PAK (`KDownLoadFile`, `KUpdateLayer*`, `package.ini`, `paklist.ini`) | báo cáo #8 | B | Địa chỉ CDN nằm trong `package.ini` (đã đổi được, báo cáo dự án 18) |
| Bản iOS/macOS (`proj.ios_mac`) | kiểm kê | E | Chưa từng build |

Trả lời:
1. **Phát triển client riêng trên source này: được** (VERIFIED có đủ mã và đường build Android).
2. **Thay đổi sâu giao diện, đồ họa, animation, hiệu ứng: được**, mức công lớn dần theo thứ tự UI rời (dễ) → chọn khung (vừa) → asset SPR mới (cần công cụ) → vượt 256 màu/atlas (sửa loader). **Gameplay**: được nhưng phải sửa đồng thời server và dữ liệu.
3. **Bỏ phụ thuộc server gốc:** không tìm thấy khóa cứng tới một máy chủ cụ thể; địa chỉ đến từ `package.ini` và danh sách server. Có cơ chế kiểm tra phiên bản/bảo vệ (`FsjxClient.ini`, `Xfsverjx.ini`, `simply_crypt` trong công cụ dự án) — bản chất đầy đủ UNKNOWN trong phiên này.
4. **Kết nối tới server mới: được**, với điều kiện server nói đúng giao thức (mục 10).
5. **Điểm khóa vào kiến trúc hiện tại:** nhịp 18 Hz xuyên suốt dữ liệu (khung đánh, thời gian kỹ năng, script); định dạng SPR 256 màu; tên file hash hóa và mã hóa GBK; logic gameplay nhân đôi client/server; struct gói tin `pack(1)` chia sẻ bằng tay; engine Cocos đã sửa.
6. **Chi phí và rủi ro kế thừa:** tệp khổng lồ khó kiểm thử; mã hóa nguồn lẫn lộn (GBK/UTF-8/hỏng); cờ biên dịch mạo hiểm (`-ffast-math -fstrict-aliasing`, `CLIENT\CMakeLists.txt:814–815`); thư viện bên thứ ba cũ, phiên bản UNKNOWN.

---

## 10. KHẢ NĂNG PHÁT TRIỂN SERVER RIÊNG

### 10.1 Giao thức và luồng (từ mã và tài liệu dự án)
- **Đóng gói:** gói nhị phân, 1 byte kiểu (`PROTOCOL_MSG_TYPE BYTE`, tối đa 249), struct `#pragma pack(1)` (`CLIENT\Classes\gamecore\KProtocol.h`). VERIFIED.
- **Mã hóa:** XOR theo khối 4 byte với khóa 32 bit, khóa mới = `khóa*31 + 134775813` (`CLIENT\Classes\network\KSG_EncodeDecode.cpp`). Chỉ là làm rối. VERIFIED. Thủ tục trao khóa ban đầu: UNKNOWN trong phiên này (báo cáo dự án 16 nói luồng đăng nhập có đủ trong mã client).
- **Luồng:** client → Bishop (đăng nhập, chọn server) → Sword3PaySys (tài khoản) / Goddess (nhân vật) → gs001 (vào bản đồ, đồng bộ) ; S3Relay (bang, bạn). Nguồn: `SRV\gateway\Sources\MultiServer\{Bishop,Goddess,S3Relay}`, `Sword3PaySys\S3AccServer`; CLAUDE.md. PROBABLE (không truy từng gói trong phiên này).
- **Vòng lặp server:** `SRV\gameserver\Sources\MultiServer\GameServer\KSOServer.cpp:90` `GAME_FPS 18`; `:1442` bước khung; xử lý gói ngay khi tới, thực thi ở nhịp kế (báo cáo dự án 33).
- **Server quyết định:** vị trí chuẩn, sát thương, trạng thái, vật phẩm, AI quái. **Client tự mô phỏng:** hoạt ảnh, đạn và hiệu ứng trúng đòn cục bộ (`KMissle::ProcessCollision` → `CreateSpecialEffect`), nên hình ảnh có thể hiện "trúng" khi server không tính (báo cáo dự án 32, 33). PROBABLE (trích từ báo cáo dự án, có số dòng; không kiểm lại).

### 10.2 Phụ thuộc giao thức đã kiểm chứng
- **ID gói:** `s2c_PROTOCOL`, `c2c`, `gm`, `playercomm` giống hệt; `c2s_PROTOCOL` cùng ID, khác một tên (`c2s_login` ↔ `c2s_login_fhgyrinhkmvnsheypo`). Script `scripts\protocol_enum_compare.py`. VERIFIED.
- **Struct payload (mới):** `scripts\protocol_struct_compare.py` so danh sách trường của 328 struct chung giữa `CLIENT\Classes\gamecore\KProtocol.h` và `SRV\gameserver\Headers\KProtocol.h`: **310 giống, 18 khác**. Các khác biệt làm đổi kích thước gói:
  - `NPC_NORMAL_SYNC`: `int nCurrentLifeMax` (client) ↔ `__int64` (server).
  - `CURPLAYER_NORMAL_SYNC`: `int m_shLife/m_shStamina/m_shMana` ↔ `__int64`.
  - `PLAYER_LEVEL_UP_SYNC`: `UINT` ↔ `__int64` (3 trường).
  - `REBORN_VALUE_SYNC`, `ROLEVIP_VALUE_SYNC`: `int` ↔ `__int64`.
  - `DATAU_BOX` (client thừa 2 trường), `LADDER_LIST`, `tagRoleEnterGame`, `tagGameSvrInfo`, `tagRequestSvrIp`, `tagGuidableInfo`, `tagMsgInGame`, `STONG_SERVER_TO_CORE_APPLY_CREATE` (server thừa trường).
  - Chỉ khác tên trường (không đổi bố cục): `NPC_SET_TMPCAMP`, `TONG_SEARCH_RESULT_SYNC`, `PLAYER_REQUEST_CP_LOCK`.
  - Server có thêm 7 struct, client có thêm `GUID`.
  Mức: VERIFIED ở mức văn bản; kích thước nhị phân không tính trong phiên này. Khớp với báo cáo dự án 45: "7 struct gói client về bố cục client 2912 … int64 vs int … HUD 0/0" đã phải sửa trên bản copy để server tự dựng chạy được.
- **Hệ quả:** source server trong repo **không phải** bản đã sinh ra exe đang chạy với client này, hoặc client đã bị chỉnh sau đó. Dựng server từ repo mà không vá sẽ sai dữ liệu hiển thị.
- **Dữ liệu:** client và server có **bản bảng khác nhau** (`Missles.txt`, `Skills.txt`, `Npcs.txt`, mục 2.1). Mức ảnh hưởng: UNKNOWN (chưa diff nội dung).

### 10.3 Đánh giá các hướng
| Hướng | Đánh giá | Mức |
|---|---|---|
| Vận hành server gốc (exe có sẵn) | Đang chạy trong VM | VERIFIED bởi dự án (ngoài phiên này) |
| **Dựng server từ source rồi vá cho khớp client** | Đã làm trong VM thử: `gs001.exe`, `CoreServer.dll`, `Engine.dll`, `LuaLibDll.dll` (MSVC v143), vào game, đánh quái, lên cấp sau khi vá 7 struct | VERIFIED bởi dự án (báo cáo 35, 45); **chưa dựng Bishop/Goddess/S3Relay/PaySys từ source** — UNKNOWN |
| Viết server mới tương thích client | Phải tái tạo ≈425.000 dòng logic `Core` + 329 struct + hàng nghìn script Lua + bảng dữ liệu | Khả thi về nguyên tắc, khối lượng rất lớn. NOT TESTED |
| Sửa client để hợp server mới / giao thức riêng | Được (có cả hai đầu mã), nhưng logic gameplay client phải theo | PROBABLE |
| Database và lưu trữ riêng | Goddess có đường MySQL (`mysql_db.cpp:51`), PaySys dùng MSSQL; động cơ đang dùng ở triển khai thật UNKNOWN từ source | PROBABLE |
| BOT phía server | Kịch bản Lua và NPC phe có sẵn; bot "client không giao diện" cũng khả thi (báo cáo dự án 16) | PROBABLE (khảo sát, chưa làm) |
| Tách logic khỏi phụ thuộc server cũ | Phụ thuộc Windows (IOCP, COM-kiểu `IServer`, MSSQL/ADO), VS2010 gốc ↔ v143 | Khó; UNKNOWN chi tiết |

**Không thể triển khai server riêng chỉ bằng đổi IP/cổng.** Tối thiểu phải: khớp 18 struct, khớp bảng dữ liệu, có đủ chuỗi dịch vụ đăng nhập, và danh sách server/địa chỉ trong `gs00N_cfg.ini` + `package.ini`.

---

## 11. BẢN ĐỒ PHỤ THUỘC SOURCE CŨ

| Phụ thuộc | Nằm ở đâu | Thoát được không | Cách thoát |
|---|---|---|---|
| Nhịp 18 Hz | Mã client + server, bảng dữ liệu (khung đánh, `LifeTime`, khoảng), Lua | Khó | Giữ 18 Hz cho logic, tách hiển thị theo thời gian vẽ (hướng dự án đang đi) |
| Định dạng PAK + hash tên | `engine\XPackFile`, `KPakList`, `KFilePath` | Dễ giữ, dễ thay | Đã hiểu đầy đủ; có thể thêm định dạng mới song song |
| Định dạng SPR 256 màu | `Kgetinidata`, `KImageStore2`, mọi asset | Trung bình | Bộ mã hóa riêng; về sau thêm loader ảnh màu thật nhiều khung |
| Tên file GBK | Bảng dữ liệu, literal trong mã, hash | Trung bình | Giữ nguyên; công cụ phải xử lý byte thô |
| Giao thức `pack(1)` chia sẻ tay | `KProtocol.h` × 3 bản | Trung bình | Một nguồn định nghĩa chung + kiểm tra kích thước tự động |
| Logic gameplay nhân đôi | `CLIENT\Classes\gamecore` ↔ `SRV\...\Core\Src` | Khó | Giữ; mọi đổi gameplay làm hai phía |
| Chuỗi dịch vụ Windows (Bishop, Goddess, S3Relay, PaySys, MSSQL) | `SRV\gateway` | Khó | Giữ trong VM; thay dần từng dịch vụ |
| Cocos2d-x 3.17.2 đã sửa | `CLIENT\cocos2d` | Trung bình | Liệt kê các chỗ sửa trước khi nghĩ tới nâng cấp |
| Công cụ gốc (`JxStudio`, `str_tool`) | `RUNTIME` | **Đã thoát** | Không cần cho PAK/SPR; nội dung khác UNKNOWN |
| Quyền sử dụng mã/asset | Ghi chú "Copyright : Kingsoft 2003" trong `engine\XPackFile.h`; không thấy tệp giấy phép cho mã game | UNKNOWN | Cần tài liệu pháp lý; ngoài phạm vi kỹ thuật |

---

## 12. SO SÁNH BỐN PHƯƠNG ÁN

Thang: Thấp / Trung bình / Cao / Rất cao. Đây là đánh giá định tính, không có ước lượng ngày công được kiểm chứng.

| Tiêu chí | PA1 Kế thừa nguyên trạng | PA2 Kế thừa có chọn lọc | PA3 Client mới trên Cocos | PA4 Kiến trúc độc lập |
|---|---|---|---|---|
| Khả thi kỹ thuật | Cao (đang chạy) | Cao | Trung bình | Trung bình-thấp |
| Khối lượng | Thấp | Trung bình | Cao | Rất cao |
| Độ khó | Thấp-TB | Trung bình | Cao | Rất cao |
| Rủi ro | Tích lũy nợ kỹ thuật; giới hạn 18 Hz/256 màu còn nguyên | Hồi quy khi thay từng lớp; cần kiểm thử tự động | Phải tái tạo toàn bộ hành vi client khớp server | Tái tạo cả server; lệch gameplay |
| Phụ thuộc source cũ | Rất cao | Cao → giảm dần | Trung bình (vẫn giao thức, dữ liệu, server) | Thấp (chỉ dữ liệu/kiến thức) |
| Nâng cấp đồ họa | Thấp | **Cao** (thay lớp animation + pipeline asset) | Cao | Cao |
| Mở rộng gameplay | Trung bình (sửa hai phía) | Trung bình-cao | Trung bình | Cao |
| Vận hành server riêng | Có (exe gốc/tự dựng) | Có | Có (server cũ) | Phải viết mới |
| Phát triển lâu dài | Thấp | **Trung bình-cao** | Cao nếu hoàn tất | Cao nếu hoàn tất |
| Thời điểm có kết quả nhìn thấy | Ngay | Sớm, theo từng lớp | Muộn | Rất muộn |

**Lựa chọn nền tảng tốt, ít nợ nhất trong khả năng thực tế: PA2.** Lý do: ba lớp gây giới hạn (chọn khung, giải mã/nạp ảnh, pipeline asset) đều **tách được** khỏi phần còn lại và có đường sửa cụ thể đã chỉ ra; trong khi PA3/PA4 buộc tái tạo hành vi của ≈425.000 dòng logic mà chưa có bộ kiểm thử nào để biết khi nào "đúng". PA2 cũng không đóng cửa PA3: các lớp viết lại trong PA2 (animation, asset, giao thức một nguồn) chính là nền của một client mới.

Về pháp lý: quyền truy cập kỹ thuật (có source, giải mã được định dạng) **không đồng nghĩa** quyền sử dụng, sửa đổi, phân phối. Không có tài liệu sở hữu/giấy phép nào trong workspace mà tôi đã thấy. Tôi không kết luận pháp lý; mọi phương án có phát hành công khai đều cần làm rõ điểm này trước.

---

## 13. NHỮNG VẤN ĐỀ CHƯA ĐƯỢC XÁC MINH

| # | Câu hỏi | Bằng chứng hiện có | Còn thiếu | Cách kiểm | Rủi ro | Cần sửa source? |
|---|---|---|---|---|---|---|
| 1 | Số khung thực sự hiện trên màn hình có đúng mô hình mục 4.2? | Công thức mã + số liệu bảng/SPR | Đo trên thiết bị | Quay 60 hình/giây một kỹ năng, đếm hình khác nhau; hoặc log chỉ số khung | Thấp | Không (quay phim); có nếu thêm log |
| 2 | Game có nạp được SPR đã thay? | Thay mục INI đã chạy | Bộ mã hóa SPR; một lần thử | Vòng khép kín giải↔mã hóa, rồi thay trong bản copy PAK qua CDN thử | Trung bình | Không |
| 3 | SPR nén từng khung: định dạng `XPackSprFrameInfo` có đúng như đọc? | Mã `GetSprFrame` | Giải thử một file | Mở rộng công cụ giải, so kích thước khung | Thấp | Không |
| 4 | Thủ tục trao khóa và bắt tay mạng | `KSG_EncodeDecode`; báo cáo dự án 16 | Truy `ClientStage.cpp`, `Bishop\SmartClient.cpp` | Đọc mã | Thấp | Không |
| 5 | Kích thước nhị phân của 18 struct khác nhau | So văn bản; báo cáo dự án 45 nói đã đo 351 struct bằng probe | Bảng kích thước/offset lặp lại được | Biên dịch tệp `static_assert` cô lập | Thấp | Không (tệp riêng) |
| 6 | Bảng dữ liệu client ↔ server khác nhau ở đâu | Băm khác, kích thước khác | Diff theo dòng | Diff trong bộ nhớ, báo cột/dòng lệch | Thấp | Không |
| 7 | Định dạng bản đồ (`.map`, `.wor`) | Đếm mục | Đọc `KSubWorld::LoadMapS`, `KRegion` | Đọc mã + header | Thấp | Không |
| 8 | Âm thanh: định dạng trong `sound.pak`, phiên bản FMOD | Đếm mục | Chữ ký file | Đọc header trong bộ nhớ | Thấp | Không |
| 9 | Cocos đã bị sửa những gì | `addImageWihtData` | Danh sách đầy đủ | Diff với Cocos2d-x 3.17.2 gốc (cần bản gốc tham chiếu) | Thấp | Không |
| 10 | Bishop/Goddess/S3Relay/PaySys có dựng được từ source và khớp exe? | Chỉ `gs001` đã dựng | Dựng thử | Build trên bản copy, trong VM thử | Trung bình | Bản copy (cần duyệt) |
| 11 | Cơ chế kiểm phiên bản/bảo vệ client (`Xfsverjx.ini`, `FsjxClient.ini`) | Tên file, công cụ `xfsverjx_compare.py`, `simply_crypt.py` | Vai trò chính xác | Đọc mã nạp | Thấp | Không |
| 12 | Bộ nhớ texture và thời gian giải mã khi tăng khung | Báo cáo dự án 46 (giải mã gây khung chậm) | Đo có hệ thống | Đo trên LDPlayer và máy yếu | Trung bình | Có thể cần log |
| 13 | Quyền sử dụng mã và asset | Ghi chú bản quyền Kingsoft | Tài liệu pháp lý | Ngoài kỹ thuật | **Cao** | — |
| 14 | 6 literal SPR kỹ năng không tìm thấy bằng hash | Kết quả script | Tên/mã hóa đúng | Thử biến thể mã hóa | Thấp | Không |

---

## 14. CÁC THỬ NGHIỆM TIẾP THEO (ĐỀ XUẤT, CHƯA THỰC HIỆN)

Ưu tiên chỉ-đọc trước.
1. **(Chỉ đọc)** Đo số khung thật trên LDPlayer cho 3 kỹ năng mẫu: một đạn bay thiếu khung (ví dụ đạn 179), một hiệu ứng va chạm bị cắt (377), một đòn đánh thường ở hai mức tốc độ đánh.
2. **(Chỉ đọc)** Diff bảng dữ liệu client ↔ server; bảng kích thước 18 struct.
3. **(Chỉ đọc)** Đọc mã bản đồ, âm thanh, bắt tay mạng, kiểm phiên bản.
4. **(Ghi ra thư mục riêng)** Bộ giải/mã hóa SPR độc lập + kiểm vòng khép kín trên bản copy.
5. **(Cần duyệt, bản copy + CDN thử)** Thay một SPR hiệu ứng, xác nhận game hiển thị.
6. **(Cần duyệt, bản build riêng)** Chọn khung theo thời gian vẽ cho đạn bay; đo lại bước 1 và FPS.
7. **(Cần duyệt)** Một kỹ năng mẫu với số khung gấp đôi; đo RAM/texture/thời gian giải mã.

---

## 15. ĐÁNH GIÁ CUỐI CÙNG VÀ KHUYẾN NGHỊ ĐẦU TƯ

### Bảng tổng hợp
| Hạng mục | Kết luận | Bằng chứng | Độ tin cậy | Mức độ khó | Rủi ro |
|---|---|---|---|---|---|
| Tăng frame animation | Được, nhưng phải **tạo khung mới**; asset hiện chỉ có trung vị 10–11 khung/hướng (hiệu ứng), 11–18 (động tác) | Header 280 SPR hiệu ứng + 2.199 SPR nhân vật/NPC (`data\*.csv`) | VERIFIED số liệu; quy trình NOT TESTED | Cao (sản xuất nội dung) | Bộ nhớ texture, dung lượng tải |
| Mở tối đa frame skill | Được một phần: 28 ô sửa bằng cấu hình; 84 đạn bay và đòn đánh nhanh cần sửa chọn khung phía client. Tổng lợi ích nhỏ: đạn bay đang phát 85%, va chạm 96%, tan biến 100% | `KMissleRes.cpp:180–199`, `KNpcRes.cpp:254–289`, `KMissle.cpp:1924` | VERIFIED mã; mô hình PROBABLE; NOT TESTED | Trung bình | Hồi quy hiển thị |
| Tạo frame mới | Định dạng cho phép; thiếu bộ mã hóa SPR; chưa thử | `KbugInfo.h:238–269`; `Kgetinidata.cpp:236–366` | PROBABLE | Trung bình (công cụ) + Cao (nội dung) | 256 màu, công sức theo từng file |
| Can thiệp asset | Đọc/trích: có. Sửa dữ liệu văn bản: có. Sửa ảnh: chưa có công cụ | `DOCS\tools\pak_extract.py`, `pak_replace.py`, `pak_verify.py` | VERIFIED (văn bản); NOT TESTED (ảnh) | Trung bình | Thấp |
| Thay thế asset | Mục văn bản trong PAK: đã chạy trong game (theo dự án). Ảnh SPR: chưa | Báo cáo dự án 08; CLAUDE.md | VERIFIED bởi dự án (văn bản); NOT TESTED (ảnh) | Trung bình | Trung bình |
| Client riêng | Khả thi trên source này; cần tái cấu trúc 3 lớp (animation, nạp ảnh, UI) | Mục 9 | VERIFIED có mã và đường build; khối lượng PROBABLE | Trung bình-cao | Nợ kỹ thuật, engine đã sửa |
| Server riêng | Khả thi bằng dựng từ source + vá; **không** chỉ đổi IP; viết mới thì rất lớn | 18 struct khác (`scripts\protocol_struct_compare.py`); báo cáo dự án 35, 45 | VERIFIED (khác biệt struct); VERIFIED bởi dự án (gs001 tự dựng); UNKNOWN (các dịch vụ gateway) | Cao | Source ≠ exe; phụ thuộc Windows |
| Giảm phụ thuộc source cũ | Làm dần được theo lớp; không thoát hẳn nhịp 18 Hz, dữ liệu và giao thức nếu giữ server | Mục 11 | PROBABLE | Cao | Lệch client/server |
| Phát triển lâu dài | Được nếu tái cấu trúc có kiểm thử; không nên tiếp tục vá trên tệp 15 nghìn dòng | Mục 9, 12 | PROBABLE | Cao | Pháp lý chưa rõ là rủi ro lớn nhất |

### Trả lời tám câu hỏi bắt buộc
1. **Có đáng tiếp tục đầu tư?** Có, về mặt kỹ thuật: mã đầy đủ hai phía, build được, định dạng đã hiểu, không có "hộp đen" chặn đường. Điều kiện: chấp nhận tái cấu trúc và làm rõ quyền sử dụng.
2. **Có thể làm chiêu thức mượt, đủ khung hơn?** Có, theo hai nấc. Nấc 1 (sửa mã client và cấu hình): phát đủ khung đang có — lợi ích có thật nhưng nhỏ. Nấc 2 (tạo khung mới + chọn khung theo thời gian vẽ): mới là thứ tạo khác biệt rõ, và tốn công sản xuất nội dung.
3. **Có cơ chế nào đang hạn chế hay bỏ bớt khung skill?** Không có cơ chế cố ý. Có giới hạn kiến trúc: 1 khung/nhịp 18 Hz, chọn khung theo tiến độ/tuổi thọ, cắt theo thời gian sống, cắt ngoài màn hình, và hai tùy chọn ẩn do người chơi bật.
4. **Có thể làm chủ asset và tự sản xuất nội dung?** Dữ liệu văn bản: đã làm chủ. Hình ảnh: hiểu định dạng, đọc được, **chưa** chứng minh được vòng sửa → đóng gói → game hiển thị. Cần bộ mã hóa SPR và một lần thử.
5. **Có thể xây client riêng và server riêng?** Client: có. Server: có nếu dựng từ source và vá cho khớp; viết mới hoàn toàn là dự án rất lớn.
6. **Phụ thuộc source cũ ở đâu?** Nhịp 18 Hz, định dạng SPR/PAK và tên GBK, giao thức `pack(1)`, logic gameplay nhân đôi, chuỗi dịch vụ Windows, engine Cocos đã sửa (mục 11).
7. **Kiến trúc tốt nhất nếu tiếp tục?** Phương án 2: giữ lõi gameplay, giao thức và server; viết lại lớp animation (theo thời gian vẽ), lớp nạp ảnh (cache/atlas, nạp nền, về sau ảnh màu thật) và pipeline asset riêng; hợp nhất định nghĩa giao thức về một nguồn có kiểm tra tự động.
8. **Có vấn đề nghiêm trọng buộc dừng hoặc chuyển hướng?** Không có trở ngại kỹ thuật ở mức đó. Ba điểm phải biết trước khi rót thêm công: (a) quyền sử dụng mã và asset chưa có tài liệu — tôi không đánh giá được, và nó có thể quyết định tất cả; (b) source server trong repo không khớp client nếu không vá; (c) mọi kết luận về hiển thị trong báo cáo này dựa trên mã và dữ liệu, chưa đo trên thiết bị.

### Khuyến nghị
**CONTINUE WITH RESTRUCTURING.**
Tiếp tục, nhưng không theo kiểu vá thêm vào mã hiện tại. Trước khi đầu tư sản xuất nội dung, nên qua ba cổng kiểm chứng rẻ: đo số khung thật trên thiết bị (mục 14.1), thay được một ảnh SPR trong game (14.4–14.5), và làm rõ quyền sử dụng. Nếu cổng thứ hai thất bại hoặc cổng thứ ba không rõ ràng, cần đánh giá lại trước khi đi tiếp.

---

### Phụ lục — Sản phẩm của phiên thẩm định
- Báo cáo: `C:\Jx1CocoV3_RESEARCH\JX1_FULL_TECHNICAL_FEASIBILITY_AUDIT.md`.
- Script chỉ-đọc mới: `C:\Jx1CocoV3_RESEARCH\scripts\audit_missile_frames.py`, `audit_character_frames.py`, `audit_summary_stats.py`, `protocol_struct_compare.py`.
- Dữ liệu mới: `C:\Jx1CocoV3_RESEARCH\data\missile_frame_audit.csv` (727 dòng), `character_frame_audit.csv` (2.203 dòng).
- Không có thay đổi nào trong `C:\Jx1CocoV3`, 11 báo cáo gốc, VM hay server. Chưa commit, chưa push.
