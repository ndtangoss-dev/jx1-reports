# LỆNH TRIỂN KHAI CHO CLAUDE CODE – PHASE 46

**Trạng thái:** ĐƯỢC NGƯỜI DÙNG CHỐT – BẮT ĐẦU THỰC HIỆN  
**Prompt yêu cầu chính:** [PHASE_46_FIX_MAP_STUTTER_AND_SKILL_36_TICK.md](PHASE_46_FIX_MAP_STUTTER_AND_SKILL_36_TICK.md)

## 1. Lệnh thực hiện

Claude Code, hãy nhận nhiệm vụ Phase 46 và bắt đầu triển khai theo prompt chính ở liên kết trên. Đây là công việc đã được người dùng duyệt, không phải bản nháp để tiếp tục hỏi duyệt.

Đọc toàn bộ prompt Phase 46 trước khi thao tác. Đồng thời đọc trạng thái mới nhất và các báo cáo Fix gần nhất trong repository để hiểu chính xác nền tảng hiện tại. Không suy luận trạng thái máy/VM chỉ từ báo cáo cũ; phải xác minh trạng thái thực tế trước khi thao tác.

## 2. Thứ tự thực hiện bắt buộc

### Giai đoạn 0 – Xác minh môi trường và bảo vệ dữ liệu
1. Xác định đang chạy trên máy công ty hay máy nhà; kiểm tra đường dẫn source, build tools, LDPlayer/ADB và quyền truy cập.
2. Đọc 00_LATEST_STATUS.md, báo cáo Fix36 và các tài liệu liên quan đến Server 36Hz.
3. Xác minh chính xác VM thử nghiệm, cấu hình hiện tại, tiến trình/server đang chạy và kết nối. Tuyệt đối không nhầm hoặc can thiệp Main VM.
4. Không dừng, khởi động lại, sửa cấu hình hoặc ghi dữ liệu lên Main VM.
5. Tạo/kiểm tra backup và ghi nhận trạng thái ban đầu. Không commit source chính nếu người dùng chưa yêu cầu.

Nếu thiếu quyền truy cập hoặc không thể thao tác trên máy/VM từ môi trường hiện tại, báo cáo chính xác giới hạn; không giả vờ đã chạy test hoặc sửa máy.

### Giai đoạn 1 – Haiku chuẩn bị nhân vật và tái hiện lỗi
1. Phân công Haiku làm QA, đọc log và thu thập bằng chứng; Opus làm developer, phân tích và sửa code.
2. Haiku làm đúng quy trình chuẩn bị nhân vật trong prompt Phase 46:
   - Lễ Quan Ba Lăng Huyện: 203/199.
   - Nhận cấp 200, kỹ năng 15x, các loại điểm, tiền vàng và tiền xu qua lệnh bài GM.
   - Học trò thợ rèn: 198/197; mua mỗi loại vũ khí cần thiết một món.
   - Sau khi nhận tiền, nhấn biểu tượng Bảo Vật riêng nằm cạnh bánh răng phía trên màn hình (không mở bánh răng), mua Thần Hành Phù và ngựa nếu chưa có.
   - Dùng Thần Hành Phù đến Phong Lăng Độ, lên ngựa, mở minimap, tìm 162/186, nhấn Tìm tọa độ rồi Đóng; quan sát màn hình chính khi nhân vật di chuyển.
3. Ghi lại bằng chứng tái hiện: video/ảnh nếu hỗ trợ, log, FPS, frame time, số frame >40ms và >=100ms, thời điểm và điều kiện xảy ra giật.
4. Không bỏ qua bài test chỉ vì không tìm được vật phẩm/kỹ năng. Ghi rõ chỗ bị chặn, thử xác định nguyên nhân trong phạm vi an toàn và báo cáo.

### Giai đoạn 2 – Điều tra và sửa lỗi giật bản đồ
1. Haiku cung cấp kết quả tái hiện cho Opus.
2. Opus phân tích nguyên nhân gốc bằng log và code; không mặc định Fix36 removeUnusedTextures() là nguyên nhân duy nhất.
3. Kiểm tra camera/map scrolling, map/tile rendering, texture/cache/loading, cấp phát bộ nhớ, main/render thread, tác vụ định kỳ, packet và đồng bộ vị trí.
4. Sửa theo nguyên nhân có bằng chứng, giữ nguyên gameplay và chất lượng hình ảnh.
5. Build APK; Haiku chạy lại đúng kịch bản chuẩn và kiểm thử mở rộng.
6. Nếu còn giật, tiếp tục vòng điều tra–sửa–test. Không tuyên bố triệt để khi chưa đạt tiêu chí.

