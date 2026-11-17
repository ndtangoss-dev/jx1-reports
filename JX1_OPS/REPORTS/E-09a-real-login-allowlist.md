# TÓM TẮT 5 DÒNG
1. DONE trong phạm vi code/offline: thêm `real_login` và cờ `--allow-test-vm`, mặc định vẫn chỉ loopback.
2. Opt-in chỉ mở đúng VM thử `192.168.56.150`, Bishop 56722/game 51189; chặn sai host/cổng trước socket/DNS, kể cả redirect permit.
3. Luồng login → role → vào game → giữ phiên 30 s → đóng TCP dùng API BOT; credential chỉ từ môi trường, không ghi file/CLI/log.
4. Lượt toàn TESTER: 28/29 đạt, một assertion Markdown sai; đã sửa và kiểm lại E-09a 7/7 đạt, các 22 test cũ đạt ở lượt toàn suite.
5. [CHƯA KIỂM] VM/gs001 thật/ABI/gameplay/lưu dữ liệu; không mạng thật, VM, exe; không commit/push vì task không yêu cầu.

## Phạm vi và cài đặt

Ngày 17/11/2026, worktree `D:\JX-wt\E-09a`, nhánh `task/E-09a`.
Kiểm status/branch một lần trước ghi: chỉ `JX1_OPS/TASKS/E-09a.md` untracked.
Giữ nội dung task gốc, chỉ thêm mục Kết quả đúng yêu cầu task. Các thay đổi còn
lại chỉ ở TESTER và báo cáo này. Đã đọc E-09a, E-05a, E-05b, B-03 và code
TESTER/BOT trực tiếp cần cho codec, login, permit và sync; không quét repo.
Không thay BOT, nguồn canonical, cấu hình model/provider hoặc credential.

- `core.py::Config`: thêm `allow_test_vm=False` và `validate_endpoint`.
  Loopback literal `127.0.0.1` vẫn mặc định, cổng nguyên 1..65535. Opt-in chỉ
  host chính xác `192.168.56.150`, cổng Bishop 56722 hoặc game 51189 theo pha.
  Không hostname/DNS/subnet/IPv6/alias hay mở rộng allowlist qua CLI.
- `real_login.py::guarded_channel`: kiểm policy sát trước mỗi
  `socket.create_connection`, bắt buộc permit cùng host cấu hình. Handshake
  lỗi đóng channel; worker/core đóng phiên khi FAIL hoặc timeout.
- `real_login.py::environment_credentials`: đọc riêng từng bot qua
  `JX1_BOT01_...` tới BOT05, gồm ACCOUNT/PASSWORD/ROLE/CLIENT_KEY/REGION/
  ENTER_MAP/OBSERVED_ONLINE; ENCODING tùy chọn, mặc định ascii. Thiếu/sai
  cấu hình FAIL trước Bishop. Không đoán key, tên nhân vật hay cấu hình game.
  Đăng ký redactor trước validation; object credential không có repr chứa giá trị.
- `REAL_LOGIN`: năm bước `real_login`, `role`, `enter_game`, `hold_session`,
  `close`. Dùng `packets.login/check_login_response/role_list/select_role/
  permit_login/logic_login`, `Channel`, `Session.poll/hold/close`. Role thiếu là
  FAIL, không tự tạo. Sync dùng client key từ môi trường, ACK END 9 byte và
  CP_LOCK theo BOT. Giữ 30 s, xử lý PING nếu nhận, không RUN/SKILL.
- `run.py`: đăng ký scenario và cờ; cờ chỉ hợp lệ với `real_login`. Các
  scenario fixture vẫn chặn VM ở API trực tiếp trong `scenarios.py`,
  `visibility.py`, không dựa riêng CLI.
- `reporting.py`: report real_login diễn đạt kết quả theo profile BOT tại
  endpoint cấu hình; không còn gắn nhãn tất cả là login giả. Không tự nhận
  PASS là nghiệm thu ABI/gameplay/lưu dữ liệu. Auth payload/GUID/key không log.
- `README.md`: ghi policy, biến môi trường, giới hạn và cách test bằng
  `python -I`; không ghi giá trị mật khẩu/khóa hoặc lệnh tự chạy VM thật.

Admission giữ quy tắc BOT: số online được cung cấp 0..99 trước thêm bot;
không tự truy vấn/điều phối tổng online nhiều worker. Profile BOT giới hạn
account/password 1..16 byte, role 1..63 byte; người vận hành phải xác nhận
encoding/key/region/map trước phiên thật. Không thử lại login tự động.

## Kiểm chứng offline đã chạy

