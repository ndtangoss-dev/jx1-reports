# A-07b - Ra soat ep con tro 64 -> 32 bit trong server

## TOM TAT
1. Dung worktree `D:\JX-wt\A-07b`, nhanh `fix/a07b-ptr-truncation`; luc tiep tuc Git sach, chi co baseline `18c6f18`.
2. Giu nguyen cac sua da co o launch/GetGameData uParam va _findfirst; bo sung sua 23 file source cho pointer result, tham so, atomic, Lua, LZO va log.
3. Da quet 1151 file source/header; 6169 hit lexical (gom numeric/offset/nhanh client), doi chieu voi build x64, khong coi hit la loi tu dong.
4. LuaLibDll + Engine + Common + CoreServer build thanh cong v143 x64; gs001 bien dich qua, link bi chan boi ms64.lib cu thieu __imp___iob_func; khong co exe moi de hash.
5. Chua chay executable, chua ket noi VM/SQL/server; chua chung minh het crash HighEntropyVA. Trang thai build toan bo: PARTIAL; Git handoff o cuoi bao cao.

## Pham vi va cach tiep tuc

Task doc tu `D:\jx1-ops-wt\JX1_OPS\TASKS\A-07b.md`; doi chieu bao cao A-07 va script build-debug-a07.ps1. Khong sua task/bao cao ops ngoai writable root. Bao cao nay dat tai goc worktree theo ngoai le cua task. Khong ghi `C:\Jx1CocoV3` hay `D:\JX-build`; chi doc library, icon, header ADO va toolchain de lap ban build rieng.

Khong lam lai 3 diem da co trong baseline: `MultiServer/GameServer/KSOServer.cpp:963` da ep pCloneServer sang uintptr_t; duong goi GetGameData voi buffer da dung uintptr_t; `Core/Src/KSortScript.cpp:328` da dung intptr_t cho _findfirst. Line number trong task/A-07 cu khong con khop hoan toan.

Quet `Sources` (MultiServer tuong ung phan S trong task), Core, Engine, Library, MySql, AutoUpdateRes, FilterText, kem Headers/include va header dung chung `server/jxOnline/header`. Tim C-style/static/reinterpret cast, handle API, LPARAM/WPARAM/callback, kich thuoc pointer, format log va field ten handle/socket/addr/ptr. Bo comment nhung giu line number. Script scan chi tao inventory ung vien; phan loai dua tren kieu du lieu, producer/consumer, project exclusions va compiler. Khong tuyen bo regex hay build thay cho phan tich runtime.

## Bang file: dong da sua

Duong dan duoi day tinh tu `server/jxOnline/gameserver/Sources/`. Giu encoding/CRLF cua cac file nguon cu.

