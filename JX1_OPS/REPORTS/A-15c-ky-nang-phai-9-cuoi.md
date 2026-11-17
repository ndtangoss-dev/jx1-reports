T?M T?T 1: [NGU?N] Danh s?ch ph?i trong Settings/faction/faction.ini c? m?c 9?15: C?n L?n, Hoa S?n, L? T?m Hoan, ??o Hoa ??o, Minh Gi?o, ?o?n Th?, T? t?o m?n ph?i.
T?M T?T 2: [NGU?N] Skills.txt c? 52 record g?n `kunlun.lua` (ID 90, 167?184, 275?276, 372?400, 630, 656, 704, 717, 721?722, 1080?1109, 1134?1168, 1796/1799) v? 47 record g?n `huashan.lua` (ID 1347?1385, 1410?1414, 1419?1421).
T?M T?T 3: [NGU?N] SkillStyle=0 l? chi?u ch? ??ng/??nh; =2 l? h? tr? ch? ??ng/AOE ho?c tr?ng th?i; =3 l? b? ??ng/h? tr?; =13/14 l? bi?n th? tr?ng th?i. Ph?n lo?i AOE c?n ??c th?m script, kh?ng suy ch? t? style.
T?M T?T 4: [NGU?N] ReqLevel, EqtLimit, HorseLimit, TargetEnemy/Ally/Self, CostValue v? AttackRadius ???c n?p t? Skills.txt t?i KSkills.cpp:2981?3047; KSkillList::SetNpcSkill n?p skill NPC v? cast b? ??ng t?i KSkillList.cpp:64?107.
T?M T?T 5: [NGU?N]/[CH?A KI?M] V?ng cast NPC ch?y CanCastByIndex ? KSkill::CanCastSkill ? Cost t?i KNpc.cpp:3640?3675; CanCastSkill ch? ?p gi?i h?n trang b? trong nh?nh IsPlayer (KSkills.cpp:267?360), n?n partner kh?ng b? ch?n b?i EqtLimit ? nh?nh n?y; `Cost` c?ng tr? TRUE ngay cho NPC kh?ng ph?i player (KNpc.cpp:7002?7005). Ch?a ch?ng minh m?i skill ?? ???c g?n cho partner.

# A-15c ? K? n?ng ph?i (9?cu?i) d?ng ???c cho NPC h?o h?u

Ng?y kh?o s?t: 17/11/2026. Kh?o s?t t?nh, kh?ng s?a m?, kh?ng ch?y exe/build/runtime.

## Ph?m vi v? ngu?n

- Ngu?n ph?i: `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/Settings/faction/faction.ini` (??c CP936; s? d?ng v?t l? n?u d??i ??y).
- Ngu?n skill: `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/Settings/Skills.txt` (tab; record c? `SkillId`, `SkillStyle`, `ReqLevel`, `EqtLimit`, `HorseLimit`, target flags, `LvlSetScript`, `SkillDesc`).
- Ngu?n cast: `D:/JX-source/server/jxOnline/gameserver/Sources/Core/Src/KSkills.cpp`, `KNpc.cpp`, `KSkillList.cpp`. B?n `KSkills.cpp` canonical v? D:-source tr?ng SHA-256; `KNpc.cpp` kh?c SHA n?n ch? d?ng ???ng D:-source ???c giao ?? ki?m tra lu?ng, kh?ng kh?ng ??nh binary.
- Kh?ng th?y t?p `FactionSkill*` trong Settings; `KFaction.cpp` c? ph?n ??c skill/ph?i b? comment (d?ng 35?110), `KPlayerFaction::OpenCurSkillLevel` c?ng return TRUE v? ph?n th?m skill b? comment (KPlayerFaction.cpp:103?138). V? v?y b?ng d??i l? danh m?c record theo script ph?i, kh?ng ph?i b?ng ch?ng roster h?o h?u ?? h?c skill.

## Danh s?ch ph?i theo th? t?

