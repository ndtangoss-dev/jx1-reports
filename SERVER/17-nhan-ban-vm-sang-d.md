# Nhân bản VM sang ổ D

## TÓM TẮT 5 DÒNG
1. Đã nhân bản `JX-Server` thành `JX-Server-D` ở `D:\VMs\JX-Server-D`, kiểu `machine` (gộp snapshot), mất 6 phút, 41.1 GB.
2. Bản clone giữ MAC `080027AD6D3F`, khởi động được, IP `<LAN-IP>`, WinRM, SQL chạy, thư mục server và cấu hình còn nguyên.
3. Chưa xóa gì: `JX-Server` cũ (24 snapshot) và `C:\VMs\JX-disk` vẫn nằm trên ổ C, ổ C còn 20.1 GB.
4. Màn hình VM có hộp thoại "VMware Tools Error" (phần mềm sót từ VMware), chưa bấm, chưa ảnh hưởng gì.
5. Thêm luật quyền cục bộ cho lệnh WinRM theo yêu cầu chủ máy, file không vào git.

Cần tôi quyết định: có

## Bằng chứng
- `clonevm ... --mode machine --options keepallmacs,keepdisknames --register` trả `Machine has been successfully cloned as "JX-Server-D"`, 08:36 đến 08:42.
- `showvminfo JX-Server-D`: `poweroff` trước khi bật, `macaddress1="080027AD6D3F"`, `nic1="bridged"`, không có snapshot. Đĩa: `D:\VMs\JX-Server-D\Snapshots\{fc58d1dc-...}.vmdk`.
- Sau khi bật: ping dưới 1 ms, ARP `<LAN-IP>` trỏ `<mac>`, cổng 5985 mở sau 70 giây.
- Qua WinRM: `MSSQL$SQLEXPRESS` Running, `gs001_cfg.ini` còn `Ip`/`localIp` là `<TAILSCALE-IP>`, 6 luật tường lửa `JX*`, 6 tác vụ `JX-*`, `mu1` đăng nhập console, `sqlcmd` đọc được `account`.
- Không exe JX nào đang chạy.

## Chưa kiểm tra
- Chạy 5 exe server trên bản clone.
- Hộp thoại VMware Tools có từ trước hay mới xuất hiện.

## Bước kế
- Chủ máy duyệt xóa VM cũ: `unregistervm JX-Server --delete` (xóa cả chuỗi snapshot và đĩa nền trong `C:\VMs\JX-disk`), rồi dọn phần còn lại của `C:\VMs\JX-disk` (file VMware `.vmx`, log) và đĩa mồ côi `JX-Server.vdi` (2 MB). Ước giải phóng khoảng 145 GB trên ổ C.
