# 38 - Mô phỏng khe lệnh: cơ chế hiện tại so với phương án A, A2, B (18 Hz và 36 Hz)

Công cụ: `docs-analysis/tools/sim_command_slot.py` (Python thuần, chạy `python -I`, 18 giây). Kết quả thô: `docs-analysis/out/sim-command-slot.json` (320 dòng + 8 dòng nhạy cảm TTL). Không sửa source server, không chạy exe, không tạo VM, không đụng `JX-Server-D`, không commit.

## TÓM TẮT 5 DÒNG
1. Cơ chế hiện tại làm mất kỹ năng khi vừa chạy vừa dùng chiêu với client không có bảo vệ: **30 % ở 18 Hz, 14,5 % ở 36 Hz** (ping 150 ms). Hai làn (A/A2/B) đưa về **0 %** ở cả hai tần số.
2. Mô phỏng phát hiện một lỗi trong đề xuất của báo cáo 37: lệnh dừng "cứng" (phương án A) vẫn làm mất 9,5 % kỹ năng ở 18 Hz khi người chơi dừng ngay sau chiêu. Sửa bằng **dừng mềm (A2)**: 0 % mất.
3. **36 Hz một mình không sửa được lỗi** (mất 14,5 %), còn làm tăng việc bỏ kỹ năng bấm sát cuối hoạt cảnh (4-5 % so với 1-2 %). Cần lớp lệnh, không chỉ đổi tần số.
4. Phương án **B (đệm kỹ năng)** có tác dụng thật nhưng nhỏ (đánh thường +2-5 điểm %), đổi cảm giác bấm phím, và TTL lớn gây trễ. Nên là **tùy chọn tắt mặc định, TTL 100-150 ms**.
5. Kiểm thử hạn sống (11 ca) đạt hết: lệnh cũ hết hạn thì bỏ, lệnh mới vẫn được giữ và thi hành đúng thứ tự. Không có đảo thứ tự, không có lệnh chạy "ma" sau lệnh dừng ở bất kỳ cấu hình nào.

Cần tôi quyết định: có - chọn A2 làm nền, và B (có/không) cho bước dựng thử.

## 1. Mô hình
Hướng dẫn: mô phỏng sự kiện theo mili-giây, đọc từ mã (báo cáo 37).
- **Mạng:** TCP giữ thứ tự gói; một chiều = ping/2 cộng nhiễu ±(15 % x một chiều + 3 ms). Ping 50, 100, 150, 200 ms.
- **Server:** gói đến lúc nào xử lý lúc đó (ghi vào khe), ô lệnh chỉ đọc ở mỗi tick (pha ngẫu nhiên so với đồng hồ client). Thứ tự trong tick đúng như `KNpc::Activate`: `ProcCommand` trước, `ProcStatus` sau (`KNpc.cpp:1000-1003`). `ProcCommand` xóa ô sau mỗi lần; `m_ProcessAI = 0` khi diễn kỹ năng; sát thương ở 60 % hoạt cảnh; `DoSkill` kiểm hồi chiêu và đặt đứng khi từ chối; tăng khung ngay trong tick bắt đầu (bù trừ `WaitForFrame`).
- **Hoạt cảnh/hồi chiêu** (giả định, không đọc từ dữ liệu): chiêu A/B/C/D hoạt cảnh 800 ms, hồi chiêu 1000/700/900/1100 ms; đánh thường 600 ms, hồi chiêu 500 ms. Số tick = làm tròn(ms x Hz / 1000), nên 18 và 36 Hz tương đương theo thời gian thực (giả sử dữ liệu 36 Hz đã quy đổi).
- **Lưu lượng client** (từ báo cáo 31): chạy thẳng 9 gói/giây (mỗi 111 ms), đổi hướng tới 18 gói/giây (mỗi 55 ms). Hai kiểu client: `raw` (fix31, không bảo vệ) và `g33` (fix33: chặn di chuyển từ lúc bấm kỹ năng tới hết hoạt cảnh, rồi gửi bản mới nhất).
- **Cơ chế** so sánh: `hien_tai` (một ô, cái cuối thắng); **A** (báo cáo 37: hai làn, lệnh dừng xóa cả hai); **A2** (A nhưng lệnh dừng mềm: xóa làn di chuyển, không hủy kỹ năng đang chờ); **B** (A2 + giữ kỹ năng đang chờ trong lúc bận tới hết TTL 250 ms, mặc định). **C** (B + báo từ chối về client) cho **thi hành giống hệt B** về mặt mô hình, chỉ khác chẩn đoán và đòi đổi giao thức, nên không chạy riêng.
- 40 lần chạy x 20 giây mỗi cấu hình (seed cố định, cùng seed cho mọi cơ chế để so cặp).