```text
python -I -m unittest discover -s JX1_OPS/TESTER -v
Ran 29 tests in 67.648s
FAILED (failures=1)
```

22 test cũ và 6/7 test E-09a đạt. Test còn lại đã thực hiện đủ năm PASS,
bao gồm hold 30.000 s và nhiều PING_REPLY; assertion tìm `hold_session` và
thời gian trên cùng dòng Markdown sai vì header/dòng số liệu khác nhau.
Đã sửa assertion đọc dòng kết quả, không thay code giao thức để xử lý lỗi này.

```text
python -I -m unittest discover -s JX1_OPS/TESTER -p test_real_login.py -v
Ran 7 tests in 30.751s
OK; exit 0
```

Bảy test E-09a:

1. Allowlist mặc định/opt-in và cổng theo pha; Main VM, host lân cận,
   hostname, IPv6/mapped, alias, khoảng trắng, cổng sai/bool/string bị từ chối.
   Mock `socket`, `getaddrinfo`, `create_connection` xác nhận chưa gọi;
   API các scenario giả cũng từ chối VM trước socket.
2. Nhánh cho phép VM tới hai cổng đúng chỉ dùng mock hoàn toàn, không kết nối.
   Loopback không được redirect sang VM kể cả đã bật cờ.
3. CLI sai mode/host/cờ exit 2 trước tạo worker.
4. Thiếu biến và sai key/online/region/role FAIL trước mở socket, dữ liệu
   tổng hợp sinh ngẫu nhiên trong RAM.
5. CLI subprocess giữ `-I`, fixture loopback: năm PASS, ACK 9 byte/CP_LOCK,
   giữ đủ 30 s và hơn 10 PING_REPLY, không RUN/SKILL. Report/console không
   có account/password/role/key tổng hợp hoặc hex/MD5 kiểm tương ứng; không BUG.
6. Bishop thật của fixture chỉ loopback; permit Main VM, host lân cận hoặc
   VM thử đều bị policy loopback chặn trước socket thứ hai, không phiên game.
7. Không có role: PASS login, FAIL role, ba bước sau BỎ QUA; không tạo nhân vật.

`test_full_cycle.py::cycle_server` được bổ sung chế độ fixture real: permit
loopback/cổng ngẫu nhiên, PING định kỳ sau sync; mặc định full_cycle giữ nguyên.
Fixture sử dụng codec BOT/vector tổng hợp cũ, credential/GUID trong RAM,
không lưu payload auth. Báo cáo test chỉ trong thư mục tạm và được dọn sau test.
Không tạo báo cáo phụ/BUG trong vùng REPORTS ngoài task.

Không chạy lại toàn suite sau sửa assertion vì thay đổi chỉ thuộc test mới;
7/7 cuối xác minh chính assertion đã sửa, 22/22 cũ có bằng chứng ở lượt trước.
BOT không sửa, không chạy lại suite BOT; không build hay chạy exe.

## Giới hạn, lỗi công cụ và bàn giao

- [CHƯA KIỂM] đăng nhập/role/giữ phiên trên VM thật, ABI binary, client key
  thật, gameplay, logout ứng dụng và dữ liệu lưu. Đóng TCP không chứng minh
  lưu nhân vật; kết quả loopback không phải nghiệm thu server thật.
- `rg : The term 'rg' is not recognized ...`: một lần; chuyển sang
  Get-ChildItem/Get-Content/Select-String giới hạn theo file/thư mục task.
- Lượt đọc đầu PowerShell hiển thị UTF-8 sai dấu: đọc đúng task bằng
  `-Encoding UTF8`, không đổi file gốc. Đầu ra ghép dài bị cắt: đọc lại đúng
  phần code cần thiết, không mở rộng phạm vi tìm kiếm.
- Một assertion test sai và cách sửa ghi ở trên; không có lỗi code/runtime
  còn tồn tại được phát hiện qua các test đã chạy. Không nâng quyền hoặc
  thay credential/config để vượt sandbox.

Trạng thái **DONE cho phạm vi code và test offline được giao**; không có
blocker. Không stage/commit/push hoặc kết nối GitHub vì không được yêu cầu.
HEAD nền được ghi bởi test report: `89fafae90b8d1fc01512d1c5f27b97c39459d568`;
đây không phải commit mới. Không có SHA mới/link GitHub, thay đổi giữ local.
Đã rà diff một lượt cho file sửa và file mới; `git diff --check` exit 0,
không báo whitespace. Diff file mới bằng `--no-index` exit 1 do có nội dung mới,
không phải lỗi kiểm thử.
