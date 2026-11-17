# TÓM TẮT 5 DÒNG

1. **BLOCKED về điều kiện giao việc:** không tìm thấy `I-07` trong `JX1_OPS/TASKS/BACKLOG.md`; quy tắc vận hành mục 11.4 yêu cầu worker dừng khảo sát khi thiếu mã backlog.
2. [NGUỒN] Đã phân biệt bạc trong túi/rương, XU nhân vật, điểm nạp `ExtPoint`, danh vọng và điểm Tống Kim/vinh dự; đây là kết quả đọc tĩnh, chưa phải hành vi runtime.
3. [NGUỒN] Hai nhánh `moneyunit_money` và `moneyunit_moneya` cùng dùng bạc thường tại các nơi đã đọc; chưa xác minh được một ví bạc khóa độc lập.
4. [NGUỒN] Giao dịch có cờ ràng buộc vật phẩm và danh sách tài khoản ngoại lệ; chưa thấy quan hệ hảo hữu cấp quyền chuyển đồ khóa ở những nhánh đã khảo sát.
5. Chỉ ghi báo cáo và mục Kết quả của task; không sửa source, không kết nối mạng/VM, không chạy game/exe, không đọc dữ liệu tài khoản thực; còn thiếu đối chiếu I-02 và các phần ghi bên dưới.

Ngày khảo sát: 2026-11-17. Nhánh xác nhận trước ghi: `task/I-07`; worktree: `D:\JX-wt\I-07`. Ban đầu task là file chưa được Git theo dõi, chưa có báo cáo `I-07-*.md`. Giữ nội dung giao việc, chỉ nối kết quả cuối file.

## Phạm vi và cách đọc bằng chứng

Quy ước đường dẫn, mọi số dòng là 1-based:

| Ký hiệu | Gốc |
|---|---|
| S | `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src` |
| G | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs` |
| C | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes` |

[NGUỒN] = câu lệnh/nhánh tồn tại trong source hoặc script, **không** chứng minh binary đang triển khai sử dụng đúng source đó. Không kiểm tra build manifest hay chạy binary. Chỉ trích symbol, điều kiện và vài giá trị liên quan; không sao chép nguyên bảng dữ liệu dài. Client gốc đã tìm thấy ở C, nhưng chưa đọc đủ luồng UI trước khi gặp blocker quy trình.

`I-07.md` không ghi commit prompt được ghim. Task có mục tiêu, đầu ra và vùng báo cáo; branch/worktree đúng. Kiểm tra backlog bằng tìm chuỗi `I-07|I-02` không có kết quả. Tra quyết định bằng từ khóa liên quan không tìm thấy quyết định riêng về I-07; không coi tìm từ khóa là rà soát toàn bộ mọi quyết định. Theo `JX1_OPS/QUY-TAC-VAN-HANH.md` mục 11.4, cần PM bổ sung/xác nhận mã backlog trong lượt có quyền sửa backlog trước khi tiếp tục source. Không tự sửa `BACKLOG.md` hoặc file trạng thái chung.

## ĐÃ XÁC MINH

### Ma trận các số dư đã thấy trong nguồn

