# PHASE 46 – ADDENDUM: GAME-AWARE QA, MINIMAP INTELLIGENCE & KNOWLEDGE DISCOVERY

**Trạng thái:** ĐƯỢC NGƯỜI DÙNG DUYỆT – PHẢI THỰC HIỆN CÙNG PHASE 46  
**Phạm vi:** Bổ sung năng lực QA tự khám phá và hiểu game; không thay thế hoặc làm thay đổi các yêu cầu kỹ thuật gốc của Phase 46.

## 1. Mục tiêu

QA không chỉ chạy theo tọa độ hoặc kịch bản có sẵn. QA phải chủ động quan sát giao diện, khám phá chức năng, hiểu mục tiêu, lập kế hoạch thao tác, kiểm tra kết quả và lưu lại kiến thức đã xác minh để tái sử dụng.

Mục tiêu cụ thể:
- Tự khám phá minimap, đọc tên/vị trí NPC và điều hướng đến NPC theo tên hoặc mục tiêu người dùng đưa ra, không phụ thuộc việc người dùng cung cấp tọa độ.
- Tự khám phá toàn bộ danh mục và chức năng thực tế hiển thị trong lệnh bài GM; ghi lại cách dùng và kết quả.
- Nhận biết bị kẹt, thất bại điều hướng hoặc thao tác không có tác dụng; không lặp vô hạn.
- Duy trì cơ sở tri thức có bằng chứng để các vòng QA sau có thể dùng lại và cập nhật.

## 2. Kiểm tra năng lực công cụ trước khi thao tác

Trước tiên, Claude Code phải xác minh những gì môi trường thực sự hỗ trợ:
- Chụp ảnh màn hình LDPlayer/thiết bị và lưu ảnh/video nếu công cụ cho phép.
- Điều khiển chạm, nhấn giữ, vuốt, joystick, bàn phím và nhập văn bản.
- ADB, logcat, log ứng dụng/server và khả năng đọc trạng thái nhân vật.
- OCR/nhận diện hình ảnh, đọc tọa độ trên minimap và theo dõi vị trí nhân vật.
- Thu thập FPS/frame time, CPU, RAM, GPU nếu có công cụ phù hợp.

Lập bảng năng lực: **CÓ THỂ DÙNG / KHÔNG CÓ / CHƯA XÁC MINH**, kèm bằng chứng kiểm tra. Không được giả vờ đã nhìn thấy màn hình, điều khiển game, chạy video capture hoặc đo FPS nếu công cụ không hỗ trợ. Nếu thiếu công cụ, tìm phương án thay thế an toàn; nếu vẫn không thể, ghi **BLOCKED** và nêu chính xác giới hạn.

Phải phân biệt rõ:
- Tần suất render của game.
- Tần suất chụp màn hình/ghi hình.
- Tần suất OCR/Computer Vision.
- Tần suất AI phân tích ảnh.
- Tần suất logic/tick của client và server.

Không suy ra game chạy 60 FPS chỉ vì có 60 ảnh/giây, hoặc suy ra AI phân tích liên tục chỉ vì có thể chụp ảnh. Muốn đánh giá giật 100ms phải có chuỗi frame-time hoặc capture đủ chi tiết; một vài ảnh tĩnh không đủ chứng minh.

## 3. Vòng lặp QA như người chơi thật

Áp dụng vòng lặp bắt buộc:

**OBSERVE → UNDERSTAND → PLAN → ACT → VERIFY → ADAPT**

1. Observe: quan sát màn hình, minimap, tọa độ, trạng thái nhân vật, mục tiêu và log/telemetry sẵn có.
2. Understand: xác định đang ở bản đồ nào, nhân vật đang làm gì, giao diện nào đang mở và điều kiện hiện tại.
3. Plan: chia mục tiêu thành các bước ngắn có thể kiểm chứng.
4. Act: thực hiện một hành động có kiểm soát.
5. Verify: xác nhận trạng thái thực tế đã thay đổi đúng như dự kiến.
6. Adapt: nếu không đúng, phân tích nguyên nhân và thay đổi cách làm; không lặp máy móc.

