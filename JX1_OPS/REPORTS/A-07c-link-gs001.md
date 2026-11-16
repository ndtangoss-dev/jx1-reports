TÓM TẮT 1/5: Đúng worktree D:\JX-wt\A-07c, nhánh fix/a07c-link, HEAD 8fde733 kế thừa A-07b; không stage/commit/push.
TÓM TẮT 2/5: Thêm shim stdio riêng cho VC100 x64 ms64.lib và 3 dòng khai báo compile trong project; không sửa logic game.
TÓM TẮT 3/5: Build sạch v143 x64: LuaLibDll, Engine, Common, CoreServer, GameServer đều exit 0; 0 lỗi compile/link.
TÓM TẮT 4/5: gs001.exe mới 1.346.560 byte; SHA-256 0c14250622f79ee2db90653ce769afb3f48d5005641662cc880f451f6dbfbe5c.
TÓM TẮT 5/5: Chưa kiểm runtime/VM/SQL/HighEntropyVA khi vận hành; chưa chạy binary sản phẩm, chưa deploy hay đè bản đang chạy.

# A-07c — link gs001 x64

## Thay đổi

Đã đọc JX1_OPS/TASKS/A-07c.md và D:\JX-wt\A-07b\A-07b-ep-con-tro.md. Không tìm thấy AGENTS.md trong worktree và các thư mục cha đã kiểm. Trước khi sửa chỉ có thư mục ops untracked.

Hai file sản phẩm dưới server/jxOnline/gameserver/Sources/MultiServer/GameServer/:

- MiraclLegacyStdio.cpp: cung cấp con trỏ hàm C __imp___iob_func, chỉ với _WIN64 và _MSC_VER >= 1900. Trả địa chỉ stdout thật của CRT hiện tại trừ 0x30 bằng uintptr_t.
- GameServer.vcxproj: thêm translation unit với PrecompiledHeader=NotUsing (3 dòng). Giữ nguyên cấu hình/link options project gốc; helper A-07b override toolset/output/options trên bản sao.

legacy_stdio_definitions.lib đã có trong helper A-07b nên chỉ thêm thư viện đó không chữa được symbol thiếu. Không sao chép FILE: layout VC100 và UCRT khác nhau; buffer/lock cần thuộc stream CRT thật.

## Cơ sở tương thích và giới hạn

ms64.lib SHA-256: 1a43e921941024edd0fe2cac4b2985dadcb65f2bbb49fa4f8b45aee871512514.

Đọc disassembly binary thăm dò, rồi kiểm lại binary cuối: 97/97 lời gọi qua __imp___iob_func đưa result + 0x30 vào rdx rồi gọi __imp_fputc (96 call thường, 1 tail jump sau epilogue). Không có tham chiếu gián tiếp khác đến symbol trong disassembly cuối. 0x30 là stride FILE x64 VC100 được mã hóa cho stdout. Bias địa chỉ giúp fputc nhận đúng stdout UCRT, không nhận FILE giả hoặc FILE từ CRT khác.

Map xác nhận symbol do MiraclLegacyStdio.obj cung cấp, fputc từ libucrt:fputc.obj. Import table không có MSVCR100.dll hoặc import __iob_func. Đối chiếu nguồn SDK ucrt/stdio/_file.cpp: __acrt_iob_func trả stream thật; shim dùng macro stdout của CRT đang compile.

Đây là adapter cho đúng mẫu sử dụng của thư viện/binary đã audit, không phải implementation tổng quát của mảng FILE legacy. Nếu đổi thư viện, toolchain, routine kéo vào link hoặc mẫu gọi, cần audit lại. Không áp dụng cho consumer dùng stdin/stderr hoặc truy cập field FILE legacy. Kiểm tra tĩnh hỗ trợ tính tương thích đường gọi này; chưa chứng minh tương đương runtime. Không sửa giao thức, allocator hoặc logic game.

## Build và bằng chứng

Lệnh build sạch đã chạy từ gốc worktree:

~~~powershell
python server/jxOnline/gameserver/Sources/A07b/build-check.py --checkpoint=checkpoint-a07c-final
~~~

Helper A-07b không thay đổi. Copy source/header/resource và đọc legacy lib/ADO/icon từ D:\JX-build\src18. Output/obj/log ở snapshot riêng. Dùng v143, SDK 10.0.19041.0, Release/Server Release, /Od /Zi /RTC1 /MT /GL-, charset .936, /we4302 /we4311 /we4312 /we4313, /DEBUG:FULL /INCREMENTAL:NO. Không dùng /FORCE để bỏ qua lỗi trong build kiểm tra. Post-build copy/deploy tắt trên bản sao như A-07b.

