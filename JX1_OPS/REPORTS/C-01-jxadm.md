# C-01 — jxadm: thiết kế và mã offline

Ngày: 17/11/2026. **PARTIAL — phần mã offline hoàn tất; commit BLOCKED** do quyền ghi metadata Git. Không xác nhận hiệu lực trên server từ kết quả test offline.

## Worker kiểm tra trước khi làm

- Đã đọc `JX1_OPS/TASKS/C-01.md` trước khi triển khai. `Get-Location` = `D:\JX-wt\C-01`; `git rev-parse --show-toplevel` = `D:/JX-wt/C-01`; nhánh `task/C-01-codex`, đúng worktree/branch task. `git status --short --branch` ban đầu chỉ có dòng nhánh, không có thay đổi local.
- Phạm vi ghi: `JX1_OPS/TOOLS/jxadm/`, báo cáo này và mục `Kết quả` trong task theo yêu cầu trực tiếp của người dùng. Không sửa nguồn `C:\Jx1CocoV3`; không chạy exe server, kết nối VM/SQL/server, đọc tài khoản thật, DB nhân vật thật hoặc tạo snapshot.
- Tái sử dụng A-01/A-02/A-03/A-06. Bảng/cột và giới hạn dữ liệu dựa vào A-02; không đọc lại workflow/lịch sử để suy đoán schema.

## Mã và cách dùng

`JX1_OPS/TOOLS/jxadm/jxadm.py` chỉ dùng thư viện chuẩn Python (Python 3.10+). Chạy trực tiếp bằng đường dẫn; không cần cài package hoặc driver. `--dry-run` là mặc định và cũng là chế độ CLI duy nhất. CLI in JSON gồm SQL với dấu `?`, danh sách tham số riêng và ghi chú. Không có driver, socket, DNS, tự kết nối hoặc tải mã adapter từ tên module.

Các ví dụ chỉ dùng định danh fixture tổng hợp; không chứa tài khoản hoặc mật khẩu thật:

```powershell
python -I JX1_OPS/TOOLS/jxadm/jxadm.py create --account offline_fixture --begin 2026-11-17T00:00:00 --end 2026-11-18T00:00:00
python -I JX1_OPS/TOOLS/jxadm/jxadm.py lock --account offline_fixture --dry-run
python -I JX1_OPS/TOOLS/jxadm/jxadm.py unlock --account offline_fixture --prompt-password
python -I JX1_OPS/TOOLS/jxadm/jxadm.py reset-password --account offline_fixture --password-env JXADM_PASSWORD
python -I JX1_OPS/TOOLS/jxadm/jxadm.py online
python -I JX1_OPS/TOOLS/jxadm/jxadm.py online --account offline_fixture
python -I JX1_OPS/TOOLS/jxadm/jxadm.py mark-bot --account offline_fixture --value true
python -I JX1_OPS/TOOLS/jxadm/jxadm.py mark-bot --account offline_fixture --value false
python -I JX1_OPS/TOOLS/jxadm/jxadm.py backup-characters --source D:/offline_fixture/database --destination D:/offline_fixture_backup
```

