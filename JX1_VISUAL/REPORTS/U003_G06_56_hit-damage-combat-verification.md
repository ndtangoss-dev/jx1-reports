# 56 – U003 G0.6: phản ứng trúng đòn (Hit), animation Hit của ani001, damage number, luật Combat

Phạm vi: CHỈ ĐỌC (client `Folder/Client2912-…/Client/Classes`, server nguồn `SwordOnline/…/jxOnline/gameserver/Sources/Core/Src`, bảng dữ liệu đã trích ở `D:\JX1_U003_work`). Không tạo Unity project, không code gameplay, không build, không sửa PAK/server/DB/VM/EXE, không đụng Goddess, U001/U002, không push.
Nhãn: **CONFIRMED** (đọc code, có file:dòng) · **TESTED** (đã chạy/đo/xem ảnh) · **HYPOTHESIS** · **DESIGN DECISION** · **UNKNOWN**. Viết tắt đường dẫn: `C/` = client `gamecore/`, `S/` = server `Core/Src/`.
Giới hạn chung: mã nguồn server có thể không khớp exe đang chạy (CLAUDE.md, chưa dựng lại từ nguồn); chưa chạy client/server nào, chưa quay màn hình; mọi "thời gian" tính theo khung logic, quy ra giây còn phụ thuộc Hz (HYPOTHESIS 18 Hz, báo cáo 30/41/55).

## TÓM TẮT 5 DÒNG
1. Client KHÔNG tự tính Hit/sát thương từ đạn: va chạm đạn ở client chỉ tạo hiệu ứng (`KMissle::ProcessDamage` là hàm rỗng trả FALSE); Hit của NPC chỉ chạy khi nhận gói server `s2c_npchurt`.
2. Skill 375 và 387 có `DoHurt=0` trong bảng Skills ⇒ theo mã server, sát thương từ chuỗi 181/193 KHÔNG gửi gói Hit: quái trúng Lôi Động Cửu Thiên chỉ mất máu (và hiện số), không phát animation Wound; đòn đánh thường (skill 1: `DoHurt=80`) thì có thể.
3. Hit không bị ngắt/khởi động lại: `DoHurt` bị bỏ qua nếu đang `do_hurt`/`do_death`; Death luôn ghi đè Hit.
4. Damage number gốc: số đỏ từ font bitmap `number_16_r.fnt`, tối đa 5 số/quái, nguồn là hiệu số máu giữa hai gói đồng bộ (không phải từng đòn); nên "mỗi lần nhận sát thương một số" của U003 là DESIGN DECISION khác gốc.
5. Combat architecture đủ điều kiện triển khai cho prototype với các DESIGN DECISION ở mục 9; còn UNKNOWN: Hz client, tên/thứ tự action "Wound", vùng sát thương thực của 181/193 trên server chạy thật.

Cần tôi quyết định: có (mục 10).

---
## A. Luồng từ missile 181 đến 193 và phản ứng của NPC

### A1. Phía client: va chạm đạn không gọi Hit/HP [CONFIRMED]
- `KMissle::DoCollision` (`C/KMissle.cpp:1560-1600`): chỉ (a) kích hoạt `pOrdinSkill->Collidsion(this)` nếu `m_bCollideEvent` (:1570-1577; chính là chỗ sinh 193 qua skill 387), (b) nếu `m_bCollideVanish` thì tạo hiệu ứng `MS_DoVanish` + `DoVanish()` (:1583-1591). Không có lệnh gọi `Npc[...].DoHurt/SetBlood/m_CurrentLife` nào.
- `KMissle::ProcessCollision` (vùng 3×3 của 193, `C/KMissle.cpp:1675-1760`): với mỗi NPC thù trong ô → chỉ `CreateSpecialEffect(MS_DoCollision, x, y, z[, mNpcIdx])` (:1738-1745); không đổi trạng thái NPC.
- `KMissle::ProcessDamage` (`C/KMissle.cpp:1520-1523`): `return FALSE;` — hàm tính sát thương phía client là rỗng. Hai nơi gọi (`:806`, `:1108`) cũng không có tác dụng.
- Tìm toàn bộ `Npc[x].Do*/Send*/Proc*/Set*` trong `C/KMissle.cpp`: không có (grep, 0 kết quả khớp). ⇒ Trả lời câu A1/A2/A3: **client không gọi trạng thái Hit, không đổi Action/State, không gọi animation Hit trực tiếp từ va chạm đạn.**
- Giới hạn: đọc theo grep và các hàm liên quan; chưa đọc từng dòng 3000 dòng `KMissle.cpp`.

