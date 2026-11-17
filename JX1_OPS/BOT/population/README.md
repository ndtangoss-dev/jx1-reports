# Điều phối dân số offline

Thư viện thuần Python, chỉ thư viện chuẩn, **chưa nối server**. Không tạo
socket, không chạy exe, không thực thi các lệnh được lập kế hoạch.
Tên bản đồ trong ví dụ là dữ liệu tổng hợp, chưa ánh xạ map ID runtime.

API (import khi thư mục BOT đã ở đường dẫn package của ứng dụng):

```python
from datetime import datetime, timezone
from population import Bot, Config, Planner

config = Config.from_json("JX1_OPS/BOT/population/population.example.json")
planner = Planner(config)
now = datetime.now(timezone.utc)
targets = planner.desired(now)
commands = planner.plan([Bot("existing-id", "map-a", busy=True)], now)
```

Giữ nguyên một instance `Planner` để duy trì ngân sách và RNG. `current` là
snapshot đầy đủ các Bot được quản lý, gồm cả Bot ở bản đồ không còn cấu hình;
`bot_id` duy nhất, `busy` là bool do bên gọi cung cấp. `Command` gồm `action`
(`spawn`/`despawn`), `bot_id`, `map`; bên gọi phải áp dụng tuần tự danh sách lệnh
và phản ánh kết quả vào snapshot trước lần gọi tiếp. ID spawn tránh ID trong
snapshot và không lặp trong vòng đời planner. Chưa có bộ thực thi, ACK, retry,
đồng bộ nhiều planner hoặc lưu trạng thái qua restart.

`hourly_curve` gồm đúng 24 hệ số trong [0, 1], dùng giờ của datetime truyền vào,
không nội suy. Bên gọi chọn timezone và truyền thời điểm không giảm.
Số mong muốn tổng = floor(`total_cap` × hệ số giờ), mặc định trần 100;
phân bổ tỷ lệ trọng số bằng phần dư lớn nhất, phân phối lại phần vượt trần map.
Hòa phần dư được quyết định theo tên map. Trọng số phải dương hữu hạn,
trần phải là số nguyên không âm. JSON có trường không hợp lệ bị từ chối.

`max_changes_per_minute` đếm cả spawn và despawn trên cửa sổ trượt 60 giây;
mốc đúng 60 giây giải phóng ngân sách. Lệnh despawn luôn trước spawn.
Jitter là khoảng chờ ngẫu nhiên [0, `jitter_seconds`] giữa các đợt lệnh không rỗng,
kèm xáo thứ tự Bot nhàn rỗi/bản đồ; không thay đổi tổng mục tiêu. Cùng seed,
snapshot và chuỗi thời điểm sẽ cho cùng lệnh. Đặt jitter bằng 0 để bỏ khoảng chờ.

Bot bận không bị despawn. Nếu snapshot đã vượt trần, làm mượt và giữ Bot bận
có thể khiến trạng thái tiếp tục vượt trần; planner chỉ loại Bot nhàn rỗi theo
ngân sách và không spawn khi đã chạm trần tổng. Trần chỉ áp dụng cho các Bot
trong snapshot, chưa đo người chơi thật hoặc tổng online toàn server.
Tính an toàn khi thực thi đồng thời và kiểm chứng runtime nằm ngoài task này.

Kiểm tra offline từ gốc worktree:

```text
python -I -m unittest discover -s JX1_OPS/BOT
```
