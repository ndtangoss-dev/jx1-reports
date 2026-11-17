TÓM TẮT 1: [NGUỒN] Phái thứ 5–8 theo danh sách là Nga My [4], Thúy Yên [5], Cái Bang [6], Thiên Nhẫn [7]; không nhầm số thứ tự với faction ID (G/Settings/faction/faction.ini:33–59).
TÓM TẮT 2: [NGUỒN] Có catalog SkillId/tên/ReqLevel/MaxLevel/EqtLimit/HorseLimit và mục tiêu bên dưới; skill phụ, alias và bản ghi dùng chung script được ghi riêng, không coi tên chiêu là khóa duy nhất.
TÓM TẮT 3: [NGUỒN] Partner có đường cast chung, nhưng phải có skill trong danh sách và level dương; SetActiveSkill nhận chỉ số slot, không phải SkillId (S/KNpc.cpp:7337–7358,3609–3674,4016).
TÓM TẮT 4: [NGUỒN] Kiểm vũ khí/ngựa chỉ nằm trong IsPlayer; Cost trả TRUE ngay cho non-player, nên không áp ngân sách mana/máu/thể lực của player lên partner theo đường này (S/KSkills.cpp:267–358; S/KNpc.cpp:7002–7005,15465–15474).
TÓM TẮT 5: [CHƯA KIỂM] Chưa chứng minh AI tự chọn đủ chiêu, luật học của partner, hiệu lực từng modifier hay AOE cuối cùng; không chạy build/test/runtime/VM/network/exe và không sửa source.

# A-15b — Kỹ năng phái 5–8 cho NPC hảo hữu

Ngày khảo sát: 17/11/2026. Trạng thái: **DONE cho khảo sát tĩnh trong phạm vi bằng chứng**, không phải xác nhận kỹ năng hoạt động trong game. Đã đọc A-12 và A-14 theo task. Chỉ tạo báo cáo này và thêm mục Kết quả trong task A-15b.

## Nguồn và quy ước

| Tiền tố | Gốc chỉ đọc |
| --- | --- |
| S/ | `D:/JX-source/server/jxOnline/gameserver/Sources/Core/Src/` |
| H/ | `D:/JX-source/server/jxOnline/header/` |
| G/ | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/` |

Đường `D:/JX-source/SwordOnline` được task nêu không tồn tại. Dùng nguồn server D: đã được A-14 chỉ ra; dữ liệu server rời G: được A-12 chỉ ra. Không trộn số dòng source canonical C: của A-12 với source D: hiện tại. **[CHƯA KIỂM] Hai gốc source/data có khớp bản đang triển khai hay không.** Chỉ dùng chúng làm bằng chứng tĩnh riêng biệt.

Số dòng vật lý từ 1. Source đọc CP936; tên Việt trong bảng là TCVN3 được chuyển sang Unicode để đọc, giữ nguyên SkillId và khóa Lua ASCII; hậu tố `##`, `11`, `npc`, `abc`, `ncp` không tự xóa. Nhãn đã hỏng/thiếu ngay trong data không tự phục dựng. Mỗi dòng catalog có `Skills.txt:<dòng>` để kiểm lại bytes gốc. Không lấy số dòng trừ 1 làm SkillId: ví dụ ID 712 ở dòng 714, ID 1601 ở dòng 1590. Loader lưu riêng SkillId và tab row tại S/KSkillManager.cpp:65–74,126–135; KSkills đọc SkillId tại :2979.

## 1. Chốt thứ tự phái

| Thứ tự (đếm từ 1) | Section/faction ID trong file | Phái | Ngũ hành | Bằng chứng |
| --- | --- | --- | --- | --- |
| 1–4 | [0]–[3] | Thiếu Lâm, Thiên Vương, Đường Môn, Ngũ Độc | Kim, Kim, Mộc, Mộc | G/Settings/faction/faction.ini:5–31 |
| 5 | [4] | Nga My / Nga Mi (`emei`) | Thủy | G/Settings/faction/faction.ini:33–38; MonPhai.ini:26–29 |
| 6 | [5] | Thúy Yên (`cuiyan`) | Thủy | G/Settings/faction/faction.ini:40–45; MonPhai.ini:31–34 |
| 7 | [6] | Cái Bang (`gaibang`) | Hỏa | G/Settings/faction/faction.ini:47–52; MonPhai.ini:36–39 |
| 8 | [7] | Thiên Nhẫn (`tianren`) | Hỏa | G/Settings/faction/faction.ini:54–59; MonPhai.ini:41–44 |
| 9 trở đi | [8]… | Có Võ Đang, Côn Lôn và các section tiếp theo | Ngoài phạm vi | G/Settings/faction/faction.ini:61–106 |

Số 8 không phải cuối danh sách, vì vậy dừng ở Thiên Nhẫn, không mở rộng sang phái 9+. Đường file chuẩn được định nghĩa H/CoreUseNameDef.h:76 (`FACTION_FILE`), :139 (`SKILL_SETTING_FILE`). Không tìm thấy file tên `*FactionSkill*` trong đúng cây G/Settings đã kiểm; không suy từ đó rằng không có bảng trong PAK hay nguồn khác. KPlayerFaction::OpenCurSkillLevel trả TRUE ở S/KPlayerFaction.cpp:107, phần thêm skill theo phái :108–138 là comment, không dùng làm đường học đang chạy.

## 2. Điều kiện học/dùng và kiểm cast kind_partner

