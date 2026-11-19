# TRẠNG THÁI TESTER (cập nhật liên tục)
- Tester: tester01 = LD `T36-tester01` (index 2, adb emulator-5558, cửa sổ ẩn), tài khoản `tester01` riêng; TASKS/TS-01.md status ready, chờ Tổng quản sinh tiểu yêu xingchi (19/11 10:10)
- Tài khoản/nhân vật: tester01 đã tạo trong DB Test-36 (nhân bản từ testa, chưa có nhân vật)
- Đang ở bước: chưa bắt đầu
- Việc dở: không
- Việc kế: Sonnet xong vũ khí #219 (đã xong 09:25) → giao tiểu yêu theo LOI-GIAO-VIEC.md; bảng môn phái đã điền (19/11 09:40)

## Điểm tiếp tục TS-01

- PARTIAL (19/11/2026): đã đối chiếu tài liệu bàn giao. Chưa chạy Test-36 trong lượt này, chưa xác minh bước chơi nào (0/7).
- Khi có lượt chơi thử, tiếp tục từ đăng nhập. Tra bảng môn phái và ngũ hành trước khi tạo nhân vật.
- Báo cáo: [TS-01](../../REPORTS/TS-01.md).

## 19/11 10:16 — cầu nối LD (Sonnet)
- `T36-tester01` (emulator-5558): client báo "Mất kết nối hoặc không đúng phiên bản" ở màn tải vì thiếu DNAT cổng CDN. Đã thêm `iptables -t nat -A OUTPUT -d 100.95.186.86 -p tcp --dport 8080 -j DNAT --to-destination 192.168.56.101:8080` (CDN tạm đã lắng nghe sẵn trên 192.168.56.101:8080). Sau đó vào được game (nhân vật hiển thị T36nv1, Ba Lăng Huyện, cấp 1). **Phải làm lại DNAT cả 3 cổng (56722, 51189, 8080) mỗi lần LD khởi động lại.**
- adb từ Sonnet chạy được (chụp màn hình, tap). Chưa rõ sandbox của tiểu yêu có cho adb không; TS-01 lượt 2 tự kiểm.

## Điểm tiếp tục TS-02 — 19/11/2026
- BLOCKED (19/11/2026): đã đọc task, lời giao việc, chỉ mục, trạng thái, nhật ký và bảng môn phái/ngũ hành; chưa chạy adb, mở LD, chụp màn hình hoặc đọc log theo giới hạn lượt này. Không phát sinh lỗi adb để ghi nhận.
- Chưa xác minh bước chơi nào (0/7). Task mô tả một phiên đã đăng nhập và có nhân vật, nhưng trạng thái bàn giao trước đó chưa xác nhận nhân vật cho tài khoản test; cần đối chiếu khi được tiếp tục.
- Báo cáo: [TS-02](../../REPORTS/TS-02.md).

## 19/11 11:35 — Sonnet chơi thật qua adb (tester01, bản vc22)
- Đã kiểm trong LD: đăng nhập vào Ba Lăng Huyện (1/7), nhân vật T36nv1 cấp 1 (2/7), đi bằng cần điều khiển (3/7), túi đồ + xem tooltip + trang bị Chùy/Yêu Đao bằng chạm→"Sử dụng" (4/7). Ảnh: `REPORTS/img/vk04-*`.
- Chưa: chiến đấu quái (cần ra ngoài thành), shop, nhiệm vụ (3/7 còn lại). Độ phủ 4/7.
