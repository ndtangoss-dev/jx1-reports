TÓM TẮT 1/5: Đã sửa 4 lỗi P1, đặt BasicRuntimeChecks=Default; không có /RTC trong 239 lệnh compile x64 đã kiểm.
TÓM TẮT 2/5: LuaLibDll, Engine, Common, CoreServer và GameServer đều build exit 0; cần chỉnh link CRT của Engine trên project snapshot khi bỏ /RTC1.
TÓM TẮT 3/5: gs001.exe 1.286.656 byte; SHA-256 988175a79c24c57b07d24d62b5f43e7acdd135e03e911bf347b123d92ff48a91; bộ EXE/DLL/PDB/map ở checkpoint-a07e-final/a07e.
TÓM TẮT 4/5: CHƯA ĐẠT điều kiện “không còn _RTC_ trong map”: không còn _RTC_CheckStackVars hoặc tham chiếu _RTC_ từ 240 object dự án, nhưng thư viện CRT vẫn mang symbol _RTC_.
TÓM TẮT 5/5: D:\JX-build\a07e bị từ chối quyền ghi; bộ bàn giao sẵn trong workspace, có lệnh copy cho PM. Không chạy EXE/DLL sản phẩm, không stage/commit/push.

# A-07e — bỏ /RTC1 và sửa lỗi mảng/biến chưa gán

Ngày 2026-11-17, Asia/Bangkok. Đã đọc task A-07e và báo cáo A-07d mục 2. Nhánh `fix/a07c-link`, HEAD `3802d29`. Không thấy AGENTS.md trong worktree hoặc thư mục cha đã kiểm. Ban đầu Git chỉ có `?? JX1_OPS/`.

`D:\JX-wt\A-07e` là reparse point tới `D:\JX-wt\A-07c`; Git xác nhận toplevel A-07c. Đường dẫn A-07e truy cập cùng nội dung; helper dùng `Path.resolve()` nên log ghi A-07c. Không tạo nhánh hoặc đổi metadata Git. Đường dẫn source dưới đây tính từ `server/jxOnline/gameserver/Sources/`.

## Thay đổi

| File:dòng hiện tại | Thay đổi |
|---|---|
| `A07b/build-check.py:55` | `BasicRuntimeChecks='EnableFastChecks'` thành `'Default'`. Áp dụng các project snapshot Release/Server Release x64, gồm Common. Giữ `/Od /Zi /MT /GL-`, charset .936, `/we4302 /we4311 /we4312 /we4313`, HighEntropyVA, DynamicBase, `/DEBUG:FULL /INCREMENTAL:NO`. |
| `Core/Src/KPlayer.cpp:1377` | Ghi `iparamr6` vào `nRItemLevel[5]` thay vì `[6]`; giữ mảng 6 phần tử khai báo tại :1362. |
| `Core/Src/KItemList.cpp:4141` | Bỏ riêng `nMagRows[6]=0`; giữ khởi tạo `[0]` đến `[5]`, không tăng kích thước mảng tại :4140. |
| `Core/Src/ScriptFuns.cpp:1068` | Ghi `iparamr6` vào `nRItemLevel[5]` thay vì `[6]`; giữ mảng 6 phần tử tại :1053. |
| `Core/Src/ScriptFuns.cpp:9440` | LuaITEM_DropOneItem trả `nItemIdx` đã gán khi tạo item; bỏ khai báo `nItemIndex` không còn dùng ở dòng cũ :9325. Dòng cũ :9441 dịch thành :9440. |

Sửa C++ theo byte ASCII, giữ encoding, line ending và nội dung tiếng Trung còn lại. Không sửa client, project gốc, logic game khác hoặc checkpoint A-07c.

### Ngoại lệ cấu hình link Engine

`A07b/build-check.py:68–78`: chỉ trong project Engine sao chép, bỏ `MSVCRT.LIB;MSVCPRT.LIB` khỏi AdditionalDependencies và bỏ `LIBCMT.lib` khỏi IgnoreSpecificDefaultLibraries. Giữ thư viện khác và metadata kế thừa. Không dùng `/FORCE` hoặc cho phép multiple definitions.