## 2. Sáu tình huống
S1 vừa chạy vừa tung kỹ năng (bấm mỗi 1,5 +- 0,3 s). S2 đổi hướng liên tục (không kỹ năng). S3 dừng ngay sau kỹ năng (lệnh dừng 10-200 ms sau chiêu). S4 nhiều kỹ năng liên tiếp (bấm mỗi 250-550 ms, bốn chiêu xoay vòng, nhanh hơn hoạt cảnh nên mất là chuyện thiết kế). S5 đánh thường kết hợp di chuyển. Ping 50/100/150/200 là trục chung.

## 3. Kết quả chính
### 3.1 Tỷ lệ kỹ năng được thi hành (%), ping 150 ms, client `raw`
| | hiện tại 18 | hiện tại 36 | A 18 | A 36 | A2 18 | A2 36 | B 18 | B 36 |
|---|---|---|---|---|---|---|---|---|
| S1 chạy + kỹ năng | 70,3 | 85,5 | 100 | 100 | 100 | 100 | 100 | 100 |
| S3 dừng sau chiêu | 90,5 | 97,5 | 90,5 | 97,5 | **100** | **100** | 100 | 100 |
| S4 nhiều kỹ năng | 42,8 | 40,6 | 42,8 | 40,6 | 42,8 | 40,6 | 48,9 | 47,5 |
| S5 đánh thường + đi | 73,8 | 84,3 | 97,7 | 95,0 | 97,7 | 95,0 | **100** | **100** |
Ping 50-200 gần như không đổi con số (ví dụ S1 hiện tại 18 Hz: 74,9 / 73,1 / 70,3 / 73,2): tỷ lệ mất do cửa sổ tick, ít phụ thuộc ping.

Với client `g33` (đang cài trên điện thoại): S1 = 100 % cho mọi cơ chế (bảo vệ phía client đã đủ). S3 vẫn như `raw` (bảo vệ không bao quát lệnh dừng): 90,5 / 97,5 % với cơ chế hiện tại. S5 hiện tại 98,4 / 96,2 %, B = 100 %.

### 3.2 Nguyên nhân mất (kỹ năng gửi = 100 %), ping 150, `raw`
| | ghi đè | lệnh dừng xóa/ghi đè | bỏ vì bận | hết hạn |
|---|---|---|---|---|
| S1 hiện tại 18 / 36 | 29,7 / 14,5 | 0 | 0 | 0 |
| S3 hiện tại 18 / 36 | 9,5 / 2,5 (lệnh dừng ghi đè kỹ năng) | - | 0 | 0 |
| S3 A 18 / 36 | 0 | 9,5 / 2,5 | 0 | 0 |
| S5 hiện tại 18 / 36 | 24,8 / 11,9 | 0 | 1,4 / 3,9 | 0 |
| S5 A2 18 / 36 | 0 | 0 | 2,3 / 5,0 | 0 |
| S4 A2 18 / 36 | 0 | 0 | 57,2 / 59,4 (thiết kế) | 0 |
| S4 B 18 / 36 | 4,3 / 2,4 | 0 | 0 | 46,9 / 50,1 |
Ghi chú S4: người chơi bấm nhanh hơn hoạt cảnh nên phần lớn lần bấm "mất" ở cả bản gốc lẫn bản sửa; đó là luật chơi, không phải lỗi. B chỉ cứu phần bấm trong 250 ms cuối.

### 3.3 Vì sao 36 Hz làm kỹ năng bấm sát cuối hoạt cảnh bị bỏ nhiều hơn (S5: 2,3 % -> 5,0 %)
Ô lệnh bị đọc và xóa ở **mọi** tick, kể cả tick nhân vật còn bận. Tick càng mau thì càng có nhiều tick "trúng lúc bận" trước khi hoạt cảnh kết thúc, nên lệnh bấm sát cuối bị tiêu thụ và bỏ thay vì chờ tới tick trống. (Truy vết: 18 Hz bỏ khi khoảng cách bấm <= 555 ms, 36 Hz bỏ khi <= 583 ms, cùng một chiêu 611 ms.) Đây là lý do B (giữ lệnh khi bận) quan trọng hơn ở 36 Hz.

