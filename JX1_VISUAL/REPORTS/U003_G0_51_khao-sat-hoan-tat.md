# 51 - JX1 Unity U003 Idle Combat World: bao cao G0 (khao sat chi doc) - hoan tat

TOM TAT:
1. Hoan tat 6 muc khao sat chi doc; khong tao project Unity, khong build APK, khong cai thu vien; khong dong PAK/source goc; VM va Goddess giu nguyen (khong restart/dung EXE).
2. SUA BAO CAO 50: ban sort-table client THUC SU dung la ban trong `updata02.pak` (khong phai `setting-new.pak`, PAK nay khong nam trong danh sach nap). Ban nay: 44 section, 148 Dir + 301 Line, 12 slot (khong co canh/slot 20), DEFAULT co 16 Dir. JSON da dung va doi chieu 495/495 dong khop.
3. Thu tu nap PAK: client nap theo thu tu trong `package.ini`, PAK dau tien co id la thang. Co 2 ban package.ini trong may (Resources vs data/data) cho ket qua khac nhau o 5 file (Skills/mapList/item*Res...); cac file MainMan/npc/map thi giong nhau. Can chot ban nao la ban chay that.
4. Map: .wor chi la file ini nho; dia hinh nam trong `Region_C.dat` theo luoi vung 512x1024 px; 960/993 map co .wor trong map.pak; ung vien nho: map 45 (14x10 vung, ngoai troi).
5. Quai mau: ani001 va enemy003 co du 6 spr (dung/di/danh/bi danh/chet); toc do danh co trong NpcS.txt (AttackSpeed) nhung DON VI chua xac dinh. Loi Dong Cuu Thien: icon, spr thi trien, am thanh da xac nhan; spr projectile/no chua xac dinh.

Can toi quyet dinh: co (xem muc 8)

Workspace: `D:\JX1_U003_work` (extract, json, tools, out_*.txt). Moi thu doc-only; nguon: `C:\Jx1CocoV3\data_cdn\data\*.pak` va ma nguon client.

## 1. Bang thu tu ve MainMan -> JSON (xong)
- File: `D:\JX1_U003_work\json\sort_table_MainMan.json` (+ `sort_table_verify.txt`). Nguon: `男主角贴图顺序表.txt`, ban updata02 (xem muc 2), GBK.
- Bao toan: action, key_frame (Dir) / frame (Line), thu tu slot goc + ten bo phan, so dong goc (line_no), chuoi raw.
- Doi chieu: tap hop 495 dong noi dung (bo trong/comment) trong TXT == 495 dong dung lai tu JSON (so khop tap hop); 0 dong khong phan tich duoc; 449 muc deu co 12 phan tu; slot xuat hien {0,1,4,5,6,7,8,9,12,13,14,16}, khong co slot la.
- Slot: 0 head, 1 hair, 4 shoulder, 5 body, 6 left_hand, 7 right_hand, 8 left_weapon, 9 right_weapon, 12/13/14 horse front/mid/rear, 16 cape, (20 wing: KHONG co trong ban nay => canh khong duoc ve theo bang nay). Suy ra tu MAX_BODY_PART=6 x SECT=4 va tap slot khop (KNpcResNode.h:23-24; 部件列表.txt).
- [DEFAULT]: UnitNum=14, DirNum=18, Dir1..Dir16 (key -1). 43 action con lai: ghi de Dir (theo huong) va Line (khoa dau = so khung). Ngu nghia chon dong: KNpcResNode.cpp:1390 GetSort; ap dung: KNpcRes.cpp:422, 665-679.
- Chua kiem tra: anh xa huong game (64/32 huong?) -> chi so Dir 1..16; Unit/DirNum dung de lam gi. Can doc them truoc G2.
- Luu y: file nguoi dung neu `.ini` (1007 byte, chi o setting-new.pak) khong duoc client nap.

