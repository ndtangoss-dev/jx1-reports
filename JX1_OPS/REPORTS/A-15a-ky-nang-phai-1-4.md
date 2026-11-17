TÓM TẮT 1: [NGUỒN] Bốn phái đầu theo faction.ini là Thiếu Lâm, Thiên Vương, Đường Môn, Ngũ Độc (section 0–3); số 4 là thứ tự, không phải cuối danh sách.
TÓM TẮT 2: [NGUỒN]/[SUY LUẬN] Catalog dưới đây có 196 dòng Skills.txt liên hệ bốn phái qua LvlSetScript và hai dòng legacy; bao gồm chiêu chính, phụ và biến thể, không coi tất cả là chiêu được học.
TÓM TẮT 3: [NGUỒN] kind_partner không qua kiểm vũ khí/ngựa của IsPlayer trong CanCastSkill và Cost trả TRUE trước khi trừ tài nguyên (S/KSkills.cpp:267–358; S/KNpc.cpp:7002–7005,15465–15474).
TÓM TẮT 4: [NGUỒN] Cast thường vẫn cần skill hợp lệ, level hiện tại >0, hết cooldown và target phù hợp; passive đi đường riêng; style 4 không được DoSkill chuyển vào DoOrdinSkill (S/KNpc.cpp:3640–3674,3748–3761).
TÓM TẮT 5: [CHƯA KIỂM] Chưa xác minh học/mở khóa của từng chiêu, mọi chuỗi missile/event/Lua, AI chọn chiêu, hiệu ứng/animation hay runtime; đây là bảng ứng viên thiết kế, không chứng nhận 196 chiêu chạy được.

# A-15a — Kỹ năng bốn phái đầu cho NPC hảo hữu

Ngày: 17/11/2026. Trạng thái **DONE cho khảo sát tĩnh và bảng thiết kế**; các giới hạn xác minh ghi rõ dưới đây. Đã đọc A-12 và A-14 theo task. Không sửa mã, cấu hình hoặc dữ liệu nguồn; không build/test game, không chạy exe, không kết nối mạng/VM/DB.

## Nguồn và ranh giới

