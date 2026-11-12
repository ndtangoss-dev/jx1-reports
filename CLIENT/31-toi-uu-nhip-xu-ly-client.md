# 31 - Tối ưu nhịp xử lý client JX1 (nội suy, xử lý gói mỗi khung, giới hạn joystick)

Ngày: 2026-11-11. Dựa trên báo cáo 30. Chỉ sửa **client** (bản copy build `D:\Android\b\Client`). Không sửa server, giao thức, logic 18 Hz, tốc độ, sát thương, kỹ năng. Không commit.

## TÓM TẮT 5 DÒNG
1. Thêm nội suy hiển thị: nhân vật, NPC, quái và camera được vẽ ở vị trí giữa hai nhịp logic 18 Hz theo thời gian thực, nên chuyển động mượt ở 60-120 FPS; vị trí logic không đổi.
2. Gói nhận từ server được xử lý **mỗi khung render** (trước: mỗi 0,1 s), cùng luồng chính như cũ, giữ nguyên thứ tự, tối đa 64 lô mỗi khung.
3. Joystick không còn gửi lệnh mỗi khung: giữ hướng thì 9 lần/giây, đổi hướng tối đa 18 lần/giây, thả tay thì gửi nốt đích cuối; gói tin y nguyên định dạng cũ.
4. Build APK thành công, chữ ký debug giống APK đang dùng (cài đè được); 15/15 kiểm thử mô phỏng thuật toán đạt. **Chưa chạy thử trên điện thoại hay emulator** (không có thiết bị nối `adb`, không có emulator).
5. APK mới: `D:\Android\b\apk-tick\jx-tailscale-8080-tick.apk`. APK đang dùng `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` không bị đụng.

**Cần tôi quyết định: có** (cài thử APK mới trên điện thoại; xem mục 9).

