# JIBS – Đánh giá kế hoạch Bot (7 câu)

**TÓM TẮT**
1. Giao thức client–gs001 **không có tài liệu**; có mã nguồn cả hai phía (đủ để đọc, không phải đoán thuần), nhưng chưa có bot nào đã chạy được.
2. Sức chứa cứng 500 người (`MAX_PLAYER`), 1 luồng, 18 Hz; chưa đo số online thật.
3. Có chỗ lọc "ai thấy ai", nhưng là theo ô bản đồ (region), không theo bán kính; vá được trong `KRegion::BroadCast` (cần dựng lại gs001).
4. Dựng từ nguồn được (VS2022 v143 x64), nhưng gs001 tự dựng crash (0xC0000005) sau "public net IP"; nguyên nhân gốc chưa tìm ra.
5. Tạo tài khoản bot: ghi thẳng `Account_Info` + `Account_Habitus` (SQL), nhân vật tạo qua client/Bishop; cấp EXP/vật phẩm hợp lệ có sẵn qua Lua (`AddOwnExp`, `AddItem`) nhưng chạy trong script server.
Cần tôi quyết định: có (chọn hướng bot: giao thức thô hay vá server; xem cuối).

Nhãn: "Chứng cứ" = đã đọc mã/báo cáo; "Chưa kiểm" = chưa chạy/đo.

## 1. Giao thức client–gs001
- Chứng cứ (tái dùng `reports/16-khao-sat-bot-ai.md`, `29`, `44`): khung gói 2 byte độ dài; mã hóa XOR khóa cuộn từ `ACCOUNT_BEGIN` (0x20); đăng nhập MD5 qua Bishop 56722 rồi chuyển sang gs001 51189 (`gateway/.../Bishop/GameServer.cpp`, `SmartClient.cpp`; client `gameui/KSelPlayer.cpp`). Lệnh đi/chạy (Run), skill, ngồi (Sit), đội, chat đều có gói riêng; client nhận cờ chiến đấu `0x02` ở `gamecore/KProtocolProcess.cpp`.
- Tài liệu: **không có** tài liệu giao thức; chỉ có mã (client Cocos `Client/Classes` và server `Core/Src`). Bảng gói tin là việc A-06 (chưa làm, Codex đang lỗi model 404).
- Chưa kiểm: chưa có bot nào đăng nhập hoàn chỉnh bằng giao thức thô; chưa đối chiếu mã nguồn với exe đang chạy (nguồn mới hơn exe).

## 2. Sức chứa gs001
- `MAX_PLAYER 500` cứng (`Core/Src/KPlayerDef.h:17`); giá trị MaxPlayer trong ini bị ghi đè về 500 (`MultiServer/GameServer/KSOServer.cpp:770-772`).
- Vòng lặp: `GAME_FPS 18` (`KSOServer.cpp:90`), `Breathe()` (dòng 1425) có vòng bù nhịp (dòng 1442) rồi `MainLoop()` (dòng 1450): **một luồng**. Số NPC tối đa lấy từ `Gameconfig MaxNpcCount` (`Core/Src/KCore.cpp:292`).
- Báo cáo 41/43/59: đã xác nhận 18 Hz; thử 36/54 Hz có kế hoạch riêng.
- Chưa kiểm: số online thật chịu được trước khi tick trễ (chưa đo); 500 cứng nên bot + người thật dùng chung 500 chỗ.

## 3. Lọc hiển thị
- Gửi đồng bộ theo vùng: `KNpc::SendDataToNearRegion` (`KNpc.cpp:14103`) gọi `KRegion::BroadCast` cho ô của NPC và 8 ô lân cận (bảng `POff`/`m_nConnectRegion`).
- `KRegion::BroadCast` (`KRegion.cpp:2223`): duyệt `m_PlayerList`, tối đa `MAX_BROADCAST_COUNT = 100` người/ô (`KRegion.h:15`), gửi cho người có `m_nNetConnectIdx >= 0` và `m_bSleepMode == FALSE`. Điều kiện khoảng cách (`MAX_SYNC_RANGE 32`) **bị comment**, nên không có lọc theo bán kính.
- Vá được: chỗ chèn điều kiện "viewer thấy NPC này không" nằm đúng trong vòng lặp này (cần dựng lại gs001, xem mục 4).
- Chưa kiểm: các đường gửi khác không qua hàm này (`BroadCastState` `KNpc.cpp:14485`, `SendSyncData` `KNpc.cpp:7663`); chưa thử vá.

## 4. Dựng lại gs001, vì sao A2 crash
- Chứng cứ (`reports/35`, `44`): dựng được bằng VS2022 v143 x64 với vài chỗ lách; gs001 tự dựng chạy tới "public net IP" rồi crash 0xC0000005; exe gốc + DLL A2 chạy ổn.
- Nguyên nhân A2 crash: **chưa kết luận** (báo cáo 44 ghi giả thuyết, chưa có bằng chứng chốt). Mã nguồn mới hơn exe gốc nên khác hành vi là khả dĩ.
- Chưa kiểm: bản dựng khớp byte với exe gốc; cách làm sạch crash (cần debug trên VM thử, hiện treo).

## 5. Tạo hàng loạt tài khoản/nhân vật Bot
- Tài khoản: dòng trong `Account_Info` (mật khẩu MD5 viết hoa) và `Account_Habitus` còn hạn (`S3PAccount.cpp`; thực hành ở `reports/02-b2-account-db.md`).
- Nhân vật: tạo qua luồng tạo nhân vật của client/Goddess (`Goddess/DBTable.cpp`, `IDBRoleServer.cpp`); bot phải nói được bước này qua Bishop.
- An toàn: chỉ làm trên DB bản copy ở VM thử; không dùng tài khoản/mật khẩu thật, không ghi mật khẩu vào file (truyền qua biến môi trường); `reports/09` đã xóa tài khoản thật khỏi DB.
- Chưa kiểm: tạo hàng loạt (chưa thử); giới hạn số nhân vật/tài khoản; ảnh hưởng của `S3Relay` (bang, bạn bè).

## 6. Cấp EXP/vật phẩm hợp lệ
- Có: Lua server `AddOwnExp` (`ScriptFuns.cpp:15908`, gọi `DirectAddExp`), `AddItem`/`AddItemEx` (đăng ký `ScriptFuns.cpp:25958-25959`), `AddGoldItem*` (8578-8765). Đây là đường cấp **qua script server**, dùng được cho bot (script NPC/quest chạy trong gs001).
- Cách hợp lệ không sửa mã C++: viết script Lua ở `gs\script\...`.
- Chưa kiểm: có lệnh GM trực tiếp từ client không (chưa dò); script của bản đang chạy có gọi được các hàm trên không.

## 7. CPU/RAM thật của VM
- Cấu hình: 4 CPU, 6144 MB (cả `JX-Server-D` và `JX-Test-36`, `VBoxManage showvminfo`; `reports/42`). Hiện `JX-Server-D` running, `JX-Test-36` kẹt "stopping".
- **Chưa đo mức dùng thật** (VM thử treo, Main VM chỉ đọc theo Q-18). Cần đo CPU/RAM trong guest khi gs001 chạy có tải rồi mới kết luận.

## Đề xuất / Cần tôi quyết định: có
Chọn hướng bot: (a) thô qua giao thức (không đụng server, nhưng chưa có tài liệu) hoặc (b) vá `KRegion::BroadCast` (cần giải crash gs001 tự dựng trước). Khuyến nghị (a) trước, A-06 làm bảng gói tin, sau khi Codex được sửa model.