| S? | Name trong faction.ini | Series/Camp | K? n?ng record x?c ??nh |
|---:|---|---|---|
| 9 | `kunlun` ? C?n L?n ph?i (d?ng 68?73) | Th? / trung l?p | `kunlun.lua`: 52 record, xem b?ng ID b?n d??i |
| 10 | `huashan` ? Hoa S?n ph?i (d?ng 75?80) | Th?y / trung l?p | `huashan.lua`: 47 record, xem b?ng ID b?n d??i |
| 11 | L? T?m Hoan (d?ng 83?86) | M?c / trung l?p | [CH?A KI?M] Kh?ng c? script ph?i t??ng ?ng trong Skills.txt |
| 12 | ??o Hoa ??o (d?ng 88?91) | Th?y / trung l?p | [CH?A KI?M] Kh?ng c? script ph?i t??ng ?ng trong Skills.txt |
| 13 | Minh Gi?o (d?ng 93?96) | H?a / trung l?p | [CH?A KI?M] Kh?ng c? script ph?i t??ng ?ng trong Skills.txt |
| 14 | ?o?n Th? (d?ng 98?101) | Th? / trung l?p | [CH?A KI?M] Kh?ng c? script ph?i t??ng ?ng trong Skills.txt |
| 15 | T? t?o m?n ph?i (d?ng 103?106) | Kim / trung l?p | [CH?A KI?M] Kh?ng c? script ph?i t??ng ?ng trong Skills.txt |

### C?n L?n ? record v? ph?n lo?i thi?t k?

`kunlun.lua` c? 52 ID: `90, 167?184, 275?276, 372?376, 386?387, 392?394, 399?400, 630, 656, 704, 717, 721?722, 1080?1081, 1108?1109, 1134, 1137?1138, 1143?1144, 1167?1168, 1796, 1799`.

| Nh?m theo `SkillStyle` | ID | Lo?i thi?t k? s? b? |
|---|---|---|
| 0 (36 record) | 90, 169, 171?176, 178?179, 181?183, 372?375, 386?387, 392?394, 399, 1080?1081, 1108?1109, 1134, 1137?1138, 1143?1144, 1167?1168, 1796, 1799 | ??nh ??n/AOE t?y `Target*`, `MisslesForm`, `AttackRadius`; [CH?A KI?M] ch?a ??c h?t script ?? t?ch ??n/AOE |
| 2 (7 record) | 170, 177, 180, 184, 276, 376, 656 | H? tr? ch? ??ng/tr?ng th?i; m?t s? target ally/self, c? th? AOE |
| 3 (6 record) | 167, 168, 275, 630, 704, 717 | H? tr?/b? ??ng |
| 13/14 | 400; 721?722 | Bi?n th? tr?ng th?i/h? tr?; [CH?A KI?M] script ??ch |

Do Skills.txt c? record tr?ng t?n/ID m? r?ng v? d?ng d? li?u b? legacy encoding, b?ng ID l? kh?a ch?nh ??ng tin h?n t?n hi?n th?. ?i?u ki?n d?ng l?y tr?c ti?p t?ng record: `ReqLevel` (m?c 0?150 t?y ID), `EqtLimit` (-2=kh?ng gi?i h?n trang b?; 0/1 l? gi?i h?n lo?i v? kh?), `HorseLimit` (0/1/2), target flags v? `CostValue`; ch?a ch?p to?n b? 52 d?ng v?o b?o c?o ?? tr?nh di?n gi?i sai c?t khi legacy record c? tr??ng r?ng.

### Hoa S?n ? record v? ph?n lo?i thi?t k?

`huashan.lua` c? 47 ID: `1347?1385, 1410?1414, 1419?1421`.

| Nh?m theo `SkillStyle` | S? record | ID ti?u bi?u | Lo?i thi?t k? s? b? |
|---|---:|---|---|
| 0 | 32 | 1347?1348, 1351?1353, 1355?1357, 1360?1363, 1366, 1368, 1372?1373, 1376?1377, 1380?1385, 1410?1414, 1419?1421 | ??nh ??n/AOE ho?c tr?ng th?i theo `Target*`/`AttackRadius`; [CH?A KI?M] c?n ??c script ?? ch?t |
| 2 | 5 | 1358, 1364, 1367, 1369, 1371 | H? tr? ch? ??ng/tr?ng th?i, c? th? AOE |
| 3 | 10 | 1349?1350, 1354, 1359, 1365, 1370, 1374?1375, 1378?1379 | H? tr?/b? ??ng |

?i?u ki?n h?c/d?ng c?a Hoa S?n c?ng l?y t? c?c c?t `ReqLevel`, `EqtLimit`, `HorseLimit`, target flags v? cost c?a t?ng record; `EqtLimit` th??ng 0 ho?c -2. [CH?A KI?M] Ch?a c? b?ng ?nh x? t?ng ID??i?u ki?n ??y ?? do Skills.txt ch?a record n?i b? (`abc328`?`abc368`) v? t?n legacy b? l?i m? h?a.

## Ki?m cast cho NPC `kind_partner`