| Loại | Định nghĩa và nơi lưu | Nguồn nhận đã thấy | Nơi tiêu đã thấy | Giới hạn/giao dịch đã thấy | Hiển thị/đồng bộ đã thấy |
|---|---|---|---|---|---|
| Bạc/lượng trong túi | `KInventory::m_nMoney`, thuộc `m_ItemList.m_Room[room_equipment]`; role `BaseInfo.iservermon` | `KPlayer::Earn` cộng vào túi | `Pay` → `CostMoney`; cửa hàng và đấu giá | `Pay` từ chối đầu vào âm; tiêu thông thường chỉ dùng túi. Giao dịch trực tiếp cho phép chọn tiền túi, phải không âm và không vượt số dư | `s2c_syncmonfs`: `m_nMoney1` = túi |
| Bạc/lượng trong rương | Cùng loại tiền, room khác `room_repository`; role `BaseInfo.isavemoney` | Có API `SetRoomMoney`, `AddmServer`; chưa lần đủ mọi điểm gửi/nhận | `DecMoney` dùng túi trước rồi rương, có thể xóa hết nếu yêu cầu lớn hơn tổng; không giống `Pay` | `GetMoney()` cộng túi+rương, trong khi `Pay()` chỉ trừ túi; không được dùng tổng này để suy ra mua được | `s2c_syncmonfs`: `m_nMoney2` = rương |
| XU nhân vật | `KInventory::m_nXu`, room equipment; role `BaseInfo.iclientx` | `EarnXu`; script Kim Nguyên Bảo; rút tiền trang | `PayXu`, shop và đấu giá loại `moneyunit_xu` | API `PayXu/EarnXu` chặn số âm; lõi cộng chỉ kiểm tra tổng âm, chưa có trần nghiệp vụ rõ ràng. Nhánh tiền giao dịch trực tiếp đã đọc chỉ có bạc, chưa có đường chuyển XU trực tiếp | `s2c_syncqianfs`, trường `m_nXu` |
| Điểm nạp / điểm thẻ `ExtPoint` | `KPlayer::m_nExtPoint`, biến thay đổi `m_nChangeExtPoint`; **không đồng nhất XU trong role** | `SetExtPoint`/`AddAndPayExtPoint`; chưa lần đường ghi PaySys/SQL | `PayExtPoint`; script tiền trang chuyển sang XU | Script `rutxuok` chặn từ 21.000 điểm trở lên; chưa xác minh persistence, trần, mất khi chết hay giao dịch | Tiền trang ghép `GetExtPoint()` vào lời thoại; chưa xác minh UI client/native packet |
| Danh vọng | `m_cRepute.m_nReputeValue`; role `BaseInfo.ireputevalue` | API Lua `AddRepute` trỏ `LuaSetPlayerReputeValue`; tên Set chưa đủ kết luận ngữ nghĩa Lua vì chưa đọc thân | Shop và đấu giá dùng `moneyunit_repute`, trừ `AddReputeValue(-price)` | Set/Add clamp sàn 0 và `MAX_REPUTE_VALUE`; chưa tìm giá trị define. Không thấy chuyển giữa hai người ở nhánh trade đã đọc | `s2c_reputesyncreputevalue` |
| Phúc duyên | `m_cFuYuan.GetFuYuanValue()`; chưa lần role field | Chưa xác minh | Shop và đấu giá `moneyunit_fuyuan`, trừ `AddFuYuanValue(-price)` | Chưa xác minh trần, mất khi chết, giao dịch | Chưa xác minh UI |
| Vinh dự | Shop/đấu giá `moneyunit_expoint` thực tế lấy `m_cTask.GetSaveVal(2051)` | Chưa xác minh nguồn thưởng | `SetSaveVal(2051, old-price)` | Không được suy từ tên `expoint` rằng tiêu `GetExtPoint()`; nhánh tiêu ExtPoint cũ đã comment | Chưa xác minh UI |
| Tích lũy Tống Kim | Shop/đấu giá `moneyunit_jifen` lấy `m_cTask.GetSaveVal(192)` | Hai script `tichluy_tongkim_tieu/dai.lua` cộng task 192 | Shop/đấu giá trừ task 192; script NPC quân nhu cũng đọc task 192 | Nhiều script cũ khác cũng đọc task 192, cần kiểm chứng tập script thực sự nạp; chưa có bằng chứng trần thống nhất | Script quân nhu ghép task 192 trong lời thoại; UI client chưa đối chiếu |
| Bạc khóa / tiền khóa | **Chưa xác minh được ví riêng** | Chưa xác minh | Trong hai đường mua đã đọc, `moneyunit_moneya` cùng trừ `Pay` như `moneyunit_money` | Không coi tên enum là bằng chứng ví khóa, càng không coi khóa vật phẩm là khóa tiền | Chưa xác minh |
| Vé / lệnh bài tiêu hao | Là vật phẩm tiềm năng, không phải số dư ví mặc định; cần xác định từng mẫu và script | Chưa xác minh đầy đủ | Chưa xác minh đủ đường tiêu và mapping bảng item | Phải xét cờ khóa, thời hạn, chồng vật phẩm, điều kiện sử dụng từng mẫu | Chưa xác minh |

Bằng chứng lưu/khôi phục: `S/KPlayerDBFuns.cpp:685` đọc `iclientx`, dòng 693 đọc `isavemoney`, dòng 701 đọc `iservermon`; `:1522`–`:1531` ghi lại ba trường. Danh vọng load `:746`, save `:1604`. Vật phẩm save cờ khóa ở `:1704`–`:1705` và load ở `:944`–`:945`.

