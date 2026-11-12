# 37 - Phân tích khe lệnh đơn (command slot) của server và đề xuất kiến trúc sửa

Phạm vi: chỉ đọc mã `SwordOnline/.../gameserver/Sources`. Không sửa code, không chạy exe mới, không tạo VM, không đụng `JX-Server-D`. Mã nguồn có thể không khớp `gs001.exe` đang chạy (báo cáo 35, chưa so hành vi); mọi kết luận dưới đây là **từ mã nguồn, chưa kiểm bằng chạy thật**.

## TÓM TẮT 5 DÒNG
1. Mỗi NPC/nhân vật có đúng **một** ô lệnh `m_Command` (`KNpc.h:895`). Mọi gói đi/chạy/kỹ năng/ngồi/nhảy đều ghi vào ô này bằng `SendSerCommand` (`KNpc.cpp:6588`), **lệnh sau ghi đè lệnh trước, không có ưu tiên**.
2. Gói của client được xử lý **ngoài nhịp tick** (mỗi vòng `Breathe`, khoảng mỗi 1 ms), còn ô lệnh chỉ được **đọc một lần mỗi tick** (`KNpc::Activate` → `ProcCommand`, `KNpc.cpp:1000`). Kỹ năng bị chạy đè trong cùng cửa sổ một tick (55,6 ms ở 18 Hz) là mất hẳn: đây là nguyên nhân gốc đã đo ở báo cáo 33.
3. Có thêm **bốn chỗ mất lệnh khác**: bị bỏ khi nhân vật đang diễn kỹ năng (`m_ProcessAI = 0`), `DoSkill` âm thầm từ chối (hồi chiêu, không ở chế độ chiến đấu, thiếu nội lực, `m_Doing` bận), `m_randmove`, và lệnh bị xóa sau mỗi `ProcCommand` dù chưa thi hành.
4. Đề xuất: **hai làn (di chuyển / hành động), mỗi làn một chỗ, có hạn sống tính bằng mili-giây**, hành động không bị di chuyển ghi đè; lệnh dừng/ngồi/dịch chuyển xóa cả hai làn. Không hàng đợi vô hạn, không đổi giao thức.
5. Cách này đứng độc lập với tần số (18 hay 36 Hz); 36 Hz một mình **không** sửa được lỗi này, chỉ làm cửa sổ ghi đè nhỏ đi một nửa.

Cần tôi quyết định: có - chọn phương án mục 6 (A/B/C) và có tạo VM thử riêng để đo trước/sau không.

## 1. Luồng đầy đủ (kèm số dòng)
**Client gửi lệnh**
- Tay cầm ảo/nhấn đất gọi `KPlayer::Walk`/`KPlayer::Active` (`KPlayer.cpp:749-777`, `712-740`): ghi ô lệnh **cục bộ** (`SendSerCommand`) rồi gửi gói `SendClientCmdRun/Walk` lên server. Nhấn kỹ năng: `KPlayer.cpp:684` và `702` (`do_skill` + `SendClientCmdSkill`). Hai bản dùng chung mã `KNpc` nên client cũng có ô lệnh đơn.

**Server nhận gói** (chưa gắn với tick)
- `KSwordOnLineSever::Breathe` (`KSOServer.cpp:1425`) gọi `MessageLoop()` (`:1431`) **trước** khi kiểm tra tới giờ tick (`:1442`), rồi `Sleep(1)` khi chưa tới giờ (`:1466`). Nghĩa là gói được xử lý liên tục, cỡ 1000 lần/giây.
- Mỗi người chơi: tối đa `MaxClienLoop` gói mỗi lượt (50, đọc từ ini `KSOServer.cpp:743`), vòng `:1591-1605` → `PlayerFsMessageProcess` → `KPlayerSet::ProcessClientMessage` (`KPlayerSet.cpp:1258`) → `KProtocolProcess::ProcessNetMsg` (`KProtocolProcess.cpp:349`) gọi hàm theo bảng `ProcessFunc` (`:213-216`, `:268`).
- Hàm xử lý ghi ô lệnh: `NpcWalkCommand` (`:5436` → `do_walk`), `NpcRunCommand` (`:5452`, cũng gọi `CheckTrap()` ngay, `:5465` → `do_run`), `NpcSkillCommand` (`:5581`, kiểm ID kỹ năng `:5588`, đổi dwID mục tiêu sang chỉ số `:5599` → `do_skill`), `NpcJumpCommand` (`:5609` → `do_jump`), ngồi/đứng (`:6054`, `:6056`), dịch chuyển `do_special4` (`:375` phía client).

