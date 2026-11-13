# 58 – U003 G0.7: xác minh Hit/action, Attrib 1002 và luồng sát thương, thời điểm cast/missile, MoveKind=Stand, anchor/render, map 45

Nhiệm vụ: `JX1_VISUAL/PROMPTS/U003_G07_58_read-only-verification.md` (kèm chỉ thị 57). Phạm vi READ-ONLY: chỉ đọc source client/server, PAK, bảng dữ liệu; script kiểm tra tạm đặt ở `D:\JX1_U003_work\tools` (`g07_sheet.py`, `g07_anchor.py`, `g07_region.py`, `g06_q*.py`), dữ liệu trích ở `D:\JX1_U003_work\g07_extract*` (ngoài Git). Không tạo Unity project, không code gameplay, không build, không cài gì, không sửa `pak_extract.py`/PAK/source/server/VM/Goddess/EXE, không đụng U001/U002.
Đường dẫn viết tắt: `C/` = `Client2912/Client/Classes/gamecore/` (hoặc `gamescene/` khi ghi rõ); `S/` = `SwordOnline/…/jxOnline/gameserver/Sources/Core/Src/`.
Nhãn: **CONFIRMED** (source/dữ liệu có file:dòng) · **TESTED** (đã chạy/đo/xem ảnh) · **HYPOTHESIS** (có bằng chứng, chưa đủ kết luận) · **UNKNOWN** (chưa xác minh) · **DESIGN** (luật U003, không phải gốc).
Giới hạn chung: nguồn server (`S/`) có thể KHÔNG trùng exe server đang chạy; chưa chạy server/client để đối chiếu hành vi. Không dùng mili giây cho các đại lượng "khung" nếu chưa xác minh.

## 1. TÓM TẮT
1. **A – Hit:** chỉ số action 7 (`cdo_hurt`) = cột `Wound` của `npc动作表.txt` = `ani001_bat.spr` (64 khung, 8 hướng, 8 khung/hướng) – CONFIRMED bằng bảng thật và code; ảnh `bat` đã dựng lại. Skill 375/387 có `DoHurt=0` ⇒ theo nguồn server **không** gọi Hit.
2. **B – SỬA SAI báo cáo 56:** "Attrib 1002" **không phải** định nghĩa sát thương mà là phân loại kỹ năng (`m_nAttrib`, `S/KSkills.cpp:2980`, `KSkills.h:108,250-251`). Sát thương nằm ở `LvlSetting1=lightingdamage_v` của **cả 375 (`leidong_jiutian` 80→260→470) lẫn 387 (`pingdi_hanlei` 25→250)** trong `kunlun.lua`. Theo nguồn server: missile **181 gây sát thương ngay khi va chạm** (3×3 ô, bằng dữ liệu 375) và missile **193 gây thêm một lần** sau khi bắt đầu (dữ liệu 387, rồi biến mất vì `ColVanish`).
3. **C – Thời gian:** `nWaitTime` đầu vào của lần cast người chơi = **0** (tham số mặc định); độ trễ 16 đạn 181 = `2 + 5k + (+rand(5) hoặc −rand(2))` khung logic, k=0..15 (CONFIRMED); khung 60% là điều kiện **bằng** `nTotalFrame*60/100`. Server chạy 18 tick/giây (`GAME_FPS 18`); Hz client vẫn UNKNOWN.
4. **D/E – Stand & anchor:** `MoveKind=Stand` = missile đứng yên tại ô sinh (nhánh `case MISSLE_MMK_Stand: break;`); 193 sinh tại vị trí 181. Anchor ani001 = **(160,192) bị trừ** – đường mã CONFIRMED và hình học TESTED (tâm ngang các khung lệch ≤ ±2 px quanh 0 ở cả 8 hướng).
5. **F – Map 45:** 122/140 `Region_C.dat` có mặt (18 thiếu, ở rìa); toạ độ buildin là **MPS tuyệt đối** (TESTED); map 45 có **0 đối tượng Tree**, 72 Line, 283 Point, 4 Above ⇒ nhánh Tree/Clone của KIpoTree không được bài thử bằng map này.

Cần người dùng quyết định: **có** (mục 7).

---
## 2. Mục A – Hit animation của ani001

### A1. Ánh xạ tên action ↔ mã ↔ sprite [CONFIRMED + TESTED]
- Bảng tên action quái thường: `\settings\npcres\npc动作表.txt` (id PAK `a18b579b`, có trong `updata02/setting/slistcl…`). Dòng tiêu đề `NpcAction`, rồi 14 dòng: `FightStand, NormalStand1, NormalStand2, FightWalk, NormalWalk, FightRun, NormalRun, Wound, Die, Attack1, Attack2, Magic, SitDown, JunpFly` (trích bằng `u003_extract.py`, đọc tay).
- Nạp: `CActionName::Init` (`C/KNpcResNode.cpp:682-709`) – `m_nCurActionNo = height−1`, `GetString(i+2, 1)` ⇒ **chỉ số 0 = FightStand … 7 = Wound, 8 = Die**. Trùng enum `CLIENTACTION` (`C/KNpc.h:104-122`: `cdo_fightstand=0 … cdo_hurt=7, cdo_death=8, cdo_attack=9, cdo_attack1=10, cdo_magic=11, cdo_sit=12, cdo_jump=13`).
- Với quái thường (`NPC_RES_NORMAL`) `GetActNo` trả `nDoing` nguyên (`C/KNpcResNode.cpp:594-596`) ⇒ `m_ClientDoing=cdo_hurt` (=7) → cột **Wound**.
- Ánh xạ sprite: bảng `\settings\npcres\普通npc资源.txt` (id `c8f8f9d8`), hàng `ani001`: `Wound = ani001_bat.spr`, `Die = ani001_die.spr`, `Attack1/2/Magic = ani001_at.spr`, `FightStand/NormalStand1 = ani001_st.spr`, `NormalStand2 = ani001_pst.spr`, các Walk/Run = `ani001_wlk.spr`. Nạp theo tên cột (`C/KNpcResNode.cpp:453-457`).
- Số khung/hướng/interval: `\settings\npcres\普通npc资源信息.txt` (id `094d300b`): `Wound=64,8,75`, `Die=80,8,100`, `Attack=96,8,80`, `Stand=96,8,116`, `Walk=120,8,84`. ⇒ Wound = **8 khung mỗi hướng**, 8 hướng. (`interval` không dùng cho NPC – báo cáo 55.)
- **`ani001_bat.spr` có thực sự là ảnh Hit?** [TESTED ở mức hình ảnh + CONFIRMED ở mức dữ liệu]: header 320×320, 64 khung, 8 hướng, `interval 75` khớp bảng thông tin Wound; ảnh dựng hướng 0 (8 khung) `D:\JX1_U003_work\g07_out_bat_d0.png`: hổ quay mặt vào camera, thân thay đổi nhẹ giữa các khung (cúi/giật nhẹ). Ảnh chỉ cho thấy đây là animation riêng, khác `st`; "nó là phản ứng bị đánh" dựa vào **tên cột Wound + mã 7**, không phải vào việc nhìn ảnh.

