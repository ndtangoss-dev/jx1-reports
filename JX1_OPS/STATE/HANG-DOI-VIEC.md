# HÀNG ĐỢI VIỆC KHÔNG-ĐỎ (Chat lập 18/11/2026 22:30; Sonnet làm theo thứ tự, KHÔNG BAO GIỜ hết việc)

Luật (Q-52): Sonnet không gõ "xong" vì "hết việc". Hết việc đang làm thì lấy việc kế tiếp trong hàng đợi này; hàng đợi cạn thì tự đề xuất 3–5 việc "hiểu game" mới từ mục "chưa kiểm" của các báo cáo (ghi vào cuối tệp này, đánh dấu [SONNET-THÊM]) rồi làm. Mỗi việc: tạo `TASKS/<mã>.md` để Tổng quản giao tiểu yêu; việc cần sửa mã hoặc chạm vùng Đỏ thì KHÔNG làm, ghi [CAN-CHU]. Việc đọc tĩnh, viết tài liệu, kiểm chéo, và thử trên `JX-Test-36` (trong phạm vi đã duyệt) là làm được. Báo cáo viết bằng lời thường, mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM, kèm file:dòng.

## Nguyên tắc chủ chốt (Q-52): HIỂU RỒI MỚI SỬA
Chủ và Chat thống nhất: hiệu ứng vũ khí sửa mãi không được vì chưa hiểu đủ. Từ giờ KHÔNG sửa mã hiệu ứng (client lẫn server) cho tới khi có tài liệu "hiểu" được Chat duyệt. Mọi lỗi hiển thị: mô tả, tái hiện được, giả thuyết có thể kiểm — rồi mới đề xuất sửa.

## Hàng đợi (thứ tự ưu tiên)
| # | Mã | Việc | Đầu ra | Ghi chú |
|---|---|---|---|---|
| 1 | W-01 (a-d đã tạo TASKS, Tổng quản giao) | **Hiểu trọn đường hiệu ứng vũ khí:** từ dữ liệu vật phẩm/ini → client nạp → NPC res → thứ tự vẽ → glow (+6/+12/+15) → sét dọc → khung/animation. Gộp H-04, H-14, BUG-002, L-01..L-03, J-01..J-05, K-02-* | `DESIGN/HIEU-HIEU-UNG-VU-KHI.md`: sơ đồ mermaid, bảng "ai vẽ cái gì, theo thứ tự nào, đọc tệp nào", danh sách giả thuyết lỗi mỗi giả thuyết có cách kiểm | KHÔNG sửa mã. Chia 3–4 tiểu yêu theo khúc (dữ liệu, nạp/res, vẽ/thứ tự lớp, animation) rồi gộp |
| 2 | W-02 | Kế hoạch tái hiện lỗi mất khung/nhảy khung trên Test-36 (LDPlayer) khi C01 đã chạy: các bước, ảnh/quay màn hình, số đo | `DESIGN/KE-HOACH-TAI-HIEN-HIEU-UNG.md` | Chạy sau C01; chỉ quan sát |
| 3 | G-01..G-06 | **Sổ tay hiểu game theo mảng**, mỗi mảng 1 tài liệu lời thường có thể kiểm: nhân vật & bộ phận; kỹ năng/môn phái; trang bị & thuộc tính; quái/NPC/bản đồ; nhiệm vụ & Lua; kinh tế (tiền/cửa hàng/rơi đồ) | `DESIGN/SO-TAY-<mảng>.md` + dòng vào `MUC-LUC-TRI-THUC.md` | Dựa trên K-02, I-0x, A-08..A-17 đã có; chỉ gộp, đối chiếu mã, đánh nhãn |
| 4 | V-01 | **Kiểm chéo chất lượng:** chọn 5 báo cáo đã gộp (ưu tiên H-04, A-05, K-02-nhan-vat, N-0x, R-07a), đối chiếu từng khẳng định có file:dòng với mã thật, đếm sai/thiếu | `REPORTS/KIEM-CHEO-01.md` | Phát hiện báo cáo sai trước khi tin tiếp |
| 5 | T-01 | Theo dõi giảm token (#183): số 429/Upstream/token mỗi việc sau khi áp dụng, so với trước | mục "kết quả" trong `TIEU-YEU-429-VA-TOKEN.md` | Cập nhật mỗi sáng |
| 6 | M-01 | Bảo trì: cập nhật mục lục tri thức, bảng tiến độ, dọn TASKS lệch trạng thái | commit nhỏ | Mỗi đợt |
| 7 | C-02..C-05 | Ca thử client C02, C04, C05 | — | CHƯA duyệt; chỉ làm khi Chat báo chủ duyệt |

## Việc Sonnet tự thêm
(trống)
