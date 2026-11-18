# NHẬT KÝ HỎI ĐÁP KIẾN THỨC GAME (Chat chấm)

| # | giờ | câu hỏi (lời người chơi) | đáp án của Sonnet | nguồn | đường tra | tin cậy | chấm | nguyên nhân lỗ hổng / vì sao được | cách vá |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2026-11-17 16:03 (giờ UTC; 23:03 địa phương) | "Hệ thống skill nhân vật, môn phái Võ Đang có những nhánh skill nào, mỗi nhánh bao nhiêu skill, cấp độ học của từng skill?" | Trả lời được một phần: wudang.lua có 45 bản ghi, bảng ReqLevel theo ID, có ID trùng, mốc 120/150 nghi là bản mở rộng; CHƯA chia được nhánh | S-01 (sau đó), `REPORTS/A-0x`, wudang.lua | đã tra báo cáo, KHÔNG tra `knowledge/skills/bang-ky-nang-cap-200.md` | thấp | Một phần | (1) báo cáo bỏ sót một môn phái; (2) không có cột nhánh; (3) tên chưa giải mã GBK/TCVN3; (4) `knowledge/` chưa có trong MUC-LUC-TRI-THUC | thêm `knowledge/` vào MUC-LUC (xong 18/11); S-01 đã làm `DESIGN/BANG-KY-NANG-THEO-PHAI.md` (16 phái, 11 có catalog); K-03 giải mã tên; nhánh chia sau khi K-03 xong |