| Lệnh | SQL / hành vi offline | Giới hạn |
|---|---|---|
| `create` | Kiểm tra tồn tại ở cả hai bảng; INSERT `Account_Info(cAccName,cPassword,iClientID)` và `Account_Habitus(cAccName,iFlag,dBeginDate,dEndDate,iLeftSecond,nExtPoint,iClientID)`. | Profile đề xuất theo thời gian: `iFlag=0`, các bộ đếm/client ID ban đầu 0; người dùng chỉ định rõ thời gian đầu/cuối. Default/constraint/cột bắt buộc còn thiếu: **chưa kiểm**. |
| `lock` | UPDATE `Account_Info.cPassword` bằng marker 32 ký tự `!`, nằm ngoài miền MD5 hệ 16; không lưu hash cũ. | Đây là phương án thiết kế để vô hiệu hóa so sánh MD5 thông thường, **chưa kiểm runtime**; không dùng cờ khóa chưa xác minh. Không hứa chặn super-password hay ngắt phiên đang mở. |
| `unlock` | UPDATE `cPassword` bằng MD5 viết hoa của **mật khẩu mới**. | Không phục hồi mật khẩu trước khóa; nghĩa mở khóa được định nghĩa rõ là đặt mật khẩu mới. |
| `reset-password` | UPDATE `cPassword` tương tự; lọc theo `cAccName`. | Không tự sửa hạn chơi hoặc phiên. |
| `online` | SELECT `cAccName,iClientID,dLoginDate,dLogoutDate`; có thể lọc tài khoản. | Chỉ xuất quan sát trạng thái phiên. Không gán `iClientID!=0` hay ngày đăng nhập thành chân lý online; số online chính xác **chưa kiểm**. |
| `mark-bot` | Kiểm tra tài khoản tồn tại; UPDATE rồi INSERT nếu chưa có `Account_BotMetadata(cAccName,is_bot)`. | Theo đề xuất A-02; bảng metadata **chưa tạo**. Không sửa `iFlag`, `iClientID`, `ServerList` hoặc blob nhân vật để đánh dấu bot. |
| `backup-characters` | Sinh yêu cầu adapter sao lưu toàn bộ môi trường Berkeley DB, gồm DB/chỉ mục/log recovery. | Không sinh SQL cho nhân vật, không mở/copy file trong CLI. Chưa có adapter sao lưu thực hoặc khôi phục thử. |

Tài khoản nhận chữ ASCII thường, số, `_` để tránh âm thầm đổi hoa/thường khi Goddess chuẩn hóa tài khoản; giới hạn độ dài SQL thực tế **chưa kiểm**, không tự đặt kích thước cột. Ngày dùng `YYYY-MM-DDTHH:MM:SS`, theo giờ local của SQL Server; không mặc định múi giờ hoặc thời hạn. SQL dùng `CONVERT(datetime, ?, 126)` cho hai mốc thời gian.

## Mật khẩu và chặn Main VM

- Không có tùy chọn nhận mật khẩu trực tiếp qua argv hoặc file. `--password-env NAME` đọc biến môi trường lúc chạy; `--prompt-password` dùng `getpass` và từ chối fallback có thể echo. Người vận hành cấp biến môi trường bằng cơ chế bí mật phù hợp; báo cáo không ghi giá trị.
- Nếu chỉ cần dry-run, bỏ cả hai tùy chọn để dùng tham số mật khẩu chưa gán. Adapter SQL từ chối kế hoạch đó trước khi tạo kết nối. Khi có mật khẩu, hash chỉ nằm trong bộ nhớ; JSON/repr che cả plaintext và hash bằng `<redacted:cPassword>`.
- MD5 viết hoa dùng để tương thích đường đăng nhập cũ được A-02 ghi nhận, không phải lựa chọn hash mới. Chỉ nhận printable ASCII; encoding mật khẩu ngoài ASCII **chưa kiểm**, không đoán GBK/UTF-8.
- `validate_host` chỉ nhận IP literal; chặn cứng `192.168.1.50` và IPv4-mapped IPv6 tương đương. Tên DNS, DSN, instance, URL, port kèm host, IPv4 không chuẩn và IPv6 zone ID bị từ chối. Kiểm tra thực hiện trước nhập mật khẩu và lặp tại điểm gọi adapter; không resolve DNS.
- CLI không có `--execute`. Parser không viết tắt option và không echo argv khi báo lỗi, tránh ghi nhầm mật khẩu vào output. Test dùng dữ liệu tổng hợp sinh lúc chạy, không lưu credential.

## Giao diện thay được và tính nguyên tử

`account_plan(...)` tạo `SqlPlan` bất biến; `Statement` giữ SQL và tuple tham số riêng. API nhúng `execute_sql(plan, connect)` nhận factory do caller cung cấp, truyền duy nhất `host` đã kiểm và `database='account'`. Không kèm connection string hoặc credential. Factory phải dùng đúng đích này, không alias/redirect sang Main VM; đây là hợp đồng với mã adapter đáng tin, không thể kiểm soát mã adapter tùy ý bên ngoài.