Bằng chứng API: `S/KPlayer.cpp:7334` (`Pay`), `:7342` (`PayXu`), `:7381` (`Earn`), `:7393` (`GetXu`), `:7398` (`GetMoney`), `:7403` (`EarnXu`). `S/KItemList.cpp:3368`, `:3373`, `:3380`, `:3385`, `:3421`, `:3436`, `:3451`, `:3522`, `:3532`. `S/KInventory.h:39`–`:46` getter/setter hai số dư; `S/KInventory.cpp:368`–`:381` phép cộng.

Bằng chứng đơn vị cửa hàng: `S/KBuySell.cpp:392`–`:447` kiểm tra đủ tiền; `:512`–`:544` trừ từng loại; đấu giá `S/KPlayer.cpp:1293`–`:1347`, `:1428`–`:1457` có cùng các ánh xạ. Mới xác minh nhánh được đọc, chưa kết luận mọi NPC/cửa hàng đều dùng cùng quy tắc.

### Persistence của điểm task

[NGUỒN] `S/KPlayerDBFuns.cpp:1314` (`LoadPlayerTaskList`) đọc `TDBTaskData.m_nTaskId/m_nTaskValue` ở `:1376`–`:1382`; `SavePlayerTaskList` ở `:1796`, ghi cặp ID/giá trị ở `:1855`–`:1856`. Điểm Tống Kim và vinh dự trong bảng trên đi qua cơ chế task này. `KPlayerTask::GetSaveVal`/`SetSaveVal` kiểm tra ID ở `S/KPlayerTask.cpp:84`–`:106`; chưa xác minh mọi điều kiện lọc giá trị của toàn hàm và chưa có test thoát/vào lại.

### Kim Nguyên Bảo, XU và tiền trang

[NGUỒN] `G/script/mineitem/kimnguyenbao.lua:7` gọi `EarnXu(1)`. Hai lệnh xóa item ở `:4`–`:5` đang comment. **Chưa được kết luận nhân vô hạn:** còn có khả năng engine hoặc wrapper dùng item tự tiêu; cần lần mapping item và hàm gọi trước khi xác nhận lỗi. Không thử sử dụng item.

[NGUỒN] `G/script/global/npcchucnang/tientrang.lua:64` (`rutxuok`) đọc điểm thẻ, chặn `GetExtPoint() >= 21000` ở `:68`; nhánh sau có điều kiện `>=1` và `<=21000` ở `:77`, nhưng 21.000 đã bị chặn ở trên, nên miền đi được theo source là 1–20.999. `:78` cộng XU theo `XURUT + XURUT*KM`, `:80` trừ điểm nạp, `:81`–`:82` tăng bộ đếm nạp. `KM=0` ở `:4`.

Chưa thấy kiểm tra kết quả `EarnXu` trước `PayExtPoint` trong script này; cần test giao dịch nguyên tử khi cộng thất bại. Lời thoại bảng giá không phải chứng cứ tỷ giá nạp thực tế. Các hàm đổi cũ phía dưới file không được coi đang truy cập được từ menu chính chỉ vì còn tồn tại.

[NGUỒN] `S/KPlayer.cpp:11070`–`:11091` có getter, trừ, set ExtPoint. `PayExtPoint(int nPoint)` chỉ kiểm tra thiếu số dư ở `:11077`, chưa có kiểm tra `nPoint < 0` trong thân hàm đã đọc. Phải kiểm tra wrapper Lua/caller trước khi đánh giá khả năng khai thác; không thử gọi runtime.

### Giao dịch, đồ khóa và hảo hữu — đầu vào cho I-02

[NGUỒN] Phải phân biệt hai cơ chế:

