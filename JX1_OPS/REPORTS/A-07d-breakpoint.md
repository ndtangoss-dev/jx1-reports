TÓM TẮT 1/5: Phân tích tĩnh tại D:\JX-wt\A-07d, nhánh fix/a07c-link, HEAD 3802d29; không build/chạy sản phẩm, không stage/commit/push.
TÓM TẮT 2/5: Không thấy breakpoint trực tiếp còn hiệu lực trong bốn vùng nguồn; SceneMath.cpp:164 là comment, int3 của Common/Macro.h chỉ thuộc _DEBUG.
TÓM TẮT 3/5: Ưu tiên kiểm /RTC1: KPlayer.cpp:1377, KItemList.cpp:4141, ScriptFuns.cpp:1068 ghi quá mảng; ScriptFuns.cpp:9441 dùng biến chưa khởi tạo; chưa chứng minh gây lần dừng đang xét.
TÓM TẮT 4/5: Chưa thấy lịch cố định 225 giây; có worker ~1 s/~300 s, script theo phút UTC, Lua GC theo cấp phát; nhiều nhánh autosave 5 phút đã comment.
TÓM TẮT 5/5: Đề xuất WER LocalDumps riêng gs001.exe và cdb first-chance trong VM thử; custom exception filter có thể ngăn WER, cần dump và EXE/DLL/PDB đúng phiên bản để kết luận.

# A-07d — Điều tra breakpoint 0x80000003 của gs001

## Phạm vi và bằng chứng

Ngày 2026-11-17 (Asia/Bangkok). Đã đọc task A-07d, báo cáo A-07c, `D:\JX-wt\A-07b\A-07b-ep-con-tro.md`, diff A-07b (`8fde733`) và cấu hình project. Không tìm thấy AGENTS.md trong các thư mục cha đã kiểm và cây Sources. Các đường dẫn bảng dưới tính từ `server/jxOnline/gameserver/Sources/`, trừ khi ghi khác.

`client`, `server`, `JX1_OPS` tại worktree này liên kết sang A-07c; metadata Git thực là `D:/JX-source/.git/worktrees/A-07c`. Chỉ ghi báo cáo được giao, không sửa source/task/checkpoint. Git ban đầu chỉ báo `?? JX1_OPS/`.

Đã tìm trong Core, Engine, MultiServer/GameServer. **LuaLibDll thực tế là `Library/LuaLib/LuaLibDll.vcxproj`**, không có thư mục Sources/LuaLibDll. Mở rộng đọc Common/Macro.h, Common/OpaqueUserData.h và `server/jxOnline/header/kgpublic.h` để giải nghĩa macro. Dùng git grep và Python vì không có rg. Phân biệt comment, guard tiền xử lý và file có/không có trong project; inventory lexical không chứng minh mã đã được compile.

Chỉ đọc thêm log/map/disassembly **đã có** tại `A07b/checkpoint-a07c-final/`; không chạy lại build helper hay dumpbin. KPlayer.cpp, KItemList.cpp, ScriptFuns.cpp, CoreServerShell.cpp, KSOServer.cpp và GameServer.cpp hiện tại khớp SHA-256 với nguồn snapshot đó. Không có dump, exception address, module list của VM, log thời điểm dừng hay script/config runtime. **Chưa xác định được nguyên nhân gốc của lần dừng ~225 s.**

## 1. Breakpoint và assertion

