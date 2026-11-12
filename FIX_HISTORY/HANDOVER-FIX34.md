# BÀN GIAO: tối ưu client JX1 đến fix34

Ngày: 2026-11-11. Tài liệu chỉ ghi trạng thái; bước này không sửa code. Chưa commit Git.

## TÓM TẮT 5 DÒNG
1. Client đã qua 4 đợt: fix31 (nội suy + xử lý gói mỗi khung + giới hạn joystick), fix33 (hết mất sát thương khi vừa chạy vừa đánh), fix34 (nội suy đạn + giảm trễ nhận gói). Người dùng đã xác nhận fix33 trên điện thoại; **fix34 chưa có xác nhận đầy đủ**.
2. Mọi thay đổi nằm ở bản copy build `D:\Android\b\Client\Classes` (12 file), repo `Folder/` không đổi. Server, giao thức, logic 18 Hz không đổi.
3. **Lỗi mới người dùng báo (chưa điều tra):** giật hình khi cưỡi ngựa di chuyển xa lúc bật minimap. Giả thuyết chính: camera nội suy gọi `SetFocusPosition` mỗi khung kéo theo cập nhật minimap mỗi khung (mục 6).
4. Nhánh server 18/36 Hz đang dừng ở bước cài trình biên dịch C++ trên máy thật (script đã sửa, chờ chủ máy chạy lại bằng Admin).
5. Muốn làm tiếp: luôn sao lưu trạng thái hiện tại trước khi vá, vá theo byte (nguồn GBK), build với `ANDROID_USER_HOME=D:\Android\user`, chạy lại 3 bộ kiểm thử mô phỏng.

**Cần tôi quyết định: có** (ưu tiên điều tra lỗi giật khi cưỡi ngựa hay nhánh server).

## 1. Lịch sử fix31 → fix34
| Đợt | Báo cáo | Nội dung | Kiểm chứng |
|---|---|---|---|
| Phân tích | `30-phan-tich-nhip-xu-ly-jx1.md` | Lõi 18 Hz cố định (server đo 18,000 nhịp/giây); render 60 FPS nhưng không nội suy; server đẩy gói 9 lần/giây; client xử lý gói 10 lần/giây; joystick gửi lệnh mỗi khung | Đo console `gs001`, đọc mã |
| fix31 | `31-toi-uu-nhip-xu-ly-client.md` | Nội suy vị trí vẽ nhân vật/NPC/quái + camera; xả gói nhận mỗi khung; joystick 9-18 lần/giây, gửi nốt đích khi thả | Build OK; 15/15 mô phỏng; người dùng thấy mượt hơn |
| Đối chiếu | `32-doi-chieu-hieu-ung-ky-nang-apk-tick.md` | Giải thích hiệu ứng "mới": server một ô lệnh, lệnh chạy đè lệnh kỹ năng | Đọc mã |
| fix33 | `33-fix-skill-damage-and-smoothness.md` | `TCP_NODELAY`; hoãn lệnh di chuyển 3 nhịp sau kỹ năng và khi đang ra chiêu (1 ô, lệnh mới nhất); lệnh chạy cục bộ không đè lệnh kỹ năng chờ; nội suy đi tiếp từ vị trí đang vẽ; log `JXFIX` | Build OK; 9/9 mô phỏng; **người dùng xác nhận hết mất sát thương** |
| fix34 | `34-toi-uu-toan-dien-do-muot.md` | Nội suy vị trí vẽ đạn đang bay; luồng nhận dò socket 2 ms thay 10 ms; đánh giá 36 Hz (chưa làm) | Build OK; 7/7 + 9/9 mô phỏng; chưa có xác nhận đầy đủ trên máy |

