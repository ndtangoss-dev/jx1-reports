# 34 - Tối ưu toàn diện độ mượt và đánh giá 36 Hz

Ngày: 2026-11-11. Dựa trên báo cáo 30-33. Chỉ sửa **client** (bản copy build `D:\Android\b\Client`). Server chính, giao thức, logic 18 Hz, tốc độ, sát thương không đổi. Toàn bộ fix31 và fix33 giữ nguyên. Không commit.

## TÓM TẮT 5 DÒNG
1. Đã làm thêm: **nội suy vị trí vẽ của đạn/projectile** (phần hình ảnh cuối cùng còn chạy 18 Hz về vị trí) và giảm trễ luồng nhận gói từ tối đa 10 ms xuống 2 ms. fix33 (`TCP_NODELAY`, hoãn lệnh di chuyển sau kỹ năng, bảo vệ lệnh kỹ năng) không bị đụng.
2. **36 Hz: không làm bản thử nghiệm.** Đổi nhịp đòi hỏi dựng lại server từ mã nguồn chưa từng dựng và chưa chắc khớp exe, quy đổi 4 bảng dữ liệu lớn, khoảng 950 dòng Lua trong hàng trăm file, dữ liệu trong 3,2 GB pak của client, cùng 16 trường gói tin theo nhịp; 13-24% tốc độ là số lẻ nên không chia đôi được mà không đổi gameplay. Rủi ro vượt xa lợi ích; chi tiết ở mục 5.
3. Phương án thay thế đã áp dụng: mô phỏng giữ 18 Hz, hình ảnh nội suy theo tần số màn hình (nhân vật, NPC, quái, camera, tên/máu, và nay là đạn); trễ thêm của hình dưới 2 nhịp, không tích lũy.
4. Build OK, cùng chữ ký debug; kiểm thử mô phỏng 7/7 (đạn) và 9/9 (fix33) đạt. **Chưa thử trên điện thoại.**
5. APK: `D:\Android\b\apk-fix34\jx-tailscale-8080-fix34.apk`; tải: `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-fix34.apk`.

**Cần tôi quyết định: có** (cài thử fix34; có muốn đi tiếp hướng 36 Hz hay các đề xuất ở mục 6 không).

## 1. Vấn đề tìm thấy
| # | Vấn đề | Trạng thái |
|---|---|---|
| 1 | Đạn/hiệu ứng bay (`KMissle`) vẽ đúng vị trí logic, chỉ đổi 18 lần/giây, trong khi thân nhân vật đã nội suy → đạn giật so với nền và thân | **Đã sửa (34)** |
| 2 | Luồng nhận socket ngủ 10 ms mỗi 2 vòng (`network/SocketClient.cpp`), cộng tới 10 ms trước khi gói tới luồng chính | **Đã giảm còn 2 ms (34)** |
| 3 | Sau sửa "đi tiếp từ vị trí đang vẽ" (33), độ trễ hình có thể hơn 1 nhịp (hội tụ khoảng 1,4 nhịp ở 60 FPS) | Chấp nhận: đổi lấy việc không giật lùi; có giới hạn, không tích lũy |
| 4 | Khung hoạt ảnh nhân vật/hiệu ứng chỉ đổi theo nhịp (≤ 18 khung/giây) | Không sửa được bằng code: sprite chỉ có số khung rời rạc, thời lượng động tác tính theo nhịp |
| 5 | Thả joystick: nhân vật chạy nốt tới đích đã gửi (trước 4 nhịp) | Giữ nguyên: là hành vi gameplay ở cả server |
| 6 | Android: khi `LimitFPS` ≤ 60 Cocos không tự điều tiết, FPS theo tần số quét hệ thống cấp cho app; chưa yêu cầu chế độ 90/120 Hz | Chưa sửa (cần thử trên máy thật; xem mục 6) |
| 7 | Server chỉ đẩy gói 9 lần/giây | Cần dựng lại server; ngoài phạm vi đợt này |
| 8 | Kỹ năng bấm khi server chưa xong động tác trước vẫn bị server bỏ | Hành vi server; chưa sửa |