**Ghi vào ô** (`KNpc.cpp:6588-6608`): trước tiên nếu `m_randmove.nTime > 0` thì **bỏ** run/runattack/jump/jumpattack/skill/magic (`:6591-6601`); còn lại ghi `CmdKind` và ba tham số, đè lên mọi thứ đang có.

**Tick 18 Hz lấy lệnh** (`KNpc::Activate`, `:939`): bỏ nếu cùng khung (`:943`), bỏ nếu đang đổi server (`:951`), `NpcAI.Activate` (`:997-998`), rồi `ProcCommand(m_ProcessAI)` (`:1000`), rồi `ProcStatus()` (`:1003`) chạy máy trạng thái theo `m_Doing` (`:1212`).

**Thi hành** (`ProcCommand`, `:1296-1407`)
- Nếu `CmdKind == do_none` thì thoát.
- `nAI != 0`: `do_stand→DoStand`, `do_walk→Goto`, `do_run→RunTo`, `do_jump→JumpTo`, `do_skill→` tra kỹ năng trong danh sách (`FindSame`, `:1321`) rồi `SetActiveSkill` + `DoSkill` (nếu không có kỹ năng thì `DoStand`, `:1328`), `do_sit`, `do_defense`, `do_idle`, `do_hurt`, `do_revive`, `do_special4`.
- `nAI == 0`: chỉ xử lý `do_hurt` và `do_revive` (`:1373-1378`); mọi lệnh khác không làm gì.
- **Cuối hàm luôn `m_Command.CmdKind = do_none` (`:1406`)**, tức lệnh bị tiêu thụ dù có thi hành hay không.
- `RunTo`/`Goto` (`:4194`, `:4245`) phát gói `s2c_npcrun/walk` tới vùng lân cận rồi `DoRun/DoWalk` (`:3441`) **không kiểm tra** `m_Doing` hiện tại.
- `DoSkill` (`:3609`): thoát nếu `m_Doing == do_skill || do_hurt` (`:3615`); người chơi không ở chế độ chiến đấu thì thoát (`:3622`); đang hồi chiêu thì thoát (`:3647`, ngựa `:3655`); sau đó kiểm `CanCastByIndex`, `CanCastSkill`, `Cost` (trừ nội lực/thể lực **ngay lúc này**, `:3673-3674`); nếu qua: đặt thời điểm hồi chiêu kế (`:3682/3684`), phát `s2c_skillcast` cho vùng (`:3737-3745`), `DoOrdinSkill` (`:3779`) đặt `m_Doing = do_attack` (ngoại công, `:3820`) hoặc `do_magic` (nội công, `:3833`), **`m_ProcessAI = 0` (`:3836`)**, `nCurrentFrame = 0`. Không qua kiểm (hồi chiêu, thiếu nội lực...) thì `DoStand()` (`:3770`).
- Sát thương/đạn thực sự phát ra trong `OnSkill` (`:3979`) khi tới `ATTACKACTION_EFFECT_PERCENT = 60 %` của số khung hoạt cảnh (`KNpc.cpp:60`, `IsReachFrame` `:6852`); hết hoạt cảnh thì `DoStand` và `m_ProcessAI = 1` (`:3984-3988`).

## 2. Những loại lệnh dùng chung một ô
Toàn bộ: `do_stand, do_walk, do_run, do_jump, do_skill, do_sit, do_defense, do_idle, do_hurt, do_revive, do_special4` (và `do_magic`/`do_runattack`/`do_jumpattack` trong điều kiện `m_randmove`). Người chơi ghi từ gói client (mục 1) và từ nhiều nơi phía server: `do_stand` ở `KItemList.cpp:2864/7694`, `KNpcSet.cpp:1078`, `KRegion.cpp:538/877`, `KPlayer.cpp:7098/7102/9596/9635/9679`, `do_revive` `KPlayer.cpp:7308`. Quái vật chủ yếu gọi hàm `Do*` trực tiếp từ AI nên ít đụng ô này (chưa kiểm hết `KNpcAI.cpp`; các dòng `SendCommand` còn lại ở đó thấy nằm trong chú thích, chưa xác nhận).

