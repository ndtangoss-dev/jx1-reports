# C1 – Đổi IP trong file cấu hình (VM)

## TÓM TẮT 5 DÒNG
1. Đã đổi `<IP>` thành `<LAN-IP>` trong 8 file ở `C:\JX\ServerNew\_bin_v2_`.
2. Đổi ở cấp byte, có file `.bak`; kiểm tra xác nhận chỉ IP thay đổi.
3. Không còn file văn bản nào chứa IP cũ. Defender: 0 phát hiện.
4. Chưa sửa `[account]` trong `database.ini` (tên máy SQL cũ, cổng, mật khẩu) và `gs\database.ini` còn IP `<LAN-IP>`.
5. Dừng để hỏi trước C2: ý nghĩa `Port=15002/5002` chưa rõ, và ghi mật khẩu `<sql-admin>` vào cấu hình đang vướng quy tắc.

Cần tôi quyết định: có

## Đã làm
- Snapshot trước khi làm: `c1-truoc-sua-ip` (UUID <uuid>).
- File đã sửa, mỗi file có bản `.bak` cùng thư mục: `gw\Bishop.cfg`, `gw\relay_config.ini`, `gw\database.ini`, `gs\gs001_cfg.ini` đến `gs\gs005_cfg.ini`.
- Dùng thay thế theo byte (Latin-1) thay vì `Get-Content`/`Set-Content` trong hướng dẫn, để không đổi mã hóa file.

## Bằng chứng
| File | Số chỗ đổi | IP cũ còn lại | Chỉ IP thay đổi |
|---|---|---|---|
| `Bishop.cfg` | 3 | 0 | Đúng |
| `relay_config.ini` | 4 | 0 | Đúng |
| `gw\database.ini` | 1 | 0 | Đúng |
| `gs001_cfg.ini` đến `gs005_cfg.ini` | 8 mỗi file | 0 | Đúng |

- "Chỉ IP thay đổi": bản `.bak` sau khi thay IP trùng khớp với file mới.
- Tìm lại `<IP>` trong `.ini/.cfg/.txt/.xml/.conf` (bỏ qua file trên 5 MB): 0 file.
- `Get-MpThreatDetection`: 0.

## Lỗi đã gặp
Không có.

## Việc còn lại trước C2 (đang chờ quyết định)
- `gw\database.ini`: `[account] Server=<hostname>\SQLEXPRESS`, `Port=15002`, `PassWord` cũ.
- `gs\database.ini`: `[account] Server=<hostname>\SQLEXPRESS`, `Port=5002`, `PassWord` cũ, `[serverlist] Server=<LAN-IP>`.
- `gw\relay_config.ini`: `account=<sql-admin>`, `password` cũ.
- `Port=` là cổng SQL hay cổng PaySys: tài liệu ghi chưa chắc (`PHAN_TICH.md`, câu hỏi mở số 4).
- Các exe cần mật khẩu `<sql-admin>` ở dạng rõ trong cấu hình; điều này mâu thuẫn với quy tắc không ghi mật khẩu vào file.

## Bước kế
Sau khi có quyết định: sửa các mục trên, chặn kết nối ra ngoài của VM trừ LAN, rồi hỏi trước khi chạy từng exe.