| Cơ chế | Bằng chứng | Kết luận giới hạn |
|---|---|---|
| Ràng buộc vật phẩm `GetIsBang()` | `S/KItemList.cpp:6082`–`:6095` chặn đưa đồ cầm tay vào trade khi có `GetIsBang()` hoặc `GetUseMapIdx()`, trừ tài khoản ngoại lệ | Không có điều kiện “là hảo hữu” trong đoạn này |
| Kiểm tra tập vật phẩm trade | `S/KItemList.cpp:8835`, `:8841` xét bound/map/thời hạn và ngoại lệ của từng phía | Cần đọc đủ thứ tự/giá trị trả về để chốt toàn giao dịch |
| Danh sách ngoại lệ | `S/KPlayer.cpp:6073` (`CheckCanTradeName`) nạp `settings/tradename.txt`, so với tên tài khoản | **Không phải danh sách hảo hữu.** Không mở nội dung file danh sách tài khoản |
| Trạng thái khóa `LockItem.nState/dwLockTime` | `S/KItem.h:413`–`:460`; DBFuns load/save như trên | Trạng thái khóa là dữ liệu riêng với `GetIsBang`; chưa chứng minh cùng một mức chặn giao dịch |
| Khóa/mở khóa | `S/KItemList.cpp:10918`–`:10938` từ chối trạng thái FOREVER/CHARACTER; mở khóa gọi `LockItem(72)` | Mở khóa có thời gian chờ theo source; chưa xác minh UI hay hành vi trade trong thời gian chờ |
| Hảo hữu | `S/KPlayer.cpp:6447` (`ChatAddFriend`) và `:6465`–`:6466` thêm dữ liệu bạn hai phía | Không thấy hàm này thay số dư hay cấp quyền ngoại lệ trade trong đoạn đã đọc |
| Tiền trực tiếp | `S/KPlayer.cpp:6640`–`:6653` kiểm tra cấm trade/trạng thái khóa trade và tiền túi; `:6819`–`:6836` kiểm tra số dư hai phía | Bạc không khóa có đường chuyển bằng trade; thêm bạn không phải điều kiện đủ để hoàn tất |

**Trả lời hiện có:** đồ không ràng buộc có thể đi vào luồng giao dịch nếu thỏa những điều kiện khác; quan hệ bạn bè không tự cho phép chuyển đồ ràng buộc. Với đồ chỉ mang `LockItem.nState` mà `GetIsBang()==0`, chưa đủ bằng chứng để trả lời cho mọi trạng thái. Không suy “khóa = tuyệt đối không giao dịch” khi chưa đọc toàn đường. Vòng kiểm tra bound ở `S/KPlayer.cpp:6851`–`:6893` nằm trong block comment, không được dùng làm bằng chứng chặn đang hoạt động.

Không có `JX1_OPS/TASKS/I-02.md` và không tìm thấy `REPORTS/I-02-*.md` trong worktree lúc kiểm tra, nên chưa đối chiếu kết luận hay mapping do I-02 cung cấp. Các bằng chứng ở mục này là đầu vào bàn giao, chưa xác nhận tương thích I-02.

### Các dấu hiệu cần review, chưa sửa

| Dấu hiệu | Bằng chứng | Phân loại |
|---|---|---|
| `PrePayXu` gọi `Pay(nXu)` thay vì `PayXu(nXu)` | `S/KPlayer.cpp:7365`–`:7372` | [NGUỒN] sai khác đơn vị ở thân hàm; chưa xác minh caller đang dùng |
| Không có trần nghiệp vụ rõ ràng trước phép cộng số nguyên | `S/KInventory.cpp:368`–`:381` | [NGUỒN] chỉ kiểm tra biểu thức tổng âm; không khẳng định chống overflow an toàn trong C++ |
| Xóa item KNB đang comment tại script | `G/script/mineitem/kimnguyenbao.lua:4`–`:7` | [GIẢ THUYẾT] cần kiểm tra engine tự tiêu |
| Rút điểm nạp không kiểm tra kết quả cộng XU trước khi trừ | `G/script/global/npcchucnang/tientrang.lua:78`–`:82` | [NGUỒN] thứ tự lệnh; chưa xác minh rollback ở tầng khác |
| Tên `moneyunit_expoint` không trỏ điểm nạp ở shop đã đọc | `S/KBuySell.cpp:432`–`:438`, `:533`–`:538` | [NGUỒN] dùng task 2051, có nguy cơ mô tả sai đơn vị |

## CHƯA XÁC MINH