Project gốc Engine Release x64 (`Engine.vcxproj:400,403`) loại LIBCMT và ép DLL CRT, trong khi helper compile `/MT`. Lần chỉ đổi RTC bị LNK2005 std::_Xlength_error giữa libcpmt và MSVCPRT, rồi LNK1169. Bỏ DLL CRT nhưng còn loại LIBCMT gây 108 unresolved externals. Cho phép CRT static mà `/MT` chọn giải quyết cả hai lỗi. Đây là thay đổi thêm cần thiết để link được: các cờ compile khác giữ nguyên, nhưng lựa chọn thư viện CRT của Engine thay đổi. Chưa kiểm runtime hoặc allocator qua biên DLL.

## Build và xác minh

VS2022 Community v143, MSVC 14.44.35207, SDK 10.0.19041.0, x64. LuaLibDll/Engine/Common/GameServer dùng Release; Core dùng Server Release. Helper tắt post-build deploy trên snapshot như sẵn có; chỉ đọc input legacy từ `D:\JX-build\src18`.

```powershell
python server/jxOnline/gameserver/Sources/A07b/build-check.py --checkpoint=checkpoint-a07e
python server/jxOnline/gameserver/Sources/A07b/build-check.py --checkpoint=checkpoint-a07e-final
python server/jxOnline/gameserver/Sources/A07b/build-check.py --checkpoint=checkpoint-a07e-final --resume --incremental Engine CoreServer GameServer
python server/jxOnline/gameserver/Sources/A07b/checkpoint-a07e-final/logs/verify-a07e.py
git diff --check
```

Hai lệnh đầu là Rebuild vào snapshot mới; giữ lại các lần thất bại, không giao bộ output lỗi. Sau sửa link CRT đầy đủ, lệnh thứ ba compile/link Engine và build lại CoreServer/GameServer trên cùng nguồn đã sửa. Có thêm relink Engine để ghi diagnostic, rồi relink lại với options đúng helper; argument array trong commands.jsonl và Engine-final-link.log exit 0. Không thêm /VERBOSE:LIB vào helper giao PM.

| Project | Exit cuối | Lệnh compile trong tlog | Object kiểm symbol |
|---|---:|---:|---:|
| LuaLibDll | 0 | 30 | 30 |
| Engine | 0 | 90 | 91, gồm testsrc.obj do assembler tạo |
| Common, static lib | 0 | 26 | 26 |
| CoreServer | 0 | 88 | 88 |
| GameServer | 0 | 5 | 5 |

Verifier exit 0: 239 lệnh compile giữ `/Od /Zi /MT`, không có switch `/RTC`; 240 object không có symbol UNDEF chứa `_RTC_`; ba file C++ sửa và MiraclLegacyStdio khớp byte snapshot; bốn binary machine 0x8664, PE32+ 0x20b, giữ HighEntropyVA/DynamicBase. Log CoreServer cuối không có C4789/C4700; còn warning legacy khác như conversion, C4172 và LNK4099 thiếu PDB vendor. Không tuyên bố toàn source hết lỗi. git diff --check thành công.

### Map: tiêu chí literal chưa đạt

**Không thể xác nhận map hoàn toàn không có `_RTC_` với bộ build này.** Verifier ghi `literal_no_rtc_in_all_maps=false`; exit 0 xác nhận các kiểm tra kỹ thuật nêu trên, không có nghĩa tiêu chí literal đã đạt.

| Map | Dòng chứa `_rtc_`, không phân biệt hoa thường | Còn lại |
|---|---:|---|
| GameServer.map | 8 | _RTC_Initialize, _RTC_Terminate, unwind và bốn marker __rtc_*, đều từ LIBCMT:initsect.obj. Không có _RTC_UninitUse, _RTC_StackFailure hoặc _RTC_CheckStackVars. |
| CoreServer.map | 8 | Như GameServer. |
| LuaLibDll.map | 8 | Như GameServer. |
| Engine.map | 32 | Startup như trên; thêm handler _RTC_UninitUse, _RTC_StackFailure, _RTC_AllocaFailure, API/data/unwind từ LIBCMT:error.obj, userapi.obj, pdblkup.obj. Không có _RTC_CheckStackVars. |

Đã đối chiếu CRT cài tại `MSVC/14.44.35207/crt/src/vcruntime/exe_common.inl:162–165` và `dll_dllmain.cpp:50–52,184–186`: source startup có gọi initialize/terminate dưới guard `_RTC`. Startup binary lấy từ thư viện toolchain; đổi cờ compile game không rebuild CRT này.

