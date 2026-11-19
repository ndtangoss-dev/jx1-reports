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
