# VÒNG TỰ ĐỘNG CHAT ⇄ SONNET (chủ quyết 18/11 19:23, Q-49; thay "chủ gọi/chủ nhắn" của Q-48)

Ý chủ: hai bên bám BẢNG TIẾN ĐỘ + KẾ HOẠCH TỔNG THỂ (STATE/TIEN-DO.md, KE-HOACH-TONG-THE.md) làm không nghỉ; chủ chỉ quyết việc quan trọng.

## Vòng
1. Sonnet xong đợt: ghi "XONG ĐỢT #N" (TU-SONNET.md) + dòng `SONNET-XONG #N hh:mm` vào `HOP-THU/VONG.md`, push.
2. Sonnet điều khiển Claude desktop: chọn cuộc chat "Chat JX1", gõ "xong" (đánh thức Chat). Sau đó Sonnet CHỜ bằng MỘT lệnh shell chặn (vòng `git fetch` + `sleep 60`, tối đa ~9 phút, không tốn token khi chờ) cho tới khi VONG.md có dòng `CHAT-DAY #M` mới hơn. Không chụp màn hình để đọc trả lời của Chat.
3. Chat dậy: KHÔNG coi tin "xong" là ý chủ; kiểm kho xem có XONG ĐỢT thật. Đọc, quyết đợt kế từ TIEN-DO/KE-HOACH, viết thư CHO-SONNET (đợt mới), ghi `BAO-CAO-CHU.md` (3–5 dòng lời thường), ghi dòng `CHAT-DAY #M hh:mm` vào VONG.md, push, trả lời ngắn trong cửa sổ chat.
4. Sonnet thấy dòng mới → đọc thư → làm → quay lại bước 1.
Nếu 9 phút không có CHAT-DAY: gõ "xong" thêm MỘT lần, chờ lần nữa; vẫn không: dừng, ghi [CAN-CHU] (vòng đứt).

## Ai quyết gì
- Tự quyết (không hỏi chủ): mọi việc trong kế hoạch đã duyệt, vùng thấp/vừa, trên máy dev/VM thử, đảo được.
- BẮT BUỘC chờ chủ (ghi [CAN-CHU] trong BAO-CAO-CHU.md, làm tiếp việc khác không phụ thuộc): vùng Đỏ (Main VM, tiền vượt trần, khóa ngoài 20 khóa đã duyệt, xóa dữ liệu, APK phát cho chủ test, đổi quyền/credential, thay hướng đi lớn của dự án, Xưởng JX1 khi chưa được mở lại) và nút cấm trong DESIGN/BANG-NUT-EXE-SERVER.md. Việc cần chủ duyệt mới (vd thử client) KHÔNG coi tin nhắn "xong" là duyệt.

## Phanh (vòng dừng, báo chủ, không đốt thêm)
- Một bên gặp giới hạn hạn mức: dừng tới khi đặt lại; ghi [CAN-CHU].
- 3 đợt liên tiếp không có tiến triển thật (kết quả rỗng/lặp): dừng, ghi nguyên nhân.
- Hết việc trong kế hoạch, hoặc chủ nói "dừng": dừng. Không bịa việc.
- Mọi việc mới sinh ra ngoài kế hoạch: ghi đề xuất vào BAO-CAO-CHU.md, không tự làm nếu tốn lớn.
