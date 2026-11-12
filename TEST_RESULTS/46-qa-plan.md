# Kế hoạch QA Phase 46

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Người lập: Sonnet (QA Lead) | Nhân vật: jxt36a, hệ Kim, Cấp 200 | LDPlayer 960x540 | Server test 36Hz (VM thử, không phải Main VM)

Phạm vi: kế hoạch và tiêu chí. Việc thao tác do Haiku, sửa code do Opus. Các ngưỡng đạt/không đạt dưới đây là ĐỀ XUẤT của QA Lead, cần Opus/chủ máy duyệt trước khi dùng làm cổng phát hành.

## 1. Bảng năng lực công cụ

| Công cụ | Trạng thái | Bằng chứng / giới hạn |
|---|---|---|
| adb screencap | CÓ THỂ DÙNG | Haiku đã chụp hàng trăm ảnh. Chụp là ảnh tĩnh: không chứng minh frame pacing. |
| adb screenrecord | CÓ THỂ DÙNG (theo thông tin Opus) | Chưa xác minh trong Phase 46: giới hạn 3 phút/lần, tốc độ ghi thực tế, có giữ được 60 khung không. Tần suất ghi khác tần suất render. |
| adb input tap | CÓ THỂ DÙNG | Chạm đúp minimap chạy được (tap, sleep 0.12, tap). |
| adb input swipe | CÓ THỂ DÙNG | Dùng cho joystick và vuốt. Swipe cùng điểm đầu/cuối với thời gian dài làm nhấn giữ: CHƯA XÁC MINH. |
| adb input text | CÓ THỂ DÙNG | Đã nhập tọa độ và số cấp vào ô nhập (p46qa-22.png, p46qa-78.png). |
| logcat (JXPERF/JXTRC) | CÓ THỂ DÙNG | Nguồn số đo chính: frame time, nhịp, vị trí camera. Cần kiểm định dạng dòng log và tần suất ghi trước khi tin (ca A0). |
| top / dumpsys meminfo | CÓ THỂ DÙNG | CPU và RAM của app và của LDPlayer; CPU của máy ảo Android không phải CPU thật của host. |
| dumpsys gfxinfo | CHƯA XÁC MINH | Game dùng GL (Cocos2d-x), số liệu có thể rỗng. |
| GPU counters | CHƯA XÁC MINH | Chưa có công cụ biết trước. |
| sendevent / gesture nhiều ngón | CHƯA XÁC MINH | Cần khi vừa chạy vừa bấm kỹ năng đồng thời; thay bằng hai lệnh input chạy nền song song, cũng CHƯA XÁC MINH. |
| Đọc tọa độ tự động | KHÔNG CÓ | Không có OCR; chỉ AI đọc ảnh chụp, chậm và có thể sai chữ số. Dùng minimap/bảng GM để đọc. |
| OCR / OpenCV / PIL | KHÔNG CÓ | Không so ảnh tự động, không đo blur/độ sắc nét bằng máy. Đánh giá hình ảnh là chủ quan. |
| Đọc log server | CHƯA XÁC MINH | Sonnet không truy cập VM; Opus/Claude Code lấy giúp. |
| Đo FPS bằng HUD game | CÓ THỂ DÙNG, độ tin thấp | HUD hiển thị FPS tức thời dao động lớn (26 đến 82 trong các ảnh). Chỉ dùng tham khảo. |

Phân biệt bắt buộc trong mọi báo cáo: tần suất render của game; tần suất chụp/ghi hình; tần suất AI đọc ảnh (chậm, không phải liên tục); tần suất logic client; tần suất logic server (36Hz). Không suy ra mượt từ ảnh tĩnh.

## 2. Quy trình vận hành (mọi ca)