| Mã | Kết luận tĩnh và điều kiện | File:dòng |
| --- | --- | --- |
| C0 | AddTongBan gắn `kind_partner`, owner và camp; không tự gán toàn bộ skill môn phái chỉ vì đặt kind. | S/KNpcSet.cpp:858–893 |
| C1 | SkillId phải có trong KSkillList, slot hợp lệ, CurrentSkillLevel dương; Add kiểm ID/level/capacity và lấy skill từ manager. `SetActiveSkill(nSkillIdx)` nhận **slot danh sách**, không nhận ID. | S/KSkillList.cpp:406–416,498–566; S/KNpc.cpp:7337–7358 |
| C2 | DoSkill kiểm subworld/region, trạng thái đang skill/hurt, hồi chiêu thường và trên ngựa, CanCastByIndex và CanCastSkill. CanCastByIndex kiểm current level > 0 và NextCastTime. | S/KNpc.cpp:3609–3674; S/KSkillList.cpp:879–887 |
| C3 | Mục tiêu NPC dùng `nParam1=-1,nParam2=NpcIndex`, phải phù hợp enemy/ally/self/dialog. Cast còn kiểm launcher/target cùng subworld. Với TargetSelf và tọa độ đầu vào, CanCastSkill đổi sang chính caster rồi return sớm. | S/KSkills.cpp:224–260,470–481 |
| C4 | Nhánh kiểm EqtLimit/HorseLimit chỉ dành IsPlayer; server IsPlayer đòi kind_player. Partner không bị hai kiểm này tại CanCastSkill/NewCanCastSkill. Dữ liệu E/H bên dưới vẫn cần cho thiết kế, không bảo đảm animation/weapon của partner tương thích. | S/KSkills.cpp:267–358,362–427; S/KNpc.cpp:15465–15474 |
| C5 | Cost được gọi trong DoSkill, nhưng `if (!IsPlayer()) return TRUE`; không kiểm/trừ mana, life, stamina cho partner tại hàm này. Giá trị CostValue=0 trên bảng không có nghĩa skill miễn phí cho player: Lua có skill_cost_v, ví dụ emei.lua:36, cuiyan.lua:37, gaibang.lua:41, tianren.lua:24. | S/KNpc.cpp:3673–3674,7002–7069; G/script/skill/{bốn file vừa nêu} |
| C6 | DoSkill nhận style 0/1/2/3 vào DoOrdinSkill, OnSkill gọi Cast; Cast dispatch đạn, active state, passive state. Không thấy guard riêng cấm kind_partner ở các đoạn này. Đây là **đường có thể đi tới cast**, không xác nhận từng chiêu thành công. | S/KNpc.cpp:3748–3761,3779–3838,4006–4016; S/KSkills.cpp:456–550 |
| C7 | Passive style 3 được Cast khi Add với level dương/NewCanCastSkill cho phép; CastPassivitySkill chỉ áp nếu có state attrib. Hiệu lực từng handler lên partner cần rà riêng, như cảnh báo player-only từ A-12/A-14. | S/KSkillList.cpp:477–488,549–559; S/KSkills.cpp:3462–3472 |
| C8 | Style 4 không nằm trong nhánh ordin của DoSkill; nhánh CreateNpc của Cast có lời gọi bị comment. Không chọn ID 106 làm kỹ năng khả dụng chỉ vì tên giống Băng Tung Vô Ảnh. Style 14 cũng không thuộc tập loader ordin 0–3 đã kiểm. | S/KNpc.cpp:3748–3761; S/KSkills.cpp:555–558; S/KSkillManager.cpp:165–190 |
| H | ReqLevel là mức dùng cho **nâng skill player**, không phải gate cast của partner: loader :2981–2983, nhánh tăng player so level hiện tại và giới hạn điểm/max. [CHƯA KIỂM] Nhiệm vụ gia nhập, bí kíp, tiền/điểm, prerequisite từng chiêu, cách học/lưu skill cho partner. Không áp máy móc luật học player cho con. | S/KSkills.cpp:2981–2986; S/KPlayer.cpp:5510–5545 |

**Điều kiện chung cho mọi dòng**: C1–C6 với skill chủ động; C1/C4/C7 với passive; C8 loại khỏi danh sách lựa chọn thông thường. C3 tùy cờ mục tiêu trong từng dòng. Không coi việc đổi faction/series của chủ hoặc con là đã học kỹ năng. Không gọi Cast trực tiếp để bỏ C2/C3: kiểm CanCastSkill trong chính KSkill::Cast ở :459–460 đang bị comment.

`Req/Max` là hai cột gốc, không phải cấp con đã được thực thi. `E/H` là EqtLimit/HorseLimit: E=-2 không hạn chế, -1 tay không, 0/1/2/3 là mã vũ khí; không đổi thành tên đồ nếu chưa đối chiếu enum. H=0 không hạn chế, 1 cấm ngựa, 2 bắt buộc ngựa (S/KSkills.cpp:279–335). Với partner xem C4. `E/A/S` là TargetEnemy/TargetAlly/TargetSelf, không phải quan hệ owner đã xác nhận runtime.

Phân loại dưới đây là **nhãn thiết kế từ data tĩnh**. `Hỗ trợ` gồm buff/heal/passive và debuff lên địch; `Đánh đơn*` là cấu hình phát một đạn, **[CHƯA KIỂM] chỉ trúng một mục tiêu**; `AOE*` là phát nhiều đạn theo hình/tại vùng, **[CHƯA KIỂM] số mục tiêu, bán kính, va chạm và event cuối**. Một đạn có thể gây AOE hoặc gọi event, vì vậy không suy AOE hoàn chỉnh từ SkillStyle hay tên. Form 0/1/2/3/5/6/7 lần lượt tường/đường/tỏa/tròn/vùng/tại đích/tại caster (S/SkillDef.h:118–128; S/KSkills.cpp:1596–1642). Mỗi dòng ghi form/số đạn/child thô để tránh che mất giới hạn này; ChildSkillId chưa được đồng nhất với SkillId của chiêu học.

## 3. Bảng kỹ năng theo phái

Catalog đối chiếu các cụm tên cơ sở và `LvlSetScript` trỏ đúng bốn phái, kể cả thư mục con. Các bản ghi không có ánh xạ phái chắc chắn được giữ trong phụ lục để tránh gán nhầm; **[CHƯA KIỂM] catalog học chính thức/đang mở từ FactionSkill hoặc script gia nhập**. `Attrib`/CharClass không đủ làm khóa phái duy nhất: Hoa Sơn/skill boss có thể dùng lại Attrib 501/503/801. Không dùng chúng để mở rộng catalog.

