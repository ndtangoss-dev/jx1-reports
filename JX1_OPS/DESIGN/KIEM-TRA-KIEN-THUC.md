# KIỂM TRA KIẾN THỨC GAME (Chat hỏi, Sonnet trả lời, cùng vá lỗ hổng)

Mục đích (chủ giao 17/11 23:46): Chat cũng phải nắm tri thức game. Chat hỏi Sonnet bằng ngôn ngữ NGƯỜI CHƠI, xem hệ thống (báo cáo, MUC-LUC-TRI-THUC, đồ thị Graphify, dữ liệu game) có trả lời được không; không trả lời được thì tìm vì sao và vá; trả lời được thì ghi lại vì sao được. Nâng dần độ hiểu sâu.

## Quy trình mỗi câu
1. Chat đặt câu hỏi kiểu người chơi (vd "Bộ An Bang gồm những trang bị nào?"). Mỗi lần Chat xem báo cáo của Sonnet/tiểu yêu, hỏi thêm ÍT NHẤT 1 câu liên quan; chủ cũng có thể đặt câu.
2. Sonnet (hoặc 1 tiểu yêu) trả lời, BẮT BUỘC có: đáp án; NGUỒN (file dữ liệu game/báo cáo + dòng); đường tra (mục lục / đồ thị / báo cáo / phải đọc mã hoặc dữ liệu thô); thời gian tra; độ tin (chắc / chưa chắc / không biết). KHÔNG ĐOÁN: không có nguồn thì ghi "không biết".
3. Chat chấm: ĐẠT (đúng và có nguồn) / MỘT PHẦN / KHÔNG. Kiểm chéo bằng ít nhất một đường độc lập (dữ liệu game trong game, tiểu yêu thứ 2 trả lời riêng, hoặc chủ xác nhận).
4. Ghi vào `KIEM-TRA/NHAT-KY-HOI-DAP.md` (mẫu bên dưới). Mỗi dòng "KHÔNG/MỘT PHẦN" phải có "NGUYÊN NHÂN LỖ HỔNG" thuộc loại: (a) chưa có báo cáo; (b) có báo cáo nhưng mục lục không trỏ tới; (c) dữ liệu nằm ở file dữ liệu thô, chưa ai đọc; (d) báo cáo mâu thuẫn; (e) khác từ cách gọi của người chơi và tên trong file (thuật ngữ); và "CÁCH VÁ" (tạo task, thêm vào mục lục, thêm bảng thuật ngữ). Dòng ĐẠT ghi "vì sao được" (vd mục lục trỏ trúng H-0x) để giữ lại cách làm tốt.
5. Vá ngay: task nhỏ cho tiểu yêu, cập nhật MUC-LUC-TRI-THUC và BẢNG THUẬT NGỮ (tên người chơi ↔ tên trong file ↔ mã).
6. Chat thống kê mỗi giờ: số câu, tỉ lệ ĐẠT, nguyên nhân lỗ hổng nhiều nhất. Mục tiêu tăng dần tỉ lệ ĐẠT.

## Lưu ý tin cậy
- Server của dự án có thể khác bản chính thức bên ngoài (bản qh7, dữ liệu tự chỉnh): đáp án đúng là THEO DỮ LIỆU CỦA DỰ ÁN, không theo wiki/diễn đàn. Thông tin trên mạng chỉ để gợi ý thuật ngữ và đối chiếu, ghi rõ "tham khảo mạng".
- Chat chưa tìm thấy nguồn mạng đáng tin cho "bộ An Bang" (17/11 23:50): không đưa đáp án từ trí nhớ; chờ đáp án từ dữ liệu game.

## Mẫu một dòng trong NHAT-KY-HOI-DAP.md
`| # | giờ | câu hỏi (lời người chơi) | đáp án của Sonnet | nguồn | đường tra | tin cậy | chấm | nguyên nhân lỗ hổng / vì sao được | cách vá |`