Mỗi mục tiêu phải có trạng thái **IN_PROGRESS / SUCCESS / FAILED / BLOCKED**. Chỉ đánh dấu SUCCESS khi có bằng chứng trực tiếp như tọa độ thay đổi, đúng NPC được chọn, cửa sổ tương tác mở, vật phẩm/điểm số thực sự thay đổi hoặc kết quả tương đương.

### Phát hiện bị kẹt

- Theo dõi tọa độ/vị trí nếu có thể; nếu không, dùng thay đổi hình ảnh và trạng thái chuyển động làm tín hiệu phụ.
- Nếu nhân vật chạy tại chỗ, tọa độ không đổi, liên tục va vào vật cản hoặc không tiến gần mục tiêu sau một khoảng kiểm tra hợp lý, đánh dấu nghi ngờ bị kẹt.
- Tối đa hai lần thử lại cùng một hướng/cách thao tác. Sau đó dừng, quan sát lại, đổi hướng hoặc lập tuyến khác.
- Nếu vẫn không đi được, ghi **MOVEMENT_BLOCKED**, lưu ảnh/log/tọa độ và nguyên nhân nghi ngờ. Không chạy vô hạn vào tường.
- Phải phân biệt bị kẹt thật với nhân vật đang thi triển kỹ năng, bị khóa điều khiển, đang tải bản đồ hoặc có độ trễ mạng.

## 4. Module A – Minimap Intelligence và tự tìm NPC

QA phải tự khám phá minimap thay vì mặc định đã biết cách dùng.

### 4.1 Khám phá minimap
- Xác định nút mở/đóng minimap và các thành phần giao diện.
- Kiểm tra minimap có hiển thị tên NPC, biểu tượng, tọa độ, danh sách NPC, tìm kiếm tên, tìm tọa độ, đánh dấu điểm đến hoặc chỉ đường hay không.
- Thử từng chức năng một cách có kiểm soát; ghi lại thao tác, phản hồi giao diện và kết quả.
- Xác định cơ chế điều hướng thực tế. Không giả định game có tìm NPC theo tên nếu giao diện không hỗ trợ.

### 4.2 Quy trình tìm NPC theo tên
Khi được giao mục tiêu như “đến gặp Lễ Quan”:
1. Xác định bản đồ hiện tại và mở minimap.
2. Tìm tên NPC trong danh sách/nhãn/biểu tượng hoặc dùng cơ chế tìm kiếm mà game thực sự cung cấp.
3. Nếu minimap chỉ hiển thị tọa độ, khám phá cách đọc tọa độ NPC bằng OCR/quan sát; không tự bịa vị trí.
4. Xác định điểm đến và cách di chuyển phù hợp.
5. Điều hướng theo từng chặng, liên tục xác minh nhân vật có tiến gần mục tiêu không.
6. Khi đến nơi, xác nhận đúng NPC bằng tên/ảnh/giao diện tương tác, sau đó mới thực hiện tương tác.
7. Ghi nhận trường hợp không tìm thấy NPC, NPC không xuất hiện, sai bản đồ hoặc đường đi bị chặn.

Mục tiêu là người dùng chỉ cần nêu **tên NPC hoặc việc cần làm**; QA tự tìm bản đồ, vị trí, cách đến và cách tương tác. Nếu game không có tính năng tự tìm NPC, QA phải tự xây dựng quy trình nhận diện và điều hướng phù hợp từ những gì đã quan sát, hoặc báo BLOCKED nếu không đủ dữ liệu.