### Giai đoạn 3 – Nâng projectile/skill effect lên 36 tick
1. Opus tách bạch server logic tick, client logic tick, projectile update tick, effect update tick, sprite frame rate và render FPS.
2. Xác định chính xác các thành phần còn bị giới hạn 18Hz.
3. Ưu tiên xử lý client-side nếu đáp ứng được mục tiêu và không cần đổi server.
4. Nâng cập nhật chuyển động projectile và hiệu ứng kỹ năng lên 36 tick/giây; dùng delta time/nội suy đúng cách, không phụ thuộc FPS cố định.
5. Không làm thay đổi tốc độ bay, sát thương, thời điểm va chạm, cooldown, thời gian thi triển hoặc lifetime của hiệu ứng.
6. Haiku kiểm thử kỹ năng tầm xa, đường bay dài/ngắn, nhiều projectile, AOE, hiệu ứng va chạm/nổ, combo nếu có; thử cả đứng yên và vừa di chuyển vừa dùng kỹ năng.
7. Đo nhịp update thực tế. Nếu sprite chỉ có 18 frame hình ảnh/giây, phải ghi rõ 36Hz là tần suất cập nhật chuyển động, không được quảng cáo thành 36 hình ảnh khác nhau mỗi giây.

### Giai đoạn 4 – Tích hợp và hồi quy
1. Tích hợp hai nhóm thay đổi có kiểm soát; tránh sửa đồng thời cùng file/hàm.
2. Haiku kiểm thử lại map stutter và projectile/effect sau khi tích hợp.
3. Kiểm tra đăng nhập, HUD, di chuyển, đánh quái/sát thương, kỹ năng, chuyển bản đồ, crash và hiệu năng.
4. Giữ Server 36Hz làm nền tảng chính. Không tự quay về 18Hz để né lỗi.
5. Nếu cần thay đổi server, phải chứng minh lý do và kiểm tra tương thích giao thức; không ảnh hưởng Main VM.

### Giai đoạn 5 – Bàn giao
Tạo báo cáo Phase 46 và cập nhật 00_LATEST_STATUS.md sau khi có kết quả thực tế. Báo cáo phải có:
- Nguyên nhân gốc và bằng chứng lỗi giật.
- Các bước tái hiện, bản đồ/điều kiện test.
- Danh sách file/code thay đổi và lý do.
- Số liệu trước/sau: FPS, frame time, >40ms, >=100ms, đỉnh giật.
- Kết quả đo projectile/effect 36 tick và kiểm thử từng nhóm kỹ năng.
- Kết quả hồi quy, lỗi còn tồn tại và giới hạn kiểm thử.
- Đường dẫn backup, diff, log, APK và SHA256.

Không ghi “đã hoàn thành” nếu chỉ mới phân tích, sửa code hoặc build. Phân loại rõ: ĐÃ XÁC MINH / CHƯA KIỂM THỬ / BỊ CHẶN / GIẢ THUYẾT.

## 3. Quy tắc giao tiếp và tự chủ
- Tự làm các thao tác kỹ thuật thông thường nếu máy và quyền truy cập cho phép: mở LDPlayer, ADB, lấy log, thao tác game, sửa code, build và test.
- Không yêu cầu người dùng chạy lệnh/copy log nếu Claude có thể tự lấy.
- Không hỏi duyệt lại các bước đã được prompt cho phép.
- Chỉ hỏi người dùng khi cần xác nhận hành động rủi ro, có thể mất dữ liệu, ảnh hưởng Main VM, hoặc cần quyết định ngoài phạm vi.
- Nếu thiếu quyền/không truy cập được thiết bị, tiếp tục các phần phân tích độc lập có thể làm được và nêu rõ phần bị chặn.
- Không tự commit source chính, không xóa backup, không ghi đè bản APK đã phát hành.
- Không đưa mật khẩu, token, cookie hoặc thông tin đăng nhập vào log/báo cáo.

## 4. Cách bắt đầu

Bắt đầu ngay bằng Giai đoạn 0, sau đó tiến hành Giai đoạn 1. Gửi báo cáo ngắn về môi trường đã xác minh và kết quả tái hiện đầu tiên; tiếp tục thực hiện các giai đoạn còn lại mà không chờ người dùng nhắc lại.

**Đây là lệnh triển khai chính thức cho Phase 46 theo nội dung người dùng đã duyệt.**