## 2. Thay đổi đã hoàn thành (tính năng)
- Nội suy hiển thị giữa 2 nhịp logic: `g_fNpcRenderAlpha` tính trong `KgameWorldVN::draw`; cờ `g_bNpcRenderInterp` chỉ bật quanh `g_ScenePlace.Paint()`/`PaintMap()`; `KNpc::GetMpsPos` trả vị trí nội suy trong pha vẽ; `KNpc::Paint` → `SetRenderPos`; camera `g_ScenePlace.SetFocusPosition` mỗi khung theo vị trí nội suy của nhân vật; `g_bNpcInterpCameraOwned` chặn `KNpcRes::SetPos` ép camera về logic.
- "Nhảy" (không nội suy): lệch > 96 đơn vị, đổi bản đồ, khe nhịp, NPC không `Activate` nhịp hiện tại, server sửa vị trí giữa nhịp (vẽ vị trí authoritative).
- Đạn: `KMissle::Paint` tự phát hiện vị trí logic đổi và nội suy khi `MS_DoFly`.
- Gói nhận: xả trong `KgameWorldVN::update` mỗi khung (tối đa 64 lô); `custom_update` 0,1 s chỉ còn phần giao diện.
- Joystick: `KPlayer::Walk` gửi khi đổi hướng (≥ 1 nhịp) hoặc mỗi 2 nhịp; `KPlayer::Active` gửi nốt đích chờ khi joystick ngừng ≥ 1 nhịp trọn; `KCoreShell::Goto` không còn reset bộ đếm.
- Lệnh kỹ năng: `SendClientCmdSkill` bật khóa 3 nhịp, hủy lệnh di chuyển chờ; `SendClientCmdRun/Walk` hoãn khi khóa; `MoveGuardTick` gửi lệnh đã hoãn; `KNpc::SendSerCommand` bảo vệ `do_skill` chờ của nhân vật mình.
- Mạng: `TCP_NODELAY`; vòng nhận `usleep(2000)`.
- Log trên máy: `adb logcat -s JXFIX` (số kỹ năng gửi, lệnh di chuyển hoãn/gửi/bị thay).

## 3. File source đã sửa (`D:\Android\b\Client\Classes\…`)
| File | Đợt | Thẻ chú thích |
|---|---|---|
| `gamecore/KNpc.h` | 31, 33 | `[tick-smooth]`, `[fix33]` |
| `gamecore/KNpc.cpp` | 31, 33 | `[tick-smooth]`, `[fix33]` |
| `gamecore/KNpcRes.h` | 31 | `[tick-smooth]` |
| `gamecore/KNpcRes.cpp` | 31 | `[tick-smooth]` |
| `gamecore/KPlayer.cpp` | 31, 33 | `[tick-smooth]`, `[tick-smooth2]`, `[fix33]` |
| `gamecore/CoreShell.cpp` | 31 | `[tick-smooth]` |
| `vn/gamescence/KgameWorldVN.cpp` | 31 | `[tick-smooth]` |
| `gamecore/KProtocol.cpp` | 33 | `[fix33]` |
| `network/SocketClient.cpp` | 33, 34 | `[fix33]`, `[fix34]` |
| `gamecore/KMissle.h` | 34 | `[fix34]` |
| `gamecore/KMissle.cpp` | 34 | `[fix34]` |

Diff từng đợt: `docs-analysis/patches/31-client-tick-smooth.diff`, `33-client-skill-guard.diff`, `34-client-missile-interp.diff`.

## 4. APK và source đang dùng
| Bản | Đường dẫn | SHA256 | Link CDN |
|---|---|---|---|
| Gốc | `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` | `82674B16…` | (không đặt trong `/apk/`) |
| fix31 | `D:\Android\b\apk-tick\jx-tailscale-8080-tick.apk` | `DAB8485E…8338` | `/apk/jx-tailscale-8080-tick.apk` |
| fix33 | `D:\Android\b\apk-fix33\jx-tailscale-8080-fix33.apk` | `E9FB0DBF…9CC4` | `/apk/jx-tailscale-8080-fix33.apk` |
| **fix34 (mới nhất)** | `D:\Android\b\apk-fix34\jx-tailscale-8080-fix34.apk` | `3164DBD11686495C06EE69BDD39BEEFF42EC19ED359CCB9176AE83F9AE533595` | `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-fix34.apk` |