| Tiền tố | Gốc chỉ đọc |
| --- | --- |
| S/ | `D:/JX-source/server/jxOnline/gameserver/Sources/Core/Src/` |
| G/ | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/` |

Đường `D:\JX-source\SwordOnline` mà task ghi không tồn tại. Dùng source copy `D:\JX-source\server` đã được A-14 dẫn; Settings lấy từ gói server G/ mà A-12 dẫn, vì thư mục gameserver của source copy chỉ có Headers/include/Lib/Sources. **[CHƯA KIỂM] Source D/ và data G/ có cùng phiên bản, được binary thực nạp hay không.** Số dòng vật lý tính từ 1, không đồng nhất dòng với SkillId. KSkillManager đọc riêng SkillId/SkillStyle/MaxLevel và lưu ánh xạ dòng (S/KSkillManager.cpp:55–74).

Source đọc CP936; tên Việt trong Skills.txt đọc CP1252 rồi chuyển ký tự TCVN3 sang Unicode ngay khi trích bảng. Giữ nguyên tên bất thường/nhãn `(##)`/`abc`/`ncp`, không tự sửa nội dung data. Có lần xuất Python qua pipe làm mất dấu, đã đối chiếu lại bằng PowerShell trước khi ghi catalog. Python chỉ dùng `python -I`, không tạo script/parser phụ trên đĩa.

## Thứ tự phái và cách lấy catalog

| Thứ tự task | Section | Phái/token | Ngũ hành | Nguồn |
| --- | --- | --- | --- | --- |
| 1 | 0 | Thiếu Lâm / shaolin | Kim | G/Settings/faction/faction.ini:6–10 |
| 2 | 1 | Thiên Vương / tianwang | Kim | G/Settings/faction/faction.ini:13–17 |
| 3 | 2 | Đường Môn / tangmen | Mộc | G/Settings/faction/faction.ini:20–24 |
| 4 | 3 | Ngũ Độc / wudu | Mộc | G/Settings/faction/faction.ini:27–31 |

Section 4 tiếp tục Nga My ở :34–38, danh sách còn đến section 15 (:103–106); vì vậy chỉ lấy bốn phái đầu. `MonPhai.ini:6–24` đối chiếu bốn tên Trung Quốc theo cùng thứ tự. KFaction::Init đọc FACTION_FILE, duyệt section và lấy Name/ShowName/Series/Camp (S/KFaction.cpp:118–179); không lấy các khối loader đã comment phía trên làm bằng chứng.

**[SUY LUẬN] Quy tắc catalog:** trích toàn bộ dòng có LvlSetScript kết thúc bằng `shaolin.lua`, `tianwang.lua`, `tangmen.lua`, `wudu.lua`; thêm ID 3 (tên Thiếu Lâm, script saolin/...) và ID 59 (tên bẫy Đường Môn trong cụm legacy, script skill.lua). Kết quả 47/52/56/41 dòng. Đây là liên hệ theo data, chưa phải whitelist học phái chính thức. Không dùng CharClass để nhận diện phái: cả Thiếu Lâm/Thiên Vương có CharClass=1, Đường Môn/Ngũ Độc=3 (G/Settings/Skills.txt:5,24,44,61). Không nhập ID 22 “Kim Ba” (:23) hoặc ID 53 “Công kích vật lý” (:54) vào phái chỉ vì nằm xen giữa.

**[CHƯA KIỂM]** Chưa xác định được bảng `FactionSkill` đang dùng, toàn bộ script NPC truyền dạy, nhiệm vụ/bí kíp/điểm kỹ năng và điều kiện tiền kỹ năng. Không có file mang tên FactionSkill trong danh sách trực tiếp Settings/faction và Settings đã đọc; không suy thành không tồn tại trong PAK/thư mục khác. `KPlayerFaction::OpenCurSkillLevel` trả TRUE ngay; đoạn thêm skill theo phái nằm trong comment (:105–138), nên không dùng nó chứng minh cấp học. Catalog có thể chứa chiêu phụ/boss/NPC dùng chung script và có thể thiếu chiêu gắn script khác; nhóm đó phải được đối chiếu trước khi lập whitelist triển khai.

## Điều kiện học/dùng và kiểm cast chung

Mỗi dòng catalog ghi `Req/Max` = ReqLevel/MaxLevel thô, **chưa phải bảo đảm cấp học hảo hữu**. KSkill nạp ReqLevel, EqtLimit, HorseLimit ở S/KSkills.cpp:2981–2986; trong CanCastSkill đã đọc không có so sánh cấp NPC với ReqLevel. Không tự cho rằng partner đạt cấp là tự học. Đường gán NPC skill có SetNpcSkill kiểm slot/ID/level dương và lookup skill (S/KSkillList.cpp:64–96); **[CHƯA KIỂM]** roster hảo hữu nào đã được gán từng ID và luồng học/save riêng.

`E/H` = EqtLimit/HorseLimit thô: E=-2 không hạn chế; -1 tay không; 0..99 loại vũ khí gần; 100..199 nhóm vũ khí xa theo comment (:279–282), nhưng code thực cộng MAX_MELEEWEAPON_PARTICULARTYPE_NUM (:301–304), chưa kiểm hằng số để coi comment là ánh xạ tuyệt đối. H=0 không hạn chế, 1 không cưỡi, 2 phải cưỡi (:315–336). Chỉ IsPlayer mới vào khối này (:267). Partner do AddTongBan gán kind_partner (S/KNpcSet.cpp:882), IsPlayer server chỉ nhận kind_player cùng player index hợp lệ (S/KNpc.cpp:15465–15474). Vì thế E/H là điều kiện data cho thiết kế, **không đang được enforce cho partner ở CanCastSkill**; đồ của chủ không tự là vũ khí của con (nền A-12/A-14).

| Mã cast trong bảng | Kết luận source cho kind_partner |
| --- | --- |
| A | Style 0/1/2: ứng viên đi đường cast NPC thường. Cần active skill tồn tại (:3640–3644), hết cooldown thường/ngựa (:3647–3659), CanCastByIndex và CanCastSkill (:3673–3674), rồi dispatch DoOrdinSkill (:3748–3749 của KNpc.cpp). Không thấy guard loại partner ở những đoạn này. |
| P | Style 3: hỗ trợ bị động; SetNpcSkill gọi Cast ngay (:99–102 của KSkillList.cpp), KSkill::Cast dispatch passive (:548–550), CastPassivitySkill áp state khi có state attributes (:3462–3472). Không coi passive là đòn AI cần spam. Tác dụng từng handler vẫn [CHƯA KIỂM]. |
| X | Style 4: data tạo NPC/bẫy; DoSkill chỉ chấp nhận 0–3 hoặc thief, default return (:3748–3761). Không đề xuất gán trực tiếp vào vòng AI thường. Đường gọi Cast trực tiếp có case CreateNpc (:555), nội dung và khả năng partner dùng nhánh riêng [CHƯA KIỂM]. |
| M | Mê Ảnh Tung ID 710, style 1 nhưng tác dụng di chuyển; cần khảo sát CastMeleeSkill thay vì coi là đòn sát thương. KNpc::DoOrdinSkill gọi CastMeleeSkill và có thể thất bại (:3795–3804). |

Các mã A/P/X/M dẫn đến bảng kiểm chung này cho **từng dòng** catalog, không phải kết quả chạy thử. Dòng `(##)`/`abc`/`ncp`, Req=0/1 hoặc dòng phụ không được tự đưa vào danh sách học.

- Target `-1,index` cần index hợp lệ và quan hệ enemy/ally/self phù hợp (S/KSkills.cpp:235–260). Khi TargetSelf=1 và tham số đầu không phải -1, CanCastSkill đổi sang chính launcher rồi return TRUE sớm (:224–228), trước cả khối kiểm E/H. CastInitiativeSkill còn kiểm lại tham số/quan hệ (:3348–3375). Owner có được tính ally với từng buff hay không **[CHƯA KIỂM]**.
- CanCastByIndex kiểm CurrentSkillLevel>0 và NextCastTime (:884–887 của KSkillList.cpp); guard chỉ số slot dùng `&&` ở :882 là điểm cần xem sau, không phải bằng chứng mọi slot đã an toàn. Chỉ dùng slot hợp lệ từ đường khởi tạo đã kiểm, không dựa vào guard này để nhận dữ liệu tùy ý.
- KNpc::Cost trả TRUE ngay nếu !IsPlayer (:7002–7005), vì vậy không yêu cầu/trừ mana/life/stamina cho partner trên đường này. CostValue, TimePerCast có thể do Lua sửa theo level; **[CHƯA KIỂM]** giá trị động từng level, không công bố chi phí/cooldown cuối từ bảng thô.
- KSkill::Cast không tự gọi CanCastSkill vì hai dòng đã comment (:459–460); nó kiểm launcher, target cùng subworld rồi dispatch style (:468–550). Gọi Cast trực tiếp không tương đương đường DoSkill đầy đủ. CastSkill ở :4522–4527 chỉ gọi SysnCastSkillEffect; hàm đó chỉ phát gói trong IsPlayer (:10808–10849 của KNpc.cpp), không được coi là cách thực thi chiêu cho partner.
- Bảng phân loại dưới đây dùng SkillStyle, target flags và **mô tả data**, không suy AOE từ AttackRadius hay số đòn liên tiếp. “Đánh đơn?” và “phạm vi?” nghĩa **[CHƯA KIỂM]** phạm vi; AOE ghi theo mô tả, chưa đo missile/collision/runtime. Hỗ trợ bao gồm buff, passive, khống chế/debuff. Nhãn hỗ trợ không bảo đảm handler nhận partner: A-12/A-14 đã ghi bốn điểm cơ bản và AllSkillV có guard player.
- Script phái có công thức động và event: ví dụ G/script/skill/tangmen.lua:12–21 khai báo skill_vanishedevent gọi ID 1113. Vì vậy không lấy ChildSkillId cố định làm toàn bộ chuỗi. **[CHƯA KIỂM]** closure của mọi Start/Fly/Collide/Vanished event, missile, skill con và Lua; không nhân rộng whitelist từ tên trùng.

## Catalog theo phái

Nguồn tất cả dòng là `G/Settings/Skills.txt:<dòng>`; cột cuối ghi đúng dòng vật lý. `Đích` liệt kê cờ E=enemy, A=ally, S=self, O=other, N=no-NPC; dấu “—” nghĩa các cờ này đều 0, không chứng minh chiêu không có target qua cơ chế khác. `Phụ/biến thể` là dấu hiệu rà soát, chưa phải xác nhận đồ thị gọi. Điều kiện chung ở trên áp dụng cùng Req/Max và E/H của mỗi dòng; điều kiện học bổ sung **[CHƯA KIỂM]** cho tất cả.

### 1. Thiếu Lâm

| ID | Kỹ năng/chiêu thức | Loại theo data | Req/Max | E/H | Đích | Cast/style | Dấu hiệu | Dòng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | Thiếu Lâm Kiếm pháp | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Ứng viên | 4 |
| 4 | Thiếu Lâm Côn pháp | Hỗ trợ bị động | 10/20 | 2/0 | — | P/3 | Ứng viên | 5 |
| 5 | Thiếu Lâm thương pháp (##) | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Nhãn (##) | 6 |
| 6 | Thiếu Lâm Đao pháp | Hỗ trợ bị động | 10/20 | 1/0 | — | P/3 | Ứng viên | 7 |
| 7 | Thiếu Lâm Chùy pháp (##) | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Nhãn (##) | 8 |
| 8 | Thiếu Lâm Quyền Pháp | Hỗ trợ bị động | 10/20 | -1/0 | — | P/3 | Ứng viên | 9 |
| 9 | Hỗn Nguyên Nhất Khí công | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Ứng viên | 10 |
| 10 | Kim Cang Phục Ma | Đánh đơn (mô tả) | 10/20 | -2/1 | E | A/1 | Ứng viên | 11 |
| 11 | Hoành Tảo Lục Hợp | AOE (mô tả) | 50/20 | 2/1 | E | A/0 | Ứng viên | 12 |
| 12 | Kim Cang Hộ Thể | Hỗ trợ bị động | 20/20 | -2/0 | — | P/3 | Ứng viên | 13 |
| 13 | Lập Địa Thành Phật | Hỗ trợ buff | 30/20 | -2/0 | A | A/0 | Ứng viên | 14 |
| 14 | Hàng Long Bất Vũ | AOE (mô tả) | 10/20 | -1/0 | E | A/0 | Ứng viên | 15 |
| 15 | Bất động Minh Vương | Hỗ trợ buff | 20/20 | -2/0 | A,S | A/0 | Ứng viên | 16 |
| 16 | La Hán Trận | Hỗ trợ aura | 30/20 | -2/0 | A,S,N | A/2 | Ứng viên | 17 |
| 17 | Long Trảo Hổ Trảo (##) | Đánh đơn (mô tả) | 40/20 | -2/1 | E | A/1 | Nhãn (##) | 18 |
| 18 | Huệ Nhãn chú | Hỗ trợ buff | 40/20 | -2/0 | A,S | A/0 | Ứng viên | 19 |
| 19 | Ma Ha Vô Lượng | Đánh đơn? (phạm vi?) | 50/20 | 1/0 | E | A/0 | Ứng viên | 20 |
| 20 | Sư Tử Hống | Hỗ trợ/debuff (phạm vi?) | 40/20 | -2/0 | E | A/0 | Ứng viên | 21 |
| 21 | Dịch Cân kinh | Hỗ trợ bị động | 60/20 | -2/0 | — | P/3 | Ứng viên | 22 |
| 202 | La Hán Trận | Hỗ trợ buff | 30/20 | -2/0 | A,S,N | A/0 | Ứng viên | 203 |
| 213 | Bất động Minh Vương | Hỗ trợ buff | 30/20 | -2/0 | A,S | A/0 | Ứng viên | 214 |
| 216 | Kim Cang Phục Ma | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 217 |
| 217 | Hoành Tảo Lục Hợp | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 218 |
| 218 | Long Trảo Hổ Trảo | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 219 |
| 271 | Long Trảo Hổ Trảo | Đánh đơn? (phạm vi?) | 50/20 | -1/1 | E | A/1 | Ứng viên | 272 |
| 272 | Long Trảo Hổ Trảo | Đánh đơn? (phạm vi?) | 30/20 | -2/0 | E | A/0 | Ứng viên | 273 |
| 273 | Như Lai Thiên Diệp | Hỗ trợ buff | 60/30 | -2/0 | S | A/2 | Ứng viên | 274 |
| 317 | Kim Phật Xuất Kích | Đánh đơn? (phạm vi?) | 30/20 | -2/0 | E | A/0 | Ứng viên | 318 |
| 318 | Đạt Ma Độ Giang | AOE (mô tả) | 80/20 | -1/1 | E | A/1 | Ứng viên | 319 |
| 319 | Hoành Tảo Thiên Quân | AOE (mô tả) | 80/20 | 2/1 | E | A/0 | Ứng viên | 320 |
| 320 | Hoành Tảo Lục Hợp 111 | AOE (mô tả) | 50/20 | -2/1 | E | A/1 | Ứng viên | 321 |
| 321 | Vô Tướng Trảm | Đánh đơn? (phạm vi?) | 80/20 | 1/0 | E | A/0 | Ứng viên | 322 |
| 709 | Đại Thừa Như Lai Chú | Hỗ trợ buff | 120/20 | -2/0 | S | P/3 | Ứng viên | 711 |
| 725 | Đại Thừa Như Lai Chú_Phản đòn bùa chú | Hỗ trợ buff | 120/20 | -2/0 | S | A/2 | Phụ/biến thể? | 727 |
| 734 | Kỹ năng phụ - Sư Tử Hống | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 736 |
| 900 | abc123 | Hỗ trợ buff | 1/20 | -2/0 | S | P/3 | Biến thể, chưa whitelist | 900 |
| 986 | abc171 | Đánh đơn? (phạm vi?) | 50/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 986 |
| 1055 | Đại Lực Kim Cang Chưởng | Đánh đơn? (phạm vi?) | 150/26 | -1/1 | E | A/1 | Ứng viên | 1055 |
| 1056 | Vi Đà Hiến Xử | AOE (mô tả) | 150/26 | 2/1 | E | A/0 | Ứng viên | 1056 |
| 1057 | Tam Giới Quy Thiền | Đánh đơn? (phạm vi?) | 150/26 | 1/0 | E | A/0 | Ứng viên | 1057 |
| 1082 | abc213 | Đánh đơn? (phạm vi?) | 150/20 | 2/1 | E | A/0 | Biến thể, chưa whitelist | 1082 |
| 1083 | Long Thừa Bát Nhã Thủ | Đánh đơn? (phạm vi?) | 30/20 | -2/0 | E | A/0 | Ứng viên | 1083 |
| 1085 | abc215 | Đánh đơn? (phạm vi?) | 150/20 | 1/0 | E | A/0 | Biến thể, chưa whitelist | 1085 |
| 1146 | ncp1 | Đánh đơn? (phạm vi?) | 80/20 | -2/0 | E | A/1 | Biến thể, chưa whitelist | 1146 |
| 1147 | ncp2 | AOE (mô tả) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1147 |
| 1148 | ncp3 | Đánh đơn? (phạm vi?) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1148 |
| 1201 | Vi Đà Hộ Pháp | Đánh đơn? (phạm vi?) | 150/20 | 2/1 | E | A/0 | Ứng viên | 1201 |

Số dòng trích: **47**. Các nhãn phạm vi? đều là **[CHƯA KIỂM]**; tên trùng khác ID không được gộp.

### 2. Thiên Vương

| ID | Kỹ năng/chiêu thức | Loại theo data | Req/Max | E/H | Đích | Cast/style | Dấu hiệu | Dòng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23 | Thiên Vương  Thương pháp | Hỗ trợ bị động | 10/20 | 3/0 | — | P/3 | Ứng viên | 24 |
| 24 | Thiên Vương  Đao pháp | Hỗ trợ bị động | 10/20 | 1/0 | — | P/3 | Ứng viên | 25 |
| 25 | Thánh Vương Đao pháp (##) | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Nhãn (##) | 26 |
| 26 | Thiên Vương  Chùy Pháp | Hỗ trợ bị động | 10/20 | 4/0 | — | P/3 | Ứng viên | 27 |
| 27 | Thiên Vương  Phủ pháp (##) | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Nhãn (##) | 28 |
| 28 | Thánh Vương Phủ pháp (##) | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Nhãn (##) | 29 |
| 29 | Trảm Long quyết | Đánh đơn? (phạm vi?) | 10/20 | 4/1 | E | A/1 | Ứng viên | 30 |
| 30 | Hồi Phong Lạc Nhạn | Đánh đơn? (phạm vi?) | 10/20 | 3/1 | E | A/1 | Ứng viên | 31 |
| 31 | Hàng Vân Quyết | Đánh đơn? (phạm vi?) | 30/20 | 4/1 | E | A/1 | Ứng viên | 32 |
| 32 | Vô Tâm Trảm | Đánh đơn? (phạm vi?) | 60/20 | 1/0 | E | A/1 | Ứng viên | 33 |
| 33 | Tĩnh Tâm Quyết | Hỗ trợ buff | 20/20 | -2/0 | S | A/2 | Ứng viên | 34 |
| 34 | Kinh Lôi Trảm | Đánh đơn? (phạm vi?) | 10/20 | 1/0 | E | A/1 | Ứng viên | 35 |
| 35 | Dương Quan Tam Điệp | Đánh đơn? (phạm vi?) | 30/20 | 3/1 | E | A/1 | Ứng viên | 36 |
| 36 | Thiên Vương Chiến ý | Hỗ trợ buff | 60/30 | -2/0 | S | P/3 | Ứng viên | 37 |
| 37 | Bát Phong Trảm | Đánh đơn? (phạm vi?) | 30/20 | 1/0 | E | A/1 | Ứng viên | 38 |
| 38 | Bàn Cổ Cửu Thức (##) | Hỗ trợ/debuff (phạm vi?) | 40/20 | -2/1 | E | A/1 | Nhãn (##) | 39 |
| 39 | Triêm Y Thập Bát Điệt (##) | Hỗ trợ buff | 40/20 | -2/0 | S | A/2 | Nhãn (##) | 40 |
| 40 | Đoạn Hồn Thích | Đánh đơn? (phạm vi?) | 40/20 | -2/0 | E | A/1 | Ứng viên | 41 |
| 41 | Huyết Chiến Bát Phương | Đánh đơn? (phạm vi?) | 60/20 | 3/1 | E | A/1 | Ứng viên | 42 |
| 42 | Kim Chung Tráo | Hỗ trợ buff | 50/20 | -2/0 | S | A/2 | Ứng viên | 43 |
| 219 | Hồi Phong Lạc Nhạn | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 220 |
| 220 | Vô Tâm Trảm | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 221 |
| 221 | Dương Quan Tam Điệp | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 222 |
| 222 | Bát Phong Trảm | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 223 |
| 224 | Đoạn Hồn Thích | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 225 |
| 225 | Huyết Chiến Bát Phương | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 226 |
| 322 | Phá Thiên Trảm | Đánh đơn? (phạm vi?) | 80/20 | 1/0 | E | A/1 | Ứng viên | 323 |
| 323 | Truy Tinh Trục Nguyệt | Đánh đơn? (phạm vi?) | 80/20 | 3/1 | E | A/1 | Ứng viên | 324 |
| 324 | Thừa Long Quyết | Đánh đơn? (phạm vi?) | 60/20 | 4/1 | E | A/1 | Ứng viên | 325 |
| 325 | Truy Phong Quyết | Đánh đơn? (phạm vi?) | 80/20 | 4/1 | E | A/1 | Ứng viên | 326 |
| 326 | Phá Thiên Trảm | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 327 |
| 327 | Truy Tinh Trục Nguyệt | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 328 |
| 404 | Kinh Lôi Trảm | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 405 |
| 405 | Trảm Long quyết | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 406 |
| 406 | Hàng Vân Quyết | Đánh đơn? (phạm vi?) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 407 |
| 407 | Thừa Long Quyết | Đánh đơn? (phạm vi?) | 60/20 | -2/0 | E | A/0 | Ứng viên | 408 |
| 408 | Truy Phong Quyết | Đánh đơn? (phạm vi?) | 60/20 | 1/0 | E | A/0 | Ứng viên | 409 |
| 708 | Đảo Hư Thiên | Hỗ trợ buff | 120/20 | -2/0 | S | P/3 | Ứng viên | 710 |
| 724 | Đảo Hư Thiên_Kháng bùa chú | Hỗ trợ buff | 120/20 | -2/0 | S | A/2 | Phụ/biến thể? | 726 |
| 930 | abc153 | Đánh đơn? (phạm vi?) | 40/20 | -2/0 | E | A/1 | Biến thể, chưa whitelist | 930 |
| 1058 | Hào Hùng Trảm | AOE (mô tả) | 150/26 | 1/0 | E | A/1 | Ứng viên | 1058 |
| 1059 | Tung Hoành Bát Hoang | AOE (mô tả) | 150/26 | 4/1 | E | A/1 | Ứng viên | 1059 |
| 1060 | Bá Vương Tạm Kim | AOE (mô tả) | 150/26 | 3/1 | E | A/1 | Ứng viên | 1060 |
| 1077 | Hào Hùng Trảm Địa Liệt | Đánh đơn? (phạm vi?) | 150/21 | 1/0 | E | A/0 | Ứng viên | 1077 |
| 1084 | abc214 | Đánh đơn? (phạm vi?) | 150/21 | 1/0 | E | A/0 | Biến thể, chưa whitelist | 1084 |
| 1086 | abc216 | Đánh đơn? (phạm vi?) | 0/21 | -2/0 | E | A/0 | Phụ/biến thể? | 1086 |
| 1087 | abc217 | Đánh đơn? (phạm vi?) | 60/21 | 1/0 | E | A/0 | Biến thể, chưa whitelist | 1087 |
| 1088 | abc218 | Đánh đơn? (phạm vi?) | 0/21 | -2/0 | E | A/0 | Phụ/biến thể? | 1088 |
| 1149 | ncp4 | AOE (mô tả) | 80/20 | -2/0 | E | A/1 | Biến thể, chưa whitelist | 1149 |
| 1150 | ncp5 | AOE (mô tả) | 80/20 | -2/0 | E | A/1 | Biến thể, chưa whitelist | 1150 |
| 1151 | ncp6 | AOE (mô tả) | 80/20 | -2/0 | E | A/1 | Biến thể, chưa whitelist | 1151 |
| 1599 | Phá Thiên Trảm | Đánh đơn? (phạm vi?) | 1/60 | -2/0 | E | A/1 | Ứng viên | 1588 |

Số dòng trích: **52**. Các nhãn phạm vi? đều là **[CHƯA KIỂM]**; tên trùng khác ID không được gộp.

### 3. Đường Môn

| ID | Kỹ năng/chiêu thức | Loại theo data | Req/Max | E/H | Đích | Cast/style | Dấu hiệu | Dòng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | Đường Môn ám khí | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Ứng viên | 44 |
| 44 | Đường Môn Đao pháp | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Ứng viên | 45 |
| 45 | Tích Lịch đơn | AOE (mô tả) | 10/20 | -2/0 | E | A/0 | Ứng viên | 46 |
| 46 | Đao Nhận cơ quan (##) | AOE/bẫy? [CHƯA KIỂM] | 10/20 | -2/0 | — | X/4 | Nhãn (##) | 47 |
| 47 | Đoạt Hồn Tiêu | Đánh đơn? (phạm vi?) | 30/20 | 100/1 | E | A/0 | Ứng viên | 48 |
| 48 | Tâm Nhãn | Hỗ trợ bị động | 60/30 | -2/0 | — | P/3 | Ứng viên | 49 |
| 49 | Địa Diệm cơ quan (##) | AOE/bẫy? [CHƯA KIỂM] | 20/20 | -2/0 | — | X/4 | Nhãn (##) | 50 |
| 50 | Truy Tâm Tiễn | Đánh đơn? (phạm vi?) | 30/20 | 101/1 | E | A/0 | Ứng viên | 51 |
| 51 | Thanh Mộc (##) | Hỗ trợ bị động | 30/20 | -2/0 | — | P/3 | Nhãn (##) | 52 |
| 52 | Âm Lôi Cơ quan (##) | AOE/bẫy? [CHƯA KIỂM] | 30/20 | -2/0 | — | X/4 | Nhãn (##) | 53 |
| 54 | Mạn Thiên Hoa Vũ | AOE (mô tả) | 30/20 | 102/1 | E | A/0 | Ứng viên | 55 |
| 55 | Thối Độc Thuật | Hỗ trợ buff | 40/20 | -2/0 | S | A/2 | Ứng viên | 56 |
| 56 | Hàn Sương Cơ quan (##) | AOE/bẫy? [CHƯA KIỂM] | 40/20 | -2/0 | — | X/4 | Nhãn (##) | 57 |
| 57 | Băng Phách Hàn Quang | Hỗ trợ buff | 50/20 | -2/0 | S | A/2 | Ứng viên | 58 |
| 58 | Thiên La Địa Võng | AOE (mô tả) | 60/20 | 102/0 | E | A/0 | Ứng viên | 59 |
| 59 | Cửu Cung Địa Sát (##) | AOE/bẫy? [CHƯA KIỂM] | 50/20 | -2/0 | — | X/4 | Nhãn (##) | 60 |
| 227 | Thiên La Địa Võng tiểu Phi Đao | Đánh đơn? (phạm vi?) | 50/20 | -2/0 | E | A/0 | Ứng viên | 228 |
| 249 | Tiểu Lý Phi Đao | Đánh đơn? (phạm vi?) | 60/20 | 101/1 | E | A/0 | Ứng viên | 250 |
| 250 | Tiểu Lý Phi Đao | Đánh đơn? (phạm vi?) | 60/20 | 101/1 | E | A/0 | Ứng viên | 251 |
| 301 | Truy Tinh Trục Điện | AOE (mô tả) | 80/20 | -2/0 | E | A/0 | Ứng viên | 302 |
| 302 | Bạo Vũ Lê Hoa | AOE (mô tả) | 80/20 | 102/0 | E | A/0 | Ứng viên | 303 |
| 303 | Độc Thích Cốt | Đánh đơn? (phạm vi?) | 20/20 | -2/1 | E | A/0 | Ứng viên | 304 |
| 304 | Độc Thích Cốt | AOE (mô tả) | 60/30 | -2/1 | E | A/0 | Ứng viên | 305 |
| 339 | Nhiếp Hồn Nguyệt ảnh | Đánh đơn? (phạm vi?) | 80/20 | 101/1 | E | A/0 | Ứng viên | 340 |
| 340 | Ngân Đao Xạ Nguyệt | AOE (mô tả) | 80/20 | 101/1 | E | A/0 | Ứng viên | 341 |
| 341 | Tán Hoa Tiêu | Đánh đơn? (phạm vi?) | 60/20 | 100/1 | E | A/0 | Ứng viên | 342 |
| 342 | Cửu Cung Phi Tinh | AOE (mô tả) | 80/20 | 100/1 | E | A/0 | Ứng viên | 343 |
| 343 | Xuyên Tâm Thích | Đánh đơn? (phạm vi?) | 30/20 | -2/1 | E | A/0 | Ứng viên | 344 |
| 344 | Xuyên Tâm Thích | AOE (mô tả) | 60/30 | -2/1 | E | A/0 | Ứng viên | 345 |
| 345 | Hàn Băng Thích | Đánh đơn? (phạm vi?) | 40/20 | -2/1 | E | A/0 | Ứng viên | 346 |
| 346 | Hàn Băng Thích | AOE (mô tả) | 60/30 | -2/1 | E | A/0 | Ứng viên | 347 |
| 347 | Địa Diệm Hỏa | Đánh đơn? (phạm vi?) | 10/20 | -2/1 | E | A/0 | Ứng viên | 348 |
| 348 | Địa Diệm Hỏa | AOE (mô tả) | 60/30 | -2/1 | E | A/0 | Ứng viên | 349 |
| 349 | Lôi Kích Thuật | Đánh đơn? (phạm vi?) | 50/20 | -2/1 | E | A/0 | Ứng viên | 350 |
| 350 | Lôi Kích Thuật | AOE (mô tả) | 60/30 | -2/1 | E | A/0 | Ứng viên | 351 |
| 351 | Loạn Hoàn Kích | Đánh đơn? (phạm vi?) | 80/20 | -2/1 | E | A/0 | Ứng viên | 352 |
| 352 | Loạn Hoàn Kích | AOE (mô tả) | 60/30 | -2/1 | E | A/0 | Ứng viên | 353 |
| 710 | Mê ảnh Tung | Hỗ trợ di chuyển | 120/20 | -2/0 | — | M/1 | Ứng viên | 712 |
| 938 | abc158 | Đánh đơn? (phạm vi?) | 80/20 | -2/1 | E | A/0 | Biến thể, chưa whitelist | 938 |
| 1018 | abc193 | Đánh đơn? (phạm vi?) | 80/20 | -2/1 | E | A/0 | Biến thể, chưa whitelist | 1018 |
| 1069 | Vô ảnh Xuyên | AOE (mô tả) | 150/26 | 101/1 | E | A/0 | Ứng viên | 1069 |
| 1070 | Thiết Liên Tứ Sát | AOE (mô tả) | 150/26 | 102/0 | E | A/0 | Ứng viên | 1070 |
| 1071 | Càn Khôn Nhất Trịch | Đánh đơn? (phạm vi?) | 150/26 | 100/1 | E | A/0 | Ứng viên | 1071 |
| 1097 | Truy Tâm Tỏa Mệnh | Đánh đơn? (phạm vi?) | 150/20 | 101/1 | E | A/0 | Ứng viên | 1097 |
| 1098 | Thiết Sa Xạ Tinh | Đánh đơn? (phạm vi?) | 150/20 | -2/0 | E | A/0 | Ứng viên | 1098 |
| 1099 | abc224 | Đánh đơn? (phạm vi?) | 150/21 | 100/1 | E | A/0 | Biến thể, chưa whitelist | 1099 |
| 1100 | abc225 | Đánh đơn? (phạm vi?) | 150/21 | 100/1 | E | A/0 | Biến thể, chưa whitelist | 1100 |
| 1110 | Tích Lịch Loạn Hoàn Kích | Đánh đơn? (phạm vi?) | 150/26 | -2/1 | E | A/0 | Ứng viên | 1110 |
| 1113 | Tích Lịch Loạn Hoàn Hãm Tĩnh | Đánh đơn? (phạm vi?) | 80/21 | -2/1 | E | A/0 | Ứng viên | 1113 |
| 1132 | abc237 | AOE (mô tả) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 1132 |
| 1133 | abc238 | AOE (mô tả) | 0/20 | -2/0 | E | A/0 | Phụ/biến thể? | 1133 |
| 1136 | abc241 | Đánh đơn? (phạm vi?) | 50/20 | -2/1 | E | A/0 | Biến thể, chưa whitelist | 1136 |
| 1158 | ncp13 | AOE (mô tả) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1158 |
| 1159 | ncp14 | AOE (mô tả) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1159 |
| 1160 | ncp15 | Đánh đơn? (phạm vi?) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1160 |
| 1600 | Nhiếp Hồn Nguyệt ảnh | Đánh đơn? (phạm vi?) | 1/60 | -2/0 | E | A/0 | Ứng viên | 1589 |

Số dòng trích: **56**. Các nhãn phạm vi? đều là **[CHƯA KIỂM]**; tên trùng khác ID không được gộp.

### 4. Ngũ Độc

| ID | Kỹ năng/chiêu thức | Loại theo data | Req/Max | E/H | Đích | Cast/style | Dấu hiệu | Dòng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 | Ngũ Độc Đao pháp | Hỗ trợ bị động | 10/20 | 1/0 | — | P/3 | Ứng viên | 61 |
| 61 | Ngũ Độc Bổng pháp (##) | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Nhãn (##) | 62 |
| 62 | Ngũ Độc Chưởng Pháp | Hỗ trợ bị động | 10/20 | -2/0 | — | P/3 | Ứng viên | 63 |
| 63 | Độc Sa chưởng | Đánh đơn (mô tả) | 10/20 | -2/0 | E | A/0 | Ứng viên | 64 |
| 64 | Băng Lam Huyền Tinh | Hỗ trợ/debuff (phạm vi?) | 30/20 | -2/0 | E | A/0 | Ứng viên | 65 |
| 65 | Huyết Đao Độc Sát | Đánh đơn (mô tả) | 10/20 | 1/0 | E | A/0 | Ứng viên | 66 |
| 66 | Tạp Nan Dược Kinh | Hỗ trợ bị động | 20/20 | -2/0 | — | P/3 | Ứng viên | 67 |
| 67 | Cửu Thiên Cuồng Lôi | Hỗ trợ/debuff AOE (mô tả) | 10/20 | -2/0 | E | A/0 | Ứng viên | 68 |
| 68 | U Minh Khô Lâu | Đánh đơn? (phạm vi?) | 30/20 | -2/1 | E | A/0 | Ứng viên | 69 |
| 69 | Vô Hình Độc | AOE aura (data) | 30/20 | -2/0 | E | A/2 | Ứng viên | 70 |
| 70 | Xích Diệm Thực Thiên | Hỗ trợ/debuff (phạm vi?) | 20/20 | -2/0 | E | A/0 | Ứng viên | 71 |
| 71 | Thiên Cương Địa Sát | AOE (mô tả) | 60/20 | -2/1 | E | A/0 | Ứng viên | 72 |
| 72 | Xuyên Tâm Độc Thích | Hỗ trợ/debuff (phạm vi?) | 50/20 | -2/0 | E | A/0 | Ứng viên | 73 |
| 73 | Vạn Độc Thực Tâm | Hỗ trợ/debuff AOE (mô tả) | 40/20 | -2/0 | E | A/0 | Ứng viên | 74 |
| 74 | Chu Cáp Thanh Minh | Đánh đơn? (phạm vi?) | 60/20 | 1/0 | E | A/0 | Ứng viên | 75 |
| 75 | Ngũ Độc Kỳ Kinh | Hỗ trợ bị động | 60/30 | -2/0 | — | P/3 | Ứng viên | 76 |
| 76 | Di Hoa Tiếp Ngọc | Hỗ trợ buff | 50/20 | -2/0 | S | A/2 | Ứng viên | 77 |
| 195 | Thiên Cương Địa Sát | Đánh đơn? (phạm vi?) | 40/20 | -2/0 | E | A/0 | Ứng viên | 196 |
| 203 | Vô Hình Độc | Đánh đơn? (phạm vi?) | 30/20 | -2/0 | E | A/0 | Ứng viên | 204 |
| 353 | Âm Phong Thực Cốt | Đánh đơn? (phạm vi?) | 80/20 | -2/1 | E | A/0 | Ứng viên | 354 |
| 354 | Thiên Cương Độc Thủ | AOE (mô tả) | 80/20 | -2/1 | E | A/0 | Ứng viên | 355 |
| 355 | Huyền Âm Trảm | Đánh đơn? (phạm vi?) | 80/20 | 1/0 | E | A/0 | Ứng viên | 356 |
| 356 | Xuyên Y Phá Giáp | Hỗ trợ/debuff (phạm vi?) | 40/20 | -2/0 | E | A/0 | Ứng viên | 357 |
| 383 | Tinh Không Phá | AOE (mô tả) | 80/20 | -2/1 | E | A/0 | Ứng viên | 384 |
| 384 | Bách Độc Xuyên Tâm | Đánh đơn? (phạm vi?) | 30/20 | -2/0 | E | A/0 | Ứng viên | 385 |
| 388 | Truy Phong Độc Cát | Đánh đơn (mô tả) | 10/20 | -2/0 | E | A/0 | Ứng viên | 389 |
| 390 | Đoạn Cân Hủ Cốt | Hỗ trợ/debuff (phạm vi?) | 80/20 | -2/0 | E | A/0 | Ứng viên | 391 |
| 711 | Hấp Tinh Yểm | Hỗ trợ buff | 120/20 | -2/0 | S | P/3 | Ứng viên | 713 |
| 719 | Hấp Tinh Yểm_Quyết Chú | Đánh đơn? (phạm vi?) | 120/20 | -2/0 | E | A/0 | Phụ/biến thể? | 721 |
| 1066 | Hình Tiêu Cốt Lập | Đánh đơn? (phạm vi?) | 150/26 | -2/1 | E | A/0 | Ứng viên | 1066 |
| 1067 | U Hồn Phệ ảnh | Đánh đơn? (phạm vi?) | 150/26 | 1/0 | E | A/0 | Ứng viên | 1067 |
| 1068 | abc212 | Đánh đơn? (phạm vi?) | 150/20 | 1/0 | E | A/0 | Biến thể, chưa whitelist | 1068 |
| 1094 | abc222 | Đánh đơn? (phạm vi?) | 150/21 | -2/1 | E | A/0 | Biến thể, chưa whitelist | 1094 |
| 1095 | Hồn ảnh Tùng Sanh | Đánh đơn? (phạm vi?) | 150/20 | -2/1 | E | A/0 | Ứng viên | 1095 |
| 1096 | abc223 | Đánh đơn? (phạm vi?) | 150/21 | -2/1 | E | A/0 | Biến thể, chưa whitelist | 1096 |
| 1156 | ncp11 | Đánh đơn? (phạm vi?) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1156 |
| 1157 | ncp12 | Đánh đơn? (phạm vi?) | 80/20 | -2/0 | E | A/0 | Biến thể, chưa whitelist | 1157 |
| 1175 | abc255 | Đánh đơn? (phạm vi?) | 0/20 | -2/1 | E | A/0 | Phụ/biến thể? | 1175 |
| 1176 | abc256 | Đánh đơn? (phạm vi?) | 0/20 | -2/1 | E | A/0 | Phụ/biến thể? | 1176 |
| 1177 | abc257 | Đánh đơn? (phạm vi?) | 0/20 | -2/1 | E | A/0 | Phụ/biến thể? | 1177 |
| 1232 | Hồn ảnh Tùng Sanh | Đánh đơn? (phạm vi?) | 120/20 | -2/1 | E | A/0 | Ứng viên | 1232 |

Số dòng trích: **41**. Các nhãn phạm vi? đều là **[CHƯA KIỂM]**; tên trùng khác ID không được gộp.

## Bảng chọn ứng viên cho thiết kế hảo hữu

Tất cả dưới đây là **[ĐỀ XUẤT]**, cần kiểm riêng trong task triển khai; không gán đồng loạt 196 dòng cho NPC. Ưu tiên ID gốc có tên/mô tả rõ, tránh `(##)`, `abc`, biến thể `ncp` dù tên gợi ý dành NPC.

| Phái | Đánh đơn để khảo sát trước | AOE để khảo sát trước | Hỗ trợ để khảo sát trước | Điểm cần chốt |
| --- | --- | --- | --- | --- |
| Thiếu Lâm | 10 Kim Cang Phục Ma (Req 10) | 11 Hoành Tảo Lục Hợp (50) | 12 Kim Cang Hộ Thể (20, passive), 16 La Hán Trận (30, aura) | Đường melee/skill con, handler phòng thủ và aura có áp đúng con/đồng minh. |
| Thiên Vương | 29 Trảm Long quyết, 30 Hồi Phong Lạc Nhạn (10) | 1058 Hào Hùng Trảm (150, mô tả tỏa ba hướng) | 33 Tĩnh Tâm Quyết (20), 42 Kim Chung Tráo (50) | Nhiều đòn không tự là AOE; giữ riêng ID chính và biến thể Req=1/Max=60 mang ID 1599. |
| Đường Môn | 50 Truy Tâm Tiễn (30, target-only), 47 Đoạt Hồn Tiêu (30, phạm vi còn cần kiểm) | 302 Bạo Vũ Lê Hoa (80) | 55 Thối Độc Thuật (40), 57 Băng Phách Hàn Quang (50) | Luật vũ khí riêng hảo hữu; bẫy/event có đường khác, không dùng style 4 trực tiếp qua AI thường. |
| Ngũ Độc | 63 Độc Sa chưởng, 65 Huyết Đao Độc Sát (10) | 71 Thiên Cương Địa Sát (60), 69 Vô Hình Độc (30, aura) | 66 Tạp Nan Dược Kinh (20, passive), 76 Di Hoa Tiếp Ngọc (50) | Poison tick, cộng dồn, phản đòn và quan hệ mục tiêu cần đối chiếu handler/Lua. |

Các số Req trong bảng là data tham khảo; thiết kế mới phải định nghĩa cách mở khóa, level skill, cấp hảo hữu, giới hạn số ô/chiêu active/passive và lưu theo ID con. Không dùng phái/cấp/vũ khí của chủ thay cho thuộc tính con. Cooldown cần chính sách vì Cost gốc không tiêu tài nguyên của partner; chưa đề xuất hệ số mới. Đường DoOrdinSkill còn phụ thuộc frame/attack/cast speed và CastMeleeSkill (S/KNpc.cpp:3786–3837), nên có skill trong list không bảo đảm model có animation phù hợp.

## Kiểm chứng, lỗi và bàn giao

- Git kiểm một lần trước ghi: branch `task/A-15a`; có sẵn `?? JX1_OPS/TASKS/A-15a.md`. Giữ nguyên nội dung task ngoài mục Kết quả cuối file. Phạm vi ghi: báo cáo này và mục Kết quả được task yêu cầu rõ; không sửa A-12/A-14/BAI_HOC hoặc source.
- Đã đối chiếu trực tiếp thứ tự section, tên/ID/điều kiện trong Skills.txt, symbol và dòng cast dẫn ở trên; catalog ghi đủ 47+52+56+41=196 dòng theo tiêu chí trích công khai. Phân loại chưa chắc chắn có nhãn, không biến mô tả data thành kết quả runtime. Chưa kiểm whitelist phái chính thức và điều kiện học nâng cao; không gọi catalog là danh sách học hoàn chỉnh.
- Lỗi đã xử lý trong cùng lượt: đọc PowerShell mặc định làm lỗi dấu → đọc UTF-8 cho Markdown; đường `D:\JX-source\SwordOnline` thiếu → dùng source copy mà A-14 dẫn và data A-12; `rg : The term 'rg' is not recognized ...` → chuyển Select-String/ReadAllLines, không cài thêm; xuất gộp bị rút gọn → thu hẹp trường/dòng; xuất Python qua pipe mất dấu → trích catalog bằng PowerShell + ánh xạ TCVN3; đường đoán `Headers/CoreUseNameDef.h` không tồn tại → không thử lặp hoặc suy thiếu chức năng. Không có lỗi nào dẫn đến sửa source/quyền/config.
- Đã xem diff hai file; kiểm cấu trúc đạt 196 dòng catalog, 5 dòng tóm tắt và một mục Kết quả. Kiểm whitespace phát hiện một dòng trắng cuối báo cáo, đã bỏ rồi kiểm lại. Bước kiểm đầu đã hiểu nhầm mã thoát 1 của git diff --no-index --check là lỗi dù không còn chẩn đoán; đã sửa cách đánh giá theo chẩn đoán whitespace. Đối chiếu tự động ID/Req/Max/Eqt/Horse/Style theo dòng nguồn đạt 196/196. Đây là kiểm tài liệu, không phải test game.
- **[CHƯA KIỂM]** Không chạy test/build/exe game/server, VM, DB/network, Lua hay PAK; không xác nhận source/data khớp binary. Chưa có bằng chứng AI tự chọn từng chiêu, học/lưu skill theo từng hảo hữu, mọi hiệu ứng có tác dụng hoặc client hiển thị đúng. Các mục này cần task riêng được phép thực nghiệm; khảo sát này không có blocker để giao bảng ứng viên.
- Trạng thái cuối: **DONE — khảo sát tĩnh**, kèm các mục **[CHƯA KIỂM]** nêu trên. Commit SHA/link: **không có**; không stage/commit/push vì task không yêu cầu. Giữ kết quả local để duyệt.
