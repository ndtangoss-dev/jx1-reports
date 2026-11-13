# U003 – G1/G2: TRIỂN KHAI UNITY VÀ BUILD APK THỬ NGHIỆM ĐẦU TIÊN

Trạng thái: ĐÃ ĐƯỢC NGƯỜI DÙNG DUYỆT. Đây là nhiệm vụ triển khai tiếp theo sau báo cáo 58. Đọc báo cáo 58 và review 57 trước khi làm.

## 1. Tài liệu bắt buộc

Đọc:
- `JX1_VISUAL/REPORTS/U003_G07_58_g07-hit-attrib-cast-anchor-map-verification.md`
- `JX1_VISUAL/REPORTS/U003_G07_57_chatgpt-review-and-next-instructions.md`
- `JX1_VISUAL/REPORTS/U003_G06_56_hit-damage-combat-verification.md`
- `JX1_VISUAL/REPORTS/U003_G05_55_spr-ipotree-direction-skill375.md`
- `JX1_VISUAL/REPORTS/U003_G0_54_thiet-ke-kien-truc.md`
- `BAI_HOC.md`

Báo cáo 58 là kết quả xác minh mới nhất, thay thế kết luận cũ khi có mâu thuẫn. Tuân thủ thêm mọi ràng buộc trong `CLAUDE.md` và quy trình dự án hiện có.

## 2. Mục tiêu và ưu tiên

Chuyển U003 từ nghiên cứu sang Unity prototype độc lập, ưu tiên có APK đầu tiên chạy được trên Android để người dùng kiểm thử sớm. Không kéo dài nghiên cứu nếu điểm chưa rõ không chặn việc triển khai. Ghi rõ mọi giả định, giới hạn và phần chưa xác minh.

Làm tuần tự G1 rồi G2, nhưng không chờ toàn bộ tính năng hoàn thiện mới build. Khi có vertical slice đủ chạy, build APK thử nghiệm ngay.

## 3. Quyết định thiết kế đã duyệt

Áp dụng các quy tắc U003 sau:

1. Unity prototype độc lập, chưa tích hợp server.
2. Giữ nguyên Cocos client/server hiện tại làm baseline; không sửa U001/U002.
3. Ưu tiên asset JX1 gốc; không tự thay bằng đồ họa chung.
4. Quái đầu tiên ani001, HP thử nghiệm 1.000.
5. Skill 375 tạo 16 missile 181 theo lưới 4×4; giữ chuỗi hiệu ứng dẫn tới missile 193.
6. Missile 181 đứng tại vị trí sinh, không dựng chuyển động homing.
7. Missile 193 xuất hiện tại vị trí va chạm của 181.
8. Trong U003, 181 chỉ tạo hiệu ứng/kích hoạt chuỗi; không gây damage.
9. Mỗi AOE của 193 gây 20 damage tại +500ms và +1000ms tính từ lúc AOE được kích hoạt. Mỗi tick xét từng quái còn sống trong vùng.
10. AOE chồng lấn được cộng dồn; mỗi lần áp dụng damage tạo một damage number riêng.
11. Cast duration 1.000ms; cooldown 1.000ms tính từ lúc bắt đầu cast.
12. Mỗi lần cast có `castId` riêng; mỗi AOE có ID riêng để quản lý timer/sự kiện độc lập.
13. Dùng 18 tick/giây làm cấu hình logic ban đầu của U003. Đây là lựa chọn prototype, KHÔNG khẳng định Hz client gốc.
14. Độ trễ 16 missile giữ công thức RANDONORDER đã xác minh; dùng seed cố định trong chế độ test để tái hiện lỗi.
15. Không phát Hit/Wound cho skill 375; bỏ qua stun trong prototype đầu tiên.
16. Anchor ani001 dùng (160,192), đồng thời áp dụng offset từng frame từ SPR.
17. Dùng vùng map 45 x=96..107, y=95..102 (các Region_C.dat trong vùng này hiện có). Không dùng 18 vùng thiếu ở rìa.
18. Map 45 không có Tree; tạo cảnh test riêng có Tree để kiểm tra KIpoTree/Clone.

Nếu source hoặc runtime có mâu thuẫn với quyết định trên, không tự ý đổi luật gameplay. Ghi bằng chứng, ảnh hưởng và dừng riêng phần bị ảnh hưởng để báo cáo.

