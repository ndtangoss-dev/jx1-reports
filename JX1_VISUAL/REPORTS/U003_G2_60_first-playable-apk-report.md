# U003 G2 – Báo cáo APK thử nghiệm đầu tiên (nhiệm vụ 59)

**Trạng thái G2: PARTIAL.** Code ✔ · project biên dịch ✔ · build Windows ✔ · chạy Windows ✔ (tự kiểm tra) · **build APK ✔** · **APK cài được ✘ (chưa thử) · APK chạy được ✘ (chưa thử) · test trên điện thoại thật ✘**. Chưa tuyên bố nghiệm thu G2: cần người dùng cài thử.

## 1. Mục tiêu
Vertical slice: map 45, 15 quái ani001 (HP 1.000, hồi sinh 2 s), nhân vật 8 hướng (HP 500), joystick, tự đánh bật/tắt, skill 375, damage number, debug overlay, APK.

## 2. Đã làm
- **Quái:** 15 điểm spawn cố định (lưới 5×3 quanh tâm vùng chơi, lệch cố định seed 12345, cách ~520×760 MPS); tối đa 15 sống; chết → hồi sinh sau 2 s tại điểm spawn; thanh HP trên đầu.
- **Nhân vật:** joystick (ảnh gốc `yaoganz/x`), 8 hướng, HP 500, nút AUTO bật/tắt (mặc định bật). Tự đánh: tìm quái gần nhất trong 650 px, dùng skill khi sẵn sàng và trong 320 px, ngược lại tiến tới đánh thường (30 dmg/1 s, Hit 65% theo công thức server, BC 58 mục A2). Quái đuổi trong 230 px, đánh 8 dmg/1,5 s (**các số này là giả định chưa được duyệt**, BC 54 mục G còn mở).
- **Skill Lôi Động Cửu Thiên** (`Skill375.cs`): nút + icon gốc, cast 1,0 s, cooldown 1,0 s tính từ lúc bắt đầu cast, mỗi lần có `castId`, mỗi AOE có `aoeId`. Tại 60% cast (0,6 s – áp dụng quy tắc `IsReachFrame(60)` của gốc, **giả định** cho cast 1 s) sinh 16 đạn 181 lưới 4×4 ô 32×32 MPS quanh mục tiêu; độ trễ `2+5k+(+rand(5) | −rand(2))` tick, 18 tick/s, seed cố định ở chế độ test; 181 đứng yên, sống 12 tick, va chạm khi có quái trong ±2 ô → nổ Bz_dian3 + sinh 193 tại vị trí 181 sau 5 tick; 181 **không gây damage**; mỗi 193 là AOE độc lập vùng 3×3 ô, 2 tick 20 dmg tại +500 ms/+1000 ms từ lúc kích hoạt, cộng dồn khi chồng lấn; mỗi lần áp dụng sinh một damage number riêng (font `number_16_r` gốc, bay lên 40 px, sống 1 s).
- **Mô phỏng** bước cố định 1/60 s, không phụ thuộc FPS render.
- **Overlay (G2.4):** FPS, tick 18 Hz, quái sống/chết/hồi sinh, HP người và quái gần nhất, tổng damage, số cast/castId, số 181/193/AOE, damage đang bay, tọa độ MPS/ô; nút DBG tắt overlay.

## 3. Lớp chính
`Game`, `Skill375` (`BeginCast/Step/AoeTick`), `Monster`, `PlayerChar`, `GameUI`, `AutoTest`.

## 4. Lý do kỹ thuật
Timer theo giờ mô phỏng tuyệt đối (không đếm khung render); tick AOE xử lý bằng so sánh thời điểm ở mỗi bước 1/60 s nên FPS thấp không mất tick; IMGUI + `Input` cũ để tránh thêm package.

