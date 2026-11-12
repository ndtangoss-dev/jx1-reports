# 33 - Sửa mất sát thương khi vừa di chuyển vừa dùng kỹ năng, và tối ưu độ mượt

Ngày: 2026-11-11. Dựa trên báo cáo 30, 31, 32. Chỉ sửa **client** (bản copy build `D:\Android\b\Client`). Server, giao thức, logic 18 Hz, tốc độ đánh, sát thương không đổi. Không commit.

## TÓM TẮT 5 DÒNG
1. **Nguyên nhân chính:** server chỉ có **một ô lệnh** mỗi nhân vật và xử lý gói ngay khi tới, còn thực thi ở nhịp 18 Hz kế tiếp; gói chạy tới sau gói kỹ năng mà trước nhịp đó sẽ **xóa lệnh kỹ năng**. Client không tắt Nagle, RTT qua Tailscale khoảng 150 ms, nên khi đang chạy gói kỹ năng thường bị TCP **gộp chung với gói chạy gửi sau** và tới server cùng lúc.
2. Hoạt ảnh và va chạm vẫn hiện vì đó là **mô phỏng cục bộ** của client (`KMissle::ProcessCollision` → `CreateSpecialEffect`); máu/sát thương chỉ do server gửi (`s2c_npchurt`). Khi đứng yên không có gói chạy nên không mất.
3. Sửa: tắt Nagle (`TCP_NODELAY`); khóa di chuyển 3 nhịp sau mỗi lệnh kỹ năng và trong lúc nhân vật đang ra chiêu (lệnh chạy được **hoãn**, chỉ giữ lệnh mới nhất, gửi khi hết khóa); lệnh chạy cục bộ không đè lệnh kỹ năng đang chờ. Giao thức không đổi.
4. Độ mượt: nhịp sau tiếp tục từ vị trí đang vẽ (hết "trượt lùi" khi server sửa vị trí giữa nhịp); tắt Nagle giảm trễ lệnh lên server. Mô phỏng: tỷ lệ kỹ năng server thực thi khi vừa chạy vừa đánh từ 0% (APK gốc) / 44% (APK 31) lên 100%.
5. Build OK, cùng chữ ký debug; **chưa thử trên điện thoại**. APK: `D:\Android\b\apk-fix33\jx-tailscale-8080-fix33.apk`, tải: `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-fix33.apk`.

**Cần tôi quyết định: có** (cài thử và đo theo mục 7).

## 1. Truy vết luồng kỹ năng → sát thương
| Bước | Client | Server |
|---|---|---|
| 1. Bấm kỹ năng / AI tự đánh | `KCoreShell::UseSkill` / `KPlayer` / `KNpcAI` gọi `Npc.SendSerCommand(do_skill,…)` (lệnh cục bộ) và `SendClientCmdSkill` (`gamecore/CoreShell.cpp:4939-4993`, `KPlayer.cpp:492-512`, `KNpcAI.cpp:827-828`) | |
| 2. Gửi | `SendPackToServer` → `CSocketClient::Write` → `send()` ngay, **không `TCP_NODELAY`** (`network/SocketClient.cpp:395-434`) | |
| 3. Nhận | | `MessageLoop` chạy ở mỗi vòng `Breathe` (≈ mỗi 1 ms khi rảnh), lấy gói và gọi ngay `NpcSkillCommand` / `NpcRunCommand` (`MultiServer/GameServer/KSOServer.cpp:1479-1605`, `Core/Src/KProtocolProcess.cpp:5452-5483, 5581-5607`) |
| 4. Ô lệnh | `KNpc::SendSerCommand` ghi đè `m_Command` (`gamecore/KNpc.cpp`, hàm `SendSerCommand`) | Cùng cơ chế: lệnh đến sau thắng |
| 5. Thực thi | `ProcCommand` mỗi nhịp → `DoSkill` → hoạt ảnh, đạn **cục bộ** | `ProcCommand` mỗi nhịp 18 Hz (`Core/Src/KNpc.cpp:1296-1407`), xóa ô lệnh sau mỗi nhịp |
| 6. Chấp nhận/từ chối | | `DoSkill` (`Core/Src/KNpc.cpp:3609-3777`): từ chối nếu đang `do_skill`/`do_hurt` (`:3615`), không ở chế độ chiến đấu (`:3622`), chưa hết hồi chiêu (`:3647-3660`), `CanCastByIndex`/`CanCastSkill`/`Cost` thất bại (`:3673-3771`), mục tiêu không hợp lệ (`:3699-3714`), cận chiến `CastMeleeSkill` thất bại (`:3797`). Chấp nhận thì phát `s2c_skillcast` cho vùng |
| 7. Ra đòn | Đạn cục bộ va chạm → **hiệu ứng trúng đòn cục bộ** (`gamecore/KMissle.cpp:1734-1744`) | `OnSkill`: tới 60% số khung (`ATTACKACTION_EFFECT_PERCENT 60`) gọi `pSkill->Cast` → sát thương (`Core/Src/KNpc.cpp:3979-4024`) |
| 8. Kết quả | Máu quái giảm khi nhận `s2c_npchurt` (`gamecore/KProtocolProcess.cpp:71`) | Gửi `s2c_npchurt`, đồng bộ máu |