- Tất cả: `com.jxclient.hoiuctruyenky` versionCode 17, `arm64-v8a`, chữ ký debug `a48601f7…f2d7` → cài đè lẫn nhau được. Chỉ khác `lib/arm64-v8a/libMyGame.so`.
- Source đang ở trạng thái **fix34**: `D:\Android\b\Client\Classes`.
- Sao lưu: `D:\Android\b\backup-tick\` (gốc 7 file), `backup-fix33\` (trước 33), `backup-fix34\` (trước 34).
- Khôi phục: `docs-analysis/scripts/khoi_phuc_client_fix34.ps1` (về fix33; `-Ve31`; `-VeGoc`), `khoi_phuc_client_fix33.ps1`, `khoi_phuc_client_tick.ps1`.
- CDN: `cdn_server.py` PID 4612, `<TAILSCALE-IP>:8080`, chỉ cho `<TAILSCALE-IP>`; file APK ở `C:\Jx1CocoV3\data_cdn\apk\` (git bỏ qua).
- Server: VM `JX-Server-D` (UUID `be011bd7-…`) đang chạy đủ 6 thành phần, 18 Hz, không bị sửa. Lưu ý vận hành: không nối TCP vào 51189 khi `gs001` đang nạp (báo cáo 29).
- Khóa debug tạo nhầm `C:\Users\<user>\.android\debug.keystore` vẫn còn (chủ máy bảo giữ).
- Trang riêng tư vô tình đăng: <link-artifact-rieng-tu> (báo cáo 32), chưa xóa.

## 5. Lỗi đã khắc phục
| Lỗi | Nguyên nhân | Sửa ở |
|---|---|---|
| Chuyển động giật 18 lần/giây | Không nội suy | fix31 |
| Trễ nhận tới 100 ms | Xả gói mỗi 0,1 s | fix31 |
| Joystick gửi 60-120 gói/giây | Giới hạn bị comment, `Goto` reset bộ đếm | fix31 |
| Vừa chạy vừa đánh: có hoạt ảnh, không sát thương | Server một ô lệnh + Nagle gộp gói kỹ năng với gói chạy sau | fix33 (đã xác nhận) |
| Hình giật lùi khi server sửa vị trí giữa nhịp | Nhịp sau nội suy từ mốc cũ | fix33 |
| Đạn giật so với thân | Đạn không nội suy | fix34 |
| APK ký sai khóa | Thiếu `ANDROID_USER_HOME` | Quy trình build |
| `gs001` crash `0xC0000005` khi nạp | Kết nối vào 51189 lúc chưa tạo `m_pCoreServerShell` | Quy trình vận hành (báo cáo 29) |

## 6. LỖI MỚI: giật hình khi cưỡi ngựa di chuyển xa lúc bật minimap
**Trạng thái:** người dùng vừa báo; **chưa tái hiện, chưa đo, chưa sửa**. Chưa biết: xảy ra ở APK nào (fix31/33/34 hay cả bản gốc), tắt minimap có hết không, đi bộ có bị không, giật theo chu kỳ hay khi qua ranh giới vùng.

**Giả thuyết cần kiểm tra (xếp theo khả năng, đều chưa có bằng chứng):**
1. **Camera nội suy gọi `SetFocusPosition` mỗi khung** (`KgameWorldVN::draw`, đoạn `[tick-smooth]`). Trong `KScenePlaceC::SetFocusPosition` (`gamescene/KScenePlaceC.cpp:891-1006`) luôn gọi `SubWorld[0].LookAt` và `m_Map.SetFocusPosition(...)` (minimap, dòng 926/972). Trước fix31 chỉ 18 lần/giây, nay 60-120 lần/giây → nếu cập nhật minimap nặng thì gây tụt khung khi minimap bật. Cưỡi ngựa nhanh hơn nên đổi vùng thường hơn.
2. **Đổi vùng (region) của camera**: khi qua ranh giới, `SetFocusPosition` chạy `ClearPreprocess`, `ChangeLoadArea`, `ChangeProcessArea` (`:979-1005`). Vị trí nội suy "đi tiếp từ vị trí đang vẽ" (fix33) có thể làm camera qua ranh giới lệch nhịp với logic; cờ `g_bNpcInterpCameraOwned` có thể bị tắt/bật quanh lúc đó làm camera nhảy logic ↔ nội suy.
3. **Ngưỡng "nhảy" 96 đơn vị**: tốc độ cưỡi ngựa cộng buff có thể làm bước mỗi nhịp lớn (trần 31 đơn vị/nhịp trong `ServeMove`), không vượt 96; nhưng sửa vị trí từ server khi chạy nhanh với ping cao có thể vượt → camera/nhân vật "nhảy". Cần log số lần `UpdateRenderPos` trả TRUE.
4. **Minimap vẽ theo vị trí khác camera**: `PaintMap` nằm trong cửa sổ nội suy, nhưng `setUiplayerPos` (trong `KNpcRes::SetPos`) vẫn theo logic 18 Hz → chấm người chơi và nền minimap lệch nhịp, trông như rung.
5. **Nạp vùng mới khi đi xa** (`ChangeLoadArea`, luồng nạp nền, `SetLoadingStatus`): có thể đã có từ bản gốc và chỉ lộ rõ hơn khi hình mượt. Cần so với APK gốc.
6. **Bắt kịp nhịp logic**: khung chậm (nạp vùng, minimap) làm `Breathe` chạy bù nhiều nhịp trong một khung; nội suy chỉ dựa 2 nhịp cuối nên có bước nhảy.
7. **Luồng nhận dò 2 ms (fix34)**: ít khả năng; kiểm bằng cách so fix33 với fix34.

**Cách kiểm tra đề xuất (chưa làm):**
- Người dùng thử cùng đoạn đường cưỡi ngựa với 4 APK (gốc, fix31, fix33, fix34), bật và tắt minimap → khoanh vùng đợt gây lỗi.
- Bản thử nghiệm riêng có log `JXFIX`: số lần đổi vùng camera, thời gian `SetFocusPosition` và `PaintMap` mỗi khung, số lần "nhảy", số nhịp chạy bù mỗi khung.
- Nếu giả thuyết 1 đúng: tách phần minimap/`LookAt` khỏi lệnh gọi mỗi khung (chỉ cập nhật khi vị trí đổi đủ lớn hoặc theo nhịp), giữ camera mượt.

## 7. Công việc chưa thực hiện
- Điều tra và sửa lỗi mục 6.
- Xác nhận fix34 trên điện thoại (8 tình huống báo cáo 33 mục 7; đạn; FPS; pin/nhiệt).
- Chế độ quét 90/120 Hz trên Android và điều tiết đúng theo `LimitFPS`.
- Khung hoạt ảnh vẫn ≤ 18/giây (giới hạn dữ liệu sprite).
- Kỹ năng bấm khi server chưa xong động tác trước vẫn có thể bị server bỏ.
- **Nhánh server 18/36 Hz:** chưa bắt đầu dựng. Máy thật thiếu trình biên dịch C++; `docs-analysis/scripts/cai_cpp_build_tools.ps1` đã sửa lỗi thiếu ngoặc kép ở `--installPath`, **chờ chủ máy chạy lại bằng Admin**. Bản sao nguồn: `D:\JX-build\src18` (lúc sao đã loại các thư mục `Release`/`Debug`/`x64`; có thể phải sao bổ sung `.lib`). Chưa tạo VM thử nghiệm (chủ máy chọn "chưa tạo"). Đánh giá 36 Hz: báo cáo 34 mục 5.
- Server đẩy gói 18 lần/giây và sửa gốc lỗi một ô lệnh: cần dựng lại server trước.
- Việc cũ còn treo: reboot thử task `JX-CDN-8080`; tắt WinRM máy thật (`tat_winrm_may_that.ps1`); dọn dữ liệu thật trong lịch sử git; cập nhật `CLAUDE.md` (còn ghi VM cũ trên ổ C); rà git và commit khi được duyệt.

## 8. Hướng dẫn tiếp tục mà không làm mất tối ưu
1. **Làm trên** `D:\Android\b\Client\Classes` (đang là fix34). Không sửa `C:\Jx1CocoV3\Folder\…`.
2. **Trước khi vá:** sao các file sắp sửa sang thư mục mới (ví dụ `D:\Android\b\backup-fix35\`), không ghi đè `backup-tick`, `backup-fix33`, `backup-fix34`.
3. **Cách vá:** file nguồn mã GBK, công cụ Edit từ chối. Dùng script Python đọc/ghi `latin-1`, mỗi chuỗi neo phải khớp đúng 1 lần, tất cả hoặc không (mẫu: `va_tick_smooth.py`, `va_fix33.py`, `va_fix34.py` trong scratchpad của phiên; logic tương tự chép lại được từ diff). Không truyền mã có dấu `"` qua `python -c` trong PowerShell 5.1; ghi ra file rồi chạy.
4. **Không đụng nếu không có lý do:** khối `[fix33]` trong `KProtocol.cpp`, `KPlayer.cpp`, `KNpc::SendSerCommand`, `TCP_NODELAY` trong `SocketClient.cpp`. Nếu sửa camera/minimap thì chỉ sửa đoạn `[tick-smooth]` trong `KgameWorldVN::draw` và `KNpcRes::SetPos`.
5. **Build:**
   ```powershell
   $env:JAVA_HOME='D:\Android\jdk'; $env:ANDROID_HOME='D:\Android\sdk'; $env:ANDROID_SDK_ROOT='D:\Android\sdk'
   $env:GRADLE_USER_HOME='D:\Android\gradle'; $env:GRADLE_OPTS='-Xmx512m'; $env:ANDROID_USER_HOME='D:\Android\user'
   Set-Location D:\Android\b\Client\proj.android
   & D:\Android\gradle-8.7\bin\gradle.bat assembleDebug --offline --no-daemon '-PPROP_APP_ABI=arm64-v8a' '-Dorg.gradle.jvmargs=-Xmx12g' *> D:\Android\b\build-fixNN.log
   ```
   Thiếu `ANDROID_USER_HOME` thì APK ký sai khóa và không cài đè được.
6. **Sau build:** chép APK sang thư mục riêng (`D:\Android\b\apk-fixNN\`), kiểm `apksigner verify --print-certs` (phải ra `a48601f7…`), so với bản trước chỉ khác `libMyGame.so`, kiểm thư viện chưa strip còn `MoveGuardTick`, `ClearJoystickPendingMove`, `KNpc::UpdateRenderPos`, chuỗi `JXFIX skill send`.
7. **Kiểm thử mô phỏng:** `python -I docs-analysis\patches\test_33_skill_guard.py` (9), `test_34_missile_interp.py` (7); `test_31_tick_smooth.py` mô tả thuật toán bản 31 (15). Cập nhật mô hình nếu đổi thuật toán.
8. **Đưa lên CDN:** chép vào `C:\Jx1CocoV3\data_cdn\apk\`, so SHA256; không đổi cấu hình hay khởi động lại CDN.
9. **Quy tắc dự án vẫn áp dụng:** hỏi trước khi chạy exe server; không commit khi chưa duyệt; không ghi mật khẩu; lệnh Admin do chủ máy chạy; một lỗi thử tối đa 3 lần; không đụng `JX-Server-D` khi chưa được phép.