### A2. Thời lượng logic và điều kiện gọi [CONFIRMED trong nguồn; thực chạy UNKNOWN]
- Server `DoHurt`: `nTotalFrame = 18 * HurtFrame * nHurtI * (100 − giam)/100000`, `giam = min(80, (m_CurrentHitRecover/10)*10)` (`S/KNpc.cpp:2991-3008`), gửi `NPC_HURT_SYNC{nFrames}`; client dùng đúng `nFrames` làm `nTotalFrame` (`C/KProtocolProcess.cpp:610-620` → `C/KNpc.cpp:1624-1658`).
- **Mapping `HitRecover` nay CONFIRMED** (báo cáo 56 đang ghi HYPOTHESIS): `m_CurrentHitRecover = m_HitRecover` (`S/KNpc.cpp:7127`), `m_HitRecover` ← cột `HitRecover` của NpcS (`S/KNpcTemplate.cpp:731`, rồi `S/KNpc.cpp:11212`). ani001: `HitRecover=50`, `HurtFrame = 12` (hàng 1) hoặc `10` (hàng 2).
- Số khung Hit khi `nHurtI=80` (đòn thường, skill 1 `DoHurt=80`): 18·12·80·50/100000 = 8,64 → **8**; 18·10·80·50/100000 = 7,2 → **7** (số nguyên, tính tay). Xác suất Hit = `nHurtI/2 + 50 − giam/2 = 65%` (`S/KNpc.cpp:3000`). [Ngoài phạm vi 375; chỉ để ghi rõ cơ chế.]
- **Có gọi Hit khi nhận sát thương từ skill 375 không?** Theo nguồn: **không** – `ReceiveDamage(..., bDoHurt=m_bDoHurt)` (`S/KMissle.cpp:1531,1544`) với `m_bDoHurt` = cột `DoHurt` của skill (`S/KSkills.cpp:2988,2863`); bảng Skills: **375 `DoHurt=0`, 387 `DoHurt=0`** (đọc `ec1243ff__script_skill.bin`); `CalcDamage` chỉ gọi `DoHurt` khi `bDoHurt` ≠ 0 (`S/KNpc.cpp:5746-5750`). Còn dưới mức kết luận: (1) exe server thật có thể khác nguồn; (2) skill 375 có `stun_p` (5%→15%, `kunlun.lua:211`) – có thể gây trạng thái choáng (`m_StunState`, `C/KNpc.cpp:1127,4541-4551`); **hiển thị của choáng chưa kiểm ⇒ UNKNOWN**, và không phải action Wound.
- U003 mặc định không phát Hit cho 375 (khuyến nghị 57) – **phù hợp** với bằng chứng nguồn.

### A3. Điều đã xác minh / chỉ suy luận
| Điều | Mức |
|---|---|
| index 7 = Wound = `ani001_bat.spr`, 64 khung/8 hướng | ĐÃ XÁC MINH (bảng + code) |
| 375/387 `DoHurt=0` ⇒ không Hit theo nguồn | ĐÃ XÁC MINH trên nguồn+bảng; chưa xác minh với exe thật |
| thời lượng Hit 7–8 khung (đòn thường) | CÓ BẰNG CHỨNG (tính từ công thức/dữ liệu), chưa đo chạy thật |
| Hit trông như thế nào trong client | CHƯA XÁC MINH (chưa có ảnh/quay màn hình client gốc) |

---
## 3. Mục B – Attrib 1002 và luồng sát thương

### B1. Định nghĩa Attrib 1002 [CONFIRMED – SỬA BÁO CÁO 56]
- Cột `Attrib` của Skills.txt → `KSkill::m_nAttrib` ("武功属性", `S/KSkills.cpp:2980`; khai báo `S/KSkills.h:108`), chỉ có accessor `IsAttrib()` và `IsBase() = (m_nAttrib <= 1)` (`S/KSkills.h:250-251`). Skill 375 có `Attrib=1002`; 387 không có. ⇒ Đây là **phân loại/thuộc tính môn công**, KHÔNG chứa trị sát thương. (Ý nghĩa chính xác của giá trị 1002: UNKNOWN; không cần cho U003.)
- Báo cáo 56 (mục A3) viết "sát thương gắn với `Attrib=1002`; 193 không có Attrib nên có thể không gây sát thương" – **sai**; thay thế bằng B2.

