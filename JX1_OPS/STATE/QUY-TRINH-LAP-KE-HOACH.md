# QUY TRÌNH LẬP KẾ HOẠCH CHUNG A–B–CHAT (chủ chốt 21/11 22:23)

Lý do chủ nêu: Chat giao việc lẻ tẻ cho A và B rồi hai bên đụng nhau (dùng chung gs001 Test-36, đăng nhập, restart), rồi phải "ưu tiên" chữa cháy — không khoa học.

## Cách làm (thay cách giao việc từng thư lẻ)
1. GOM: Chat gom tất cả việc đang có và việc mới (của chủ, của A, của B) vào một danh sách.
2. HỌP BA BÊN bằng thư: Chat gửi A và B cùng một thư "ĐỀ XUẤT KẾ HOẠCH". Mỗi bên trả lời: (a) việc mình cần làm, (b) TÀI NGUYÊN dùng chung sẽ chạm (gs001/Test-36, restart, đăng nhập atest, LD, APK, file Lua/ini/binary trên VM, repo file), (c) thời gian ước tính, (d) việc phụ thuộc bên kia, (e) lúc nào cần bên kia KHÔNG online/KHÔNG đụng.
3. THỐNG NHẤT: Chat ghép thành `STATE/LICH-CONG-VIEC.md` (bảng theo thứ tự thời gian: việc, ai làm, tài nguyên, chạy song song được hay tuần tự, điều kiện bắt đầu/kết thúc). A và B đọc và trả lời "ĐỒNG Ý" hoặc nêu xung đột. Chỉ khi cả ba bên đồng ý mới giao.
4. GIAO: Chat giao theo lịch. Việc chạm tài nguyên chung đi tuần tự; việc không chạm tài nguyên chung chạy song song (A làm UI/APK, B đọc sổ tay/phân tích tĩnh/sửa mã trên worktree riêng).
5. CHỦ: việc cần chủ (test trên điện thoại, bấm cho phép) cũng nằm trong lịch với giờ ước tính; Chat báo chủ trước, không để A/B đứng chờ chủ.
6. THAY ĐỔI GIỮA CHỪNG: khi có việc mới, Chat chèn vào lịch, báo cả hai bên và ghi việc nào dời; không giao thư lẻ làm lệch lịch. Cấp cứu (ghi rõ) mới được chen ngang, và Chat ghi lại hệ quả cho bên kia.
7. KHÓA TÀI NGUYÊN: dùng bảng khóa trong LICH-CONG-VIEC.md. Ai cần gs001 chạm (restart/đăng nhập) phải ghi "GIỮ gs001: <ai>, <từ giờ>, <dự kiến>", làm xong ghi "TRẢ gs001". Bên kia không chạm khi đang bị giữ.
8. Chat tự điều phối sau khi lịch chốt, không để A/B tự tranh nhau.
