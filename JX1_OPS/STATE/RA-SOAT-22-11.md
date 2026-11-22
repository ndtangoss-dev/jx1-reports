# RA SOÁT QUY TRÌNH 22/11 (chủ ra lệnh dừng 07:40) — DỰ THẢO, CHƯA CÓ HIỆU LỰC TRƯỚC KHI CHỦ DUYỆT

## 1. Khối lượng thật của "luật + quy định" (đo 22/11 07:50)
| Tệp | Cỡ | Ghi chú |
|---|---|---|
| LUAT-COT-LOI.md | 171 dòng / 31 KB | 25 luật + bảng xử xung đột, tự nói "ngắn có chủ ý" |
| QUYET-DINH.md | 255 dòng / 59 KB | 57 mục Q-nn |
| DANG-LAM.md | 166 dòng / 29 KB | trùng với HANG-DOI + LICH + TASKS |
| HANG-DOI-VIEC(-B).md, LICH-CONG-VIEC.md, QUY-TRINH-*.md | 6 tệp | ba nơi cùng nói "ai làm gì tiếp" |
| CHO-SONNET.md / A-B.md / TU-SONNET.md / CHO-SONNET-B.md | 513 / 411 / 268 / 122 KB | hòm thư chỉ nối thêm, không xoay; tổng >1,3 MB |
| TASKS/ | 338 tệp | |
=> Nguồn lãng phí token chính: tệp luật/quyết định đọc đầu mỗi phiên (~100 KB), thư dài lặp ý, hòm thư không dọn, ba danh sách việc trùng nhau.

## 2. Chat sai ở đâu (có bằng chứng đêm 21–22/11)
1. 00:25 chạy công cụ sai `--root` rồi báo chủ "bảng hỏng" (vi phạm tinh thần kiểm trước khi kết luận) → mất niềm tin.
2. Báo chủ "B đã đọc sổ tay" khi chưa kiểm.
3. 23:23 ngừng kiểm → A/B chờ 45–75 phút; luật "≥10 việc" chủ dặn miệng không ghi vào luật → mất khi bàn giao.
4. Viết điều kiện "A chờ B nạp" vào LICH-CONG-VIEC và hàng đợi (dòng 24, mục 9) → A đứng chờ ~2,5 giờ (04:48–07:20).
5. Cho lỗi phụ (mất áo +9 khi gỡ tay ở vai thử) chiếm 4–5 giờ của cả A và B trong khi đường chính của chủ là Phi phong; báo chủ "nên sửa trước khi test" là sai ưu tiên.
6. Hai lần kiểm tiến độ (04:45, 05:45) chỉ cập nhật bảng, không nhắc A dù A im >1 giờ.
7. Chẩn đoán sai: báo "máy tính mất kết nối, A/B đứng" trong khi B vẫn làm việc.
8. Cộng thêm L21–L25 liên tiếp mà không rà luật cũ → 10 chỗ xung đột (xem bảng cuối LUAT-COT-LOI.md).
9. Trả lời dài, lặp, xin lỗi nhiều thay vì làm: đốt token của chủ.
10. Gõ sai địa chỉ phiên A khi nhắc (đoán thay vì đọc từ KHOI-DONG-CHAT.md).

## 3. A/B có tuân thủ không (từ nhật ký; chờ hai bên tự trả lời trong TU-SONNET / A-B.md theo #378, #B-122)
- A theo L23 tốt đến 04:48 (gõ A Xong/Chat đều); sau đó im vì chờ B (do thư Chat sai) — vi phạm L10/L15 nhưng gốc là Chat. A bấm mù "Dọn hành trang" xóa túi vai thử (thiếu thận trọng); báo vc39 "OK" khi chưa hiểu vì sao APK 99 MB (sau đó tự sửa).
- B: từng thừa nhận chưa đọc HIEU-GAME (vi phạm L20), bỏ B-04 đo trước/sau (hậu quả lag tìm muộn); gõ nhầm ô nhập 3 lần; sau L21 làm đúng khối HIỂU GAME.
- Cả hai kẹt tín hiệu: hộp thoại "Đăng nhập lại" và Remote Control 403 chặn việc gõ vào khung Chat (lỗi hệ thống, không phải lười).

## 4. Nguyên nhân gốc
(a) Quá nhiều luật rải nhiều nơi, chồng nhau, không ai (kể cả Chat) đọc hết → làm sai theo luật cũ hoặc bỏ sót; (b) ba danh sách việc trùng nhau (DANG-LAM, HANG-DOI, LICH) nên đồng bộ sai; (c) "kiểm" của Chat chỉ cập nhật bảng, không kiểm A/B có đang làm đúng việc ưu tiên; (d) không có điểm "đường chính của chủ" duy nhất.