## 3. Lệnh mới ghi đè lệnh cũ ở thời điểm nào
Bất cứ lúc nào trước lần `ProcCommand` kế tiếp. Vì gói được xử lý ~1 ms/lần còn tick 55,6 ms (18 Hz), trong một tick có thể có nhiều gói; chỉ gói **cuối** còn sống. Không có phân biệt ưu tiên: `SendSerCommand` chỉ có ngoại lệ `m_randmove` (`:6591`).

Hệ quả đã đo ở báo cáo 33: gói kỹ năng rồi gói chạy cách nhau vài ms (hoặc dính nhau do Nagle) trong cùng cửa sổ → kỹ năng mất, chạy thắng. Mô phỏng: kỹ năng được thi hành khi đang chạy: 0 % (bản gốc), 44 % (fix31), 100 % (fix33, nhờ chặn phía client).

## 4. Có phân biệt ưu tiên không
Không. Chỉ có hai cơ chế "gần giống ưu tiên", đều tình cờ:
- `m_ProcessAI = 0` trong lúc diễn kỹ năng làm `ProcCommand` bỏ mọi lệnh trừ `hurt/revive` (mục 1). Nên **chạy không hủy được kỹ năng đang diễn** trên server (tốt), nhưng **mọi lệnh gửi trong lúc đó bị bỏ luôn**, kể cả kỹ năng kế tiếp.
- `m_randmove` (trạng thái bị điều khiển/hỗn loạn) chặn chạy, nhảy, kỹ năng.

## 5. Các trường hợp mất lệnh (từ mã)
| # | Trường hợp | Chỗ trong mã | Mất cái gì | Gây ra thế nào |
|---|---|---|---|---|
| L1 | Kỹ năng bị chạy/đi đè trong cùng tick | `KNpc.cpp:6604-6607` | kỹ năng (cả sát thương lẫn hoạt cảnh) | một ô, ghi đè; gói xử lý ngoài tick |
| L2 | Lệnh đến lúc đang diễn kỹ năng | `ProcCommand` nhánh `nAI==0`, `:1373-1406` | kỹ năng kế tiếp, lệnh dừng, đổi hướng | `m_ProcessAI = 0` (`:3836`), rồi ô bị xóa |
| L3 | `DoSkill` từ chối âm thầm | `:3615`, `:3622`, `:3647`, `:3655`, `:3673` | kỹ năng | hồi chiêu chưa xong, ngoài chế độ chiến đấu, thiếu nội lực, `m_Doing` bận. Từ chối thì `DoStand` (`:3770`), nhân vật đứng lại giữa lúc đang chạy |
| L4 | `m_randmove` | `:6591-6601` | chạy/nhảy/kỹ năng | thiết kế, giữ nguyên |
| L5 | Kỹ năng bị đổi thành `DoStand` vì không tìm thấy trong danh sách | `:1321-1328` | kỹ năng | `FindSame` trả 0 |
| L6 | Kỹ năng mục tiêu: chỉ số NPC mục tiêu sai/đã đi | `KProtocolProcess.cpp:5599-5603` (`FindAroundNpc` không thấy thì **không gọi** `SendSerCommand`) và `KNpc.cpp:3709-3714` | kỹ năng | mục tiêu không còn trong vùng |
| L7 | Chạy và kỹ năng đến chéo thứ tự do mạng | `NpcRunCommand` / `NpcSkillCommand` | kỹ năng hoặc đoạn chạy | TCP giữ thứ tự gói trên **một** kết nối; nhưng Nagle ghép (đã sửa `TCP_NODELAY` ở fix33) và jitter làm cả hai rơi vào một cửa sổ |
| L8 | Chạy làm mất lệnh dừng/đổi hướng | `ProcCommand` | đổi hướng cuối trong cửa sổ | với lệnh di chuyển thì "cái cuối thắng" là đúng ý; vấn đề chỉ khi lệnh cuối là chạy còn lệnh trước là kỹ năng/dừng |

Không có xung đột "run hủy skill" ở server: `DoRun` không kiểm `m_Doing`, nhưng lệnh chạy không bao giờ tới `DoRun` khi `m_ProcessAI == 0` (L2). Do đó nguy cơ hủy giữa chừng chỉ xảy ra qua đường **trực tiếp** gọi `RunTo` từ script/mã khác (chưa rà).

