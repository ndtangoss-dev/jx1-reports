# THIẾT KẾ BOT v1 — CHỦ ĐÃ DUYỆT (19/11 08:41, Q-62). GIAO SONNET theo thư #220.
Nguồn: DESIGN/BOT/HE-THONG-BOT-3-LOAI.md (yêu cầu chủ). Mọi điểm [CHƯA KIỂM] do Sonnet khảo sát trước khi làm.

## Nguyên tắc
- Nhẹ nhất có thể; Bot không có dữ liệu túi tiền. Sonnet khảo sát và chọn hướng: (A) client ngoài server, hay (B) Bot trong server giống NPC mang hình người. Tiêu chí: số Bot gánh được, ảnh hưởng nhịp 18 Hz, độ khó sửa server (Q-26: chưa vá server cho tới khi cần).
- Giọng tiếng Việt: hảo hữu thân mật; giao dịch mời chào, gạ gẫm. Chat hiểu người chơi bằng luật từ khóa + kịch bản (không dùng AI lúc chạy).

## Giai đoạn
0. Nền: tester01 + 1 Bot đăng nhập, đi, đánh trên Test-36 (E-01/E-09). Khảo sát A/B cho dân số (số Bot tối đa, chi phí). 
1. Bot bán hàng 3a: file gia-vat-pham; kho bán hôm nay làm mới mỗi ngày; chat thế giới.
2. Bot dân số: sinh quanh người chơi, đi/đứng rồi đi.
3. Bot hảo hữu: bảng phái × đường; gõ "hảo hữu" → hiện cạnh người chơi; chọn vào party; tự theo + đánh; trang bị do người chơi; lên cấp như người; điểm tiềm năng/kỹ năng người chơi tự tăng cho Bot; tự chọn chiêu điểm cao; 1 Bot ↔ 1 người chơi, xóa account thì giải phóng.
4. Bot giao dịch 3b: chat lân cận/mật/thế giới, mặc cả có giá sàn, nhận biết đủ tiền trong ô giao dịch.

## File giá gia-vat-pham (chủ đã duyệt cấu trúc)
Cột: mã món, tên, loại, cấp, độ hiếm, giá gốc, hệ số bán, giá sàn mặc cả (vd 50%), thành thị bán, nhóm kho bán hôm nay. Sonnet dựng bản đầu (giá gốc lấy bảng vật phẩm game nếu có cột giá, còn lại theo công thức cấp/phẩm/loại); chủ sửa món quan trọng.

## Cổng duyệt (không qua cổng thì không sang giai đoạn)
- Sang GĐ1 khi: Bot vào server thật ổn, kết quả khảo sát A/B có số đo.
- Sang GĐ3 khi: tester/Bot đánh được thật và có bằng chứng nhóm party hoạt động.
- GĐ4 làm sau cùng, thử từng bước nhỏ (mặc cả trước, tiền trong ô giao dịch sau).
