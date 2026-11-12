# 32 - Đối chiếu APK cũ và APK tối ưu nhịp: vì sao hiệu ứng kỹ năng "mới hơn, rõ hơn"

Ngày: 2026-11-11. Chỉ đọc mã nguồn và so sánh APK; không sửa source, không đổi APK, không đụng server.

APK cũ: `D:\Android\b\apk-cdn8080\jx-tailscale-8080.apk` (SHA256 `82674B16…`). APK mới: `D:\Android\b\apk-tick\jx-tailscale-8080-tick.apk` (SHA256 `DAB8485E…8338`). Mã client: `D:\Android\b\Client\Classes` (bản vá), bản gốc `D:\Android\b\backup-tick`. Mã server: `SwordOnline/.../Core/Src`.

## TÓM TẮT 5 DÒNG
1. Hai APK chỉ khác `lib/arm64-v8a/libMyGame.so`; từ lúc build APK cũ, chỉ 7 file đã vá thay đổi; **không file nào về hoạt ảnh/hiệu ứng** (`KSprControl`, `KNpcResVN::Draw`, `KMissle`, kỹ năng) bị sửa.
2. Nguyên nhân trực tiếp và mạnh nhất: **giới hạn gửi lệnh joystick**. APK cũ gửi `c2s_npcrun` mỗi khung (≈ 60/giây); server chỉ có **một ô lệnh mỗi nhân vật**, lệnh chạy đến sau ghi đè lệnh kỹ năng trước khi nhịp server chạy, nên nhiều kỹ năng bấm khi đang di chuyển **bị server bỏ**. APK mới chỉ gửi 9-18 lần/giây nên lệnh kỹ năng sống sót, server thực thi, và các hiệu ứng do server gửi về (buff/trạng thái, sát thương, quái trúng đòn, người khác thấy) **xuất hiện**.
3. Nguyên nhân phụ: xử lý gói mỗi khung giảm trường hợp lệnh kỹ năng của quái/người khác bị lệnh sau ghi đè trong cùng một đợt xử lý.
4. Nội suy làm hiệu ứng gắn trên nhân vật (vòng buff, hiệu ứng đặc biệt) di chuyển mượt theo thân và camera, nên trông "rõ hơn"; tốc độ hoạt ảnh **không đổi** (vẫn 1 khung/nhịp 18 Hz).
5. Chưa đo trên máy; kết luận dựa trên mã nguồn và so sánh file. Hiện tượng là trò chơi đang hoạt động **đúng hơn**, không phải thêm hiệu ứng mới.

**Cần tôi quyết định: không.**

## 1. Thay đổi trong `libMyGame.so`
- So sánh 962 file trong hai APK: chỉ `lib/arm64-v8a/libMyGame.so` khác CRC; `assets/` (gồm `package.ini`, dữ liệu hiệu ứng) giống hệt.
- File nguồn đổi kể từ APK cũ (09:44:29): đúng 7 file của bản vá (`KNpc.cpp/.h`, `KNpcRes.cpp/.h`, `KPlayer.cpp`, `CoreShell.cpp`, `vn/gamescence/KgameWorldVN.cpp`), giờ ghi 18:35-18:36. Không có file nào khác trong `Classes`.
- Không có thay đổi trong mã hoạt ảnh: `KSprControl::GetNextFrame` vẫn tăng 1 khung khi nhịp logic đổi (`gamecore/KSprControl.cpp:342-370`, so `SubWorld[0].m_dwCurrentTime`). Hiệu ứng trạng thái, hiệu ứng đặc biệt, hiệu ứng khung trong `KNpcResVN::Draw` vẫn dùng hàm này (`gamecore/KNpcRes.cpp:393-415`). Vì vậy **tốc độ hoạt ảnh không đổi** giữa hai APK.
- Thay đổi duy nhất ảnh hưởng tới vẽ: vị trí vẽ (`m_nXpos/m_nYpos` qua `SetRenderPos`, và `GetMpsPos` trong pha vẽ) cùng camera.

## 2. Luồng kích hoạt hiệu ứng kỹ năng
**Kỹ năng của chính mình:**
1. Bấm kỹ năng → `KCoreShell::UseSkill` hoặc `KPlayer` đặt lệnh cục bộ `Npc.SendSerCommand(do_skill, …)` và gửi `c2s_npcskill` (`gamecore/CoreShell.cpp:4939-4993`, `gamecore/KPlayer.cpp:492-512`).
2. Nhịp logic client kế tiếp: `KNpc::ProcCommand` → `DoSkill` tạo hoạt ảnh và đạn cục bộ (`gamecore/KNpc.cpp:850-888`).
3. Server: `NpcSkillCommand` đặt lệnh vào ô lệnh của nhân vật (`Core/Src/KProtocolProcess.cpp:5581-5607`); nhịp server kế tiếp thực thi, tính sát thương, áp trạng thái, rồi phát `s2c_skillcast` cho vùng (`Core/Src/KNpc.cpp:10520-10555`). Client **bỏ qua gói kỹ năng của chính mình** (`KPlayer::ConformIdx`, `gamecore/KPlayer.cpp:798-803`). Phần do server quyết (buff/trạng thái `s2c_syncstateeffect`, cờ trạng thái trong `s2c_syncnpcmin`, quái trúng đòn, máu) tới sau.