### 4.3 Cơ sở dữ liệu NPC
Tạo/cập nhật `knowledge/npcs/` với mỗi NPC gồm:
- Tên hiển thị chính xác.
- Bản đồ/khu vực.
- Tọa độ đã quan sát (nếu có).
- Ảnh tham chiếu hoặc bằng chứng nhận diện.
- Chức năng NPC (chỉ ghi khi đã xác minh).
- Cách tiếp cận và thao tác tương tác.
- Điều kiện/yêu cầu để sử dụng.
- Kết quả thực tế khi tương tác.
- Trạng thái: **VERIFIED / DISCOVERED / UNKNOWN**.
- Ngày/phiên bản client hoặc build đã kiểm chứng.

Không nâng thông tin DISCOVERED/UNKNOWN thành VERIFIED nếu chưa có bằng chứng thực nghiệm.

## 5. Module B – Khám phá toàn bộ lệnh bài GM

QA phải tự mở lệnh bài GM và lập bản đồ đầy đủ các chức năng thực sự có trên giao diện.

### 5.1 Kiểm kê giao diện
- Chụp/ghi nhận màn hình chính của lệnh bài GM.
- Khám phá từng danh mục, tab, nút, menu con, trang, danh sách cuộn, hộp thoại và trường nhập.
- Cuộn đến cuối từng danh sách; không chỉ ghi nhận những mục đang nhìn thấy ban đầu.
- Ghi đúng tên/nhãn hiển thị và cấu trúc phân cấp; lưu ảnh bằng chứng nếu có thể.
- Không tự suy diễn chức năng từ tên nút nếu chưa kiểm tra kết quả.

### 5.2 Phân loại mức độ an toàn

Mỗi chức năng phải được phân loại:

- **READ_ONLY:** chỉ xem/tra cứu, không thay đổi dữ liệu.
- **REVERSIBLE:** thay đổi có thể hoàn tác an toàn.
- **GAME_STATE_CHANGE:** thay đổi trạng thái nhân vật/game như cấp độ, điểm, kỹ năng, tiền, vật phẩm.
- **IRREVERSIBLE_OR_RISKY:** có thể xóa/reset dữ liệu, ảnh hưởng tài khoản/server, phát sinh tác động khó hoàn tác.

Quy tắc:
- Có thể khám phá READ_ONLY trong phạm vi môi trường test.
- REVERSIBLE và GAME_STATE_CHANGE chỉ được thử trên nhân vật/VM test được phê duyệt và trong phạm vi nhiệm vụ Phase 46; ghi lại trạng thái trước/sau.
- IRREVERSIBLE_OR_RISKY chỉ kiểm kê giao diện và mô tả rủi ro; tuyệt đối không thực thi nếu chưa có phê duyệt cụ thể của người dùng.
- Không thử chức năng có thể tác động Main VM hoặc dữ liệu thật.
- Không nhập lệnh tùy ý, token lạ hoặc giá trị không hiểu rõ chỉ để xem phản ứng.

### 5.3 Hồ sơ từng chức năng GM
Với mỗi mục, ghi:
- Tên và đường dẫn menu.
- Mục đích (phân biệt mô tả theo nhãn với kết quả đã xác minh).
- Các trường tham số/giá trị hợp lệ quan sát được.
- Điều kiện sử dụng.
- Các bước thao tác.
- Phân loại an toàn.
- Trạng thái trước và sau khi thử.
- Kết quả thực tế, thông báo thành công/thất bại và lỗi.
- Có thể hoàn tác không, cách hoàn tác đã được xác minh hay chưa.
- Trạng thái **VERIFIED / DISCOVERED / NOT_TESTED / BLOCKED**.

Ưu tiên hiểu các nhóm liên quan Phase 46 như cấp độ, điểm thuộc tính, điểm kỹ năng, kỹ năng, vàng/xu, trang bị/vũ khí/vật phẩm, dịch chuyển/bản đồ/ngựa nếu thực sự có. Tuy nhiên phải kiểm kê tất cả mục truy cập được, không chỉ các nhóm ưu tiên.