Lệnh MSBuild đầy đủ của cả 5 project lưu dạng argument array tại Sources/A07b/checkpoint-a07c-final/logs/commands.jsonl. GameServer dùng /t:Rebuild /m:1 /nologo /v:minimal /p:Configuration=Release /p:Platform=x64 /p:PlatformToolset=v143 /p:WindowsTargetPlatformVersion=10.0.19041.0 /p:BuildProjectReferences=false /p:TargetName=gs001; OutDir/IntDir trỏ vào snapshot cuối.

| Thành phần | Kết quả |
|---|---|
| LuaLibDll, Engine, Common | exit 0 |
| CoreServer | exit 0 |
| GameServer / gs001 | exit 0; 0 lỗi compile/link; không LNK2001/LNK1120 |

Vẫn có warning legacy, ví dụ numeric conversion, C4172 và LNK4099 thiếu PDB vendor; không tuyên bố hết warning.

Artifact cuối:

~~~text
D:\JX-wt\A-07c\server\jxOnline\gameserver\Sources\A07b\checkpoint-a07c-final\out\gs001.exe
~~~

- Kích thước: 1.346.560 byte.
- SHA-256: 0c14250622f79ee2db90653ce769afb3f48d5005641662cc880f451f6dbfbe5c.
- PE machine 0x8664 (x64), optional-header magic 0x020b (PE32+).
- DllCharacteristics 0x8060: có HighEntropyVA 0x20 và DynamicBase 0x40.

Bằng chứng dưới Sources/A07b/checkpoint-a07c-final/, ignored theo .gitignore sẵn có:

- logs/results.json, logs/commands.jsonl, log thường và diagnostic của 5 project.
- source-sha256.json: manifest trước khi helper rewrite project.
- out/GameServer.map, out/gs001-headers.txt, out/gs001-imports.txt, out/gs001-disasm.txt.
- logs/a07c-verification.json, logs/a07c-iob-call-sites.json: hash/PE và 97 mẫu gọi.
- logs/verify-a07c.py: chỉ đọc binary/map/log để tái tạo bằng chứng; đã chạy exit 0. Shim source khớp byte với snapshot đã build.

~~~powershell
python server/jxOnline/gameserver/Sources/A07b/checkpoint-a07c-final/logs/verify-a07c.py
Get-FileHash server/jxOnline/gameserver/Sources/A07b/checkpoint-a07c-final/out/gs001.exe -Algorithm SHA256
git diff --check
~~~

Snapshot checkpoint-a07c trước đó dùng tái hiện lỗi và link thăm dò import CRT để đọc mã máy; không dùng artifact thăm dò để bàn giao. Build sạch cuối không có thư viện/import thăm dò. Giữ nguyên checkpoint; không đưa vào commit.

## Chưa kiểm và bàn giao PM

Chưa chạy gs001 hoặc DLL sản phẩm; không kết nối VM/SQL/server. Chưa kiểm stdout runtime, đường lỗi MIRACL, crypto/round-trip, crash HighEntropyVA hoặc tương thích triển khai. Chưa build Win32, VS100 hoặc Debug gốc. DLL cùng snapshot đã rebuild; cần môi trường được phép chạy để xác nhận runtime.

Không sửa task ops. Không stage/commit/push. PM review/stage đúng hai file sản phẩm và báo cáo này; thư mục ops đã untracked từ đầu, không gom toàn bộ nó. git diff --check thành công.

## Thử trong VM thử (PM, 2026-11-17 03:05, JX-Test-36)
- gs001 build A-07c, HighEntropyVA BẬT (SHA-256 0C142506...FBE5C): crash 0xC0000005 sau ~40 giây. => A-07b chưa đủ, còn chỗ cắt con trỏ.
- Cùng bản, HighEntropyVA TẮT (SHA-256 D2EABEDC...BE24D): chạy, cổng 51189 nghe, không crash trong lúc theo dõi (vài phút; chưa đo dài hạn).
- Kết luận: bản dựng từ nguồn dùng được khi tắt cờ (build tái lập được); lỗi nằm ở logic con trỏ, cần A-07d (tìm bằng dump/gỡ lỗi). Bản đang chạy trong VM thử: bản tắt cờ A-07c.
