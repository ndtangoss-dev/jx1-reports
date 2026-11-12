# 30 - Phân tích nhịp xử lý (FPS, tick, mạng) của JX1

Ngày: 2026-11-11. Nghiên cứu mã nguồn và đo không xâm lấn. Không sửa source, cấu hình, không đổi nhịp server hay client, không commit.

Đường dẫn viết tắt: `C/` = `Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/`; `S/` = `SwordOnline/SwordOnline/jxOnline/gameserver/Sources/`. Mã nguồn có thể không khớp hoàn toàn exe/APK đang chạy; chỗ nào đã đối chiếu với thực tế thì ghi rõ.

## TÓM TẮT 5 DÒNG
1. Lõi game (server và client) là mô phỏng bước cố định **18 nhịp/giây**, hằng số biên dịch `GAME_FPS 18`. Đo trên `gs001`: đúng 18,000 nhịp/giây suốt 14 phút (không tải).
2. Render client là chuyện khác: Cocos2d-x 3.17.2, mục tiêu **60 FPS** mặc định (chỉnh được 30-120), nhưng vị trí và hoạt ảnh chỉ đổi 18 lần/giây vì **không có nội suy**: ở 60 FPS mỗi trạng thái được vẽ lại khoảng 3,3 lần.
3. Mạng: server gom gói và chỉ đẩy đi **9 lần/giây** (mỗi 2 nhịp); NPC đồng bộ vị trí 9 lần/giây; client chỉ xử lý gói nhận **10 lần/giây** (bộ hẹn 0,1 s). Hai nhịp này cộng thêm tới khoảng 200 ms trễ.
4. Nút thắt của "độ mượt" là thiếu nội suy phía client và nhịp xử lý gói 10 Hz phía client; nút thắt "cứng" là 18 Hz mô phỏng, gắn vào mọi dữ liệu game (tốc độ, khung đánh, thời gian kỹ năng, script).
5. Có thể làm client mượt 60+ FPS mà không đụng server (nội suy, xử lý gói mỗi khung, giới hạn gửi lệnh joystick). Không nên đổi 18 Hz.

**Cần tôi quyết định: không.**

## 1. Bảng tần suất từng thành phần

