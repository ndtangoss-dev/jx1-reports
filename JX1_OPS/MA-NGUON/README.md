# MA-NGUON

Tự sinh bởi `TOOLS/quet_ma_nguon.py` (chỉ ĐỌC mã game, chỉ GHI vào thư mục này). Kho PUBLIC: chỉ bảng mô tả bằng chữ, không mã nguồn, không exe/APK, không khóa.

- `ban-do-client.md`, `ban-do-server.md`: tệp nào làm gì, hàm nào gọi hàm nào (khớp theo tên).
- `goi-tin.md`: bảng gói tin client↔server.
- Chuỗi chữ và nhập khẩu của exe: `exe-chuoi.md` (TOOLS/quet_exe.py, làm sau).

Lưu ý: mã gói trong `goi-tin.md` tính theo thứ tự enum; khi enum gán giá trị bằng hằng ký hiệu (ví dụ `g_nGlobalProtocolType`) thì mã sau đó có thể lệch, cần đối chiếu `KProtocolDef.h`. Tên hàm là heuristic theo dòng (không phải trình phân tích C++ đầy đủ).
