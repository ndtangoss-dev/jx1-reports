# Chuẩn báo cáo JX1 (áp dụng từ 17/11/2026, chủ duyệt)

Mục đích: mọi báo cáo cùng một khuôn để tìm nhanh, đọc nhanh, đối chiếu được và lộ ngay chỗ sót.
Áp dụng cho báo cáo mới và cho toàn bộ báo cáo cũ trong `REPORTS/` (nhiệm vụ R-01..R-07 chuẩn hóa dần).

## Khuôn bắt buộc (theo thứ tự)
1. `TÓM TẮT 1..5` (đúng 5 dòng, gắn `[NGUỒN]` hoặc `[CHƯA KIỂM]`). Dòng 5 = giới hạn: đã/chưa chạy build, exe, VM.
2. Tiêu đề `# <ID> — <chủ đề>`.
3. **Khối thông tin** ngay dưới tiêu đề, mỗi mục một dòng:
   - `Loại:` một trong khảo sát | thiết kế | sửa lỗi | công cụ | kiểm thử | tổng hợp
   - `Chủ đề:` một câu
   - `Từ khóa:` 5–10 từ, có cả tên Việt và tên gốc/ID (ví dụ `Võ Đang, wudang, 武当, ReqLevel`)
   - `Trạng thái:` DONE | PARTIAL | BLOCKED | FAILED, kèm lý do ngắn
   - `Độ phủ:` đã phủ X trên tổng Y (đơn vị: phái, bản đồ, file, gói tin...). Không đếm được thì ghi `chưa đếm được` và lý do.
   - `Liên quan:` danh sách báo cáo/DESIGN/BUG liên quan
   - `Cần tôi quyết định:` có | không
4. **Sơ đồ Mermaid** một cái (luồng hoặc quan hệ chính).
5. **Phạm vi và độ phủ**: bảng liệt kê đủ mọi phần tử của phạm vi, mỗi phần tử ghi đã phủ / chưa phủ. Lỗi sót như báo cáo bỏ Võ Đang phải lộ ra ở đây.
6. Thân báo cáo. Bằng chứng luôn dạng `file:dòng`; mã hóa ghi rõ (GBK, TCVN3, UTF-8).
7. **Đã xác minh / Chưa xác minh**.
8. **Bàn giao**: commit, bước tiếp theo.

## Quy tắc khi chuẩn hóa báo cáo cũ
- KHÔNG đổi kết luận, số liệu, bằng chứng. Chỉ thêm khối thông tin, sơ đồ, bảng phạm vi, từ khóa, liên quan.
- Phát hiện sai hoặc sót thì ghi vào mục `Phát hiện khi chuẩn hóa` cuối file, không sửa lặng.
- Bảng phạm vi lập bằng cách đối chiếu dữ liệu gốc (chỉ đọc), không suy từ trí nhớ.
- File phải đọc được bằng UTF-8 không BOM; nếu chữ lỗi thì ghi vào `Phát hiện khi chuẩn hóa`.
- Mỗi nhiệm vụ nộp thêm một bảng chỉ mục `REPORTS/_CHIMUC/<ID>.tsv`, cột: file, loại, chủ đề, từ khóa, trạng thái, độ phủ, liên quan. PM gộp vào `MUC-LUC-TRI-THUC.md`.
