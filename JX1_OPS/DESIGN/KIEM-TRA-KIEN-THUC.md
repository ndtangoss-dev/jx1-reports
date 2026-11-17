# KIỂM TRA KIẾN THỨC GAME (Chat hỏi, Sonnet trả lời, cùng vá lỗ hổng)

Mục đích (chủ giao 17/11 23:46): Chat cũng phải nắm tri thức game. Chat hỏi Sonnet bằng ngôn ngữ NGƯỜI CHƠI, xem hệ thống (báo cáo, MUC-LUC-TRI-THUC, đồ thị Graphify, dữ liệu game) có trả lời được không; không trả lời được thì tìm vì sao và vá; trả lời được thì ghi lại vì sao được. Nâng dần độ hiểu sâu.

## Quy trình mỗi câu
0. TRƯỚC KHI HỎI, Chat hỏi Sonnet: việc chuẩn hóa dữ liệu (UTF-8/TCVN3) đã xong chưa, xong phần nào (tỉ lệ/ngày giờ, nhóm file nào đã chuẩn, nhóm nào chưa). Chưa xong thì chỉ hỏi trong phần đã chuẩn hóa xong hoặc chờ; không chấm SAI vì lý do dữ liệu chưa chuẩn (ghi là 'chờ chuẩn hóa').
1. Chat đặt câu hỏi kiểu người chơi (vd "Bộ An Bang gồm những trang bị nào?"). Mỗi lần Chat xem báo cáo của Sonnet/tiểu yêu, hỏi thêm ÍT NHẤT 1 câu liên quan; chủ cũng có thể đặt câu.
2. Sonnet (hoặc 1 tiểu yêu) trả lời, BẮT BUỘC có: đáp án; NGUỒN (file dữ liệu game/báo cáo + dòng); đường tra (mục lục / đồ thị / báo cáo / phải đọc mã hoặc dữ liệu thô); thời gian tra; độ tin (chắc / chưa chắc / không biết). KHÔNG ĐOÁN: không có nguồn thì ghi "không biết".
3. Chat chấm: ĐẠT (đúng và có nguồn) / MỘT PHẦN / KHÔNG. Kiểm chéo bằng ít nhất một đường độc lập (dữ liệu game trong game, tiểu yêu thứ 2 trả lời riêng, hoặc chủ xác nhận).
4. Ghi vào `KIEM-TRA/NHAT-KY-HOI-DAP.md` (mẫu bên dưới). Mỗi dòng "KHÔNG/MỘT PHẦN" phải có "NGUYÊN NHÂN LỖ HỔNG" thuộc loại: (a) chưa có báo cáo; (b) có báo cáo nhưng mục lục không trỏ tới; (c) dữ liệu nằm ở file dữ liệu thô, chưa ai đọc; (d) báo cáo mâu thuẫn; (e) khác từ cách gọi của người chơi và tên trong file (thuật ngữ); và "CÁCH VÁ" (tạo task, thêm vào mục lục, thêm bảng thuật ngữ). Dòng ĐẠT ghi "vì sao được" (vd mục lục trỏ trúng H-0x) để giữ lại cách làm tốt.
5. Vá ngay: task nhỏ cho tiểu yêu, cập nhật MUC-LUC-TRI-THUC và BẢNG THUẬT NGỮ (tên người chơi ↔ tên trong file ↔ mã).
6. Chat thống kê mỗi giờ: số câu, tỉ lệ ĐẠT, nguyên nhân lỗ hổng nhiều nhất. Mục tiêu tăng dần tỉ lệ ĐẠT.

## Lưu ý tin cậy
- Server của dự án có thể khác bản chính thức bên ngoài (bản qh7, dữ liệu tự chỉnh): đáp án đúng là THEO DỮ LIỆU CỦA DỰ ÁN, không theo wiki/diễn đàn. Thông tin trên mạng chỉ để gợi ý thuật ngữ và đối chiếu, ghi rõ "tham khảo mạng".
- Chủ chốt (17/11 23:48): nguồn chuẩn để đối chiếu là VINAGAME (nhà phát hành VLTK). Chat ưu tiên trang/tài liệu Vinagame; nếu chỉ tìm được trang người chơi chép lại, ghi rõ "nguồn thứ cấp" và phiên bản.
- Đáp án đúng cuối cùng vẫn là DỮ LIỆU CỦA DỰ ÁN (đối chiếu hai bên; khác nhau thì ghi chênh lệch, không tự sửa).

## ĐÁP ÁN THAM KHẢO (nguồn mạng, KHÔNG phải đáp án của dự án; Sonnet trả lời từ dữ liệu game TRƯỚC, rồi Chat mới đối chiếu)
- Câu 1 (bộ An Bang), 17/11 23:58: gamemoira.org "Trang Bị Hoàng Kim An Bang phiên bản CTC - VLTK (JX1)" (đăng 13/11/2019, nguồn thứ cấp, bản Công Thành Chiến): bộ Hoàng Kim An Bang gồm 4 loại: Hạng Liên, Ngọc Bội, Nhẫn (Thủy), Nhẫn (Hỏa); mặc 4 món cùng loại và cấp thì kích hoạt thuộc tính của cả bộ; mỗi món cấp 1-5, dòng thuộc tính cố định theo loại, mọi món đều có Nội lực và Sinh lực 161-200; không phân biệt môn phái. Ví dụ Hạng Liên cấp 1: kháng tất cả 16-20, kháng lôi 11-15, thời gian trúng độc 2-10. Trang không nói có món nào khác ngoài 4 món này. Bản CTC có thể khác bản của dự án (qh7). Cách lấy: đồ phổ Hoàng Kim + Mảnh Hoàng Kim (An Bang cần 6 mảnh/món theo trang tinh luyện của gamemoira) tại Thợ rèn thần bí Lâm An.

## Mẫu một dòng trong NHAT-KY-HOI-DAP.md
`| # | giờ | câu hỏi (lời người chơi) | đáp án của Sonnet | nguồn | đường tra | tin cậy | chấm | nguyên nhân lỗ hổng / vì sao được | cách vá |`

## TIÊU CHÍ CHẤM (chủ chốt 17/11 23:53, thay cho phần kiểm chéo nặng ở trên)
- Chat chỉ cần nắm SƠ BỘ về game, không cần chuẩn từng chi tiết; không sa đà tìm nguồn mạng. Dữ liệu của chủ đã/đang được chuẩn hóa UTF-8 và TCVN3 bởi Sonnet (quy trình chủ đưa), nên dữ liệu dự án là nguồn đúng.
- Nếu bản của chủ khác bản mạng (vd bộ An Bang nhiều món hơn): Sonnet phải DẪN ĐƯỢC tới các file/mục dữ liệu có tên "An Bang" (gồm cả tên chuẩn hóa/TCVN3/tên Hán nếu có), liệt kê món từ đó. ĐÚNG = dẫn được tới đúng các file/mục mang tên đó và đáp án khớp nội dung file. SAI = đưa ra tên khác không có trong file, đoán, hoặc không dẫn được file.
- Chat không tự quyết đúng sai theo trí nhớ/mạng; chấm theo: có dẫn đúng file mang tên đó không, đáp án có khớp file không. Đáp án mạng chỉ là gợi ý thuật ngữ.
- Chủ sẽ xem cách Chat và Sonnet tương tác rồi tối ưu bài test cho Chat; Chat ghi lại những chỗ vướng khi chấm (khó chấm, câu hỏi chưa rõ) vào cuối NHAT-KY-HOI-DAP.md để chủ tối ưu.