- Trong lúc server đang ra chiêu, `DoOrdinSkill` đặt `m_ProcessAI = 0` (`Core/Src/KNpc.cpp:3836`) nên mọi lệnh chạy tới sau đó bị **bỏ qua và xóa** (`:1371-1406`). Lệnh chạy không cắt ngang được kỹ năng **đã bắt đầu**; nó chỉ phá được kỹ năng **chưa tới nhịp**.

## 2. Nguyên nhân chính xác
**Có bằng chứng mã nguồn:**
1. Server xử lý gói ngay khi tới nhưng chỉ thực thi ô lệnh ở nhịp 18 Hz (cửa sổ tới 55,6 ms). Gói chạy tới sau gói kỹ năng trong cửa sổ đó **xóa lệnh kỹ năng**; server không gọi `DoSkill`, không có `s2c_skillcast`, không sát thương.
2. Client không đặt `TCP_NODELAY` (không có trong `network/`); Android mặc định bật Nagle: khi còn dữ liệu chưa được ACK, gói nhỏ mới bị giữ lại cho tới khi ACK về (≈ 1 RTT ≈ 150 ms qua DERP). Khi giữ joystick (APK 31: gửi 9 lần/giây) luôn có gói chưa ACK, nên gói kỹ năng chờ trong bộ đệm và được gửi **cùng** với gói chạy tiếp theo → tới server cùng một lúc, gói chạy đứng sau → ghi đè.
3. Client hiển thị hoạt ảnh và va chạm bằng mô phỏng cục bộ (bước 5, 7), nên người chơi thấy "trúng" dù server không đánh.
4. Đứng yên: không có gói chạy → không có ghi đè → sát thương bình thường, khớp quan sát.

**Định lượng (mô phỏng, chưa đo trên máy)** – `docs-analysis/patches/test_33_skill_guard.py bang` (RTT 150 ms, dao động 20 ms, bấm kỹ năng mỗi 0,9-1,1 s trong 60 s):

| Kịch bản | Bấm | Server thực thi | Tỷ lệ |
|---|---|---|---|
| Đứng yên, APK gốc | 59 | 59 | 100% |
| Chạy, APK gốc (joystick mỗi khung + Nagle) | 59 | 0 | 0% |
| Chạy, APK 31 (9 lần/giây + Nagle) | 59 | 26 | 44% |
| Chạy, bản sửa 33 (khóa + `TCP_NODELAY`) | 59 | 59 | 100% |
| Chạy 120 FPS, bản sửa 33 | 59 | 59 | 100% |

Mức 44% của mô phỏng gần với quan sát "5 lần trúng 1" (RTT thật qua DERP/4G thường cao và dao động hơn 150 ms, làm tỷ lệ thấp hơn).

**Không phải nguyên nhân (đã loại trừ bằng mã):** server không kiểm khoảng cách trong `CanCastSkill` (`Core/Src/KSkills.cpp:221-281`, chỉ kiểm quan hệ/vũ khí); lệnh chạy không cắt ngang kỹ năng đã bắt đầu (mục 1).