## 2. Co che nap PAK (bang chung ma nguon)
- `KUpdateLayer.cpp:831` -> `g_pcPakList.Open("data/package.ini")`; `KPakList.cpp:171-200` doc khoa "0","1",... theo thu tu va mo tung PAK; `KPakList.cpp:66-77` pFindElemFileA: duyet tu dau, PAK dau tien chua id la thang (khong merge, khong uu tien kich thuoc/ngay).
- Id = hash ten (GBK, chu thuong) - da dung trong tool.
- Hai danh sach: A = `Resources/package.ini` (script_skill, update10, update_music, updata07...), B = `data/data/package.ini` (volam00, volam01, updata07...). `copyData("package.ini")` (KUpdateLayer.cpp:217,629) copy file ban kem APK ra thu muc ghi; ban B co ve la ban thu nghiem. CHUA xac nhan duoc duong dan thuc te (writable/package.ini vs writable/data/package.ini) -> can quyet dinh dung A hay doc ban tren may that.
- Bang ket qua: `D:\JX1_U003_work\pak_winner.tsv` (41 muc): updata02 thang cho kind file, sort table, part tables; Skills.txt/Missles/NpcS khac nhau giua A (script_skill) va B (updata02/updata08), cung ban 375 chi khac AttackRadius 470 (A) vs 480 (B). `setting-new.pak` khong nam trong hai danh sach.
- Ngoai le: entry `kl_02_疾电法b.spr` bao loi giai nen UCL (lookbehind overrun) - tool giai nen can kiem tra neu can file nay.

## 3. Map (.wor va vung)
- Duong dan: `\maps\<MapList path>.wor` (KScenePlaceC.cpp:578). 993 map trong MapList, 960 co .wor trong map.pak (`map_wor_scan.tsv`), 33 khong thay.
- .wor la INI nho (~280 byte): [MAIN] rect=x0,y0,x1,y1 (luoi vung), IsInDoor, brightness, color, windspeed, [Weather]. Khong chua dia hinh.
- Du lieu vung: `\maps\<path>\v_<yyy>\<xxx>_Region_C.dat` (KScenePlaceRegionC.cpp:93, SceneDataDef.h:13): bang 6 phan (obstacle, trap, npc, obj, ground, buildin) roi noi dung. Vung 512x1024 px (RWPP_AREGION_*), luoi chan 16x32.
- Da kiem chung tren file that (map 凤翔, 3 vung): obstacle 512 o x 4 byte (gia tri nhu 0,17,20,33,36,49,65,81 => loai o vuong), ground 61-64 nut gach nen (spr + frame, vd `游戏资源\室外地表\中型地表图素\黄土.spr`) + doi tuong tham mat dat (0-86), buildin 18-24 doi tuong (tree/line/point/above), trap, npc. Danh sach vung co that: 1066/1650 o luoi (凤翔).
- Co che che khuat: buildin chia 4 nhom sap xep: Tree, Line (theo day), Point, Above (tren dau) (SceneDataDef.h:127-149 KBuildinObjFileHead); thuat toan sap xep chi tiet (KIpotLeaf) CHUA doc. Co the dung Props/ImgPos 4 diem de dung sorting trong Unity.
- Kha nang Unity: doc duoc cau truc; can doi SPR -> PNG (da co duong U001/U002); khong dung nguyen vung ngay duoc khi chua giai ma KBuildinObj day du va thu tu ve.
- Ung vien map: `out_map_sizes.txt` (481 map co rect). Ngoai troi nho nhat: id 45 `中原北区\天忍教\天忍教室外` 14x10 vung (~7168x10240 px), id 68 青螺岛 17x14, id 56 衡山派 19x17, id 7 秦陵 25x16. Khuyen nghi id 45 hoac cat 1 vung con ra tu map lon. Chua kiem tra co du Region_C.dat, so cay, so vat can map 45.
- Diem spawn 15: khong co san trong du lieu client (Npc_C.dat chi cho NPC cua map); U003 phai tu dat va ghi vao du lieu map.

