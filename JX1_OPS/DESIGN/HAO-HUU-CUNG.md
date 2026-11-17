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

## KẾT QUẢ A-08 (đọc mã tĩnh, 2026-11-17 02:00) và kiến trúc đề xuất
**Môn phái:** có 16 mục khai báo, nhưng chỉ **11 phái gia nhập được** (Thiếu Lâm, Thiên Vương, Đường Môn, Ngũ Độc, Nga My, Thúy Yên, Cái Bang, Thiên Nhẫn, Võ Đang, Côn Lôn, Hoa Sơn). 5 mục còn lại (Lý Tầm Hoan, Đào Hoa Đảo, Minh Giáo, Đoàn Thị, Tự sáng môn phái) chưa đủ dữ liệu. Nghĩa là "15 phái" trong ví dụ của chủ dự án thực tế là **11 (-> 10 hảo hữu/người)**, tối đa 15-16 nếu mở thêm phái sau. Cần chủ dự án chốt.
**Hệ thống đồng bạn (同伴) gốc đã có:** là thực thể **NPC/pet** (`kind_partner`, tạo bằng `AddTongBan`), thuộc một người chơi, **không phải người online** nên **không chiếm chỗ trong 500 người**, chỉ chiếm ô trong pool NPC (`MAX_NPC`, chưa đo). Có AI theo chủ (`ProcessCompanion`: bám theo, đánh khi chủ đánh, chọn kỹ năng 1-4), có kỹ năng theo ngũ hành (95 file), có kho trang bị đồng bạn (`room_equipmentex`), có cờ lưu `IsCreatTongBan`.
**Chỗ thiếu:** (1) mỗi người chỉ **1 đồng bạn** (`m_TongBanNum` là một số); (2) cấp/EXP đồng bạn chưa thấy đường gọi hoàn chỉnh; (3) chưa lưu đủ dữ liệu từng đồng bạn; (4) kỹ năng gốc theo **ngũ hành**, không theo **môn phái**; (5) **không có độ thân mật**.
**Kiến trúc đề xuất:** hảo hữu cứng = **mở rộng hệ đồng bạn gốc**, không dùng tài khoản/nhân vật thật. Mỗi người chơi có danh sách (tối đa 10-15) hảo hữu, mỗi hảo hữu có dữ liệu: phái, cấp, EXP, thân mật, trang bị, kỹ năng. Tối đa 4 hảo hữu được gọi ra cùng lúc (tổ đội 5 kể cả người chơi). Hảo hữu là NPC server nên **không ăn chỗ online**: giải được bài toán trần 500 người. Việc cần làm: nhiều đồng bạn cùng lúc, lưu dữ liệu từng hảo hữu, gán kỹ năng môn phái cho NPC (kiểm hạn chế vũ khí), AI chọn kỹ năng theo vai (đơn mục tiêu/AOE), hệ cấp/EXP/thân mật.
**Lửa trại:** game gốc có script đốt lửa bằng vật phẩm (`huozhong.lua`, `gouhuo.lua`), sống 1.800/3.600 giây (không phải 120), EXP bảng cố định 5.000-15.000 mỗi 10 giây (`GouHouTime=10`). Chưa có: lửa sinh từ boss tinh anh, x2 khi cùng tổ đội, +0,5%/giây. Boss tinh anh xanh nước biển = `GoldType` 2-4 (client tô RGB 100,100,255, `KNpcGold.cpp`): có điểm móc để sinh lửa khi boss chết hoặc xuất hiện.
**Nướng cá:** game gốc chỉ có ăn cá trực tiếp; câu cá có callback nhưng thiếu bảng tọa độ. Nướng cá + thân mật là tính năng mới.
**Kinh nghiệm:** `AddOwnExp` chỉ cộng cho một người; `AddExp(exp,level,1)` chia theo tổ đội (cùng map, cách <= 768). `GetNextExp()` = ngưỡng EXP của cấp hiện tại. `SetTimer(18,id)` = 1 giây. Lưu ý `DirectAddExp` mất phần EXP vượt ngưỡng khi lên cấp: lửa trại +0,5%/giây phải tự xử lý lên cấp.


## KẾT QUẢ A-09/A-10 (Chat, 04:40)
- Số NPC: gs001 chọn MAX_NPC=100000 (nguồn); 100 người x 15 đồng bạn = 1500 NPC, chưa phải nút thắt. Chưa đo binary thực.
- m_TongBanNum là một DWORD đơn: nhiều slot cần viết lại quản lý slot/Lua/AI/trang bị/đồng bộ client. Roster 10-15 chưa tồn tại, cần bảng lưu riêng mỗi đồng bạn (task 10000 ID dùng chung buffer 128 KiB nên không đủ).
- Skill môn phái cho NPC có đường gán/cast; AI có hai điểm móc chọn vai (trước SetActiveSkill, FollowAttackCompanion) → chia vai đánh đơn/AOE làm được ở đó.
- Offline xóa NPC, đổi map teleport/xóa theo lockMap; chủ chết chưa có chính sách → phải định nghĩa.
- Lửa trại: boss xanh = GoldType 2-4; điểm móc là KNpc::OnDeath (OnGoldDeath đang comment, đồng bạn kết liễu không gọi callback). Lửa mẫu NPC 2078 skill 1705, sống 1800/3600 s; yêu cầu mới 120 s. Skill 1705/1706 thiếu trong Skills.txt; chưa chứng minh aura, x2 đội, 0,5%/giây chạy.
- Nướng cá và thân mật: chưa có gì, làm mới hoàn toàn.
- Quyết định chờ chủ dự án: số đồng bạn (10/15), nghĩa "nhân đôi", mô hình mặc định.

## Quyết định chủ dự án 17/11 07:01
- Lửa trại: nhân đôi kinh nghiệm mỗi người nhận (đã chốt). 
- Phân biệt: Pet (thú cưng, đi theo, 1 con, không phái) khác Hảo hữu cứng (đồng bạn NPC theo phái, có cấp, trang bị, thân mật, vai đánh đơn/AOE) khác Bạn bè (người chơi thật). Chủ dự án đang hình dung hảo hữu như đồng hành dạng pet; cần giải thích và chốt số lượng.

## Chốt 17/11 07:08
- 10 hảo hữu mỗi người (Q-36). Mục tiêu chơi: người chơi tự kiếm trang bị cho hảo hữu để tổ đội mạnh lên (A-12 khảo sát khả năng mặc đồ).