### A2. Hit đến từ server [CONFIRMED]
- Client nhận `s2c_npchurt` (`C/KProtocolProcess.cpp:71,610-620`) → `Npc[nIdx].ProcNetCommand(do_hurt, nFrames, nX, nY)` → `KNpc::ProcNetCommand` case `do_hurt` → `DoHurt(x, y, z)` (`C/KNpc.cpp:10202-10203`); đường dự phòng `ProcCommand` cũng gọi `DoHurt` (`C/KNpc.cpp:894-896, 927-929`).
- Client `KNpc::DoHurt(nHurtFrames, nX, nY, nRank)` (`C/KNpc.cpp:1624-1658`): đặt `m_Doing = do_hurt`, `m_ClientDoing = cdo_hurt`, `m_ProcessAI = 0`, `m_Frames.nTotalFrame = nHurtFrames` (≥1), `nCurrentFrame = 0`, lưu điểm đẩy `m_nHurtDesX/Y`. Tức là **có đổi State/Action** nhưng chỉ khi gói server tới.
- Server `KNpc::CalcDamage` (`S/KNpc.cpp:5067`): trừ máu (`:5719`), nếu `nDamage > 0 && bDoHurt` → `DoHurt(0,0,0,bDoHurt)` (`:5746-5750`); nếu `m_CurrentLife <= 0` → `DoDeath` (`:5753-5762`). Server `DoHurt` (`S/KNpc.cpp:2965-3045`) gửi `NPC_HURT_SYNC{ID, nFrames, nX, nY}` (`:3028-3033`, struct `C/KProtocol.h:~450-458`).
- Tham số `bDoHurt` đi từ cột `DoHurt` của bảng Skills qua `KSkill` → `KMissle::m_bDoHurt` (`S/KSkills.cpp:2988, 2863`) → `ReceiveDamage(..., m_bDoHurt, ...)` (`S/KMissle.cpp:1531,1544`) → `CalcDamage(..., bDoHurt, ...)` (`S/KNpc.cpp:4792-4798` cho sát thương sét).
- Dữ liệu [TESTED, đọc bảng `ec1243ff__script_skill.bin`, cột `DoHurt`]: **skill 375 `DoHurt=0`; skill 387 `DoHurt=0`; skill 1 (đòn vật lý thường) `DoHurt=80`, `IsMelee=1`, `IsPhysical=1`.** Skill 375 chỉ có `Attrib=1002`; skill 387 không có cột Attrib nào khác 0 (script kiểm tra tay, `tools/g06_q3.py`).
- ⇒ **Theo mã nguồn server + dữ liệu: Lôi Động Cửu Thiên không kích hoạt Hit của quái.** Giới hạn: exe server đang chạy có thể khác nguồn; không có test thực.

### A3. So sánh bốn loại nguồn sát thương
| Nguồn | Client | Server (nguồn) | Hit? |
|---|---|---|---|
| Đòn đánh thường (skill 1/2) | chỉ hiệu ứng/animation tấn công | `DoHurt=80` ⇒ có thể gọi `DoHurt` (xác suất, A6) | CÓ thể (HYPOTHESIS cho kết quả thực vì còn xác suất) |
| Missile 181 (skill 375) | chỉ vẽ + kích hoạt sự kiện va chạm sinh 193 (`DoCollision`) | cùng đường `ReceiveDamage` với `bDoHurt=0` | KHÔNG |
| Missile 193 (skill 387) | vẽ vùng 3×3, `ProcessCollision` chỉ tạo hiệu ứng | skill 387 không có Attrib sát thương; `DoHurt=0` | KHÔNG (và có thể không gây sát thương, xem dưới) |
| Skill vùng nói chung | như 193; client không trừ máu | `ProcessCollision` server gọi `ProcessDamage` cho từng NPC trong vùng (`S/KMissle.cpp:1785-1860`) | tùy `DoHurt` của skill |
- Nguồn sát thương thực của chuỗi 375: sát thương gắn với `Attrib=1002` của skill 375 (đạn 181 do 375 tạo, mang dữ liệu sát thương của 375); 193 do skill 387 tạo mà 387 không có Attrib ⇒ **HYPOTHESIS: sát thương server đến từ 181, không phải 193** (chưa đọc `Attrib 1002` và lua `kunlun.lua` để xác minh). Điều này không ảnh hưởng luật U003 (luật riêng).
- `DmgInterval` [CONFIRMED phía server]: `KMissle::ProcessCollision` bỏ qua nếu `m_ulNextCalDamageTime > GetGameTime()`, ngược lại đặt `next = now + DmgInterval` (`S/KMissle.cpp:1788-1796`) ⇒ giới hạn tần suất gây sát thương mỗi missile (181: 10, 193: 4; đơn vị = `GetGameTime`, **HYPOTHESIS: khung game**). Gốc không có "tick 500 ms/1000 ms" cố định; đó là luật U003.
- Cập nhật "khác biệt gốc ↔ U003": gốc 193 sống 12 khung và có thể áp sát thương lặp theo `DmgInterval`; U003 thay bằng hai tick cố định.