### 3.4 Độ trễ thi hành (ms, từ lúc client gửi tới lúc server bắt đầu), ping 150
| | 18 Hz p50 / p95 | 36 Hz p50 / p95 |
|---|---|---|
| Kỹ năng, cơ chế hiện tại (S1) | 98 / 127 | 88 / 108 |
| Kỹ năng, A2/B (S1) | 105 / 132 | 89 / 109 |
| Kỹ năng B TTL 250 (S4) | 124 / 297 | 108 / 289 |
| Kỹ năng B TTL 150 (S4) | 114 / 200 | 98 / 203 |
| Di chuyển, mọi cơ chế (S2, ping 100) | 76,5 / 102,5 | 63,9 / 80,6 |
Chờ ở server (từ lúc gói đến tới lúc thi hành): p50 23-29 ms ở 18 Hz, 12-15 ms ở 36 Hz. Bản gốc nhìn "nhanh hơn" A2 ở 18 Hz chỉ do thiên lệch sống sót (bản gốc bỏ những chiêu đến muộn trong cửa sổ). 36 Hz tiết kiệm khoảng 10-12 ms trung vị, ~22 ms ở p95.

### 3.5 Ghi đè, thứ tự, đổi hướng, dừng
- **Đổi hướng liên tục (S2):** không mất lệnh ở mọi cơ chế; 4,5 % gói chạy bị gói chạy mới thay trước tick ở 18 Hz (đúng ý "cái cuối thắng"), 0 % ở 36 Hz. A2 và B giống hệt cơ chế hiện tại (không hồi quy khi không có kỹ năng).
- **Thứ tự thi hành:** số cặp đảo thứ tự = 0 trong mọi tình huống và mọi cơ chế. Số lệnh chạy "ma" (gửi trước lệnh dừng nhưng thi hành sau) = 0.
- **Lệnh dừng:** không mất lệnh dừng nào làm nhân vật chạy tiếp; phần lớn lệnh dừng rơi đúng lúc đang diễn chiêu nên bị bỏ vô hại (hết hoạt cảnh tự đứng).
- **Từ chối do hồi chiêu làm đứng khi đang chạy:** 0 lần trong các tình huống đã chạy (các kịch bản không bấm chiêu khi còn hồi chiêu lúc chạy).
- **Di chuyển bị bỏ vì bận (S1 `raw`):** 33,6 % (hiện tại) và 48,5 % (A2) - A2 thi hành nhiều chiêu hơn nên nhân vật bận lâu hơn; đúng ý. Client `g33` không gửi gói chạy trong lúc bận nên 0 %.

### 3.6 Nhạy cảm TTL của B (ping 150, `raw`)
| TTL | S4 chạy 18 / 36 % | S4 ghi đè 18 / 36 % | trễ p95 18 / 36 | S5 chạy |
|---|---|---|---|---|
| 100 ms | 44,8 / 44,0 | 0 / 0 | 157 / 154 | 100 % |
| 150 ms | 46,6 / 45,9 | 0 / 0 | 200 / 203 | 100 % |
| 250 ms | 48,9 / 47,5 | 4,3 / 2,4 | 297 / 289 | 100 % |
| 400 ms | 51,9 / 50,4 | 30,8 / 29,2 | 443 / 438 | - |
TTL 100 ms đã đủ cho đánh thường; TTL lớn chỉ thêm vài điểm % kỹ năng nhưng trễ p95 vọt lên gần nửa giây và kỹ năng cũ bị chiêu mới đè.

