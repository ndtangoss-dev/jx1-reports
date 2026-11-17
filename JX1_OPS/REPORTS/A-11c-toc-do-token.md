# A-11c — Đo tốc độ token (xingchi, /v1/responses)

TÓM TẮT 5 DÒNG
1. `gpt-6.1-sol` sinh ~28–34 token/giây ổn định trên cả K2, K3, K4 (cả effort low và high); không khác biệt đáng kể giữa các khóa.
2. TTFT (chờ token đầu) dao động rất lớn: 5–49 giây cho cùng prompt ~4,3k token; đây là độ trễ nhà cung cấp, không phụ thuộc kích thước prompt.
3. Tải 3 song song trên một khóa (K4): không thấy 429; tốc độ sinh gần như không giảm (27,5–30,5 tok/s), chỉ TTFT có lần 49 s.
4. `gpt-6-astra` trả 503 (Service Unavailable) ở mọi lần gọi trên K2, K3, K4 (kể cả gọi đơn lẻ lúc 11:02) → chưa đo được; A-11b không làm được cho tới khi xingchi bật lại astra.
5. Worker thật chỉ đạt 5–35 token ra/giây tính cả thời gian chạy lệnh (trung vị ~20); khâu nghẽn là số vòng gọi model + đọc ngữ cảnh lớn (hàng triệu token vào), không phải tốc độ sinh.

## Phương pháp
`speed.py`: gọi streaming `/v1/responses` (User-Agent `codex_cli_rs/0.166.0`), prompt cố định ~4,3k token vào (đã gồm ~4k overhead ẩn), đo TTFT (tới `response.output_text.delta` đầu), tổng giây, `tps_gen = out_tok / (total − TTFT)`. `run_all.sh` chạy song song nhiều luồng ghi chung một file nên vài dòng JSONL bị dính nhau; chỉ dùng các dòng đọc được (9 dòng, 7 hợp lệ cho sol) cộng 1 lần gọi lại đơn lẻ lúc 11:03.

## Kết quả `gpt-6.1-sol`
| Khóa | Effort | Điều kiện | TTFT (s) | Tổng (s) | Token ra | tok/s sinh |
|---|---|---|---|---|---|---|
| K2 | low | đơn/4 luồng chung | 18,7 | 133,9 | 3412 | 29,6 |
| K2 | low | đơn lẻ | 11,3 | 94,7 | 2399 | 28,8 |
| K3 | high | 4 luồng chung | 27,9 | 102,7 | 2523 | 33,7 |
| K3 | high | 4 luồng chung | 14,4 | 90,9 | 2469 | 32,3 |
| K4 | low | tải 3 | 5,5 | 83,5 | 2383 | 30,5 |
| K4 | low | tải 3 | 6,0 | 88,3 | 2260 | 27,5 |
| K4 | low | tải 3 | 49,3 | 150,3 | 2984 | 29,5 |

Effort high chỉ thêm ~200–250 token suy luận (reasoning) cho prompt này; chênh lệch tốc độ không đáng kể. [CHƯA KIỂM] effort max, prompt dài, và nhiều giờ khác nhau (mới đo trong ~10 phút, 10:53–11:03).

## `gpt-6-astra`
503 trên cả 3 khóa, ở lúc 10:53–10:59 (4 luồng) và 11:02 (đơn lẻ), phản hồi trong ~1,4 s. Không phải lỗi khóa (cùng khóa gọi sol bình thường). [CHƯA KIỂM] có phải xingchi chưa bật model hay tạm ngưng. Hệ quả: A-11b (bài sâu astra) và việc dùng astra làm trợ lý điều phối bị chặn.

## Tốc độ thực của worker (từ log codex, `tasks_stats.py`)
Token ra/giây tính trên toàn thời gian task (gồm chạy lệnh, build, chờ): A-12 25,0; E-03 23,5; D-01 32,9; E-01 34,4; C-01 34,4; A-07 15,0; A-02 8,4; B-02 5,5; B-02c 11,2; A-14 14,9. Task nặng đọc mã (A-02, B-02, A-07b) chỉ 5–9 tok/s với 4,4–13,9 triệu token vào (phần lớn là cache). Log codex không có mốc thời gian từng sự kiện nên **không tách được** tỉ lệ chờ model so với chờ lệnh [CHƯA KIỂM]; suy luận gián tiếp: tok/s thấp đi cùng số lệnh gọi công cụ cao (B-02: 56 lần, A-07b: 77 lần).

## Giá
Hệ số nhóm "Tổ chức từ thiện GPT" là 0,25× giá niêm yết. Đơn giá niêm yết/triệu token của sol: [CHƯA KIỂM] (chưa đối chiếu bảng giá/dashboard xingchi, không tự bịa số).

## Kết luận nút cổ chai
Tốc độ sinh (~30 tok/s) cố định và không đổi theo khóa/tải 3; chờ token đầu (TTFT, 5–49 s) là biến động lớn nhất cho mỗi lượt gọi; với worker thật, số vòng gọi và ngữ cảnh lớn quyết định thời gian.

## Khuyến nghị sơ bộ theo loại việc
- Khảo sát tĩnh/đọc mã (A-xx, E-07, E-08): giới hạn ngữ cảnh đưa vào (chỉ file cần), nêu rõ file:dòng để giảm số vòng đọc; effort high là đủ, không dùng max.
- Viết/sửa mã + build (B-02x): tách task nhỏ theo module; build chạy nền, tránh model chờ lệnh.
- Viết báo cáo dài (>3k token ra): ~100 s/3k token, chấp nhận; chia 2 task nếu cần dưới ~5 phút.
- Điều phối: chưa dùng được astra (503); tạm để Sonnet làm.
- Song song: 3 luồng/khóa không giảm tốc, không thấy 429 → giữ ≤3 worker/khóa là hợp lý.