| File: dong hien tai | Phan loai va ly do |
|---|---|
| `Core/Src/CoreServerShell.cpp:163, 164, 1136, 1184, 1186, 1187, 1338` | CHAC CHAN: SGDI_CHECK_TONG tra dia chi qua int; doi return/local result va nParam co the mang pointer sang intptr_t. Cap nhat ca declaration va definition. |
| `Core/Src/CoreServerShell.h:13, 232, 234` | CHAC CHAN: dong bo ABI iCoreServerShell voi result/nParam intptr_t; include stdint.h tuong minh. |
| `Core/Src/KInventory.cpp:660, 666` | CHAC CHAN (log): m_pArray la int*, doi %d thanh %p va truyen void*. |
| `Core/Src/KPlayer.cpp:7474, 7494, 7650, 7671, 7829, 7850` | CHAC CHAN (log): 6 overload nhan char* ScriptFileName lai in %d; doi sang %s, giu cac overload dung dwScriptId. |
| `Core/Src/LuaFuns.cpp:84, 85, 123, 175, 178` | CHAC CHAN neu bat USEOLD: script-state handle truyen qua unsigned int/number; doi ca producer, consumer va lookup sang userdata/con tro that. |
| `Core/Src/S3PDBConnection.cpp:72, 103` | CHAC CHAN neu dung adapter MySQL cu: gan truc tiep &m_res/&m_res2, bo ep DWORD. |
| `Core/Src/S3PDBConnection.h:38` | CHAC CHAN: m_pRes chua dia chi Result/ResNSel; doi DWORD thanh void*. |
| `Core/Src/ScriptFuns.cpp:9805, 9809, 9810, 9811, 9812, 9813, 9814, 9815, 9816` | CHAC CHAN: LuaTestDropItem ep type tag int thanh int*; doc table 16 vao mang 6 int that, giu can bang stack, dung mang trong loi goi dong bo. |
| `Engine/Src/KCodecLzo.cpp:13, 45, 52, 53, 64, 65, 214, 215, 217, 218` | CHAC CHAN: so sanh/tru dia chi bi cat truoc khi kiem offset; dung uintptr_t. Bang 0x4000 pointer can 131072 byte tren x64, khong phai 65536; cap phat theo sizeof(BYTE*) va zero moi input. |
| `Engine/Src/KForBitGua----.cpp:181` | CHAC CHAN (log, ban sao khong build): base address in %08X qua DWORD; doi %p/void*. |
| `Engine/Src/KForBitGua--.cpp:181` | CHAC CHAN (log, ban sao khong build): base address in %08X qua DWORD; doi %p/void*. |
| `Engine/Src/KForBitGua.cpp:190` | CHAC CHAN (log, duoc Core build): base address in %08X qua DWORD; doi %p/void*. |
| `Engine/Src/KMemManager.cpp:13, 151, 193, 201` | CO THE: next vua la pointer vua la pool tag. So sentinel bang pointer day du; chi ha xuong int sau khi doc pool tag qua intptr_t. Khong doi layout allocator. |
| `Engine/Src/KNetServerNode.cpp:117, 182` | CHAC CHAN (log, khong nam Engine project hien tai): this/ims bi cat thanh int; doi %p/void*. |
| `Engine/Src/KStepLuaScript.cpp:296` | CHAC CHAN: callback OnMessage dung format d/int cho StateAddr; doi sang format p/void* da duoc CallFunctionS ho tro. |
| `Engine/Src/LuaFuns.cpp:108, 109, 147, 199, 202` | CHAC CHAN neu bat USEOLD: dong bo adapter cu voi opaque userdata; khong dua pointer qua double/unsigned int. |
| `Engine/Src/S3PDBConnection.cpp:72, 103` | CHAC CHAN neu dung ban adapter cu: bo ep dia chi Result/ResNSel thanh DWORD; header chung Core da doi void*. |
| `Library/LuaLib/src/llimits.h:65, 66` | CO THE/PHONG NGUA: IntPoint dung uintptr_t truoc khi shift; pointer hash khong con ep qua long 32-bit. |
| `Library/LuaLib/src/lstring.c:65` | Dong bo bien tam cua userdata hash thanh uintptr_t. Ket qua cuoi van la chi so bucket, khong doi layout TString. |
| `Library/LuaLib/src/ltable.c:43` | Dong bo bien tam pointer hash thanh uintptr_t; giu number hash cu va bucket mask. |
| `MultiServer/Common/Buffer.cpp:369, 370, 427, 428` | AN TOAN: 2 field serialize la ID 32-bit, khong phai dia chi; them static_cast co chu dich, giu wire format 4 byte. |
| `MultiServer/Common/OpaqueUserData.h:16, 17, 34, 46, 48, 51, 69` | CHAC CHAN/CO THE: bo fallback atomic LONG 32-bit, dung SDK pointer atomic; GetUserPtr load bang CompareExchange thay vi exchange gia tri co the cu. Integer accessors dung ULONG_PTR. |
| `MultiServer/GameServer/KSOServer.cpp:2021` | CHAC CHAN: TongBase nhan dia chi ten bang hoi qua int truoc strcpy; doi intptr_t de giu tron duong truyen. |

## Cac nhom an toan da doi chieu

