# 45 - Fix36: giật bản đồ (client) và nhánh server 36Hz

TÓM TẮT 5 DÒNG
1. Giật bản đồ: nguyên nhân là `removeUnusedTextures()` chạy MỖI GIÂY trong `KgameWorldVN::custom_update` (có từ bản gốc). Sửa: chỉ dọn khi cache texture > 384 MB, kiểm tra mỗi 10 s. LDPlayer: khung > 40 ms 197 -> 12, khung >= 100 ms 15 -> 1.
2. APK Fix36: `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-fix36.apk` (SHA256 9ABDF095…1F66), chỉ khác Fix35 ở `libMyGame.so`, ký cùng khóa.
3. Server tự dựng (exe + DLL, có A2) nay tương thích client 2912: vào game, HUD đúng, đi lại, đánh quái mất máu, lên cấp (QA trên LDPlayer).
4. 36Hz: `LogicFps=36` chạy thật 36/36 nhịp/s, mỗi nhịp ~0,6-0,8 ms; nhịp lẻ chỉ đi nửa bước + đồng bộ vị trí, nhịp chẵn chạy đủ logic 18Hz. Tốc độ chạy đo được 6 ô/10 s (36Hz) so với 7 ô/10 s (18Hz gốc) - cùng cỡ, chưa đủ chính xác để khẳng định bằng nhau.
5. VM thử đang chạy server GỐC 18Hz (an toàn cho người dùng). Bản 36Hz nằm ở `C:\JX\Bisect\T4`, chưa đưa cho người dùng.

Cần tôi quyết định: có (có muốn thử bản server 36Hz trên điện thoại không; mặc định vẫn chạy bản gốc).

## 1. Client
| File (D:\Android\b\Client\Classes) | Thay đổi |
|---|---|
| `vn/gamescence/KgameWorldVN.cpp` | Dọn texture theo ngưỡng (thẻ `[fix36]`); log `JXPERF` đo khung (chỉ in khi khung > 40 ms và tóm tắt 5 s) |
| `gamescene/KScenePlaceC.cpp` | Log đo Preprocess/chờ nạp/đổi vùng (`[fix36]`) |
| `gamecore/JxPerf.h` | Mới: tiện ích đo |
Giữ nguyên Fix31/33/34/35. Sao lưu: `D:\Android\b\backup-fix36\`. Thư viện chưa strip: `D:\Android\b\apk-fix36\libMyGame-fix36-unstripped.so`.

Bằng chứng: 106/106 khung giật lớn rơi đúng một mốc ms trong mỗi giây, phần tốn là `Paint` (84-120 ms) ngay sau lệnh dọn texture. Giả thuyết minimap/camera bị loại: các khung đổi vùng không trùng khung giật.

## 2. Server (D:\JX-build\src18, bản sao; nhị phân: D:\JX-build\fix36-bin)
| Sửa | Lý do |
|---|---|
| 7 struct gói client về bố cục client 2912 (`CURPLAYER_NORMAL_SYNC`, `NPC_NORMAL_SYNC`, `PLAYER_LEVEL_UP_SYNC`, `REBORN/ROLEVIP_VALUE_SYNC`, `DATAU_BOX`, `LADDER_LIST`) | int64 vs int, thiếu/thừa trường -> HUD 0/0 |
| `OperationRequest/GetGameData/OperationRequestInfo` tham số `uintptr_t` | exe cắt con trỏ IServer (`(unsigned int)pCloneServer`) -> crash khi đăng nhập |
| `s2c_querymapinfo` gói ngắn -> đăng ký bản đồ | phòng thủ |
| `KSortScript.cpp` `intptr_t` (Fix35), `KPlayer.cpp:7606` (Fix35) | crash x64 |
| `LogicFps` (gs001_cfg.ini [GameServer], 18/36) + nửa bước (`KNpc::JxHalfMove`, `KRegion/KSubWorld::JxHalfActivate`, `KSubWorldSet::JxHalfLoop`) + đẩy gói mỗi vòng khi 36 | 36Hz giữ đơn vị thời gian 18Hz |
Struct gateway (gs <-> Bishop/Goddess) GIỮ bố cục server: Bishop/Goddess gốc dùng định dạng mới (thử đổi theo client -> "Máy chủ chưa hoạt động").

Kích thước 351 struct chung đã so bằng probe (client NDK arm64 trên LDPlayer, server MSVC x64): gói server->client cố định khớp hết; còn khác `OBJ_ADD_SYNC` (độ dài thay đổi, có m_wLength) và `PLAYER_REQ_COMMAND` (unsigned long, giống server gốc).

## 3. Kết quả kiểm thử
| Hạng mục | 18Hz gốc + Fix36 | T4 tự dựng 18Hz | T4 tự dựng 36Hz |
|---|---|---|---|
| Vào game, HUD | Đạt | Đạt (204/204) | Đạt |
| Đi lại | Đạt | Đạt | Đạt |
| Đánh quái mất máu | Đạt (quái chết, lên cấp) | Chưa đánh được (QA chưa tới tầm) | Đạt (máu giảm, lên cấp) |
| Tốc độ chạy (phải/trái 10 s) | 7/7 ô | - | 6/6 ô |
| SvrFPS / tick | - | 18/18, ~0,8 ms | 36/36, ~0,6-0,8 ms |
| Crash | Không | Không | Không |
Chưa thử: kỹ năng tầm xa/AOE/liên hoàn (nhân vật thử cấp 1-2, chưa lấy được lệnh bài GM), cưỡi ngựa, nhiều người chơi.

## 4. Rủi ro còn lại (36Hz)
- Đạn (missile), trạng thái, AI vẫn chạy 18 lần/s (đúng thiết kế); chỉ di chuyển và đồng bộ vị trí dày hơn.
- Khi NPC dừng giữa hai nhịp có thể đi lố nửa bước (<= 15 đơn vị).
- Còn ~270 chỗ ép con trỏ 32 bit trong CoreServer (phần lớn mã client) chưa rà; tính năng bang hội/giao dịch trên bản tự dựng chưa thử.
- Dữ liệu nhân vật do bản tự dựng ghi: chỉ thử trên DB VM thử.

## 5. Khôi phục
- Client: cài lại Fix35/Fix34 từ CDN; mã: chép `D:\Android\b\backup-fix36\` đè lại.
- Server: VM thử đang chạy bản gốc (tác vụ `JX-gs001`). Bản 36Hz: tác vụ `JX-dbg-T4c` (thư mục `C:\JX\Bisect\T4`, `gs001_cfg.ini.bak-18` để về 18).
- Forwarder/CDN đang cho phép thêm <TAILSCALE-IP> (chính máy thật, cho LDPlayer); bản cũ `*.bak-fix36` trong `docs-analysis/scripts`.
