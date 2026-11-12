# PHASE 46 – FIX MAP STUTTER TRIỆT ĐỂ & NÂNG ANIMATION PROJECTILE/SKILL LÊN 36 TICK

## 1. Mục tiêu và kết quả người dùng đã xác nhận

Tiếp tục trên nền Client Fix36 và Server 36Hz.

Người dùng đã trực tiếp thử Server 36Hz và ghi nhận:
- Animation di chuyển của nhân vật mượt hơn.
- Hiện tượng giật màn hình/bản đồ khi di chuyển vẫn còn.
- Animation đường bay đạn và đường bay kỹ năng chưa có thay đổi rõ rệt.

Hai mục tiêu bắt buộc:
A. Haiku kiểm thử chuyên sâu để tái hiện, phân loại và tìm bằng chứng lỗi giật bản đồ; Opus tìm nguyên nhân gốc, sửa và phối hợp kiểm thử đến khi đạt.
B. Nghiên cứu và nâng nhịp cập nhật chuyển động/animation đường bay đạn và kỹ năng lên 36 tick/giây ở phía phù hợp, sau đó đo và cho người dùng so sánh.

Không chỉ tối ưu trên lý thuyết. Phải có kiểm thử thực tế, số liệu trước/sau và báo cáo. Không tuyên bố hoàn thành chỉ vì code đã sửa hoặc build thành công.

## 2. Phân công vai trò

### Haiku – QA chuyên sâu
- Tự vận hành game trên LDPlayer/thiết bị kiểm thử nếu môi trường hỗ trợ.
- Chuẩn bị nhân vật theo đúng quy trình mục 3.
- Tái hiện lỗi giật nhiều lần, ở nhiều bản đồ, tốc độ và trạng thái.
- Thu thập video/ảnh, log, FPS, frame time, thời điểm giật và thông tin CPU/bộ nhớ nếu có.
- Phân loại nguyên nhân có thể: render, camera, map streaming, texture, packet, đồng bộ vị trí, main-thread blocking hoặc nguyên nhân khác.
- Kiểm thử từng nhóm kỹ năng: tầm xa, nhiều projectile, đường bay dài/ngắn, AOE, va chạm/nổ, combo.
- Kiểm thử hồi quy sau từng bản sửa của Opus; báo cáo rõ điều kiện tái hiện và bằng chứng.

### Opus – Developer
- Đọc kết quả QA, phân tích nguyên nhân gốc.
- Kiểm tra và sửa mã nguồn Client Cocos2d-x, cùng server nếu thật sự cần.
- Build APK, xử lý lỗi build/chạy, phối hợp Haiku kiểm thử lại.
- Không sửa theo kiểu giảm chất lượng đồ họa, bỏ hiệu ứng hoặc che giấu lỗi bằng cách giảm tốc độ.
- Không thay đổi gameplay ngoài phạm vi đã phân tích.

Haiku tập trung QA/đọc lỗi; Opus phụ trách thay đổi code. Nếu cần sửa chung file/hàm, phải phối hợp tuần tự, tránh ghi đè hoặc xung đột.

## 3. Quy trình bắt buộc chuẩn bị nhân vật

Haiku không được bỏ qua bước chuẩn bị. Nhân vật cấp thấp, thiếu kỹ năng/trang bị và chỉ đi bộ bằng joystick sẽ không tái hiện đủ điều kiện kiểm thử.

### Bước 1 – NPC Lễ Quan tại Ba Lăng Huyện
Dùng chức năng tìm tọa độ trên minimap:
1. Mở minimap.
2. Nhập tọa độ **203/199**.
3. Nhấn **Tìm tọa độ**.
4. Nhấn **Đóng**.
5. Đến đúng NPC Lễ Quan và tương tác.

Tọa độ 203/199 là tọa độ chính xác của NPC Lễ Quan đã được người dùng trực tiếp xác minh. Không đoán hoặc thay bằng tọa độ khác.

Tại lệnh bài GM:
- Nhận các loại điểm theo giao diện.
- Nhận cấp độ 200.
- Vào lại phần chọn các loại điểm và nhận kỹ năng 15x.
- Nhận các loại điểm cần thiết.
- Nhận tiền vàng và tiền xu.
- Nhận ngựa trong lệnh bài GM nếu có mục nhận ngựa ở đó.

### Bước 2 – NPC Học trò thợ rèn
Dùng minimap:
1. Mở minimap.
2. Nhập tọa độ **198/197**.
3. Nhấn **Tìm tọa độ**.
4. Nhấn **Đóng**.
5. Đến đúng NPC Học trò thợ rèn, tương tác và mua mỗi loại vũ khí cần thiết một món để thử các chiêu thức.

Tọa độ 198/197 là tọa độ chính xác của NPC Học trò thợ rèn đã được người dùng trực tiếp xác minh.