Không coi toast “thành công” là bằng chứng đủ. Phải kiểm tra trạng thái nhân vật/inventory/skill thực tế sau thao tác.

## 6. Module C – Khám phá vật phẩm, kỹ năng và bản đồ

Khi có điều kiện an toàn:
- Ghi nhận tên, biểu tượng, mô tả và cách sử dụng vật phẩm cần cho test.
- Ghi nhận kỹ năng, cấp kỹ năng, mục tiêu, tầm đánh, thời gian thi triển, cooldown và hiệu ứng quan sát được.
- Phân biệt hiệu ứng hình ảnh với tác động gameplay.
- Ghi lại bản đồ đã vào được, lối chuyển bản đồ, điểm xuất hiện và NPC quan trọng.
- Chỉ ghi những gì đã quan sát/kiểm chứng; phần chưa rõ phải đánh dấu UNKNOWN.

Tổ chức tri thức theo cấu trúc gợi ý:
- `knowledge/minimap/`
- `knowledge/npcs/`
- `knowledge/navigation/`
- `knowledge/gm-token/`
- `knowledge/items/`
- `knowledge/skills/`
- `knowledge/maps/`

Có thể điều chỉnh cấu trúc nếu repository đang có quy ước phù hợp hơn. Mỗi hồ sơ cần có bằng chứng và trạng thái xác minh.

## 7. Module D – Đo hiệu năng và chất lượng hình ảnh

Kết hợp công cụ đo tự động với đánh giá QA:
- Thu thập frame time/FPS liên tục nếu công cụ hỗ trợ; báo cáo P50/P95/P99, số frame >33.3ms, >40ms và >=100ms, các đỉnh giật và thời điểm tương ứng.
- Gắn thời điểm đo với hành động trong game, vị trí/bản đồ, log, CPU/RAM và hoạt động tải texture nếu có.
- Nếu có thể, dùng Computer Vision/OpenCV để hỗ trợ phát hiện thay đổi khung hình, chuyển động, đứng yên bất thường, blur hoặc độ sắc nét.
- Đánh giá hình ảnh dựa trên ảnh gốc và phong cách JX1: độ rõ sprite, viền, texture, aliasing, blur và hiện tượng mất/nhấp nháy asset.
- Không tự ý làm sắc nét, thay texture hoặc đổi phong cách pixel-art trong nhiệm vụ đo lường.
- Phân biệt số liệu đo tự động với nhận xét chủ quan của QA.
- Không tuyên bố “mượt”, “sắc nét” hoặc “đã hết giật” nếu không có dữ liệu và kịch bản kiểm chứng tương ứng.

Một ảnh tĩnh chỉ hỗ trợ đánh giá chất lượng hình ảnh tại thời điểm chụp; không chứng minh được frame pacing hoặc loại bỏ hitch ngắn. Nếu không thể capture liên tục/đo frame time, ghi rõ giới hạn.

## 8. Phân công vai trò AI và phương án dự phòng

Vai trò mục tiêu:
- **Claude Code:** điều phối, kiểm tra môi trường/công cụ, giao nhiệm vụ, quản lý file/báo cáo, bảo vệ dữ liệu và đảm bảo quy trình.
- **Sonnet:** QA Lead – lập kế hoạch kiểm thử, điều phối Game-Aware QA, đánh giá bằng chứng và quyết định đạt/chưa đạt.
- **Haiku:** QA Assistant – thao tác lặp lại, khám phá UI, chụp ảnh, thu thập log/telemetry, chạy test theo kế hoạch và ghi kết quả.
- **Opus:** Developer – phân tích nguyên nhân gốc, đề xuất/sửa code, build và giải thích diff.