OBSERVE: chụp màn hình, đọc bản đồ, tọa độ, trạng thái nhân vật, bảng đang mở. UNDERSTAND: xác định nhân vật đang ở đâu, đang làm gì, bảng nào khóa điều khiển. PLAN: chia mục tiêu thành bước ngắn kiểm chứng được. ACT: một hành động điều khiển. VERIFY: chụp và so với dự kiến (tọa độ đổi, đúng NPC, HP/hành trang đổi). ADAPT: sai thì tìm nguyên nhân và đổi cách, không lặp máy móc.

Mỗi mục tiêu có trạng thái IN_PROGRESS / SUCCESS / FAILED / BLOCKED; SUCCESS chỉ khi có bằng chứng trực tiếp.

### Phát hiện kẹt
- Đọc tọa độ minimap trước và sau 3 giây. Tọa độ không đổi 2 lần liên tiếp (6 giây) mà không phải đang cast, tải bản đồ, bảng khóa điều khiển, ping cao: nghi kẹt.
- Tối đa 2 lần thử cùng một cách (cùng hướng/cùng lệnh). Sau đó đổi: hướng khác, đi vòng, Tìm tọa độ tới điểm trung gian, đóng bảng.
- Vẫn không đi: ghi MOVEMENT_BLOCKED kèm ảnh, tọa độ, hướng đã thử, nghi ngờ. Không chạy vô hạn.

## 3. Điều kiện chung và cách đo

Điều kiện chung: xác nhận build là Fix36 + p46 diag, server test 36Hz (log khởi động có LogicFps=36), nhân vật Cấp 200 đã có ngựa; đóng mọi bảng giao diện trước khi đo; không có thao tác khác trên LDPlayer; ghi thời điểm bắt đầu/kết thúc (đồng hồ HUD) để đối chiếu log; mỗi ca chạy tối thiểu 3 lần, báo cả ba, không chỉ lần đẹp nhất.

Ca A0 (kiểm định công cụ, làm trước): chạy 60 giây đứng yên rồi 60 giây chạy; xác nhận logcat JXPERF/JXTRC có dòng mỗi khung hoặc mỗi khoảng bao lâu, định dạng, mất dòng không. Không có chuỗi frame time liên tục thì mọi ca A chỉ được kết luận BLOCKED về frame pacing.

Số đo cho ca A (từ JXPERF): tổng số khung và thời lượng; p50, p95, p99 frame time (ms); số khung >33,3 ms; >40 ms; >=100 ms; chuẩn hóa theo phút; thời điểm các đỉnh và khoảng cách giữa chúng (kiểm tra chu kỳ, ví dụ mỗi 1 s hoặc mỗi 10 s); vị trí/bản đồ lúc đỉnh; kèm CPU và RAM (top, dumpsys meminfo) lấy mỗi 10 giây; sự kiện đổi vùng, tải texture nếu log có.

Số đo cho ca B (từ JXTRC): tần suất cập nhật vị trí đạn (số lần cập nhật/giây, p50 khoảng cách giữa hai lần cập nhật), tần suất đổi khung hình sprite hiệu ứng (tách riêng với cập nhật vị trí), thời gian bay từ lúc phát đến lúc va chạm, tọa độ điểm va chạm, số đạn đồng thời, sát thương (HP đích trước/sau), cooldown và thời gian thi triển đo bằng đồng hồ log.

## 4. Nhóm A: giật bản đồ

Điều kiện tiên quyết cho cả nhóm: ca A0 xong; nhân vật đã cưỡi ngựa (xác nhận bằng ảnh, ví dụ nút ngựa chuyển trạng thái và tốc độ di chuyển cao hơn); kịch bản chuẩn đặt ở Phong Lăng Độ.