### B2. Nơi khai báo và truyền giá trị sát thương [CONFIRMED]
- Skills.txt: skill 375 có `LvlSetScript=\script\skill\kunlun.lua`, `LvlSetting1=lightingdamage_v`, `LvlData1=leidong_jiutian`, các `LvlSetting` khác: `skill_eventskilllevel, skill_collideevent, skill_showevent, skill_cost_v, addskillexp1, skill_skillexp_v, seriesdamage_p, stun_p, skill_attackradius`. Skill 387: `LvlSetting1=lightingdamage_v`, `LvlData1=pingdi_hanlei`, `LvlSetting2=seriesdamage_p` (đọc tay bảng `ec1243ff__script_skill.bin`).
- `kunlun.lua` (trích `D:\JX1_U003_work\out_kunlun_leidong.txt`, đúng nội dung `leidong_jiutian` ở dòng 199-239): `lightingdamage_v = { [1]={{1,80},{15,260},{20,470}}, [3]={{1,80},{15,260},{20,470}} }`, `seriesdamage_p={{{1,20},{15,20},{20,60},{21,62}}}`, `skill_collideevent[3]={{1,387},{20,387}}`, `stun_p`, `addskilldamage1`. `pingdi_hanlei` (dòng 283-289): `lightingdamage_v [1]=[3]={{1,25},{20,250}}`, `seriesdamage_p={{{1,20},{20,60},{21,62}}}`. Chỉ số [1] và [3] tương ứng `nValue[0]` (min) và `nValue[2]` (max) – `CalcDamage(nMin=pTemp_LightDamage[0], nMax=pTemp_LightDamage[2], …)` (`S/KNpc.cpp:4792-4798`). Mức kỹ năng người chơi lúc chơi thật: UNKNOWN (không đọc dữ liệu nhân vật). Giá trị 20 dmg/tick của U003 là **DESIGN**, không phải dữ liệu gốc.
- Lệnh chuyển thành thuộc tính phép: `KSkill` nạp các cột `LvlSetting/LvlData` thành `m_pDamageMagicAttribs` của skill (chi tiết hàm nạp lua chưa đọc từng dòng ⇒ HYPOTHESIS về cơ chế nạp, nhưng đường tiêu thụ ở dưới là CONFIRMED).

### B3. Chuỗi 375 → 181 → 387 → 193 → trừ HP (nguồn server) [CONFIRMED, trừ ghi chú]
1. `KNpc::OnSkill` tại mốc 60% gọi `pSkill->Cast(m_Index, m_DesX, m_DesY)` – **không truyền `nWaitTime`** (`S/KNpc.cpp:3989-4016`, mặc định 0, `S/KSkills.h:208`).
2. `KSkill::Cast` → `CastMissles` → `__CastFixed` → `CastZone` (`S/KSkills.cpp:523-531, 1577-1641, 1394-1480, 1668-1776`): 16 missile 181 (lưới 4×4) với `m_nStartLifeTime = nWaitTime + GetMissleGenerateTime(i*N+j)`.
3. Missile 181 (`CollidRange=2` ⇒ nhánh "tấn công nhóm"): mỗi tick khi đang ở trạng thái bay `FsCheckCollision` duyệt ô ±2 (5×5) tìm NPC kẻ thù; nếu thấy: **`ProcessCollision()`** (ở vị trí missile, vùng `DmgRange=2` ⇒ ±1 ô = 3×3) rồi **`DoCollision()`** (`S/KMissle.cpp:575-641`, `1989-1997`, `1785-1860`). `ProcessCollision` gọi `ProcessDamage` cho từng NPC trong 3×3 (`S/KMissle.cpp:1851`) – bị giới hạn nhịp bởi `DmgInterval` (`:1788-1796`).
4. `ProcessDamage` → `Npc[nNpcId].ReceiveDamage(m_nLauncher, …, m_pMagicAttribsData->m_pDamageMagicAttribs, m_bUseAttackRating, m_bDoHurt[, nDameXG])` (`S/KMissle.cpp:1531,1544`) – thuộc tính phép của **skill tạo ra missile đó**: 181 mang dữ liệu của **375**.
5. `ReceiveDamage` (`S/KNpc.cpp:4466-…`): bỏ qua nếu mục tiêu đã `do_death/do_revive`; nếu `bUseAR` kiểm tra trúng/né (`CheckHitTarget`, trượt ⇒ `SendBloodNo(...,999999999)` nhưng thân hàm `SendBloodNo` đã bị comment, `S/KNpc.cpp:14255-14270`); với sát thương sét gọi `CalcDamage(..., damage_light, ..., bDoHurt)` (`:4792-4798`).
6. **Sự kiện trừ HP quái:** `KNpc::CalcDamage` → `m_CurrentLife -= nDamage` (`S/KNpc.cpp:5716-5719`); nếu `<=0` → `DoDeath` (`:5753-5762`). Giá trị damage: `nMin + g_Random(nMax−nMin)` rồi qua kháng/ngũ hành (`:5085-…`).
7. `DoCollision` của 181 → `Collidsion` → cast skill **387** với bên phóng là missile 181 (`SKILL_SLT_Missle`, `S/KSkills.cpp:1469-1479`, 791) tại vị trí hiện tại của 181; do `ColVanish=1`, 181 biến mất ngay (`S/KMissle.cpp:1670-1700`).
8. Missile 193 (từ 387, `m_nStartLifeTime = 0 + 5`): sau 5 tick bắt đầu bay; mỗi tick `FsCheckCollision` (CollidRange 2 ⇒ 5×5) – nếu có kẻ thù: `ProcessCollision()` (3×3, dữ liệu **387**: `pingdi_hanlei`) rồi `DoCollision()` → `ColVanish=1` ⇒ **biến mất sau lần chạm đầu tiên**. Hết đời mà chưa chạm: `AutoExplode=0` ⇒ không gây sát thương thêm (`S/KMissle.cpp:389-412`).
- ⇒ **193 có sát thương riêng (dữ liệu 387)**, nhưng tối đa **một lần** (khi có kẻ thù trong 5×5 tại tick bắt đầu hoặc sau đó, trước khi hết đời); 181 gây một lần ngay khi va chạm. Số HP mất do mỗi cặp 181→193 trong gốc: ≤ 2 lần sát thương (375 rồi 387), cách nhau ≥ 5 khung (tính từ tick 181 va chạm).
- Sự kiện làm giảm HP trong gốc: `CalcDamage` trên **server** ⇒ máu mới gửi xuống client qua đồng bộ `SyncNpcMin` (`C/KProtocolProcess.cpp:2521-2547`) – client không tự trừ (báo cáo 56).

