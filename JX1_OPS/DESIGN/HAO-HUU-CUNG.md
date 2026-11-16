# Thiết kế sơ bộ: Hảo hữu cứng (Chat, 2026-11-16) - BẢN NHÁP, chờ kết quả A-08

Nguồn yêu cầu: `owner-inputs/08`. Đây là bản nháp, chưa xác minh bằng mã. Mục "Chưa biết" phải được A-08 trả lời.

## Yêu cầu (tóm tắt)
- Mỗi môn phái (trừ phái của người chơi) có 1 **hảo hữu cứng**: số phái N -> N-1 hảo hữu mỗi người chơi.
- Hảo hữu thuộc về từng người chơi, người chơi tự trang bị và dắt đi luyện cấp.
- Tổ đội tối đa 5 người **kể cả người chơi** (tối đa 4 hảo hữu đi cùng). Chọn theo hoạt động: săn boss -> hảo hữu sát thương đơn mục tiêu; Tống Kim -> hảo hữu có chiêu diện rộng (AOE).
- Lửa trại: xuất hiện khi có boss tinh anh (màu xanh nước biển). Đốt cùng party: x2 kinh nghiệm và +0,5% kinh nghiệm cấp hiện tại mỗi giây.
- Nướng cá: người chơi có cá thì nướng, tăng **độ thân mật** với hảo hữu. Thân mật càng cao, hảo hữu lên cấp càng nhanh.

## Phát hiện từ kho kiểm kê (chưa đọc mã, chỉ thấy tên file)
- Server có `gs\Settings\faction\{faction.ini, MonPhai.ini}`, `script\header\factionhead.lua`: nơi lấy danh sách môn phái.
- Server có sẵn `gs\script\skill\partner\{fire,water,wood,earth,gold}` (10 file/hệ), `partner\expansion` (40), `partner\resistance` (5), `Settings\maps\partner\*`, và `script\deadth\同伴死亡` (xử lý "đồng bạn chết"). Có thể game gốc đã có **hệ thống đồng bạn (同伴)**. Chưa xác minh.
- Có `script\skill\special\篝火.lua` và `两湖区\npc\篝火.lua` (lửa trại), `两湖区\npc\烤鱼.lua` (nướng cá), `script\task\fishing.lua` (câu cá). Game gốc có thể đã có phần lớn cơ chế.
- Chưa thấy chữ "độ thân mật" trong tên file (có thể nằm trong nội dung Lua, chưa kiểm).

## Va chạm với giới hạn đã biết
- gs001 cứng 500 người online. Nếu hảo hữu là **tài khoản/nhân vật thật** (hướng (a)), mỗi tổ 5 người ngốn 5 chỗ: tối đa ~100 tổ, và trần Bot online ban đầu 100 nghĩa là chỉ ~25 người chơi có đủ 4 hảo hữu. **Không đủ cho tính năng này.**
- Nếu hảo hữu là **thực thể server (kiểu NPC/pet/đồng bạn)** thì không tốn chỗ người online. Đây là hướng nên ưu tiên nếu hệ thống đồng bạn gốc dùng được.
- Hảo hữu tự trang bị, có EXP, kỹ năng riêng: dễ với nhân vật thật, khó với pet nếu không có sẵn kho trang bị. Phải xem hệ thống đồng bạn gốc hỗ trợ đến đâu.

## Cân bằng (chủ dự án đã chốt một phần, 2026-11-16 23:37)
- **Lửa trại tồn tại 120 giây.** Mỗi giây +0,5% kinh nghiệm của cấp hiện tại: một lần đốt cho tối đa ~60% một cấp (chưa tính hệ số nhân đôi khi đốt cùng tổ đội; hiểu "nhân đôi" thế nào cần xác nhận lại: nhân đôi lượng đó, hay nhân đôi kinh nghiệm đánh quái trong lúc cháy).
- Thời hạn, % mỗi giây, hệ số nhân đặt trong `.ini` để chỉnh được.
- Chống lạm dụng: nhiều acc cùng đốt lửa trại, hảo hữu của acc phụ chia kinh nghiệm; cần hồi chiêu hoặc trần số lần mỗi ngày nếu thấy có lạm dụng.

## Việc kế (giao qua HOP-THU)
A-08: kiểm kê môn phái, đồng bạn, lửa trại, nướng cá, kinh nghiệm theo giây, thân mật. Sau đó Chat viết thiết kế chi tiết (B/E-phase) và chọn kiến trúc.