| Ca | Mục đích | Điều kiện | Bước | Số đo | Đạt | Không đạt |
|---|---|---|---|---|---|---|
| A1 | Kịch bản chuẩn Phong Lăng Độ | Thần Hành Phù có trong hành trang; ngựa | Dùng Thần Hành Phù tới Phong Lăng Độ; lên ngựa; mở bản đồ lớn, nhập 162/186, Tìm tọa độ, Đóng; để nhân vật tự đi và ghi 60 giây; lặp 3 lần, mỗi lần bắt đầu từ cùng điểm | Toàn bộ số đo ca A; thời gian tới đích | Mỗi lần: khung >=100 ms bằng 0 hoặc tối đa 1 và không lặp theo chu kỳ; p99 <= 40 ms; khung >40 ms dưới 1% tổng khung; tới đích đúng 162/186 | Có đỉnh >=100 ms lặp theo chu kỳ, hoặc p99 >40 ms, hoặc không tới đích (ghi BLOCKED nếu bị chặn) |
| A2 | Đường dài liên tục | Bản đồ rộng, ngựa | Chạy thẳng tối thiểu 3 phút theo 2 tuyến khác nhau | Như A1 theo từng phút | Như A1; không tăng dần RAM bất thường (RAM cuối - đầu < 50 MB) | Frame time xấu dần theo thời gian hoặc RAM tăng đều |
| A3 | Đổi hướng liên tục | Bãi trống | Zigzag 30 giây, đổi hướng mỗi 1 đến 2 giây bằng swipe joystick | Như A1; độ trễ cảm nhận chủ quan ghi riêng | Không có đỉnh >=100 ms; p99 <= 40 ms | Có đỉnh khi đổi hướng |
| A4 | Qua ranh giới vùng | Có tuyến đi qua nhiều vùng tải | Chạy đúng một tuyến qua ít nhất 5 lần đổi vùng; ghi tọa độ lúc đổi vùng | Frame time quanh lúc đổi vùng (trước/sau 1 s) | Khung quanh ranh giới không tệ hơn nền (p95 không tăng quá 20%) và không có >=100 ms | Đỉnh trùng điểm đổi vùng (ghi là hướng nghi ngờ cho Opus) |
| A5 | Nhiều NPC/quái/hiệu ứng | Khu đông (Ba Lăng Huyện gần Lễ Quan) | Chạy qua khu NPC dày 60 giây, ngựa; lặp 3 lần | Như A1; số đối tượng ước lượng từ ảnh | p99 <= 40 ms; không mất NPC/texture trong ảnh | Khung dài tăng khi vào khu đông, hoặc NPC/texture mất |
| A6 | Mở/đóng minimap khi chạy | Đang chạy | Trong lúc chạy ngựa, chạm đúp minimap mở bản đồ lớn rồi Đóng, 5 lần, cách nhau 10 giây; ghi thời điểm từng lần | Frame time 2 giây quanh mỗi lần mở/đóng | Mỗi lần không có khung >=100 ms; p99 <= 40 ms | Có đỉnh trùng mỗi lần mở/đóng |
| A7 | Chu kỳ dài (soak) | | Chạy hoặc đứng 10 phút, ghi đỉnh | Khoảng cách các đỉnh; kiểm tra chu kỳ 1 s và 10 s (cơ chế dọn texture Fix36 mỗi 10 s khi cache > 384 MB) | Không có chu kỳ đỉnh >=100 ms | Có chu kỳ lặp đều |

Ngưỡng tham chiếu từ Fix36 trên LDPlayer: khung >40 ms từ 197 xuống 12 và >=100 ms từ 15 xuống 1 trong một lần đo (độ dài đo không ghi trong tài liệu, nên không so trực tiếp với ca mới; bắt buộc đo lại baseline Fix36 cùng kịch bản A1 để so cạnh nhau).

Một ca A chỉ là SUCCESS khi cả số đo log lẫn quan sát không mâu thuẫn. Nếu người dùng thấy giật mà log không đỉnh: ghi "log không bắt được", nghi giật do hiển thị/camera không nằm trong frame time (ví dụ camera cập nhật theo nhịp logic thay vì theo render); Opus xem JXTRC vị trí camera.

