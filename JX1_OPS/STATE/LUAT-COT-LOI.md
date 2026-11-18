# LUẬT CỐT LÕI (chủ chốt 18/11/2026, sáng) — ĐỌC ĐẦU TIÊN, KHÔNG ĐƯỢC QUÊN

File này ngắn có chủ ý. Đọc nó: đầu mỗi phiên, sau mỗi lần bị nén, trước khi dừng lượt. Không ai được sửa nghĩa các luật dưới đây trừ chủ (qua thư Chat).

## L1. Kênh làm việc
- Chủ CHỈ giao lệnh cho Chat. Chat viết thư vào `HOP-THU/CHO-SONNET.md`. Sonnet làm theo thư. Hòm thư (nhánh `jx1-ops`) là nguồn sự thật duy nhất; điều không có trong kho coi như chưa có.
- Nếu chủ vẫn nhắn thẳng trong Claude Code: ghi ngay vào `STATE/QUYET-DINH.md` (hoặc mục "CHỦ NÓI TRỰC TIẾP" trong `TU-SONNET.md`) rồi mới làm.
- Thư hiệu lực xem `HOP-THU/THU-HIEN-HANH.md`. Thư không sửa; thư mới ghi "thay thế/bổ sung #N".

## L2. Không treo
- Không bao giờ kết thúc lượt bằng câu hỏi, không dùng hộp chọn (Q-21). Việc làm lại được: tự quyết sau 10 phút, ghi `[TỰ QUYẾT]`. Chỉ chờ chủ với: Main VM, tiền vượt trần, khóa ngoài 20 khóa đã duyệt, xóa dữ liệu, phát APK mới cho chủ test. Đang chờ thì vẫn làm việc khác.
- Thẻ `[DUNG-CAN-CHU]` hiệu lực tối đa 60 phút; việc xong thì xóa ngay.
- Làm theo ĐỢT (Q-48, `STATE/QUY-TRINH-KHONG-NGUOI-GAC.md`): đọc hòm thư một lần, làm hết, ghi MỘT báo cáo "XONG ĐỢT #N" vào TU-SONNET.md, push, dừng. Không nhịp gác, không dòng chờ.
- KẸT CẦN QUYẾT: không hỏi chủ, không đứng chờ. Ghi mục `[HỎI-CHAT]` trong `HOP-THU/TU-SONNET.md` (vấn đề, các phương án, phương án khuyến nghị), push, rồi làm việc khác. Chat trả lời trong `CHO-SONNET.md` (thường ≤10 phút khi có việc mở, tối đa 30 phút) và ghi "Chat quyết thay chủ" vào QUYET-DINH. Quá 30 phút chưa có trả lời: làm theo phương án khuyến nghị nếu làm lại được. Chỉ vùng Đỏ mới lên chủ (qua Chat).
- KHÔNG gõ cửa, không người gác (Q-48). [HỎI-CHAT] ghi trong báo cáo đợt, không chặn đợt: nêu giả định, làm tiếp phần độc lập.
- KÉO HÒM THƯ SAU MỖI MỤC (không chờ xong cả thư): `git pull` jx1-ops; có thư mới thì đọc; thư mới quan trọng hơn thì làm trước. Thư tiêu đề có `[KHẨN]`: dừng mục đang làm ở điểm an toàn gần nhất và làm ngay; người gác thấy `[KHẨN]` thì đánh thức Sonnet.
- Không có người gác (JX-Guard đã tắt; khôi phục: `schtasks /Change /TN JX-Guard /ENABLE`). Tổng quản chạy lịch Windows, chỉ ghi tệp, không gọi claude; tiểu yêu chết thì Tổng quản tự chạy lại.

## L3. Chống quên khi bị nén
- TRƯỚC khi nén: ghi "ĐANG LÀM DỞ" (việc, bước, lệnh chạy lại) vào `STATE/TRANG-THAI.md`, push.
- SAU khi nén, đọc theo thứ tự: file này → `STATE/TIEN-DO.md` → `HOP-THU/THU-HIEN-HANH.md` + thư mới trong `CHO-SONNET.md` → `STATE/QUYET-DINH.md` → lịch sử chat Claude Code (`C:\Users\PC\.claude\projects\...\*.jsonl`) từ lần push cuối lùi 15 phút, tối thiểu 60 phút, tối đa 3 giờ; chỉ đọc tin của chủ và trả lời cuối của Sonnet, bỏ log/kết quả lệnh. Điều chủ nói mà chưa có trong kho thì ghi vào kho ngay.

