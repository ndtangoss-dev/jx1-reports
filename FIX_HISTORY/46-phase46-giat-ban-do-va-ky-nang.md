# 46 - Phase 46: giật bản đồ khi di chuyển, giật khi ra chiêu, cập nhật đạn/hiệu ứng

TÓM TẮT 5 DÒNG
1. Giật màn hình khi chạy chủ yếu do nội suy RĂNG CƯA 18 Hz (fix33): khung đầu mỗi nhịp đi chậm còn 0,47 lần. Sửa xong tỉ lệ = 1,00, biến thiên vận tốc camera 0,36 -> 0,09 (ĐÃ XÁC MINH, cùng tuyến).
2. Khung cực chậm khi di chuyển: dựng ẩn bảng Tự động (KuiAutoPlay) ~700 ms đúng lúc ra khỏi thành, giải mã texture vùng mới trên luồng chính, tên NPC có chữ Việt mới (~110 ms). Đã sửa/hoãn/nạp trước: lúc di chuyển, khởi động nguội, max 755-939 ms -> 39-69 ms, không còn khung >=100 ms (ĐÃ XÁC MINH trên LDPlayer).
3. Giật nặng khi ra chiêu: bóng mờ (afterimage) vẽ cả 24 phần kể cả phần đã trong suốt. Sửa: chỉ vẽ phần alpha > 0. Ra chiêu liên tục (ấm): p95 103 -> 45 ms, khung >=100 ms 58 -> 0 (ĐÃ XÁC MINH).
4. Đạn bay: vị trí vẽ đổi 43-59 lần/s (>= 36), răng cưa 0,68 -> ~1,0. Khung hình sprite ~17 lần/s là giới hạn của asset (1 khung/nhịp), KHÔNG phải 36 hình/giây. Chỉ đo được 1 kỹ năng (Đại Lực Kim Cang Chưởng); kỹ năng khác BỊ CHẶN do hạn chế vũ khí.
5. APK cuối: xem mục 9. Server 36Hz giữ nguyên (không sửa server). Chưa có kết quả người dùng thử trên điện thoại.

Cần tôi quyết định: có (thử APK trên điện thoại; quyết định có tối ưu tiếp bóng mờ/KuiAutoPlay không).

## 1. Môi trường (ĐÃ XÁC MINH)
- Máy <hostname>; VM đang chạy duy nhất: JX-Test-36 (VM thử). Main VM JX-Server-D tắt, không đụng.
- Server: bản tự dựng 36Hz (C:\JX\Bisect\T4), SvrFPS 36/36. Không sửa server trong Phase 46.
- Client thử: LDPlayer9 960x540, Android 9, ADB. Nhân vật test <test-char> (cấp 200).
- Vai trò model đã chạy THẬT: Opus 5.5 (điều phối + developer), Sonnet 5.5 (QA Lead: kế hoạch QA, knowledge base, đánh giá bằng chứng), Haiku (QA Assistant: thao tác game, ảnh, hồi quy). Một số thao tác chuẩn bị (mở bản đồ lớn, mua bình nội lực, dò kỹ năng, đo ra chiêu) do Opus làm trực tiếp khi Haiku bị kẹt - ghi rõ ở mục 6.

## 2. Công cụ đo
- Log trong app (bật bằng file /sdcard/jxtrace): JXTRC C (camera mỗi khung), T (vị trí logic mỗi nhịp), N (vị trí bị đổi ngoài nhịp), M (mỗi lần vẽ đạn: vị trí, khung sprite, tuổi, nhịp). JXPERF: tóm tắt 5 s, khung > 40 ms (hitch, kèm texN/tex/img), pha Director (dir), pha Paint (paintph), đối tượng vẽ > 30 ms (slowobj), NpcOther, autoplay-create, blur, fontwarm.
- Phân tích: p46_analyze.py, sawtooth.py, ftime.py (p50/p95/p99, > 33/40/100 ms), missile_an.py.
- Tuyến cố định: cưỡi ngựa, Tìm tọa độ Ba Lăng Huyện 203/198 <-> 180/195, cửa sổ 30 s; "nguội" = khởi động lại app ngay trước lượt.
- Không có OCR/OpenCV; ảnh chỉ dùng cho quan sát, không dùng để kết luận frame pacing.