## 5. Nhóm B: kỹ năng và đạn 36 tick

Điều kiện tiên quyết: nhân vật có vũ khí hợp kỹ năng (kỹ năng "Tâm Giới Quy Thiên" cần Đơn Đao theo mô tả), có mục tiêu thử (quái hoặc NPC thử), HP/nội lực đầy; xác định trước danh sách kỹ năng nào có đạn (từ skills/bang-ky-nang-cap-200.md); ghi nhịp 18 hay 36 của baseline bằng cách chạy cùng ca trên bản đối chứng.

| Ca | Mục đích | Bước | Số đo | Đạt | Không đạt |
|---|---|---|---|---|---|
| B1 | Tầm xa có đạn | Đứng cách mục tiêu gần tầm tối đa, dùng 1 kỹ năng đạn, 10 lần | Tần suất cập nhật vị trí đạn; thời gian bay; điểm va chạm; sát thương | Vị trí đạn cập nhật 34 đến 38 lần/giây khi bay (p50 khoảng cách giữa hai lần xấp xỉ 27,8 ms); thời gian bay và điểm va chạm bằng baseline (chênh <= 1 tick, 28 ms) | Cập nhật vẫn 18/giây, hoặc thời gian bay đổi |
| B2 | Đường bay dài / ngắn | Một kỹ năng, 2 khoảng cách (gần và xa) | Như B1 theo khoảng cách | Như B1; hiệu ứng không nhanh gấp đôi hay lặp | Hiệu ứng chạy nhanh hơn, mất, hoặc sai thời gian tồn tại |
| B3 | Nhiều đạn | Kỹ năng bắn nhiều đạn hoặc dùng liên tiếp sao cho nhiều đạn đồng thời | Số đạn đồng thời, cập nhật mỗi đạn, frame time lúc đó | Như B1 cho từng đạn; p99 frame time không xấu hơn baseline quá 10% | Giảm FPS hoặc đỉnh >=100 ms khi nhiều đạn |
| B4 | AOE | Kỹ năng diện rộng, đứng giữa nhóm mục tiêu | Thời điểm bắt đầu/kết thúc hiệu ứng, thời gian tồn tại, số mục tiêu trúng, sát thương | Thời gian tồn tại bằng baseline; số mục tiêu trúng không giảm | Hiệu ứng ngắn/dài khác baseline, mục tiêu trúng thay đổi |
| B5 | Nổ/va chạm | Đạn trúng mục tiêu, và trúng tường/ngoài tầm nếu kỹ năng có | Thời điểm nổ so với thời điểm va chạm theo log; khung sprite nổ | Nổ đúng thời điểm va chạm (chênh <= 1 tick), không nổ hai lần | Nổ sai chỗ, thiếu, lặp |
| B6 | Liên hoàn / combo | Chuỗi kỹ năng nếu có | Thứ tự, khoảng cách thời gian, cooldown | Khoảng cách và cooldown bằng baseline | Rút ngắn/kéo dài cooldown |
| B7 | Đứng yên so với vừa chạy | Cùng một kỹ năng khi đứng và khi chạy ngựa | Như B1; frame time | Như B1 trong cả hai; không thêm đỉnh | Chỉ đạt khi đứng |
| B8 | Hồi quy gameplay | Cùng mục tiêu, cùng kỹ năng, 20 lần, với và không có fix | Sát thương trung bình, thời gian cast, cooldown, tốc độ bay | Không khác biệt ngoài ngưỡng ngẫu nhiên của game (xác định bằng biến thiên của baseline) | Khác biệt có hệ thống |