## 6. Đề xuất sửa (chưa làm, chờ duyệt)
**Mục tiêu:** bảo toàn kỹ năng; không làm mất lệnh dừng hoặc đổi hướng; không hàng đợi vô hạn; giữ nguyên gameplay và giao thức.

**Ý tưởng chung: hai làn, mỗi làn đúng một chỗ, có hạn sống**
- Làn MOVE: `do_walk`, `do_run` (cái mới thay cái cũ: giữ nguyên "cái cuối thắng", để đổi hướng vẫn đúng).
- Làn ACT: `do_skill`. Cái mới thay cái cũ cùng làn.
- Lệnh KIỂM SOÁT: `do_stand`, `do_sit`, `do_jump`, `do_special4`, `do_revive`, `do_idle`, `do_defense`: xóa cả hai làn rồi tự thi hành (cái cuối thắng, nên lệnh dừng/ngồi/dịch chuyển không mất).
  **Đính chính sau mô phỏng (báo cáo 38):** riêng `do_stand` phải là lệnh **mềm** (chỉ xóa làn di chuyển, không hủy kỹ năng đang chờ). Bản "xóa cả hai làn" làm mất 9,5 % kỹ năng ở 18 Hz khi người chơi dừng ngay sau chiêu. Đây gọi là phương án A2.
- Quy tắc ghi:
  - MOVE đến khi ACT đang chờ: **không** ghi đè ACT (bỏ MOVE hoặc giữ MOVE cho sau, xem dưới).
  - ACT đến: xóa MOVE đang chờ (ý người chơi: dùng chiêu rồi mới đi; khớp với bảo vệ phía client ở fix33).
- `ProcCommand` mỗi tick: nếu `nAI`: thi hành ACT trước; nếu ACT đã bắt đầu một hoạt cảnh thì MOVE bỏ; ngược lại thi hành MOVE.
- Hạn sống tính bằng mili-giây, không bằng số tick: `TTL_ACT_ms` (đề xuất 250 ms ≈ 4-5 tick ở 18 Hz, 9 tick ở 36 Hz), `TTL_MOVE_ms` (đề xuất 120 ms). Quá hạn thì bỏ. Khi `nAI == 0` (đang diễn kỹ năng): **giữ nguyên hành vi cũ** (bỏ MOVE; ACT cũng bỏ ở phương án A, giữ tối đa TTL ở phương án B).
- Dung lượng cố định: 2 làn x 1 chỗ x vài byte; không có hàng đợi, không tăng theo thời gian.

**Ba phương án**
| | Nội dung | Rủi ro gameplay | Giải quyết |
|---|---|---|---|
| A (khuyến nghị) | Hai làn, ACT không bị MOVE ghi đè, ACT xóa MOVE, lệnh kiểm soát xóa cả hai. Khi `nAI==0` vẫn bỏ như cũ. | Gần như bằng 0: chỉ sửa L1 và L8. | L1, L8 |
| B | A cộng giữ ACT tới `TTL_ACT_ms` khi `nAI==0` (kỹ năng bấm lúc đang diễn kỹ năng sẽ chạy ngay khi xong). | Có: đổi nhịp tấn công người chơi, thêm "đệm phím". Cần cờ cấu hình, mặc định tắt. | L1, L2, L8 |
| C | B cộng đệm xác nhận (ack) từ server cho client biết kỹ năng bị từ chối (L3). | Cần thêm trường giao thức. Không giữ "nguyên giao thức". | L1-L3 |

Khuyến nghị: làm A trước, đo, rồi cân nhắc B. C chỉ khi thực sự cần và đã chấp nhận đổi giao thức.

**Vị trí sửa dự kiến** (khi được duyệt): `KNpc.h:895` (thêm trường), `KNpc.cpp:6588` (`SendSerCommand` định tuyến theo làn), `KNpc.cpp:1296-1407` (`ProcCommand` đọc hai làn, hạn sống), `KNpc::Load/Init` (khởi tạo). Gói và `ProcessFunc` giữ nguyên.