## 1. File đã sửa (bản copy build, có bản gốc)
Bản gốc: `D:\Android\b\backup-tick\` (7 file). Khôi phục: `docs-analysis/scripts/khoi_phuc_client_tick.ps1`. Toàn bộ thay đổi dạng diff: `docs-analysis/patches/31-client-tick-smooth.diff` (397 dòng). Mọi chỗ sửa có chú thích `[tick-smooth]` / `[tick-smooth2]`.

| File (`Classes/…`) | Thay đổi |
|---|---|
| `gamecore/KNpc.h` | Thêm 7 thành viên vị trí hiển thị (`m_nRndPrevX/Y`, `m_nRndCurX/Y`, `m_nRndSubWorld`, `m_dwRndTick`, `m_bRndValid`), hàm `UpdateRenderPos`, khai báo 3 biến toàn cục |
| `gamecore/KNpc.cpp` | Biến toàn cục `g_fNpcRenderAlpha`, `g_bNpcRenderInterp`, `g_bNpcInterpCameraOwned`; hàm `UpdateRenderPos`; `GetMpsPos` trả vị trí nội suy chỉ trong pha vẽ; ghi mốc mỗi nhịp trong `Activate`; `Paint` đặt vị trí vẽ thân nhân vật; khởi tạo cờ khi NPC được đặt lại |
| `gamecore/KNpcRes.h` | `SetRenderPos(x, y)` chỉ đổi vị trí vẽ |
| `gamecore/KNpcRes.cpp` | `SetPos` không ép camera theo vị trí logic khi pha vẽ đang điều khiển camera |
| `gamecore/KPlayer.cpp` | Giới hạn gửi lệnh joystick trong `Walk`; gửi nốt đích chờ trong `Active` |
| `gamecore/CoreShell.cpp` | `Goto` không còn đặt lại bộ đếm gửi mỗi khung (làm mất giới hạn) |
| `vn/gamescence/KgameWorldVN.cpp` | Bật `scheduleUpdate`; chuyển khối xả gói từ `custom_update` sang `update`; tính alpha và đặt camera nội suy trong `draw` |

Repo (`Folder/…`) không đổi: `git status -- Folder` 0 dòng.

## 2. Nội suy chuyển động
**Vì sao nội suy giữa các nhịp logic, không giữa các gói tin:** client JX1 tự mô phỏng chuyển động mỗi nhịp (`KNpc::ServeMove`) và server sửa vị trí bằng gói đồng bộ (`s2c_syncnpcmin` 9 lần/giây). Trạng thái logic sau mỗi nhịp đã gộp sẵn dữ liệu server, nên "snapshot" chính xác nhất là vị trí logic của 2 nhịp gần nhất. Cách này độ trễ thêm tối đa 1 nhịp (55,6 ms), không tích lũy, bộ đệm cố định 2 vị trí mỗi NPC.

**Cách làm:**
1. Mỗi nhịp, ngay khi `KNpc::Activate` tính vị trí logic (`NewMap2Mps`), `UpdateRenderPos(x, y)` chuyển vị trí "hiện tại" cũ thành "trước" và lưu vị trí mới, kèm số nhịp (`g_SubWorldSet.m_nLoopRate`).
2. Trong `KgameWorldVN::draw`, sau vòng `Breathe` 18 Hz: `alpha = (elapsed*18 - (nLoopCount-1)*1000)/1000`, kẹp vào [0, 1] = phần nhịp đã trôi qua.
3. Bật cờ `g_bNpcRenderInterp` chỉ quanh `g_ScenePlace.Paint()` và `PaintMap()`. Trong khoảng đó `GetMpsPos` trả `trước + (hiện tại - trước) * alpha`. Thân nhân vật (`KNpc::Paint` → `SetRenderPos`), tên, thanh máu/mana, chat, mũi tên mục tiêu, kiểm tra trong khung nhìn (`CoreDrawGameObj`) đều dùng chung vị trí này nên không lệch nhau.
4. Camera: đặt `SetFocusPosition` theo vị trí nội suy của nhân vật mỗi khung; `KNpcRes::SetPos` không ép camera về vị trí logic khi pha vẽ đang điều khiển, để camera không giật qua lại ở ranh giới vùng.

**Trường hợp đặc biệt (không nội suy, vẽ đúng vị trí logic):**
- Lệch > 96 đơn vị trong 1 nhịp (dịch chuyển, server sửa vị trí lớn).
- NPC không được cập nhật ở nhịp trước (vừa xuất hiện, vừa vào vùng, khe nhịp).
- Đổi bản đồ (`m_SubWorldIndex` khác).
- NPC không được `Activate` ở nhịp hiện tại.
- **Vị trí logic đã khác mốc của nhịp này** (gói server tới sau nhịp và sửa vị trí): vẽ ngay vị trí authoritative, không giữ vị trí cũ.
- Nhân vật bị "nhảy" thì camera theo logic ngay nhịp đó (`g_bNpcInterpCameraOwned = false`).
- Ngoài pha vẽ (logic, AI, gửi lệnh, va chạm) `GetMpsPos` trả vị trí logic như cũ.

**Hướng và xuyên địa hình:** hướng nhân vật (`m_Dir`/`m_ResDir`) không đổi. Nội suy chỉ trên đoạn giữa hai vị trí logic hợp lệ liên tiếp, mỗi đoạn ngắn hơn một bước di chuyển (< 32 đơn vị), nên không có điểm vẽ xa hơn bước logic.

**Người chơi, NPC, quái:** cùng cơ chế (tất cả là `KNpc`). Khác biệt duy nhất: camera chỉ theo nhân vật mình.

## 3. Xử lý gói nhận
- Trước: `schedule(custom_update, 0.1f)` xả hàng đợi 10 lần/giây (`KgameWorldVN.cpp`, dòng cũ 362).
- Nay: khối xả gói y nguyên (gồm xử lý đổi server `s2c_notifyplayerexchange`, kiểm tra loại và kích thước gói) chuyển sang `KgameWorldVN::update(float)`, bật bằng `scheduleUpdate()`. Cocos gọi `update` mỗi khung **trước** `draw` (nơi chạy `Breathe`), giống thứ tự cũ.
- **Không có luồng mới:** luồng socket (`CSocketClient::Run`) vẫn chỉ nhận vào bộ đệm có khóa; xử lý gameplay vẫn trên luồng chính. Không tạo race condition mới.
- **Thứ tự:** một lô = một lần `GetPackFromServer` (dữ liệu đã ghép theo thứ tự đến); duyệt tuần tự như cũ.
- **Không bỏ sót hoặc lặp:** giới hạn 64 lô mỗi khung chỉ dừng trước khi gọi `GetPackFromServer` lần kế tiếp; phần chưa lấy vẫn nằm trong bộ đệm nhận và được lấy ở khung sau. Lô đã lấy được xử lý hết như trước.
- `custom_update` (0,1 s) vẫn giữ phần giao diện (máu/mana/ping/thông báo mất kết nối) như cũ.

## 4. Giới hạn joystick
Đường gọi: `HRocker::updateMovement` (mỗi khung) → `KCoreShell::Goto` → `KPlayer::Walk`.
- Lệnh cục bộ `SendSerCommand` (dự đoán phía client) vẫn chạy mỗi lần gọi như cũ.
- Gói `c2s_npcrun` / `c2s_npcwalk` (định dạng không đổi) chỉ gửi khi:
  - lần đầu bấm (gửi ngay);
  - đổi hướng hoặc đổi chạy/đi, sau ít nhất 1 nhịp → tối đa 18 lần/giây;
  - giữ nguyên hướng: mỗi 2 nhịp → 9 lần/giây. Đích nằm trước 4 nhịp (`GetMps(..., nSpeed*4, ...)`), nên server không dừng giữa chừng.
- Thả joystick: nếu đích mới nhất chưa gửi, `KPlayer::Active` gửi nốt khi joystick đã ngừng ít nhất 1 nhịp trọn, để server dừng đúng chỗ client.
- `KCoreShell::Goto` không còn đặt lại bộ đếm mỗi khung (dòng đó bị chuyển thành chú thích).
- Không áp dụng cho kỹ năng, tấn công, nhặt đồ, chạm bản đồ (`GotoWhere` vẫn giới hạn 5 nhịp như gốc), tương tác.
- Điều kiện chọn chạy/đi giữ nguyên gốc (`m_RunStatus` và thể lực/PK).

## 5. Kết quả build và kiểm thử
- Build: Gradle 8.7, JDK 17, NDK 25.2, `assembleDebug --offline --no-daemon -PPROP_APP_ABI=arm64-v8a`, `GRADLE_OPTS=-Xmx512m`, `-Dorg.gradle.jvmargs=-Xmx12g`, `GRADLE_USER_HOME=D:\Android\gradle`, **`ANDROID_USER_HOME=D:\Android\user`** (khóa debug cũ). Lần 1: thành công 4 phút 16 giây (log `D:\Android\b\build-tick1.log`); lần 2 (đóng gói lại với đúng khóa): 19 giây (`build-tick2.log`).
- Cảnh báo trình biên dịch: chỉ các cảnh báo có sẵn (API Cocos cũ, chuỗi literal); không có cảnh báo hay lỗi ở dòng mới.
- APK: `com.jxclient.hoiuctruyenky` versionCode 17, minSdk 25, targetSdk 34, chỉ `arm64-v8a`, ký `CN=Android Debug` SHA-256 `a48601f7…f2d7` (giống APK đang dùng). So với APK đang dùng: 962/962 file, chỉ khác `lib/arm64-v8a/libMyGame.so`; `assets/package.ini` giống hệt (CDN 8080, Tailscale). Thư viện chưa strip có `KNpc::UpdateRenderPos`, `g_fNpcRenderAlpha`, `g_bNpcRenderInterp`, `g_bNpcInterpCameraOwned`.
- Unit test có sẵn: dự án client không có (chỉ `ltests.c` nội bộ Lua). Đã viết kiểm thử mô phỏng bằng Python tái hiện đúng các thuật toán (`docs-analysis/patches/test_31_tick_smooth.py`): **15/15 đạt**:
  - alpha luôn trong [0, 1] ở 30, 60, 90, 120 FPS;
  - vị trí vẽ tăng đều, không lùi, không vượt vị trí logic, trễ ≤ 1 nhịp;
  - ở 60 FPS số vị trí vẽ khác nhau > 2 lần số nhịp;
  - dịch chuyển, khe nhịp, đổi bản đồ thì "nhảy"; NPC không cập nhật thì vẽ vị trí logic;
  - gói server sửa vị trí giữa nhịp thì vẽ vị trí authoritative; ngoài pha vẽ không ảnh hưởng; bộ đếm nhịp tràn 32 bit vẫn đúng;
  - joystick: giữ hướng 8,5-9,5 lần/giây ở 60 và 120 FPS (trước: bằng FPS); đổi hướng mỗi khung ≤ 18,5 lần/giây; khoảng cách giữa 2 lần gửi ≤ 3 nhịp; thả tay thì đích cuối được gửi trong ≤ 3 nhịp; lần bấm đầu gửi ngay.
- Thiết bị/emulator: không có (adb không thấy thiết bị, SDK không có emulator/system image). **Hạng mục 4 (8 hướng, dừng/đổi hướng, joystick, chạm bản đồ, người khác, NPC/quái, đánh, chuyển bản đồ, mất mạng, nhiều gói cùng lúc) chưa kiểm trên máy thật.**
- Server: không đổi; `JX-Server-D` vẫn chạy.

## 6. Lỗi đã sửa trong quá trình làm
- **APK ký sai khóa:** lần build đầu không đặt `ANDROID_USER_HOME`, Gradle tự tạo khóa debug mới ở `C:\Users\<user>\.android\debug.keystore` (18:41:07) nên chữ ký khác (`84341660…`), không cài đè được. Build lại với `ANDROID_USER_HOME=D:\Android\user`, chữ ký khớp. File khóa mới tạo ngoài ý muốn **vẫn còn** (chưa xóa vì cần hỏi).
- **Gửi nốt joystick làm mất giới hạn:** bản đầu gửi nốt đích chờ ở mọi nhịp, khiến lúc giữ joystick tần suất lại lên 18 lần/giây. Sửa: chỉ gửi nốt khi joystick đã ngừng ít nhất 1 nhịp trọn (kiểm bằng test `test_rate_limit_straight`).
- `KCoreShell::Goto` đặt lại bộ đếm mỗi khung nên mọi giới hạn trong `Walk` vô hiệu: đã bỏ dòng đó.

## 7. Còn tồn tại / rủi ro
- **Chưa thử trên điện thoại.** Cần kiểm mục 4 thủ công (danh sách ở mục 9).
- Đạn, hiệu ứng kỹ năng, vật phẩm rơi và hoạt ảnh sprite vẫn 18 Hz (chỉ vị trí NPC/nhân vật/camera được nội suy). Hiệu ứng gắn theo nhân vật dùng vị trí logic có thể lệch tối đa 1 bước so với thân.
- Hình ảnh trễ thêm tối đa 1 nhịp (55,6 ms) so với logic (giá phải trả của nội suy).
- Khi nhân vật chạy qua ranh giới vùng, việc đổi vùng camera có thể sớm hoặc muộn tối đa 1 nhịp so với trước.
- Nếu `nIsHideNpc`/ẩn người chơi thì không ảnh hưởng (dừng trước khi vẽ như cũ).
- Không bật `TCP_NODELAY` (không trong phạm vi; Nagle có thể giữ gói nhỏ).
- Server vẫn đẩy gói 9 lần/giây; độ trễ phần server không đổi.
- Mã nguồn client bản copy build được giả định là nguồn của APK đang dùng (APK mới chỉ khác `libMyGame.so`, các file khác giống hệt).

## 8. Đường dẫn
- **APK mới:** `D:\Android\b\apk-tick\jx-tailscale-8080-tick.apk` (78.917.739 byte, SHA256 `DAB8485EBEBE634DC6734199C66007B2BB4337AF79CC7F07C1AA1543C6338338`).
- APK đang dùng (không đổi): `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk`.
- Bản gốc 7 file: `D:\Android\b\backup-tick\`; khôi phục: `docs-analysis/scripts/khoi_phuc_client_tick.ps1`.
- Diff: `docs-analysis/patches/31-client-tick-smooth.diff`; kiểm thử: `docs-analysis/patches/test_31_tick_smooth.py`.

## 9. Việc cần chủ máy
1. Duyệt cài APK mới lên điện thoại (cài đè được vì cùng chữ ký và versionCode; dữ liệu app giữ nguyên). Gửi qua Taildrop như trước nếu được duyệt.
2. Thử theo danh sách: chạy 8 hướng; dừng và đổi hướng liên tục; chạy bằng joystick; chạm bản đồ; nhìn người chơi khác và NPC/quái di chuyển; đánh quái (hoạt ảnh đánh); qua cổng đổi bản đồ; tắt/bật Wi-Fi để mất mạng rồi kết nối lại; khu đông NPC. Ghi lại chỗ giật, lệch tên/thanh máu so với thân, hoặc nhân vật "trượt".
3. Quyết định có xóa khóa debug tạo nhầm `C:\Users\<user>\.android\debug.keystore` không (không ảnh hưởng gì khi build với `ANDROID_USER_HOME=D:\Android\user`).

## 10. Chuẩn bị cài thử (chủ máy duyệt, 2026-11-11 18:45)
- APK mới chép vào gốc CDN: `C:\Jx1CocoV3\data_cdn\apk\jx-tailscale-8080-tick.apk` (thư mục `data_cdn/` bị git bỏ qua). Không đổi cấu hình, không khởi động lại CDN (PID 4612 vẫn nghe `<TAILSCALE-IP>:8080`, chỉ cho `<TAILSCALE-IP>`).
- **Link tải trên điện thoại (Tailscale bật):** `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-tick.apk`
- SHA256 (bản gốc và bản trên CDN, khớp): `DAB8485EBEBE634DC6734199C66007B2BB4337AF79CC7F07C1AA1543C6338338`, 78.917.739 byte.
- CDN gửi kiểu `application/octet-stream` (Python không biết MIME của `.apk`); trình duyệt vẫn lưu được file, mở file vừa tải để cài (có thể phải cho phép "cài ứng dụng không rõ nguồn" với trình duyệt).
- Giữ nguyên: APK cũ `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` (SHA256 `82674B16…`), bản gốc 7 file `D:\Android\b\backup-tick\`, khóa debug `C:\Users\<user>\.android\debug.keystore`. Không sửa source thêm.
- Muốn quay lại APK cũ: tải `jx-tailscale-8080.apk` cùng chữ ký và versionCode, cài đè (hoặc chủ máy duyệt chép nó vào `data_cdn\apk\` như trên).