**Còn có thể gây mất, không do di chuyển (chưa sửa, server quyết):** bấm kỹ năng khi server còn đang ra chiêu trước (client kết thúc động tác sớm hơn server khoảng ½ RTT + ≤ 1 nhịp); đang bị đánh (`do_hurt`); hồi chiêu; thiếu mana; mất chế độ chiến đấu.

## 3. Phân loại kỹ năng
- **Vừa chạy vừa đánh:** không có trong bản mã này. Mọi kỹ năng thường (`Missles`, `Melee`, `InitiativeNpcState`, `PassivityNpcState`) đều chuyển nhân vật sang `do_attack`/`do_magic` (đứng tại chỗ) (`Core/Src/KNpc.cpp:3748-3749, 3820, 3833`); `do_runattack`/`do_runattackmany` có trong enum nhưng `ProcCommand` không xử lý (`:1364-1367`).
- **Yêu cầu đứng yên:** tất cả kỹ năng trên. Khóa di chuyển của bản sửa phù hợp với hành vi server (server cũng bỏ lệnh chạy khi đang ra chiêu).
- **Server từ chối:** các điều kiện ở bước 6. Client không có gói xác nhận riêng; dấu hiệu là không có `s2c_npchurt`/thay đổi máu.
- **Server chấp nhận:** server phát `s2c_skillcast` cho vùng (client bỏ qua gói của chính mình qua `ConformIdx`) và sau đó `s2c_npchurt` khi trúng.

## 4. File đã sửa (đợt 33)
Bản trước đợt 33 (trạng thái APK 31): `D:\Android\b\backup-fix33\`. Khôi phục: `docs-analysis/scripts/khoi_phuc_client_fix33.ps1` (thêm `-VeGoc` để về hẳn bản gốc trước 31). Diff: `docs-analysis/patches/33-client-skill-guard.diff` (224 dòng). Chú thích trong mã: `[fix33]`.

| File (`Classes/…`) | Thay đổi |
|---|---|
| `network/SocketClient.cpp` | `#include <netinet/in.h>`, `<netinet/tcp.h>`; đặt `TCP_NODELAY` ngay khi tạo socket (`CreateConnectionSocket`) |
| `gamecore/KProtocol.cpp` | Khóa di chuyển: `SendClientCmdRun/Walk` hoãn lệnh khi khóa (1 ô, lệnh mới nhất); `SendClientCmdSkill` bật khóa 3 nhịp, hủy lệnh di chuyển chờ cũ và đích joystick chờ; `MoveGuardTick()` gửi lệnh đã hoãn khi hết khóa (cập nhật cả lệnh cục bộ); bộ đếm và log `JXFIX` (Android log, cả bản Release) |
| `gamecore/KPlayer.cpp` | Gọi `MoveGuardTick()` mỗi nhịp; `ClearJoystickPendingMove()` |
| `gamecore/KNpc.cpp` | `SendSerCommand`: với nhân vật của mình, lệnh chạy/đi không ghi đè lệnh kỹ năng chưa thực thi; nội suy: nhịp sau bắt đầu từ vị trí đã vẽ, ghi lại vị trí vẽ |
| `gamecore/KNpc.h` | `m_nRndDrawX/Y`, `m_dwRndDrawTick`, `HasPendingSkillCmd()` |

Repo (`Folder/`) không đổi.

## 5. Cơ chế sửa
**Khóa di chuyển (`KProtocol.cpp`):**
- Khóa bật khi: còn ≤ 3 nhịp kể từ lần gửi kỹ năng gần nhất, hoặc nhân vật đang `do_attack`/`do_magic`, hoặc còn lệnh kỹ năng cục bộ chưa thực thi.
- Lệnh chạy/đi trong khóa **không bị mất**: lưu vào 1 ô (lệnh mới nhất thắng), gửi ngay nhịp đầu tiên hết khóa, đồng thời đặt cùng đích cho lệnh cục bộ để client và server khớp. Không có hàng đợi.
- Gửi kỹ năng hủy lệnh di chuyển chờ trước đó và đích joystick chờ (kỹ năng thay thế chúng ở cả client lẫn server), tránh server chạy tới đích cũ sau khi đánh.
- 3 nhịp = 167 ms > 1 nhịp server (55,6 ms) + dao động mạng. Trong thời gian nhân vật ra chiêu server vốn bỏ qua lệnh chạy, nên hoãn không làm mất gì.
- Không lặp lại kỹ năng, không đổi thời gian hồi chiêu, tốc độ đánh, sát thương; gói giữ nguyên định dạng.
- Lệnh dừng/đổi hướng (ví dụ `SetNpcCurPos`, chạm bản đồ, joystick) đi qua cùng cơ chế: hoãn rồi gửi, không mất.