### A4. Điều kiện khiến NPC không phát Hit [CONFIRMED trong mã]
Client `DoHurt` bỏ qua khi: `m_RegionIndex < 0`, `m_Doing == do_hurt` hoặc `do_death` (`C/KNpc.cpp:1629-1632`). Server `DoHurt` bỏ qua khi: sai subworld/region (`S/KNpc.cpp:2967-2970`), `m_nImmortal > 0` (:2973), `m_Doing ∈ {do_hurt, do_death, do_revive, do_runattack}` (:2976), `m_IgnoreNegativeState.nValue[1] > 1` (:2986), và **xác suất**: `!g_RandPercent(nHurtI/2 + 50 − giam_tho_thuong/2)` ⇒ return (:2989-3002; `giam_tho_thuong = min(80, (m_CurrentHitRecover/10)*10)`). Và `bDoHurt==0` ⇒ không gọi (`:5746`). Một số nhánh sét/lạnh đặt `bDoHurt=false` (`:4647,4653,4730`).
- Với `DoHurt=80` và `HitRecover` = 50 (cột NpcS của ani001) ⇒ xác suất = 80/2 + 50 − 50/2 = **65%** (tính tay từ công thức; mapping `m_CurrentHitRecover` ← cột `HitRecover` là HYPOTHESIS).

### A5. Hit có bị ngắt khi nhận thêm đòn? [CONFIRMED]
Không. Khi đang `do_hurt`, đòn mới: máu vẫn trừ nhưng `DoHurt` trả về ngay (client `:1631`, server `:2976`) ⇒ **không phát lại, không nối tiếp, không kéo dài**; animation hiện tại chạy hết (`OnHurt` → `WaitForFrame()` → `DoStand()`, `C/KNpc.cpp:1823-1830`). Đòn nhận trong lúc Hit chỉ hiện số (mục C).

### A6. Nhiều đạn va chạm gần như đồng thời [CONFIRMED logic, HYPOTHESIS thực nghiệm]
- Server xử lý tuần tự trong cùng tick: đòn đầu có thể (nếu `bDoHurt≠0` và qua xác suất) đặt `do_hurt`; các đòn sau cùng tick bị chặn bởi `m_Doing == do_hurt`. Với 375 (`DoHurt=0`) không có Hit nào.
- Client: số đòn/gói không cộng dồn animation; trạng thái Hit nếu đã có thì giữ.
- Giới hạn: không mô phỏng chạy thật.

---
## B. Animation Hit (Wound) của ani001

