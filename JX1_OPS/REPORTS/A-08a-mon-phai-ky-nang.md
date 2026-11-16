TÓM TẮT 1: Có 16 mục môn phái [0]–[15] trong cả hai INI; gồm cả “Tự sáng môn phái”, chưa chứng minh 16 phái chơi được (G/Settings/faction/MonPhai.ini:6–84).
TÓM TẮT 2: Header gia nhập chỉ có 11 phái, hệ lần lượt 2 Kim, 2 Mộc, 3 Thủy, 2 Hỏa, 2 Thổ; không thể chốt giả định 15 phái (G/script/header/factionhead.lua:5–17).
TÓM TẮT 3: Đã đối chiếu các nhánh kỹ năng 90 của 11 phái với Skills/Missles; tầm gốc, số đạn và vùng va chạm được tách riêng (G/Settings/Skills.txt:1; G/Settings/Missles.txt:1).
TÓM TẮT 4: Nga My có hồi máu/hồi nội lực/trợ lực; ID 1661 sai tên so với header, ID 1702 không có trong Skills; năm mục INI bổ sung chưa đủ dữ liệu phân vai (G/script/skill/emei.lua:176–180; G/script/header/factionhead.lua:391–395; E01).
TÓM TẮT 5: Kiểm tra tĩnh, không build/chạy exe/kết nối VM/SQL/server; số mục tiêu mỗi lần tung chiêu và danh sách phái vận hành còn chưa kiểm (S/KMissle.cpp:1830–1866; JX1_OPS/TASKS/A-08a.md:16,27–28).

# A-08a — Môn phái và kỹ năng

Ngày kiểm: 17/11/2026. **Trạng thái nội dung: PARTIAL** — đã lập đầy đủ danh sách khai báo và bảng đối chiếu; bất nhất dữ liệu không cho phép xác nhận mọi phái/kỹ năng hoạt động. Không suy runtime từ source.

## Worker kiểm tra trước khi làm

- Đã đọc task trước khi điều tra. `Get-Location` = `D:\JX-wt\A-08a`; `git status --short --branch` = `## task/A-08a-codex`, không có thay đổi local; khớp `JX1_OPS/TASKS/A-08a.md:7–8`.
- Chỉ ghi báo cáo này và mục Kết quả của task theo yêu cầu trực tiếp của người dùng. `C:\Jx1CocoV3` chỉ đọc; không chạy exe, build, kết nối VM/SQL/server, không sửa canonical (task:15–16,23–28).
- Đã đọc hai báo cáo nền được chỉ định: A-03 chỉ kiểm kê cây source nên kết quả Lua/INI=0 không áp dụng cho gói gs; D-01 đã xác định gói runtime trong Folder có script (`JX1_OPS/REPORTS/A-03-kiem-ke-cau-hinh.md:1–9`; `JX1_OPS/REPORTS/D-01-bang-hoat-dong.md:1–5`).
- Đã đọc tài liệu chủ dự án tại `D:\jx1-ops-wt\JX1_OPS\owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md:3` và `DESIGN/HAO-HUU-CUNG.md:3–8`: “15 phái” là ví dụ, mục tiêu là chọn hảo hữu theo đơn mục tiêu/AOE; chưa triển khai hệ thống hảo hữu trong task này.

## Gốc bằng chứng và mã hóa