### B4. Client vs server vs EXE
| Tầng | Kết luận | Mức |
|---|---|---|
| Client | `KMissle::ProcessDamage` rỗng (`C/KMissle.cpp:1520-1523`); va chạm chỉ tạo hiệu ứng, sinh 387/193 hiển thị; HP lấy từ gói đồng bộ | CONFIRMED |
| Nguồn server | chuỗi B3 | CONFIRMED trên nguồn |
| Server EXE đang chạy | CHƯA XÁC MINH; không kết nối/thao tác VM, không dựng lại từ nguồn (CLAUDE.md: "mã nguồn có thể không khớp exe") | UNKNOWN |
| Lua `kunlun.lua` | đọc tự chứa trong repo nguồn; bản trong PAK `script_skill` (id khác) chưa đối chiếu byte-to-byte | HYPOTHESIS cùng nội dung |

### B5. Mâu thuẫn với luật U003 (DESIGN, không thay đổi, chỉ báo)
- Gốc: 181 gây sát thương **ngay** khi va chạm (vùng 3×3 quanh 181, dữ liệu 375); 193 gây **một** lần sau ≥ 5 khung (3×3, dữ liệu 387), rồi biến mất. U003: AOE tại vị trí kích hoạt 193, hai tick +500/+1000 ms, 20/tick, AOE chồng lấn cộng dồn.
- Gốc: một quái có thể bị nhiều 181/193 (16 cặp) nhưng mỗi missile chỉ chạm một lần; U003 cho phép tick lặp trong 1 s. ⇒ Chuỗi hình ảnh giữ gốc, **luật sát thương là DESIGN** (không nên gọi là "bản gốc").

---
## 4. Mục C – Thời điểm thi triển

### C1. Mốc 60% của action [CONFIRMED]
- `KNpc::OnSkill` (`S/KNpc.cpp:3979-4016`): `if (WaitForFrame() && nTotalFrame != 0) → kết thúc; else if (IsReachFrame(ATTACKACTION_EFFECT_PERCENT)) → Cast`. `ATTACKACTION_EFFECT_PERCENT = 60` (`S/KNpc.cpp:60`). `IsReachFrame(p)` là so sánh **bằng**: `nCurrentFrame == nTotalFrame * p / 100` (số nguyên, `S/KNpc.cpp:6852-6859`). Client dùng cùng mẫu (`C/KNpc.cpp:3742`).
- `nTotalFrame` (nội công, cast): `m_CastFrame * naAttackSpeed / (m_CurrentCastSpeed + nbAttackSpeed)` (`S/KNpc.cpp:3965-3976`; client `C/KNpc.cpp:2394-2402`). **`naAttackSpeed=nbAttackSpeed=100`** (`gamesetting_gs001.ini` dòng 56 `NpcAttackSpeed=100,100`; đọc `S/KGameglobalSet.cpp:20-21,89`) ⇒ `nTotalFrame = m_CastFrame*100/(CurrentCastSpeed+100)`.
- `m_CastFrame`: mặc định 20 (`C/KNpc.cpp:449`), template NpcS cột `CastSpeed` (default 20, `S/KNpcTemplate.cpp:668`). **Giá trị của nhân vật người chơi và `m_CurrentCastSpeed` thực: UNKNOWN** (không đọc dữ liệu nhân vật). Với `CastFrame=20, CurrentCastSpeed=0`: `nTotalFrame=20`, sự kiện tại khung **12**.
- Skill 375 không có `AttackFrame` riêng; `CharAnimId=11`, `TimePerCast=0` (không cooldown gốc). Cooldown 1 s và cast 1 s của U003 là **DESIGN**.

### C2. Ý nghĩa và đơn vị `nWaitTime`, `WaitTime`, `MslsGenerateData` [CONFIRMED]
- `WaitTime` (cột Skills) → `m_nWaitTime` (`S/KSkills.cpp:3038`): độ trễ cơ sở cộng vào `GetMissleGenerateTime`. 375: 2; 387: 5.
- `MslsGenerateData` → `m_nMisslesGenerateData` (375: 5): bước/biên độ thời gian giữa các missile; `MslsGenerate` = kiểu (375: 3 = `SKILL_MGS_RANDONORDER`; 387: 0 = `SKILL_MGS_NULL`).
- `nWaitTime` (tham số `Cast`): độ trễ chuyền từ skill cha; **lần cast của người chơi = 0** (`S/KNpc.cpp:4016`, tham số mặc định `nWaitTime=0` ở `S/KSkills.h:208`; `Cast` còn ép `<0 → 0`, `S/KSkills.cpp:528-531`). Skill con từ missile: `CastMissles(..., 0, SKILL_SLT_Missle)` (`S/KSkills.cpp:791`) ⇒ cũng 0.
- `GetMissleGenerateTime(nNo)` (`S/KSkills.cpp:3272-3312`): `NULL → WaitTime`; `SAMETIME → WaitTime + data`; `ORDER → WaitTime + nNo*data`; **`RANDONORDER → WaitTime + nNo*data + (g_Random(2)==1 ? +g_Random(data) : −g_Random(data/2))`** với `data=5 ⇒ data/2=2`.
- **Đơn vị**: số lần `KMissle::Activate()` được gọi (mỗi lần `m_nCurrentLife++`, `S/KMissle.cpp:497`) – tức "tick logic server". Server có `GAME_FPS 18` (`S/CoreServerShell.cpp:2227`) và `FRAME2TIME 18` (`S/KNpc.cpp:78`; "mỗi giây" = 18 tick, `:1442`); báo cáo 41 đã đo server 18 Hz (TESTED ở báo cáo đó, không tái đo ở đây). **Hz của client = UNKNOWN**; không quy đổi sang mili giây trong báo cáo này.

