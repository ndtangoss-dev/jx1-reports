# 52 - U003 G0 bo sung: package.ini, quai, Loi Dong (projectile/no/cooldown), che khuat

Chi doc. Khong tao project Unity/APK, khong cai thu vien; khong sua PAK/source/server/DB/VM; khong dung hay restart Goddess/EXE. Ghi chu: bao cao nay BO SUNG bao cao 50-51, khong ghi de du lieu goc. Workspace: `D:\JX1_U003_work` (`out_*.txt`, `tools\`).

TOM TAT:
1. package.ini that: moi APK test cua du an (fix33..p47, tick) deu dong goi `package.ini` = ban A (`Resources/package.ini`, md5 4f70894f...). Ban B (`data/data/package.ini`) khong nam trong APK nao. => Ban A gan nhu chac chan; chua doc file tren dien thoai.
2. Loi Dong Cuu Thien (375): da XAC NHAN chuoi projectile that: skill 375 la BaseSkill nen `ChildSkillId=181` la MISSLE id 181 "Loi Dong Cuu Thien" (spr bay `\spr\skill\kl\雷动九天.spr`, no `Bz_dian3_爆炸.spr`); va cham -> skill 387 -> missle 193 (spr `\spr\skill\tm\雷击术.spr`). Hai spr deu ton tai trong skills.pak. Sua nhan dinh bao cao 51 (khong con "chua tim thay projectile").
3. Cooldown: du lieu skill 375 khong co cooldown rieng (`TimePerCast=0`); khoang cach cast = animation/CastSpeed va `GetDelayPerCast`. UI cooldown tren nut skill chua tim thay (ProgressTimer o KgameWorldVN la chi bao pin).
4. Che khuat: cay doi tuong sap xep bang cay "Ipot" (Branch=doan thang/diem cua noi dung built-in, Leaf=doi tuong dong); chi la mo ta tu header, chua doc KIpoTree.cpp.
5. Quai: bang so sanh ani001 / enemy003 o muc 3; chua chon.

Can toi quyet dinh: co (muc 6)

## Quy uoc: [XN]=xac nhan (co bang chung ma/du lieu), [TN]=ket qua thu nghiem (tu script/tinh toan), [GT]=gia thuyet

## 1. package.ini thuc su duoc client dung
- [XN] `KUpdateLayer.cpp:831` mo `data/package.ini`; `KUpdateLayer.cpp:217,629` `copyData("package.ini")` chep file tu assets APK ra thu muc ghi moi lan khoi dong.
- [XN] md5 `assets/package.ini` trong 7 APK trong `data_cdn\apk` (fix33, fix34, fix35, fix36, p46, p47, tick) = `4f70894f5c10283a60f74bf8ed4f1bb6` = `Resources/package.ini` = ban A (script_skill, update10, update_music, updata07...). Bang chung: `out_apk_package_ini.txt`.
- [XN] `data/data/package.ini` (ban B, md5 24b3a5da...) khong co trong APK nao; `jxmobile.apk` goc 2023 co ban thu ba (md5 50a03aed..., bat dau volam00, volam01, updata07).
- [XN] Nhat ky CDN (`out/cdn-8080.log`) chi co 1 dong, khong chua yeu cau package.ini -> khong dung lam bang chung.
- [GT] Dien thoai chay ban A neu cai tu cac APK tren; chua kiem tra file trong bo nho dien thoai (khong doc duoc tu may nay) va chua thay mo ta ghi de package.ini tu CDN.
- Hau qua [TN] (A): Skills.txt/Missles/NpcS/mapList/*Res.txt = ban `script_skill.pak`; kind file/sort table/part tables = `updata02`/`slistcl` nhu bang `pak_winner.tsv`. Skill 375 AttackRadius = 470.

## 2. Loi Dong Cuu Thien (SkillId 375): projectile, vung no, cooldown
### 2.1 Xac nhan
- [XN] `KSkills.cpp:1625` `m_eMisslesForm` la enum hinh dang (SkillDef.h:117-127: Wall, Line, Spread, Circle, Random, Zone, AtTarget=6, AtFirer). Skill 375/181/387 co MisslesForm=6 = AtTarget (khong phai id Missles).
- [XN] Voi `BaseSkill=1`, `CreateMissle(nLauncher, m_nChildSkillId, ...)` (`KSkills.cpp:1775, 1929`) dung `ChildSkillId` lam MISSLE id. Skill 375: BaseSkill=1, ChildSkillId=181, ChildSkillNum=4, MslsGenerate=3, MslsGenerateData=5, WaitTime=2 (do tre sinh dan: `KSkills.cpp:3090-3120`).
- [XN] Missles.txt id 181 "Loi Dong Cuu Thien": MoveKind=0, CollidRange=2, IsRangeDmg=0, DmgInterval=10, LifeTime=12, ColVanish=1, AnimFile2=`\spr\skill\kl\雷动九天.spr` (6 khung), AnimFile4=`\spr\skill\昆仑\Bz_dian3_爆炸.spr` (8 khung), mau 255,255,239, LightRadius 90.
- [XN] Cham (CollideEvent=1, CollidSkillId=387; server `kunlun.lua:207-210` skill_collideevent[3]={387}): skill 387 BaseSkill=1? -> ChildSkillId=193 => Missles id 193 "Binh Dia Ham Loi": AnimFile2=`\spr\skill\tm\雷击术.spr` (27 khung), AnimFile4 = Bz_dian3, IsRangeDmg=1, DmgRange=2, DmgInterval=4, LifeTime=12.
- [XN] Asset ton tai trong PAK (tool giai nen doc-only): icon `\spr\Ui\skill\雷动九天.spr` (spr.pak, 36x36, 1 khung); cast `\spr\skill\昆仑\kl_16_魔法施放.spr` (skills.pak, 260x260, 10 khung, interval header 50); projectile 181 (skills.pak, 98752 B, 400x400, 6 khung, interval 50); explosion Bz_dian3 (53335 B, 320x320, 8 khung, interval 40); projectile 193 (skills.pak, 423336 B, 400x400, 27 khung, interval 50); am thanh `\sound\skill\五雷正法m.wav`/`f.wav` (sound.pak va ban old). So khung khop voi AnimFileInfo trong Missles (6/8/27) => header SPR doc dung. Bang chung: `out_spr_heads.txt`.
- [XN] Server `kunlun.lua` (chi doc) `leidong_jiutian` (dong 199-239): lightingdamage_v cap 1/15/20 = 80/260/470; seriesdamage_p; stun_p; skill_collideevent[3]=387; skill_showevent={0..4}; skill_cost_v 40/60/95. KHONG co tick 500 ms; sat thuong goc la tung vien dan (4 vien, DmgInterval/LifeTime theo tick game) va ky nang va cham 387.
### 2.2 Cooldown
- [XN] `Skills.txt` 375: `TimePerCast=0`, `TimePerCastOnHorse=0` -> khong co khoang cooldown rieng trong du lieu. Khoang gian cast: `KNpc.cpp:2260` dat `NextCastTime = now + pSkill->GetDelayPerCast()`; client auto dung `GetDelayPerCast` (`KgameWorld.cpp:5559, 12962`). Toc do cast con theo CastSpeed va CharAnimId=11.
- [XN] UI cooldown tren nut skill: chua tim thay trong mã client da doc (ProgressTimer o `KgameWorldVN.cpp:1008-1034` la chi bao pin, khong phai cooldown).
### 2.3 Khong tim thay
- Chua tim thay so tick mien phi "500 ms" hay "20 sat thuong/tick" trong du lieu goc: do la thiet ke U003. Cac sprite Con Lon khac (KL_04, kl_05) KHONG con la ung vien cua 375: chi la hieu ung ky nang khac (Missles 17, 18).
- [GT] Vung no AOE: DmgRange/CollidRange=2 (don vi o); ban kinh nguoi choi AttackRadius=470 (don vi pixel/khoang cach logic chua xac nhan).

## 3. So sanh quai mau (chua chon; de ChatGPT/nguoi dung duyet)
(Nguon: NpcS.txt ban script_skill, 普通npc资源信息, header SPR; `out_monster_compare.txt`.)
| Tieu chi | ani001 (dong vat) | enemy003 (nguoi) |
|---|---|---|
| Hang NpcS dung | 2 hang, ca 2 Kind=0 (quai) | 14 hang (5 Kind=3 doi thoai/NPC, 9 Kind=0) |
| Duong dan sprite | `\spr\npcres\animal\ani001\` | `\spr\npcres\enemy\enemy003\` |
| Sprite co du | st, pst, wlk, bat, die, at (6) | st, pst, wlk, bat, die, at (6) |
| Kich thuoc khung | 320x320, 8 huong | 320x320, 8 huong |
| Khung/huong | st 12, wlk 15, bat 8, die 10, at 12 | st 6, wlk 14, bat 7, die 13, at 14 |
| Interval (header) | st 116, wlk 84, bat 75, die 100, at 80 | st 200, wlk 85, bat 128, die 80, at 100 |
| Dung luong 6 spr | ~1895 KB | ~1188 KB |
| AttackSpeed (NpcS, Kind0) | 18 (2/2) | 12 (5), 18 (3), 15 (1) |
| WalkSpeed | 6-7 | 6 (6), 12 (2), 10 (1) |
| ReviveFrame | 810 | 0/1/270/810/1080 (khong dong nhat) |
| Tinh nhat quan cho prototype | cao (1 loai, it bien the) | thap hon (nhieu bien the, co boss/NPC doi thoai) |
| Rui ro | Dung luong lon; thieu thong tin map xuat hien | It dong nhat; co the lan voi NPC |
- [XN] interval trong bang thong tin == header SPR (kiem tra ca 2 quai). [GT] don vi interval la mili giay (cast 10 khung x 50 = 0.5 s hop ly) - chua xac nhan.
- [XN] Toc do danh goc: chi co chi so `AttackSpeed` (khong don vi ro) + cong thuc client `KNpc.cpp:2381` (khung tong = m_AttackFrame * a/(b+bonus)); `m_AttackFrame` tu dau chua truy duoc => TOC DO DANH CHUA XAC DINH; U003 phai ghi ro la gia tri cau hinh cua U003 neu dung.
- Nhan dinh [GT] de xuat: ani001 (dong nhat, Kind=0 ca 2 hang, du 5 hanh dong). Chua chon.

## 4. Co che che khuat trong map (KIpotLeaf/KIpotBranch/KIpoTree)
- [XN] `KIpotBranch.h`: "doi tuong cay" gom nhanh (Branch) la doan thang (2 diem) hoac diem gan voi mot doi tuong built-in (sap xep theo day/duong/diem); la (Leaf) la doi tuong dong luc chay (rto: nhan vat, quai...). Ham `PaintObjectLayer`, `AddBuildinObjLine/Point` cho 2 kieu sap xep da neu o SceneDataDef (Tree/Line/Point/Above).
- [GT] Nhan vat duoc xep truoc/sau cay theo vi tri doi voi doan day hoac diem cua vat the (trai/phai nhanh). Chua doc `KIpoTree.cpp` (1701 dong) de xac nhan thuat toan -> chua dung lam co so cai dat. Phuong an Unity: dung cung dinh nghia (Tree/Line/Point/Above) va so sanh y theo day.
- [XN] Du lieu tho: `KBuildinObj` co 4 diem anh (ImgPos1-4), Props; tren vung mau co 8-24 vat the, 0-1 tree, 8-12 line, 8-11 point.

## 5. Con lai chua xac minh
- Thu tu Dir 1..16 <-> huong game; `UnitNum=14`, `DirNum=18` o [DEFAULT].
- Map 45: file vung day du va so cay/vat can.
- Mat bang hieu ung 'ShowEvent=4' (`KSkills.cpp:2916`: "co hien su kien dan"): client dung de bat hieu ung nao chua doc.
- UI nut skill/auto/cooldown: chua tim.
- Thu tu nap PAK tren dien thoai (khong the doc tu may nay).

## 6. Can quyet dinh de duyet kien truc
1. Chap nhan ban A (package.ini trong APK) lam co so; cho phep ghi chu "chua kiem tra tren may that".
2. Hieu ung Loi Dong cho U003: dung chuoi goc (cast kl_16 -> missle 181 x4 -> no Bz_dian3; va cham -> missle 193) nhung tick 500 ms / 20 sat thuong la thiet ke U003, khong phai goc: dong y?
3. Chon quai (de xuat ani001, can duyet).
4. Cho phep doc tiep KIpoTree.cpp (che khuat) va tim UI nut skill/auto/cooldown (chi doc).