Lưu ý bắt buộc:
- Sprite gốc có thể chỉ 18 khung hình/giây: báo cáo riêng "cập nhật vị trí" và "khung hình sprite"; không tuyên bố sprite 36 FPS nếu log cho thấy khung hình đổi 18 lần/giây.
- Tác động gameplay (sát thương, thời điểm trúng) phân biệt với hiệu ứng hình ảnh; kiểm tra bằng HP đích trước/sau, không chỉ nhìn đạn.
- So sánh trước/sau cần hai APK (hoặc cờ) trên cùng nhân vật, cùng điều kiện, thứ tự ngẫu nhiên hóa; mỗi cấu hình tối thiểu 3 lượt.
- Ngưỡng 34 đến 38 lần/giây là đề xuất; cần Opus xác nhận cơ chế đo của JXTRC trước khi dùng.

## 6. Đóng ca

Báo cáo mỗi ca: ID, build, ngày giờ, điều kiện, số đo (bảng), ảnh bằng chứng (tên file), kết quả SUCCESS/FAILED/BLOCKED, nhận xét chủ quan tách riêng. Không tuyên bố "mượt", "hết giật" hay "sắc nét" nếu thiếu dữ liệu và kịch bản tương ứng. Không chạm Main VM. Không thực thi mục GM CẦN DUYỆT (xem knowledge/gm-token).

## 7. Quyết định của Opus (bổ sung 2026-11-12, ghi bởi Sonnet)

1. Ngưỡng đã duyệt: p99 frame time <= 40 ms khi chạy đều; không có khung >=100 ms lặp theo chu kỳ. Chỉ số chính thêm cho lỗi người dùng thấy:
   - Tỉ lệ tốc độ camera "khung ngay sau nhịp logic / khung khác" khi chạy đều: mượt = 0,9 đến 1,1.
   - Biến thiên vận tốc camera khi chạy đều: đạt <= 0,15.
   - Đạn: vị trí vẽ đổi >= 36 lần/giây khi bay. Khung sprite đổi tối đa 36 lần/giây (giới hạn do asset; không đòi 36 nếu sprite ít khung). Điều này thay ngưỡng đề xuất "34 đến 38 lần/giây" ở mục 5.
2. Định dạng log (bật bằng file jxtrace): JXTRC "C t_us x y alpha nBreathe" mỗi khung (camera); "T t_us loop x y doing" mỗi nhịp logic; "N" khi vị trí nhân vật bị đổi ngoài nhịp; "M t_us id x y frame life all loop" mỗi khung cho mỗi đạn đang bay. JXPERF: "sum" mỗi 5 s, "hitch" khi khung >40 ms (từ bản fix1b có texN/tex/img), "dir" pha Director. Công cụ phân tích p46_analyze.py, sawtooth.py do Opus giữ. Ca A0 chỉ còn cần xác nhận log đã bật và đủ dòng.
3. Kết quả đã đo (Opus): nguyên nhân giật khi di chuyển là nội suy răng cưa 18 Hz do fix33. Cùng tuyến cưỡi ngựa Ba Lăng Huyện 203/198 đến 180/195: tỉ lệ khung-sau-nhịp 0,47 thành 1,00; biến thiên vận tốc 0,36 thành 0,09; khung camera đứng yên 56 thành 27. Khung chậm còn lại ở pha vẽ (visit 30 đến 84 ms) khi đổi vùng bản đồ, đang đo tiếp. Ca A4 phải nhắm vào điểm này. QA Lead chưa tự kiểm các số này (chưa thấy log).
4. Menu GM CẦN DUYỆT: mặc định KHÔNG mở, không thực thi; chỉ kiểm kê những gì hiển thị sẵn.
5. Log server: Opus tự lấy khi cần.
6. Opus rà và push knowledge.
7. An toàn nhân vật: jxt36a đã chết một lần ở Phong Lăng Độ (quái Lãnh Thượng/Thần Tý đánh khi đứng yên), mất khoảng 50% bạc, đã về Ba Lăng Huyện. Ca A1 và mọi ca ở Phong Lăng Độ: không đứng yên; phải liên tục di chuyển hoặc đánh trả; theo dõi HP và dừng ca nếu HP thấp.