- **Điều kiện tiếp tục:** PM bổ sung/xác nhận `I-07` trong backlog; bổ sung tài liệu I-02 hoặc xác nhận chưa có. Đây là blocker quy trình, không phải lỗi đọc source hoặc thiếu quyền mạng.
- Chưa kiểm tra UI client gốc, nhãn tiền trong túi/rương/cửa hàng, định dạng vạn/lượng, giới hạn ô nhập và tooltip khóa. Chỉ biết packet/source server nêu trên.
- Chưa xác minh ví bạc khóa độc lập, điểm hoạt động cụ thể, nguồn thưởng/giá đổi đầy đủ của danh vọng/phúc duyên/vinh dự/Tống Kim.
- Chưa lần vé/lệnh bài đến bảng mẫu, script dùng, tiêu stack, nơi phát thưởng và quyền chuyển. Tên `lenhbaitanthu.lua` không tự chứng minh đây là vé bị tiêu hao.
- Chưa xác minh trần tiền/XU và điểm nghiệp vụ; không coi giới hạn kiểu số nguyên là trần cấu hình được phép đổi. Chưa đọc giá trị define `MAX_REPUTE_VALUE`.
- Chưa chốt mất tiền khi chết: thấy `DEATH_MODE_MONEY_PUNISH` tại `S/KNpc.cpp:11846`, nhưng chưa đọc đủ nhánh tính/trừ. `KNpc::LoseMoney` còn dùng cho quái rơi tiền, nên không lấy riêng tên hàm để kết luận người chơi mất bạc/XU.
- Chưa lần lưu điểm nạp qua PaySys/Goddess, giao dịch XU qua vật phẩm quy đổi, đấu giá trả tiền người bán, thuế/hoàn tiền và chuyển server. Không đọc SQL/dump/tài khoản thật.
- Chưa chứng minh file script được nạp trong binary triển khai; script cũ có thể trùng task ID hoặc không còn được dùng. Không đồng nhất mọi chỗ `GetTask(192)` với cùng một hoạt động đang bật.
- Không build, không test runtime, không kết nối VM/mạng. Mọi ca bên dưới **CHƯA CHẠY**.

## Ca test cho TESTER

Chỉ chạy sau một task thử nghiệm được duyệt riêng, trên dữ liệu thử; không dùng tài khoản thật. Ghi số dư trước/sau, UI, packet phù hợp và thoát/vào lại; không dùng báo cáo này làm quyền chạy VM.

| ID | Ca kiểm tra | Điều cần xác nhận |
|---|---|---|
| I07-T01 | Túi thiếu, rương đủ; mua bằng bạc, gửi/rút rồi thử lại | `GetMoney` tổng không đồng nghĩa `Pay` đủ tiền; cả hai số dư persist đúng |
| I07-T02 | Nhận/tiêu XU rồi đăng nhập lại | Chỉ `iclientx`/XU thay đổi; bạc không bị trừ nhầm |
| I07-T03 | Rút ExtPoint ở dưới, bằng, trên ngưỡng script | Phân biệt 20.999 và 21.000; XU tăng bằng điểm trừ khi KM=0; không mất điểm nếu nhận thất bại |
| I07-T04 | Dùng KNB một lần với stack kiểm soát | XU tăng đúng; xác định engine hay Lua tiêu vật phẩm; không kết luận nhân bản trước bằng chứng |
| I07-T05 | Mua từng đơn vị tiền trong shop và đấu giá | Bạc, XU, danh vọng, phúc duyên, task 2051/192 đúng số dư; không trừ điểm nạp thay vinh dự |
| I07-T06 | Hai tài khoản thử thường, so chưa kết bạn/đã kết bạn | Đồ không khóa, bound, map-bound, hết hạn và từng `LockItem` có kết quả riêng; thêm bạn không tự mở trade bound |
| I07-T07 | Trade bạc: hủy, khóa/mở, hai phía xác nhận, thiếu chỗ | Bảo toàn tổng tiền/vật phẩm; hủy trả đúng; không dùng tài khoản trong danh sách ngoại lệ |
| I07-T08 | Chết theo từng chế độ phạt và map an toàn | Định lượng túi/rương/XU/điểm trước-sau; tách phạt chết khỏi quái rơi tiền |
| I07-T09 | Điểm thưởng, tiêu điểm, thoát/vào lại | Task 192/2051 và danh vọng không bị ghi đè do script cũ; UI đúng đơn vị |
| I07-T10 | Một vé/lệnh bài đã xác định mẫu: đủ/thiếu điều kiện | Thành công tiêu đúng số lượng; thất bại không tiêu; kiểm tra khóa/thời hạn/stack |
| I07-T11 | Biên số dư qua công cụ thử có kiểm soát | Không âm/tràn/sai đồng bộ; chưa thử giá trị lớn trên runtime trong task này |