### 5 — Nga My (emei) — 49 bản ghi

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 77 | Nga Mi Kiếm pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | 0/0 | 0/0/0 | 7/0/0 | emei_jianfa | Skills.txt:78 |
| 78 | Tiếp Dẫn Kiếm pháp (##) | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | — | Skills.txt:79 |
| 79 | Nga Mi Chưởng pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | emei_zhangfa | Skills.txt:80 |
| 80 | Phiêu Tuyết Xuyên Vân | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | -2/0 | 1/0/0 | 1/1/68 | piaoyun_chuanxue | Skills.txt:81 |
| 81 | Thu Phong Diệp | Hỗ trợ | 2; 1 | 10/20 | -2/0 | 0/0/1 | 7/1/204 | staminareplenish_v | Skills.txt:82 |
| 82 | Tứ Tượng Đồng Quy | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 30/20 | -2/1 | 1/0/0 | 6/1/101 | sixiang_tonggui | Skills.txt:83 |
| 83 | Vọng Nguyệt | Hỗ trợ | 2; 1 | 20/20 | -2/0 | 0/1/1 | 7/1/205 | lifereplenish_v | Skills.txt:84 |
| 84 | Phong Vũ Phiêu Hương | Hỗ trợ: debuff địch | 2; 0 | 20/20 | -2/0 | 1/0/0 | 6/0/0 | slowmissle_b | Skills.txt:85 |
| 85 | Nhất Diệp Tri Thu | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | 0/1 | 1/0/0 | 1/1/2 | yiye_zhiqiu | Skills.txt:86 |
| 86 | Lưu Thủy | Hỗ trợ | 2; 1 | 40/20 | -2/0 | 0/1/1 | 7/1/206 | liushui | Skills.txt:87 |
| 87 | Băng Tâm Quyết | Hỗ trợ: bị động | 3; 0 | 30/20 | -2/0 | 0/0/0 | 7/0/0 | coldres_p | Skills.txt:88 |
| 88 | Bất Diệt Bất Tuyệt | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 60/20 | 0/1 | 1/0/0 | 1/1/3 | bumie_bujue | Skills.txt:89 |
| 89 | Mộng Điệp | Hỗ trợ | 2; 1 | 30/20 | -2/0 | 0/1/1 | 7/1/207 | mengdie | Skills.txt:90 |
| 91 | Phật Quang Phổ Chiếu | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 60/20 | -2/1 | 1/0/0 | 7/1/4 | foguang_puzhao | Skills.txt:92 |
| 92 | Phật Tâm Từ Hữu | Hỗ trợ | 2; 1 | 50/20 | -2/0 | 0/1/1 | 7/1/208 | foxin_ciyou | Skills.txt:93 |
| 93 | Từ Hàng Phổ D | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 6/1/5 | cihang_pudu | Skills.txt:94 |
| 94 | Từ Hàng Phổ Độ11 | Hỗ trợ | 0; 0 | 0/20 | -2/0 | 0/1/1 | 5/1/5 | cihang_pudu | Skills.txt:95 |
| 188 | Bạch Ba | AOE* | 0; 0 | 50/20 | -2/0 | 1/0/0 | 3/32/81 | — | Skills.txt:189 |
| 204 | Thu Phong Diệp | Hỗ trợ | 0; 0 | 10/20 | -2/0 | 0/1/1 | 3/1/92 | staminareplenish_v | Skills.txt:205 |
| 205 | Vọng Nguyệt | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 3/1/92 | lifereplenish_v | Skills.txt:206 |
| 206 | Lưu Thủy | Hỗ trợ | 0; 0 | 30/20 | -2/0 | 0/1/1 | 3/1/92 | liushui | Skills.txt:207 |
| 207 | Mộng Điệp | Hỗ trợ | 0; 0 | 40/20 | -2/0 | 0/1/1 | 3/1/92 | mengdie | Skills.txt:208 |
| 208 | Phật Tâm Từ Hữu | Hỗ trợ | 0; 0 | 50/20 | -2/0 | 0/1/1 | 3/1/92 | foxin_ciyou | Skills.txt:209 |
| 212 | Thanh Tâm Phạn Âm | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 3/16/59 | badstatustimereduce_v | Skills.txt:213 |
| 243 | Tứ Tượng Đồng Quy | AOE* | 0; 0 | 20/20 | -2/1 | 1/0/0 | 3/4/1 | sixiang_tonggui | Skills.txt:244 |
| 246 | Bất Diệt Bất Tuyệt npc | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 40/20 | -2/1 | 1/0/0 | 1/1/103 | physicsenhance_p | Skills.txt:247 |
| 252 | Phật Pháp Vô Biên | Hỗ trợ: bị động | 3; 0 | 60/30 | -2/0 | 0/0/1 | 7/0/0 | fofa_wubian | Skills.txt:253 |
| 280 | Ba La Tâm Kinh | Hỗ trợ ally/self [CHƯA KIỂM hiệu ứng] | 2; 1 | 30/20 | -2/0 | 0/1/1 | 7/1/281 | stun_p | Skills.txt:281 |
| 281 | Ba La Tâm Kinh | Hỗ trợ | 0; 0 | 30/20 | -2/0 | 0/1/1 | 3/1/92 | qingyin_fanchang | Skills.txt:282 |
| 282 | Thanh Âm Phạn Xướng | Hỗ trợ | 2; 1 | 60/20 | -2/0 | 0/1/1 | 7/1/281 | qingyin_fanchang | Skills.txt:283 |
| 328 | Tam Nga Tề Tuyết | AOE* | 0; 0 | 80/20 | 0/1 | 1/0/0 | 0/3/142 | sane_jixue | Skills.txt:329 |
| 329 | Ngọc Tuyền Tẩy Trần | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 7/1/143 | yuquan_xichen | Skills.txt:330 |
| 330 | Thiên Phật Thiên Diệp | AOE* | 0; 0 | 80/20 | -2/1 | 1/0/0 | 3/32/145 | qianfo_qianye | Skills.txt:331 |
| 331 | Kim Đỉnh Phật Quang | AOE* | 0; 0 | 80/20 | -2/1 | 1/0/0 | 3/4/144 | jinding_foguang | Skills.txt:332 |
| 332 | Phổ Độ Chúng Sinh | Hỗ trợ | 2; 1 | 80/20 | -2/0 | 0/1/1 | 7/1/333 | pudu_zhongsheng | Skills.txt:333 |
| 333 | Phổ Độ Chúng Sinh | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 3/1/137 | pudu_zhongsheng | Skills.txt:334 |
| 334 | Thanh Âm Phạn Xướng 11 | Hỗ trợ | 2; 1 | 20/20 | -2/0 | 0/1/1 | 7/1/314 | qingyin_fanchang | Skills.txt:335 |
| 335 | Thanh Âm Phạn Xướng | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 3/1/92 | qingyin_fanchang | Skills.txt:336 |
| 380 | Phong Sương Toái ảnh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 6/1/186 | fengshuang_suiying | Skills.txt:381 |
| 385 | Thôi Song Vọng Nguyệt | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 30/20 | 0/1 | 1/0/0 | 1/1/191 | tuichuang_wangyue | Skills.txt:386 |
| 712 | Bế Nguyệt Phất Trần | Hỗ trợ | 2; 1 | 120/20 | -2/0 | 0/1/1 | 7/0/718 | emei120 | Skills.txt:714 |
| 718 | Kỹ năng phụ - Bế Nguyệt Phất Trần | Hỗ trợ | 0; 0 | 120/20 | -2/0 | 0/1/1 | 3/1/92 | emei120 | Skills.txt:720 |
| 1061 | Kiếm Hoa Vãn Tinh | AOE* | 0; 0 | 150/26 | 0/1 | 1/0/0 | 0/5/323 | jianemei150 | Skills.txt:1061 |
| 1062 | Băng Vũ Lạc Tinh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | -2/1 | 1/0/0 | 6/1/324 | zhangemei150 | Skills.txt:1062 |
| 1089 | Kiếm Tâm Tĩnh Điển | AOE* | 0; 0 | 0/20 | -2/0 | 1/0/0 | 3/8/325 | jianemei150_2 | Skills.txt:1089 |
| 1114 | Ngọc Tuyền Tâm Kinh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | -2/0 | 1/0/0 | 6/1/375 | fuzhuemei150 | Skills.txt:1114 |
| 1115 | Minh Tâm Kiến Tính | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 6/1/376 | cihang_pudu | Skills.txt:1115 |
| 1234 | Từ Hàng Phổ D | Hỗ trợ | 0; 0 | 120/20 | -2/0 | 0/1/1 | 7/1/5 | cihang_pudu | Skills.txt:1234 |
| 1601 | Tam Nga Tề Tuyết | AOE* | 0; 0 | 1/60 | -2/0 | 1/0/0 | 0/3/142 | sane_jixue | Skills.txt:1590 |

### 6 — Thúy Yên (cuiyan) — 35 bản ghi

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 95 | Thúy Yên Đao pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | 1/0 | 0/0/0 | 7/0/0 | cuiyan_daofa | Skills.txt:96 |
| 96 | Thúy Yên Kiếm pháp (##) | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | addphysicsdamage_p | Skills.txt:97 |
| 97 | Thúy Yên Song đao | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | cuiyan_shuangdao | Skills.txt:98 |
| 98 | Bích Yên kiếm pháp (##) | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | — | Skills.txt:99 |
| 99 | Phong Hoa Tuyết Nguyệt | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | 1/0 | 1/0/0 | 1/1/6 | fenghua_xueyue | Skills.txt:100 |
| 100 | Hộ Thể Hàn Băng | Hỗ trợ | 2; 0 | 40/20 | -2/0 | 0/0/1 | 7/0/0 | huti_hanbing | Skills.txt:101 |
| 101 | Trị liệu thuật | Hỗ trợ | 0; 0 | 10/20 | -2/0 | 0/1/1 | 6/1/13 | lifereplenish_v | Skills.txt:102 |
| 102 | Phong Quyển Tàn Tuyết | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | -2/1 | 1/0/0 | 1/1/7 | fengjuan_canxue | Skills.txt:103 |
| 103 | Thiên Lý Băng Phong | Hỗ trợ | 2; 0 | 20/20 | -2/0 | 0/0/1 | 7/0/0 | rangedamagereturn_v | Skills.txt:104 |
| 104 | Băng Hồn | Hỗ trợ: bị động | 3; 0 | 20/20 | -2/0 | 0/0/0 | 7/0/0 | fireres_p | Skills.txt:105 |
| 105 | Vũ Đả Lê Hoa | AOE* | 0; 0 | 30/20 | 1/1 | 1/0/0 | 6/4/8 | yuda_lihua | Skills.txt:106 |
| 106 | Băng Tung Vụ ảnh 111 | Hỗ trợ/triệu hồi [C8: không chọn] | 4; 0 | 30/20 | -2/0 | 0/0/0 | 1/0/0 | — | Skills.txt:107 |
| 107 | Nhiếp Tâm Thuật | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 30/20 | -2/0 | 1/0/0 | 1/1/6 | colddamage_v | Skills.txt:108 |
| 108 | Mục Dã Lưu Tinh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 60/20 | 1/1 | 1/0/0 | 6/1/9 | muye_liuxing | Skills.txt:109 |
| 109 | Tuyết ảnh | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | xueying | Skills.txt:110 |
| 110 | Ngũ hành độn | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 40/20 | -2/0 | 0/0/0 | 1/1/6 | colddamage_v | Skills.txt:111 |
| 111 | Bích Hải Triều Sinh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 60/20 | -2/1 | 1/0/0 | 7/1/10 | bihai_chaosheng | Skills.txt:112 |
| 112 | Bích Hải Triều Sinhb | AOE* | 0; 0 | 50/20 | -2/0 | 1/0/0 | 3/16/11 | bihai_chaosheng | Skills.txt:113 |
| 113 | Phù Vân Tán Tuyết | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 30/20 | -2/1 | 1/0/0 | 6/1/12 | fuyun_sanxue | Skills.txt:114 |
| 114 | Băng Cốt Tuyết Tâm | Hỗ trợ: bị động | 3; 0 | 60/30 | -2/0 | 0/0/0 | 7/0/0 | binggu_xuexin | Skills.txt:115 |
| 189 | Vũ Đả Lê Hoa | AOE* | 0; 0 | 30/20 | -2/0 | 1/0/0 | 6/3/79 | yuda_lihua | Skills.txt:190 |
| 190 | Mục Dã Lưu Tinh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 40/20 | -2/0 | 1/0/0 | 6/1/80 | muye_liuxing | Skills.txt:191 |
| 269 | Băng Tâm Trái ảnh | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/0/1 | 6/1/111 | bingxin_qianying | Skills.txt:270 |
| 270 | Đạp Tuyết Vô Ngân | Hỗ trợ | 0; 0 | 50/20 | -2/0 | 0/0/1 | 6/1/112 | taxue_wuhen | Skills.txt:271 |
| 336 | Băng Tung Vô ảnh | AOE* | 0; 0 | 80/20 | 1/1 | 1/0/0 | 2/5/146 | bingzong_wuying | Skills.txt:337 |
| 337 | Băng Tâm Tiên Tử | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 1/1/147 | bingxin_xianzi | Skills.txt:338 |
| 338 | Phong Tuyết Băng Thiên | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 7/1/148 | fengxue_bingtian | Skills.txt:339 |
| 381 | Băng Tâm Ngọc Lăng | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 50/20 | -2/1 | 1/0/0 | 7/1/187 | bingxin_yuling | Skills.txt:382 |
| 382 | Băng Tâm Tuyết Liên | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 50/20 | -2/1 | 1/0/0 | 7/1/188 | bingxin_xuelian | Skills.txt:383 |
| 398 | Phong Quyển Tàn Tuyết (ảnh động) | AOE* | 0; 0 | 10/20 | -2/1 | 1/0/0 | 1/16/196 | fengjuan_canxue | Skills.txt:399 |
| 713 | Ngự Tuyết ẩn | Hỗ trợ | 2; 0 | 120/20 | -2/1 | 0/0/1 | 7/0/0 | cuiyan120 | Skills.txt:715 |
| 1063 | Băng Tước Hoạt Kỳ | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | 1/1 | 1/0/0 | 1/1/326 | daocuiyan150 | Skills.txt:1063 |
| 1064 | Băng Ngưng Hàn Yên | AOE* | 0; 0 | 150/20 | -2/0 | 1/0/0 | 2/5/354 | daocuiyan150_2 | Skills.txt:1064 |
| 1065 | Thủy Anh Man Tú | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | -2/1 | 1/0/0 | 1/1/327 | neicuiyan150 | Skills.txt:1065 |
| 1093 | Khinh Sa Phù Thủy | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/20 | -2/1 | 1/0/0 | 7/1/355 | neicuiyan150_2 | Skills.txt:1093 |

### 7 — Cái Bang (gaibang) — 30 bản ghi

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 115 | Cái Bang Bổng pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | 2/0 | 0/0/0 | 7/0/0 | gaibang_bangfa | Skills.txt:116 |
| 116 | Cái Bang Chưởng Pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | gaibang_zhangfa | Skills.txt:117 |
| 117 | Đầu Thạch Vấn Lộ | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | -2/0 | 1/0/0 | 1/1/44 | physicsdamage_v | Skills.txt:118 |
| 118 | Cô Mộc Độn Lôi | Hỗ trợ | 0; 0 | 10/20 | -2/0 | 0/1/1 | 6/1/49 | lightingres_p | Skills.txt:119 |
| 119 | Diên Môn Thác Bát | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | 2/0 | 1/0/0 | 1/1/45 | yanmen_tuobo | Skills.txt:120 |
| 120 | Bôn Lưu Đáo Hải | Hỗ trợ | 0; 0 | 20/20 | -2/0 | 0/1/1 | 6/1/50 | fireres_p | Skills.txt:121 |
| 121 | Diệu Thủ Không Không | Hỗ trợ | 2; 0 | 20/20 | -2/0 | 0/0/0 | 6/0/0 | skill_cost_v | Skills.txt:122 |
| 122 | Kiến Nhân Thần Thủ | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | -2/1 | 1/0/0 | 1/1/46 | jianren_shenshou | Skills.txt:123 |
| 123 | Khuê Mộc Tinh Chiếu | Hỗ trợ | 0; 0 | 30/20 | -2/0 | 0/1/1 | 6/1/51 | poisonres_p | Skills.txt:124 |
| 124 | Đả Cẩu bổng | Hỗ trợ: bị động | 3; 0 | 30/20 | -2/0 | 0/0/0 | 7/1/0 | dagou_zhen | Skills.txt:125 |
| 125 | Bổng Đả ác Cẩu | AOE* | 0; 0 | 50/20 | 2/1 | 1/0/0 | 3/16/47 | bangda_egou | Skills.txt:126 |
| 126 | Kim Ô ánh Tuyết | Hỗ trợ | 0; 0 | 40/20 | -2/0 | 0/1/1 | 6/1/52 | coldres_p | Skills.txt:127 |
| 127 | Hoạt Bất Lưu Thủ 11 | Hỗ trợ | 0; 0 | 10/20 | -2/0 | 0/0/1 | 6/0/0 | huabu_liushou | Skills.txt:128 |
| 128 | Kháng Long Hữu Hối | AOE* | 0; 0 | 50/20 | -2/1 | 1/0/0 | 2/8/48 | kanglong_youhui | Skills.txt:129 |
| 129 | Hóa Hiểm Vi Di | Hỗ trợ: bị động | 3; 0 | 20/20 | -2/0 | 0/0/0 | 7/0/0 | huaxian_weiyi | Skills.txt:130 |
| 130 | Túy Điệp Cuồng Vũ | Hỗ trợ | 2; 0 | 60/30 | -2/0 | 0/0/1 | 7/0/0 | zuidie_kuangwu | Skills.txt:131 |
| 274 | Giáng Long Chưởng | Hỗ trợ: bị động | 3; 0 | 30/20 | -2/0 | 0/0/0 | 7/0/0 | xianglong_zhang | Skills.txt:275 |
| 277 | Hoạt Bất Lưu Thủ | Hỗ trợ | 0; 0 | 40/20 | -2/0 | 0/0/1 | 6/1/114 | huabu_liushou | Skills.txt:278 |
| 357 | Phi Long Tại Thiên | AOE* | 0; 0 | 80/20 | -2/1 | 1/0/0 | 0/3/166 | feilong_zaitian | Skills.txt:358 |
| 358 | Tiềm Long Tại Uyên | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 50/20 | -2/1 | 1/0/0 | 7/1/167 | qianlong_zaiyuan | Skills.txt:359 |
| 359 | Thiên Hạ Vô Cẩu | AOE* | 0; 0 | 80/20 | 2/1 | 1/0/0 | 0/16/168 | tianxia_wugou | Skills.txt:360 |
| 360 | Tiêu Diêu Công | Hỗ trợ: bị động | 3; 0 | 60/20 | -2/0 | 0/0/1 | 7/0/0 | xiaoyao_gong | Skills.txt:361 |
| 389 | Long Chiến Ư Dã | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 7/1/195 | longzhan_yuye | Skills.txt:390 |
| 714 | Hỗn Thiên Khí Công | Hỗ trợ: bị động | 3; 0 | 120/20 | -2/0 | 0/0/0 | 7/0/0 | gaibang120 | Skills.txt:716 |
| 720 | Hỗn Thiên Khí Công_Quyết Chú | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 120/20 | -2/0 | 1/0/0 | 6/1/275 | gaibang120zuzhou | Skills.txt:722 |
| 1072 | Ngũ Diệu Càn Khôn | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/20 | -2/1 | 1/0/0 | 7/1/334 | zhanggaibang150_2 | Skills.txt:1072 |
| 1073 | Thời Thặng Lục Long | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | -2/1 | 1/0/0 | 1/1/335 | zhanggaibang150 | Skills.txt:1073 |
| 1074 | Bổng Huýnh Lược Địa | AOE* | 0; 0 | 150/26 | 2/1 | 1/0/0 | 1/5/336 | gungaibang150 | Skills.txt:1074 |
| 1103 | Thời Thặng Lục Long Hỏa | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/20 | -2/0 | 1/0/0 | 7/1/344 | — | Skills.txt:1103 |
| 1602 | Thiên Hạ Vô Cẩu | AOE* | 0; 0 | 1/60 | -2/0 | 1/0/0 | 0/16/168 | tianxia_wugou | Skills.txt:1591 |

### 8 — Thiên Nhẫn (tianren) — 35 bản ghi

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 131 | Thiên Nhẫn  Đao pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | tianren_daofa | Skills.txt:132 |
| 132 | Thiên Nhẫn  Mâu pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | 3/0 | 0/0/0 | 7/0/0 | tianren_maofa | Skills.txt:133 |
| 133 | Thiên Nhẫn  phủ pháp (##) | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | — | Skills.txt:134 |
| 134 | Thiên Nhẫn  Chùy pháp | Hỗ trợ: bị động | 3; 0 | 10/20 | -2/0 | 0/0/0 | 7/0/0 | addphysicsdamage_p | Skills.txt:135 |
| 135 | Tàn Dương Như Huyết | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | 3/0 | 1/0/0 | 1/1/54 | canyang_ruxue | Skills.txt:136 |
| 136 | Hỏa Liên Phần Hoa | Hỗ trợ: debuff địch | 0; 0 | 10/20 | -2/0 | 1/0/0 | 6/1/20 | huolian_fenhua | Skills.txt:137 |
| 137 | ảo ảnh Phi Hồ | Hỗ trợ: debuff địch | 0; 0 | 20/20 | -2/0 | 1/0/0 | 6/1/20 | huanying_feihu | Skills.txt:138 |
| 138 | Thôi sơn  Điền Hải | AOE* | 0; 0 | 30/20 | -2/1 | 1/0/0 | 0/10/55 | tuishan_tianhai | Skills.txt:139 |
| 139 | Hỗn Thủy Mạc Ngư | Hỗ trợ: debuff địch | 0; 0 | 20/20 | -2/0 | 1/0/0 | 1/1/70 | physicsenhance_p | Skills.txt:140 |
| 140 | Phi Hồng Vô Tích | Hỗ trợ: debuff địch | 0; 0 | 30/20 | -2/0 | 1/0/0 | 6/1/20 | feihong_wuji | Skills.txt:141 |
| 141 | Liệt Hỏa Tình Thiên | AOE* | 0; 0 | 30/20 | 3/0 | 1/0/0 | 3/16/56 | liehuo_qingtian | Skills.txt:142 |
| 142 | Thâu Thiên Hoán Nhật | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 60/20 | 3/0 | 1/0/0 | 1/1/69 | toutian_huanri | Skills.txt:143 |
| 143 | Lịch Ma Đoạt Hồn | Hỗ trợ: debuff địch | 0; 0 | 50/20 | -2/0 | 1/0/0 | 6/1/20 | limo_duopo | Skills.txt:144 |
| 144 | Minh Tôn Bản Sinh (##) | Hỗ trợ: bị động | 3; 0 | 30/20 | -2/0 | 0/1/0 | 7/0/0 | fireres_p | Skills.txt:145 |
| 145 | Đơn Chỉ Liệt Diệm | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 10/20 | -2/1 | 1/0/0 | 1/1/57 | tanzhi_lieyan | Skills.txt:146 |
| 146 | Ngũ hành trận | Hỗ trợ | 2; 1 | 40/20 | -2/0 | 0/1/1 | 7/1/226 | wuxing_zhen | Skills.txt:147 |
| 147 | Huyền Minh Hấp Tinh | Hỗ trợ: debuff địch | 0; 0 | 40/20 | -2/0 | 1/0/0 | 1/1/71 | physicsenhance_p | Skills.txt:148 |
| 148 | Ma Diệm Thất Sát | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 60/20 | -2/1 | 1/0/0 | 6/1/58 | moyan_qisha | Skills.txt:149 |
| 149 | Thực Cốt Huyết Nhận | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | addfiredamage_v | Skills.txt:150 |
| 150 | Thiên Ma Giải Thể | Hỗ trợ | 2; 0 | 60/30 | -2/0 | 0/0/1 | 7/0/0 | tianmo_jieti | Skills.txt:151 |
| 226 | Ngũ hành trận | Hỗ trợ | 0; 0 | 0/20 | -2/0 | 0/1/1 | 3/1/92 | wuxing_zhen | Skills.txt:227 |
| 254 | Tam Muội Chân Hỏa | Hỗ trợ: bị động | 3; 0 | 60/20 | -2/0 | 0/0/1 | 7/0/0 | fireenhance_p | Skills.txt:255 |
| 361 | Vân Long Kích | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | 3/0 | 1/0/0 | 1/1/169 | yunlong_ji | Skills.txt:362 |
| 362 | Thiên Ngoại Lưu Tinh | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 6/1/171 | tianwai_liuxing | Skills.txt:363 |
| 363 | Nghiệp Hỏa Phàn Thành | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 7/1/170 | yehuo_fencheng | Skills.txt:364 |
| 364 | Bi Tô Thanh Phong | Hỗ trợ: debuff địch | 0; 0 | 40/20 | -2/0 | 1/0/0 | 6/1/20 | beisu_qingfeng | Skills.txt:365 |
| 378 | Phong Hỏa Liên Thiên | AOE* | 0; 0 | 80/20 | -2/1 | 1/0/0 | 3/8/184 | fenghuo_liantian | Skills.txt:379 |
| 379 | Ma Viêm Tại Thiên | AOE* | 0; 0 | 80/20 | -2/1 | 1/0/0 | 3/16/185 | moyan_zaitian | Skills.txt:380 |
| 391 | Nhiếp Hồn Loạn Tâm | Hỗ trợ: debuff địch | 0; 0 | 80/20 | -2/0 | 1/0/0 | 6/1/20 | shehun_luanxin | Skills.txt:392 |
| 715 | Ma Âm Phệ Phách | Hỗ trợ | 2; 0 | 120/20 | -2/0 | 0/0/1 | 7/0/0 | tianren120 | Skills.txt:717 |
| 723 | Ma Âm Phệ Phách - Hoảng loạn | Hỗ trợ/đặc biệt [C8; CHƯA KIỂM] | 14; 0 | 120/20 | -2/0 | 1/0/0 | 7/1/273 | quntisuijizoudong | Skills.txt:725 |
| 1075 | Giang Hải Nộ Lan | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | 3/0 | 1/0/0 | 1/1/337 | zhanren150 | Skills.txt:1075 |
| 1076 | Tật Hỏa Liệu Nguyên | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/26 | -2/1 | 1/0/0 | 6/1/366 | moren150 | Skills.txt:1076 |
| 1131 | Ma Âm Kích | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/20 | 3/0 | 1/0/0 | 1/1/337 | zhanren150 | Skills.txt:1131 |
| 1236 | Ma Âm Phệ Phách | Hỗ trợ | 2; 0 | 120/20 | -2/0 | 0/0/1 | 7/0/0 | tianren120 | Skills.txt:1236 |

### Cách dùng bảng cho thiết kế hảo hữu

- Nga My: ID 85 Nhất Diệp Tri Thu là ứng viên đòn đơn; 328 Tam Nga Tề Tuyết cấu hình 3 đạn tường; 332 Phổ Độ Chúng Sinh là ứng viên hỗ trợ ally/self. ID 333 là bản phát hiệu ứng, không đồng nhất với chiêu cha 332. ID 712 còn nối 718; 1114 nối event 1115, phải giữ chuỗi chứ không chọn theo tên “Tâm Kinh” mà đoán loại.
- Thúy Yên: ID 99 Phong Hoa Tuyết Nguyệt là ứng viên đòn đơn; 105 Vũ Đả Lê Hoa có 4 đạn tại đích, 336 Băng Tung Vô Ảnh có 5 đạn tỏa; 100 Hộ Thể Hàn Băng là hỗ trợ tự thân. Không dùng ID 106 thay 336 vì 106 có style 4 (C8). ID 1063 có event 1064 nên không chốt là đơn chỉ vì phát 1 đạn.
- Cái Bang: ID 119 Diên Môn Thác Bát là ứng viên đòn đơn; 125 Bổng Đả Ác Cẩu có 16 đạn tròn, 128 Kháng Long Hữu Hối có 8 đạn tỏa; 277 Hoạt Bất Lưu Thủ là hỗ trợ self. ID 118/120/123/126 có cờ ally/self và thuộc tính kháng, không gán thành AOE damage theo tên.
- Thiên Nhẫn: ID 135 Tàn Dương Như Huyết là ứng viên đòn đơn; 138 Thôi Sơn Điền Hải có 10 đạn tường, 141 Liệt Hỏa Tình Thiên có 16 đạn tròn; 150 Thiên Ma Giải Thể là hỗ trợ self. ID 136/137/140/143 là debuff, không tự gán “đánh đơn” từ cờ enemy. G/script/skill/tianren.lua:34–40,58–60,107–109 xác nhận giảm phản damage/accuracy/defense/damage.

Tất cả ứng viên trên chỉ có bằng chứng data + đường cast C1–C7; **[CHƯA KIỂM] AI của template hảo hữu sẽ tự gọi chúng**, chưa lựa level cân bằng hay giới hạn số kỹ năng. Quyền cast không đồng nghĩa có UI học, lưu qua login, buff tác dụng lên chủ, hoặc có animation hợp lệ.

ID 192 Thất Thương Thần Quyền và 283 Kháng Long Hữu Hối dùng script tianren nhưng tên không đủ xác nhận thuộc Thiên Nhẫn; ID 209 Đả Cẩu Bổng dùng emei.lua không biến thành kỹ năng Nga My. Ba bản ghi được chuyển phụ lục, [CHƯA KIỂM] ánh xạ chính thức. ID 90 Mê Tung Ảo Ảnh ở giữa dải ID Nga My nhưng dùng kunlun.lua (G/Settings/Skills.txt:91), nên không đưa vào chỉ vì ID liền nhau.

Một số điểm cần đối chiếu riêng trước khi chọn: ID 77/79 là passive; một số modifier weapon/player-only có thể không tác dụng trên con. A-12/A-14 đã chỉ ra allskill và bốn điểm cơ bản không mặc nhiên áp lên partner; không coi đăng ký passive là tất cả thuộc tính đã có hiệu lực. Tên trùng không là ID trùng: 105/189, 108/190, 715/1236, 328/1601, 359/1602 là các record khác nhau. Comment `khong su dung` tại G/script/skill/tianren.lua:133,196 là cảnh báo thiết kế cho Ngũ Hành Trận/Phong Hỏa Liên Thiên, không phải bằng chứng một guard cấm runtime.

## 4. Phụ lục bản ghi dùng chung script, alias và trạng thái

Các dòng sau **không được tự động coi là skill môn phái có thể học**: gồm tên abc/ncp, hiệu ứng nhiệm vụ, trang trí, và các bản phụ dùng lại script. Nhóm chỉ là nơi đặt file Lua; C1–C8 và H vẫn áp dụng. Giữ chúng để người thiết kế có danh sách ID đầy đủ của tập lọc đã khảo sát và tránh nhầm chúng với chiêu chính.

### Script emei — 8 bản ghi bổ sung

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 209 | Đả Cẩu bổng | Hỗ trợ | 0; 0 | 50/20 | -2/0 | 0/1/1 | 3/1/92 | dagou_zhen | Skills.txt:210 |
| 1090 | abc219 | AOE* | 0; 0 | 150/20 | -2/1 | 1/0/0 | 3/4/352 | zhangemei150_2 | Skills.txt:1090 |
| 1091 | abc220 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 0/20 | -2/0 | 1/0/0 | 6/1/353 | jianemei150_2 | Skills.txt:1091 |
| 1142 | abc247 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 50/20 | -2/1 | 1/0/0 | 1/1/382 | sane_jixue | Skills.txt:1142 |
| 1145 | abc250 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 0/20 | -2/0 | 1/0/0 | 6/1/383 | sane_jixue | Skills.txt:1145 |
| 1152 | ncp7 | AOE* | 0; 0 | 80/20 | -2/0 | 1/0/0 | 0/5/323 | jianemei150 | Skills.txt:1152 |
| 1153 | ncp8 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/0 | 1/0/0 | 6/1/324 | zhangemei150 | Skills.txt:1153 |
| 1418 | abc367 | Hỗ trợ: bị động | 3; 0 | 10/20 | 0/0 | 0/0/1 | 7/0/0 | — | Skills.txt:1418 |

### Script cuiyan — 21 bản ghi bổ sung

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 251 | Pháo Hoa | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 0/0 | 0/0 | 0/0/0 | 6/1/108 | — | Skills.txt:252 |
| 500 | Hiệu úy Vòng tròn | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:501 |
| 501 | Thống Lĩnh Vòng tròn | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:502 |
| 502 | Phó tướng Vòng tròn | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:503 |
| 503 | Đại tướng Vòng tròn | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:504 |
| 504 | Nguyên Soái Vòng tròn | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:505 |
| 509 | Hoàn thành nhiệm vụ | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:510 |
| 541 | Hoàn thành nhiệm vụ  Sát thủ | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:543 |
| 548 | Vòng tròn  tăng đôi kinh nghiệm (hoàn thành nhiệm vụ sát thủ) | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:550 |
| 662 | trạng thái nhiệm vụ ngẫu nhiên | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:664 |
| 687 | Hoa | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 0/0 | 0/0 | 0/0/0 | 6/1/260 | — | Skills.txt:689 |
| 764 | Câu hỏi Lễ tình nhân | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:766 |
| 765 | Thanh diễn tiến Lễ Tình Nhân | Hỗ trợ | 2; 0 | 50/20 | -2/0 | 0/0/1 | 7/0/0 | — | Skills.txt:767 |
| 1092 | abc221 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 50/20 | -2/1 | 1/0/0 | 7/1/354 | daocuiyan150_2 | Skills.txt:1092 |
| 1102 | abc227 | AOE* | 0; 0 | 150/20 | -2/1 | 1/0/0 | 0/3/362 | neicuiyan150 | Skills.txt:1102 |
| 1154 | ncp9 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/0 | 1/0/0 | 1/1/326 | daocuiyan150 | Skills.txt:1154 |
| 1155 | ncp10 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/0 | 1/0/0 | 1/1/327 | neicuiyan150 | Skills.txt:1155 |
| 1172 | abc252 | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 0/1 | -2/0 | 0/0/0 | 6/1/385 | — | Skills.txt:1172 |
| 1263 | abc295a | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 120/20 | -2/0 | 0/0/0 | 6/1/108 | — | Skills.txt:1263 |
| 1288 | abc308 | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 0/20 | -2/0 | 0/0/0 | 6/4/404 | — | Skills.txt:1288 |
| 1471 | Pháo | [CHƯA KIỂM] mục tiêu/loại | 0; 0 | 0/0 | 0/0 | 0/0/0 | 6/1/430 | — | Skills.txt:1471 |

### Script gaibang — 3 bản ghi bổ sung

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1101 | abc226 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 150/20 | -2/1 | 1/0/0 | 1/1/363 | zhanggaibang150 | Skills.txt:1101 |
| 1161 | ncp16 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/0 | 1/0/0 | 1/1/335 | zhanggaibang150 | Skills.txt:1161 |
| 1162 | ncp17 | AOE* | 0; 0 | 80/20 | -2/0 | 1/0/0 | 1/5/336 | gungaibang150 | Skills.txt:1162 |

### Script tianren — 7 bản ghi bổ sung

| SkillId | Tên data (Unicode) | Loại thiết kế | S; aura | Req/Max | E/H | E/A/S | Form/N/Child | Khóa Lua hoặc thuộc tính đầu | Nguồn G/Settings/ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 283 | Kháng Long Hữu Hối | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 20/20 | -2/1 | 1/0/0 | 6/1/117 | firedamage_v | Skills.txt:284 |
| 192 | Thất Thương Thần Quyền | AOE* | 0; 0 | 50/20 | -2/1 | 1/0/0 | 3/8/82 | — | Skills.txt:193 |
| 876 | abc100 | Hỗ trợ/đặc biệt [C8; CHƯA KIỂM] | 14; 0 | 1/20 | -2/0 | 1/0/0 | 7/1/273 | quntisuijizoudong | Skills.txt:876 |
| 931 | abc154 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 6/1/171 | boss_tianwai | Skills.txt:931 |
| 1104 | abc228 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/1 | 1/0/0 | 7/1/338 | moren150 | Skills.txt:1104 |
| 1163 | ncp18 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/0 | 1/0/0 | 1/1/337 | zhanren150 | Skills.txt:1163 |
| 1164 | ncp19 | Đánh đơn* / AOE [CHƯA KIỂM] | 0; 0 | 80/20 | -2/0 | 1/0/0 | 6/1/366 | moren150 | Skills.txt:1164 |

## 5. Kiểm chứng, giới hạn và bàn giao

- Đã đọc trực tiếp A-12/A-14, hai file faction, Skills.txt, các đoạn KSkills.cpp/KNpc.cpp và loader/list liên quan. Trích xuất bằng cột TAB, giữ SkillId riêng số dòng. Tập đối chiếu script bốn phái có **188 record**, gồm **149 record catalog** và **39 record phụ lục**; phân nhóm không làm rơi record. Bảng không phải danh sách mọi skill trong PAK hoặc toàn bộ luật học.
- Đã xem các block/khóa Lua ở emei.lua:12–423, cuiyan.lua:12–424, gaibang.lua:13–384, tianren.lua:3–307 theo tìm kiếm khóa giới hạn; chỉ những đoạn ghi cụ thể mới được dùng để kết luận hiệu ứng. Không chạy Lua hoặc đánh giá hệ số ở từng level.
- **[CHƯA KIỂM]** Gate học từng chiêu/giới tính/bí kíp/điểm/phái, FactionSkill trong PAK, cấp skill thật của template partner, scheduler AI hỗ trợ/đánh, handler áp lên partner/chủ, mọi chuỗi event và missile collision/damage area, tài nguyên SPR, round-trip save, binary đang dùng. AOE* và Đánh đơn* đều là ứng viên cấu hình, không phải kết quả runtime.
- Test/build/runtime/VM/network: **không chạy**, đúng phạm vi tĩnh. Chỉ kiểm cấu trúc Markdown và diff hai file khi bàn giao; không gọi đó là test game.
- Lỗi và xử lý: lần đọc task mặc định lỗi dấu, đọc lại UTF-8; một số output dài bị rút gọn, đã thu hẹp cột/đoạn cần dùng và ghi catalog trực tiếp từ TAB. `rg : The term 'rg' is not recognized ...` nên dùng Select-String/ReadAllLines. `D:/JX-source/SwordOnline` không tồn tại, chuyển đúng gốc A-14. Hai đường header đoán dưới Sources/header không tồn tại, chuyển đúng `D:/JX-source/server/jxOnline/header` theo include/bản cây đã xác nhận. Lệnh Get-Item nhiều ứng viên thiếu có exit 1, không phải lỗi nội dung nguồn. Không lặp lỗi quá 3 lần, không sửa source/config để khắc phục.
- Lỗi khi ghi: kiểm checkpoint ban đầu dùng tìm chuỗi `## Kết quả` nên bắt nhầm câu hướng dẫn trong task và dừng sau khi đã tạo báo cáo. Đã sửa phép kiểm thành heading nguyên dòng, giữ nguyên báo cáo đã tạo và thêm đúng mục Kết quả, không ghi đè công việc đang dở.
- Lỗi kiểm cấu trúc: phép đếm đầu tiên tính cả 4 dòng thứ tự phái nên ra 192 thay vì 188; đã giới hạn vào dòng catalog có Skills.txt. In Unicode lần đầu gặp `UnicodeEncodeError` do stdout CP1252; đã cấu hình stdout UTF-8, nội dung file UTF-8 không bị mất dấu.
- Git trước ghi: branch `task/A-15b`, có sẵn `?? JX1_OPS/TASKS/A-15b.md`; giữ nguyên nội dung đó và chỉ thêm mục Kết quả. Không ghi ra ngoài hai file task cho phép, không tạo helper/parser file, không sửa BAI_HOC hoặc báo cáo nền.
- Trạng thái cuối: **DONE — khảo sát tĩnh và catalog kèm giới hạn bằng chứng**. Không có blocker để bàn giao báo cáo; các mục [CHƯA KIỂM] cần task xác minh sau, không được quảng bá thành tính năng đã hoạt động.
- Commit SHA/link: **không có**. Không stage/commit/push vì người dùng không yêu cầu công bố Git và giới hạn lượt này là ghi báo cáo/mục Kết quả. Giữ kết quả local.