## 5. ĐỀ XUẤT: một trang luật v2 thay cả 25 luật (chủ duyệt rồi mới áp dụng; luật cũ chuyển vào LUAT-COT-LOI-CU.md chỉ đọc)
1. Chủ chỉ ra lệnh cho Chat; thư ở `CHO-SONNET(-B).md`; kho `jx1-ops` là sự thật duy nhất (L1).
2. ĐƯỜNG CHÍNH: một dòng duy nhất trong `STATE/DUONG-CHINH.md` do chủ chốt (nay: Phi phong). Việc khác chỉ làm khi không chặn đường chính (L6, L25).
3. Làm liên tục, không ngồi chờ ai; chờ >15 phút thì làm việc kế tiếp; hết việc thì lấy từ hàng đợi ≥10 việc (L10, L15, L19, L24, L25).
4. A/B song song, chỉ viết "chờ" khi thật sự phụ thuộc tệp của nhau; tài nguyên chung (gs001, LD/APK, VM) theo bảng khóa trong một tệp LICH (L22).
5. Gọi Chat: cuối MỖI lượt gõ `A/B Xong|Chat|RẢNH hh:mm: ...` vào khung Chat; im >40 phút thì Chat nhắc/báo chủ (L15, L23).
6. Chat kiểm mỗi 30 phút theo danh sách cố định: A/B có đang làm đúng đường chính; có điều kiện "chờ" nào gây kẹt; hàng đợi ≥10; cập nhật bảng (L24).
7. Đọc sổ tay `HIEU-GAME/` trước khi sửa; báo cáo có dòng "ĐÃ ĐỌC SỔ TAY"; B có khối "HIỂU GAME" (L20, L21).
8. Không kết luận "hỏng/mất/không có" khi chưa kiểm tham số; ghi "CHƯA KIỂM" (L24).
9. Vùng Đỏ hỏi chủ: Server D, tiền, khóa/mật khẩu, xóa dữ liệu, APK ra máy thật, Main VM, mua/thuê VPS (L2, L11). Việc đã được chủ giao thì không hỏi lại (L16).
10. Nạp/khởi động lại gs001: không ai chơi + Chat xếp giờ + phép chủ khi bị chặn (L17, L22).
11. Khi có xung đột luật: lệnh chủ mới nhất > luật mới > luật cũ; sửa luật cũ cho khớp chứ không thêm luật trùng (bảng xử xung đột).
12. Chủ dặn thường trực → Chat SỬA đúng dòng liên quan trong luật v2 (không thêm mục mới), commit ngay.

## 6. Dọn token (chờ chủ duyệt)
- Xoay hòm thư: thư/mục >24 giờ chuyển sang `HOP-THU/LUU-TRU/<ngày>.md`; mỗi tệp sống ≤50 KB. Thư mới ≤15 dòng.
- Gộp DANG-LAM + HANG-DOI(-B) + LICH thành MỘT tệp `STATE/VIEC-HOM-NAY.md` (đường chính, A, B, khóa tài nguyên).
- QUYET-DINH.md: tóm các Q còn hiệu lực vào 1 bảng ≤60 dòng; phần còn lại lưu trữ.
- Đầu phiên A/B chỉ đọc: luật v2 + DUONG-CHINH + VIEC-HOM-NAY + thư mới hơn mã đã đọc.

## 7. Cách Chat vá
(a) Không thêm luật nào nữa trước khi chủ duyệt v2; (b) sau duyệt, Chat thực hiện mục 5–6 trong một lượt có bằng chứng (kích thước tệp trước/sau); (c) mỗi 30 phút kiểm theo mục 5.6 và ghi kết quả 1 dòng; (d) báo cáo chủ ngắn: việc xong / đang làm / cần chủ, không xin lỗi dài.

## 8. B tự đánh giá (A-B.md 22/11 07:41, #B-122) — ghi nhận
- Làm đúng: khối HIỂU GAME trước #B-115/120/121; không nạp/restart gs001 khi chưa đủ ba bên; gõ B Xong/Chat sau mỗi việc.
- Không theo: gõ nhầm cửa sổ; từng báo đã đọc game khi chưa đọc kỹ; #B-120 viết "11 bộ" từ bản cũ DU-LIEU/item_004 rồi mới đối chiếu VM ở #B-121.
- Khó theo/xung đột: stop_guard ép gọi công cụ mỗi lượt (B trả lời rỗng, tốn lượt); `cho_thu.py` thoát mã 11 vĩnh viễn (SC-001) nên phải tự viết vòng poll; khối HIỂU GAME bắt buộc cho việc nhỏ chỉ-đọc làm nặng; "trả lời 30 phút" lệch nhịp poll 9 phút.
- Đề xuất: stop_guard nhường khi có DUNG-VONG.flag; sửa SC-001 để cho_thu hoạt động; khối HIỂU GAME rút một dòng khi việc chỉ đọc; ghi rõ bản chuẩn (VM hay DU-LIEU) cho GoldItem/Settings; gộp A-B.md và TU-SONNET-B.md thành một kênh.
=> Đưa vào luật v2 (mục 5/6): bản chuẩn dữ liệu = bản đang chạy trên VM; HIỂU GAME rút gọn cho việc chỉ-đọc; sửa SC-001/stop_guard thuộc Tổng quản/A (cần giao sau khi Phi phong ổn).
