# NPC "Lễ Quan"

Ngày: 2026-11-12 | Build: Fix36 + p46 diag

- Tên hiển thị: nhãn trên bản đồ lớn là "Lễ Quan" (p46-m3.png). Tên trên đầu NPC trong màn hình game đọc là "Lệ Quan" / "Lễ Quan" tùy ảnh và độ phân giải (p46qa-08.png, p46qa-60.png, p46qa-22.png). Chưa xác định chữ gốc chính xác trong dữ liệu: ghi cả hai biến thể, UNKNOWN cho chính tả gốc. Khung mục tiêu trên HUD khi chọn NPC cũng cần chụp zoom để đối chiếu.
- Bản đồ: Ba Lăng Huyện. Tọa độ: 203/199 (khi nhân vật đứng cạnh, bảng GM ghi 203/199, p46qa-18.png).
- Cách tiếp cận: bản đồ lớn, nhập 203/199, Tìm tọa độ, Đóng; hoặc đi bộ tới sát NPC. Nhân vật jxt36a bắt đầu ngay cạnh NPC khi vào game (p46qa-08.png).
- Tương tác: chạm NPC mở hội thoại gồm Lệnh Bài GM / Sự kiện nạp thẻ đầu tiên / Hủy vật phẩm / Đóng.
- Kết quả: chọn "Lệnh Bài GM" thì thông báo hệ thống "Lệnh bài GM x 1" và vật phẩm vào hành trang (p46qa-14.png). Trạng thái: VERIFIED.
- Các mục "Sự kiện nạp thẻ đầu tiên", "Hủy vật phẩm": DISCOVERED, NOT_TESTED. "Hủy vật phẩm" có thể xóa vật phẩm (phân loại tạm IRREVERSIBLE_OR_RISKY theo nhãn, chưa xác minh): không bấm nếu chưa cần.
- Điều kiện: chưa biết giới hạn số lần nhận lệnh bài (UNKNOWN); nhận lại có được thêm hay không NOT_TESTED.
- Trạng thái tổng: VERIFIED cho việc nhận lệnh bài; còn lại DISCOVERED.