`dumpbin /linkermember:1 libcmt.lib` cho thấy `_RTC_UninitUse`, `sprintf_s`, `_vsprintf_s_l` và `__local_stdio_printf_options` cùng member offset `4F0C4A` (error.obj). Điều này giải thích khả năng handler được giữ khi member CRT được kéo vào, chưa chứng minh đường game gọi handler. Bằng chứng trực tiếp về bỏ instrumentation: không có /RTC trên lệnh compile và không có tham chiếu UNDEF _RTC_ từ object dự án. Không vá CRT, thêm stub hoặc đổi tối ưu linker chỉ để xóa tên khỏi map.

## Artifact và SHA-256

| File | Byte | SHA-256 |
|---|---:|---|
| gs001.exe | 1.286.656 | `988175a79c24c57b07d24d62b5f43e7acdd135e03e911bf347b123d92ff48a91` |
| CoreServer.dll | 3.231.744 | `d508a609f29f870b42f72a0adc300595422589e68797d9243e2f991c60a7a26e` |
| Engine.dll | 1.878.016 | `639e64c0b3fc5ed5e7901e703d386244b56257423b2d0ea7c1c5be49c2b15cba` |
| LuaLibDll.dll | 790.528 | `ed8012a037ec3ff2c804792779f9e75d0e0424b8d753f19d863a489de45134b7` |

Bộ 15 file: bốn binary, bốn PDB tương ứng, bốn map, build-results.json, verification.json và SHA256SUMS.txt. Hash bản copy đã đối chiếu output. Vị trí qua workspace hiện tại:

```text
D:\JX-wt\A-07e\server\jxOnline\gameserver\Sources\A07b\checkpoint-a07e-final\a07e\
```

Đường dẫn vật lý là A-07c thay cho A-07e. Tạo `D:\JX-build\a07e` bằng New-Item nhận `UnauthorizedAccessException: Access to the path 'a07e' is denied`. **Chưa có bộ artifact tại D:\JX-build\a07e**; phiên chỉ được ghi workspace và không được yêu cầu nâng quyền. PM có thể copy bộ đã chuẩn bị trong phiên có quyền ghi đích:

```powershell
$jxA07ePack = 'D:\JX-wt\A-07e\server\jxOnline\gameserver\Sources\A07b\checkpoint-a07e-final\a07e'
New-Item -ItemType Directory -Path 'D:\JX-build\a07e' -Force -ErrorAction Stop
Get-ChildItem -LiteralPath $jxA07ePack -File | Copy-Item -Destination 'D:\JX-build\a07e' -ErrorAction Stop
Get-FileHash 'D:\JX-build\a07e\gs001.exe' -Algorithm SHA256
```

Bằng chứng trong checkpoint-a07e-final: source-sha256.json; snapshot project/source; logs/results.json, commands.jsonl; CL/link tlog dưới obj; log build/diagnostic/final-link; logs/a07e-verification.json, verify-a07e.py; import table bốn binary; logs/libcmt-linkermember.txt; out/ chứa artifact gốc. Lần lỗi trước sửa CRT giữ tại logs/attempt-before-crt-fix/ và checkpoint-a07e. Checkpoint đều ignored theo .gitignore sẵn có.

## Bàn giao PM

Đã sửa source, bỏ cờ RTC khi compile, build và gom artifact trong workspace. Hai điều kiện chưa đạt nguyên văn: chép đến thư mục ngoài workspace và map không còn bất kỳ _RTC_. Không chạy/load sản phẩm; chưa xác nhận lỗi dừng ~225 giây, VM/SQL, gameplay hoặc runtime/allocator sau chỉnh link Engine. Không sửa task, không stage/commit/push. PM review bốn file source/helper thay đổi và báo cáo này; không gom toàn bộ JX1_OPS untracked hoặc checkpoint vào commit.
## Thu trong VM thu (PM, 04:13)
- Bo A-07e (exe HEVA tat SHA 91BC8EB67058 = 988175A7... da editbin; CoreServer D508A609F29F, Engine 639E64C0B3FC, LuaLibDll ED8012A037EC) trong JX-Test-36 tu 04:02:49: SONG QUA MOC ~225 s (bo A-07c cu chet o moc nay 3/3 lan), >610 s, nghe 51189, bo nho rieng 6,3 GB. Ket luan so bo: nguyen nhan 0x80000003 la /RTC1 (hoac cac loi mang P1), da het khi bo.
- CHUA thu: bat HEVA (cho dung khong can co); chua co nguoi/bot vao; chua chay du lau. Con theo doi.