## L4. Tiến độ
- `STATE/TIEN-DO.md` sinh TỰ ĐỘNG bằng script từ front-matter `TASKS/*.md` (không viết tay). Đầu file 3 dòng: ĐANG LÀM / KẾ TIẾP / BỊ CHẶN (vì sao). Dưới là một sơ đồ Mermaid ≤30 ô theo 3 chặng (#091), màu theo trạng thái, mũi tên = chặn; việc xong lâu gom thành một ô.

## L5. Chuẩn hóa = hiểu game
- "Chuẩn hóa" của chủ là MỘT việc: chuẩn hóa báo cáo của tiểu yêu để hiểu game, gồm (a) khuôn `DESIGN/CHUAN-BAO-CAO.md`, (b) GIẢI MÃ tên ra chữ đúng (Hán: GBK; Việt cũ: TCVN3) và ghi cả tên gốc, (c) SẮP dữ liệu theo cấu trúc game (ví dụ kỹ năng phái: chia nhánh, xếp theo cấp học; bộ trang bị: liệt kê món). Thư #099 nói Sonnet "hiểu lầm" là SAI, đã thay bằng #107.
- Mỗi đợt chuẩn hóa xong, Chat hỏi thử bằng câu của người chơi (`DESIGN/KIEM-TRA-KIEN-THUC.md`). Đạt = trả lời được từ kho, dẫn đúng file mang tên đó.

## L8. Khóa xingchi và tiểu yêu (Q-41, Q-44; chủ chốt lại 18/11 09:29)
- Trần: 20 khóa × 3 tiểu yêu = tối đa 60 tiểu yêu, miễn phân công hợp lý. Dùng nhiều khóa KHÔNG gây quá tải; 429/lỗi Responses là do xingchi quá tải phía họ.
- Chỉ tạo khóa mới khi: còn việc chờ giao VÀ mọi khóa hiện có đã đủ 3 tiểu yêu. Không tạo sẵn, không tạo hàng loạt.
- Giãn cách tạo khóa: tối thiểu 1 phút giữa hai khóa. Tạo xong ping /v1/models rồi mới giao.
- Cách tạo ghi ở `DESIGN/QUY-TRINH-TAO-KHOA.md`. Giá trị khóa chỉ nằm trong `C:\Users\PC\.jx1keys\`, không ghi vào kho/log, không in ra màn hình. Không cần hỏi chủ trong trần 20.
- Sống/chết tiểu yêu xét bằng tiến trình + log/nhịp (`D:\\JX-wt\\<ID>.nhip`), KHÔNG bằng commit. Im 20–60 phút mà tiến trình còn: chỉ báo, không giết. Im > 60 phút: giết, chạy lại. Tiểu yêu không commit được thì người gác/chay_codex commit hộ.
- Rải đều do CODE làm (chay_codex.ps1/guard/Tổng quản tự chọn khóa ít việc nhất, ≤3/khóa), không dựa vào trí nhớ. Không chạy tiểu yêu bằng khóa mặc định.

## L9. Tổng quản là người duy nhất quản tiểu yêu (chủ chốt 18/11 09:47)
- Sonnet KHÔNG giao tay tiểu yêu nữa (không gọi chay_codex.ps1 trực tiếp). Sonnet chỉ viết TASKS/<ID>.md (status ready) để Tổng quản giao.
- Tổng quản làm hết: giao việc, rải khóa (≤3/khóa, hết chỗ báo CẦN KHÓA MỚI), xét sống/im/treo/chết, chạy lại khi chết/429 (chờ tăng dần), commit hộ khi xong, cập nhật status.
- Tổng quản ghi sự kiện vào `STATE/TONG-QUAN-GHI.md`; Sonnet đọc khi bắt đầu đợt.
- Khi chủ (qua Chat) hỏi tình hình tiểu yêu: Sonnet lấy báo cáo của Tổng quản (`STATE/TIEN-DO.md` + bảng tiểu yêu do Tổng quản sinh) rồi báo lại, không tự đoán.

## L7. Kế thừa khi đổi tài khoản
- Gõ cửa đã bỏ (Q-48); không cần ghi GO-CUA.log.
- Chat mới: đọc `HOP-THU/KHOI-DONG-CHAT.md`. Sonnet mới: đăng nhập lại Claude Code rồi `/tiep-tuc`; file này tự hiện qua hook.

## L6. Ưu tiên (#091)
Hiểu game (chuẩn hóa) → đường truyền client-server + hiểu exe → tick/độ phản hồi/đồ họa. Chỉ làm bản A (qh9A).
