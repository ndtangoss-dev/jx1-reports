# HÀNG ĐỢI VIỆC KHÔNG-ĐỎ (Chat lập 18/11/2026 22:30; Sonnet làm theo thứ tự, KHÔNG BAO GIỜ hết việc)
> 19/11 17:10: ĐÂY LÀ HÀNG ĐỢI CỦA SONNET A. Của B: `STATE/HANG-DOI-VIEC-B.md`. Việc cha của A: A-07, A-07b, A-07c, B-02, B-04, CL-01, D-02, T-04, M-01, P-01, 0-08, O-01. Chờ chủ: B-05, X-05, C02/C04/C05.

Luật (Q-52): Sonnet không gõ "xong" vì "hết việc". Hết việc đang làm thì lấy việc kế tiếp trong hàng đợi này; hàng đợi cạn thì tự đề xuất 3–5 việc "hiểu game" mới từ mục "chưa kiểm" của các báo cáo (ghi vào cuối tệp này, đánh dấu [SONNET-THÊM]) rồi làm. Mỗi việc: tạo `TASKS/<mã>.md` để Tổng quản giao tiểu yêu; việc cần sửa mã hoặc chạm vùng Đỏ thì KHÔNG làm, ghi [CAN-CHU]. Việc đọc tĩnh, viết tài liệu, kiểm chéo, và thử trên `JX-Test-36` (trong phạm vi đã duyệt) là làm được. Báo cáo viết bằng lời thường, mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM, kèm file:dòng.

## Nguyên tắc chủ chốt (Q-52): HIỂU RỒI MỚI SỬA
Chủ và Chat thống nhất: hiệu ứng vũ khí sửa mãi không được vì chưa hiểu đủ. Từ giờ KHÔNG sửa mã hiệu ứng (client lẫn server) cho tới khi có tài liệu "hiểu" được Chat duyệt. Mọi lỗi hiển thị: mô tả, tái hiện được, giả thuyết có thể kiểm — rồi mới đề xuất sửa.

## Hàng đợi (thứ tự ưu tiên)
| # | Mã | Việc | Đầu ra | Ghi chú |
|---|---|---|---|---|
| 1 | W-01 (XONG 18/11 23:40: a-d đã gộp, `DESIGN/HIEU-HIEU-UNG-VU-KHI.md`) | **Hiểu trọn đường hiệu ứng vũ khí:** từ dữ liệu vật phẩm/ini → client nạp → NPC res → thứ tự vẽ → glow (+6/+12/+15) → sét dọc → khung/animation. Gộp H-04, H-14, BUG-002, L-01..L-03, J-01..J-05, K-02-* | `DESIGN/HIEU-HIEU-UNG-VU-KHI.md`: sơ đồ mermaid, bảng "ai vẽ cái gì, theo thứ tự nào, đọc tệp nào", danh sách giả thuyết lỗi mỗi giả thuyết có cách kiểm | KHÔNG sửa mã. Chia 3–4 tiểu yêu theo khúc (dữ liệu, nạp/res, vẽ/thứ tự lớp, animation) rồi gộp |
| 2 | W-02 (XONG phần quan sát 19/11) | Kế hoạch tái hiện lỗi mất khung/nhảy khung trên Test-36 (LDPlayer) khi C01 đã chạy: các bước, ảnh/quay màn hình, số đo | `DESIGN/KE-HOACH-TAI-HIEN-HIEU-UNG.md` | Chạy sau C01; chỉ quan sát |
| 3 | SO-01..SO-06, HG-01..HG-05, KC-01, KC-02 (thay G-01..G-06; #196) | **Sổ tay hiểu game theo mảng** (nhân vật, kỹ năng, trang bị, đăng nhập, chiến đấu, bảng item, cường hóa Lua). 19/11 00:30: SO-01..03, HG-01, HG-04 đã gộp; **HG-02b, HG-03b** (làm lại có đường dẫn nguồn tuyệt đối), HG-05, KC-01, KC-02, SO-04..06 đang chạy | `DESIGN/SO-TAY-*.md`, `HIEU-*.md` | Tiểu yêu làm; Sonnet gộp khi XONG-CHO-GOP |
| 4 | V-01 | **Kiểm chéo chất lượng:** chọn 5 báo cáo đã gộp (ưu tiên H-04, A-05, K-02-nhan-vat, N-0x, R-07a), đối chiếu từng khẳng định có file:dòng với mã thật, đếm sai/thiếu | `REPORTS/KIEM-CHEO-01.md` | Phát hiện báo cáo sai trước khi tin tiếp |
| 5 | TK-01 (thay T-01; XONG 19/11: 7 nhật ký, 0 lần 429, 7 Upstream, token vào TB 2,71 triệu) | Theo dõi giảm token sau Q-51/#195 | `REPORTS/TIEU-YEU-TOKEN-THEO-DOI-01.md` | Lặp lại mỗi sáng nếu còn đáng đo |
| 6 | M-01 | Bảo trì: cập nhật mục lục tri thức, bảng tiến độ, dọn TASKS lệch trạng thái | commit nhỏ | Mỗi đợt |
| 7 | C-02..C-05 | Ca thử client C02, C04, C05 | — | CHƯA duyệt; chỉ làm khi Chat báo chủ duyệt |

## Việc Sonnet tự thêm
Làm được ngay (Sonnet, không chờ tiểu yêu): (a) #193 còn lại: SHA APK trong T36test, quay video H4/H5; (b) V-01 kiểm chéo 5 báo cáo; (c) M-01 mục lục/bảng tiến độ mỗi đợt; (d) gộp XONG-CHO-GOP khi có; (e) #199 các đề xuất bằng mã.
Chờ tiểu yêu: HG-02b, HG-03b, HG-05, KC-01, KC-02, SO-04..06 (8 việc đang chạy, tối đa 2/khóa, 5 khóa).
Chờ chủ duyệt: C-02, C-04, C-05; #134; Xưởng JX1; nhân vật thứ 4.