## 5. Gốc hay U003
Gốc (nguồn, BC 58): chuỗi 375→16×181→va chạm→193, vị trí 193 = vị trí 181, trễ RANDONORDER, 181 đứng yên, 5×5 ô va chạm, 3×3 ô vùng sát thương, không Hit cho 375. **Khác gốc (U003, đã duyệt):** 181 không gây damage; 2 tick 500/1000 ms × 20; cast/cooldown 1 s; stun bỏ qua; damage number tách riêng. Gốc gây sát thương tức thì khi 181 va chạm (+ một lần từ 193) – **không** làm theo.

## 6. Hoàn thành / chưa / lược giản
- ✔ các mục G2.1–G2.4 chạy trong bản Windows.
- ✘ APK chưa cài/chạy (không có thiết bị/emulator kết nối ADB: `adb devices` rỗng).
- ✘ Chưa chuyển APK qua Taildrop (chỉ chuẩn bị; không mở cổng Internet).
- Lược giản: không vật cản; không âm thanh; không nút bật tắt hit; không hồi sinh quái theo AI phức tạp; người chơi chết → hồi sinh sau 3 s tại chỗ (giả định); cooldown overlay là hình chữ nhật co theo thời gian.

## 7. Lệnh build/test và kết quả thật
- `-executeMethod U003Ed.U003Build.BuildAndroid` (IL2CPP, ARM64, minSdk 24, Development, keystore debug mặc định) → `Build Succeeded`, 0 lỗi, 1 phút 46 s.
- Bản Windows chạy `U003_AUTOTEST`, cast tay 1 lần, quái đứng yên, seed cố định:
  `spawned181=16 collided=16 spawned193=16 damageEvents=18 totalDamage=360 (18×20) HP quái 15000→14640 dmgNumbersSpawned=18` – số damage riêng khớp số lần áp dụng; sinh 193 đúng 16. Có 18 chứ không phải 32 sự kiện vì 16 AOE chỉ chồng lên một con hổ, 9 AOE phủ được con đó × 2 tick (cộng dồn đúng quy tắc). Kết quả lặp lại giữa hai lần chạy cùng seed là chưa kiểm hết.
- **Chưa làm:** kiểm tick AOE ở FPS 15/30/60/144; test dài hạn; test khi mất focus.

## 8. Ảnh/log
Cục bộ: `D:\JX1_U003_work\shots3\g2_01..05_*.png`, `autotest_result.txt` (có nhật ký sự kiện từng castId/aoeId). Không đẩy lên repo công khai (chứa asset game).

## 9. Lỗi và cách sửa
Đạn 181 lúc đầu lặp theo `interval` header (50 ms); dữ liệu gốc `6,1,2` nghĩa là 2 tick/khung → sửa thành `LogicHz/2`. Phần còn lại xem báo cáo 59.

## 10. Hiệu năng
Windows (960×540): 52–60 FPS, GC ~7 MB. **Android chưa đo.**

## 11. APK
- Đường dẫn: `D:\JX1_U003_build\android\JX1_U003_debug.apk` (ngoài repo)
- Dung lượng: 30.604.847 byte
- SHA256: `dfbc9020097e62bf17ea62f4ff45284d48698ce4c9a905ea691ab551ab9ae808`
- Cấu hình: Unity 6000.2.14f1, IL2CPP, ARM64, minSdk 24, Development build, `com.u003.jx1proto`, ký bằng keystore debug.
- Lưu ý: APK dựng trước khi tôi chỉnh kịch bản `AutoTest` (chỉ chạy khi có biến môi trường, không ảnh hưởng chơi).

## 12. Giới hạn/rủi ro
Chưa biết APK chạy trên điện thoại (RAM, FPS: ~6.800 sprite, atlas RGBA32 không nén); IMGUI trên màn hình lớn; Y-sort thay KIpoTree; giả định chiến đấu chưa duyệt; dữ liệu asset gốc nằm trong APK (chỉ để dùng nội bộ, không phát tán).

## 13. Bước tiếp theo
Người dùng cài thử APK (Taildrop qua Tailscale, bật "cài ứng dụng không rõ nguồn") và báo FPS/lỗi; sau đó port KIpoTree và đối chiếu ảnh client gốc.
