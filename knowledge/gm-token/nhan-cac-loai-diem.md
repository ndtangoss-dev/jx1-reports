# GM: Nhận Các Loại Điểm (menu con)

Ngày: 2026-11-12 | Build: Fix36 + p46 diag | Đường dẫn: Lệnh bài GM > Nhận Các Loại Điểm

## Các mục (theo nhãn đã quan sát)
| Mục | Phân loại | Trạng thái | Bằng chứng / ghi chú |
|---|---|---|---|
| Nhận Cấp Độ | GAME_STATE_CHANGE | VERIFIED | Hộp nhập "Nhap Cap Do" có ô số, nút "Xác nhận", "Hủy bỏ" (p46qa-20.png, p46qa-22.png). Nhập 200, xác nhận: chat hệ thống "Đẳng cấp của Bạn thăng lên đến 196...200" (p46qa-28.png); HUD từ Cấp 1, HP 204/204 sang Cấp 200, HP 1000/1000 (p46qa-14.png so với p46qa-60.png). Giá trị tối đa hợp lệ: UNKNOWN (mới thử 200). Hoàn tác (hạ cấp): chưa xác minh. |
| Các Loại Điểm | GAME_STATE_CHANGE | DISCOVERED | Sau thao tác Haiku, chat báo "Bạn nhận được 10000000 lượng bạc!" và "Bạn nhận được 10000 Xu!", hành trang từ 100 lượng / 0 Xu lên "1000 vạn 100 lượng" / "1 vạn Xu" (p46qa-70.png). Chưa rõ chính mục này hay mục khác trong menu đã cho tiền; cần Haiku ghi rõ nút đã bấm. Điểm kỹ năng, điểm thuộc tính từ mục này: chưa kiểm (bảng kỹ năng cho thấy "Điểm kỹ năng 199", p46qa-28.png, có thể do lên cấp). |
| Nhận Kỹ Năng 15x | GAME_STATE_CHANGE | DISCOVERED | Sau đó bảng kỹ năng có 23 kỹ năng, mỗi cái cấp 20 (p46qa-28.png). Chưa xác minh 23 kỹ năng này có đúng là bộ "15x" hay là tất cả kỹ năng môn phái Kim ở cấp 20: UNKNOWN. Nhãn "15x" chưa rõ nghĩa. |
| Trang trước | READ_ONLY | NOT_TESTED | Điều hướng trang. Có trang kế/các mục thêm: UNKNOWN. |
| Đóng | READ_ONLY | NOT_TESTED | |

## Việc cần làm
- Haiku mở lại menu và chụp từng trang, ghi đúng nhãn mọi nút (kể cả trang sau "Trang trước"); không bấm lại mục đã dùng nếu có nguy cơ trùng.
- So sánh trạng thái trước/sau từng mục: điểm thuộc tính, điểm kỹ năng, tiền, xu.