**Kỹ năng của quái và người khác:** `s2c_skillcast` → `NetCommandSkill` → `Npc.SendSerCommand(do_skill, …)` (`gamecore/KProtocolProcess.cpp:819-879`); thực thi ở nhịp client kế tiếp.

**Điểm mấu chốt:** cả client lẫn server, mỗi NPC chỉ có **một ô lệnh** `m_Command`; `SendSerCommand` ghi đè không điều kiện (`gamecore/KNpc.cpp:3522-3543`). Lệnh nào đến sau trong cùng một nhịp thắng.

## 3. Tần suất cập nhật sprite và animation
| Thành phần | APK cũ | APK mới |
|---|---|---|
| Khung hoạt ảnh nhân vật/hiệu ứng | 1 khung / nhịp logic (≤ 18/giây) | Không đổi |
| Vị trí vẽ nhân vật, NPC | đổi 18 lần/giây | nội suy mỗi khung render |
| Vị trí hiệu ứng gắn theo nhân vật (vòng buff, hiệu ứng đặc biệt, hiệu ứng khung) | theo `m_nXpos`, 18 lần/giây | theo `m_nXpos` nội suy, mỗi khung |
| Đạn/hiệu ứng bay (`KMissle`) | 18 lần/giây | Không đổi (không nội suy) |
| Camera | 18 lần/giây | mỗi khung |
| Xử lý gói nhận | mỗi 0,1 giây | mỗi khung |
| Gửi lệnh chạy khi giữ joystick | mỗi khung render (≈ 60/giây) | 9/giây (giữ hướng), ≤ 18/giây (đổi hướng) |

## 4. Đoạn code có thể làm hiệu ứng hiển thị khác trước
**A. Giới hạn joystick (trực tiếp, mạnh nhất).**
- APK cũ: `HRocker::updateMovement` chạy mỗi khung (`gamescene/KHRocker.cpp:587, 598-639`) → `KCoreShell::Goto` → `KPlayer::Walk` gửi `c2s_npcrun` **mỗi lần** (giới hạn đã bị comment, bản gốc `KPlayer.cpp:651`), và `Goto` đặt lại bộ đếm mỗi khung (bản gốc `CoreShell.cpp:5149`).
- Server ghi lệnh chạy (`KProtocolProcess.cpp:5481`) và lệnh kỹ năng (`:5603-5606`) vào cùng ô `m_Command`, chỉ thực thi 18 lần/giây. Với ≈ 3,3 gói chạy mỗi nhịp server, một gói kỹ năng chỉ được thực thi nếu nó là gói cuối cùng của nhịp đó → **phần lớn kỹ năng bấm khi đang giữ joystick bị bỏ ở server**.
- `HRocker` chỉ ngừng gọi `Goto` khi nhân vật đã ở trạng thái đánh (`KHRocker.cpp:619-624`); giữa lúc bấm kỹ năng và nhịp client kế tiếp, joystick vẫn gửi lệnh chạy, nên khoảng chồng lấn luôn tồn tại.
- APK mới: ≈ 0,5 gói chạy mỗi nhịp server khi giữ hướng → lệnh kỹ năng thường sống sót → server thực thi → buff/trạng thái (`s2c_syncstateeffect`, `StateInfo` trong `s2c_syncnpcmin`), máu quái, quái trúng đòn và hoạt ảnh kỹ năng mà **người khác** thấy (`s2c_skillcast`) giờ xuất hiện ở những lúc trước đây không có.
- Phía client của chính mình: lệnh cục bộ vẫn bị `Walk` ghi đè mỗi khung như cũ (bản vá giữ nguyên lời gọi cục bộ), nên hoạt ảnh tay/đạn cục bộ khi vừa chạy vừa bấm không đổi; cái thay đổi là phần hiệu ứng do server quyết định.