| Thành phần | Giá trị trong source | Đo thực tế | Bằng chứng |
|---|---|---|---|
| Render FPS client (mục tiêu) | 60 mặc định; đọc `LimitFPS` trong `jx50ai/Setting.ini`, nếu < 30 thì đặt 60; thanh trượt 30-120 | Chưa đo | `C/Classes/vn/gamescence/KgameWorldVN.cpp:313-319`; `C/Classes/gameui/KuiOptions.cpp:450-457`; `C/Classes/AppDelegate.cpp:119` (1/60) |
| Render FPS thực trên Android | ≤ 60 (1/60 trở xuống thì không tự điều tiết, theo VSync); 30-59 thì `Thread.sleep` | Chưa đo | `C/cocos2d/cocos/platform/android/java/src/org/cocos2dx/lib/Cocos2dxRenderer.java:85-104` |
| Logic client (`Breathe`) | 18/giây, theo đồng hồ, bù tối đa 128 nhịp/khung; chạy bên trong `draw()` | Chưa đo | `KgameWorldVN.cpp:1529-1560` (`nLoopCount*1000 <= elapsed*18`) |
| Hoạt ảnh sprite | tối đa 1 khung hình / nhịp logic = ≤ 18 khung/giây | Chưa đo | `C/Classes/gamecore/KSprControl.cpp:244-251` (`ChangeNextFrame` chỉ tăng khi `m_dwCurrentTime` đổi); `KSubWorld.cpp:148` (`++m_dwCurrentTime`) |
| Độ dài động tác | đi 12 nhịp, chạy 15 nhịp, đánh 20 nhịp (nhân hệ số tốc độ) | – | `C/Classes/gamecore/KNpc.cpp:443-449, 2092, 2381` |
| Di chuyển (client và server) | bước theo nhịp: `MoveSpeed` đơn vị/nhịp, giới hạn < 32 | – | `KNpc.cpp:3256-3295` (`ServeMove`) |
| Nội suy vị trí | **Không có** | – | Không tìm thấy `interpol`/`lerp`/`smooth` trong `gamecore` vẽ nhân vật |
| Client xử lý gói nhận | 10/giây (`schedule(custom_update, 0.1f)`), mỗi lần xả hết hàng đợi | Chưa đo | `KgameWorldVN.cpp:362, 3553-3614` |
| Luồng nhận socket client | luồng riêng, socket non-blocking, ngủ 10 ms mỗi 2 vòng (≈ 100-200 lần thăm dò/giây) | – | `C/Classes/network/SocketClient.cpp:288-331, 206-214` |
| Client gửi lệnh đi (chạm bản đồ) | tối đa 1 lệnh / 5 nhịp = 3,6/giây | – | `C/Classes/gamecore/GameDataDef.h:29`; `CoreShell.cpp:5034`; `KPlayer.cpp:234, 528-545` |
| Client gửi lệnh đi (joystick) | **mỗi khung render** (60/giây ở 60 FPS); giới hạn 5 nhịp đã bị comment | Chưa đo | `C/Classes/gamescene/KHRocker.cpp:587, 598-639`; `CoreShell.cpp:5124-5149`; `KPlayer.cpp:588-662` (dòng 651 comment) |
| Gửi gói từ client | gửi ngay (không gom), không đặt `TCP_NODELAY` | – | `C/Classes/network/ClientStage.cpp:136-177`; không có `TCP_NODELAY` trong `network/` |
| Tick logic server | 18/giây, `GAME_FPS 18`, theo `KTimer` (QueryPerformanceCounter), chạy bù khi chậm, `Sleep(1)` khi rảnh | **18,000/giây** (GameLoop +1080/phút, 18:05-18:19, 0 người chơi) | `S/MultiServer/GameServer/KSOServer.cpp:90, 1425-1471`; console `gs001` |
| Cập nhật người chơi, NPC, đạn, chiến đấu | mỗi nhịp, một luồng, duyệt `MAX_SUBWORLD` bản đồ (OpenMP đã comment) | – | `S/Core/Src/KSubWorldSet.cpp:505-612`; `KSubWorld.cpp:302-305`; `KRegion.cpp:1100-1191` |
| Server đẩy gói ra mạng | mỗi 2 nhịp = **9/giây** (`SendPackToClient(-1)` khi `m_nGameLoop & 1`) | – | `KSOServer.cpp:4378-4379` |
| Đồng bộ NPC (vị trí, máu, trạng thái) | mỗi NPC mỗi 2 nhịp = 9/giây, chỉ ở vùng có người chơi | – | `S/Core/Src/KRegion.cpp:1117-1127`; `KNpc.cpp:7886-7945` (`s2c_syncnpcmin`) |
| Đồng bộ chỉ số bản thân (máu, mana, thể lực) | đóng gói mỗi nhịp (18/giây), đi ra cùng đợt đẩy 9/giây | – | `S/Core/Src/KPlayer.cpp:341, 1147-1173` |
| Ping server → client | khoảng cách tối thiểu 5 s, timeout 30 s; nhưng mỗi nhịp chỉ xét 1 ô trạng thái (500 ô) nên mỗi người chơi được xét khoảng mỗi 27,8 s | – | `KSOServer.cpp:4381-4430` |
| Băng thông thực (phiên điện thoại) | – | 32,4 s trong gs001: 6.841 byte lên (≈ 211 B/s), 992.799 byte xuống (≈ 30 KB/s, gồm đồng bộ ban đầu) | `reports/19-cdn-8080-va-forwarder.md:28` |

## 2. Giới hạn cứng và mềm

**Cứng (cần dựng lại exe và đổi dữ liệu):**
- `GAME_FPS 18` biên dịch trong `gs001` (`KSOServer.cpp:90`, `CoreServerShell.cpp:2227`) và client (`KgameWorldVN.cpp:1544` dùng số 18 viết thẳng).
- Mọi đại lượng tính theo nhịp: tốc độ di chuyển (đơn vị/nhịp), số nhịp động tác, thời gian trạng thái, cooldown, timer Lua (nhiều chỗ `18*60`, `FRAME2TIME 18`, `GAME_UPDATE_TIME 10` trong `KNpc.cpp:78-80`), timeout mạng (`defMAX_PING_TIMEOUT 30*GAME_FPS`).
- Đồng bộ thời gian client theo khung server (`KProtocolProcess.cpp:3227` `m_dwCurrentTime = WorldSync->Frame`).
- Server một luồng cho toàn bộ thế giới.

**Mềm (chỉ cần sửa client):**
- Render FPS (đã cấu hình được 30-120).
- Nhịp xử lý gói 0,1 s phía client.
- Giới hạn gửi lệnh joystick.
- Nội suy hình ảnh giữa hai nhịp.
- Nhịp đẩy gói 9/giây của server: một dòng code, nhưng phải dựng lại `gs001` (mã nguồn có thể không khớp exe), nên xếp vào nhóm "cứng" về thực tế.