**`TCP_NODELAY`:** mỗi gói đi ngay, không chờ ACK; thứ tự TCP giữ nguyên. Áp dụng cho mọi kết nối của client (Bishop, gs).

**Bảo vệ lệnh cục bộ (`KNpc::SendSerCommand`):** chỉ với nhân vật của mình: khi đang có `do_skill` chờ, lệnh `do_run`/`do_walk` cục bộ bị bỏ trong nhịp đó (lệnh tiếp theo vẫn vào bình thường). NPC/người khác không áp dụng.

## 6. Tối ưu độ mượt
| Hạng mục | Làm gì |
|---|---|
| 1-2. Nội suy nhân vật, NPC/quái | Giữ cơ chế 31. Sửa: nhịp sau bắt đầu từ **vị trí đang vẽ** (nếu đã vẽ ở nhịp trước), nên khi server sửa vị trí giữa nhịp, hình không còn nhảy về vị trí cũ rồi chạy lại ("trượt lùi") |
| 3. Camera | Theo vị trí nội suy của nhân vật (31); hưởng lợi từ sửa trên |
| 4. Đổi hướng | Hướng vẽ (`m_ResDir`) giữ nguyên cơ chế gốc (quay dần mỗi khung). Gói đổi hướng không còn bị Nagle giữ → server đổi hướng sớm hơn ½-1 RTT |
| 5. Trượt vị trí | Như 1-2; sửa vị trí lớn hơn 96 đơn vị vẫn "nhảy" ngay (không nội suy sai authoritative) |
| 6. Thiếu snapshot | NPC không cập nhật ở nhịp trước → vẽ đúng vị trí logic (31); không ngoại suy |
| 7. Thân, tên, máu, hiệu ứng | Dùng chung vị trí vẽ (31) |
| 8. Đạn, kỹ năng | **Chưa nội suy** (vẫn 18 Hz). Kỹ năng giờ được server thực thi đúng nên hiệu ứng/sát thương nhất quán hơn |
| 9. Bộ đệm | Cố định 2 vị trí + 1 vị trí đã vẽ mỗi NPC; không tăng |
| 10. Trễ gói | Xử lý gói mỗi khung (31); `TCP_NODELAY` bỏ trễ Nagle ở chiều lên |

Không thêm ngoại suy, không đổi tốc độ hay vị trí logic.

## 7. Kiểm thử
**Build:** Gradle 8.7, JDK 17, NDK 25.2, `assembleDebug --offline --no-daemon -PPROP_APP_ABI=arm64-v8a`, `GRADLE_OPTS=-Xmx512m`, `-Dorg.gradle.jvmargs=-Xmx12g`, `GRADLE_USER_HOME=D:\Android\gradle`, `ANDROID_USER_HOME=D:\Android\user`. Lần 1: 3 phút 15 giây (`D:\Android\b\build-fix33.log`); lần 2 (đổi log sang Android log vì `CCLOG` bị loại trong bản native Release): 2 phút 9 giây (`build-fix33b.log`). 0 lỗi biên dịch ở file đã sửa.

**APK:** `com.jxclient.hoiuctruyenky` versionCode 17, `arm64-v8a`, chữ ký `CN=Android Debug` SHA-256 `a48601f7…f2d7` (giống APK đang dùng và APK 31); chỉ khác APK 31 ở `libMyGame.so`; `package.ini` giống. Thư viện chưa strip có `MoveGuardTick`, `ClearJoystickPendingMove`, `KNpc::UpdateRenderPos`, chuỗi `JXFIX skill send`, `JXFIX move flushed`.