## 2. Thay đổi đã thực hiện (đợt 34)
Bản trước đợt 34 (trạng thái fix33): `D:\Android\b\backup-fix34\`. Diff: `docs-analysis/patches/34-client-missile-interp.diff`. Chú thích trong mã: `[fix34]`.

| File (`Classes/…`) | Thay đổi |
|---|---|
| `gamecore/KMissle.h` | 6 biến vị trí vẽ (`m_nRndPrev/Cur/DrawX,Y`) và 2 mốc nhịp |
| `gamecore/KMissle.cpp` | `KMissle::Paint`: khi đạn đang bay (`MS_DoFly`) và đang trong pha vẽ, phát hiện vị trí logic vừa đổi, đặt đoạn nội suy từ vị trí đang vẽ tới vị trí mới, vẽ theo `g_fNpcRenderAlpha` |
| `network/SocketClient.cpp` | Vòng nhận khi đã kết nối: `usleep(10000)` → `usleep(2000)` |

**Nội suy đạn – chi tiết:**
- Chỉ đổi tọa độ truyền vào `m_MissleRes.Draw`; vị trí logic, hướng, va chạm, sát thương cục bộ, thời gian sống không đổi.
- Không nội suy (vẽ đúng vị trí logic) khi: đạn mới tạo, đạn không được vẽ ở nhịp trước, lệch hơn 96 đơn vị, trạng thái chờ/va chạm/tan.
- Dùng chung hệ số alpha với NPC nên đạn và thân cùng "trễ" như nhau, không lệch pha.
- Không cần sửa `Activate`/`OnFly` (nhiều nhánh thoát) vì việc phát hiện đổi vị trí làm ngay trong `Paint`.

**Giữ nguyên từ 31/33 (đã kiểm còn trong thư viện):** `KNpc::UpdateRenderPos`, xử lý gói mỗi khung, giới hạn joystick, `MoveGuardTick`, `ClearJoystickPendingMove`, log `JXFIX`, `TCP_NODELAY`.

## 3. Kiểm thử
- **Build:** như báo cáo 33 (`ANDROID_USER_HOME=D:\Android\user`), `BUILD SUCCESSFUL in 3m 5s` (`D:\Android\b\build-fix34.log`), 0 lỗi ở file đã sửa.
- **APK:** `com.jxclient.hoiuctruyenky` versionCode 17, `arm64-v8a`, chữ ký `a48601f7…f2d7` (cài đè được); so với fix33 chỉ khác `libMyGame.so`; `package.ini` giống.
- **Mô phỏng đạn** (`docs-analysis/patches/test_34_missile_interp.py`): **7/7 đạt** – khung đầu vẽ đúng vị trí logic kể cả khi bộ nhớ slot là rác; vị trí vẽ không lùi, không vượt logic, trễ < 2 bước và không tích lũy với tốc độ 1, 7, 24, 40 ở 60 và 120 FPS; số vị trí vẽ > 2 lần số nhịp; nhảy xa và không vẽ nhịp trước thì "nhảy"; trạng thái không bay giữ nguyên; logic không bị đổi.
- **Hồi quy fix33** (`test_33_skill_guard.py`): **9/9 đạt** (không file nào của cơ chế lệnh bị sửa trong đợt 34).
- Trong lúc làm: một kiểm thử trượt do ngưỡng "trễ ≤ 1 bước" tôi đặt sai với thiết kế "đi tiếp từ vị trí đang vẽ"; đã sửa ngưỡng kiểm thử thành "< 2 bước, không tích lũy" (mã client không đổi).
- **Điện thoại/emulator:** không có. Chưa xác nhận bằng mắt: đạn mượt, không lệch tay nhân vật khi bắn, FPS, nhiệt/pin, và việc fix33 vẫn đúng trên máy thật với bản 34.

## 4. So sánh trước và sau
| Thành phần | APK gốc | fix31 | fix33 | **fix34** |
|---|---|---|---|---|
| Vị trí nhân vật/NPC/quái | 18 lần/giây | nội suy mỗi khung | + không giật lùi khi server sửa | giữ |
| Camera | 18 lần/giây | mỗi khung | giữ | giữ |
| Tên, máu, hiệu ứng trên người | 18 lần/giây | bám thân | giữ | giữ |
| Đạn/projectile | 18 lần/giây | 18 lần/giây | 18 lần/giây | **nội suy mỗi khung** |
| Khung hoạt ảnh | ≤ 18/giây | giữ | giữ | giữ |
| Xử lý gói nhận | mỗi 0,1 s | mỗi khung | giữ | giữ; luồng nhận dò mỗi 2 ms |
| Gói lên server | Nagle | Nagle | `TCP_NODELAY` | giữ |
| Lệnh joystick | mỗi khung (≈ 60/s) | 9-18/s | + hoãn sau kỹ năng | giữ |
| Kỹ năng khi đang chạy được server thực thi (mô phỏng, RTT 150 ms) | 0% | 44% | 100% (người dùng đã xác nhận trên máy) | giữ |

## 5. Đánh giá 36 Hz
**Kết luận: không dựng bản 36 Hz trong đợt này; không nên làm nếu mục tiêu là cảm giác mượt.**

Dữ kiện đo được (mã nguồn server `Core/Src` + `MultiServer/GameServer`, dữ liệu `gs\Settings`, `gs\script`):
| Hạng mục phụ thuộc nhịp | Số liệu |
|---|---|
| Hằng số nhịp trong mã server | `GAME_FPS 18` (2 chỗ), `FRAME2TIME 18`, `GAME_UPDATE_TIME 10`; 24 dòng dùng trực tiếp; 87 dòng có số 18 viết thẳng; 19 chỗ `… % N` theo bộ đếm nhịp; 113 dòng dùng mốc `m_dwCurrentTime` |
| Client | `18` viết thẳng trong vòng `Breathe`, `/18`, `18*60` (`CoreShell.cpp`, `KPlayer.cpp`), bản sao logic `KNpc`/`KMissle`/`KSkill` |
| `skills.txt` | 1.721 dòng; cột theo nhịp `WaitTime`, `TimePerCast`, `TimePerCastOnHorse`, `FlyEventTime` |
| `missles.txt` | 462 dòng; `Speed`, `LifeTime`, `DmgInterval`, `Zspeed`; **24% `Speed` là số lẻ** (nhỏ nhất 1) |
| `npcs.txt` | 2.436 dòng; `WalkSpeed`/`RunSpeed` (**13% lẻ**, nhỏ nhất 2), `StandFrame`, `WalkFrame`, `RunFrame`, `HurtFrame`, `DeathFrame`, `ReviveFrame`, `AttackSpeed`, `CastSpeed`, `LifeReplenish`, `AIMaxTime` |
| Lua | 4.029 file; 952 dòng có hệ số 18; 1.607 dòng (458 file) dùng hệ số 18 hoặc hàm hẹn giờ/trạng thái theo nhịp |
| Giao thức | 16 trường trong `KProtocol.h` mang giá trị theo nhịp (thời gian trạng thái, `nWaitTime`, khung thế giới, tốc độ) |
| Dữ liệu client | Bản sao các bảng nằm trong 40 file pak (3.248 MB) trên CDN |
| Công cụ | Máy thật có Visual Studio 2022/2026; dự án server dùng toolset v100/v140, 34 file `.lib` kèm theo; **chưa từng dựng lại**, chưa biết mã nguồn có khớp `gs001.exe` đang chạy |

Vì sao không khả thi an toàn:
1. **Giữ nguyên thời gian thực đòi hỏi đổi dữ liệu, không chỉ đổi hằng số.** Mọi tốc độ là số nguyên "đơn vị/nhịp": ở 36 Hz phải chia đôi, nhưng 13-24% giá trị là số lẻ (có giá trị 1) → hoặc đổi tốc độ thật (thay đổi gameplay), hoặc phải viết lại phép di chuyển sang đơn vị nửa bước ở cả server lẫn client. Mọi số khung (động tác, hồi chiêu, thời gian sống đạn, trạng thái) phải nhân đôi ở 3 bảng và gần 1.000 dòng Lua, không sót chỗ nào.
2. **Server phải dựng lại từ mã nguồn chưa kiểm chứng.** Nếu mã nguồn lệch exe đang chạy, bản 36 Hz còn mang theo khác biệt không biết trước; không tách được lỗi do 36 Hz với lỗi do lệch mã.
3. **Client và dữ liệu client phải đổi đồng bộ** (APK mới + pak mới + CDN riêng), vì client tự mô phỏng cùng công thức.
4. **Giao thức mang giá trị theo nhịp** → client 36 Hz không nói chuyện được với server 18 Hz và ngược lại; cần server thử nghiệm riêng, VM riêng (hai VM hiện có trùng MAC/IP, không chạy song song được), DB riêng để không đụng dữ liệu nhân vật.
5. **Lợi ích thực tế nhỏ so với nội suy:** 36 Hz chỉ giảm trễ logic tối đa từ 55,6 ms xuống 27,8 ms; hình ảnh đã mượt theo tần số màn hình nhờ nội suy; khung hoạt ảnh vẫn bị giới hạn bởi số khung sprite. CPU server (một luồng) tăng gấp đôi.

Không tạo server 36 Hz nên server chính và dữ liệu không bị ảnh hưởng gì.

## 6. Đề xuất thay thế (chưa làm, cần quyết định)
| Đề xuất | Lợi ích | Điều kiện/rủi ro |
|---|---|---|
| A. Dựng lại `gs001` từ nguồn **giữ 18 Hz** trên VM thử nghiệm, so hành vi với exe hiện tại | Biết mã nguồn có dùng được không; mở đường cho B, C | Cần duyệt chạy exe tự dựng trong VM riêng |
| B. Server đẩy gói mỗi nhịp (18 thay 9 lần/giây): bỏ điều kiện `m_nGameLoop & 1` (`KSOServer.cpp:4378`) | Giảm trễ nhận tới 55 ms; không đổi gameplay, giao thức | Cần A |
| C. Sửa gốc lỗi một ô lệnh ở server (kỹ năng không bị lệnh chạy đè; kỹ năng tới khi đang ra chiêu được giữ 1 lệnh) | Hết mất kỹ năng kể cả với client cũ | Cần A |
| D. Yêu cầu chế độ quét cao (90/120 Hz) trên Android và điều tiết đúng theo `LimitFPS` | Hình mượt hơn trên máy 120 Hz | Sửa Java (`AppActivity`/`Cocos2dxRenderer`), phải thử trên máy thật; tốn pin, nóng |
| E. Client dự đoán dừng/đổi hướng cho nhân vật mình (giảm cảm giác trễ khi ping cao) | Phản hồi nhanh hơn | Thay đổi cảm giác điều khiển, cần thử kỹ |

## 7. Giới hạn còn tồn tại
- Chưa thử fix34 trên điện thoại.
- Khung hoạt ảnh ≤ 18/giây; hiệu ứng tĩnh tại chỗ (va chạm, nổ) không cần nội suy.
- Hình trễ so với logic tối đa dưới 2 nhịp (khoảng 80-110 ms ở 60 FPS), không tích lũy.
- Server đẩy gói 9 lần/giây; kỹ năng liên tiếp sát nhau có thể bị server bỏ.
- Luồng nhận dò socket dày hơn (tối đa khoảng 500 lần/giây thay vì 200): CPU tăng không đáng kể, chưa đo pin.
- FPS thực trên máy, chế độ 90/120 Hz chưa kiểm.

## 8. Khôi phục
- Về fix33: `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Jx1CocoV3\docs-analysis\scripts\khoi_phuc_client_fix34.ps1`
- Về bản 31: thêm `-Ve31`; về bản gốc: thêm `-VeGoc`. Sau đó build lại APK nếu cần.
- Trên điện thoại: cài đè APK cũ hơn (cùng chữ ký, cùng versionCode): `…/apk/jx-tailscale-8080-fix33.apk` vẫn còn trên CDN.
- Sao lưu: `D:\Android\b\backup-tick\` (gốc, 7 file), `backup-fix33\` (trước 33), `backup-fix34\` (trước 34).

## 9. Đường dẫn
- **APK fix34:** `D:\Android\b\apk-fix34\jx-tailscale-8080-fix34.apk`, 78.917.739 byte, SHA256 `3164DBD11686495C06EE69BDD39BEEFF42EC19ED359CCB9176AE83F9AE533595`.
- **CDN (SHA256 khớp):** `C:\Jx1CocoV3\data_cdn\apk\jx-tailscale-8080-fix34.apk` → `http://<TAILSCALE-IP>:8080/apk/jx-tailscale-8080-fix34.apk`
- Giữ nguyên: APK gốc (`82674B16…`), fix31 (`DAB8485E…`), fix33 (`E9FB0DBF…`), khóa debug, CDN (PID 4612, không khởi động lại), server `JX-Server-D`.