## 4. Quai mau
- Ung vien da XAC NHAN du 6 sprite trong spr.pak: `ani001` (`\spr\npcres\animal\ani001\ani001_{st,pst,wlk,bat,die,at}.spr`) va `enemy003` (`\spr\npcres\enemy\enemy003\...`, 4+2 file nhu tren). Bang `普通npc资源.txt` (updata02): FightStand/NormalStand = _st; NormalWalk/Run = _wlk; Wound = _bat; Die = _die; Attack1/2/Magic = _at.
- `普通npc资源信息.txt` (khung tong, huong, interval): ani001: Stand 96,8,116; Walk 120,8,84; Wound 64,8,75; Die 80,8,100; Attack 96,8,80 => 12 khung/huong khi danh. enemy003: Stand 48,8,200; Walk 112,8,85; Wound 56,8,128; Die 104,8,80; Attack 112,8,100.
- Toc do danh: `NpcS.txt` co cot AttackSpeed (vd hang dau enemy003 = 18, boss = 12, khac = 15), CastSpeed, WalkSpeed, ReviveFrame (hang dau 1080) nhung DON VI/cong thuc tu cot -> tong khung chua xac dinh (client: KNpc.cpp:2381 `m_AttackFrame * naAttackSpeed/(nbAttackSpeed+m_CurrentAttackSpeed)`; chua truy duoc m_AttackFrame lay tu dau). Don vi `interval` cua animation cung chua xac dinh. => KHONG co gia tri toc do danh nao duoc ghi la du lieu goc cho U003; bao: CHUA XAC DINH.
- Yeu cau thiet ke U003 (HP 100, dame 2, hoi sinh 2 s) la gia tri cua U003, khong phai goc (goc: ReviveFrame, Life/Damage theo cong thuc).
- Chua doc: lay tu 8 huong ra 8 huong game (huong goc 64? hay 8 trong spr) va bang NpcS->NpcResType cho quai cu the trong ban do chon.

## 5. UI goc
- HP quai/nguoi: thanh mau = sprite trong SpriteBatchNode `ui/state/normal.png` (KgameWorld.cpp:655; entry co trong uinew.pak, 2842 byte); ti le = `m_CurrentLife/m_CurrentLifeMax` (KgameWorld.cpp:9321-9323). HP nguoi choi con co cau `\ui\main\life\hongbanqiu_NN.png` (qua cau mau, updata03.pak, co ban `hongbanqiu_01_0.png` 5984 byte).
- So sat thuong: `CCLabelBMFont` voi `fonts/number_16_r.fnt` (do) va `number_16_w.fnt` (trang) - file ton tai ngoai PAK tai `Resources/fonts/` (KgameWorld.cpp:9259). Code chi dat vi tri theo NPC (KgameWorld.cpp:9267-9269); KHONG thay hieu ung bay len 1 s => U003 phai tu lam (giu font goc).
- Joystick: `KHRocker.cpp` dung `yaoganz.png`/`yaoganx.png` (Resources/ui/buttons, co ban ui_vn). Nut ky nang: `KSkillRocker.cpp`; nut Auto, cooldown: chua xac dinh (ung vien: ProgressTimer o `vn/gamescence/KgameWorldVN.cpp:1024`, chua doc). Chua doi chieu texture nut skill (`mainskillmix*.png`).

