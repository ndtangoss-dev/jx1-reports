# O-01 - Chat duyệt B-02 (trên REPORTS/B-02-tom-tat-diff.md, 05:30)

**Kết luận: DUYỆT CÓ ĐIỀU KIỆN cho thử trong VM thử (JX-Test-36). Chưa duyệt đưa vào bản chính.** Chat chưa đọc mã, chỉ duyệt trên tóm tắt.

Tốt: công tắc Enabled=0 trả đúng đường cũ ở mọi điểm móc; REMOVE không bị chặn bừa; kiểm m_dwID chủ chống tái dùng slot.

Điều kiện / rủi ro cần xử lý:
1. **REMOVE chỉ gửi nếu từng ADD (m_VisibleNpcs)**: nếu có đường gửi ADD chưa móc (còn các đường KNpc.cpp:14993-15030, KObj) thì viewer có NPC mà server nghĩ chưa thấy → REMOVE bị chặn → "người ma". Đổi luật an toàn hơn: chặn REMOVE chỉ khi (chưa từng ADD) VÀ (hiện không thấy được); và kiểm client có bỏ qua REMOVE id lạ không.
2. m_VisibleNpcs phải xóa khi viewer vào game/đổi map/thoát; NPC xóa thì dọn (đã có KNpc::Remove:10234). Xác nhận phần viewer.
3. Thiếu P2: người ẩn vẫn có thể bị trúng AOE/PK từ người không thấy mình. Cần luật: bên này không thấy bên kia thì không gây sát thương người thật (trừ Bot/quái).
4. Chat/mời tổ đội/giao dịch theo tên vẫn dùng được giữa người ẩn: ghi lại là quyết định thiết kế, chủ dự án chốt sau.
5. Hiệu năng: ViewerCanSee gọi mỗi viewer mỗi gói; đo ở 100 bot + 20 người, so với Enabled=0.
6. Thử theo thứ tự: (a) Enabled=0 phải hành vi y hệt (đăng nhập, đi, đánh, nhóm); (b) Enabled=1 Solo: 2 client cùng map không thấy nhau, cùng đội thấy nhau; (c) Bot thấy bởi tất cả; (d) rời/vào nhóm hoạt động; không "người ma".
Giao Sonnet: rebase lên fix/a07c-link rồi build; thử (a) trước.