`G/` = `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\`.
`S/` = `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\`.
Số dòng vật lý tính từ 1; bảng TAB giữ nguyên ô rỗng, tra bằng cột SkillId/MissleId, không coi số dòng là ID (ví dụ ID 1661 ở Skills.txt:1649).

INI/header chứa cả GBK (tên Hán/hệ) và chuỗi Việt legacy TCVN3: đọc toàn file bằng GBK không khôi phục đúng tên Việt. Dùng GBK cho `MonPhai.ini`/Hán tự, đối chiếu các byte Việt bằng Windows-1252 để nhận dạng TCVN3 rồi ghi tên Việt chuẩn hóa; giữ Hán tự và ID để kiểm lại. Ví dụ `§¹t Ma §é Giang` = Đạt Ma Độ Giang (G/script/header/factionhead.lua:340), `少林派` = Thiếu Lâm (G/Settings/faction/MonPhai.ini:7). Không chuyển mã hay ghi lại nguồn.

## Danh sách môn phái chính xác theo từng nguồn

Có **16 mục khai báo**, không tính section `[Name]`: Kim 3, Mộc 3, Thủy 4, Hỏa 3, Thổ 3. Có **11 mục gia nhập trong FACTION_INFO**; `gianhapmonphai` dùng chỉ số `newfac+1`, rồi SetFaction/SetCamp/học SKILLNORMAL (G/Settings/faction/MonPhai.ini:6–84; G/script/header/factionhead.lua:5–26,106–110).

| ID INI | Tên Việt chuẩn hóa / tên gốc | Hệ | Có FACTION_INFO | Bằng chứng |
| --- | --- | --- | --- | --- |
| 0 | Thiếu Lâm / 少林派 | Kim | Có, dòng 6 | G/Settings/faction/MonPhai.ini:6–9; G/Settings/faction/faction.ini:7–9 |
| 1 | Thiên Vương / 天王帮 | Kim | Có, dòng 7 | G/Settings/faction/MonPhai.ini:11–14; G/Settings/faction/faction.ini:14–16 |
| 2 | Đường Môn / 唐门 | Mộc | Có, dòng 8 | G/Settings/faction/MonPhai.ini:16–19; G/Settings/faction/faction.ini:21–23 |
| 3 | Ngũ Độc / 五毒教 | Mộc | Có, dòng 9 | G/Settings/faction/MonPhai.ini:21–24; G/Settings/faction/faction.ini:28–30 |
| 4 | Nga My / 峨嵋派 | Thủy | Có, dòng 10 | G/Settings/faction/MonPhai.ini:26–29; G/Settings/faction/faction.ini:35–37 |
| 5 | Thúy Yên / 翠烟门 | Thủy | Có, dòng 11 | G/Settings/faction/MonPhai.ini:31–34; G/Settings/faction/faction.ini:42–44 |
| 6 | Cái Bang / 丐帮 | Hỏa | Có, dòng 12 | G/Settings/faction/MonPhai.ini:36–39; G/Settings/faction/faction.ini:49–51 |
| 7 | Thiên Nhẫn / 天忍教 | Hỏa | Có, dòng 13 | G/Settings/faction/MonPhai.ini:41–44; G/Settings/faction/faction.ini:56–58 |
| 8 | Võ Đang / 武当派 | Thổ | Có, dòng 14 | G/Settings/faction/MonPhai.ini:46–49; G/Settings/faction/faction.ini:63–65 |
| 9 | Côn Lôn / 昆仑派 | Thổ | Có, dòng 15 | G/Settings/faction/MonPhai.ini:51–54; G/Settings/faction/faction.ini:70–72 |
| 10 | Hoa Sơn / 华山派 | Thủy | Có, dòng 16 | G/Settings/faction/MonPhai.ini:56–59; G/Settings/faction/faction.ini:77–79 |
| 11 | Lý Tầm Hoan / 李寻欢 | Mộc | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:61–64; G/Settings/faction/faction.ini:84–86 |
| 12 | Đào Hoa Đảo / 桃花岛 | Thủy | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:66–69; G/Settings/faction/faction.ini:89–91 |
| 13 | Minh Giáo / 明教 | Hỏa | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:71–74; G/Settings/faction/faction.ini:94–96 |
| 14 | Đoàn Thị / 段氏 | Thổ | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:76–79; G/Settings/faction/faction.ini:99–101 |
| 15 | Tự sáng môn phái / 自创门派 | Kim | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:81–84; G/Settings/faction/faction.ini:104–106 |

**Không gán kỹ năng theo vị trí các mảng mở rộng:** SKILLNORMAL chỉ có [1]–[10]; SKILL90_ARRAY có [1]–[13], nhưng [12] ghi “Minh Giáo kiếm” (1661), [13] ghi “Nghênh Phật Tây Thiên” (1702), không khớp INI [11]=Lý Tầm Hoan, [12]=Đào Hoa Đảo khi dùng `+1`. SKILL150_ARRAY lại chỉ có 10 nhóm. Đây là bất nhất dữ liệu, không phải bằng chứng 13/15/16 phái đã chơi được (G/script/header/factionhead.lua:172–335,338–397,404–449).

## Cách phân loại kỹ năng và số mục tiêu

- Chọn **nhánh kỹ năng 90** làm nhóm tấn công chính để so sánh nhất quán, không khẳng định mạnh nhất/meta; tên và nhánh vũ khí lấy từ SKILL90_ARRAY (G/script/header/factionhead.lua:338–389). Kỹ năng 150 có khai báo riêng, chưa truy toàn bộ (cùng file:404–449).
- `T` = AttackRadius gốc trong Skills.txt, đơn vị nội bộ; không đổi sang mét hoặc gọi là bán kính AOE. Lua có thể ghi đè, engine còn chặn theo nAttackRadius toàn cục (S/KSkills.cpp:3031–3036,3643–3650). Ví dụ 328: T gốc 360 nhưng Lua ghi 448 ở cấp 1, 512 ở cấp 20 (G/script/skill/emei.lua:182–191); 353: T gốc 420 nhưng Lua ghi 448→480 (G/script/skill/wudu.lua:188–192).
- `C` = ChildSkillNum gốc, `R` = DmgRange của mẫu đạn, **không phải số người trúng**. Engine dùng C để sinh đạn/kỹ năng con; các dạng 0=tường, 1=đường, 2=tỏa, 3=vòng, 6=tại mục tiêu, 7=tại người dùng (S/KSkills.cpp:1725–1726,2989–2990; S/SkillDef.h:120–127).
- Nhãn **AOE vùng**: R>1; **AOE nhiều đạn**: C>1, có thể trúng nhiều mục tiêu theo vị trí; **đơn va chạm**: C=1/R=1, chỉ xét một ô mỗi lần va chạm, chưa bảo đảm cả lần tung chiêu chỉ trúng một người. Đạn có thể xuyên/va chạm lại hoặc phát sinh skill event (G/Settings/Missles.txt:1; S/KMissle.cpp:1800–1803,1830–1851; S/KSkills.cpp:3007–3010).
- Lưu ý cờ IsRangeDmg không luôn khớp R: đạn 96/181 có IsRangeDmg=0 nhưng R=2; ProcessCollision đang đọc nRange trực tiếp để quét ô. Phân loại vùng ở đây bám đường xử lý source, chưa xác nhận binary dùng cùng nhánh (G/Settings/Missles.txt:97,182; S/KMissle.cpp:1830–1851,1997).
- **Số mục tiêu chính xác mỗi lần tung chiêu: chưa xác minh cho mọi dòng.** Trong một lần ProcessCollision, vòng lặp quét `(2*floor(R/2)+1)^2` ô, gọi FindNpc rồi ProcessDamage; chỉ dừng sớm theo m_nHitCount khi giá trị >0. Đây là số ô tối đa được xét, không phải số người trúng cố định hay tổng mục tiêu của cả chiêu; m_nHitCount khởi tạo 0 và còn có thể được sửa (S/KMissle.cpp:249,1802–1803,1830–1866).
- `E` = EqtLimit gốc. `-2` là không giới hạn vũ khí, `-1` là tay không trong phần mô tả engine (S/KSkills.cpp:4246–4253); tên nhánh như chưởng/đao không thay thế giới hạn thực tế. Các mã còn lại được giữ kèm tên nhánh trong header, chưa kiểm toàn bộ bảng WeaponLimit.

## Kỹ năng tấn công chính của 11 phái có header

Mỗi dòng dưới có vai trò **sát thương** theo các thuộc tính damage/enhance và TargetEnemy=1 trong chính dòng Skills.txt; “đơn” chỉ là đơn va chạm theo định nghĩa trên. Chỉ số C/R là giá trị gốc trước Lua/event.

| Phái | Kỹ năng (ID), nhánh / E | Phân loại tĩnh; T; C; R | Bằng chứng Skills / mẫu đạn |
| --- | --- | --- | --- |
| Thiếu Lâm | Đạt Ma Độ Giang (318), quyền / -1 | AOE vùng; T=90; C=2; R=3 | G/Settings/Skills.txt:319; G/Settings/Missles.txt:318 (ID 317) |
| Thiếu Lâm | Hoành Tảo Thiên Quân (319), côn / 2 | AOE vùng; T=75; C=1; R=6 | G/Settings/Skills.txt:320; G/Settings/Missles.txt:136 (ID 135) |
| Thiếu Lâm | Vô Tướng Trảm (321), đao / 1 | AOE nhiều đạn theo đường; T=400; C=2; R=1 | G/Settings/Skills.txt:322; G/Settings/Missles.txt:137 (ID 136) |
| Thiên Vương | Phá Thiên Trảm (322), đao / 1 | Đơn va chạm; T=90; C=1; R=1 | G/Settings/Skills.txt:323; G/Settings/Missles.txt:327 (ID 326) |
| Thiên Vương | Truy Tinh Trục Nguyệt (323), thương / 3 | AOE nhiều đạn; T=90; C=5; R=1 | G/Settings/Skills.txt:324; G/Settings/Missles.txt:328 (ID 327) |
| Thiên Vương | Truy Phong Quyết (325), chùy / 4 | AOE vùng; T=72; C=1; R=5 | G/Settings/Skills.txt:326; G/Settings/Missles.txt:409 (ID 408) |
| Đường Môn | Nhiếp Hồn Nguyệt Ảnh (339), phi đao / 101 | Đơn va chạm, đạn không mất khi va chạm; T=360; C=1; R=1 | G/Settings/Skills.txt:340; G/Settings/Missles.txt:150 (ID 149) |
| Đường Môn | Cửu Cung Phi Tinh (342), phi tiêu / 100 | AOE nhiều đạn tỏa; T=360; C=5; R=1 | G/Settings/Skills.txt:343; G/Settings/Missles.txt:153 (ID 152) |
| Đường Môn | Bạo Vũ Lê Hoa (302), tụ tiễn / 102 | AOE vùng theo R=2 của source, đạn không mất khi va chạm; T=470; C=1; R=2 | G/Settings/Skills.txt:303; G/Settings/Missles.txt:97 (ID 96) |
| Đường Môn | Loạn Hoàn Kích (351), hãm tĩnh / -2 | AOE vùng (bẫy); T=50; C=1; R=2 | G/Settings/Skills.txt:352; G/Settings/Missles.txt:162 (ID 161) |
| Ngũ Độc | Âm Phong Thực Cốt (353), chưởng / -2 | AOE vùng, độc; T=420; C=1; R=3 | G/Settings/Skills.txt:354; G/Settings/Missles.txt:164 (ID 163) |
| Ngũ Độc | Huyền Âm Trảm (355), đao / 1 | AOE nhiều đạn, độc; T=180; C=2; R=1 | G/Settings/Skills.txt:356; G/Settings/Missles.txt:166 (ID 165) |
| Nga My | Tam Nga Tề Tuyết (328), kiếm / 0 | AOE nhiều đạn dạng tường; T=360; C=3; R=1 | G/Settings/Skills.txt:329; G/Settings/Missles.txt:143 (ID 142) |
| Nga My | Phong Sương Toái Ảnh (380), chưởng / -2 | AOE vùng; T=480; C=1; R=3 | G/Settings/Skills.txt:381; G/Settings/Missles.txt:187 (ID 186) |
| Thúy Yên | Băng Tung Vô Ảnh (336), đao / 1 | AOE nhiều đạn tỏa; T=360; C=5; R=1 | G/Settings/Skills.txt:337; G/Settings/Missles.txt:147 (ID 146) |
| Thúy Yên | Băng Tâm Tiên Tử (337), chưởng / -2 | Đơn va chạm, đạn không mất khi va chạm; T=240; C=1; R=1 | G/Settings/Skills.txt:338; G/Settings/Missles.txt:148 (ID 147) |
| Cái Bang | Phi Long Tại Thiên (357), chưởng / -2 | AOE nhiều đạn dạng tường; T=400; C=3; R=1 | G/Settings/Skills.txt:358; G/Settings/Missles.txt:167 (ID 166) |
| Cái Bang | Thiên Hạ Vô Cẩu (359), bổng / 2 | AOE nhiều đạn dạng tường; T=400; C=16; R=1 | G/Settings/Skills.txt:360; G/Settings/Missles.txt:169 (ID 168) |
| Thiên Nhẫn | Vân Long Kích (361), mâu / 3 | Đơn va chạm, đạn không mất khi va chạm; T=60; C=1; R=1 | G/Settings/Skills.txt:362; G/Settings/Missles.txt:170 (ID 169) |
| Thiên Nhẫn | Thiên Ngoại Lưu Tinh (362), chưởng / -2 | Đơn va chạm; cần truy event để chốt AOE cả chiêu; T=420; C=1; R=1 | G/Settings/Skills.txt:363; G/Settings/Missles.txt:172 (ID 171) |
| Võ Đang | Thiên Địa Vô Cực (365), chưởng / -2 | AOE vùng; T=470; C=1; R=4 | G/Settings/Skills.txt:366; G/Settings/Missles.txt:174 (ID 173) |
| Võ Đang | Nhân Kiếm Hợp Nhất (368), kiếm / 0 | AOE nhiều đạn theo đường; T=90; C=3; R=1 | G/Settings/Skills.txt:369; G/Settings/Missles.txt:176 (ID 175) |
| Côn Lôn | Ngạo Tuyết Tiêu Phong (372), đao / 1 | AOE vùng; T=400; C=1; R=4 | G/Settings/Skills.txt:373; G/Settings/Missles.txt:179 (ID 178) |
| Côn Lôn | Lôi Động Cửu Thiên (375), chưởng / -2 | AOE nhiều đạn; có event cần truy tiếp; T=470; C=4; R=2 | G/Settings/Skills.txt:376; G/Settings/Missles.txt:182 (ID 181) |
| Hoa Sơn | Đoạt Mệnh Liên Hoàn Tam Tiên Kiếm (chiêu sát thương con) (1363), kiếm / 0 | AOE nhiều đạn tỏa; T=480; C=3; R=1 | G/Settings/Skills.txt:1363; G/Settings/Missles.txt:419 (ID 418) |
| Hoa Sơn | Phách Thạch Phá Ngọc (1382), khí (header) / 0 | AOE vùng + nhiều đạn; T=380; C=3; R=3 | G/Settings/Skills.txt:1382; G/Settings/Missles.txt:427 (ID 426) |

**Hoa Sơn cần phân biệt nút và chiêu sát thương:** header trỏ 1364; Skills 1364 là TargetSelf=1/TargetEnemy=0, autoreplyskill trong Lua mã hóa sang 1363. Do đó không coi T=0 của 1364 là tầm đánh của cả nhánh. ID 1363 có T=480/C=3; phần liên kết autoreply vẫn cần kiểm runtime (G/script/header/factionhead.lua:388; G/Settings/Skills.txt:1363–1364; G/script/skill/huashan.lua:252–255).

## Vai trò hồi máu, trợ lực và năm mục bổ sung

Với 11 phái trên, vai trò sát thương đã có bằng chứng từng nhánh; bảng dưới ghi thêm vai trò quan sát được, không kết luận những phái còn lại hoàn toàn không có buff/hồi phục.

| Phái / nhóm | Vai trò và giới hạn kết luận | Bằng chứng |
| --- | --- | --- |
| Nga My | Sát thương + **hồi máu/hồi nội lực/trợ lực** qua Phổ Độ Chúng Sinh (332): T gốc 180, E=-2, TargetAlly=1/TargetSelf=1, TargetEnemy=0; tăng hồi máu, hồi nội lực, kháng và phục hồi sau trúng đòn. Số đồng đội hưởng mỗi lần chưa chốt. | G/script/header/factionhead.lua:361–363; G/Settings/Skills.txt:333; G/script/skill/emei.lua:176–180 |
| Ngũ Độc | Sát thương độc; thêm nhánh bùa Đoạn Cân Hủ Cốt (390), T=440, TargetOnly=1/TargetEnemy=1, các thuộc tính allres_p/allresmax_p. Chưa kiểm đầy đủ trị số để chốt mức suy yếu. | G/script/header/factionhead.lua:356–358; G/Settings/Skills.txt:391 |
| Thiên Nhẫn | Sát thương; Nhiếp Hồn Loạn Tâm (391), T=440/E=-2 là nhánh bùa. Lua có các giá trị hồi máu âm và hiệu ứng quần thể với missle_hitcount=6; chưa coi 6 là trần toàn bộ chiêu nếu chưa nối đủ event. | G/script/header/factionhead.lua:374–376; G/Settings/Skills.txt:392; G/script/skill/tianren.lua:243–276 |
| Côn Lôn | Sát thương; thêm nhánh bùa Túy Tiên Tá Cốt (394), T=440/E=-2. Vai trò hiệu ứng/khống chế cần đối chiếu toàn nhánh; không ghi là hồi máu chỉ từ tên thuộc tính. | G/script/header/factionhead.lua:383–385; G/Settings/Skills.txt:395 |
| Thiếu Lâm, Thiên Vương, Đường Môn, Thúy Yên, Cái Bang, Võ Đang, Hoa Sơn | Có nhánh sát thương trong bảng trên; chưa kiểm hết buff/hồi phục để gán vai trò phụ hoặc xếp hạng cho hảo hữu. | G/script/header/factionhead.lua:340–353,366–380,387–389; các dòng Skills trong bảng tấn công |
| Lý Tầm Hoan (INI 11) | Chưa xác định kỹ năng tấn công, đơn/AOE, tầm, số mục tiêu, vũ khí, vai trò. Header gia nhập không có mục; SKILL90 [12] lại ghi Minh Giáo nên không gán nhầm. | G/Settings/faction/MonPhai.ini:61–64; G/script/header/factionhead.lua:5–17,391–393 |
| Đào Hoa Đảo (INI 12) | Chưa xác định các trường kỹ năng/vai trò; SKILL90 [13] trỏ 1702 nhưng không có dòng SkillId tương ứng trong bảng đã đọc. | G/Settings/faction/MonPhai.ini:66–69; G/script/header/factionhead.lua:394–395; E01 |
| Minh Giáo (INI 13) | Header có nhãn Thánh Hỏa Liêu Nguyên (1661), nhưng Skills 1661 là bachchienbachthang, TargetSelf=1/TargetEnemy=0, script vongevent.lua. Không xác nhận đây là chiêu sát thương Minh Giáo; mọi trường phân loại/tầm/vũ khí/số mục tiêu của phái còn chưa kiểm. | G/Settings/faction/MonPhai.ini:71–74; G/script/header/factionhead.lua:392; G/Settings/Skills.txt:1649 |
| Đoàn Thị (INI 14) | Chưa có ánh xạ kỹ năng đủ bằng chứng; đơn/AOE, tầm, số mục tiêu, vũ khí, vai trò chưa kiểm. | G/Settings/faction/MonPhai.ini:76–79; G/script/header/factionhead.lua:5–17,338–397 |
| Tự sáng môn phái (INI 15) | Là mục khai báo riêng; chưa chứng minh là một phái cố định cho người chơi, chưa xác định bộ kỹ năng/vũ khí/vai trò. | G/Settings/faction/MonPhai.ini:81–84; G/Settings/faction/faction.ini:103–106; G/script/header/factionhead.lua:5–17 |

**E01 — kiểm trực tiếp bảng:** đọc toàn `G/Settings/Skills.txt` (1721 dòng kể cả dòng rỗng cuối), tách TAB theo header dòng 1: số dòng có SkillId=1702 là 0; SkillId=1661 nằm tại dòng 1649, tên bachchienbachthang. Đây là bằng chứng vắng mặt trong file rời này, không chứng minh vắng trong PAK hoặc bản triển khai khác.

## Chưa kiểm

- Phái nào thực sự gia nhập được trên bản triển khai; số phái chơi được chưa chốt. Không lấy 16 mục cấu hình để cam kết 15 hảo hữu/người chơi hoặc lấy 11 mục header để kết luận chỉ có 11 phái trong game (các bất nhất nêu trên).
- Bộ kỹ năng đúng của Lý Tầm Hoan, Đào Hoa Đảo, Minh Giáo, Đoàn Thị, Tự sáng môn phái; nguồn/ánh xạ thay thế cho 1661 và 1702. Giữ tên/ID hiện có, không tự sửa canonical.
- Toàn bộ chuỗi skill con/Start/Fly/Collide/Vanished event, các ghi đè theo cấp, số lần va chạm, trần hitcount từng cấp, tầm hiệu lực cuối cùng và số mục tiêu khác nhau mỗi lần tung chiêu; nhãn đơn/AOE trong bảng là phân loại cấu trúc tĩnh.
- Tất cả kỹ năng 1–89/120/150 và kỹ năng mở rộng; buff/hồi phục phụ của từng phái, tốc đánh/hồi chiêu, hệ số sát thương, hiệu quả boss/Tống Kim, AI và cân bằng hảo hữu. Chưa đủ bằng chứng xếp hạng DPS hoặc chọn đội hình cuối cùng.
- Ưu tiên PAK/file rời, binary có khớp source không, bảng WeaponLimit và đơn vị hiển thị client. Không build/test game, không chạy exe hoặc kết nối VM/SQL/server theo task.

## Lỗi đã gặp và cách xử lý

| Lỗi | Đã thử / kết quả / phần còn tồn tại |
| --- | --- |
| PowerShell Get-Content mặc định làm chữ Việt Markdown hiển thị sai, đầu ra gộp bị rút gọn | Đọc lại các đoạn nền cần thiết bằng UTF-8 trong Node; không ghi lại nguồn. |
| `The encoded data was not valid for encoding gbk` | Decoder GBK nghiêm ngặt không nhận toàn file trộn chuỗi Việt legacy; dùng GBK cho phần Hán, Windows-1252 cho nhận dạng byte TCVN3, ASCII cho ID/token; không dùng chữ lỗi GBK làm tên Việt. |
| `rg : The term 'rg' is not recognized ...` | Thử một lần, chuyển sang đọc file trực tiếp và lọc dòng trong phiên công cụ; không cài thêm công cụ. |
| `ENOENT ... Core\Src\KSkill.cpp` | Kiểm tra tên trong đúng thư mục Core/Src, tìm được KSkills.cpp rồi đọc; không mở rộng khảo sát toàn repo. |

## Kiểm chứng và bàn giao

Đã đọc lại báo cáo, đối chiếu nguồn theo số dòng và rà diff theo phạm vi. Đây là rà tài liệu, không phải build/test game. Không tạo script phụ hoặc sửa BAI_HOC. Bước tiếp theo là xác nhận dữ liệu mở rộng/chuỗi event trên nguồn được duyệt trước khi thiết kế danh sách hảo hữu.

**Commit: BLOCKED — BỊ CHẶN – CHƯA PUSH.** Chưa có commit SHA hoặc link GitHub mới. Lệnh stage đã thử một lần, exit 1:

~~~text
git add -- JX1_OPS/REPORTS/A-08a-mon-phai-ky-nang.md JX1_OPS/TASKS/A-08a.md
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/A-08a/index.lock': Permission denied
~~~

Git metadata ở ngoài writable root của phiên; không được nâng quyền. Không đổi ACL/credential/config, không dùng index hoặc repository thay thế. Stage chưa thành công nên chưa chạy commit; không push vì chỉ được yêu cầu commit. Trạng thái bàn giao **PARTIAL**: đã có báo cáo, còn thiếu xác minh nêu trong Chưa kiểm và commit bị chặn.

PM gộp hoặc phiên có quyền ghi metadata tiếp tục từ đúng hai file local trên nhánh đã xác nhận:

~~~text
git -C "D:\JX-wt\A-08a" add -- JX1_OPS/REPORTS/A-08a-mon-phai-ky-nang.md JX1_OPS/TASKS/A-08a.md
git -C "D:\JX-wt\A-08a" commit -m "A-08a Kiem ke mon phai va ky nang"
~~~

Sau đó ghi SHA vào bàn giao; không cần đọc lại toàn bộ workflow hoặc khảo sát lại nguồn đã có bằng chứng.