- Chọn sprite: với quái thường (`NPC_RES_NORMAL`) `KNpcResNode::GetActNo` trả thẳng `nDoing` (`C/KNpcResNode.cpp:594-596`): chỉ số hành động = `m_ClientDoing` = `cdo_hurt` (= 7 trong enum `CLIENTACTION`, `C/KNpc.h:104-122`). Tên hành động lấy từ `npc动作表.txt` (`CoreUseNameDef.h:49`; `KNpcResNode.cpp:437-456`) – **nội dung/thứ tự file này chưa đọc ⇒ UNKNOWN** thứ tự thật; báo cáo 51/55 ghi ani001 có hành động "Wound" nên **HYPOTHESIS: Wound = chỉ số 7 = file `ani001_bat.spr`**.
- Dữ liệu [TESTED/đọc bảng; `out_monster_compare.txt`]: `Wound=64,8,75` ⇒ 64 khung, 8 hướng ⇒ **8 khung mỗi hướng**; interval header 75 (không dùng cho NPC, mục A5 báo cáo 55). Sprite `bat` đã giải mã đúng (báo cáo 55).
- Thời gian phát [CONFIRMED + HYPOTHESIS]: client dùng `nFrames` từ gói server làm `nTotalFrame` (`C/KProtocolProcess.cpp:617` → `DoHurt(nFrames,…)`). Server: `nTotalFrame = 18*HurtFrame*nHurtI*(100−giam)/100000` (`S/KNpc.cpp:3008`, số nguyên cắt cụt). Với ani001 `HurtFrame=12` (hàng 1) hoặc `10` (hàng 2), `nHurtI=80`, `giam=50`: 18·12·80·50/100000 = 8,64 → **8 khung** (hàng 2: 7,2 → **7 khung**) (tính tay; mapping HitRecover là HYPOTHESIS). Hoạt ảnh Wound (8 khung/hướng) kéo giãn theo `nCurFrame/nAllFrame` (báo cáo 55 mục A5) ⇒ khớp ≈ 1 khung sprite / khung logic. Quy ra giây (7–8 khung) ≈ 0,4–0,45 s nếu 18 Hz (HYPOTHESIS).
- Hướng: dùng hướng hiện tại của NPC (`m_Dir`), 8 hướng như các action khác (báo cáo 55 mục C). Hit không đổi `m_Dir`.
- Có bị ngắt bởi Attack/Move/Death? [CONFIRMED trong mã]:
  - Trong Hit, NPC **không thể phát skill/đánh**: `DoSkill` return nếu `m_Doing == do_hurt` (`C/KNpc.cpp:2202`); AI bị khóa vì `m_ProcessAI = 0` (:1636) cho tới khi Hit xong (`m_ProcessAI = 1`, :1829); đi bộ/chạy chỉ cho phép khi `m_Doing ∈ {walk, run, hurt, runattack}` (`C/KNpc.cpp:3259`, nghĩa là lệnh di chuyển được xử lý có điều kiện – ý nghĩa chính xác chưa đọc hết ⇒ HYPOTHESIS: Move không ngắt Hit).
  - **Death ưu tiên hơn Hit**: client `DoDeath` chỉ chặn khi `m_Doing == do_death` (`C/KNpc.cpp:1319-1320`) rồi đặt `m_Doing = do_death` (:1344) bất kể đang Hit; server `CalcDamage` gọi `DoHurt` rồi (nếu máu ≤ 0) `DoDeath` ngay trong cùng hàm (`S/KNpc.cpp:5746-5762`), `DoDeath` chỉ chặn `m_Doing==do_death` (`S/KNpc.cpp:2429-2430`). Ngược lại Hit không thể ghi đè Death (`DoHurt` chặn `do_death`).
- Nhiều đòn liên tiếp: **ghi đè không xảy ra; đòn thêm bị bỏ qua cho animation** (A5).
- Đẩy lùi: `OnHurt` nội suy vị trí tới `(m_nHurtDesX, m_nHurtDesY)`; server gửi chính vị trí hiện tại (`GetMpsPos`, `S/KNpc.cpp:3033`; sau đó có bảng `POff[8]` :3035-3045 – phần dùng chưa đọc) ⇒ **UNKNOWN** có đẩy lùi thật hay không với quái.

### Đề xuất tái hiện trong Unity (phân loại)
| Nội dung | Loại |
|---|---|
| Hit chỉ bắt đầu theo sự kiện "nhận sát thương có cờ Hit"; không bắt đầu từ va chạm đạn | QUY TẮC GỐC (A1–A2) |
| Đang Hit/Death thì không bắt đầu Hit mới; Death ghi đè Hit; Hit không kéo dài khi nhận thêm | QUY TẮC GỐC (A4–A5) |
| Trong Hit quái không đánh/di chuyển tự chủ | QUY TẮC GỐC (khóa AI) |
| Skill 375 (`DoHurt=0`) **không** phát Wound của ani001 | QUY TẮC GỐC theo nguồn; **DESIGN DECISION cần chốt**: để đúng gốc (không Hit) hay thêm Hit để dễ nhìn |
| Hit 8 khung ≈ 0,45 s, xác suất 65% với đòn thường | CHỈ nếu U003 có đòn thường vào quái; chưa thuộc phạm vi |
| Nếu thêm Hit cho 375: một lần/mỗi trạng thái Hit, bỏ qua đòn khi đang Hit, Death ưu tiên, độ dài Hit = 8 khung ×(1/18 s) | **DESIGN DECISION** (đề xuất, đánh dấu rõ không phải gốc) |