## Lỗi công cụ, xử lý và trạng thái bàn giao

| Sự việc | Cách xử lý | Kết quả |
|---|---|---|
| Đọc UTF-8 bằng mặc định PowerShell hiện mojibake | Đặt OutputEncoding và `Get-Content -Encoding UTF8` cho tài liệu; không ghi ngược chuỗi lỗi vào source | Đọc được văn bản; không đổi mã hóa file gốc |
| `rg : The term 'rg' is not recognized ...` | Chuyển sang `Select-String`/đọc trực tiếp Python `-I`; không cài công cụ | Tìm được source cần thiết |
| `UnicodeEncodeError: 'charmap' codec can't encode characters ...` khi in source | `sys.stdout.reconfigure(encoding='utf-8')`, đọc lại phần lệnh bị ngắt | Đọc được đoạn liên quan; không tạo parser/script phụ trên đĩa |
| Kết quả tìm rộng bị cắt | Thu hẹp sang symbol/đoạn cần đọc; kết quả bị cắt không dùng chứng minh đầy đủ danh mục | Các kết luận khẳng định ở trên có vị trí cụ thể; phần còn lại ghi chưa xác minh |
| Thiếu mã I-07 trong backlog | Giữ vùng file, không sửa backlog; lưu cùng báo cáo này | BLOCKED; PM xử lý điều kiện giao việc |
| Stage Git bị từ chối | Một lần `git add -- JX1_OPS/REPORTS/I-07-cac-loai-tien-te.md JX1_OPS/TASKS/I-07.md` | `fatal: Unable to create 'D:/jx1-reports/.git/worktrees/I-07/index.lock': Permission denied`; không thử vượt sandbox |
| Kiểm tra cấu trúc lần đầu trả false do literal Unicode qua stdin PowerShell | Đối chiếu lại bằng `Get-Content -Encoding UTF8` và `Select-String` | File có đúng Unicode, đủ các mục; không phải mất nội dung |

Trạng thái cuối: **BLOCKED** (có kết quả khảo sát tĩnh một phần). Bước tiếp theo: PM sửa điều kiện giao việc; sau đó tiếp tục từ các khoảng trống ở CHƯA XÁC MINH, ưu tiên UI client → tiền khóa/điểm hoạt động → vé/lệnh bài → phạt chết → I-02. Không làm lại những nhánh đã có bằng chứng.

Commit SHA: **không có**, stage bị chặn bởi quyền ghi Git metadata như lỗi ở trên. **BỊ CHẶN – CHƯA PUSH**. Người dùng cấm mạng trong task này; không thử remote, không dùng connector ngoài. Bản local đã lưu, PM có quyền phù hợp có thể review rồi stage/commit đúng hai file; không đổi credential/config/quyền để vượt lỗi trong phiên này.

## ĐỀ XUẤT TỐI ƯU

| Đề xuất cho task sau, không áp dụng ở đây | Lợi ước tính | Rủi ro | Cách đo lại |
|---|---|---|---|
| Ghi rõ tên nghiệp vụ cho các moneyunit và task ID, cùng mapping server/client | Giảm nhầm XU nạp với vinh dự; chưa có số đo thời gian | Đổi ID sẽ phá dữ liệu cũ; chỉ tài liệu hóa trước | Ma trận I07-T05, kiểm tra số dư/UI |
| Review phép cộng có kiểm tra tràn và trần đồng bộ server/client | Giảm nguy cơ số dư âm/sai; chưa định lượng | Đổi trần có thể mất dữ liệu/không tương thích packet | I07-T11 trên dữ liệu thử, trước/sau build được duyệt |
| Review giao dịch rút điểm theo cơ chế kiểm tra/hoàn tác khi nhận XU lỗi | Bảo toàn điểm nạp; chưa có tần suất lỗi | Tầng account có đồng bộ bất đồng bộ; tránh trừ hai lần | I07-T03 và thử lỗi có kiểm soát |
| Kiểm chứng cơ chế tự tiêu KNB và sửa mô tả khóa sau khi lần đầy đủ | Ngăn kết luận sai và phát hiện sai lệch nguồn tiền | Sửa vội có thể tiêu item hai lần | I07-T04, T06, T10 |

