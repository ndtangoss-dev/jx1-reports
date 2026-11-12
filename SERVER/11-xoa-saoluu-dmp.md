# Xóa sao lưu roledb và file dump trong VM

## TÓM TẮT 5 DÒNG
1. Đã xóa 37 thư mục sao lưu trong `gw\database` và 15 file `.dmp` (156,3 MB).
2. `gw\database` còn `roledb`, `roledb.0`, `log.0000000004`.
3. Server vẫn chạy đủ 5 exe, đủ 8 cổng.
4. Chủ máy chưa chọn phương án đổi IP và thay `roledb`, nên `gs001_cfg.ini` chưa đổi, chưa khởi động lại, chưa mở cổng.
5. Dữ liệu thật còn ở `roledb`, `log.*`, `gw\dbfriend`, `gs\TongSet`, `jx_account.sql`, log hôm nay, snapshot cũ, lịch sử git.

Cần tôi quyết định: có

## Đã làm
- Snapshot: `truoc-xoa-saoluu-dmp` (UUID <uuid>).
- Xóa thư mục tên dạng ngày trong `gw\database`, chỉ khi đếm đúng 37.
- Xóa `*.dmp` trong `gs\DumpInfo` và `gw\bishopDump`.

## Bằng chứng
- `backup dirs matched: 37`, `dmp files matched: 15`, `dmp left: 0`.
- 5 exe `responding=True`; cổng 5001, 5002, 5003, 5004, 5005, 51189, 56722, 56732 đang nghe.
- `gs001_cfg.ini`: `localIp=<LAN-IP>`, chưa đổi.

## Lỗi đã gặp
Không có.

## Bước kế
Chờ chủ máy chọn phương án đổi IP và thay `roledb`.
