# 47 - Điều tra nhấp nháy cây cối/NPC/quái khi di chuyển nhanh (P46) + Sonnet QA độc lập

TÓM TẮT 5 DÒNG
1. Video điện thoại (Xiaomi 13T Pro, 2,8 s, 183 khung, ~65 fps): 2 sự kiện, mỗi lần TOÀN BỘ lớp đối tượng (cây, đá, quái, NPC và cả nhân vật) biến mất 4-5 khung = 53-59 ms; nền đất, tên, thanh máu, giao diện vẫn còn.
2. Nguyên nhân (ĐÃ XÁC MINH trên LDPlayer bằng log + video): khi camera sang vùng mới, `SetFocusPosition` xóa cây đối tượng (`ClearPreprocess` -> `m_ObjectsTree.Fell()`), nhưng cây chỉ dựng lại ở `Preprocess()` trong nhịp logic KẾ TIẾP (<= 55,6 ms). Từ Fix31 camera được đặt ở pha VẼ nên có khung được vẽ với cây rỗng.
3. Đây là lỗi hồi quy từ Fix31 (có cả ở Fix33-36 và P46), KHÔNG do phần nạp trước texture của P46. Trên màn 120 Hz thấy 4-6 khung trống, trên LDPlayer 60 Hz 2 khung.
4. LDPlayer, 30 s cưỡi ngựa: 22 lần đổi vùng, 9 lần có khoảng trống 45-68 ms, 18 khung vẽ với 0 đối tượng (bình thường rto=8, bio=52). Video LDPlayer: 8 sự kiện ~48-53 ms, khớp 8 khoảng trống >= 45 ms trong log.
5. Đề xuất sửa (CHỜ DUYỆT): dựng lại cây ngay trong cùng khung khi đổi vùng (gọi Preprocess ngay sau ChangeProcessArea nếu dữ liệu vùng đã sẵn sàng), giữ nguyên camera mượt. Chưa sửa code.

Cần tôi quyết định: có (duyệt phương án sửa ở mục 5).

## 1. Video người dùng (A1)
- File: Screenrecorder-2026-11-12-14-02-09-415.mp4; HEVC 2712x1220; 183 khung; 2,801 s; fps danh nghĩa 65,3; khoảng cách khung 10-29 ms (trung vị 15 ms); chỉ 3 khoảng > 25 ms -> không có mất khung quay đáng kể.
- Phương pháp: OpenCV (D:\tools\cvenv) - mỗi khung: mật độ viền Canny vùng cảnh (bỏ HUD), tỉ lệ điểm xanh lá, sai khác khung liền trước, độ sáng. Sự kiện = mật độ viền < 75% trung vị ±10 khung. Script: scratchpad vid_an.py; kết quả: D:\Android\b\p47-video\frames.csv, ảnh f000-f182.jpg (không đưa lên GitHub).
| Sự kiện | Khung | Thời gian | Thời lượng | Mật độ viền | Ghi chú |
|---|---|---|---|---|---|
| 1 | 31-35 | 437-496 ms | ~59 ms (5 khung) | 0,21 -> 0,13 | trước đó bình thường |
| 2 | 154-157 | 2323-2376 ms | ~53 ms (4 khung) | 0,24 -> 0,14 | khung 152-153 gần như trùng nhau (game đứng ~40 ms) ngay trước |
- Quan sát khung 31 (so với 30 và 36): mất đồng thời cây, đá, quái (Lãnh Thượng, Thần Tý), nhân vật người chơi; còn nền cỏ, tên nhân vật/quái, giao diện, minimap. => không phải lỗi texture từng đối tượng hay lỗi quay video; là trạng thái chung của lớp đối tượng.
- Thời lượng đo được 53-59 ms (không phải 100-200 ms như cảm nhận; có thể 2 sự kiện gần nhau hoặc khung đứng trước sự kiện làm cảm giác dài hơn).

## 2. Nguyên nhân trong source (A2)
- `KScenePlaceC::SetFocusPosition` (gamescene/KScenePlaceC.cpp ~988): khi vùng chứa camera đổi -> `ClearPreprocess(false)` -> `m_ObjectsTree.Fell()`: xóa nhánh cây vật thể bản đồ và chuyển MỌI runtime object (nhân vật/NPC/quái/đạn) sang danh sách tạm `m_PermanentLeaf` (không được vẽ). Trên Android đoạn khóa quanh Fell bị comment sẵn trong mã gốc.
- `ChangeProcessArea` chỉ đặt `m_bPreprocessEvent`; `Preprocess()` (dựng lại cây + `StrewRtoLeafs` gắn lại runtime object) chạy trong `KScenePlaceC::Breathe`, được gọi từ `KCoreShell::Breathe` ở NHỊP LOGIC (18/s).
- Mã gốc: camera đặt trong `KNpcRes::SetPos` (pha logic, trong `g_SubWorldSet.MainLoop`), ngay sau đó cùng Breathe gọi `g_ScenePlace.Breathe()` -> Preprocess: không có khung nào vẽ với cây rỗng.
- Fix31 (tick-smooth): `if (!g_bNpcInterpCameraOwned)` bỏ đặt camera ở pha logic; camera đặt trong `KgameWorldVN::custom_update` theo vị trí nội suy, TRƯỚC khi vẽ. Khi đổi vùng giữa 2 nhịp -> cây rỗng tới nhịp sau.
- Đã kiểm tra và loại trừ: texture cache/giải phóng (tex/img ~0 ở khung trống), nạp trước P46 (lỗi có từ Fix31; công tắc jxnopre không liên quan), culling `m_RepresentArea` (đối tượng không còn trong cây chứ không bị lọc), khóa luồng (lock=0), đồng bộ NPC từ server (nhân vật chính cũng mất).