[NGU?N] `KNpc::ProcessCommand`/???ng th?c thi skill l?y skill ?ang active r?i ki?m cooldown (`KNpc.cpp:3640?3660`), `KSkillList::CanCastByIndex` (`KSkillList.cpp:879?887`), `KSkill::CanCastSkill` v? `Cost` (`KNpc.cpp:3673?3675`). `KSkill::CanCastSkill` tr??c h?t ki?m quan h? m?c ti?u; sau ?? to?n b? ki?m `EqtLimit` v? v? kh? n?m trong `if (Npc[nLauncher].IsPlayer())` (`KSkills.cpp:267?360`). V?i `kind_partner`, `IsPlayer()` false, n?n nh?nh gi?i h?n trang b?/ng?a trong CanCastSkill kh?ng ch?y. Partner v?n ph?i qua cooldown, quan h? m?c ti?u v? target flags. `Cost` kh?ng ch?n/kh?ng tr? mana-life-stamina cho NPC kh?ng ph?i player v? c? guard ??u h?m (`KNpc.cpp:7002?7005`); ph?n tr? t?i nguy?n ch? thu?c nh?nh player (`KNpc.cpp:7014?7067`).

[NGU?N] `KSkillList::SetNpcSkill` ki?m ID/count, n?p delay/horse delay/style/equipment limit v? n?u skill b? ??ng th? g?i `Cast` ngay (`KSkillList.cpp:64?107`). ?i?u n?y cho ph?p thi?t k? g?n skill ph?i cho NPC, nh?ng [CH?A KI?M] ch?a t?m th?y n?i g?n to?n b? c?c ID 9?15 v?o t?ng h?o h?u; c?ng ch?a x?c minh script `kunlun.lua`/`huashan.lua` c? guard `kind_partner` ri?ng.

[CH?A KI?M] `KSkill::Cast` c? l?i g?i ki?m ??u v?o b? comment (`KSkills.cpp:456?460`), n?n kh?ng d?ng ?? l?m b?ng ch?ng b? qua m?i ki?m. AOE/??nh ??n ph?i ph?n lo?i theo `TargetEnemy/TargetAlly/TargetSelf`, `MisslesForm`, `AttackRadius` v? script th?c thi; kh?ng suy t? t?n skill ho?c `SkillStyle` m?t m?nh.

## B?ng cho thi?t k? h?o h?u

| H?ng m?c | K?t lu?n t?nh | Quy?t ??nh thi?t k? ?? ngh? |
|---|---|---|
| Danh m?c | Ch? C?n L?n/Hoa S?n c? nh?m script r?; ph?i 11?15 [CH?A KI?M] | Kh?ng t? g?n skill 11?15 cho ??n khi c? data/registry |
| Skill ch? ??ng | C? th? ch?y qua c?ng lu?ng NPC n?u ???c `SetNpcSkill` | M?i partner gi? danh s?ch skill ri?ng, ID server ki?m tra |
| EqtLimit | B? b? qua trong `CanCastSkill` cho partner | N?u c?n gi?i h?n v? kh?, th?m rule partner ri?ng ? task tri?n khai; kh?ng s?a trong task n?y |
| ReqLevel/cost/cooldown | ReqLevel n?p v?o KSkill; lu?ng NPC th?y cooldown, c?n `Cost` bypass cho non-player | Ch?t ri?ng policy level/cost cho partner; kh?ng suy theo player |
| Passive/aura | SetNpcSkill g?i cast ngay v?i `SKILL_SS_PassivityNpcState`; IsAura ???c gi? | T?ch passive/aura kh?i chi?u ??nh khi thi?t k? roster |
| Ngo?i l? script/target | [CH?A KI?M] | T? ch?i m?c ??nh n?u target/series/script ch?a ???c x?c minh |

## Ki?m ch?ng v? b?n giao

- ?? ??c ??ng task, hai b?o c?o n?n A-12/A-14 v? c?c file ngu?n n?u trong ph?m vi; kh?ng qu?t r?ng ngo?i t?n file/th? m?c c?n thi?t.
- ?? ki?m tra Git m?t l?n tr??c khi ghi: branch `task/A-15c`; task `JX1_OPS/TASKS/A-15c.md` ?ang untracked c? s?n.
- Kh?ng s?a source, Settings hay m?; kh?ng ch?y exe/game/server/VM/network/build/test.
- [CH?A KI?M] Ch?a ki?m tra data/skill registry cho ph?i 11?15, to?n b? Lua script, binary/PAK, runtime cast v? t?ng template partner.
- Tr?ng th?i cu?i: **DONE** cho kh?o s?t t?nh trong ph?m vi ngu?n hi?n c?; ph?n thi?u d? li?u gi? [CH?A KI?M].
- Commit SHA/link: **kh?ng c?**; ch?a stage/commit/push theo r?o ch?n task.


