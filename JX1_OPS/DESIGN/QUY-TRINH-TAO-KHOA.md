# QUY TRÌNH TẠO KHÓA XINGCHI (#114/#115, L8)

Tuyệt đối KHÔNG ghi giá trị khóa vào file trong kho, báo cáo, chat, git. Chỉ ghi TÊN khóa.

## Chính sách
- Trần 20 khóa (= 60 tiểu yêu, ≤3 tiểu yêu/khóa). Vượt 20 khóa: hỏi chủ qua Chat.
- Chỉ tạo khóa mới khi CÓ việc đang chờ và mọi khóa hiện có đã đủ 3 tiểu yêu. Không tạo trước.
- Hai lần tạo cách nhau ≥ 1 phút.
- Cấm dùng khóa mặc định trong `config.toml` của Codex (khóa đó từng lộ, #106.3): mọi lần chạy phải có `JX_CODEX_KEY=JX-Kn`.
- Không giới hạn cứng 5 tiểu yêu; chỉ tạm ngừng giao thêm khi ≥3 tiểu yêu chết cùng lúc vì 429 hoặc `upstream_error` (cầu dao trong `TOOLS/tong_quan.py`).

## Các bước (qua Chrome, phiên đã đăng nhập của chủ)
1. Mở trang quản lý khóa của xingchi trong Chrome; chọn số n kế tiếp chưa dùng (xem `STATE/KHOA-XINGCHI.md`).
2. Tạo khóa mới, đặt tên `JX-Kn`.
3. Sao chép giá trị, lưu vào `C:\Users\PC\.jx1keys\JX-Kn.txt` (một dòng, không BOM). Không dán vào chat/kho.
4. Kiểm: gọi `GET /v1/models` với khóa đó, mong HTTP 200. Ghi kết quả ping vào `STATE/KHOA-XINGCHI.md` (chỉ "200" hoặc mã lỗi).
5. Thêm một dòng vào bảng; Tổng quản tự thấy khóa mới qua thư mục `.jx1keys` ở vòng sau.

## Chọn khóa khi giao việc
`TOOLS/tong_quan.py` chọn khóa đang có ít tiểu yêu nhất (≤3), truyền qua biến môi trường `JX_CODEX_KEY` cho `chay_codex.ps1`; giá trị đọc lúc chạy từ `.jx1keys`.
