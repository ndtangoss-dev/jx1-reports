# A-11 - So sanh gpt-6.1-sol va gpt-6-astra (qua xingchi)

TÓM TẮT 5 DÒNG
1. Làm được gì: 3 bài (T1 tóm tắt A-05, T4 soạn file task, T5 tóm tắt D-01 theo mẫu TÓM TẮT) × 2 mô hình, effort low, sandbox read-only, 1 lần/bài.
2. Kết quả: cả hai ĐÚNG ở cả 3 bài, không có 429; chất lượng gần như ngang nhau; thời gian lộn xộn (astra nhanh hơn T1, T5; chậm hơn T4).
3. Còn thiếu: mỗi ô chỉ 1 lần chạy nên chưa kết luận tốc độ; chưa thử bài sửa mã/lập luận dài; chưa đo trên bảng điều khiển xingchi.
4. Rủi ro: lần chạy đầu một tiến trình treo >2 giờ ở T4 (không rõ do mô hình hay mạng): luôn đặt thời hạn khi chạy hàng loạt.
5. Bước tiếp: dùng astra làm bể thứ hai cho việc đọc/tóm tắt/soạn task (effort low); giữ sol cho sửa mã, build, lập luận khó. Cần chủ máy quyết: không.

| Bài | Mô hình | Giây | 429 | input tok (cache) | output tok | Đúng/sai |
|---|---|---|---|---|---|---|
| T1 tóm tắt 5 dòng | sol | 26 | không | 79.879 (4.096) | 175 | Đúng, 5 dòng |
| T1 | astra | 20 | không | 68.390 (55.680) | 180 | Đúng, 5 dòng |
| T4 soạn task | sol | 72 | không | 68.174 (4.096) | 513 | Đúng: front matter, 4 mục đủ, nhãn chỉ-đọc |
| T4 | astra | 266 | không | 56.685 (3.712) | 541 | Đúng: front matter, 4 mục đủ, có yêu cầu bằng chứng file:dòng |
| T5 tóm tắt D-01 | sol | 208 | không | 77.728 (4.096) | 187 | Đúng mẫu: 5 dòng đánh số + "Can toi quyet dinh: co" |
| T5 | astra | 81 | không | 66.239 (3.712) | 196 | Đúng mẫu; số liệu (27 hoạt động; 0/24/1/1/1) trùng sol |

Nhận xét: nội dung T5 hai mô hình khớp nhau về số liệu; astra dùng ~15% ít token input hơn ở cả 3 bài, output ngang nhau. Thời gian dao động lớn (20-266 s) và không theo một mô hình nào, nên nghi do độ trễ phía nhà cung cấp, không phải mô hình. Sol ghi `level: investigation` (tự đặt), astra `level: 1`: cả hai chấp nhận được, cần PM kiểm lại khi dùng file task do máy soạn.
Ghi chú kỹ thuật: lần chạy đầu T1 đều 0 giây vì thiếu `--skip-git-repo-check` (đã sửa). Raw output là UTF-8 bị đọc sai trên console (mojibake); decode bằng cp437→utf-8 hoặc đọc bằng Python UTF-8.
Dữ liệu thô: `D:\JX-wt\A11\*.raw.txt`, `ketqua.txt` (không đưa vào kho).