| Vi tri/nhom | Ket luan |
|---|---|
| KSOServer.cpp:2829-2835 | pPlayers la WORD*, pPlayers[i] la ID so 16-bit; ep unsigned long khong phai ep dia chi. |
| KSOServer.cpp:5709, KSOServer.h:GetLocalIpAddress; Common/Socket*, Utils.cpp | DWORD/unsigned long la IPv4/client ID/protocol length; giu 32-bit. SOCKET thuc su va HANDLE van dung kieu SDK. |
| Common/IOCompletionPort.h/.cpp; SocketServer.cpp:354,441 va WorkerThread | Completion key dung ULONG_PTR tu producer toi GetQueuedCompletionStatus; OVERLAPPED va socket object van la pointer. |
| Common/Buffer.cpp:369,427,489 | lnUserData la field packet ID; 4 byte la giao thuc, khong phai sizeof(pointer). Socket user pointer duoc luu rieng trong ServerData. |
| Engine/KMemManager.cpp:125,151,193,201 | next trong block da cap phat la sentinel -1 hoac chi so pool, khong phai dia chi freelist. Da bo narrow cast truc tiep de the hien ro phan nay. |
| Engine/KBmp2Spr.cpp:137, KSpriteCodec.cpp:143, KCodecLzo.cpp ket qua PackLen/DataLen, KZipCodec.cpp | Hieu con tro duoc doi thanh length/offset cua buffer co kich thuoc DWORD, khong khoi phuc thanh dia chi tuyet doi. |
| AutoUpdateRes/src/aliases*.h | `(int)(long)&((struct stringpool_t*)0)->...` la offset cua string pool sinh tu dong, khong luu dia chi heap/module. Khong doi layout bang tra cua thu vien. |
| LuaLib/src/ltable.c | Hash chi dung chon bucket; pointer equality van dung pointer that. Doi hash trung gian sang uintptr_t la phong ngua/loai warning, khong khang dinh day la crash goc. |
| Engine/acc/acc_type.h:191-212; ucl cac nhanh DOS16 | Pointer type chon theo SIZEOF_VOID_P; nhanh unsigned long cho segmented pointer la DOS16, khong phai duong Windows x64. |
| Engine/KDDraw.cpp:SetWindowLong | GWL_STYLE/GWL_EXSTYLE la bit flags 32-bit, khong phai GWL_USERDATA/WNDPROC. |
| Engine/KThread.cpp, KNetThread.cpp; Heaven CPerConnectionData | _beginthreadex co prototype process.h, return duoc luu HANDLE; thrdaddr la thread ID unsigned int. Heaven param dung WPARAM/LPARAM pointer-sized. |

## Vi tri nghi ngo/chua sua va gioi han pham vi

| Vi tri | Phan loai / ly do chua sua |
|---|---|
| Core/Src/CoreShell.h:1014,1031,1083,1123 va CoreShell.cpp; cac CoreDataChanged cast trong KPlayer/KItemList/KProtocolProcess/KPlayerChat/... | CHAC CHAN neu build client x64: API callback/client uParam/nParam 32-bit va nhieu pointer cast. CoreShell.cpp bi ExcludedFromBuild cho Server Debug/Release; cac nhanh client tuong ung khong hoat dong trong build _SERVER da kiem. Chua doi client ABI/callback UI ngoai muc tieu gs001. Xem inventory de lay tung file:line. |
| Core/Src/KNpc_backup.cpp; KPlayer - Copy - Copy.cpp; Scene client files | Cac ban sao/nhanh client con cast CoreDataChanged; khong nam server build hien tai. Khong tua vao file backup de ket luan binary. |
| MySql/Include/mysql.h:51 va my_global.h:115-133 | CO THE neu khoi phuc MySQL adapter cu tren x64: typedef SOCKET unsigned int va SIZEOF_CHARP=4 khong phu hop Windows x64. Khong doi vendor struct/ABI khi chua co thu vien MySQL x64 tuong ung. Server hien tai dung MSSQL/ADO; S3PDBConnection cu khong nam project dang build. |
| Library/LuaLib/src/ltests.c:272 | Test-only cast userdata -> int; khong nam DLL build binh thuong. Chua chay/rebuild harness LUA_DEBUG cu. |
| Core/Engine LuaFuns.cpp USEOLD | Da sua producer/consumer sang userdata, nhung nhanh USEOLD khong duoc build/chay. Script cu coi handle la so can doi sang opaque handle; chua co tap script runtime de kiem. |
| KNetServerNode.cpp, hai KForBitGua--/----.cpp va S3PDBConnection.cpp cu | Da sua cast ro rang, nhung cac translation unit nay khong nam project server hien tai; chua compile doc lap voi cac cau hinh legacy. |
| Engine/Src/KThread.cpp:99 | Log pthread trong nhanh non-Windows con `(int)p_thread`; khong phai Windows HANDLE va khong vao Windows x64 build. Chua danh gia pthread_t theo ABI Linux dich. |
| Engine/Src/KForBitGua.cpp:182 | C4172 tra dia chi bien local; loi lifetime rieng, khong phai cat bit. Giu trong danh sach de xu ly task rieng. |
| Compiler C4789/C4473/C4717/C4700, format size_t/time_t/__int64 | Co warning san ve buffer/format/thieu doi so/recursion/uninitialized. Da sua pointer-format C4313, nhung khong mo rong thanh dot sua logic/format so hoc toan server. Log giu du chi tiet. |
| External ms64.lib, AutoUpdateRes.lib, libdb181.lib, USBKey libs | Khong co day du source/ABI va PDB cua binary dau vao. Chua the chung minh khong co cat pointer ben trong thu vien dong/static cu. |