### Bước 3 – Mua Thần Hành Phù và ngựa tại Bảo Vật
Sau khi đã nhận tiền vàng và tiền xu:
1. Quan sát thanh biểu tượng phía trên màn hình.
2. Nhấn biểu tượng **Bảo Vật nằm cạnh biểu tượng bánh răng**.
3. Không mở biểu tượng bánh răng để tìm Bảo Vật; Bảo Vật là biểu tượng riêng nằm bên cạnh bánh răng.
4. Tìm và mua **Thần Hành Phù**.
5. Tìm và mua **ngựa** nếu chưa nhận được ngựa từ lệnh bài GM.
6. Kiểm tra hành trang đã có Thần Hành Phù và ngựa.
7. Nếu không thấy vật phẩm hoặc không đủ tiền, kiểm tra số dư/danh mục và báo cáo nguyên nhân; không tự bỏ qua bước.

### Bước 4 – Di chuyển đến Phong Lăng Độ và tái hiện lỗi
- Sử dụng Thần Hành Phù để di chuyển đến Phong Lăng Độ.
- Lên ngựa để có tốc độ di chuyển đủ nhanh.
- Không chỉ dùng joystick đi bộ vì tốc độ chậm, khó quan sát lỗi.
- Mở minimap, nhập tọa độ **162/186**, nhấn **Tìm tọa độ**, sau đó nhấn **Đóng**.
- Quan sát màn hình chính trong lúc nhân vật di chuyển đến tọa độ này. Đây là kịch bản ưu tiên vì người dùng xác nhận tình trạng giật màn hình dễ quan sát nhất ở đây.
- Ghi hình/ghi log nếu công cụ hỗ trợ.

## 4. Nhiệm vụ A – Điều tra và xử lý lỗi giật bản đồ

Haiku phải kiểm tra:
- Di chuyển đường dài trên bản đồ.
- Cưỡi ngựa/tốc độ cao.
- Đổi hướng liên tục.
- Khu vực có nhiều NPC, quái vật và hiệu ứng.
- Qua ranh giới vùng/chuyển cảnh.
- Mở/đóng minimap khi đang di chuyển.
- Di chuyển liên tục đủ lâu để phát hiện lỗi theo chu kỳ.
- Kịch bản chuẩn Phong Lăng Độ, tọa độ 162/186.

Opus không được mặc định nguyên nhân vẫn là removeUnusedTextures() như Fix36. Phải xác minh lại bằng dữ liệu. Kiểm tra tối thiểu:
- Camera follow, camera update, map scrolling.
- Tile/map rendering, map streaming và nạp tài nguyên.
- Texture cache, texture loading/free, sprite batch, draw call.
- Bộ nhớ, cấp phát/giải phóng.
- Packet vị trí, đồng bộ nhân vật/NPC/quái.
- Main thread/render thread và tác vụ gây block.
- Tác vụ định kỳ trong lúc di chuyển.

Tìm tương quan giữa thời điểm giật với frame time, log, CPU/bộ nhớ, tải texture, hoạt động mạng và camera/map update.

### Tiêu chí hoàn thành A
- Xác định nguyên nhân gốc của các loại giật đã tái hiện, hoặc ghi rõ phần chưa xác định và bằng chứng còn thiếu.
- Có số liệu trước/sau: FPS, frame time, số frame >40ms, >=100ms, đỉnh giật và tần suất.
- Kịch bản chuẩn không còn khựng nghiêm trọng/có tính chu kỳ sau sửa.
- Không mất texture, NPC, quái, hiệu ứng hoặc nội dung bản đồ.
- Không crash, treo hoặc lỗi chuyển bản đồ.
- Không thay đổi tốc độ di chuyển/camera/gameplay ngoài chủ đích.
- Nếu vẫn còn giật, tiếp tục điều tra; không đánh dấu hoàn thành chỉ vì FPS trung bình cao.

## 5. Nhiệm vụ B – Cập nhật projectile và animation kỹ năng 36 tick

### Phân tích
Opus phải xác định riêng:
- Server logic tick.
- Client logic tick.
- Projectile/missile update tick.
- Skill effect update tick.
- Sprite animation frame rate.
- Render FPS.

Kiểm tra hàm update projectile/missile/effect, nội suy vị trí, thời điểm bắt đầu/kết thúc, thời gian tồn tại, va chạm và các giới hạn 18Hz còn tồn tại.

### Thực hiện
Mục tiêu là cập nhật chuyển động projectile và hiệu ứng kỹ năng theo nhịp 36 tick/giây nếu hiện tại đang bị giới hạn 18 lần/giây. Ưu tiên client-side nếu không cần đổi logic server.

