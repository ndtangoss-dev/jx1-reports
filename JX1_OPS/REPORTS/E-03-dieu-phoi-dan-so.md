TÓM TẮT 5 DÒNG
1. DONE: bổ sung thư viện population độc lập, chưa nối server.
2. Cấu hình JSON hỗ trợ trọng số, đường cong 24 giờ, trần tổng mặc định 100 và trần map.
3. plan(current, now) giữ Bot bận, giới hạn thay đổi trong 60 giây và jitter có seed.
4. Kiểm tra yêu cầu đạt 53/53 test: 41 test cũ và 12 test mới.
5. Không chạy exe game/server, không kết nối mạng, không ghi mật khẩu/khóa; chưa commit/push.

## Phạm vi và kết quả

- `JX1_OPS/BOT/population/__init__.py`: `Config.from_json`, `Planner.desired`,
  `Planner.plan`, các record `MapConfig`, `Bot`, `Command`.
- `population.example.json`: cấu hình ba map tổng hợp; cao điểm 19–20 giờ đạt
  100 Bot, 03 giờ đạt 20 Bot.
- `test_population.py`: 12 test mới bao phủ trần, trọng số/phần dư, tái phân bổ
  khi chạm trần map, giờ cao điểm, cửa sổ trượt qua ranh giới phút, giữ Bot bận,
  loại Bot map lạ, jitter/seed, hội tụ, dữ liệu lỗi và thời gian lùi.
- `README.md` trong module: hợp đồng snapshot, thực thi lệnh tuần tự, timezone,
  thuật toán phân bổ, giới hạn và cách chạy kiểm tra.

Giới hạn thay đổi tính cả spawn và despawn, không reset theo phút đồng hồ.
Jitter chèn khoảng chờ giữa các đợt, thứ tự chọn được xáo bằng RNG riêng có seed.
Planner không thực thi lệnh và không sửa snapshot đầu vào.

## Bằng chứng kiểm tra

Lệnh đã chạy tại `D:\JX-wt\E-03`, nhánh `task/E-03-dieu-phoi`:

```text
python -I -m unittest discover -s JX1_OPS/BOT
.....................................................
----------------------------------------------------------------------
Ran 53 tests in 0.141s

OK
```

Không build, chạy binary game/server hoặc kiểm tra kết nối. Chỉ chạy Python
theo lệnh được duyệt. Không sử dụng thư viện ngoài, credential hoặc dịch vụ ngoài.

## Lỗi, cách xử lý và giới hạn còn lại

- `rg` không có trên máy (`The term 'rg' is not recognized`); không thử lại,
  dùng `Get-ChildItem` và `Get-Content` để đọc các file cần thiết. Không còn blocker.
- Lần đọc đầu bằng encoding mặc định của PowerShell hiển thị sai dấu tiếng Việt;
  đọc lại bằng UTF-8 thành công, không sửa nội dung nguồn vì lỗi hiển thị.
- Snapshot đã vượt trần không thể được bảo đảm hạ ngay khi phải đồng thời giữ
  Bot bận và giới hạn tốc độ; chỉ giảm Bot nhàn rỗi theo ngân sách, chặn spawn
  khi chạm trần tổng. Test có bao phủ trường hợp Bot bận vượt trần.
- Trần tính các Bot được quản lý, chưa bao gồm người chơi thật. Chưa xác minh
  map ID, trạng thái busy, ACK thực thi hoặc hành vi server runtime.
- Bên gọi phải giữ planner và cập nhật snapshot sau khi áp dụng từng batch;
  chưa có persistence, cơ chế nhiều worker hay thực thi bất đồng bộ.

## Trạng thái bàn giao

**DONE** trong phạm vi thư viện offline. Test yêu cầu đã chạy và đạt; runtime
server chưa kiểm, không thuộc phạm vi được duyệt. Chỉ bổ sung module, báo cáo
và mục Kết quả của task; giữ nguyên file task có sẵn chưa được Git theo dõi.
Commit SHA: chưa có vì task không yêu cầu commit. Push: chưa thực hiện vì task
cấm kết nối mạng; không có link GitHub để xác nhận.
