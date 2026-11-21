# LG-07 Đo khung hình trên LD (22/11 01:13–01:28, vc38, atestqhhai, Ba Lăng Huyện)

Cách đo: bấm đi lại luân phiên 2 điểm trong 15 phút, ghi logcat thẻ JXPERF (tổng kết mỗi 5 giây) vào docs-analysis/out/lg07-jxperf.txt.
- 186 mẫu 5 giây, 51.415 khung. FPS thấp nhất 48,6; trung bình 55,2.
- Khung >40 ms: 128 (0,25%); >66 ms: 3; >100 ms: 0; khung dài nhất 93 ms.
- Texture: 77,0 MB → 78,6 MB sau 15 phút (+1,6 MB), purge=0 suốt, check=5 ms.
- [fix36]: không có dòng log thẻ fix36 nào, nên CHƯA xác nhận dọn texture chạy; purge=0 vì chưa chạm ngưỡng. Cần bài đo đi nhiều bản đồ để xác nhận.
Kết luận: mượt trong một bản đồ; chưa kiểm khi chuyển bản đồ.