### C3. Timeline cast và 16 missile 181 (đơn vị: tick logic; gốc JX1)
Quy ước: `T0` = tick bắt đầu action cast (DoSkill); `E` = tick sự kiện 60% = `nTotalFrame*60/100` (`E=12` nếu `CastFrame=20`, `CurrentCastSpeed=0` – giả định, xem C1); tick tuyệt đối của missile = `E + d_k` (missile tạo ở tick E với `m_nCurrentLife=0`; bắt đầu bay khi `m_nCurrentLife == d_k`).
| Sự kiện | Khung | Nguồn |
|---|---|---|
| Bắt đầu cast (`DoSkill`), đặt `NextCastTime = now + 0` | T0 | `S/KNpc.cpp` (DoSkill; `TimePerCast=0`) |
| Kết thúc action cast (`WaitForFrame`) | `nTotalFrame` (=20 nếu mặc định) | `S/KNpc.cpp:3984` |
| `CastZone` tạo 16 missile 181 | E (=`nTotalFrame*60/100`, =12 nếu mặc định) | `S/KNpc.cpp:3989-4016` |
| Missile 181 thứ k bắt đầu bay (k=0..15; `d_k = 2 + 5k + X_k`, `X_k ∈ {0..4}` (xác suất ½) hoặc `{−1,0}` (xác suất ½); `k = i*4 + j`) | E + d_k | `S/KSkills.cpp:1776, 3292-3298` |
| — k=0: `d_0 ∈ [1..6]`; k=1: `[6..11]`; k=5: `[26..31]`; k=10: `[51..56]`; k=15: `[76..81]` | | tính từ công thức |
| 181 chạm kẻ thù trong 5×5 → damage 375 (3×3) + `DoCollision` → sinh 387 và biến mất | tick chạm c_k ≥ E + d_k (nếu có kẻ thù trong 5×5 ở tick đó) | `S/KMissle.cpp:575-641` |
| 193 tạo tại vị trí 181; bắt đầu bay | c_k + 5 | `S/KSkills.cpp:3277-3279`, `1776` |
| 193 chạm → damage 387 (3×3) + biến mất (`ColVanish`) | ≥ c_k + 5 (nếu có kẻ thù trong 5×5); tối đa đời `LifeTime=12` (+5 bắt đầu) | `S/KMissle.cpp:389-412, 1989-1997` |
| 193 hết đời không chạm | c_k + 5 + 12 | `S/KMissle.cpp:389-412` (`AutoExplode=0`) |
- `m_nLifeTime += m_nStartLifeTime` (đời tính từ lúc bắt đầu bay) – lấy từ báo cáo 55, không đọc lại.
- Đây là chuỗi **gốc**; luật U003 (cast 1 s, cooldown 1 s, tick +500/+1000 ms, 20 dmg) là DESIGN và **không** suy ra từ bảng trên.
- Khoảng trễ tổng cộng của 16 missile: từ khung E+1 đến E+81 (k=0 nhỏ nhất `d≥1`; k=15 lớn nhất `d≤81`), tức tối đa ~81 tick sau khung phóng; quy sang giây phụ thuộc Hz (server 18 Hz ⇒ ~4,5 s, chỉ để tham khảo **server**, HYPOTHESIS cho cảm nhận trên client).
- Rủi ro chồng cast: với cooldown U003 1 s và đời gốc tới ~81 tick, nhiều đợt missile của các lần cast liên tiếp **chắc chắn chồng nhau** ⇒ cần `castId` riêng cho mỗi đợt (đúng yêu cầu mục 3 của chỉ thị).

---
## 5. Mục D – `MoveKind = Stand`

### D1. Xử lý trong nguồn [CONFIRMED]
- `OnFly()` (`S/KMissle.cpp:650-…`): sau kiểm tra người phóng, ngắt khi di chuyển (`m_nInteruptTypeWhenMove`), `TestBarrier()` (vật cản ⇒ `DoVanish`), `FsCheckCollision()`, rồi `switch(m_eMoveKind)`: **`case MISSLE_MMK_Stand: break;`** (`S/KMissle.cpp:731-734`) – không có đoạn cập nhật vị trí/vận tốc/hướng nào cho Stand; các nhánh `Parabola/Line` (`:735-…`) là nơi có theo dõi mục tiêu/độ lệch. Client: cùng cấu trúc (`C/KMissle.cpp` tương ứng, báo cáo 55).
- ⇒ Missile 181: **đứng yên tại ô sinh** (vị trí tính ở `CastZone`: `begin = ref − N*cell/2`, `+ (j*cellW, i*cellH)`), không "bay"; không homing. Hiển thị `AnimFile2` 6 khung chạy theo `LifeTime` tại chỗ.
- Điều kiện vô hiệu hóa: `TestBarrier()` tại ô sinh (vật cản ⇒ 181 biến mất không gây sát thương), người phóng rời map/chết (`Activate`, `S/KMissle.cpp:350-361`), `m_nInteruptTypeWhenMove` (giá trị của 181: UNKNOWN – chưa đọc cột tương ứng), hết đời.
- Vị trí 193: CONFIRMED – `SKILL_SLT_Missle` dùng toạ độ hiện tại của missile 181 (`NewMap2Mps(m_nRegionId, m_nCurrentMapX/Y, offsets)`) làm `nRefPX/nRefPY`, `ChildSkillNum=1` ⇒ 193 tại chính điểm đó (`S/KSkills.cpp:1469-1479`). Không có nhánh nhắm vào quái.
- Điều kiện collision 181: có kẻ thù (`m_eRelation`) trong ±2 ô (5×5) quanh ô hiện tại của missile, **khi `m_eMissleStatus == MS_DoFly`** (sau `start` tick) (`S/KMissle.cpp:414-429, 619-640`). Chưa đọc từng dòng phần sau `switch` của `OnFly` (cập nhật offset); với Stand các `nDOffset` mặc định 0 ⇒ HYPOTHESIS-cao không dịch chuyển.

---
## 6. Mục E – Render, blend, anchor

