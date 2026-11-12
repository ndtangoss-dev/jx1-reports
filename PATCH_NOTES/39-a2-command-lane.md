# 39 - A2 command lane (Phase 1)

**TÓM TẮT 5 DÒNG**
1. A2 đã cài vào BẢN COPY `D:\JX-build\src18` (nguồn gốc không đổi), build xong x64, **chưa chạy EXE nào**.
2. Hai làn (move / act): move không đè skill đang chờ; skill thay act và xóa move; stop mềm không hủy skill chờ.
3. TTL tính bằng ms (skill 250, move 120), lệnh ctl không hết hạn; mỗi làn tối đa 1 mục (không hàng đợi dài).
4. Giao thức, tốc độ, damage, thời gian chiêu giữ nguyên; NPC/quái dùng khe lệnh gốc.
5. Có bộ đếm debug mỗi 60 s (console + `CmdLane_stat.log`), cấu hình `Settings\CmdLane.ini`, tắt bằng Enable=0.

Cần tôi quyết định: không

## Kiểm tra client (bước 1 của brief)
- `KHRocker.cpp:457-486` `onTouchEnded`: dòng gửi stop/run bị comment -> client KHÔNG gửi stop khi thả cần. Sit gửi nơi khác (CoreShell.cpp:4572-4589). Server nhận stop qua `NpcSitCommand` (KProtocolProcess.cpp:6041-6056).
- Lua không gọi RunTo/DoSkill/SendSerCommand trực tiếp; AI/quái gọi `Do*` trực tiếp, không qua khe lệnh (xem báo cáo 37).

## Thiết kế (mọi thứ trong `#ifdef _SERVER`, nhãn `[A2-CMDLANE]`)
- `NPC_CMD_LANE {bValid, CmdKind, X, Y, Z, tArrive}` (GetTickCount64) ở KNpc.h; `m_CmdMove`, `m_CmdAct`.
- `ProcCommand` cũ đổi tên `ProcCommandLegacy`; `ProcCommand` mới điều phối, người chơi -> `CmdLaneProc`.
- `SendSerCommand` -> `CmdLaneReceive` (chỉ người chơi). `SendSerCommandSoftStop()` chỉ dùng ở nhánh stand của `NpcSitCommand`; `do_stand` hệ thống vẫn cứng.
- Khi `m_ProcessAI==0` (đang diễn chiêu): move bỏ, skill bỏ trừ khi `BufferBusy=1` (tùy chọn B, mặc định 0); hurt/revive vẫn chạy.
- Sau khi thực thi skill, move chờ chỉ chạy nếu skill bị từ chối.
- Bộ đếm: recv, superseded, overwritten, cleared, absorbed, expired, busy discards, executed, wait ms avg/max + histogram skill.

## File
Diff: `docs-analysis/patches/a2-cmdlane/a2-cmdlane.diff` (4 file: KNpc.h, KNpc.cpp, KProtocolProcess.cpp, CoreServerShell.cpp). Mẫu cấu hình: `CmdLane.ini.sample`. Bản gốc lưu `D:\JX-build\backup-a2`.

## Build (đã chạy được)
MSBuild từng project, `/p:Configuration=<cfg>;Platform=x64;PlatformToolset=v143;WindowsTargetPlatformVersion=10.0.19041.0`: Engine Release, LuaLibDll Release, Common Release, Core "Server Release", GameServer Release. Không build qua .sln (ánh xạ hỏng). Props: `/source-charset:.936 /execution-charset:.936 /Zc:sizedDealloc- /Zc:strictStrings- /wd4996`; shim `iob_shim.obj`. Output `D:\JX-build\_bin_v2_\gs\`.

## Trạng thái
- Đã build: có. Đã chạy: **không**. Đã kiểm chứng hành vi thật: **không** (chỉ mô phỏng Python, báo cáo 38 - không phải kết quả server thật).
- Chưa chạy được ở 18 Hz "server cũ" để so sánh; cần VM thử (xem báo cáo 42).