Claude Code phải kiểm tra thực tế khả năng gọi/khởi chạy từng model/subagent trong môi trường hiện tại. Không được tuyên bố đã phân công Sonnet/Haiku/Opus nếu không thực sự gọi được. Nếu model hoặc công cụ không khả dụng:
1. Báo rõ vai trò nào không thể khởi chạy.
2. Không giả lập kết quả như thể agent đó đã chạy.
3. Dùng phương án thay thế khả dụng nhưng giữ tách biệt trách nhiệm QA và Developer.
4. Đánh dấu giới hạn trong báo cáo.

## 9. Tiêu chí nghiệm thu năng lực QA

QA chỉ được đánh dấu đạt khi có bằng chứng cho các mục tương ứng:
1. Tự mở minimap và giải thích được các chức năng đã khám phá.
2. Tìm được NPC theo tên mà không cần người dùng cung cấp tọa độ (với NPC có thể nhận diện trên client).
3. Điều hướng đến đúng NPC, phát hiện vật cản/bị kẹt, đổi cách đi hoặc báo BLOCKED đúng cách.
4. Xác nhận đúng NPC và tương tác thành công.
5. Mở lệnh bài GM, kiểm kê toàn bộ mục có thể truy cập, kể cả mục nằm dưới vùng cuộn/menu con.
6. Phân loại an toàn từng chức năng; chỉ thực thi các thao tác đã được cho phép.
7. Xác minh trạng thái trước/sau đối với thao tác thay đổi nhân vật.
8. Lưu hồ sơ tri thức có bằng chứng, trạng thái xác minh và hướng dẫn tái sử dụng.
9. Thu thập được số liệu hiệu năng/chất lượng hình ảnh hoặc ghi rõ công cụ/giới hạn khiến chưa thể đo.
10. Không can thiệp Main VM và không thực hiện thao tác rủi ro chưa được duyệt.

Nếu một mục không thể hoàn thành do thiếu công cụ hoặc điều kiện game, báo **BLOCKED/NOT TESTED**, không đánh dấu PASS.

## 10. Bàn giao bắt buộc

Báo cáo addendum phải bao gồm:
- Danh sách công cụ QA thực tế và năng lực đã xác minh.
- Các chức năng minimap đã khám phá và cách dùng.
- Danh sách NPC đã phát hiện, tọa độ/bản đồ nếu có, trạng thái xác minh và bằng chứng.
- Sơ đồ menu GM đầy đủ; chức năng, phân loại rủi ro, mục đã thử/chưa thử và kết quả.
- Hồ sơ vật phẩm/kỹ năng/bản đồ được khám phá.
- Quy trình phát hiện stuck và ví dụ thực tế.
- Số liệu capture/FPS/frame time và đánh giá hình ảnh; nêu rõ phương pháp/giới hạn.
- Các file knowledge mới/cập nhật, ảnh, log và đường dẫn.
- Vai trò model/subagent thực sự đã chạy và phần không khả dụng.
- Danh sách mục VERIFIED, DISCOVERED, NOT TESTED, BLOCKED, UNKNOWN.

## 11. Bảo vệ dữ liệu và giới hạn phạm vi

- Chỉ thao tác trên Clone/Test VM và nhân vật test đã được phê duyệt.
- **Tuyệt đối không can thiệp Main VM.**
- Không thực thi chức năng GM IRREVERSIBLE_OR_RISKY nếu chưa được người dùng duyệt cụ thể.
- Không xóa dữ liệu, backup, tài khoản hoặc cấu hình ngoài phạm vi.
- Không ghi token, mật khẩu, cookie hoặc thông tin đăng nhập vào log/báo cáo.
- Giữ nguyên yêu cầu gốc Phase 46 về Fix36 baseline, Server 36Hz, sửa map stutter, projectile/effect 36 tick và không commit source chính khi chưa được yêu cầu.

**Addendum này là phần bổ sung bắt buộc của Phase 46. Không được dùng việc khám phá game để trì hoãn hoặc bỏ qua các hạng mục sửa lỗi và kiểm thử kỹ thuật gốc.**