## 4. G1 – Unity foundation

### G1.1 Kiểm tra môi trường
Kiểm tra Unity Editor/version, Android Build Support, SDK/NDK/JDK, khả năng build APK, GPU/RAM/dung lượng và đường dẫn source/PAK/workspace/asset.

Không cài package, thư viện, model hoặc công cụ mới nếu chưa được duyệt. Nếu thiếu thành phần bắt buộc, báo tên, nguồn, dung lượng và lý do rồi chờ duyệt trước khi tải/cài.

### G1.2 Project riêng
- Tạo Unity project U003 độc lập tại `D:\JX1_U003`.
- Không tạo project trong `D:\JX1_U003_work`.
- Dùng Unity Editor 6000.2.14f1 nếu môi trường hỗ trợ.
- Không ghi đè U001/U002; giữ nguyên workspace, script phân tích và dữ liệu trích xuất hiện có.

### G1.3 Pipeline asset
Xây pipeline SPR → Unity hỗ trợ TYPE_FRAME, alpha/palette, frame offset và metadata. Lưu nguồn gốc PAK/entry cho từng asset. Không đưa PAK gốc vào APK; không sửa PAK/source gốc. Chỉ xử lý asset cần cho vertical slice: ani001, nhân vật, missile 181/193, hiệu ứng, damage font, joystick và map. Không cần quét toàn bộ spr.pak nếu không có lý do cụ thể.

### G1.4 Animation
Triển khai ani001 (idle, walk, hit, death và action cần thiết), nhân vật 8 hướng, mapping hướng logic → sprite theo báo cáo 55. Giữ frame timing, anchor/offset và alpha; không méo hình, đổi màu hoặc tự thay trang phục. Không nội suy AI/tăng frame trong giai đoạn này.

### G1.5 Map/render
- Dựng vùng map 45 x=96..107, y=95..102.
- Áp dụng chuyển đổi MPS/Region/screen theo báo cáo 58 và điểm chân runtime y+6 MPS.
- Port KIpoTree sang C#, không dùng Y-sort đơn giản làm giải pháp cuối.
- Giữ các lớp ground/cover/object/above/in-front theo kiến trúc đã nghiên cứu.
- Tạo cảnh test riêng có Tree để kiểm tra Tree/Line/Point/Clone và che khuất.
- Nếu chưa port đầy đủ nhánh nào, đánh dấu chính xác nhánh đã chạy/chưa chạy.

**Nghiệm thu G1:** Unity mở được scene; nhân vật và ani001 hiển thị đúng hướng/anchor; map render được; có test che khuất cơ bản. Lưu ảnh và log.

## 5. G2 – APK thử nghiệm đầu tiên

### G2.1 Quái và bản đồ
- 15 điểm spawn cố định trong vùng chơi; tối đa 15 quái sống.
- Quái chết hồi sinh sau 2 giây.
- HP quái 1.000.
- Dùng ani001 và action đã xác minh.
- Có thanh HP hoặc cách quan sát HP rõ ràng.

### G2.2 Nhân vật
- Nhân vật xuất hiện trên bản đồ.
- Joystick di chuyển, 8 hướng.
- Tự động tấn công có nút bật/tắt.
- HP nhân vật 500.

### G2.3 Skill Lôi Động Cửu Thiên
- Có nút kích hoạt.
- Cast 1 giây, cooldown 1 giây từ lúc bắt đầu cast.
- Tạo 16 missile 181 theo lưới 4×4 và độ trễ đã xác minh.
- 181 đứng tại vị trí sinh, dùng asset/hiệu ứng gốc.
- Khi điều kiện chuỗi va chạm được thỏa mãn, tạo 193 tại vị trí tương ứng.
- Mỗi 193 tạo AOE độc lập.
- Mỗi AOE gây hai tick 20 damage ở +500ms/+1000ms.
- AOE chồng lấn cộng dồn.
- Mỗi damage event tạo một số damage riêng, bay lên và tồn tại 1 giây.
- Timer/damage không phụ thuộc FPS render.
- Dùng castId/AOE ID để truy vết.

Nếu mô phỏng collision U003 khác source gốc, ghi rõ khác biệt. Không âm thầm đổi quy tắc.