## Build va bang chung

Build helper: `Sources/A07b/build-check.py`; scan helper: `Sources/A07b/scan-pointer-width.py`. Ban sao build va artifact nam trong `Sources/A07b/checkpoint-2/`, duoc .gitignore cuc bo loai khoi commit. Khong sua project tracked; tat post-build, override duong output/lib va v143/SDK trong project copy. Ban dau Debug gap inline _asm int 3 khong ho tro x64; chuyen sang cau hinh Release/Server Release, giu `/Od /Zi /RTC1 /MT /DEBUG:FULL`, `/GL-`, va charset .936. Day la build kiem tra, khong phai goi deploy.

`/we4302 /we4311 /we4312` bat loi explicit pointer cast; dot kiem tra CoreServer/gs001 cuoi them `/we4313` cho format pointer. Khong con C4302/C4311/C4312/C4313 trong log thanh phan da bien dich, khong thay C4013 (ham chua prototype) trong C sources duoc build. Compiler warning numeric/length va legacy khac van con.

| Thanh phan | Ket qua |
|---|---|
| LuaLibDll (Lua 4), Engine, Common | Build x64 thanh cong, exit 0. |
| CoreServer | Build x64 thanh cong, exit 0; dung LuaLibDll/Engine/Common import library moi. |
| GameServer/gs001 | Cac .cpp va resource compile qua; link fail LNK2001 `ms64.lib(mrcore.obj): __imp___iob_func`, LNK1120. |

Da doc shim tai `D:\JX-build\shim\iob_shim.cpp`: shim copy FILE vao mang gia; khong dua vao build nay vi chua chung minh ABI VC100/UCRT phu hop. Khong dung /FORCE de tao exe loi, khong tat HighEntropyVA. Can rebuild/thay ms64.lib bang ban x64 ho tro UCRT, hoac shim da duoc kiem chung ABI o task rieng.

Lenh tao checkpoint moi tu goc worktree (khong ghi de checkpoint da co):

~~~powershell
python server/jxOnline/gameserver/Sources/A07b/build-check.py --checkpoint=checkpoint-3
python server/jxOnline/gameserver/Sources/A07b/scan-pointer-width.py
~~~

Lenh MSBuild day du tung lan duoc luu trong `checkpoint-2/logs/commands.jsonl`. Cac log loi cu duoc giu tai `checkpoint/`, `checkpoint-2/logs-attempt1` den `logs-attempt4`. Checkpoint cu khong bi xoa. Resume chi build snapshot; khong ngam copy source moi.

23/23 file source da sua khop byte voi snapshot cuoi (`logs/final-source-check.json`). Snapshot/source manifests va inventory: `logs/scan-source-sha256.json`, `pointer-candidates.tsv`, `scan-summary.json`. Inventory hien co 5177 narrow-cast, 848 format, 18 pointer-size, 65 numeric-pointer-field, 36 callback, 25 handle-api hit; nhieu hit la chi so/offset/nhanh client/ma sinh tu dong, khong phai 6169 loi.