## 3. Nguyên nhân gốc và sửa (client; mã ở D:\Android\b\Client)
| # | Nguyên nhân (bằng chứng) | Sửa | File |
|---|---|---|---|
| A1 | fix33 luôn nội suy từ vị trí ĐANG VẼ -> đoạn 1,25 nhịp bị nén vào 1 nhịp, khung đầu mỗi nhịp đi +1 px thay vì +4 (chuỗi JXTRC C) | Chỉ "đi tiếp từ vị trí đang vẽ" khi vị trí đó lệch khỏi đường nội suy cũ (> 3 đơn vị: có sửa vị trí). Bình thường nội suy chuẩn từ vị trí logic nhịp trước | KNpc.cpp (UpdateRenderPos, JxDistSqToSeg), KNpc.h |
| A2 | Đổi vùng: giải mã SPR + tạo texture + đọc SPR trên luồng chính (paint 30-84 ms, tex/img) | Nạp trước texture các vùng đã tải quanh nhân vật trong thời gian rảnh của khung (<= 4 ms/khung, trylock, cùng hàm giải mã nên ảnh giống hệt). Công tắc tắt: /sdcard/jxnopre | KScenePlaceC.cpp/.h, KScenePlaceRegionC.cpp/.h, KgameWorldVN.cpp |
| A3 | Dựng ẩn bảng Tự động (autoCallback(NULL,false)) ~690-760 ms sau 180 khung trạng thái chiến đấu - thường đúng lúc chạy ra khỏi thành (JXPERF autoplay-create) | Hoãn bước cuối tới khi nhân vật đứng yên >= 30 khung. Chức năng giữ nguyên; 700 ms vẫn còn nhưng rơi vào lúc đứng yên | KgameWorldVN.cpp |
| A4 | Tên NPC có chữ Việt chưa có trong atlas TTF (vd. "Hươu đốm") -> vẽ glyph giữa lúc chơi ~110 ms | Nạp trước toàn bộ bảng chữ Việt vào atlas (TTF 14, viền 1) khi vào màn chơi (fontwarm 46 ms lúc tải) | KgameWorldVN.cpp |
| B1 | Bóng mờ ra chiêu vẽ đủ 24 phần kể cả phần alpha = 0 (35-40 ms/lớp, 58 khung >= 100 ms) | Chỉ vẽ phần alpha > 0 (phần alpha 0 vốn trong suốt -> hình không đổi) | KNpcRes.cpp (KNpcBlur::Draw) |
| B2 | Đạn: cùng lỗi răng cưa fix34 | Cùng quy tắc A1 cho đạn | KMissle.cpp |
| B3 | Độ cao Z đạn vòng cung không nội suy | Nội suy Z | KMissle.cpp/.h |
| B4 | Khung sprite đạn theo cả nhịp | Chọn khung theo nửa nhịp khi sprite có nhiều khung hơn số nhịp sống (tổng thời gian giữ nguyên, trễ tối đa nửa nhịp) | KMissleRes.cpp/.h |
| B5 | Hiệu ứng bám NPC lấy vị trí logic chưa nội suy | Dùng vị trí vẽ đã nội suy của NPC | KSkillSpecial.cpp |
| D | Đo lường (không đổi gameplay) | JxPerf.h, CCDirector.cpp, Kgetinidata.cpp, CoreDrawGameObj.cpp | |
Không đổi: logic 18 nhịp/giây phía client, tốc độ chạy, sát thương, hồi chiêu, thời gian sống của đạn, giao thức, server.

## 4. Số liệu trước/sau (LDPlayer, ĐÃ XÁC MINH)
### 4.1 Camera khi chạy đều (cùng tuyến 203/198 -> 180/195)
| Chỉ số | Trước (Fix36) | Sau |
|---|---|---|
| Tốc độ khung-ngay-sau-nhịp / khung khác | 0,47 | 1,00 (run2), 1,00-1,01 các lượt sau |
| Biến thiên vận tốc khi chạy đều | 0,36 | 0,09-0,10 |
| Khung camera đứng yên giữa lúc chạy | 56 | 27 |