## 7. Một kiến trúc cho cả 18 Hz và 36 Hz
1. **Tách ba tầng.** (a) Nhận gói: không đổi, chạy mỗi vòng `Breathe`. (b) Hai làn lệnh: gắn dấu thời gian mili-giây lúc ghi (thời gian tường, cùng đồng hồ với `m_Timer`, `KSOServer.cpp:1442`). (c) Mô phỏng: `ProcCommand` mỗi tick lấy lệnh theo làn, kiểm hạn sống bằng mili-giây. Vì hạn sống tính bằng ms nên đổi 18→36 Hz **không đổi** ngữ nghĩa lệnh.
2. **Hệ số tần số.** Một hằng `TICK_HZ` (hiện nằm rải ở `KSOServer.cpp:90`, `CoreServerShell.cpp:2227`, và nhiều `GAME_FPS`/`FRAME2TIME`); lớp lệnh chỉ dùng `ms_to_ticks()` để quy đổi.
3. **18 Hz giữ nguyên toàn bộ dữ liệu**: hai làn chạy trên nhịp 18 Hz, không đụng `skills.txt`, `npcs.txt`, `missles.txt`, Lua, giao thức.
4. **36 Hz** (nhánh riêng, sau): chỉ nên bật khi đã quy đổi dữ liệu theo tick (báo cáo 34 mục 5). Lớp lệnh không cản trở việc đó; nó còn giảm xác suất đè ở 36 Hz xuống (cửa sổ 27,8 ms).
5. **Nếu 36 Hz quá sâu/không kiểm soát được:** dùng chế độ trung gian "tầng nhập liệu 36 Hz, mô phỏng 18 Hz": đọc hai làn mỗi 27,8 ms nhưng chỉ thi hành `DoSkill/DoRun` ở tick chẵn của mô phỏng 18 Hz. Cho client cảm giác nhận lệnh nhanh hơn mà không sửa dữ liệu. (Chưa phân tích kỹ; cần xét lại `m_LoopFrames`, `GetGameTime()`.)
6. **Client:** mã `KNpc` dùng chung nên ô lệnh phía client có cùng lỗi (mô phỏng cục bộ); giữ nguyên bảo vệ fix33 cho tới khi server có hai làn đã kiểm, rồi mới nới lỏng bảo vệ (bước riêng).

## 8. Kiểm chứng đề xuất trước khi sửa
- **Đo trước, chưa sửa:** thêm bộ đếm (chỉ in log, không đổi hành vi) vào `SendSerCommand` và `ProcCommand`: số lệnh bị ghi đè theo cặp loại lệnh, số lệnh bị bỏ do `nAI == 0`, số lần `DoSkill` từ chối theo lý do (L3). Dựng bằng bộ build ở báo cáo 35, chạy chỉ trong VM thử riêng, DB riêng.
- **Mô phỏng ngoài game:** viết mô phỏng đơn giản của hai làn với lưu lượng gói thực (kỹ năng + chạy 9 gói/giây, RTT 150 ms, jitter) ở 18 và 36 Hz để so tỉ lệ kỹ năng được thi hành.
- **Tiêu chí:** kỹ năng thi hành khi đang chạy → 100 %; không có lệnh nào sống quá TTL; số lệnh dừng/ngồi/dịch chuyển bị mất = 0; không đổi nhịp tấn công khi không bấm đè.

## 9. Điều chưa biết / chưa kiểm tra
- Chưa chạy: mọi nhận định về vòng `Breathe`, `MessageLoop` (mỗi ~1 ms) lấy từ đọc mã, chưa đo thật.
- Mã nguồn có thể không khớp `gs001.exe` đang chạy (báo cáo 35).
- Chưa rà toàn bộ lời gọi `RunTo/Goto/DoSkill` trực tiếp từ script Lua (`ScriptFuns.cpp`) và `KNpcAI.cpp`.
- Chưa kiểm các gói khác có thể ghi ô lệnh (`KProtocolProcess.cpp:2424`, `NpcSync->m_Doing`) khi chạy.
- `KNpc_backup.cpp`, `KPlayer - Copy - Copy.cpp` là bản sao cũ trong thư mục, chưa rõ có nằm trong project không; đã lấy mã từ `KNpc.cpp` và `KPlayer.cpp`.

## 10. Không làm trong bước này
Không sửa mã, không chạy exe mới, không tạo VM, không đụng `JX-Server-D`, CDN, forwarder, không commit. Chỉ thêm báo cáo này.
