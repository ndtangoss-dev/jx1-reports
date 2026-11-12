# 47 - Nhật ký QA tự vận hành (Sonnet 5.5, claude-sonnet-5-5)

Câu đầu: model thật của người viết là Sonnet 5.5 (claude-sonnet-5-5). Build P47-diag, server 36Hz (VM thử), nhân vật jxt36a, LDPlayer 960x540.

## Mục 0 - Năng lực công cụ (kiểm tra 2026-11-12)
| Công cụ | Kết quả | Bằng chứng |
|---|---|---|
| Chụp màn hình (ldshot) | CÓ | s47-00.png, thấy HUD 180/195, HP 1692/2001 |
| adb tap | CÓ | run46 mở bản đồ lớn, tọa độ minimap đổi 180/195 -> 202/198 (s47-01.png) |
| Đọc log game | CÓ | diag1-prep.log ghi liên tục, dòng JXTRC trùng giờ thiết bị |
| screenrecord + OpenCV | CÓ (có điều kiện) | Start-Job làm ghi dừng sau 5 s (video 314 khung); Start-Process cho 18,5-30 s ở ~60 fps |
| input swipe, input text | CÓ | nhập tọa độ trong run46 |
| OCR | KHÔNG CÓ | đọc số bằng mắt qua ảnh |

## Mục 1 - Nhấp nháy (VERIFIED)
- r2 (đi 203->180): video 1100 khung/18,5 s, 8 nhóm khung mật độ viền giảm >20% (3-4 khung, ~50-67 ms); 7/8 khớp log khoảng trống R clear->R prep >20 ms (6 sự kiện 47-72 ms, 3-4 khung vẽ rto=0 bio=0).
- r3 (180->203): 1794 khung/30 s, 5 nhóm video, 3 khớp log (4 sự kiện).
- Run1 (22 lần đổi vùng): 23 khung bio=0, khoảng trống trung bình 21,8 ms, tối đa 65,6 ms.
- Đối tượng mất: toàn bộ cây, NPC, nhân vật và ngựa trong khung đó; còn nền, bóng, thanh máu (s47-cmp-r2.jpg khung 499/502/506).
- Kết luận: tái hiện được, ~6-8 sự kiện/20-30 s khi chạy ngựa; nguyên nhân gần là cây đối tượng xóa rồi dựng lại cách vài khung. Độ tin cậy cao. Đã báo main.
- Ghi chú phương pháp: lệch giờ video-log cố định 0,25-0,75 s.

## Mục 3 - Tiềm năng (VERIFIED, xem knowledge/stats/diem-tiem-nang.md, experiments/potential.csv). Tiềm năng còn 1048. Trạng thái dở: mục 2 (hồ sơ nhân vật) chưa lưu, mục 4 chưa làm. Đã chụp bảng nhân vật s47-10 (Sức 35, Thân 25, Sinh khí 25, Nội công 4910, cấp 200). Hiện đang tạm dừng để cài P47-test theo yêu cầu Opus.
