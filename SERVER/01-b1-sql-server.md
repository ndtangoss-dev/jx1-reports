# B1 – Cài SQL Server 2019 Express trong VM

**Trạng thái: XONG.**

## Đã làm
- Snapshot trước khi làm: `b1-truoc-sql` (UUID <uuid>).
- Tải `SQL2019-SSEI-Expr.exe` từ Microsoft vào `C:\JX\sql` trong VM, tải media Core, giải nén ra `C:\JX\sql\extract`.
- Cài bằng `setup.exe /Q`: instance `SQLEXPRESS`, tính năng `SQLEngine`, `SECURITYMODE=SQL` (Mixed Mode), TCP bật, Named Pipes tắt, sysadmin = `BUILTIN\Administrators`, Browser tự khởi động, không tải bản cập nhật, chấp nhận điều khoản cấp phép SQL Server (`/IACCEPTSQLSERVERLICENSETERMS`).
- Đặt IPAll `TcpPort=1433`, xóa cổng động, khởi động lại dịch vụ.

## Bằng chứng
- `Get-AuthenticodeSignature`: `SQL2019-SSEI-Expr.exe`, `SQLEXPR_x64_ENU.exe`, `setup.exe` đều `Valid`, người ký Microsoft Corporation.
- `Summary.txt`: `Final result: Passed`, `Exit code 0`, 09:18:36 đến 09:25:58.
- Dịch vụ `MSSQL$SQLEXPRESS` và `SQLBrowser`: `Running`, `Automatic`.
- `Get-NetTCPConnection`: lắng nghe 0.0.0.0:1433 và [::]:1433.
- `sqlcmd -S tcp:127.0.0.1,1433 -U sa`: thành công, `Express Edition (64-bit)`, `15.0.2000.5`, `IsIntegratedSecurityOnly=0`, `auth_scheme=SQL`.
- Quét toàn bộ thư mục log setup tìm chuỗi mật khẩu: 0 file khớp.

## Lỗi đã gặp
1. Lần cài đầu qua WinRM thất bại: `There was an error generating the XML document`, bên trong là `CryptographicException: Access is denied`. SQL Setup mã hóa mật khẩu `<sql-admin>` bằng DPAPI, không chạy được trong phiên đăng nhập mạng của WinRM. Không để lại dịch vụ hay thư mục instance.
2. Khắc phục: chạy lại bằng cách gõ phím vào cửa sổ PowerShell đang đăng nhập trong VM. Không dùng scheduled task vì sẽ ghi mật khẩu ra file XML của task.
3. Sau khi cài, màn hình VM hiện lỗi đỏ của Pester (`The Setup command may only be used inside a Describe block`). Chỉ ảnh hưởng dòng in mã thoát (nghi dấu ngoặc kép bị rơi khi gõ phím). Kết quả cài dựa trên `Summary.txt` và đăng nhập `<sql-admin>` ở trên.

## Lưu ý
- Tường lửa chưa mở 1433 ra ngoài; cổng chỉ dùng nội bộ VM theo hướng dẫn.

## Bước kế
B2: tạo DB `account`, nạp `account.sql`, tạo tài khoản thử.