### E1. Đường vẽ NPC và cờ anchor [CONFIRMED]
- Ảnh thân NPC khởi tạo với `bRenderFlag = RUIMAGE_RENDER_FLAG_REF_SPOT`, `bRenderStyle = IMAGE_RENDER_STYLE_ALPHA` (`C/KNpcRes.cpp:165-183`); không có `FRAME_DRAW`.
- `KgameWorld::DrawPrimitives` (`gamescene/KgameWorld.cpp:11344-…`) lấy ảnh bằng **`ccgetTxtData`** (`:11404`; định nghĩa `:8115-8183`), đặt sprite với `setAnchorPoint(ccp(0,0))` và `setPosition(NewscrX − x, visibleSize.height − NewscrY − rect.height − y)` (`:11477-11492`).
- `ccgetTxtData`: `nX,nY = GetLocalPositionByMps(mps, z)`; vì có `REF_SPOT`: nếu `CenterX||CenterY` ≠ 0 thì trừ `(CenterX,CenterY)` của header; **ngược lại nếu `Width > 160` thì trừ `(160,192)`**; vì không có `FRAME_DRAW`: cộng `(OffsetX,OffsetY)` của khung (`:8146-8177`).
- **ani001**: `Center=(0,0)`, `Width=320 > 160` ⇒ trừ **(160,192)** rồi cộng offset khung (CONFIRMED trong code cho đường vẽ NPC).
- Đính chính báo cáo 55 (nhãn hàm): đoạn `KgameWorld.cpp:8029-8057` tôi từng gọi `ccgetTxtData` thực ra là **`ccgetTxtData_g`** (`:8002-8064`); bản `_p` (`:8066-8111`) **không** có nhánh mặc định (160,192) và dùng ở `Draw_Part_map` (`:7485`) và biểu tượng trạng thái (`:9081`); bản `ccgetTxtData` (đúng đường NPC) có cùng logic với `_g`.

### E2. Kiểm tra hình học [TESTED]
Script `g07_anchor.py` (giải mã mọi khung của 6 sprite ani001, tính hộp bao điểm không trong suốt trong toạ độ canvas 320×320 rồi trừ (160,192)):
| sprite | tâm ngang (px, so với anchor) | đáy (chân) | đỉnh |
|---|---|---|---|
| st / pst (hướng 0..7) | −4…+2 (đa số trong ±2) | +6…+24 | −66…−43 |
| wlk | −5…+4 | +2…+28 | −68…−46 |
| bat (Wound) | −12…+10 | +6…+30 | −69…−43 |
| die | −20…+19 | +6…+42 | −66…−24 |
| at | −23…+22 | −4…+33 | −109…−35 |
- Hướng 0 và 4 (chính diện/lưng) có tâm ngang = 0 (±0) ở st/pst/wlk/bat ⇒ phù hợp với việc điểm chân/đứng nằm ở x=0 sau khi trừ 160 ⇒ **(160,192) khớp thiết kế sprite** (suy luận từ đối xứng; **không** phải chứng minh tuyệt đối). Chân ở y ≈ +6…+24 dưới anchor (192 là điểm cao hơn chân vì sprite chứa thêm chiều sâu vẽ); không đổi kết luận trừ 192.
- Không có ảnh chụp client gốc để đối chiếu pixel ⇒ **giới hạn**: chưa đo lệch thật giữa client và Unity.

### E3. Giải mã/alpha/blend/frame [đã có ở 55 + bổ sung]
- Giải mã & alpha: giữ kết luận 55 (RLE (count,alpha), palette 24-bit; `Reserved[1]=0` ⇒ không dùng nhánh "xóa viền" – mẫu đã quét: 257 `skills.pak` + 2500 `spr.pak`, 13 sprite U003).
- **Blend**: trong mã vẽ NPC/đạn **không có `setBlendFunc` riêng** (grep `setBlendFunc/BlendFunc/ccBlendFunc` trên `KgameWorld.cpp`, `KNpcRes.cpp`, `KMissleRes.cpp`, `KSkillSpecial.cpp`, `Kgetinidata.cpp`: chỉ `GL::blendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)` ở `KgameWorld.cpp:14860`, thuộc đường batch của `lifeBatchNode`) ⇒ sprite NPC/đạn dùng blend mặc định của `CCSprite`/texture RGBA straight-alpha; chế độ cộng/sáng cho hiệu ứng (nếu có) **UNKNOWN** (có thể được mã hóa trong dữ liệu/ảnh, không tìm thấy trong mã). Cần ảnh gốc để chốt → **không tự chọn additive**.
- Chuyển frame theo hướng/action: `KNpcRes::Draw` (báo cáo 55, mục A5/C): `dirNo*per + per*nCurFrame/nAllFrame`; ở Wound: 8 khung/hướng ép vào `nTotalFrame` Hit (7–8).
- Rủi ro lệch/viền/tỉ lệ: (i) viền alpha: texture straight-alpha, nếu Unity dùng premultiplied sai sẽ ra viền sáng/tối; (ii) neo: nhớ trừ (160,192) trước khi cộng `(OffsetX,OffsetY)`; (iii) khung sprite có kích thước nhỏ (ví dụ 28×76) cắt từ canvas 320×320 ⇒ phải dùng offset khung; (iv) y của màn hình bị đảo (`visibleSize.height − y`) – chỉ là chi tiết của Cocos; (v) kích thước không bị scale trong mã đã đọc (`__scaleFactor` bị comment, `:8143`).

---
## 7. Mục F – Map 45 và toạ độ

### F1. Dữ liệu đã kiểm [TESTED, `g07_region.py`, đọc từ `map.pak`]
- `\maps\中原北区\天忍教\天忍教室外.wor` (id `989a8a6a`, `map.pak`): `rect=95,94,108,103`, `IsInDoor=0` ⇒ lưới 14×10 = 140 vùng.
- `\maps\中原北区\天忍教\天忍教室外\v_YYY\XXX_Region_C.dat`: **122/140 có mặt; 18 thiếu** (rìa): hàng y=94: x=95,96,97,98,101,103,104,108; cột x=95 ở y=95..99; hàng y=103: x=95,96,102,103,108 (danh sách đủ ở bản đồ ô trong `g07_region.py`; ảnh lưới: `#` có, `.` thiếu). Không có lỗi giải nén.
- Nội dung (122 vùng): ground nodes tổng 7168; buildin **Tree 0, Line 72, Point 283, Above 4** (tổng 359 bản ghi); ô obstacle ≠ 0: 34001; trap/npc/obj theo từng vùng (không tổng hợp). 14 ảnh buildin khác nhau (ví dụ `菩提树1.spr` 115 lần, `菩提树2.spr` 84, nhà `house121-1.spr` 38…).
- Kết luận về "đầy đủ": **chưa thể kết luận map 45 hoàn chỉnh**. 18 vùng thiếu có thể là vùng không có gì (rìa) hoặc dữ liệu cắt; cần chọn **hình chữ nhật chơi** nằm trong vùng đủ file (ví dụ x=96..107, y=95..102 đều có đủ) – quyết định thuộc người dùng (mục 8).

