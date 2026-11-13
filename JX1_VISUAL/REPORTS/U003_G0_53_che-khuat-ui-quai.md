# 53 – U003 G0 bổ sung lần cuối: che khuất, UI skill/auto/cooldown, chọn quái

Phạm vi: CHỈ ĐỌC mã nguồn client. Không tạo Unity project/APK, không sửa source/PAK/server/VM, không chạy/dừng EXE, không push.
Nhãn: CONFIRMED (đọc code) / TESTED (có chạy/đo) / HYPOTHESIS / UNKNOWN. Đường dẫn tính từ `Client2912/Client/Classes/`.

## TÓM TẮT 5 DÒNG
1. Che khuất = painter order theo cây BSP 2D (`KIpoTree`/`KIpotBranch`): Tree/Line/Point sắp xếp bằng quan hệ điểm–đường; nhân vật là "lá runtime" chèn lại cây mỗi khi đổi toạ độ. Không dùng z-buffer.
2. "Above" KHÔNG nằm trong cây: vẽ riêng sau lớp OBJECT, trước lớp INFRONTOF_ALL; có công tắc `nIsHideTreeAndBuilding`.
3. UI cooldown gốc CÓ (sửa nhận định cũ): lớp đen `timeLoopLayer` co `scaleY` theo `_nextUseTime`, `KgameWorld.cpp:5527-5540`; nút auto gốc là `autoCallback_`/`KuiAutoPlay`.
4. AttackSpeed trong NpcS = số khung game (`m_AttackFrame`, `KNpcTemplate.cpp:50`); ani001 đồng nhất (18) nên khuyến nghị ani001, còn rủi ro chưa kiểm tra.
5. `FillLineObstacle` là che SÁNG (lighting), không phải vật cản đi lại; vật cản đi lại nằm ở `obstacle` của Region_C.dat.

Cần tôi quyết định: có (chọn quái ani001/enemy003; có cho phép dùng thuật toán cây thật hay bản đơn giản hoá cho Unity — xem mục 6).

## A. Thuật toán che khuất

### A1. Cấu trúc [CONFIRMED]
- `KIpoTree` có `m_pMainBranch`, `m_DefaultBranch`, `m_PermanentLeaf` (`gamescene/KIpoTree.cpp:56-87,169-175`). `AddBranch` tạo main branch từ vật thể Tree đầu tiên (`:187-199`).
- `KIpotBranch`: nhánh = 1 đường thẳng (`m_oHeadPoint`→`m_oEndPoint`), 2 phía: phía 0 = RELATION_UP (trên đường, tức xa người xem), phía 1 = còn lại. Mỗi phía là nhánh con hoặc danh sách lá (`m_pSubBranch[i]`/`m_pLeafs[i]`, `IS_BRANCH(i)`) (`KIpotBranch.cpp:235-292,381-420`).
- Lá có 2 loại: `IPOTL_T_BUILDIN_OBJ` (vật thể nền từ Region_C.dat) và `IPOTL_T_RUNTIME_OBJ` (NPC/missile/obj động) (`KIpotLeaf.h`, `AddPointLeafToList :430`).

