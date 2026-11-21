# LUẬT RIÊNG CỦA B — VIỆC ĐẦU TIÊN LUÔN LÀ ĐỌC HIỂU GAME (chủ chốt 21/11 22:02)

Lý do chủ nêu: B hay đọc ngược mã rồi đoán, không xem tài liệu về game; A trước đây cũng vậy (làm Cường hóa) nhưng từ khi đọc HIEU-GAME hiệu quả của A tiến triển rõ rệt. B phải làm theo cách đó.

## Quy tắc (bất biến, mạnh hơn L20 đối với B)
1. MỌI việc B nhận (đo, sửa, thử, phân tích, đọc mã, tìm lỗi, viết thư) — BƯỚC ĐẦU TIÊN là ĐỌC HIỂU GAME. Chưa xong bước này thì cấm chạy lệnh đo, cấm mở mã để đoán, cấm sửa, cấm build, cấm restart (trừ việc Chat ghi rõ là cấp cứu).
2. Đọc gì: `HIEU-GAME/README.md`, `THUAT-NGU.md`, `DO-CHAC.md`, rồi TOÀN BỘ sổ tay của các nhóm liên quan đến việc đó (không chỉ 1-2 file), và lịch sử đã làm (`FIX_HISTORY`, `TASKS`, `QUYET-DINH`, `TU-SONNET-B.md`) về chính phần này. Việc server/tick/giật/quái/gói tin: đọc cả nhóm 03, 04, 06, 07 trước.
3. Sau khi đọc, B viết khối "HIỂU GAME" vào đầu báo cáo (A-B.md hoặc TU-SONNET-B.md), gồm:
   - Game làm gì ở phần này (luồng từ người chơi bấm → client → gói → server → trả về), bằng lời của B, ngắn.
   - Phần nào ĐÃ có sổ tay/lịch sử nói thẳng; phần nào sổ tay THIẾU.
   - Giả thuyết của B và sổ tay nào ủng hộ/bác bỏ.
   - Dòng "ĐÃ ĐỌC SỔ TAY: <từng file>" (mỗi file 1 dòng, kèm 1 câu rút ra).
4. Chat kiểm khối này TRƯỚC. Thiếu, mỏng, hoặc đọc ít hơn mức cần = Chat trả lại, B chưa được làm bước tiếp. Báo "XONG" mà thiếu khối này = không tính.
5. Khi gặp việc mới giữa chừng (Chat giao thư mới, tình huống mới): lặp lại bước 1-3 cho phần mới, kể cả ngắn. Không dùng "đã đọc hôm qua" thay cho khối mới nếu phần đó khác.
6. Sổ tay sai/thiếu thì B sửa/bổ sung ngay (cùng commit) để công sức cộng dồn (L20.4).
7. Chat cũng bị ràng buộc: mỗi thư giao B phải có dòng "SỔ TAY LIÊN QUAN" và Chat không giao việc sửa mã khi chưa thấy khối HIỂU GAME của B.