### F2. Hệ toạ độ [CONFIRMED + TESTED]
- **Region**: `RWPP_AREGION_WIDTH=512`, `HEIGHT=1024` (`gamescene/KScenePlaceRegionC.h:35-38`); gốc vùng `m_LeftTopCornerScenePos = (rx*512, ry*1024)` (`KScenePlaceRegionC.cpp:95-96`) – tức MPS tuyệt đối `x = rx*512 + local`, `y = ry*1024 + local`.
- **Ô logic**: `CellWidth/Height = 32 MPS` (báo cáo 55), vùng = 16 × 32 ô (`KSPTrap.cX 0-16, cY 0-32`, `SceneDataDef.h`).
- **Ground**: toạ độ ô cục bộ trong vùng + gốc vùng: `x = h*CellWidth + left`, `y = (v*CellHeight)*2 + top` (`KScenePlaceRegionC.cpp:789-790`) – chú ý nhân 2 theo y.
- **Obj (KSPObj)**: toạ độ **tuyệt đối**, trừ gốc vùng để thành cục bộ khi dựng (`:404-405`: `x − left`, `(y − top)/2`).
- **Buildin (`KBuildinObj.oPos1/oPos2`, `ImgPos1-4`)**: struct 228 byte (kiểm tay: `16 + n*228 = kích thước section` đúng ở 122/122 vùng); ở bản ghi, `oPos1` là toạ độ **MPS tuyệt đối**: 0/359 bản ghi nằm trong khoảng cục bộ [0,512)×[0,1024); 263/359 nằm trong chính vùng chứa chúng; 96/359 nằm ngoài rect của vùng chứa (vật thể gần/vượt biên – lưu ở vùng khác với vị trí điểm đầu). Ví dụ vùng (100,94): `oPos1=(51368, 97616, 0)` ⇒ x = 100·512 + 168, y = 95·1024 + 336 (thuộc hàng vùng 95, lưu ở hàng 94). Ý nghĩa 96 bản ghi ngoài vùng (tại sao lưu ở vùng đó): **chưa phân tích**.
- **MPS → màn hình**: `screen_x = mps_x − m_nLeft`; `screen_y = mps_y/2 − m_nTop − ((z*887)>>10)` (`C/KSubWorld.cpp:188-192`, báo cáo 55; CONFIRMED). Đối tượng runtime đặt tại (x, y+6) (báo cáo 54/55).
- **Chuyển cell ↔ MPS** khi tính collision: `NewMap2Mps(region, mapX, mapY, offX, offY)` (đã dùng ở các hàm trên).

### F3. Cần cho port KIpoTree
- Map 45 chỉ có **Line (72) / Point (283) / Above (4)** – **không có Tree** ⇒ `AddBranch`, `Clone`, `SM_Relation_LineLine_CheckCut` (cắt) **không** được đi qua bởi dữ liệu map này. Test T-IPOT cho nhánh Tree/Clone cần **cảnh tổng hợp** hoặc chọn thêm một map có Tree (không bắt buộc cho G0.7).
- Obstacle: 34001 ô khác 0 trong 122 vùng; ý nghĩa giá trị (20/17/33/36/49/65/81…) chưa tra bảng ⇒ UNKNOWN (chặn/đi được/nước…).
- Buildin Point 283 gồm cây Bồ Đề (ảnh `菩提树*.spr`), nhà `house121-1.spr`; sprite buildin có `nFrame/nImgNumFrames/nAniSpeed` (animation theo ms thật – báo cáo 55).
- Trap/NPC/Obj từng vùng: có nhưng không cần cho prototype; **15 điểm spawn không có trong dữ liệu client** (đã biết, chưa đổi).

---
## 8. Mâu thuẫn với báo cáo trước (kết luận bị thay thế – không xóa lịch sử)
| # | Báo cáo/nội dung cũ | Thay thế | Bằng chứng |
|---|---|---|---|
| 1 | BC 56 mục A3/C: "sát thương gốc có thể đến từ Attrib 1002 của 375/181; 387 không có Attrib nên 193 có thể không gây sát thương" | `Attrib` là phân loại kỹ năng (`m_nAttrib`); **387 có `lightingdamage_v` (`pingdi_hanlei` 25→250)** ⇒ 193 có damage riêng (1 lần) | `S/KSkills.cpp:2980`, `KSkills.h:108,250`; bảng Skills; `kunlun.lua:283-289` |
| 2 | BC 56 A3: "193: KHÔNG (và có thể không gây sát thương)" | 193 gây sát thương một lần (3×3, dữ liệu 387) sau ≥5 tick bắt đầu; 181 gây ngay khi chạm | `S/KMissle.cpp:575-641, 1785-1860, 1989` |
| 3 | BC 55 D2.3 / BC 57 mục 2.4: "`nWaitTime` đầu vào của lần cast người chơi UNKNOWN (có thể 0)" | **= 0** (tham số mặc định, `Cast(m_Index, m_DesX, m_DesY)`) | `S/KNpc.cpp:4016`, `S/KSkills.h:208` |
| 4 | BC 55: nhánh trừ của RANDONORDER viết `−rand(2)` | Đúng: `−g_Random(MslsGenerateData/2)` = `rand(2)` khi data=5 | `S/KSkills.cpp:3294-3298` |
| 5 | BC 56 A2/A4 và mục 8.6: `HitRecover → m_CurrentHitRecover` HYPOTHESIS | **CONFIRMED** | `S/KNpc.cpp:7127`, `S/KNpcTemplate.cpp:731` |
| 6 | BC 55 mục A6/BC 57: anchor (160,192) là HYPOTHESIS "chỉ suy luận từ một đường nạp ảnh" | đường vẽ NPC thật dùng `ccgetTxtData` với `REF_SPOT` ⇒ trừ (160,192) cho ani001 (CONFIRMED code) và khớp hình học (TESTED) | mục E |
| 7 | BC 55: nhãn hàm `ccgetTxtData` ở `:8029-8057` | thực là `ccgetTxtData_g`; `ccgetTxtData` (`:8115`) dùng cho NPC; `_p` khác (không mặc định 160,192) | mục E1 |
| 8 | BC 56 mục 8.1: "nội dung/thứ tự `npc动作表.txt` UNKNOWN; Wound = chỉ số 7 HYPOTHESIS" | **CONFIRMED** (đọc bảng thật) | mục A1 |
| 9 | BC 51/54: map 45 "ứng viên, chưa kiểm Region_C" | đã kiểm: 122/140 có, 0 Tree | mục F |
| 10 | BC 56 mục C: "chưa thấy gói số damage riêng" | đúng, và `SendBloodNo` còn bị comment thân hàm (`S/KNpc.cpp:14255-14270`) | cùng kết luận, thêm bằng chứng |