---
## C. Damage number (con số bay) của client gốc

- **Nguồn dữ liệu** [CONFIRMED]: NPC thường/đồng hành (`kind_normal`/`kind_partner`): hiệu số máu giữa hai lần đồng bộ `SyncNpcMin`: `if (nOldLife − m_CurrentLife > 0) Npc.SetBlood(nOldLife − m_CurrentLife)` (`C/KProtocolProcess.cpp:2524-2547`; máu mới = `LifeMax × nLifeDamagePerCent / 1000`, :2531-2534). Lúc chết: `SetBlood(m_CurrentLife)` trong `DoDeath` (`C/KNpc.cpp:1339-1340`) — con số hiển thị lúc chết là **máu còn lại tại thời điểm đó** (đọc thẳng mã, ý nghĩa gameplay chưa kiểm). ⇒ số hiển thị = tổng máu mất giữa hai gói, **không phải từng đòn riêng** (nhiều đòn giữa hai gói gộp một số). Sát thương server không gửi riêng từng đòn (chưa thấy gói số damage riêng trong `KProtocolDef.h`).
- **Vị trí** [CONFIRMED]: `KNpc::PaintBlood` (`C/KNpc.cpp:10362-10429`) gọi `DrawPrimitives_NpcBlood(..., nMpsX, nMpsY, nHeightOff)`; `nHeightOffset = GetNpcPate()/4` (:10364-10369); nhãn đặt tại `(screenX(mps), visibleSize.height − screenY + nOffsetY)` (`C/../gamescene/KgameWorld.cpp:9267-9269`). Tức: ngay trên quái theo cao độ `Pate/4`, căn theo gốc nhãn BMFont (anchor mặc định).
- **Font/màu** [CONFIRMED + TESTED xem ảnh]: `CCLabelBMFont::create(str, "fonts/number_16_r.fnt")` (`KgameWorld.cpp:9259`); file `Resources/fonts/number_16_r.fnt`+`.png` (128×20, 12 ký tự: `.`, `/`, `0–9`, mỗi glyph 8×18, `size=16`); ảnh PNG cho thấy chữ số đỏ viền tối. Không có glyph `-`/`+`. `setColor` bị comment (:9265). Hằng `SHOW_BLOOD_COLOR 0x00ff0000` thuộc bản vẽ chữ cũ nằm trong khối comment (`C/KNpc.cpp:62, 10228-10287`) — không dùng. **Không tự nhận font khác là gốc.**
- **Chuyển động** [CONFIRMED]: `nHeightOff = nHeightOffset + i*BLOOD_LAYER_SPACING(12) + (defMAX_SHOW_BLOOD_TIME(50) − t) * defSHOW_BLOOD_MOVE_SPEED(0.1)` (`C/KNpc.cpp:10404`, hằng :63-65) với `i` = chỉ số tầng, `t` = bộ đếm còn lại ⇒ bay lên đều 0,1 đơn vị mỗi lần vẽ, tổng 5 đơn vị (50 lần vẽ) – **rất nhỏ** (int hoá khi truyền vào hàm: `int nOffsetY` ⇒ phần lẻ bị cắt, có thể gần như đứng yên; HYPOTHESIS). Không có hiệu ứng mờ/phóng to trong đường vẽ đang dùng (alpha chỉ trong khối comment).
- **Thời gian tồn tại** [CONFIRMED, đơn vị là số lần gọi `PaintBlood`]: `m_nBloodNo[i][1] = defMAX_SHOW_BLOOD_TIME (50)`, giảm 1 mỗi lần `PaintBlood` được gọi (:10413-10421), gọi từ vòng vẽ NPC (`C/CoreDrawGameObj.cpp:93`) ⇒ **phụ thuộc số lần vẽ cây hiển thị, không phải đồng hồ cố định** (≈ 50 khung hình; nếu 60 fps ≈ 0,83 s; HYPOTHESIS cho tốc độ vẽ thực của client).
- **Nhiều số cùng lúc** [CONFIRMED]: `defMAX_SHOW_BLOOD_NUM = 5` (`C/KNpc.h:25`); `SetBlood` (bản đang dùng, `C/KNpc.cpp:10320-10349`) đẩy các số cũ xuống một tầng (index tăng) rồi ghi số mới vào tầng 0; nếu đầy 5 thì số cũ nhất bị đẩy mất; mỗi tầng cách nhau 12 đơn vị cao độ ⇒ **số mới nằm ở tầng 0 (thấp nhất), số cũ bị đẩy lên cao dần**. Nhãn có tag `bloodindex+1`, cùng cha theo NPC (`blood_<npcIdx>`). Chồng lấn: không có luật tránh chồng khác ngoài khoảng cách 12.
- **Chỉ cho quái/đồng hành**: `PaintBlood` trả về ngay cho người chơi/`kind_dialoger` (`C/KNpc.cpp:10366-10367`) ⇒ người chơi không có số damage kiểu này. UNKNOWN: có cơ chế khác (chat, UI thanh máu) hiển thị sát thương của người chơi.
- **U003** (luật đã chốt): mỗi lần nhận sát thương một số, không gộp. Khác gốc (gốc gộp theo gói đồng bộ). ⇒ **DESIGN DECISION**: dùng số riêng từng lần nhận (U003 là nguồn sự thật tức thời, không có gói đồng bộ). Phần tái hiện từ gốc: font bitmap số đỏ 8×18 (có thể dùng lại PNG/fnt như asset tham chiếu, cần duyệt dùng asset), bay lên nhẹ, tối đa ~5 số/quái cùng lúc xếp tầng, hết bằng thời gian.

