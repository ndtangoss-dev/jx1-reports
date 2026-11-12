# Điểm tiềm năng - quy luật đã xác minh (C2)

Build P47-diag, server 36Hz (VM thử), nhân vật jxt36a cấp 200 hệ Kim, tay không, ngày 2026-11-12. Số liệu: experiments/potential.csv (16 thí nghiệm, mỗi thuộc tính 3 lần +1 và 1 lần +10, ảnh s47-*). Chỉ số đọc từ ảnh bảng nhân vật. Tiềm năng trước thí nghiệm: 1100 (không phải ~100); sau: 1048; mỗi điểm cộng trừ đúng 1 tiềm năng.

| Thuộc tính | Tác dụng đo được (mỗi +1) | Kiểm tra +10 | Trạng thái |
|---|---|---|---|
| Thân pháp | Chính xác +8 mỗi điểm (144->152->160->168) | +10: 168->248 (+80) tuyến tính | VERIFIED |
| Thân pháp | Né tránh tăng chậm, khoảng 0,2-0,25/điểm (1502 ở 25-27, 1503 ở 28, 1505 ở 38) | khớp | VERIFIED (xấp xỉ, làm tròn) |
| Sức mạnh | Lực tay trái: 8/8 ở 35-38, 10/10 ở 48 (khớp floor(Sức/5)+1, giả thuyết theo 3 điểm dữ liệu); Công kích hiển thị 0/0 vì tay không | +10 | VERIFIED số đo; công thức DISCOVERED |
| Sinh khí | Sinh lực tối đa +9 mỗi điểm (2001->2010->2019->2028); Thể lực tối đa +1 mỗi điểm | +10: Sinh lực +90, Thể lực +10, tuyến tính | VERIFIED |
| Nội công | Nội lực tối đa +1 mỗi điểm (5735->5736->5737->5738) | +10: +10 | VERIFIED |

- Không đổi khi cộng: Chạy 20, Phòng thủ 9%, các kháng tính (hàn 2, lôi 27, hỏa -36, độc 60).
- Hiển thị: HP hiện tại không tăng theo mức tối đa tức thời (Sinh lực 1691 giữ nguyên khi tối đa lên 2118 lúc đó; đổi sau, UNKNOWN thời điểm).
- Chưa xác định (NOT_TESTED): ảnh hưởng của Sức mạnh lên sát thương (cần vũ khí); Thân pháp lên tốc độ đánh.
- Độ tin cậy: cao cho số tuyến tính, trung bình cho công thức làm tròn.
