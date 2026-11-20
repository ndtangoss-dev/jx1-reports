---
name: jx1-bug-fix
description: Quy trình sửa/khảo sát lỗi JX1 theo 6 bước, tra đồ thị và báo cáo cũ trước khi đọc mã; dùng khi task nói về một lỗi (BUG-xxx).
---
# Sửa lỗi JX1 (JX1_OPS/DESIGN/QUY-TRINH-SUA-LOI.md)
1. Ghi nhận: mở/đọc JX1_OPS/BUGS/BUG-<số>.md (nguyên văn lời chủ, bản, máy).
2. TRA TRƯỚC KHI ĐỌC MÃ: DESIGN/MUC-LUC-TRI-THUC.md → DESIGN/HUONG-DAN-TRA-CUU.md →
   graphify query/explain/path đúng gốc (kiểm .graphify_root) → REPORTS/ và BUGS/ cũ.
   Ghi vào mục "ĐÃ TRA GÌ" của bug cái đã dùng và kết quả.
3. Tái hiện bằng cách ngắn nhất, ghi "gây bởi X" kèm bằng chứng; không đoán.
4. Sửa nhỏ nhất, có công tắc hoàn tác, chỉ trong vùng task cho phép. Task chỉ đọc thì dừng ở nguyên nhân + đề xuất.
5. Kiểm lại đúng cảnh lỗi và các trạng thái lân cận; chưa kiểm thì ghi CHUA XAC MINH.
6. Để lại tri thức: ghi vào phiếu BUG đường đi triệu chứng → file:dòng → nguyên nhân; thêm hàng cho MUC-LUC-TRI-THUC.
Task có loai: sua-code → dùng skill jx1-sua-code (đủ bước build + gói giao).
Không build/chạy exe/VM/sửa mã nếu task không cho quyền.