---
## D. Luật Combat U003 (đã chốt, giữ nguyên – DESIGN DECISION)

**Skill 375 – Lôi Động Cửu Thiên**
1. Một lần cast tạo **16 missile 181 theo bố trí 4×4** (nguồn gốc: CONFIRMED báo cáo 55 mục D2.3, `__CastFixed`/`CastZone`, ô 32×32).
2. **Độ trễ xuất hiện theo dữ liệu gốc** (RANDONORDER: `WaitTime(2) + k*5 + (rand(2)==1 ? +rand(5) : −rand(2))` khung, k=0..15; CONFIRMED báo cáo 55; `nWaitTime` ban đầu UNKNOWN).
3. Missile 181 va chạm ⇒ tạo missile 193 **tại vị trí va chạm** (CONFIRMED báo cáo 55).
4. **Mỗi vị trí nổ tạo một vùng AOE độc lập**; **vùng AOE chồng lấn được phép cộng dồn sát thương**.
5. Mỗi vùng gây **hai tick**: tick 1 = **500 ms** sau khi vùng kích hoạt; tick 2 = **1000 ms** sau khi vùng kích hoạt.
6. Mỗi tick **20 sát thương** cho **mỗi quái còn sống** trong vùng; kiểm tra quái độc lập tại từng thời điểm tick.
7. Quái nằm trong nhiều vùng cùng thời điểm tick nhận sát thương từ **tất cả** các vùng đó.
8. **Cast 1 s**; **cooldown 1 s tính từ lúc bắt đầu cast**; cooldown kết thúc cùng lúc cast hoàn tất.

**Quái kiểm thử**: ani001; **HP kiểm thử 1.000** (đổi từ 100 ở thiết kế cũ; chỉ là cấu hình kiểm thử, không phải cân bằng cuối); HP về 0 ⇒ Death; respawn ⇒ Idle (respawn 2 s đã chốt trước đó).
**Damage number**: mỗi lần nhận sát thương một số tại vị trí quái; nhiều vùng cùng gây sát thương ⇒ hiển thị từng lần; **không gộp** trong giai đoạn kiểm thử.
**Không thêm** quy tắc animation Hit vào U003 khi chưa xác minh: kết quả mục B cho thấy gốc KHÔNG phát Hit với skill 375 ⇒ **U003 mặc định không có Hit cho 375**; nếu muốn có Hit, đó là DESIGN DECISION riêng (mục 10).

Ghi chú tính toán (hệ quả của luật, không đổi luật): tối đa số tick/quái trong một lần cast = 2 × số vùng chứa quái; tối đa 16 vùng ⇒ ≤ 32 tick = 640 sát thương/quái nếu quái nằm trong mọi vùng ở cả hai tick; với HP 1.000 quái chưa chết sau một cast. [tính tay từ luật; không có mô phỏng]

