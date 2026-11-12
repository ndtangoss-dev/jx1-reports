# Khảo sát bot AI (chỉ đọc mã nguồn, chưa sửa gì)

## TÓM TẮT 5 DÒNG
1. Bot tổ đội làm được bằng một "client không giao diện" viết bằng Python, đăng nhập như người chơi thật.
2. Mã hóa gói tin đơn giản (XOR khóa xoay), luồng đăng nhập và lệnh đi, đánh, mời tổ đội, chat đều có trong mã client.
3. Bot Tống Kim nên làm phía server bằng Lua: kịch bản Tống Kim gốc đã tự tạo lính NPC hai phe, NPC khác phe là kẻ địch.
4. Chưa chắc: mã nguồn có khớp exe đang chạy không, NPC có tự đánh NPC khác phe không. Cần thử nhỏ để biết.
5. Đề xuất làm theo thứ tự: thử NPC đánh nhau, rồi 1 bot đăng nhập, rồi đi theo, tổ đội, lệnh "tập trung", rồi Tống Kim.

Cần tôi quyết định: có

## 1. Bot tổ đội (4-5 bot đi cùng người chơi)

Cách làm: chương trình Python chạy trong VM, mỗi bot là một tài khoản và nhân vật thật, kết nối như client điện thoại.

Bằng chứng trong mã client (`Folder/Client2912-.../Client/Classes`):
- Khung gói: 2 byte độ dài (tính cả đầu gói) rồi dữ liệu (`network/ClientStage.cpp:140-268`).
- Mã hóa: XOR từng 4 byte với khóa, phần lẻ XOR với byte thấp của khóa, sau mỗi gói `key = key*31 + 134775813` (`KSG_EncodeDecode.cpp`).
- Khóa lấy từ gói `ACCOUNT_BEGIN` (loại `0x20`) server gửi khi vừa kết nối, khóa hai chiều bị đảo bit (`network/SocketClient.cpp:455-525`, `Cipher.h`).
- Đăng nhập: `c2s_login` tới Bishop 56722, mật khẩu MD5 (`Klogin.cpp:471-495`). Bishop trả địa chỉ gs và GUID, client nối gs và gửi GUID.
- Lệnh: `SendClientCmdRun(x,y,map)`, `SendClientCmdSkill(skill,x,y)`, `SendClientCmdSit` trong `gamecore/KProtocol.cpp`.
- Tổ đội: `c2s_teaminviteadd` (`KPlayerTeam.cpp:74-78`), nhận lời `c2s_teamacceptmember` (`KPlayer.cpp:1790`), lời mời đến `s2c_teaminviteadd`.
- Chat: `c2s_extendchat` / `s2c_extendchat`. Bot đọc kênh đội, thấy chữ "tập trung" thì chạy về tọa độ người chơi.

Hành vi theo luật, không cần AI ngôn ngữ:
- Đi theo người chơi khi cách xa quá N ô.
- Có quái gần thì dùng chiêu; máu thấp thì uống thuốc hoặc lùi.
- Lệnh chat: "tập trung", "đánh", "nghỉ", "về thành".

## 2. Bot Tống Kim (10 phe ta, 25-30 phe địch)

Cách làm: NPC do server tạo bằng Lua, không cần tài khoản, nhẹ hơn nhiều so với 40 client.

Bằng chứng:
- Kịch bản Tống Kim gốc đã tạo lính hai phe: `gs\script\missions\宋金战场pk战\sj_creatnpc.lua:137-142` gọi `AddNpc(random(631,635),75,...)` trong vòng lặp.
- Quan hệ: hai NPC thường khác phe trả về kẻ địch (`Core/Src/KNpcSet.cpp:214-218`). NPC với người chơi khác phe cũng là kẻ địch (dòng 176-177).
- Lua có `AddNpc`, `SetNpcCurCamp`, `SetNpcCamp`, `SetNpcPos`, `SetNpcScript`, `SetNpcDeathScript` (`ScriptFuns.cpp:26192-26209`). Tham số 8, 9 của `AddNpc` là cờ vàng và boss (`ScriptFuns.cpp:12670-12675`), không phải phe.
- NPC tìm mục tiêu bằng `GetNearestCharacter(relation_enemy, ...)` (`KNpcAI.cpp:2248`), quét các NPC trong tầm nhìn qua `FindNpcAuto`.

Kế hoạch: tạo NPC rồi gọi `SetNpcCurCamp` cho mỗi phe, đặt điểm xuất phát hai đầu bản đồ, cho chạy về giữa bằng `SetNpcPos` theo đợt hoặc điểm tuần tra.

## 3. Hệ thống "đồng hành" có sẵn
33 file Lua gọi `PARTNER_*`, nhưng mã nguồn server không đăng ký hàm nào tên `PARTNER_`. Có thể exe có mà nguồn không có. Không dựa vào phần này.

## Chưa kiểm tra
- Mã nguồn có khớp exe đang chạy không (CLAUDE.md đã ghi chưa dựng lại từ nguồn). Cấu trúc gói tin có thể lệch, chỉ biết khi bot thật kết nối.
- `FindNpcAuto` có chọn NPC khác phe làm mục tiêu không, hay chỉ người chơi.
- Cấu trúc gói tổ đội, chat, danh sách nhân vật ở Bishop, bảng kích thước gói server gửi về.
- Bản đồ Tống Kim có nằm trong 28 bản đồ thiếu `.wor` không.

## Thứ tự đề xuất
1. Thử NPC đánh nhau: một file Lua nhỏ (bản sao, có `.bak`) tạo 2 nhóm NPC khác phe cạnh người chơi ở Biện Kinh. Cần khởi động lại `gs001` (khoảng 7 phút).
2. Bot đăng nhập: tạo 1 tài khoản bot trong SQL (`Account_Info`, `Account_Habitus`), viết Python nối Bishop, chọn nhân vật, vào gs, đứng yên.
3. Bot đi theo, nhận lời mời tổ đội, nghe lệnh "tập trung". Rồi nhân lên 4-5 bot.
4. Bot đánh quái cùng người chơi.
5. Tống Kim: gắn bước 1 vào kịch bản Tống Kim, 10 NPC phe ta, 25-30 phe địch.

Mỗi bước cần duyệt riêng: sửa Lua server, tạo tài khoản bot, chạy chương trình bot, khởi động lại `gs001`.
