# B2 – Tạo DB `account`, nạp `account.sql`, tạo tài khoản thử

## TÓM TẮT 5 DÒNG (cuối chặng B)
1. SQL Server 2019 Express đã cài trong VM, instance `SQLEXPRESS`, Mixed Mode, TCP 1433.
2. DB `account` đã tạo, `account.sql` nạp 0 lỗi, có 32 bảng.
3. Tài khoản thử `<test-account>` đã tạo.
4. Script được rà trước khi nạp, không có lệnh nguy hiểm. Mật khẩu không có trong log setup.
5. Dump gốc có sẵn 672 tài khoản, cần coi VM là có dữ liệu thật.

Cần tôi quyết định: không

**Trạng thái: XONG.**

## Đã làm
- Snapshot trước khi làm: `b2-truoc-account` (UUID <uuid>).
- Rà `C:\JX\ServerNew\_bin_v2_\account.sql` trước khi nạp: 922 141 byte, 5611 dòng, 1559 batch `GO`, 32 `CREATE TABLE`.
- Tạo DB `account` (collation `SQL_Latin1_General_CP1_CI_AS`).
- Nạp bằng `sqlcmd -d account -f 65001`. Log: `C:\JX\sql\account-load.log` trong VM.
- Tạo tài khoản `<test-account>` trong `Account_Info` (mật khẩu lưu MD5 viết hoa).

## Bằng chứng
- Tìm trong script: 0 kết quả cho `xp_cmdshell`, `sp_configure`, `OPENROWSET`, `OPENDATASOURCE`, `OPENQUERY`, `sp_addlinkedserver`, `sp_OACreate`, `BULK INSERT`, `CREATE LOGIN`, `CREATE USER`, `ALTER/DROP DATABASE`, `EXEC(`, `xp_regwrite`, `xp_dirtree`, `RECONFIGURE`, `ASSEMBLY`.
- `sqlcmd` nạp thoát 0; trong log có 0 dòng `Msg`.
- `sys.tables`: 32 bảng (tiêu chí của hướng dẫn: từ 30 trở lên). `sys.procedures`: 2. `Account_Info`: 672 dòng có sẵn trong dump, cộng tài khoản thử. `ServerList`: 5 dòng.
- `SELECT` lại `<test-account>`: có 1 dòng, độ dài mật khẩu 32.

## Lỗi đã gặp
Không có.

## Lưu ý
- `Account_Info` chứa sẵn dữ liệu tài khoản từ dump gốc. Không xem hay xuất nội dung các dòng đó. VM cần được coi là có dữ liệu tài khoản thật.
- Mật khẩu `<test-account>` không ghi ở đây.

## Bước kế
C1: đổi IP trong các file cấu hình.