## MỤC SỔ THÔNG SỐ

Chỉ ghi số tác động đến tiền/điểm/khóa đã gặp; ID/enum được đánh dấu KHÔNG để tránh coi là núm cân bằng. Giá trị trong đoạn comment, menu cũ hoặc nhánh chưa xác minh không được coi đang có hiệu lực runtime. Nguồn đo ở đây là đọc tĩnh, không đo live.

| Nhóm | Tên/hằng số | file:line | Giá trị hiện tại | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Tiền trang | KM | G/script/global/npcchucnang/tientrang.lua:4 | 0 | tỷ lệ cộng thêm | XU nhận = điểm rút × (1+KM) | CẨN THẬN | source script |
| Tiền trang | Chặn điểm rút | G/script/global/npcchucnang/tientrang.lua:68 | >=21000 | điểm nạp | 21.000 bị chặn trước nhánh rút | CẨN THẬN | source script |
| Tiền trang | Điều kiện rút sau kiểm tra | G/script/global/npcchucnang/tientrang.lua:77 | 1..21000 | điểm nạp | Miền thực đi được 1..20999 do điều kiện trước | CẨN THẬN | source script |
| KNB | EarnXu | G/script/mineitem/kimnguyenbao.lua:7 | 1 | XU/lần gọi | Số XU cộng, chưa chốt tiêu item | CẨN THẬN | source script |
| Tiền trang | Giá tiểu hồng bao | G/script/global/npcchucnang/tientrang.lua:26 | 20000 | lượng | Ngưỡng và số bạc trừ dòng 27 | CẨN THẬN | source script |
| Tiền trang | Giá đại hồng bao | G/script/global/npcchucnang/tientrang.lua:36 | 110000 | lượng | Ngưỡng và số bạc trừ dòng 37 | CẨN THẬN | source script |
| Tiền trang cũ | Ngưỡng chế tạo DINGZHIA | G/script/global/npcchucnang/tientrang.lua:205 | 500 | điểm thẻ | Điều kiện gọi OpenVipDaZao; chưa chốt menu truy cập | CẨN THẬN | source nhánh cũ |
| Tiền trang cũ | Điểm giữ lại PayPiont | G/script/global/npcchucnang/tientrang.lua:261 | 500 | điểm thẻ | Chặn đổi khi số dư sau đổi thấp hơn | CẨN THẬN | source nhánh cũ |
| Khóa vật phẩm | Thời gian mở khóa | S/KItemList.cpp:10935 | 72 | giờ | Gọi LockItem theo thời gian chờ | CẨN THẬN | source C++ |
| Khóa vật phẩm | Quy đổi giờ | S/KItem.h:420 | 3600 | giây/giờ | Tính thời điểm khóa, không phải tỷ lệ cân bằng | KHÔNG | source C++ |
| Danh vọng | Sàn Set/Add | S/KPlayerRepute.cpp:46,70 | 0 | điểm | Clamp âm về 0 | CẨN THẬN | source C++ |
| Danh vọng | MAX_REPUTE_VALUE | S/KPlayerRepute.cpp:47,72 | Chưa đọc được giá trị define | điểm | Clamp trần; chưa đủ để đề nghị đổi | CẨN THẬN | tên hằng tại chỗ dùng |
| Điểm | Vinh dự | S/KBuySell.cpp:435,537 | 2051 | task ID | Ánh xạ số dư vinh dự | KHÔNG | source C++ |
| Điểm | Tống Kim | S/KBuySell.cpp:443,543 | 192 | task ID | Ánh xạ số dư Tống Kim | KHÔNG | source C++ |
| Tống Kim | Tích lũy tiểu | G/script/mineitem/tichluy_tongkim_tieu.lua:2 | 500 | điểm/lần gọi | Cộng task 192; chưa chốt mapping/tiêu item | CẨN THẬN | source script |
| Tống Kim | Tích lũy đại | G/script/mineitem/tichluy_tongkim_dai.lua:2 | 10000 | điểm/lần gọi | Cộng task 192; chưa chốt mapping/tiêu item | CẨN THẬN | source script |
| Nạp | TASK_NAP_XU | G/script/header/taskid.lua:172 | 1130 | task ID | Bộ đếm nạp tiền trang | KHÔNG | source script |
| Túi/XU | Sàn phép cộng | S/KInventory.cpp:370,378 | Tổng <0 bị từ chối | đơn vị số dư | Không thay thế kiểm tra overflow/trần nghiệp vụ | CẨN THẬN | source C++ |
| Trade | Miền tiền chào | S/KPlayer.cpp:6649 | 0..GetEquipmentMoney() | lượng | Ngoài miền đổi tiền chào thành 0 | CẨN THẬN | source C++ |
| Cổng Lua khác | RoleChangeMoney mặc định | S/ScriptFuns.cpp:14172 | 50000000 | tiền, chưa chốt nghiệp vụ | Giá trị fallback đọc từ Setting; ngoài nhánh đã lần | CẨN THẬN | giá trị mặc định source |
| Script mẫu đã thấy | PayXu | G/script/item/gm.lua:292 | 2000 | XU | Điểm gọi tiêu XU; chưa đọc điều kiện/hiệu lực | CẨN THẬN | kết quả tìm tĩnh |
| Script mẫu đã thấy | PayXu | G/script/item/34.lua:657 | 500 | XU | Điểm gọi tiêu XU; chưa đọc điều kiện/hiệu lực | CẨN THẬN | kết quả tìm tĩnh |
| Script mẫu đã thấy | PayXu | G/script/global/npcchucnang/sugiamonphai.lua:212 | 500 | XU | Điểm gọi tiêu XU; chưa đọc điều kiện/hiệu lực | CẨN THẬN | kết quả tìm tĩnh |
| Script mẫu đã thấy | EarnXu | G/script/item/xuanchuan.lua:14 | 20 | XU | Nguồn cộng có trong script, chưa chốt nạp thực | CẨN THẬN | kết quả tìm tĩnh |
| Script hoạt động | EarnXu | G/script/System/activity.lua:53 | inHour*2 | XU | Công thức thưởng theo biến giờ, chưa đọc điều kiện | CẨN THẬN | kết quả tìm tĩnh |
| Script hỗ trợ | EarnXu | G/script/global/npcchucnang/hotrotanthu.lua:989 | 10000 | XU | Nhánh hỗ trợ, chưa chốt quyền truy cập | CẨN THẬN | kết quả tìm tĩnh |
| Script hỗ trợ | AddDiemTongKim | G/script/global/npcchucnang/hotrotanthu.lua:961 | 100000 | điểm | Chưa chốt hàm định nghĩa và quyền truy cập | CẨN THẬN | kết quả tìm tĩnh |
| Script test/GM | EarnXu | G/script/global/npcchucnang/hotrotanthu_gm.lua:1039 | 5002 | XU | Comment ghi 5000, khác lệnh; chưa chốt hiệu lực | CẨN THẬN | kết quả tìm tĩnh |
| Script test/GM | EarnXu | G/script/global/npcchucnang/hotrotanthu_test.lua:506 | 100 | XU | Comment ghi 1000, khác lệnh; chưa chốt hiệu lực | CẨN THẬN | kết quả tìm tĩnh |
| Script mẫu đã thấy | PayXu | G/script/item/3434.lua:559 | 500 | XU | Nhánh song song với item/34, chưa chốt mẫu được dùng | CẨN THẬN | kết quả tìm tĩnh |
| Script mẫu đã thấy | PayXu | G/script/mineitem/gmroleitem.lua:304 | 3 | XU | Chưa đọc điều kiện/caller | CẨN THẬN | kết quả tìm tĩnh |
| Script mẫu đã thấy | PayXu | G/script/mineitem/gmroleitem.lua:371 | giờ 20 trả 6, giờ khác trả 3 | XU | Giá theo giờ; chưa chốt hiệu lực | CẨN THẬN | kết quả tìm tĩnh |
| Script GM | AddDiemTongKim | G/script/mineitem/gmroleitem.lua:2534 | 9999 | điểm | Chưa chốt quyền truy cập/hàm định nghĩa | CẨN THẬN | kết quả tìm tĩnh |
| Script áp tiêu | EarnXu | G/script/deadth/yabiao.lua:68 | tonumber(nJB)*2 | XU | Nhánh thưởng dùng biến nJB, chưa đọc nguồn biến | CẨN THẬN | kết quả tìm tĩnh |