| Vị trí | Kết luận tĩnh |
|---|---|
| `Core/Src/Scene/SceneMath.cpp:163,164` | `_ASSERT(false); DebugBreak();` nằm trong comment :142–178. File còn bị ExcludedFromBuild cho Server Release/Debug (Core.vcxproj:1024 và các dòng sau). Loại khỏi ứng viên trực tiếp. |
| `Engine/testsrc.asm:11,16` | Hai `int 3` trong mã thử nghiệm, không nằm trong compile input Engine.vcxproj. Các listing Core/ClientRelease và ClientReleasex là output client cũ. |
| `MultiServer/Common/Macro.h:29,34,38,41,44` | ASSERT/VERIFY dùng `_asm { int 0x03 }` dưới _DEBUG; Release ASSERT rỗng, VERIFY chỉ đánh giá biểu thức. Đây là nguồn inline-asm từng cản Debug x64; không chứng minh bản A-07c Release phát breakpoint qua macro này. |
| `Engine/Src/KDebug.h:20,21,23`; `Engine/Src/KDebug.cpp:109,112,114,115` | KASSERT chỉ bật với _DEBUG; handler ghi log, MessageBox rồi exit(1), không gọi DebugBreak. |
| `server/jxOnline/header/kgpublic.h:18`; `Core/Src/MyAssert.H:7,12` | Có đường ASSERT → assert và ASSERT_VALID → _ASSERT; phải xét header/guard của đúng translation unit. |
| `Core/Src/KRegion.cpp:1995` | ASSERT(FALSE) khi thêm player đã có node reference. Nghi trạng thái/lifetime nếu stack và cấu hình assertion phù hợp, không phải lịch cố định. |
| `Core/Src/KNewProtocolProcess.cpp:103,117,131,145` | ASSERT(pBuffer) trên đường gửi packet. Chỉ ưu tiên nếu stack về đây. |
| `Core/Src/S3PDB_MSSQLServer_Connection.cpp:286`; `Core/Src/S3P_MSSQLServer_Result.cpp:76` | assert(0) trên đường lỗi ADO/result. Có trong Core project; assert chuẩn bị NDEBUG tắt trong Server Release. |
| `Core/Src/KLogFile.cpp:36,100,174,224`; `Engine/Src/KLogFile.cpp:29,93,167,217` | Kiểm threshold/path của log; không thấy lịch 225 s, assert chuẩn phụ thuộc NDEBUG. |
| `Core/Src/kbufpool.cpp:82`; `Core/Src/kgc_dbmanager.cpp:145,212,314,321,333,348,403,424,632,649,842,872` | Có ASSERT(FALSE), nhưng các .cpp này không nằm trong compile input Core.vcxproj đang dùng; kgc_dbmanager còn có KG_GC_SERVER. |
| `MultiServer/GameServer/KSOServer.cpp:1738,1754,2798,2799,2856,2861,3113,3509` | _ASSERT ngoài comment: kiểm kích thước protocol/độ dài chat, relay và lỗi transfer. _ASSERT thuộc cấu hình debug CRT. Các hit :3915 v.v. ở vùng comment cũ. |
| `Library/LuaLib/src/lobject.h:15,16,18,19,21,22` | LUA_ASSERT/LUA_INTERNALERROR bật với LUA_DEBUG, khi đó còn undef NDEBUG. LuaLibDll.vcxproj hiện không khai báo LUA_DEBUG. |
| `Engine/Include/luaconf.h:724,726` | luai_apicheck → assert chỉ với LUA_USE_APICHECK; không tự suy ra Lua 4 DLL đang bật API assertions. |

Không thấy `__debugbreak`, `_CrtDbgBreak` hoặc `RaiseException` trong bốn vùng nguồn đã tìm. Phụ lục liệt kê toàn bộ vị trí assertion lexical trong source/header, cả KASSERT và LUA_ASSERT; không đồng nhất chúng với các điểm breakpoint thật của binary.

## 2. Hướng ưu tiên: runtime checks do compiler chèn