### 4.2 Khung chậm khi di chuyển, khởi động nguội (chỉ tính khung đang di chuyển)
| Lượt | max | > 40 ms | >= 100 ms |
|---|---|---|---|
| Trước (không nạp trước, chưa hoãn AutoPlay) | 939 ms | 8 | 1 |
| Trước (bản 2d) | 755 ms | 4 | 1 |
| Sau (bản 3, 3 lượt) | 39 / 69 / 65 ms | 0 / 2 / 4 | 0 / 0 / 0 |
Chiều ngược, nguội, cả cửa sổ: > 40 ms 12 (bản 1) -> 4 (bản 2); p99 31,8 -> 29,4 ms.

### 4.3 Ra chiêu (Đại Lực Kim Cang Chưởng, 16 lần nhấn/30 s, cả cửa sổ)
| Bản | p95 | p99 | max | >= 100 ms |
|---|---|---|---|---|
| Mốc Fix36 (ít lần đánh) | 54 | 111 | 134 | 5 |
| Bản 3, ấm | 103 | 162 | 225 | 58 |
| Bản 4, nguội | 41 | 58 | 88 | 0 |
| Bản 4, ấm | 45 | 57 | 82 | 0 |

### 4.4 Đạn bay (missile_an.py)
| | Mốc | Bản 4 |
|---|---|---|
| Vị trí vẽ đổi (lần/s, trung vị) | 42 | 43-52 (tối đa ~60 = FPS) |
| Tỉ lệ răng cưa đạn | 0,68 | 1,01-1,16 |
| Khung sprite đổi (lần/s) | 15 | 17 |
Kết luận: chuyển động đạn được cập nhật theo FPS hiển thị (>= 36 lần/s). Khung hình sprite vẫn ~1 khung/nhịp (18/s) vì asset chỉ có chừng đó khung; không quảng cáo là 36 hình/giây.

## 5. Kiểm thử hồi quy (Haiku, bản 4)
| Mục | Kết quả |
|---|---|
| HUD số thật, tên, cấp | SUCCESS |
| Đánh quái bằng phím chính | PARTIAL (quái mất máu, rơi đồ; hiệu ứng khó thấy trong ảnh) |
| Dùng bình hồi nội lực | SUCCESS |
| Vừa chạy vừa đánh | PARTIAL (không crash) |
| Cưỡi ngựa + Tìm tọa độ 203/198 | SUCCESS; log: tỉ lệ răng cưa 1,01, biến thiên 0,10; 1 khung 121 ms do tên NPC mới -> đã sửa A4 ở bản 5 |
| Mở/đóng bản đồ lớn khi chạy | SUCCESS |
| Chuyển bản đồ bằng Thần Hành Phù | NOT RUN (vòng sau) |
| Crash | Không |

## 6. Giới hạn, lỗi còn lại, bị chặn
- Kịch bản chuẩn Phong Lăng Độ 162/186: đo trước sửa có log (Haiku chạy) nhưng nhân vật chết vì quái khi đứng yên; chạy lại sau sửa: xem mục 10 (cập nhật khi có).
- Ra chiêu: bóng mờ vẫn tốn 13-32 ms/lớp trên LDPlayer dù không tạo texture mới (chi phí đổi shader/uniform/vẽ GL trực tiếp mỗi phần; LDPlayer dịch GL sang GPU máy chủ). Cần đo trên điện thoại thật; nếu còn, đề xuất gom các phần bóng mờ vào một lần vẽ.
- Bảng Tự động: vẫn mất ~700 ms một lần mỗi phiên, nay lúc đứng yên. Đề xuất tối ưu KuiAutoPlay (Phase sau).
- Kỹ năng khác: Vô Ảnh Xuyên cần Phi Đao, Tam Giới Quy Thiên cần Đơn Đao -> BLOCKED; AOE/nhiều đạn/liên hoàn chưa đo riêng. Nội suy Z và hiệu ứng bám NPC: đã sửa, CHƯA KIỂM THỬ riêng.
- Quái/NPC khác dưới server 36Hz: gói đồng bộ ~36/s gán thẳng vị trí logic -> NPC đó không nội suy (GIẢ THUYẾT ảnh hưởng thị giác, chưa đo).
- Bảng nhân vật thiếu nút "+" ở các dòng Sức mạnh/Thân pháp/Sinh khí/Nội công (vẫn bấm được) - để Phase sau.
- Thao tác do Opus làm thay QA: mở bản đồ lớn (chạm đúp), đóng bảng kỹ năng/cửa hàng, tháo vũ khí, mua bình nội lực ở Ngô Thần Y, toàn bộ lượt đo tuyến cố định và ra chiêu bằng script ADB.