### G2.4 Debug overlay
Hiển thị FPS, quái sống/chết, HP nhân vật/quái, tổng damage, số cast, số 181/193 đang hoạt động, số AOE, cast ID gần nhất, tọa độ và timer hồi sinh, logic tick. Có thể tắt overlay khi đánh giá hình ảnh.

### G2.5 Build
- Build APK debug/development ngay khi vertical slice đủ chạy.
- Ghi Unity version, Android target và cấu hình build.
- Kiểm tra APK tồn tại, dung lượng, SHA256.
- Cài/chạy trên emulator hoặc thiết bị nếu có thể.
- Không tuyên bố đã test điện thoại thật nếu chưa cài/chạy thật.
- Chuẩn bị chuyển APK qua Tailscale/Taildrop; không mở cổng Internet công khai.
- Nếu thiếu Android toolchain, báo blocker và chờ duyệt cài đặt.

**Nghiệm thu G2:** APK cài được, vào scene, điều khiển nhân vật, thấy quái, kích hoạt skill và quan sát damage. Ghi rõ tính năng chưa hoàn thiện.

## 6. Nguyên tắc an toàn và triển khai

- Làm tuần tự G1.1 → G1.5 → G2; ưu tiên vertical slice chạy được.
- Sau mỗi mốc chạy test, lưu log và ảnh.
- Chủ động điều tra/sửa lỗi trong phạm vi nhiệm vụ.
- Không dùng dữ liệu giả để báo cáo test thành công.
- Có thể tạo code/script mới trong project U003.
- Không sửa source client/server gốc, PAK gốc, U001/U002.
- Không thao tác VM, database, Goddess hoặc EXE server.
- Không cài công cụ/model/package mới nếu chưa được duyệt.
- Không xóa/ghi đè dữ liệu cũ, không reset/clean.
- Nếu có nguy cơ mất dữ liệu hoặc ảnh hưởng hệ thống đang chạy, dừng và hỏi người dùng.

## 7. Báo cáo bắt buộc

Tạo:
- `JX1_VISUAL/REPORTS/U003_G1_59_unity-foundation-report.md`
- `JX1_VISUAL/REPORTS/U003_G2_60_first-playable-apk-report.md`

Mỗi báo cáo phải ghi:
1. Mục tiêu và trạng thái NOT STARTED / IN PROGRESS / COMPLETED / BLOCKED.
2. Đã làm gì; file/thư mục tạo hoặc sửa.
3. Class/component/scene/hàm chính.
4. Lý do kỹ thuật cho quyết định quan trọng.
5. Phần nào theo source gốc, phần nào là luật U003.
6. Phần hoàn thành, chưa hoàn thành, lược giản.
7. Lệnh build/test và kết quả thực tế.
8. Ảnh Unity Editor/APK và log liên quan.
9. Lỗi gặp phải, nguyên nhân và cách sửa.
10. Hiệu năng/FPS/RAM nếu đo được.
11. APK path, dung lượng, SHA256 nếu đã build.
12. Giới hạn/rủi ro còn tồn tại.
13. Bước tiếp theo và lý do.

Phải phân biệt rõ: code đã viết; project mở được; build thành công; APK cài được; APK chạy được; APK đã test trên thiết bị thật. Không gộp các trạng thái này thành một chữ "hoàn thành".

## 8. GitHub và bàn giao

- GitHub reports là nguồn chính thức theo dõi tiến độ.
- Commit/push báo cáo và source U003 cần thiết theo cấu trúc repo.
- Không đẩy PAK, APK, asset thô, binary lớn hoặc dữ liệu nhạy cảm vào repo báo cáo.
- APK lưu ngoài repo và cung cấp đường dẫn/Tailscale.
- Chỉ stage file thuộc nhiệm vụ; không stage file sửa dở hoặc dữ liệu ngoài phạm vi.
- Không reset, clean, force push. Nếu conflict, dừng và báo cáo.
- Sau mỗi mốc cung cấp commit SHA, danh sách file và link báo cáo.

## 9. Dừng và bàn giao

Sau G1, nếu có thể tiếp tục G2 an toàn thì tiếp tục, không chờ duyệt lại vô ích. Khi có APK đầu tiên, bàn giao APK và báo cáo để người dùng cài thử. Dừng trước mọi hành động vượt phạm vi hoặc có rủi ro cần phê duyệt.

Mục tiêu là có U003 đầu tiên chạy được trên Android để người dùng đánh giá, không phải chỉ có project/code chưa kiểm chứng.