**Kiểm thử mô phỏng** (`docs-analysis/patches/test_33_skill_guard.py`, mô hình client + Nagle + server 1 ô lệnh, TCP giữ thứ tự): **9/9 đạt**:
- đứng yên: 100% kỹ năng được thực thi (APK gốc và bản sửa);
- chạy: APK gốc < 50% (thực tế 0%), APK 31 < 80% (44%), bản sửa 100% ở 60 và 120 FPS với 3 seed;
- chỉ có khóa (vẫn Nagle) ≥ 90%;
- không gói chạy nào trong 3 nhịp sau gói kỹ năng;
- lệnh hoãn chỉ 1 ô, gửi đúng 1 lần;
- nội suy: không nhảy lùi sau khi server sửa vị trí giữa nhịp; chuyển động đều không lùi, không vượt vị trí logic.
- Trong lúc làm đã phát hiện và sửa một lỗi **của mô hình** (cho phép gói TCP đảo thứ tự), không phải của bản vá.
- `test_31_tick_smooth.py` mô phỏng thuật toán bản 31 (không còn đúng chi tiết sau sửa "vị trí đã vẽ"); thay bằng kiểm thử nội suy trong `test_33`.

**Trên điện thoại / emulator:** không có thiết bị nối `adb`, không có emulator. **Tám tình huống (đứng đánh, chạy đánh, đổi hướng + kỹ năng, chạy + buff, nhiều quái, kỹ năng liên tiếp, mục tiêu di chuyển, dừng joystick ngay sau tung chiêu) chưa chạy thật.**

**Cách đo số lần theo yêu cầu (khi có điện thoại):**
| Đại lượng | Cách đo |
|---|---|
| Nhấn kỹ năng | Đếm tay theo kịch bản (vd 20 lần) |
| Client gửi lệnh | `adb logcat -s JXFIX`: dòng `JXFIX skill send … skill=<n>` (bộ đếm tích lũy), kèm số lệnh di chuyển hoãn/gửi/bị thay thế |
| Server nhận / chấp nhận | Server không log sẵn; đề xuất (cần duyệt) bật chế độ debug sát thương của server (`DamageParmInfo.nIsDebug` + tên nhân vật trong cấu hình) để console in `[OnSkill]` khi ra đòn, hoặc dựa vào người chơi khác thấy `s2c_skillcast` |
| Server gây sát thương | Số lần máu quái giảm / số dòng sát thương hiển thị (đến từ `s2c_npchurt`), không dùng hoạt ảnh |

## 8. Chưa kiểm chứng / còn tồn tại
- Toàn bộ trên điện thoại (mục 7).
- Kỹ năng bấm ngay khi động tác trước vừa xong ở client nhưng server chưa xong (lệch ½ RTT) vẫn có thể bị server bỏ (hành vi server, không do di chuyển).
- Đạn và hiệu ứng bay vẫn 18 Hz.
- `TCP_NODELAY` tăng nhẹ số gói TCP chiều lên (mỗi lệnh một gói); lệnh joystick đã giới hạn ≤ 18/giây nên không đáng kể.
- Mã nguồn server có thể không khớp hoàn toàn `gs001.exe` (phần ô lệnh và `MessageLoop` chưa đối chiếu mã máy).

## 9. Đường dẫn
- **APK mới:** `D:\Android\b\apk-fix33\jx-tailscale-8080-fix33.apk`, 78.917.739 byte, SHA256 `E9FB0DBFEB7633CD0FF2BD2CE6F75A3F4D74612FB2C47CCED084EFEA8CF69CC4`.
- **Trên CDN (SHA256 khớp):** `C:\Jx1CocoV3\data_cdn\apk\jx-tailscale-8080-fix33.apk`.
- **Link tải trên điện thoại:** `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-fix33.apk`
- Giữ nguyên: APK gốc `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk`, APK 31 `D:\Android\b\apk-tick\jx-tailscale-8080-tick.apk` (cả hai vẫn trên CDN/ổ D), bản gốc `D:\Android\b\backup-tick\`, bản trước 33 `D:\Android\b\backup-fix33\`, khóa debug. CDN không đổi cấu hình, không khởi động lại (PID 4612). Server `JX-Server-D` không bị đụng.