---
## E. Đối chiếu nhất quán với báo cáo 51–55 và `BAI_HOC.md`
Không xóa lịch sử; các kết luận cũ bị thay thế (nguồn đúng = báo cáo 55 và 56):
| Vị trí cũ | Kết luận cũ | Thay thế | Lý do/bằng chứng |
|---|---|---|---|
| BC 51 dòng 57 (`ChildSkillId=181 x4`); BC 52 dòng 73 ("missle 181 x4"); BC 54 dòng 157, 206 ("4 missile 181") | 4 đạn | **16 đạn (4×4)** | `CastZone` lặp `i,j` trong `ChildSkillNum`², `KSkills.cpp:1695-1837` (BC 55 D2.3) |
| BC 54 (tâm nổ/193 "khi chạm" chưa nói vị trí) | 193 vị trí chưa rõ | **193 sinh tại vị trí đạn 181 vừa va chạm** | `SKILL_SLT_Missle`, `KSkills.cpp:1511-1523, 1737-1741` (BC 55 D2.6) |
| BC 52 dòng 8: "UI cooldown trên nút skill chưa tìm thấy" | chưa thấy | UI cooldown gốc CÓ (`timeLoopLayer`, `KgameWorld.cpp:5527-5540`), đã sửa ở BC 53; **với skill 375 `TimePerCast=0` ⇒ `NextCastTime = now + 0` (`KNpc.cpp:2259-2264`) nên vòng cooldown gốc không có độ dài để hiển thị** (HYPOTHESIS-cao, suy từ mã, chưa chạy client) | BC 52 dòng 33, BC 53 dòng 9 |
| BC 54 dòng 24, 161 (cooldown "chưa chốt từ đầu hay cuối cast") | chưa chốt | **chốt**: 1 s từ lúc bắt đầu cast, kết thúc cùng lúc cast xong | quyết định ChatGPT (mục D); là DESIGN DECISION, không phải gốc |
| BC 54 B2 (HP quái 100, tick 500/1000) | HP 100 | **HP kiểm thử 1.000** | quyết định ChatGPT (mục D) |
| BC 52 dòng 28 (`DmgInterval=10/4` ý nghĩa chưa rõ), BC 55 D2.7 ("UNKNOWN phía server") | UNKNOWN | Server dùng `DmgInterval` làm khoảng chặn gây sát thương mỗi missile (`S/KMissle.cpp:1788-1796`); đơn vị HYPOTHESIS khung game | mục A3 |
| BC 55 D2.8 ("sát thương thực UNKNOWN") | UNKNOWN | một phần: Hit phụ thuộc `DoHurt` (375/387 = 0) và sát thương gắn Attrib 1002 của 375 (HYPOTHESIS: đến từ 181) | mục A2–A3 |
| BC 55 mục B2 "AddPointLeafToList…": không liên quan | — | không đổi | — |
- Phản biện nội bộ (không phải lỗi, để rõ ràng): BC 53 nêu "UI cooldown gốc CÓ", yêu cầu hiện tại nêu "gốc không có vòng cooldown vì TimePerCast=0". Hai điều **không mâu thuẫn**: cơ chế UI tồn tại (CONFIRMED) nhưng với skill 375 không có khoảng cooldown nên vòng không có thời gian đáng kể (suy luận, chưa TESTED bằng chạy client). Ghi vào `BAI_HOC.md`.
- Đã cập nhật `docs-analysis/BAI_HOC.md` (mục "U003 G0.6").