Da chay Microsoft dumpbin 14.44.35207 `/headers` chi doc tren cac DLL moi. Ca ba la machine 8664 x64, PE32+, van bat High Entropy Virtual Addresses + Dynamic base. Gia tri DllCharacteristics duoc ghi dung nhu header, khong suy ra tu flags project:

| Artifact | Bytes | SHA-256 | DllCharacteristics |
|---|---:|---|---|
| CoreServer.dll | 3613696 | `868c23632fda2d5357bdf1e6a34e70bdbd9fea486a3e298f06790b9f709fce38` | `0x0060` |
| Engine.dll | 1385472 | `c5837fb97c6213b5632fec9d102c179b08b8e89dbd5f39673f4c2bbceea8551b` | `0x0160` |
| LuaLibDll.dll | 815616 | `018285d4d879040c570146c4911ba7eda5e49531c1b2f736dbfe97d1b82e9a81` | `0x0160` |

Headers thuc nam o `checkpoint-2/out/*-headers.txt`; hashes o `logs/artifact-sha256.json`. **Khong co gs001.exe moi hop le, nen khong co SHA-256/DllCharacteristics cua exe moi.** Khong lay hash exe cu de thay the.

## Chua kiem

- Runtime HighEntropyVA, dia chi heap thuc, first-chance dump va dong crash goc: chua kiem; khong khang dinh cac sua nay da giai quyet crash van hanh.
- Round-trip LZO, heap tren bien 4 GiB, bang hoi/invite, LuaTestDropItem va callback/script USEOLD: chua chay do task cam chay exe.
- Cau hinh client, Linux, Win32, module Heaven/Rainbow binary, adapter MySQL va ABI vendor DLL/static libs: chua build/kiem runtime.
- ABI thay doi: can rebuild va dong goi CoreServer + gs001 cung header; Common inline/user-data thay doi can rebuild cac module mang tu source phu hop. Khong tron DLL cu vao ban thu moi. Chua deploy hay thay binary ngoai checkpoint.
- Chua cap nhat file task ops vi nam ngoai writable root. PM dung bao cao nay de cap nhat Ket qua/Da thu nhung khong duoc/Buoc tiep theo.

## Ket qua Git va ban giao

**CHUA STAGE / CHUA COMMIT / CHUA PUSH.** Da thu `git add` dung 28 file (23 source + 4 file cong cu + bao cao) mot lan, that bai:

~~~text
fatal: Unable to create 'D:/JX-source/.git/worktrees/A-07b/index.lock': Permission denied
~~~

Metadata Git nam ngoai writable root. Khong doi permission/config/safe.directory, khong tao kho Git thay the. PM/chu may commit trong phien co quyen ghi metadata (cac checkpoint da duoc .gitignore cuc bo loai tru):

~~~powershell
git add -- A-07b-ep-con-tro.md server/jxOnline/gameserver/Sources/Core server/jxOnline/gameserver/Sources/Engine server/jxOnline/gameserver/Sources/Library/LuaLib/src server/jxOnline/gameserver/Sources/MultiServer/Common/Buffer.cpp server/jxOnline/gameserver/Sources/MultiServer/Common/OpaqueUserData.h server/jxOnline/gameserver/Sources/MultiServer/GameServer/KSOServer.cpp server/jxOnline/gameserver/Sources/A07b
git diff --cached --stat
git commit -m 'A-07b: Fix server x64 pointer truncation and record build audit'
~~~

Truoc khi stage bang duong dan thu muc o tren, kiem `git status` de khong gom thay doi moi cua nguoi khac. Khong co commit SHA vi thao tac stage bi chan. `git diff --check` cuoi thanh cong.

Buoc tiep theo: xu ly __imp___iob_func trong ms64.lib de link gs001 bang toolchain v143/UCRT, ghi hash/header exe moi, sau do nguoi van hanh thu trong moi truong duoc cap phep va thu dump. Nhanh client x64/adapter vendor cu can task rieng neu duoc dua vao pham vi hoat dong.