## Ph? l?c record theo t?ng ID (Skills.txt)

| Ph?i/script | ID | T?n record | Lo?i theo SkillStyle | ?i?u ki?n h?c/d?ng ?? ??c |
|---|---:|---|---|---|
| C?n L?n | 90 | Mª Tung ¶o ¶nh | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=50; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 167 | C«n L«n §ao ph¸p | h? tr? b? ??ng | `ReqLevel=10; EqtLimit=1; HorseLimit=0; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 168 | C«n L«n KiÕm ph¸p | h? tr? b? ??ng | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 169 | H« Phong Ph¸p | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=1; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=300` |
| C?n L?n | 170 | §¹i L·ng Thùc Kh«ng | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 171 | Thanh Phong phï | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 172 | Thiªn TÕ TÊn L«i | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=360` |
| C?n L?n | 173 | Thiªn Thanh §Þa Träc | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=-2; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 174 | Ki B¸n phï | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=20; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 175 | Khi Hµn Ng¹o TuyÕt | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=40; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 176 | Cuång Phong SËu §iÖn | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=50; EqtLimit=1; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=180` |
| C?n L?n | 177 | B¸ch Xuyªn N¹p H¶i | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=30; EqtLimit=-2; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 178 | NhÊt KhÝ Tam Thanh | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=1; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 179 | Cuång L«i ChÊn §Þa | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 180 | §éc Tª TÞ Tµ | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=40; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 181 | KhÝ T©m phï | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=40; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 182 | Ngò L«i Ch¸nh Ph¸p | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 183 | TuÕ NguyÖt V« T×nh phï | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=50; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=180` |
| C?n L?n | 184 | Kim ThiÒn Tho¸t X¸c | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=50; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 275 | S­¬ng Ng¹o C«n L«n | h? tr? b? ??ng | `ReqLevel=60; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 276 | TuÕ NguyÖt V« T×nh | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=20; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| C?n L?n | 372 | Ng¹o TuyÕt Tiªu Phong | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=1; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 373 | KhiÕu Phong Tam Liªn KÝch | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 374 | Vô Táa C«n L«n | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 375 | L«i ®éng Cöu Thiªn | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 376 | Tóy Tiªn T¸ Cèt 99 | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=80; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 386 | Ngù Phong thuËt | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=300` |
| C?n L?n | 387 | B×nh §Þa H¸m L«i | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 392 | Thóc Ph­îc Chó | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 393 | B¾c Minh §¸o H¶i | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 394 | Tóy Tiªn T¸ Cèt | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 399 | Thiªn TÕ TÊn L«i (¶nh ®éng) | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=360` |
| C?n L?n | 400 | KiÕp Phó TÕ BÇn | tr?ng th?i ??c bi?t | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=360` |
| C?n L?n | 630 | HuyÒn Thiªn V« Cùc | h? tr? b? ??ng | `ReqLevel=60; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 656 | Gi¶m tèc ®o¹t cê (Tèng Kim) | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=20; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=440` |
| C?n L?n | 704 | Th«ng minh lanh lîi | h? tr? b? ??ng | `ReqLevel=1; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 717 | L­ìng Nghi Ch©n KhÝ | h? tr? b? ??ng | `ReqLevel=120; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 721 | L­ìng Nghi Ch©n KhÝ_Ma Ph¸p §én | tr?ng th?i ??c bi?t | `ReqLevel=120; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 722 | L­ìng Nghi Ch©n KhÝ_Gia Tèc | tr?ng th?i ??c bi?t | `ReqLevel=120; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 1080 | Cöu Thiªn C­¬ng Phong | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=1; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 1081 | Thiªn L«i ChÊn Nh¹c | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 1108 | Phong Minh Ngäc To¸i | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 1109 | L«i §éng Cµn Kh«n | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| C?n L?n | 1134 | abc239 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=0; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=800` |
| C?n L?n | 1137 | abc242 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=100` |
| C?n L?n | 1138 | abc243 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=100` |
| C?n L?n | 1143 | abc248 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=0; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 1144 | abc249 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=360` |
| C?n L?n | 1167 | ncp22 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| C?n L?n | 1168 | ncp23 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=80; EqtLimit=-2; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=470` |
| Hoa S?n | 1347 | B¹ch Hång Qu¸n NhËt | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| Hoa S?n | 1348 | V©n Ch­ng Hµ óy | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=0; HorseLimit=1; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=400` |
| Hoa S?n | 1349 | KiÕm T«ng Tæng QuyÕt | h? tr? b? ??ng | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1350 | D­ìng Ng« KiÕm Ph¸p | h? tr? b? ??ng | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1351 | Kim Nh¹n Hoµnh Kh«ng | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1352 | H÷u Phông Lai Nghi | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1353 | abc328 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1354 | Hi Di KiÕm Ph¸p | h? tr? b? ??ng | `ReqLevel=40; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1355 | Thiªn Th©n §¶o HuyÒn | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=50; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=360` |
| Hoa S?n | 1356 | abc329 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=50; EqtLimit=0; HorseLimit=1; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1357 | Cao S¬n L­u Thñy | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=50; EqtLimit=0; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1358 | HuyÔn Nh·n V©n Yªn | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=60; EqtLimit=0; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1359 | abc330 | h? tr? b? ??ng | `ReqLevel=10; EqtLimit=0; HorseLimit=0; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1360 | Th­¬ng Tïng Nghªnh Kh¸ch | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1361 | abc330 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1362 | abc331 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1363 | Th¸i Nh¹c Tam Thanh Phong | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=90; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1364 | §o¹t MÖnh Liªn Hoµn Tam Tiªn KiÕm | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=90; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1365 | Tö Hµ KiÕm KhÝ | h? tr? b? ??ng | `ReqLevel=120; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1366 | L¹c Nh¹n Kinh Hång | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=0; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1367 | abc332 | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=0; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1368 | §éc C« Cöu KiÕm | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1369 | Cöu kiÕm hîp nhÊt | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=150; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1370 | H¹o Nhiªn Chi KhÝ | h? tr? b? ??ng | `ReqLevel=0; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1371 | abc333 | h? tr? ch? ??ng/tr?ng th?i | `ReqLevel=0; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1372 | Thanh V©n Tèng S¶ng | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=400` |
| Hoa S?n | 1373 | Kü n¨ng v« hiÖu Thanh Phong ChiÕm VÞ | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=0; HorseLimit=1; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1374 | Long NhiÔu Th©n | h? tr? b? ??ng | `ReqLevel=10; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1375 | H¶i N¹p B¸ch Xuyªn | h? tr? b? ??ng | `ReqLevel=20; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1376 | Long HuyÒn KiÕm KhÝ | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=360` |
| Hoa S?n | 1377 | Long HuyÒn KiÕm KhÝ 2 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=0; HorseLimit=1; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1378 | KhÝ ChÊn S¬n Hµ | h? tr? b? ??ng | `ReqLevel=40; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1379 | KhÝ Qu¸n Tr­êng Hång | h? tr? b? ??ng | `ReqLevel=50; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1380 | Ma V©n KiÕm KhÝ | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=360` |
| Hoa S?n | 1381 | KiÕm KhÝ V« CÊp | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=0; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=360` |
| Hoa S?n | 1382 | Ph¸ch Th¹ch Ph¸ Ngäc | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=90; EqtLimit=0; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=380` |
| Hoa S?n | 1383 | abc334 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=90; EqtLimit=0; HorseLimit=0; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=220` |
| Hoa S?n | 1384 | ThÇn Quang Toµn NhiÔu | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=0; HorseLimit=1; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=600` |
| Hoa S?n | 1385 | abc335 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=0; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=360` |
| Hoa S?n | 1410 | abc359 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1411 | abc360 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1412 | abc361 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1413 | abc362 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=10; EqtLimit=-2; HorseLimit=1; target E/A/S=1/0/0; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1414 | abc363 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=60; EqtLimit=-2; HorseLimit=0; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1419 | abc368 | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=-2; HorseLimit=1; target E/A/S=0/0/1; CostType=0, CostValue=0; AttackRadius=0` |
| Hoa S?n | 1420 | KiÕm Ph¸p - Th¸i Nh¹c Tam Thanh Phong | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=90; EqtLimit=0; HorseLimit=1; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| Hoa S?n | 1421 | KiÕm ph¸p - §éc C« Cöu KiÕm | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=150; EqtLimit=0; HorseLimit=1; target E/A/S=0/0/0; CostType=0, CostValue=0; AttackRadius=480` |
| C?n L?n | 1796 | Thanh Long XuÊt ThÕ | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=-2; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=0` |
| C?n L?n | 1799 | Kim Long XuÊt ThÕ | ??nh/chi?u ch? ??ng (??n ho?c AOE ? c?n target/script) | `ReqLevel=30; EqtLimit=-2; HorseLimit=0; target E/A/S=0/1/1; CostType=0, CostValue=0; AttackRadius=0` |