`A07b/build-check.py:54,55` đặt Optimization=Disabled và BasicRuntimeChecks=EnableFastChecks. Define Release vẫn giữ: Core.vcxproj:596 có NDEBUG + _SERVER; GameServer.vcxproj:178 có NDEBUG. **Release ở đây vẫn có /RTC1.** Theo [Microsoft /RTC](https://learn.microsoft.com/en-us/cpp/build/reference/rtc-run-time-error-checks?view=msvc-170), /RTC1 gồm kiểm stack và biến chưa khởi tạo; không tự bao gồm /RTCc kiểm thu hẹp số.

Bằng chứng đã có: `out/GameServer.map:867,887,888` chứa _RTC_CheckStackVars, _RTC_StackFailure và _RTC_UninitUse từ LIBCMT. `out/gs001-disasm.txt:82804` gọi hàm gián tiếp trong `failwithmessage`, :82805 so kết quả với 1, :82807 có **CC / int 3** tại preferred VA `0x14004B94E`, tức **RVA 0x4B94E**. Đây là breakpoint có nhánh điều kiện trong runtime, khác byte CC làm padding giữa hàm. `out/CoreServer.map:6391` cũng có _RTC_UninitUse. Địa chỉ chỉ dùng đối chiếu đúng artifact A-07c; ASLR thay VA thực.

| Ưu tiên | File:dòng | Lỗi và điều kiện để liên quan |
|---|---|---|
| P1 | `Core/Src/KPlayer.cpp:1362,1377` | BuyItem khai báo nRItemLevel[6] rồi ghi nRItemLevel[6], quá 4 byte. Log CoreServer.log có C4789 ngay :1377. Phù hợp _RTC_StackFailure khi đường mua item chạy. |
| P1 | `Core/Src/KItemList.cpp:4140,4141` | BlueBianShi khai báo nMagRows[6] rồi khởi tạo cả [6]. C4789 trong log cũ. Cần đường nhận diện item thực sự được gọi. |
| P1 | `Core/Src/ScriptFuns.cpp:1053,1068` | LuaGetShopItemData lặp lại lỗi nRItemLevel[6]. C4789 trong log. Cần script lấy lại item đấu giá chạy. |
| P1 | `Core/Src/ScriptFuns.cpp:9291,9325,9441` | LuaITEM_DropOneItem khai báo int nItemIndex không gán rồi đưa vào Lua_PushNumber tại :9441; biến dùng tạo item là nItemIdx. C4700 đã có trong log; phù hợp _RTC_UninitUse khi callback chạy. |
| P2 | `Core/Src/CoreServerShell.cpp:3528,3599` | sprintf dùng itemName làm format. Dữ liệu chứa % có thể đọc đối số không có/ghi sai; cần stack và dữ liệu. Không phải bằng chứng truncation hoặc breakpoint tự thân. |
| P2 | `Engine/Src/KForBitGua.cpp:156,182` | Trả địa chỉ me32.szExePath thuộc biến stack; C4172 có trong log. Lỗi lifetime còn tồn tại sau A-07b, chỉ liên quan nếu caller dùng kết quả. |
| P2 | `Core/Src/kregionsearcher.h:45` | Log cũ có C4717 constructor đệ quy vô hạn. Phải phân biệt stack overflow 0xC00000FD với breakpoint 0x80000003. |
| P2 | `KSOServer.cpp:5567,5570` so với :4370 | Worker gọi ExeCoreTask/CheckItemTime; MainLoop dùng g_csFlow, case 6 không lấy cùng lock tại đây. Có khả năng truy cập player/item đồng thời; cần stack mọi thread trước khi đề xuất sửa đồng bộ. |

Các P1 là lỗi mã rõ ràng, nhưng **chưa có bằng chứng chúng chạy lúc 225 s**. Nếu server trống, chưa có thao tác item/player, hạ ưu tiên các nhánh có điều kiện player và xem script khởi động/backend/network/runtime/DLL ngoài. Không sửa lỗi trong task chỉ đọc. Không tắt /RTC hoặc HighEntropyVA để coi như đã chữa xong.

## 3. Lịch định kỳ và mốc ~225 giây

| Đường gọi / dòng | Chu kỳ suy ra và giới hạn |
|---|---|
| `KSOServer.cpp:93,1444,1447,1456,1460` → MainLoop:4378 → `CoreServerShell.cpp:2233,2238,2239,2264` | LogicFps là 18 hoặc 36; Core bỏ nửa vòng full ở 36 để giữ full game tick ~18 Hz. 225 s tương ứng ~4050 full tick hoặc 8100 vòng GS ở 36 Hz; chưa thấy timeout tương ứng. Phân biệt uptime process với thời gian sau init/timer start. |
| `KSOServer.cpp:36,675,681,685,688,695,697,1304` | ThreadSaveDataTask tăng counter mỗi vòng, Sleep(10) chỉ vòng lẻ. TIME_FARM=200: case 6 khoảng 1 s; case 7 mỗi 60000 vòng khoảng 300 s, phụ thuộc scheduler/tác vụ. Không phải 200 giây và không phụ thuộc GAME_FPS. |
| `KSOServer.cpp:5564,5567,5570,5573,5576`; `CoreServerShell.cpp:3213,3262,3707,3732,3734` | Case 6 xử lý player/offline và hạn item; case 7 đồng bộ đấu giá. Hạn item phụ thuộc dữ liệu lưu nên có thể đến sau 225 s mà không có hằng 225. Cần log iid, hạn, uptime và thread. |
| `CoreServerShell.cpp:3249–3260,3388–3466`; `Core/Src/KPlayer.h:48` | Các nhánh grep thấy defPLAYER_SAVE_TIMEOUT=18*60*5 đều comment; không phải bằng chứng autosave đang chạy. |
| `Core/Src/KPlayerSet.cpp:42,1774,1782`; `Core/Src/KSubWorldSet.cpp:619` | AutoSave dùng 5400 tick = 5 phút ở 18 Hz, nhưng lời gọi MainLoop bị comment; không thấy lời gọi trực tiếp còn hiệu lực khác trong bốn vùng. Không đổi 300 s thành 225 s chỉ bằng phỏng đoán. |
| `CoreServerShell.cpp:2209,2216,2242,2245,2249,2251` | StartGame từ system/serverscript.lua khi launch; servertimer.lua/Main khi game time chia hết 18 và giây UTC bằng 0. Script có thể cài timer riêng. Không có các Lua runtime này trong tracked source để kiểm lịch. |
| `KSOServer.cpp:626,640,643,646,647`; `Core/Src/KSubWorld.cpp:183–195` | Worker transfer reconnect theo counter; query ranking lúc đầu và mốc 07:00:00; case 9 mỗi 6 vòng. stateActivate hiện chỉ có comment. Không thấy cleanup toàn server hard-code 225 s tại đây. |
| `KSOServer.cpp:4386,4393–4395,4402,4425,773–775`; `Core/Src/KPlayer.h:26` | Quét một status/vòng, ping 5/30 s, login 15 s. MaxGameStaus đọc config rồi bị gán MAX_PLAYER=500, nên vòng status ~27,8 s ở 18 Hz; không phải 4096/18 s. Retry kéo dài tùy trạng thái. |
| `Library/LuaLib/src/lgc.c:339,344,349–351` | GC khi nblocks >= GCthreshold; sau thu gom đặt threshold=2*nblocks. Theo lượng cấp phát, không phải đồng hồ 225 s; lỗi heap trước đó có thể lộ lúc GC/cleanup. |
| `Engine/Src/KTimer.cpp:122,132,135,136`; `KSOServer.cpp:1436` | Windows dùng hiệu QPC 64-bit hoặc GetTickCount64; reset GameLoop ở 1512000 vòng. Không thấy overflow timer 32-bit ở 225 s trong đường này. |

Chưa có cơ sở chốt “autosave sau 225 giây”. Lần thử sau cần so uptime với phút UTC, vòng worker, hạn item và script. Cùng tick gợi ý logic/tick; cùng phút đồng hồ gợi ý script; phụ thuộc lượng cấp phát gợi ý GC/heap. Đây là đề xuất phân loại, chưa phải kết quả thử.

## 4. Đối chiếu pointer/handle với A-07b

Đã đọc diff A-07b, quét lại narrow casts, biến DWORD/int có tên Handle/Socket/Addr/Ptr, _findfirst/_beginthreadex, callback và producer/consumer. **Chưa xác nhận thêm trường hợp cắt địa chỉ 64→32 còn chạy trên gs001 trong phạm vi nguồn này.** Không đồng nghĩa toàn bộ chương trình/thư viện nhị phân đã sạch.

| Vị trí | Kết quả |
|---|---|
| `KSOServer.cpp:963,2021,2022`; `CoreServerShell.h:218,232,234,240`; `CoreServerShell.cpp:1184,1187,1338` | Launch dùng uintptr_t; GetGameData trả intptr_t; tên bang hội không còn đi qua int TongBase. Các int nhận NETID/ID/status là số. GetGameData_New uParam còn unsigned long nhưng các case hiện dùng chỉ số/ID, chưa thấy producer đưa địa chỉ vào đó. |
| `Engine/Src/KCodecLzo.cpp:45,52,53,64,65,215,218` | So sánh/trừ địa chỉ dùng uintptr_t; 0x4000 pointer cấp phát theo sizeof(BYTE*) và zero mỗi input; không quay lại bảng 65536 byte cho x64. |
| `Engine/Src/KMemManager.cpp:189,190,193,201` | intptr_t → int ở :201 là pool tag sau sentinel check, không phải địa chỉ freelist. Nếu heap hỏng cần kiểm magic/tag; hiện lỗi magic chỉ hiện MessageBox rồi tiếp tục. |
| `Core/Src/KSortScript.cpp:328,332,369` | _findfirst lưu intptr_t, _findnext nhận cùng handle; không thấy int còn sót trên đường này. |
| `MultiServer/Common/OpaqueUserData.h:34,46,48,51,69`; `Common/Buffer.cpp:370,428` | Pointer atomics và ULONG_PTR giữ địa chỉ; packet user data vẫn serialize unsigned int ID 32-bit có chủ đích, không đổi wire format. |
| `Core/Src/CoreShell.cpp:480,6861`; `KPlayer.cpp:5085,9166`; `KItemList.cpp:660`; `KPlayerChat.cpp:733`; `ScriptFuns.cpp:25538` | Vẫn có cast địa chỉ sang unsigned int/DWORD/int ở client/callback UI. CoreShell.cpp bị exclude ở Server; các đoạn tương ứng trong file chung thuộc nhánh client. Nợ client x64 đã ghi A-07b, chưa chứng minh là đường crash gs001. |
| `Library/LuaLib/src/llimits.h:66`, `lstring.c:65`, `ltable.c:43,85` | Pointer hash đã dùng uintptr_t. Cast long tại luaH_getnum:85 xử lý Number key, không phải địa chỉ. |
| `Library/LuaLib/src/ltests.c:37,272` | Còn userdata → int → Lua number trong LUA_DEBUG. File có trong project nhưng thân test bị guard; build hiện không khai báo LUA_DEBUG. Nếu bật test phải sửa round-trip, không chỉ hash. |
| `Core/Src/KForBitGua.cpp:335`; `Engine/Src/KForBitGua.cpp:336–340` | DWORD dwHandle thuộc API version-info legacy; HMODULE thật vẫn dùng HMODULE. Tên Handle không chứng minh truncation. |
| `Engine/Src/KMp4Video.h:22`; `KMp4Video.cpp:292,293,306` | DWORD m_dwHandle tạo từ GetTickCount làm codec ID, không từ pointer/HANDLE; video không phải đường game logic đang xét. |
| `Engine/Src/KThread.cpp:88,99`; `KNetThread.cpp:79` | Windows _beginthreadex cast thẳng sang HANDLE; :99 là log pthread trong nhánh non-Windows. |
| Vendor MySql, `Core/Src/db.h:125`, static libs/DLL ngoài | Có typedef/ABI legacy (ví dụ uintptr_t 32-bit) phải xét guard/include thực và binary tương ứng; không tự sửa hàng loạt. Không đủ source/PDB để loại trừ lỗi bên trong ms64.lib hoặc DLL backend cũ. |

0x80000003 không tự chứng minh truncation: pointer sai có thể đưa RIP vào padding CC hoặc làm runtime phát breakpoint. Cần thấy producer có đủ 64 bit, field/local làm mất high DWORD, rồi consumer dùng địa chỉ đã cắt. Giữ HighEntropyVA khi lấy bằng chứng. Các lỗi mảng/lifetime ở mục 2 là nhóm lỗi khác, không gán nhầm thành cắt pointer.

## 5. Đề xuất thu dump trong VM thử — chưa thực hiện

### Bộ binary và custom crash handler

Giữ EXE/DLL/PDB cùng snapshot, hash và module paths. Theo báo cáo A-07c, gs001.exe có SHA-256 `0c14250622f79ee2db90653ce769afb3f48d5005641662cc880f451f6dbfbe5c`; chưa xác minh VM dùng đúng bản. /MT có thể đặt runtime ngay trong gs001/CoreServer/LuaLibDll, không cần thấy ucrtbased.dll mới nghi RTC.

**Điểm ảnh hưởng WER trong mã:** `GameServer/GameServer.cpp:146` đăng ký ExceptionFilter (:129). Khi không có debugger, gọi GenerateMiniDump (:136), ghi `DumpInfo` tương đối với cwd (:93–102), dùng MiniDumpWithDataSegs (:114,115), trả EXCEPTION_EXECUTE_HANDLER (:125). Không kiểm kết quả MiniDumpWriteDump. Tìm dump này ở cwd thực của process trước; nó không phải full-memory dump.

Microsoft nêu LocalDumps không hỗ trợ ứng dụng có custom crash reporting và không thu khi bật automatic debugging. **Bật registry không bảo đảm WER thu được dump của gs001.** Nếu không có WER dump hoặc process chỉ dừng, dùng cdb first-chance; không thay filter trong task này. [Microsoft LocalDumps](https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps).

### WER theo tên executable

Chỉ là lệnh đề xuất cho người vận hành **trong VM thử**, PowerShell 64-bit quyền Administrator, chưa chạy ở máy này. Cấp Modify cho đúng tài khoản chạy gs001 vào C:\JX1Dumps (kể cả service account), đảm bảo đủ dung lượng. Kiểm tra AeDebug/automatic debugging và custom handler trước khi kỳ vọng dump.

```powershell
New-Item -ItemType Directory -Path 'C:\JX1Dumps' -Force
$jxWerKey = 'HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\gs001.exe'
reg.exe query $jxWerKey /reg:64
if ($LASTEXITCODE -eq 0) {
    reg.exe export $jxWerKey 'C:\JX1Dumps\gs001-LocalDumps-before.reg' /y
}
reg.exe add $jxWerKey /v DumpFolder /t REG_EXPAND_SZ /d 'C:\JX1Dumps' /f /reg:64
reg.exe add $jxWerKey /v DumpType /t REG_DWORD /d 2 /f /reg:64
reg.exe add $jxWerKey /v DumpCount /t REG_DWORD /d 5 /f /reg:64
reg.exe query $jxWerKey /reg:64
```

DumpType=2: full dump; DumpCount=5: số dump giữ; chỉ áp dụng gs001.exe, không thay global settings. Sau thử: nếu key có sẵn thì phục hồi ba giá trị theo export, loại giá trị mới trước import nếu trước đó chưa có; nếu key mới hoàn toàn thì chỉ xóa key gs001.exe vừa tạo. Không xóa global LocalDumps/dump bằng chứng.

### cdb first-chance khi WER không thu hoặc process chỉ dừng

Dùng cdb x64 attach đúng PID trước mốc lỗi, với quyền debug process và PDB đúng build. Ví dụ thay PID/đường dẫn thực:

```text
cdb.exe -p <PID_GS001> -y "C:\JX1Symbols;srv*C:\Symbols*https://msdl.microsoft.com/download/symbols" -logo C:\JX1Dumps\gs001-live.txt
```

Attach có điểm dừng ban đầu do debugger, không phải lỗi 225 s. Tại prompt ban đầu:

```text
sxe bpe
sxe av
g
```

Tại lần dừng bất thường kế tiếp, ghi trước khi tiếp tục:

```text
.lastevent
.exr -1
r
kv
~* kv
lm
.time
.dump /ma /u C:\JX1Dumps\gs001-firstchance.dmp
```

sxe dừng first chance, /ma lưu full memory và thông tin bổ sung, /u thêm định danh tránh đè dump. Không tự g qua lỗi trước khi lưu. Có exception context thì dùng .ecxr; nếu chỉ attach/pause thì giữ context thread hiện tại và ghi rõ không phải original exception. Chạy debugger và WER là hai cách thử riêng, không kỳ vọng WER thu khi debugger đang attach. [Microsoft sxe](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-), [Microsoft .dump](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-dump--create-dump-file-).

### Phân tích offline

```text
cdb.exe -z "C:\JX1Dumps\<dump>.dmp" -y "C:\JX1Symbols;srv*C:\Symbols*https://msdl.microsoft.com/download/symbols" -logo C:\JX1Dumps\gs001-analysis.txt
```

```text
.reload /f
.lastevent
!analyze -v
.exr -1
.ecxr
r
kv
~* kv
lm
lmvm gs001
lmvm CoreServer
lmvm Engine
lmvm LuaLibDll
ln @rip
ub @rip L10
u @rip L10
.time
```

Nếu không có exception context, .ecxr có thể thất bại; dùng thread/context được lưu, ghi rõ dump chụp thủ công. PDB lệch thì không suy tên source/line và không ép bỏ mismatch. Đặt .srcpath về source đúng snapshot nếu cần. Dùng số frame từ kv với `.frame /r <n>` rồi `dv /t` để xem locals còn trong dump.

Phân loại để quyết định patch:

1. Stack có _RTC_UninitUse/_RTC_StackFailure/failwithmessage: tìm caller đầu tiên thuộc source, so bốn P1, tên biến/mảng và thông báo RTC. RVA 0x4B94E chỉ áp đúng EXE A-07c; không dùng preferred VA như địa chỉ runtime cố định.
2. _CrtDbgReport/_wassert/DebugBreak/ASSERT thư viện: lấy caller, biểu thức, module và define build. NDEBUG của EXE không áp cho DLL khác.
3. RIP vào padding CC hoặc stack/return address hỏng: nghi control-flow corruption/use-after-free; không coi mọi CC là assertion có chủ ý. Dùng `!address <address>` và `!heap -p -a <address>` khi heap/dump hỗ trợ; thiếu metadata không chứng minh heap tốt.
4. ntdll!DbgBreakPoint/DbgUiRemoteBreakin ngay attach: loại khỏi thống kê tái hiện; cần bắt sự kiện sau đó.
5. Stack cho thấy callback/ABI hoặc địa chỉ mất high DWORD: so module hashes và ABI iCoreServerShell đã đổi ở A-07b, kiểm EXE/DLL có cùng bộ trước khi sửa thêm cast.

Kèm dump: PID/TID, thời gian bắt đầu process/hoàn thành init, uptime, giờ UTC, command line/cwd, LogicFps, số player, thao tác cuối, script/config hash, log trước lỗi và module paths/hashes. Chỉ sau đó mới kết luận root cause/đề xuất patch ứng với stack.

## 6. Kiểm tra và bàn giao

Đã đọc mã/project/diff/log/map/disassembly và tài liệu Microsoft; không build, chạy executable/DLL sản phẩm, attach process, kết nối VM/SQL, đổi registry hoặc triển khai. Không có kiểm thử runtime trong task này. Chỉ tạo báo cáo; không stage/commit/push. PM review và commit riêng file báo cáo, không gom toàn bộ JX1_OPS đang untracked.

## 7. Phu luc: inventory assertion trong source/header

Quet 687 file tracked .c/.cpp/.h/.hpp/.inl/.inc/.ch trong bon vung, co 619 token assertion/macro tai 88 file. Bo comment va string literal, giu so dong. Gom ca dinh nghia macro, code duoi guard va file khong build; khong dem la 619 breakpoint runtime. Cac listing .asm client cu khong nam trong bang. DebugBreak/comment va int3 assembly thu nghiem da phan loai o muc 1. Khong co __debugbreak/_CrtDbgBreak/RaiseException trong bon vung.

| File (tu Sources/) | Macro | Dong |
|---|---|---|
| `Core/Src/KBasPropTbl.CPP` | _ASSERT | 238, 245, 261, 364, 365, 374, 424, 427, 429, 439, 443, 447, 451, 741, 742, 755, 756, 761, 859, 860, 906, 911, 926, 951, 952, 975, 976, 993, 994, 1034, 1035, 1049, 1075, 1076, 1122, 1123, 1138, 1165, 1166, 1225, 1226, 1239, 1265, 1266, 1319, 1324, 1345, 1346, 1422, 1423, 1439, 1448, 1476, 1477, 1566, 1567, 1584, 1591, 1626, 1627, 1722, 1723, 1740, 1747, 1776, 1777, 1866, 1867, 1885, 1894, 1924, 1925, 1991, 1992, 1998, 1999, 2049, 2050, 2051, 2067, 2068, 2127, 2128, 2129, 2130, 2165, 2166, 2167, 2181, 2182, 2195, 2196, 2197 |
| `Core/Src/KBuySell.cpp` | KASSERT | 283, 603, 604 |
| `Core/Src/KCore.cpp` | _ASSERT | 443, 1006, 1237 |
| `Core/Src/KCore.cpp` | KASSERT | 879, 880, 881 |
| `Core/Src/KCore.cpp` | assert | 1171, 1175 |
| `Core/Src/KFaction.cpp` | _ASSERT | 166, 178 |
| `Core/Src/KGMProcess.cpp` | _ASSERT | 47 |
| `Core/Src/KItem.cpp` | _ASSERT | 142, 143, 267, 268, 410, 431, 458, 474, 490, 505, 680, 700, 1847, 1848, 1849, 1852 |
| `Core/Src/KItemGenerator.CPP` | _ASSERT | 111, 112, 151, 152, 275, 276, 359, 642, 643, 920, 921, 991, 1024, 1025, 1075, 1558, 1559, 1785, 1786, 1993, 1994, 2231, 2232, 2338, 2692, 2693, 2785, 3214, 3215, 3597, 3598, 3626, 3627, 3664, 3665, 3728, 3729, 3812, 3813, 3880, 3881 |
| `Core/Src/KItemGenerator.CPP` | KASSERT | 3122 |
| `Core/Src/KItemList.cpp` | _ASSERT | 120, 157, 818, 1212, 1399, 1870, 2528, 2595, 2718, 7809, 7857, 8506, 8525, 8696, 8714, 9122, 10966 |
| `Core/Src/KItemSet.cpp` | _ASSERT | 514, 515 |
| `Core/Src/KLogFile.cpp` | assert | 36, 100, 174, 224 |
| `Core/Src/KLogFile.cpp` | _ASSERT | 278 |
| `Core/Src/KMissionArray.h` | _ASSERT | 25, 93 |
| `Core/Src/KMissle.cpp` | _ASSERT | 963, 1188, 1189, 1616, 1651, 1672 |
| `Core/Src/KNewProtocolProcess.cpp` | ASSERT | 103, 117, 131, 145 |
| `Core/Src/KNpc.cpp` | _ASSERT | 499, 509, 2862, 2935, 3071, 3775, 3781, 3867, 3942, 6914, 7712, 7850, 7853, 15167, 16489 |
| `Core/Src/KNpcAI.h` | _ASSERT | 126, 127 |
| `Core/Src/KNpcSet.cpp` | _ASSERT | 1828 |
| `Core/Src/KNpc_backup.cpp` | _ASSERT | 495, 505, 2845, 2918, 3048, 3714, 3720, 3806, 3881, 7198, 8003, 8141, 8144, 15338, 16650 |
| `Core/Src/KPlayer - Copy - Copy.cpp` | _ASSERT | 3774, 3835 |
| `Core/Src/KPlayer.cpp` | _ASSERT | 3714, 3775 |
| `Core/Src/KPlayerDBFuns.cpp` | _ASSERT | 176, 1396, 1620, 1734, 1756, 1767, 1798 |
| `Core/Src/KPlayerDBFuns.cpp` | KASSERT | 441, 820, 1156, 1219, 1270 |
| `Core/Src/KPlayerMenuState.cpp` | _ASSERT | 152 |
| `Core/Src/KProtocolProcess.cpp` | _ASSERT | 351, 354, 2487, 2509, 4677, 4727, 4746 |
| `Core/Src/KRegion.cpp` | _ASSERT | 516, 1244, 1277, 1324, 2616 |
| `Core/Src/KRegion.cpp` | ASSERT | 1995 |
| `Core/Src/KSkillList.cpp` | _ASSERT | 1056, 1127 |
| `Core/Src/KSkillManager.cpp` | _ASSERT | 68, 88, 129, 149, 197 |
| `Core/Src/KSkills.cpp` | _ASSERT | 51, 59, 101 |
| `Core/Src/KSubWorld.cpp` | _ASSERT | 1195, 2761, 2780 |
| `Core/Src/KTaskFuns.cpp` | _ASSERT | 30, 35, 50, 55, 76, 82 |
| `Core/Src/KThiefSkill.cpp` | _ASSERT | 56, 81, 111, 120, 129, 137, 145, 156, 198, 290, 341 |
| `Core/Src/MyAssert.H` | _ASSERT | 12 |
| `Core/Src/S3PDBConnection.cpp` | assert | 19, 20, 34, 35 |
| `Core/Src/S3PDB_MSSQLServer_Connection.cpp` | assert | 29, 50, 51, 255, 286 |
| `Core/Src/S3P_MSSQLServer_Result.cpp` | assert | 76 |
| `Core/Src/Scene/KIpoTree.cpp` | _ASSERT | 63, 69, 458, 459, 1618 |
| `Core/Src/Scene/KIpotBranch.cpp` | _ASSERT | 92, 234, 240, 378, 401, 416, 543 |
| `Core/Src/Scene/KIpotLeaf.cpp` | _ASSERT | 268, 294 |
| `Core/Src/Scene/KScenePlaceC.cpp` | _ASSERT | 935, 1618, 1815 |
| `Core/Src/Scene/KScenePlaceRegionC.cpp` | _ASSERT | 63, 739, 1404, 1448, 1449 |
| `Core/Src/Scene/Kjxpathfinder.cpp` | _ASSERT | 34, 118, 196, 197, 199, 312, 319, 433, 483, 539, 552, 582 |
| `Core/Src/Scene/Kjxpathfinder.h` | _ASSERT | 151 |
| `Core/Src/Scene/Kpathfinder.cpp` | _ASSERT | 37, 38, 126, 135, 278, 453, 458, 514, 515, 525, 532, 587, 596, 597, 613, 620, 635, 644, 683, 704, 751, 771, 799, 1219, 1232, 1245, 1336, 1337, 1574, 1687, 1690, 1691, 1702, 1709, 1787, 1796, 1819, 1832, 1894, 1959, 1990 |
| `Core/Src/Scene/ScenePlaceMapC.cpp` | _ASSERT | 1137 |
| `Core/Src/Scene/pathfinder/Kjxpathfinder.h` | ASSERT | 148 |
| `Core/Src/cLittleMap.cpp` | ASSERT | 20, 59, 106 |
| `Core/Src/kbufpool.cpp` | _ASSERT | 55 |
| `Core/Src/kbufpool.cpp` | ASSERT | 82 |
| `Core/Src/kgc_dbcallback.h` | ASSERT | 76 |
| `Core/Src/kgc_dbmanager.cpp` | ASSERT | 145, 212, 314, 321, 333, 348, 403, 424, 632, 649, 842, 872 |
| `Core/Src/kgc_mysql_database.cpp` | _ASSERT | 141, 142, 143, 480, 522 |
| `Core/Src/kgc_mysql_database.cpp` | ASSERT | 657, 674, 697, 731 |
| `Core/Src/kregionsearcher.cpp` | _ASSERT | 41, 59, 83, 92, 142, 180, 186, 216, 273, 306 |
| `Engine/Include/luaconf.h` | luai_apicheck | 726 |
| `Engine/Include/luaconf.h` | assert | 726 |
| `Engine/Src/KDebug.h` | KASSERT | 21, 23 |
| `Engine/Src/KFilePath.cpp` | KASSERT | 37, 64 |
| `Engine/Src/KImageRes.cpp` | _ASSERT | 196 |
| `Engine/Src/KLogFile.cpp` | assert | 29, 93, 167, 217 |
| `Engine/Src/KLogFile.cpp` | _ASSERT | 271 |
| `Engine/Src/KLubCmpl_Blocker.h` | assert | 25 |
| `Engine/Src/KNetClient.cpp` | KASSERT | 279, 280, 323, 324 |
| `Engine/Src/KNetServer.cpp` | _ASSERT | 192, 213, 234, 238, 279, 403, 520, 558, 642, 656 |
| `Engine/Src/KNetServerNode.cpp` | KASSERT | 227, 228 |
| `Engine/Src/KNetThread.cpp` | KASSERT | 56, 217, 218 |
| `Engine/Src/KNode.h` | KASSERT | 79, 96, 112, 113 |
| `Engine/Src/KOctree.cpp` | KASSERT | 33, 88 |
| `Engine/Src/KPackFileManager.cpp` | assert | 592, 666, 697, 907, 913, 933, 1109 |
| `Engine/Src/KPakList.cpp` | _ASSERT | 77 |
| `Engine/Src/KWin32.h` | _ASSERT | 53 |
| `Engine/Src/KZipCodec.cpp` | KASSERT | 117, 118 |
| `Engine/Src/S3PDBConnection.cpp` | assert | 19, 20, 34, 35 |
| `Engine/Src/Text.cpp` | _ASSERT | 25, 621, 673, 810, 959, 1274 |
| `Engine/Src/XPackFile.cpp` | _ASSERT | 192, 239, 351, 407 |
| `Engine/Src/ucl/n2_99.ch` | assert | 167, 186, 246, 310, 313, 314, 318, 320, 323, 324, 325, 329, 490, 491, 494, 495, 504, 527, 540, 541, 542, 575, 581, 591, 612, 624 |
| `Engine/Src/ucl/ucl_mchw.ch` | assert | 100, 131, 135, 141, 255, 256, 262, 266, 267, 274, 275, 289, 298 |
| `Engine/Src/ucl/ucl_ptr.c` | assert | 60, 65, 71, 72 |
| `Engine/Src/ucl/ucl_swd.ch` | assert | 210, 284, 298, 420, 426, 432, 450, 464, 495, 504, 515, 535, 572, 573, 583, 611, 617 |
| `Library/LuaLib/src/lapi.c` | LUA_ASSERT | 269, 276, 332, 340, 348, 433, 443 |
| `Library/LuaLib/src/lcode.c` | LUA_INTERNALERROR | 192, 208, 621 |
| `Library/LuaLib/src/lcode.c` | LUA_ASSERT | 283, 401, 408, 625 |
| `Library/LuaLib/src/ldebug.c` | LUA_ASSERT | 100, 106, 113, 126, 312, 315, 320, 327, 372, 375, 393, 401, 453 |
| `Library/LuaLib/src/ldo.c` | LUA_ASSERT | 96, 193 |
| `Library/LuaLib/src/lgc.c` | LUA_ASSERT | 171, 178, 266 |
| `Library/LuaLib/src/lmem.c` | assert | 57 |
| `Library/LuaLib/src/lobject.c` | LUA_ASSERT | 52 |
| `Library/LuaLib/src/lobject.h` | LUA_INTERNALERROR | 18, 21 |
| `Library/LuaLib/src/lobject.h` | assert | 18, 19 |
| `Library/LuaLib/src/lobject.h` | LUA_ASSERT | 19, 22 |
| `Library/LuaLib/src/lparser.c` | LUA_ASSERT | 68, 286, 343, 356, 357, 1120 |
| `Library/LuaLib/src/lstate.c` | LUA_ASSERT | 62, 100, 102, 103, 104, 115, 117, 118 |
| `Library/LuaLib/src/lstring.c` | LUA_ASSERT | 39, 42, 67 |
| `Library/LuaLib/src/ltable.c` | LUA_ASSERT | 63, 156, 215 |
| `Library/LuaLib/src/lvm.c` | LUA_ASSERT | 393, 659, 660, 690 |
| `Library/LuaLib/src/opt.c` | LUA_ASSERT | 24 |
| `Library/LuaLib/src/stubs.c` | LUA_ASSERT | 82, 88, 95 |
| `MultiServer/GameServer/KSOServer.cpp` | _ASSERT | 1738, 1754, 2798, 2799, 2856, 2861, 3113, 3509 |
