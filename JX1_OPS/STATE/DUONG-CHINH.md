# ĐƯỜNG CHÍNH (chủ chốt; một dòng duy nhất — Chat sửa khi chủ đổi)
22/11 07:55 — **PHI PHONG** (Cường hóa đã xong: chủ test OK 22/11 01:08, Q-108). A: client (PP-02, vc41…); B: hỗ trợ + kiểm server (PP-01, chỉ đọc/gs001 không nạp khi chưa đủ ba bên + phép chủ).
Chờ chủ quyết: nạp `checkpoint-b119c` (b113 + sửa ô give) lên gs001 — chủ duyệt sau khi test vc41.

**LỆNH CHỦ 22/11 08:03 — DỪNG SAU PHI PHONG:** khi xong (a) Phi phong M3 (vc42 + link) và (b) sách "Hỗ trợ Cường hóa" không mở được (#375) thì A và B DỪNG việc mới. Việc kế: A và B (và Chat) viết PHÂN TÍCH "vì sao lỗi #359 đã sửa mà bị lại": dòng thời gian file `qh_bothu.lua`/`baowubox.lua` trên VM (ai chép, lúc nào, bản nào), vì sao không có kiểm hồi quy, đề xuất ngăn tái phát. Chủ xem rồi mới cho chạy tiếp. Chat tạo `STATE/DUNG-VONG.flag` khi (a)+(b) xong.
Ghi chú: VPN trên máy chủ là Tailscale (cần cho forwarder/APK) — KHÔNG khuyên tắt.