## 3. Tái hiện và đo (A3) - LDPlayer, bản chẩn đoán P47 (= P46 + log, không đổi hành vi)
- Log mới: `R clear` (xóa cây), `R prep` (dựng lại), `O rto= bio=` (số runtime object / vật thể bản đồ được vẽ mỗi khung).
- Tuyến cưỡi ngựa 203/198 -> 180/195, 30 s, đồng thời screenrecord.
| Chỉ số | Giá trị |
|---|---|
| Số lần đổi vùng | 22 |
| Lần có khoảng trống >= 45 ms | 9 (45,3-68,0 ms) |
| Khung vẽ với 0 đối tượng | 18 (2/lần ở 60 Hz) |
| Bình thường mỗi khung | rto 8, bio 52 (trung vị) |
| Sự kiện trong video LDPlayer | 8 (48-53 ms) + 1 lần 132 ms |
- Frame time cùng lượt (P46 đã đo ở báo cáo 46): p99 ~27-39 ms, không có khung >= 100 ms -> nhấp nháy KHÔNG phải do khung chậm.
- So sánh Fix36: cùng cơ chế (Fix31 có trong Fix36); không chạy lại trên điện thoại.

## 4. Kết luận
VERIFIED: cơ chế "xóa cây khi đổi vùng ở pha vẽ, dựng lại ở nhịp logic sau" gây toàn bộ đối tượng biến mất ~1 nhịp logic. GIẢ THUYẾT: sự kiện 132 ms là 2 lần đổi vùng liên tiếp hoặc chờ vùng tải (m_nFirstToLoadIndex < 25) - cần thêm log.

## 5. Phương án sửa (CHỜ CHỦ MÁY DUYỆT)
1. (Khuyến nghị) Trong `SetFocusPosition`, ngay sau `ChangeProcessArea`, nếu `m_bPreprocessEvent` và không đang tải (`!m_bLoading`) thì gọi `Preprocess()` luôn (đúng việc Breathe sẽ làm, chỉ sớm hơn ~0-55 ms). Preprocess đo được ~0-1 ms. Giữ nguyên camera mượt của Fix31/P46.
   - Rủi ro: Preprocess chạy ở pha vẽ thay vì pha logic: nó lấy m_ProcessCritical (Paint chưa giữ khóa lúc này) -> không deadlock; vùng chưa tải xong thì vẫn chờ như mã gốc.
2. (Không khuyến nghị) Bỏ ClearPreprocess khỏi SetFocusPosition, để Preprocess tự xóa+dựng: cây giữ tham chiếu dữ liệu vùng có thể bị luồng tải ghi đè -> rủi ro crash.
3. (Không khuyến nghị) Trả camera về pha logic: mất độ mượt Phase 46.
Kiểm thử hồi quy sau sửa: lặp lại tuyến + screenrecord + gap_an (kỳ vọng 0 khung rto=0/bio=0, 0 sự kiện video), Phong Lăng Độ 162/186, đổi bản đồ (Thần Hành Phù), đăng nhập lại, đánh quái/đạn, frame time p99, crash; Sonnet xác minh độc lập.

## 5b. Bản sửa thử P47 (chủ máy duyệt phương án 1, chỉ bản thử)
- Kiểm tra trước khi áp: KHÔNG thể giữ cây cũ sau khi đổi vùng vì `ChangeProcessArea` -> `LeaveProcessArea()` giải phóng `m_BiosData.pLeafs` (lá vật thể mà cây cũ trỏ tới) -> giữ cây cũ = dùng vùng nhớ đã giải phóng. Vì vậy: xóa -> đổi vùng -> dựng lại NGAY trong cùng lời gọi `SetFocusPosition`, trước khi khung được vẽ; nếu dữ liệu vùng chưa sẵn sàng thì chờ có giới hạn 100 ms (khung chậm thay vì khung trống). Không vẽ trùng: cờ m_bPreprocessEvent được hạ. Camera nội suy P46 giữ nguyên.
- APK thử: D:\Android\b\apk-p46\jx-p47-test.apk, SHA256 FCFBAB67EB2F37FE25108F59E52DC7AE79CE459F90D5D206213BA1A8D224D28E (không phát hành). Diff: D:\Android\b\p47-diff\p47-client.diff.
- Kết quả (LDPlayer, FPS game đặt 90, log 58 s di chuyển do Sonnet thao tác): 67 lần đổi vùng; khung vẽ với 0 đối tượng 0 (trước: 18/30 s); khoảng trống xóa->dựng tối đa 11 ms trong cùng khung (trước 68 ms); Preprocess tb 0,47 ms, max 7,7 ms; chờ dữ liệu 0 lần; ok=0 0 lần; camera tỉ lệ 0,97, biến thiên 0,11; p99 26,5 ms; 1 khung 311 ms do app bị dừng ngoài vòng vẽ (gap 218 ms, nghi do thao tác cài đặt/chụp màn hình).
- CHƯA LÀM (dừng Sonnet để tiết kiệm hạn mức theo yêu cầu chủ máy): bài 5 phút liên tục + video đối chứng sau sửa, đo CPU/RAM, hồi quy đạn/hiệu ứng, kiểm thử điện thoại thật.

## 6. Sonnet QA độc lập (Phần B) - xem 47-autonomous-qa-architecture.md và TEST_RESULTS/47-autonomous-qa-log.md
## 7. Đường dẫn
- Bản chẩn đoán: D:\Android\b\apk-p46\jx-p47-diag.apk (không phát hành). Sao lưu trước sửa: D:\Android\b\backup-p47\.
- Video/khung: D:\Android\b\p47-video\ (video người dùng, ld-p47rec1.mp4, frames.csv). Log: D:\Android\b\p46-logs\diag1-prep.log (mốc 1794467742-1794467771).