## 9. Quyết định thiết kế U003 cần người dùng phê duyệt
1. **Chuỗi sát thương gốc ≠ luật U003.** Gốc: 181 gây sát thương ngay khi chạm (3×3) + 193 gây thêm 1 lần sau ≥5 tick. U003 (đã duyệt): hai tick +500/+1000 ms từ lúc 193 kích hoạt, 20/tick, cộng dồn. **Giữ luật U003** (khuyến nghị theo chỉ thị) và ghi rõ trong tài liệu là DESIGN; hay muốn một chế độ "đúng gốc" để so sánh?
2. Có thể **181 không gây sát thương** trong U003 (chỉ 193) – hay phải nhất quán với gốc là 181 cũng gây sát thương? (Luật đã duyệt chỉ nêu 193/AOE.) Đề xuất: không, để giữ luật đã duyệt; ghi chú khác biệt.
3. **Trạng thái `stun_p`** của 375 (5–15%): U003 bỏ qua (không có choáng). Chấp nhận?
4. **Đơn vị thời gian của timeline gốc:** U003 dùng giây cho cast/cooldown/tick; chuỗi hình ảnh (độ trễ 16 đạn) tính theo "tick": dùng 18 tick/giây (hằng server, `GAME_FPS 18`) để quy đổi? Client Hz chưa biết; chọn 18 chỉ là DESIGN.
5. **Độ trễ ngẫu nhiên** của 16 đạn: giữ ngẫu nhiên theo công thức gốc (kèm seed cố định để test lặp lại) hay cố định giá trị trung bình?
6. **Anchor ani001 = (160,192)** (nay có bằng chứng): duyệt dùng, kèm test đối chiếu ảnh client gốc khi có.
7. **Map 45:** chọn hình chữ nhật chơi trong vùng đủ file (đề xuất x=96..107, y=95..102 – đều có Region_C.dat), chấp nhận 18 vùng thiếu ở rìa; chấp nhận rằng map 45 không kiểm được nhánh Tree/Clone (dùng cảnh tổng hợp).
8. **Không phát Hit cho 375** (khuyến nghị 57, nay có bằng chứng nguồn) – duyệt.

## 10. Việc còn thiếu trước khi bắt đầu G1
| # | Việc | Loại |
|---|---|---|
| 1 | Ảnh/quay màn hình client gốc: ani001 (anchor, Hit, Death), hiệu ứng 181/193/cast (blend, kích thước), một cây Bồ Đề + nhà | cần người dùng (không thể từ source) |
| 2 | Đo Hz client; đối chiếu `nTotalFrame` cast của nhân vật người chơi (`CastFrame`, `CurrentCastSpeed`) | cần dữ liệu nhân vật/ chạy client |
| 3 | Xác minh exe server thật = nguồn (chạy thử trong VM sau khi người dùng cho phép), nhất là chuỗi B3 | nằm ngoài READ-ONLY |
| 4 | Bản đồ giá trị obstacle (20/17/33/36/49/65/81) và 96 buildin lưu ngoài vùng | đọc tiếp (READ-ONLY) |
| 5 | Chọn/ghép map có Tree để thử `Clone`, hoặc cảnh tổng hợp | thiết kế test |
| 6 | Quét tiếp `spr.pak` ngoài mẫu 2500 chỉ nếu asset U003 cần (manifest riêng) | thiết kế |
| 7 | Test specification bổ sung `TYPE_FRAME` cho công cụ trích (không sửa công cụ): (a) entry cờ byte cao `0x11` giải đúng `W×H` và số khung; (b) so sánh băm từng khung với script riêng; (c) lỗi UCL ⇒ báo lỗi, không ghi file rỗng; (d) entry nén cả file không đổi | chỉ spec, chưa implement |
| 8 | Đóng UNKNOWN còn lại: ý nghĩa `Attrib=1002`, `m_nInteruptTypeWhenMove` của 181, hiển thị choáng, blend hiệu ứng | không chặn G1 nếu được chấp nhận bằng văn bản |

## 11. Các kiểm tra đã làm / chưa làm
- Đã làm: đọc bảng action/sprite/thông tin quái; dựng ảnh `bat`; hộp bao 6 sprite × 8 hướng; đọc luồng Hit (client/server); đọc `Skills`/`kunlun.lua` cho 375/387; đọc chuỗi missile server (`Activate/FsCheckCollision/OnFly/DoCollision/ProcessCollision/ProcessDamage`, `Cast/CastZone/GetMissleGenerateTime`, `OnSkill/IsReachFrame`, `ReceiveDamage/CalcDamage`); quét 140 `Region_C.dat` của map 45 và đo toạ độ buildin.
- Chưa làm / ngoài phạm vi: chạy client/server; đối chiếu ảnh gốc; đọc phần sau `switch` của `OnFly`; nạp lua → thuộc tính phép (`KSkill::LoadLevelSetting`); nội dung `Attrib=1002`; xem đầy đủ mọi nhánh `bDoHurt=false` của sát thương sét/lạnh; xác nhận exe server.