Yêu cầu:
- Nội suy vị trí projectile theo thời gian thực.
- Cập nhật vị trí/trạng thái effect theo nhịp 36 tick.
- Không phụ thuộc cứng vào FPS thiết bị.
- Không làm thay đổi tốc độ bay thực tế, sát thương, thời điểm gây sát thương, điểm va chạm, cooldown hoặc thời gian thi triển.
- Không làm hiệu ứng chạy nhanh gấp đôi, lặp, mất hoặc sai thời gian tồn tại.
- Không làm giảm FPS hoặc gây thêm giật bản đồ.

Nếu sprite gốc chỉ có 18 frame hình ảnh/giây, phải phân biệt cập nhật chuyển động 36 tick với số frame hình ảnh thực tế. Không tuyên bố sprite animation đạt 36 FPS nếu asset không có đủ frame.

### Kiểm thử B
Haiku kiểm tra tối thiểu:
- Kỹ năng tầm xa có projectile.
- Đường bay dài và ngắn.
- Nhiều projectile.
- Kỹ năng AOE.
- Hiệu ứng va chạm/nổ.
- Combo/liên hoàn nếu có.
- Đứng yên và vừa di chuyển vừa dùng kỹ năng.

Đo nhịp update thực tế, quay/chụp so sánh trước/sau nếu hỗ trợ. Xác nhận sát thương, tốc độ bay và thời gian hiệu lực không đổi.

### Tiêu chí hoàn thành B
- Có bằng chứng projectile/effect update đạt 36 tick/giây trong điều kiện phù hợp.
- Quan sát thực tế mượt hơn.
- Không thay đổi gameplay hoặc phát sinh lỗi va chạm/sát thương.
- Không làm giảm hiệu năng tổng thể.
- Có báo cáo đo đạc và hồi quy.

## 6. Nguyên tắc Server 36Hz và an toàn

- Giữ Server 36Hz làm nền tảng chính; không tự ý quay lại 18Hz để né lỗi.
- Không thay đổi công thức sát thương, tốc độ đánh, cooldown, tốc độ di chuyển hoặc gameplay nếu chưa có phân tích và lý do rõ ràng.
- Tăng tần suất cập nhật hình ảnh không được làm game chạy nhanh gấp đôi.
- Giữ tương thích giao thức Client/Server.
- Không can thiệp Main VM hoặc dữ liệu server chính.
- Dùng VM thử đã được xác định; xác minh đúng VM trước mọi thao tác.
- Không commit hoặc ghi đè source chính khi chưa được yêu cầu.
- Giữ backup, diff, log và APK từng phiên bản.

## 7. Quy trình phối hợp

1. Haiku chuẩn bị nhân vật và tái hiện lỗi bản đồ.
2. Opus đồng thời phân tích camera/map/texture/render và các tác vụ liên quan.
3. Haiku cung cấp bằng chứng; Opus xác định nguyên nhân và sửa.
4. Build APK; Haiku kiểm thử lại.
5. Opus phân tích/triển khai projectile/effect 36 tick.
6. Haiku kiểm thử riêng từng nhóm kỹ năng.
7. Tích hợp hai thay đổi và chạy hồi quy.
8. Cung cấp APK cuối để người dùng thử trên điện thoại.

Hai nhiệm vụ có thể phân tích song song nhưng không được sửa đồng thời cùng file/hàm gây xung đột. Phải quản lý thứ tự tích hợp.

## 8. Tự chủ thực hiện

Claude Code tự thực hiện các thao tác thông thường nếu môi trường cho phép:
- Mở LDPlayer, thao tác game, ADB, lấy log, quay/chụp.
- Đọc source, sửa code, build, kiểm thử.
- Tự xử lý lỗi build/chạy/test và tiếp tục đến kết quả.
- Không yêu cầu người dùng chạy lệnh hoặc sao chép log nếu Claude tự lấy được.
- Không hỏi xác nhận từng bước kỹ thuật thông thường.

Chỉ hỏi người dùng khi cần quyết định ngoài phạm vi, thiếu quyền truy cập không thể tự xử lý, hoặc có nguy cơ mất dữ liệu không thể khôi phục/ảnh hưởng Main VM.

## 9. Báo cáo bắt buộc

Tạo báo cáo Phase 46 gồm:
1. Nguyên nhân gốc lỗi giật bản đồ.
2. Các kịch bản đã tái hiện, ảnh/video/log.
3. Thay đổi code và lý do.
4. Frame time/FPS trước và sau, số frame >40ms và >=100ms.
5. Kết quả projectile/effect 36 tick.
6. Kết quả từng nhóm kỹ năng.
7. Kiểm thử hồi quy.
8. Lỗi còn tồn tại và lý do.
9. Đường dẫn backup, diff, log, APK.
10. SHA256 APK cuối.

Chỉ đánh dấu hoàn thành khi có kết quả kiểm thử thực tế.