### A2. Thứ tự vẽ [CONFIRMED]
- `KIpotBranch::PaintObjectLayer` (`KIpotBranch.cpp:67-88`): vẽ phía 0 → các vật thể nằm TRÊN chính đường nhánh (`PaintABranchObject :90-173`, cắt ảnh theo đoạn x nếu `bImgPart`) → phía 1. Tức xa trước, gần sau (painter's algorithm).
- Trong danh sách lá của một phía, sắp tăng dần theo `oPosition.y` (`AddPointLeafToList :513-530`, `AddLineLeafToList :631-642`), y nhỏ vẽ trước.
- Thứ tự lớp toàn cảnh (`KScenePlaceC.cpp:1621-1645`): nền đất (`PaintGround_old`) → `Paint(COVER_GROUND)` → `Paint(OBJECT)` → "Above" (nếu `!nIsHideTreeAndBuilding`) → `Paint(INFRONTOF_ALL)`.
- Cờ lớp của runtime obj (`SceneDataDef.h:55-58`): COVER_GROUND 0x01, OBJECT 0x02, INFRONTOF_ALL 0x04 (vẽ trên cùng: tên, thanh máu...), LIGHT_PROP 0x08. NPC đăng ký `OBJECT|INFRONTOF_ALL|LIGHT_PROP` (`gamecore/KNpcRes.cpp:215`); missile `OBJECT[|LIGHT_PROP]` (`gamecore/KMissle.cpp:514,520`).

### A3. Vai trò Tree / Line / Point / Above
- Kiểu sắp xếp là 2 bit của `Props`: POINT 0x000, LINE 0x100, TREE 0x200 (`SceneDataDef.h:244-253`) [CONFIRMED].
- **Tree**: gom theo cùng đường thẳng (`SM_IsLineLinkable(fAngleXY,fNodicalY)`), mỗi nhóm sắp theo x, nhóm dài nhất (`nLength2` lớn) thêm vào cây trước → thành nhánh cấp cao; `AddBranch` (`KScenePlaceC.cpp:1905-2004`). Vật thể cắt ngang nhánh được `Clone` tại giao điểm thành 2 nửa (`KIpotBranch.cpp:235-292`, `KIpotLeaf.cpp:277`).
- **Line**: sắp theo độ dài giảm dần, rồi `AddLeafLine` (`KScenePlaceC.cpp:2007-2054`): đi xuống cây theo vị trí đầu/cuối so với từng nhánh, vào danh sách lá (`AddLineLeafToList`). Hộp so sánh mở rộng 7 px (`fsize 7`, `KIpotBranch.cpp:580`).
- **Point**: `AddLeafPoint` từng điểm (`KScenePlaceC.cpp:2056-2063`); khi đã có Line trong cùng danh sách thì kiểm tra điểm có nằm trong hộp của Line (mở rộng ngang 13, lên 3, xuống 128 px; `KIpotBranch.cpp:458-460`) → nếu có, đặt làm con trái/phải (`pLChild/pRChild`) của Line đó: điểm "UP/ON" vẽ trước Line, "DOWN" vẽ sau.
- **Above**: mảng `m_pObjsAbove` vẽ bằng `PaintAboveHeadObj_old` riêng, không qua cây (`KScenePlaceC.cpp:1637-1643`); ẩn được bằng `nIsHideTreeAndBuilding` (`gamecore/KCore.cpp:90`, bật ở `gameui/KuiOptions.cpp:281,493`).

### A4. Cập nhật khi di chuyển [CONFIRMED]
- `MoveObject` (`KScenePlaceC.cpp:1444-1516`): nếu đổi toạ độ → `PluckRto` (gỡ khỏi danh sách) → đặt `oPosition = (x, y + POINT_LEAF_Y_ADJUST_VALUE)` (=6, `KIpotLeaf.h:20`) → `AddLeafPoint` lại. Tức mỗi lần đổi toạ độ là một lần chèn lại từ gốc cây; không đổi toạ độ thì không làm gì.
- Ra ngoài vùng xử lý → `PluckRto` và `free`. Có khoá `m_ProcessCritical`.
- Mỗi lần đổi vùng nạp: dựng lại cây, rồi `StrewRtoLeafs(KeepArea)` chèn lại các lá runtime còn giữ (`KIpoTree.cpp:428-470`, `KScenePlaceC.cpp:2079-2084`). Lưu ý: điều kiện giữ dùng `||` thay vì `&&` (`KIpoTree.cpp:443-446`) → hầu như luôn giữ; [CONFIRMED đọc code, hệ quả chưa kiểm tra].
- Điểm tham chiếu để so sánh là chân nhân vật (y + 6), không phải tâm sprite. Phụ thuộc: toạ độ thế giới (x,y), loại sắp xếp của vật thể, vùng 512×1024. KHÔNG phụ thuộc hướng nhân vật; `nPositionZ` được lưu nhưng chưa thấy dùng để sắp (chưa kiểm tra mọi nơi).

### A5. `FillLineObstacle`/`ObjectsCallback`/`RenderLightMap`
- Chỉ phục vụ ánh sáng động (`m_bDynamicLighting`, `SPBIO_P_BLOCK_LIGHT_*`): đánh dấu lưới `pObstacle[]` để chặn tia sáng (`KIpoTree.cpp:473-560`). [CONFIRMED] KHÔNG phải vật cản đi lại và KHÔNG ảnh hưởng thứ tự vẽ. Vật cản đi lại: lớp `obstacle` (512×4 byte/vùng) trong Region_C.dat (báo cáo 52).

### A6. Giới hạn / trường hợp đặc biệt
- Cắt tại giao điểm (`Clone`) làm tăng số vật thể; ảnh bị cắt bằng `bImgPart` (cần 4 điểm ImgPos).
- Thứ tự ổn định chỉ khi sắp xếp ban đầu đúng: tree sắp theo độ dài giảm dần (`:1980-1991`). UNKNOWN: hành vi khi hai nhánh cắt chéo nhiều lần.
- UNKNOWN: các nhánh `PaintABranchObject` với nhiều `bImgPart` cạnh nhau; chưa chạy thử vẽ.

## B. UI skill / auto / cooldown

| Thành phần | Trạng thái | Bằng chứng |
|---|---|---|
| Nút đánh chính | UI gốc đã tìm | `gamescene/KgameWorld.cpp:680` (`mianSkillCallback`), `:2982` |
| Nút kỹ năng phụ (icon + vòng tròn che) | UI gốc đã tìm | struct `auxiliarySkillData` `KgameWorld.h:65-78`; tạo `KgameWorld.cpp:12758-12960`; `mainskillmix.png` mặt nạ tròn (`:12758`) |
| Icon skill 375 | Asset gốc đã tìm | `\spr\Ui\skill\雷动九天.spr` (spr.pak, 36×36, 1 khung) – báo cáo 52 |
| Cooldown trực quan | **UI gốc đã tìm** (sửa báo cáo 50/52) | `timeLoopLayer` = `CCLayerColor(0,0,0,100)` cắt tròn bằng `ClippingNode` (`:12886-12905`); mỗi khung `setScaleY(n*nPer)` với `n=_nextUseTime - SubWorld[0].m_dwCurrentTime`, hết thì scale 0 (`:5527-5540`) |
| Số giây cooldown | Chỉ có khung code | `cdLabel` Arial 20, vàng, viền đen, ở giữa icon, tạo ẩn (`:12931-12937`); chưa thấy chỗ ghi chữ (chưa tìm hết) |
| Nguồn thời gian | CONFIRMED | `KNpc.cpp:2264` gọi `setSkillNextUseTime(_nTime, m_ActiveSkillID)`; `_nTime = m_dwCurrentTime + GetDelayPerCast()` (`:2260`); `nPer = 1/GetDelayPerCast()` (`KgameWorld.cpp:5561`); ngựa dùng `GetHorsePerCast` |
| Nút Auto | UI gốc đã tìm | nút `autoCallback_` (`:1885`, định nghĩa `:4291`); bật/tắt `startOpenAuto` → `KuiAutoPlay::setAutoPlay` (`:2178-2203`); trạng thái `g_pCoreShell->GetAutoplayid()` |
| Nhãn "đang auto" trên đầu | Asset gốc | `\spr\Ui3\剑侠助手\state_autofight.spr` (`:10013`) |
| Auto-mở bảng trợ thủ | Chỉ có trong code | đếm `_openAutoPlyer` khi `m_FightMode` (`:9596-9599`) |
| `ProgressTimer` ở KgameWorldVN | KHÔNG phải cooldown (pin) | `vn/gamescence/KgameWorldVN.cpp:1008-1034` |

Phân loại cho U003: dùng lại ý tưởng gốc (mặt nạ tròn đen, scaleY co dần theo `thời điểm hết/độ dài cooldown`); asset icon dùng lại; số giây, nút Auto 1 chạm, nhãn trạng thái phải tự xây (nhãn spr gốc có thể dùng). Lưu ý: cooldown 375 gốc là `TimePerCast=0` nên gốc KHÔNG hiện vòng che cho skill này (`loopTimel<=0` → ẩn, `:12965`). Cooldown 1 s của U003 là thiết kế riêng [báo cáo 52].

## C. Đối chiếu ani001 / enemy003

- **AttackSpeed** [CONFIRMED nơi dùng]: cột `AttackSpeed` của NpcS → `m_AttackFrame` (`gamecore/KNpcTemplate.cpp:50`, mặc định 20) → `KNpc.cpp:7005`; tổng khung đòn đánh `nTotalFrame = m_AttackFrame * naAttackSpeed/(nbAttackSpeed+m_CurrentAttackSpeed)` (`KNpc.cpp:2381`). Đơn vị = khung game (tên "Frame"; người chơi mặc định 20, `KNpcSet.cpp:104`). Quy ra giây cần tần số logic: server đo 18 Hz ở báo cáo 41 (TESTED trước đó) → 18 khung ≈ 1 s [HYPOTHESIS cho client vì chưa đo lại]. Số khung của sprite (at=12 ở ani001) KHÔNG bằng AttackSpeed: client kéo giãn animation theo `nTotalFrame` (cách nội suy chưa đọc → UNKNOWN).
- ani001: 8 hướng, 320×320, st12/wlk15/bat8/die10/at12, AttackSpeed 18 đồng nhất, 2 hàng NpcS Kind=0 → dữ liệu gọn, ít ngoại lệ. enemy003: 14 hàng (5 Kind=3 đối thoại + 9 Kind=0), AttackSpeed 12/15/18 không đồng nhất, st6/wlk14/bat7/die13/at14, nhẹ hơn (~1188 KB vs ~1895 KB).
- Điểm neo/độ lệch: header SPR có `cx,cy` (báo cáo 52); chưa so sánh độ lệch từng hướng của hai quái → UNKNOWN. Chưa kiểm tra đủ 8 hướng có ảnh thật cho từng trạng thái (chỉ đọc header: khung/hướng).
- **Khuyến nghị: ani001** — lý do: chỉ 2 hàng cùng Kind=0, AttackSpeed thống nhất, đủ 6 sprite st/pst/wlk/bat/die/at. Chưa chắc: dung lượng lớn hơn ~60%; chưa xem hình thực tế có hợp bối cảnh map 45 hay không; chưa xác nhận tên/cấp quái trong spawn gốc. Quyết định cuối thuộc người dùng.

## D. Đề xuất kiến trúc Unity theo nhóm (đề xuất, chưa phải kết luận)
1. Che khuất: không bê nguyên cây BSP. Cách 1 (khuyến nghị cho G1): sort theo "y chân" (y+6) cho NPC/vật thể điểm; vật thể Tree/Line/Point nạp từ JSON đã parse, dùng `sortingOrder` theo y chân và cắt đôi tại giao điểm khi cần (chỉ cho cây/nhà cắt qua nhân vật). Cách 2: port đúng thuật toán nếu thấy lỗi che sai ở map thử. Hỏi lại sau prototype vì A6 còn UNKNOWN.
2. Lớp vẽ: giữ 4 lớp ground / cover-ground / object(sắp theo y) / above / infront (tên, máu); công tắc ẩn Above tuỳ chọn.
3. Vật cản: dùng lưới `obstacle` thật của Region_C.dat; KHÔNG dùng `FillLineObstacle`.
4. UI: cooldown = mặt nạ tròn co theo `endTime`; Auto = nút bật/tắt tự xây; icon 375 từ asset gốc.
5. Quái/tốc độ: dùng ani001; tốc độ đánh lấy từ NpcS chỉ sau khi xác minh Hz client; nếu chưa, đặt tham số trong file cấu hình prototype và ghi rõ là giá trị thử, không phải gốc.

## E. Điểm chưa xác minh (tổng hợp)
- Không chạy client nên chưa có ảnh chụp đối chiếu thứ tự vẽ (TESTED = chưa có).
- Điều kiện `||` ở `StrewRtoLeafs` chưa kiểm tra hệ quả.
- `cdLabel` chưa thấy nơi gán chữ; `KSkillRocker` chưa đọc hết.
- Cách client nội suy animation theo `nTotalFrame`; Hz logic của client.
- Map 45: chưa kiểm tra đủ `Region_C.dat`/số cây; spawn không có trong dữ liệu client.
- Văn bản trong báo cáo 50/52 nói "chưa tìm thấy UI cooldown" nay được thay bằng mục B.