Factory trả connection theo giao diện DB-API: tắt autocommit, dùng cùng cursor/transaction cho toàn kế hoạch, kiểm `rowcount=1` ở INSERT/UPDATE tài khoản, commit khi thành công, rollback khi có lỗi hoặc sai số dòng và luôn đóng cursor/connection. Kiểm tra tồn tại/upsert dùng `UPDLOCK,HOLDLOCK`; tài khoản đã tồn tại hoặc chỉ có một trong hai bảng sẽ bị từ chối. Lỗi DB không được ghi tự động; caller phải lọc lỗi driver có thể chứa tham số. API này chỉ kiểm bằng adapter giả trong C-01, không được gọi với driver thật trong task.

`backup_plan(...)` và `execute_backup(plan, adapter, cold_confirmed=True)` là giao diện riêng vì nhân vật không nằm trong SQL account. Trước dispatch, kiểm lại host/đường dẫn, từ chối UNC/URL/đường dẫn tương đối/`..` và thư mục trùng hoặc lồng nhau. Không kiểm filesystem trong dry-run. Adapter thực phải xác minh đường dẫn local sau resolve (bao gồm junction, symlink, mapped drive), nguồn đã đóng nhất quán, đích mới không ghi đè; copy đủ môi trường, lập hash manifest và kiểm khôi phục ở bản copy riêng. Cờ `cold_confirmed` là tiền điều kiện do caller chịu trách nhiệm, không phải phát hiện trạng thái server. Không có adapter thực đi kèm; không tự mở Berkeley DB bằng `dbm` hay đổi tên dump `.bak` thành `roledb`.

## Căn cứ và điểm chưa kiểm

| Căn cứ | Áp dụng / giới hạn |
|---|---|
| `A-02-luong-dang-nhap.md:58-60,70-80,120` | MD5 viết hoa; hai bảng tài khoản; `iFlag=0` theo thời gian; `iClientID` chưa đủ chứng minh online. Không có bằng chứng cờ khóa chuyên dụng. |
| `A-02-luong-dang-nhap.md:86-103` | Berkeley DB và backup toàn môi trường; dump `.bak` là cặp key/blob, không phải B-tree. Tính nhất quán/khôi phục chưa kiểm. |
| `A-02-luong-dang-nhap.md:105-114` | `Account_BotMetadata`, `is_bot bit NOT NULL DEFAULT 0`, không có dòng coi là false. Kiểu/chiều dài/collation/unique/FK của `cAccName` phải lấy từ schema thật; không tạo migration bằng kiểu đoán. Game server chưa tự tiêu thụ cờ. |
| `A-01-ban-do-tien-trinh.md:14-17` | Vai trò SQL, PaySys, Goddess; không kết nối các tiến trình này. |
| `A-03-kiem-ke-cau-hinh.md:1-5` và `A-06-bang-goi-tin.md:2-5` | Cấu hình/binary/ABI runtime chưa xác minh; không dùng packet để đoán trạng thái online hoặc sao lưu. |

**Chưa kiểm:** schema sống, schema SQL owner, datatype/length/collation, NULL/default/trigger/unique/FK, SQL Server version và hỗ trợ `THROW`, driver/rowcount thực, hash/encoding đúng binary hiện hành, marker khóa có được schema chấp nhận không, super-password, phiên online, tác dụng `is_bot` trong game, backend nhân vật thực, adapter sao lưu thật, tính nhất quán/khôi phục, múi giờ server. Phải xác minh các điểm liên quan trong task vận hành được duyệt trước khi cấp adapter thật; test offline không thay thế các bước này.

## Kiểm chứng và lỗi trong cùng task