## 7. Server
Không thay đổi. JX-Test-36 chạy bản tự dựng 36Hz (C:\JX\Bisect\T4), tick ~0,45-0,8 ms. Main VM không đụng.

## 8. Sao lưu, diff, log
- Sao lưu trước Phase 46: D:\Android\b\backup-p46\ (gồm bản gốc CCDirector.cpp, KMissleRes.h).
- Diff: D:\Android\b\p46-diff\p46-client.diff (18 file).
- Log: D:\Android\b\p46-logs\ (diag1-prep.log và các cửa sổ run*.log, cast*.log, runs.txt mốc thời gian). Log có thể chứa tên nhân vật test, không đưa lên GitHub.
- Các APK trung gian: D:\Android\b\apk-p46\ (diag1 = mốc Fix36 + log; fix1..fix5).

## 9. APK
- Bản cuối: `jx-tailscale-8080-p46.apk` (= bản sửa 5), SHA256 `235DBD37F35C2B266588B209733E578D7D6528363DD19158F8ECD80BCCB3B847`, 94 994 607 byte. D:\Android\b\apk-p46-final\ và CDN /apk/jx-tailscale-8080-p46.apk (HTTP 200 đã kiểm).
- Ký cùng khóa a48601f7…f2d7; so với Fix36 chỉ khác lib/arm64-v8a/libMyGame.so -> cài đè được.
- Thư viện chưa strip: D:\Android\b\apk-p46-final\libMyGame-p46-unstripped.so.
- Log đo chỉ chạy khi có file /sdcard/jxtrace; bình thường chỉ in JXPERF khi khung > 40 ms và tóm tắt 5 s.

## 10. Kết quả vòng cuối (Phong Lăng Độ, đồ HK, bản cuối)
Kịch bản chuẩn: Thần Hành Phù -> Phong Lăng Độ, cưỡi ngựa, Tìm tọa độ 162/186 (Haiku thao tác, Opus đo log).
| Chỉ số | Trước (Fix36, cùng kịch bản) | Sau (bản cuối) |
|---|---|---|
| Tỉ lệ tốc độ camera khung-sau-nhịp / khung khác | 0,45 | 0,98 |
| Biến thiên vận tốc camera khi chạy đều | 0,43 | 0,09 |
| p99 / max thời gian khung | 39,1 / 87 ms | 38,8 / 90 ms |
| Khung >= 100 ms | 0 | 0 |
Kết luận: trong kịch bản chuẩn, hiện tượng "giật màn hình khi di chuyển" là nhịp răng cưa camera (không phải khung chậm) và đã hết theo số đo. Còn ~22 khung 40-90 ms trong 45 s (vẽ nhân vật/ngựa ~33-38 ms, giải mã texture) - chưa phải mục tiêu của Phase này.
Bước C (đánh quái ở Phong Lăng Độ): BỊ CHẶN - nhân vật trúng độc, HP < 40% khi xuống ngựa, chưa có thuốc hồi sinh lực; chuyển phiên sau (mua Ngũ Hoa Ngọc Lộ Hoàn ở thành thị).
- Mặc đồ: Tiếu Ngạo Giang Hồ Lục -> Hỗ trợ Thử Nghiệm -> Trang bị HK (Bộ Kim Phong) mặc được; vũ khí xanh Kim Cô Bổng cần Sức mạnh 165 -> chưa mặc.
- Nội công 15 -> 4910 bằng điểm tiềm năng (Nội lực tối đa 215 -> 5110, sau đồ 5802).