## 6. Loi Dong Cuu Thien (SkillId 375, dong 376 trong Skills.txt)
DA XAC NHAN:
- Icon: `\spr\Ui\skill\雷动九天.spr` (spr.pak, 2184 byte).
- Spr thi trien (PreCast): `\spr\skill\昆仑\kl_16_魔法施放.spr` (skills.pak, 116645 byte).
- Am thanh thi trien: `\sound\skill\五雷正法m.wav` / `五雷正法f.wav` (sound.pak, ~411/394 KB).
- Du lieu ky nang: MislesForm=6, MslsGenerate=3, MslsGenerateData=5, ChildSkillId=181 x4, CollideEvent=1 -> CollidSkillId=387 (sub-skill co PreCast giong, ChildSkill 193), AttackRadius=470/480, CharAnimId=11, WaitTime=2, ReqLevel=80, script `kunlun.lua` ham `leidong_jiutian` (server). Chuoi: 375 -> 181(x4) -> 22 ; va 375 va cham -> 387 -> 193 -> 83 (chua giai het).
CHUA XAC DINH / CHUA TIM THAY:
- Spr projectile/vung no cua chinh Loi Dong: `MisslesForm=6` KHONG phai id Missles (Missles id 6 = 风云突起, spr Thuy Yen, khong hop). Chua thay missle id gan voi 375/181/387. Ung vien cung nhom Con Lon, DA CO trong skills.pak: `KL_04_狂雷震地.spr` (115 KB), `kl_05_五雷正法.spr` (106 KB), `Bz_dian3_爆炸.spr` (53 KB) - chua duoc xac nhan la cua 375.
- So lieu goc cua tick/sat thuong (script server) - chua doc `kunlun.lua` (server). Gia tri 20/500ms/1s/1s cua thiet ke U003 la thiet ke, khong phai goc.

## 7. Phu thuoc, rui ro (cho G1-G5)
| GD | Noi dung | Phu thuoc | Rui ro |
|---|---|---|---|
| G1 pipeline asset | SPR->PNG + metadata (offset, khung, huong, interval); doc Region_C.dat -> JSON | SPR decoder da co (U001/U002); JSON sort table; du lieu ground/buildin | UCL loi 1 entry; nhieu ban entry (muc 2); dung luong |
| G2 nhan vat | 8 huong, joystick, thu tu ve theo bang (theo khung+huong), thay trang bi | Anh xa huong; bang 部件/trang bi; slot 20 khong ve | Thu tu theo khung gay dat sorting tung khung; thieu part/trang bi |
| G3 map 2.5D | map 45 (hoac cat vung), ground tiles, buildin (tree/line/point/above), obstacle, 15 spawn, quai | Giai ma KBuildinObj + KIpotLeaf; spr tile | Ma tran che khuat phuc tap; map lon -> dung luong |
| G4 chien dau | tu danh, AOE 20 dmg/500 ms, cast 1 s, cd 1 s, so sat thuong bay 1 s, HP bar, debug panel | Missile/effect Loi Dong chua xac dinh; UI nut/cooldown | Hieu ung that chua xac nhan; dung hieu ung tam la bi cam neu chua bao |
| G5 Android | man ngang, APK moi theo phien ban (khong ghi de), Tailscale | Quy tac an toan da duyet | Hieu nang IL2CPP voi so khung lon |

## 8. Quyet dinh kien truc can nguoi dung duyet
1. Chot danh sach PAK chay that (A hay B) hay chap nhan "ban updata02 cho cac file cua MainMan, script_skill/updata02 cho skill".
2. Chon map mau (khuyen nghi id 45, hoac cat vung tu 凤翔/华山).
3. Chon quai mau (ani001 sinh vat hay enemy003 nguoi) va chap nhan "toc do danh chua xac dinh -> dung gia tri cau hinh U003 ghi ro".
4. Cho phep doc them: `kunlun.lua` (server, chi doc) va KIpotLeaf/KgameWorldVN (client) de lam ro tick/hieu ung/che khuat/cooldown.
5. Cach xu ly hieu ung Loi Dong neu khong tim duoc projectile goc: dung `kl_16_魔法施放` + ung vien Con Lon da bao cao (ghi ro la ung vien), khong dung hieu ung tu che.
6. Ten project: JX1 Unity U003 - Idle Combat World (da chot); thu muc Unity rieng moi; khong dung lai U001/U002.