- Lệnh bắt buộc: `python -I -m unittest discover -s JX1_OPS/TOOLS/jxadm -v`. Lần đầu 21 test pass; sau rà soát parser, bổ sung một test bảo vệ argv rồi chạy lại: **22 test trong 0,097 giây, OK, exit 0**.
- Chạy trực tiếp `create ... --dry-run` với fixture/ngày ở ví dụ: exit 0, in ba statement (kiểm tra tồn tại + hai INSERT), tham số riêng và `<redacted:cPassword>`. Chạy trực tiếp `lock ... --host 192.168.1.50`: `jxadm: Main VM 192.168.1.50 is blocked`, shell exit 1; unit test xác nhận mã trả về `main()` là 2. Không mở kết nối.
- Test kiểm SQL đúng cột/tham số, marker khóa/mật khẩu mới, cả hai giá trị bot, quan sát online không suy diễn; commit/rollback/đóng tài nguyên bằng fake, lỗi INSERT thứ hai, rowcount 0/2, thiếu secret từ chối trước connect; chặn Main VM/alias và kế hoạch bị sửa host; adapter backup giả; môi trường/getpass/redaction/lỗi argv. CLI tests chặn socket/DNS bằng mock; không truy cập server hay dữ liệu thật.
- Lệnh đọc nền ban đầu dùng wildcard `A-0*.md` rộng hơn bốn báo cáo được chỉ định, khiến lẫn A-05/A-07, output bị cắt và PowerShell giải mã UTF-8 sai. Đã giới hạn lại các đoạn cần dùng ở A-01/A-02/A-03/A-06 bằng UTF-8; không dùng phần ngoài phạm vi làm căn cứ nghiệp vụ, không sửa tài liệu gốc.
- `rg` không có trong PATH: `The term 'rg' is not recognized`. Không thử lại/cài đặt; kiểm tra đúng đường dẫn bằng PowerShell/Python chuẩn. Không tạo parser/script phụ cho trích xuất tài liệu.
- Rà soát phát hiện `argparse` mặc định có thể viết tắt option/echo giá trị khi báo lỗi; đã tắt abbreviation và dùng thông báo lỗi không kèm argv, có test riêng. Không có credential thật trong lần chạy nào.
- Kiểm diff ban đầu dừng sau task và `.gitignore` do coi exit 1 của `git diff --no-index --check` trên file mới là lỗi; output kiểm whitespace trống. Đã xử lý đúng exit do có khác biệt, tiếp tục ba file chưa xem; không chạy lại test hoặc thao tác stage bị chặn.
- Không chạy build game, exe, VM/SQL/server, migration hay backup/restore thực. Chỉ chạy Python offline theo task.

## Commit và bàn giao

Đã thử stage đúng năm file C-01 một lần bằng lệnh bên dưới; exit 1:

```text
fatal: Unable to create 'D:/jx1-reports/.git/worktrees/C-01/index.lock': Permission denied
```

Metadata Git ngoài writable root `D:\JX-wt\C-01`; phiên này không được nâng quyền. Không thử lại cùng lỗi, không đổi ACL/config/credential hoặc tạo Git directory khác để vượt sandbox. Chưa stage, chưa gọi commit vì stage thất bại; **không có commit SHA hoặc link commit mới**. **BỊ CHẶN – CHƯA PUSH**. Người dùng chỉ yêu cầu commit local, không yêu cầu push.

PM tiếp tục bằng phiên có quyền ghi metadata Git trên nhánh `task/C-01-codex`, giữ năm file local đã kiểm chứng:

```powershell
git add -- JX1_OPS/TOOLS/jxadm/.gitignore JX1_OPS/TOOLS/jxadm/jxadm.py JX1_OPS/TOOLS/jxadm/test_jxadm.py JX1_OPS/REPORTS/C-01-jxadm.md JX1_OPS/TASKS/C-01.md
git commit -m "C-01 Them jxadm va test offline"
git log -1 --format=%H
```

Không cần chạy lại test nếu mã không thay đổi. Việc xác minh runtime/schema/khôi phục là task riêng cần phạm vi vận hành được duyệt, không thuộc C-01 offline.