---
## 1–7. Trả lời các câu hỏi cuối
1. **Skill 375 có kích hoạt Hit của quái không?** Theo mã client: không (client không gọi Hit từ va chạm đạn, A1). Theo nguồn server + dữ liệu: không (`DoHurt=0` ở skill 375 và 387, A2). Giới hạn: chưa kiểm exe server thật hay chạy thử.
2. **Animation Hit có bị ngắt bởi đòn liên tiếp không?** Không bị ngắt/khởi động lại; đòn thêm bị bỏ qua cho animation (A5) [CONFIRMED trong mã].
3. **Death có ưu tiên hơn Hit không?** Có: Death ghi đè Hit (client `:1319-1344`, server `:2429-2430, 5746-5762`); Hit không ghi đè Death (B).
4. **Damage number gốc?** Số đỏ bitmap từ font `number_16_r.fnt`, sinh từ hiệu số máu giữa hai gói đồng bộ (gộp nhiều đòn), bay lên nhẹ, tối đa 5 tầng/quái, tồn tại 50 lần vẽ, chỉ cho quái/đồng hành (mục C).
5. **Cần tái hiện từ gốc:** chuỗi hiệu ứng 375 (cast kl_16, 16 đạn 4×4 trễ gốc, 181→193 tại vị trí va chạm, Bz_dian3); quy tắc trạng thái (Death > Hit, Hit không chồng, khóa AI); font số + kiểu xếp tầng; Death và respawn→Idle theo luật đã chốt.
6. **Phải tự xây (DESIGN DECISION/không có trong client):** toàn bộ tính sát thương (client gốc không tính), luật AOE tick 500/1000 ms, kiểm soát cooldown/cast 1 s, HP kiểm thử 1.000, số damage từng lần (gốc gộp), quyết định có phát Hit cho 375 hay không, thời gian respawn, đồng hồ mô phỏng.
7. **Combat architecture đủ điều kiện triển khai chưa?** **Đủ cho giai đoạn prototype Unity**, với điều kiện: (a) chốt mục 10, (b) giữ nguyên các UNKNOWN còn lại nêu rõ trong tài liệu, (c) vẫn phải qua các test bắt buộc ở báo cáo 55 mục 4 (SPR, hướng, cây che khuất, đồng hồ). Chưa đủ để tuyên bố "khớp gốc" cho Hit/animation Wound (tên action chưa kiểm).

## 8. UNKNOWN còn lại
1. Nội dung/thứ tự `npc动作表.txt` ⇒ chỉ số/tên thật của "Wound" cho ani001 (B).
2. Hz client thật (18 Hz?) và tốc độ vẽ ⇒ thời lượng giây của Hit, số damage, 193.
3. `Attrib 1002` và `kunlun.lua` cụ thể ⇒ nguồn sát thương 181/193 thực.
4. Đơn vị `GetGameTime` cho `DmgInterval`.
5. Có đẩy lùi quái khi Hit (`POff[8]` server dùng thế nào).
6. Ánh xạ cột `HitRecover` → `m_CurrentHitRecover` cho quái.
7. Hiển thị sát thương của người chơi (client chỉ cho quái/đồng hành).
8. Exe server chạy thật có khớp nguồn không.

## 9. DESIGN DECISION đề xuất để đưa vào tài liệu thiết kế
- **Kiến trúc**: lớp `CombatSim` (đồng hồ cố định) sở hữu HP/tick/AOE; lớp `NpcState` (Stand/Hit?/Death/Idle) tách biệt; lớp `DamageNumberView` nhận sự kiện `DamageApplied(npc, amount, time)` – mỗi sự kiện một số.
- **Hit cho 375**: mặc định KHÔNG (đúng gốc); cờ cấu hình `hitOnSkill375=false`, nếu bật: quy tắc Hit gốc (không chồng, Death ưu tiên, 8 khung).
- **Damage number**: dùng sự kiện từng tick; xếp tầng giống gốc (tối đa 5 tầng/quái, tầng mới thấp nhất, 12 đơn vị/tầng), thời gian sống theo thời gian thực (DESIGN, không theo "50 lần vẽ").
- **Kiểm thử**: log CSV sự kiện (thời điểm cast, từng 181/193, từng tick, HP) và kiểm tra luật D bằng test không giao diện ở FPS 15/30/60/144.

## 10. Cần tôi quyết định: có
1. Skill 375 có phát animation Hit (Wound) cho ani001 không? (Gốc: không. Đề xuất: **không**, giữ đúng gốc; cờ cấu hình để bật sau.)
2. Có dùng lại font `number_16_r` (đỏ, 8×18) làm tham chiếu cho damage number Unity không, hay chỉ tái tạo kiểu tương tự bằng font tự tạo? (Đề xuất: tự tạo font số riêng, giữ kiểu màu đỏ và xếp tầng.)
3. Có cho phép đọc thêm `npc动作表.txt`, `Attrib 1002`/`kunlun.lua` (chỉ đọc) để đóng UNKNOWN 1 và 3 trước khi khóa thiết kế?