## 4. Kiểm tra hạn sống (yêu cầu 7)
11 ca đơn vị chạy trước khi mô phỏng (`unit_tests()`), đều đạt:
- T1: kỹ năng cũ (TTL 250) hết hạn tại tick 300, lệnh chạy mới đến lúc 290 vẫn được thi hành.
- T2: lệnh chạy cũ (TTL 120) hết hạn, kỹ năng mới đến lúc 190 được giữ và thi hành.
- T3: kỹ năng hết hạn không xóa lệnh chạy đến sau.
- T4: kỹ năng sau thay kỹ năng trước, bản cũ ghi "ghi đè".
- T5/T6: B giữ kỹ năng lúc bận, thi hành khi hết bận nếu còn trong TTL; hết hạn nếu chờ quá TTL.
- T7: A (không đệm) bỏ kỹ năng lúc bận như cũ.
- T8: dừng mềm giữ kỹ năng chờ; dừng cứng (A) hủy nó.
- T9: cơ chế hiện tại: gói sau thắng (chạy xóa kỹ năng; kỹ năng đè chạy).
- T10/T11: lệnh chạy đến sau kỹ năng không đè kỹ năng; "dừng rồi chạy" giữ đúng thứ tự.

## 5. Kết luận: phương án phù hợp cho server 18 Hz và 36 Hz
1. **A2 là phương án nền, dùng cho cả hai tần số:** hai làn (di chuyển / hành động), mỗi làn một chỗ, hạn sống tính bằng mili-giây (di chuyển 120 ms, hành động 250 ms), kỹ năng không bị chạy ghi đè, kỹ năng xóa lệnh chạy đang chờ, **lệnh dừng mềm** (xóa lệnh chạy, không hủy kỹ năng đang chờ), ngồi/nhảy/dịch chuyển vẫn là lệnh cứng. Sửa **báo cáo 37 mục 6**: lệnh dừng không còn "xóa cả hai làn".
2. **B là tùy chọn có cờ cấu hình, mặc định tắt**, TTL 100-150 ms (không dùng 250 ms trở lên). Nên bật cùng lúc khi chuyển 36 Hz, vì tick mau làm lệnh sát cuối hoạt cảnh bị bỏ nhiều hơn (mục 3.3).
3. **C không đáng làm** để cải thiện thi hành: mô hình cho kết quả như B, đổi lại phải sửa giao thức.
4. **18 Hz:** triển khai A2 giữ nguyên toàn bộ dữ liệu. **36 Hz:** A2 chạy nguyên si nhờ hạn sống theo ms; lợi thêm cửa sổ ghi đè nhỏ hơn (14,5 % thay vì 30 % trên client không bảo vệ) và trễ thấp hơn 10-12 ms, nhưng vẫn cần quy đổi dữ liệu theo tick (báo cáo 34 mục 5).
5. **Giá trị thực tế với client đang có (fix33):** khá nhỏ cho S1; còn ý nghĩa ở **lệnh dừng sau chiêu (9,5 % -> 0 % ở 18 Hz)**, đánh thường khi bận (1-5 %) và, quan trọng hơn, **không phụ thuộc vào việc client có bảo vệ hay không** (client Unity mới, bot, bản client khác).

## 6. Hạn chế và điều chưa kiểm
- **Số tuyệt đối chưa hiệu chuẩn:** mô hình cho S1 `raw` 18 Hz mất 30 % trong khi mô phỏng ở báo cáo 33 cho fix31 là 56 % (44 % chạy được); hai mô hình dùng giả định lưu lượng khác nhau. Thứ tự và xu hướng (A/A2/B tốt hơn, 36 Hz giảm cửa sổ) đáng tin hơn con số cụ thể.
- **Chưa mô hình:** mất gói/truyền lại, Nagle (fix33 đã bật `TCP_NODELAY`), nhiễu nhịp tick của server, nhiều người chơi, ảnh hưởng của `MaxClienLoop`, kỹ năng có mục tiêu/đạn, dữ liệu thật của `skills.txt`.
- **Giả định chưa xác nhận:** client có gửi lệnh dừng (gói ngồi/đứng, `KProtocolProcess.cpp:6041-6056`) khi nhả tay cầm hay không. Nếu không, S3 chỉ còn là "chạy rồi chiêu"; kết luận 2 vẫn đúng với bất kỳ client nào có gửi lệnh dừng.
- **Chưa đo CPU/mạng** của hai làn (nhỏ: hai ô thêm vài byte mỗi nhân vật); sẽ đo khi dựng thử.
- Mã nguồn server có thể không khớp `gs001.exe` đang chạy (báo cáo 35).

## 7. Bước tiếp (cần duyệt)
Dựng A2 trên bản copy `D:\JX-build\src18` (chưa chạy), kèm bộ đếm log; thử trong VM riêng, DB riêng sau khi chủ máy duyệt tạo VM. Chưa sửa gì ở bước này.