## 3. Nút thắt
- **Độ mượt hình ảnh:** thiếu nội suy (18 Hz vị trí, ≤ 18 khung hoạt ảnh) dù render 60 FPS.
- **Độ trễ phản hồi:** server đẩy 9/giây (đến 111 ms) cộng client xử lý 10/giây (đến 100 ms) cộng mạng (ping qua DERP khoảng 150 ms). Hai nhịp 9 Hz và 10 Hz lệch nhau nên đôi khi client xử lý 2 đợt dữ liệu cùng lúc (giật).
- **Lưu lượng lên:** joystick gửi lệnh mỗi khung render (đến 60-120 gói/giây), trong khi server chỉ mô phỏng 18 nhịp/giây.
- **Tick server:** không phải nút thắt khi rảnh (18,000/giây). Dưới tải chưa đo.

## 4. Có thể nâng lên bao nhiêu
| Mục | Đề xuất | Điều kiện | Ảnh hưởng |
|---|---|---|---|
| Render client | 60 FPS (hoặc theo màn hình 90-120) | Thêm nội suy giữa nhịp t-1 và t (alpha = thời gian dư / 55,6 ms) | CPU/GPU điện thoại tăng; server không đổi |
| Xử lý gói client | mỗi khung (thay 0,1 s) | Sửa `custom_update` hoặc tách phần xả gói sang `update()` | Giảm trễ trung bình khoảng 50 ms; CPU tăng không đáng kể |
| Gửi lệnh joystick | ≤ 9-18 lần/giây, chỉ khi hướng đổi | Khôi phục giới hạn kiểu `defMAX_PLAYER_SEND_MOVE_FRAME` | Giảm băng thông lên và tải server |
| Server đẩy gói | 18/giây (bỏ điều kiện `& 1`) | Dựng lại `gs001` từ nguồn và kiểm tra khớp | Gấp đôi số gói TCP, payload gần như không đổi; trễ giảm đến 55 ms |
| Tick logic | Giữ 18 | Đổi sang 30/60 cần đổi mọi hằng số, dữ liệu, script và cả server; rủi ro sai gameplay cao | Không khuyến nghị |

## 5. Kiến trúc nhịp đề xuất cho Unity client mới
1. **Mô phỏng bước cố định 18 Hz** (bộ tích lũy thời gian riêng, không dùng `Update` thô), tái hiện đúng logic chạy, đánh, khung động tác theo nhịp như server.
2. **Render theo màn hình** (60/90/120), vẽ nội suy giữa 2 trạng thái nhịp gần nhất; nhân vật của mình có thể dự đoán (client-side prediction) rồi sửa mượt khi server điều chỉnh.
3. **Bộ đệm snapshot từ server:** giữ khoảng 2 lần đẩy (≈ 110-220 ms), vẽ NPC và người chơi khác trễ một chút cho mượt.
4. **Luồng mạng riêng:** nhận và giải mã, đẩy vào hàng đợi thread-safe; luồng chính xả hàng đợi **mỗi khung**, không theo bộ hẹn 0,1 s.
5. **Gửi input theo nhịp mô phỏng** (≤ 18/giây), chỉ khi thay đổi; giữ đúng định dạng gói `c2s_npcrun`/`c2s_npcwalk` hiện có để server không cần sửa.
6. **Hoạt ảnh:** chọn khung theo thời gian nhịp (có thể nội suy chỉ vị trí, giữ khung sprite 18 fps để khớp hitbox/timing gốc).
7. Bật `TCP_NODELAY` ở client mới để lệnh nhỏ không bị Nagle giữ lại (cần thử, chưa đo).

## 6. Chưa đủ dữ liệu
- FPS render thực trên điện thoại Xiaomi (không có thống kê; `setDisplayStats` chỉ bật được bằng nút dành cho GM, `KgameWorldVN.cpp:2859-2867`), tần số quét màn hình máy đang dùng.
- Số gói lên/xuống mỗi giây khi chơi thật, tỷ lệ gói joystick; độ dao động.
- Tick server và CPU `gs001` khi có người chơi, nhiều NPC, đánh nhau.
- Cách `Heaven.dll` đẩy gói (có tự đẩy ngoài lời gọi `SendPackToClient` không) – cần đo gói trên dây.
- APK và exe đang chạy có khớp mã nguồn ở các chỗ trên không (đã khớp ở chỗ crash `gs001`, báo cáo 29; phần client chưa đối chiếu).

## 7. Cách đo ít xâm lấn (đề xuất, chưa làm)
- Server: đọc dòng `SvrFPS`/`GameLoop` mỗi phút trên console `gs001` trong lúc chơi; đo CPU `gs001` bằng `Get-Process` trong VM (chỉ đọc).
- Mạng: forwarder đã ghi tổng byte mỗi phiên; có thể thêm (bản riêng) bộ đếm gói theo giây trong `tcp_forwarder.py`, hoặc chạy `pktmon`/Wireshark trên máy thật (cần duyệt).
- Client: build APK thử nghiệm bật `setDisplayStats(true)` hoặc ghi log FPS mỗi giây; không thay APK đang thử khi chưa duyệt.
