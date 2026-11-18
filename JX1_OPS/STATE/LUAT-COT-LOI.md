# LUẬT CỐT LÕI (chủ chốt 18/11/2026, sáng) — ĐỌC ĐẦU TIÊN, KHÔNG ĐƯỢC QUÊN

File này ngắn có chủ ý. Đọc nó: đầu mỗi phiên, sau mỗi lần bị nén, trước khi dừng lượt. Không ai được sửa nghĩa các luật dưới đây trừ chủ (qua thư Chat).

## L1. Kênh làm việc
- Chủ CHỈ giao lệnh cho Chat. Chat viết thư vào `HOP-THU/CHO-SONNET.md`. Sonnet làm theo thư. Hòm thư (nhánh `jx1-ops`) là nguồn sự thật duy nhất; điều không có trong kho coi như chưa có.
- Nếu chủ vẫn nhắn thẳng trong Claude Code: ghi ngay vào `STATE/QUYET-DINH.md` (hoặc mục "CHỦ NÓI TRỰC TIẾP" trong `TU-SONNET.md`) rồi mới làm.
- Thư hiệu lực xem `HOP-THU/THU-HIEN-HANH.md`. Thư không sửa; thư mới ghi "thay thế/bổ sung #N".

## L2. Không treo
- Không bao giờ kết thúc lượt bằng câu hỏi, không dùng hộp chọn (Q-21). Việc làm lại được: tự quyết sau 10 phút, ghi `[TỰ QUYẾT]`. Chỉ chờ chủ với: Main VM, tiền vượt trần, khóa ngoài 20 khóa đã duyệt, xóa dữ liệu, phát APK mới cho chủ test. Đang chờ thì vẫn làm việc khác.
- Thẻ `[DUNG-CAN-CHU]` hiệu lực tối đa 60 phút; việc xong thì xóa ngay.
- Nhịp: cứ 30 phút một dòng trạng thái + commit + push, kể cả khi chưa có gì mới. Im > 60 phút là lỗi quy trình.
- Có người gác ngoài Sonnet (script lịch, không tốn token): im > 30 phút thì gọi tiếp phiên với lệnh "đọc hòm thư, làm tiếp". Tiểu yêu chết thì người gác/Tổng quản tự chạy lại tối đa 2 lần, chờ tăng dần.

## L3. Chống quên khi bị nén
- TRƯỚC khi nén: ghi "ĐANG LÀM DỞ" (việc, bước, lệnh chạy lại) vào `STATE/TRANG-THAI.md`, push.
- SAU khi nén, đọc theo thứ tự: file này → `STATE/TIEN-DO.md` → `HOP-THU/THU-HIEN-HANH.md` + thư mới trong `CHO-SONNET.md` → `STATE/QUYET-DINH.md` → lịch sử chat Claude Code (`C:\Users\PC\.claude\projects\...\*.jsonl`) từ lần push cuối lùi 15 phút, tối thiểu 60 phút, tối đa 3 giờ; chỉ đọc tin của chủ và trả lời cuối của Sonnet, bỏ log/kết quả lệnh. Điều chủ nói mà chưa có trong kho thì ghi vào kho ngay.

## L4. Tiến độ
- `STATE/TIEN-DO.md` sinh TỰ ĐỘNG bằng script từ front-matter `TASKS/*.md` (không viết tay). Đầu file 3 dòng: ĐANG LÀM / KẾ TIẾP / BỊ CHẶN (vì sao). Dưới là một sơ đồ Mermaid ≤30 ô theo 3 chặng (#091), màu theo trạng thái, mũi tên = chặn; việc xong lâu gom thành một ô.

## L5. Chuẩn hóa = hiểu game
- "Chuẩn hóa" của chủ là MỘT việc: chuẩn hóa báo cáo của tiểu yêu để hiểu game, gồm (a) khuôn `DESIGN/CHUAN-BAO-CAO.md`, (b) GIẢI MÃ tên ra chữ đúng (Hán: GBK; Việt cũ: TCVN3) và ghi cả tên gốc, (c) SẮP dữ liệu theo cấu trúc game (ví dụ kỹ năng phái: chia nhánh, xếp theo cấp học; bộ trang bị: liệt kê món). Thư #099 nói Sonnet "hiểu lầm" là SAI, đã thay bằng #107.
- Mỗi đợt chuẩn hóa xong, Chat hỏi thử bằng câu của người chơi (`DESIGN/KIEM-TRA-KIEN-THUC.md`). Đạt = trả lời được từ kho, dẫn đúng file mang tên đó.

## L6. Ưu tiên (#091)
Hiểu game (chuẩn hóa) → đường truyền client-server + hiểu exe → tick/độ phản hồi/đồ họa. Chỉ làm bản A (qh9A).