**B. Xử lý gói mỗi khung (phụ).**
- APK cũ xả hàng đợi mỗi 0,1 giây; server đẩy 9 lần/giây, nên khoảng 1 lần mỗi giây một lần xả gộp 2 đợt đẩy (4 nhịp sự kiện). Nếu trong đó có `s2c_skillcast` rồi lệnh đi/chạy của cùng NPC, lệnh kỹ năng bị ghi đè trước nhịp client → hoạt ảnh/hiệu ứng kỹ năng của quái/người khác mất.
- APK mới: mỗi đợt đẩy được xử lý riêng và nhịp client chạy giữa các đợt → ít mất hơn (vẫn mất nếu 2 lệnh nằm trong cùng một đợt đẩy, như cũ).

**C. Nội suy vị trí (cảm nhận "rõ hơn").**
- Vòng buff, hiệu ứng đặc biệt, hiệu ứng khung, tên và thanh máu vẽ theo vị trí nội suy (`KNpc::Paint` → `SetRenderPos`; `GetMpsPos` trong pha vẽ) và camera mượt → hiệu ứng bám thân, không giật 18 lần/giây.
- Đạn không nội suy: thân nhân vật có thể trễ tối đa 1 nhịp so với điểm phát đạn; có thể nhìn thấy khác trước ở kỹ năng bắn nhanh.

**D. Nhịp khung đều hơn (giả thuyết, chưa đo).**
- Xả gói theo lô 0,1 giây có thể gây khung chậm; khi một khung chạy bù nhiều nhịp, `GetNextFrame` chỉ tăng 1 khung/lần vẽ, nên hoạt ảnh hiệu ứng có thể bị cắt khi đạn hết thời gian sống (tính theo nhịp). Xả mỗi khung giảm đột biến → hiệu ứng có thể chạy đủ hơn. Chưa có số liệu FPS để chứng minh.

## 5. Thay đổi nào trực tiếp giải thích hiện tượng
| Cảm nhận | Thay đổi giải thích | Mức chắc chắn |
|---|---|---|
| "Kỹ năng có hiệu ứng mới" khi vừa di chuyển bằng joystick vừa bấm kỹ năng (buff/trạng thái hiện, quái trúng đòn, người khác thấy kỹ năng) | A: giới hạn joystick → server không còn ghi đè lệnh kỹ năng | **Cao** (mã client và server khớp; không đo) |
| Hoạt ảnh kỹ năng của quái/người khác xuất hiện đều hơn | B: xử lý gói mỗi khung | Trung bình |
| Hiệu ứng trên người "rõ, mượt" hơn | C: nội suy vị trí + camera | Cao về cơ chế; mức cảm nhận tùy người |
| Hiệu ứng chạy đủ khung hơn | D: nhịp khung đều | Thấp (giả thuyết) |

Không có thay đổi nào thêm dữ liệu hiệu ứng mới, đổi tốc độ khung hình hiệu ứng, đổi sát thương hay thời gian hồi chiêu.

## 6. Hệ quả cần lưu ý
- Nếu A đúng, APK mới làm **kỹ năng khi đang chạy được server thực thi nhiều hơn** → sát thương/tiêu hao mana thực tế khi vừa chạy vừa đánh cao hơn APK cũ. Đây là hành vi đúng thiết kế (APK cũ làm mất lệnh), nhưng là thay đổi cảm nhận gameplay.
- Lệnh kỹ năng cục bộ vẫn có thể bị `Walk` ghi đè trên client (không đổi so với cũ); có thể gây lệch: server đánh nhưng client không diễn hoạt ảnh tay. Chưa sửa (không trong phạm vi, không sửa source giai đoạn này).

## 7. Cách kiểm chứng (đề xuất, chưa làm)
1. Đứng yên bấm kỹ năng buff: hai APK phải giống nhau (A và B không áp dụng).
2. Giữ joystick chạy và bấm cùng kỹ năng buff 20 lần: đếm số lần biểu tượng/vòng buff xuất hiện trên APK cũ và mới; dự đoán APK mới cao hơn rõ.
3. Đếm gói lên: thêm (bản riêng) bộ đếm số gói theo giây vào `tcp_forwarder.py`, hoặc so tổng byte lên mỗi phiên trong `forwarder.log` khi chạy liên tục 30 giây bằng joystick.
4. Theo dõi console `gs001` hoặc log tiêu hao mana khi đánh trong lúc chạy.

## 8. Chưa đủ dữ liệu
- Chưa có log/đo trên máy về tỷ lệ kỹ năng bị bỏ ở server trước và sau.
- Không biết người chơi dùng joystick hay chạm bản đồ khi thấy khác biệt; nếu không dùng joystick thì A không áp dụng, B và C là nguyên nhân.
- Mã nguồn server có thể không khớp hoàn toàn với `gs001.exe` đang chạy (phần ô lệnh chưa đối chiếu mã máy).
