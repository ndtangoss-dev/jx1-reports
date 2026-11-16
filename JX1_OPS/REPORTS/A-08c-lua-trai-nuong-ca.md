TÓM TẮT 1: Có script tạo lửa bằng vật phẩm/GM/task, chưa chứng minh boss tinh anh sinh lửa (`G/script/item/huozhong.lua:74–89`; `S/KNpc.cpp:2618–2623`).
TÓM TẮT 2: Lửa được đặt sống 1.800/3.600 giây, có thêm củi; chưa phải luật 120 giây (`G/script/item/huozhong.lua:79`; `G/script/task/gouhuo.lua:29`; `N:85–108`).
TÓM TẮT 3: Có bảng EXP cố định 5.000–15.000 và callback theo GouHouTime=10; thiếu nối skill 1705/1706, chưa xác nhận x2 party hay +0,5%/giây (`K:8`; `S/KNpc.cpp:1801–1817`; `G/Settings/gamesetting_gs001.ini:503`; E02).
TÓM TẮT 4: Nướng cá đang chỉ báo ăn cá trực tiếp; câu cá có callback cấp item nhưng thiếu bảng tọa độ (`F:48–50`; `G/script/tnlteam/cauca/quahuyhoang.lua:115–135`; E03).
TÓM TẮT 5: GoldType 2–4 được client gán RGB 100,100,255; mọi kết quả là đọc tĩnh, chưa kiểm game/VM (`S/KNpcGold.cpp:479–498`; `C/KNpc.cpp:5334–5347`).

# A-08c — Lửa trại và nướng cá

Ngày kiểm tra: 17/11/2026. **Nội dung: DONE trong phạm vi khảo sát tĩnh**; các điểm chưa thể nối hoặc chưa thử được ghi rõ bên dưới. Không khẳng định bản exe đang chạy dùng đúng những file này.

## Worker kiểm tra trước khi làm

- Đã đọc task trước khi điều tra. Working directory của lệnh là `D:\JX-wt\A-08c`; `git status --short --branch` trả `## task/A-08c-codex`, không có thay đổi local. Khớp `JX1_OPS/TASKS/A-08c.md:7–8`.
- Chỉ tạo báo cáo này; cập nhật phần kết quả của chính task theo yêu cầu trực tiếp của người dùng. `C:\Jx1CocoV3` chỉ đọc, không chạy exe/build, không kết nối VM/SQL/server, không đọc hoặc ghi credential.
- Đã đọc A-03 và D-01: không dùng thống kê thiếu Lua ở cây source thay cho gói gs; chưa coi script trên đĩa là runtime đang hoạt động (`JX1_OPS/REPORTS/A-03-kiem-ke-cau-hinh.md:9,102–105`; `JX1_OPS/REPORTS/D-01-bang-hoat-dong.md:4,92–97`).
- Đã đọc tài liệu chủ dự án và bản thiết kế nháp ở `D:\jx1-ops-wt\JX1_OPS`: boss xanh → lửa, x2 party, +0,5%/giây, nướng cá tăng thân mật là yêu cầu; 120 giây là thông số thiết kế đã ghi, không phải hành vi đã xác minh (`owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md:3`; `DESIGN/HAO-HUU-CUNG.md:9–10,23–25`).

## Quy ước nguồn và mã hóa

| Ký hiệu | Đường dẫn thật |
| --- | --- |
| `G/` | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\` |
| `S/` | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\` |
| `C/` | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\` |
| `K` | `G/script/skill/special/óô»ð.lua` — tên logic `篝火.lua` |
| `N` | `G/script/Á½ºþÇø/npc/óô»ð.lua` — tên logic `两湖区/npc/篝火.lua` |
| `F` | `G/script/Á½ºþÇø/npc/¿¾Óã.lua` — tên logic `两湖区/npc/烤鱼.lua` |

Số dòng tính từ 1 theo LF của byte gốc, giữ dòng trống. Markdown và client `KNpc.cpp` đọc UTF-8. Lua Hán tự đọc CP936/GBK; phần tiếng Việt chứa byte legacy không thuần GBK, nên giữ token ASCII và kiểm byte thô khi dấu nháy hiển thị bất thường. `goldacition.lua` là UTF-8. Không đổi tên/chuyển mã/ghi lại nguồn.

### Bằng chứng đọc filesystem và tìm kiếm có giới hạn

- **E01:** Đường literal Hán tự của ba script không tồn tại; tìm trong `gs/script` thấy đúng ba tên vật lý K/N/F ở bảng trên. Đối chiếu các đường `SetNpcScript` Hán tự trong `G/script/item/huozhong.lua:83` và `G/script/Pass/creatcitynpc.lua:607` với tên giải mã từ CP936 → Latin-1. Đây là lệch tên filesystem; chưa chứng minh loader runtime có thể nối hai dạng.
- **E02:** Tìm token `gouhuo`, `addexp_v`, `篝火` và cột `SkillId` bằng `1705`/`1706` trong toàn bộ `G/Settings/Skills.txt`: không có kết quả. Vì vậy chưa có dòng cấu hình nối K với hai skill mà N và các script spawn sử dụng. Không tìm/trích archive `Settings_skills_V1.rar`, không kiểm PAK.
- **E03:** Đọc literal `G/Settings/maps/great_night/phonglangdofish.txt` trả `ENOENT: no such file or directory`. Đây chính là đường được `G/script/tnlteam/cauca/lib_huyhoang.lua:47` truyền tới `TabFile_Load` ở dòng 64. Chưa kiểm bảng có trong PAK hoặc tên khác.
- **E04:** Tìm các literal lửa `篝火`, `gouhuo`, `1705`, `1706` trong Lua rời và đọc các nhánh spawn liên quan: có item/GM/task; không thấy lời gọi tạo lửa trong `G/script/global/golddeath.lua` đã đọc. Kết luận chỉ giới hạn cây file rời/nhánh này, không phủ mọi death script hoặc PAK.

## Sinh lửa khi nào, ai thấy và thời hạn

| Nhánh | Hành vi trong code | Bằng chứng |
| --- | --- | --- |
| Dùng vật phẩm `huozhong` | Chặn khi đang có state 1705/1706; map 53 còn chặn gần NPC tân thủ dưới 512 đơn vị. `CheckMap()==1` hoặc đang chiến đấu (`GetFightState()~=0`) thì không tạo. Tạo NPC template 2078 gần vị trí người dùng, skill 1705 cấp 50. Lệnh xóa item bị comment, không suy rằng lửa tiêu hao vật phẩm. | `G/script/item/huozhong.lua:35–65,69–89` |
| Task lửa ban ngày | `taskcontent` chỉ chạy thân khi ngày >=20210521, tạo tại map 53, tọa độ nội bộ (51717,102750), skill cấp 30, sống 3.600 giây. | `G/script/task/gouhuo.lua:7–33` |
| Task lửa lớn | Tạo cùng vị trí map 53, cấp 50, sống 3.600 giây. | `G/script/task/dahuo.lua:7–29` |
| Lịch khai báo | `tasklist_default.ini` khai báo `dahuo.lua` lúc 20:00 và `gouhuo.lua` lúc 11:00, cả hai `IsOpen=-1`. Đây là dữ liệu lịch, chưa chứng minh scheduler nạp file này hay hai hoạt động được mở. | `G/Settings/Task/tasklist_default.ini:401–409,421–429` |
| GM | `GIVEHUOZHONGA` nhận cấp nhập vào, tạo NPC 2078 gần người gọi, skill 1705 cấp đó, sống 3.600 giây. Chỉ ghi nhận hàm, chưa xác minh quyền/menu và các biến truyền vào. | `G/script/item/gm.lua:1070–1106` |

**Ai thấy:** Các nhánh trên tạo NPC trong subworld dùng chung, không có kiểm party/chủ sở hữu riêng trong khối spawn; thông báo bằng `Msg2SubWorld`. Cơ chế đồng bộ NPC chung có nhánh gửi tới vùng lân cận, nên bằng chứng phù hợp với lửa nhìn thấy trong vùng bản đồ, không đủ để nói mọi người toàn server đều thấy hoặc chỉ party thấy (`G/script/item/huozhong.lua:75–89`; `S/KNpc.cpp:7663,7701–7718,8044–8052`). Nhìn thấy NPC khác với được nhận EXP; đối tượng/bán kính aura chưa chốt vì E02.

**Thời hạn:** Item đặt 1.800 giây (30 phút); task/GM 3.600 giây (60 phút); nhánh `JIHUO` đặt lại 5.400 giây (90 phút) và đổi sang skill 1706 cùng cấp (`G/script/item/huozhong.lua:79`; `G/script/task/gouhuo.lua:29`; `G/script/item/gm.lua:1096`; `N:44–48`). API ghi `m_GameliveTime`; server giảm mỗi giây và có nhánh xóa NPC hết hạn. Không có căn cứ đổi các số này thành frame hoặc 120 giây (`S/ScriptFuns.cpp:21619–21650`; `S/KNpc.cpp:1442–1463,1483–1487,1533–1552`).

**Thêm củi:** `GOUHUO` đếm item genre 4/detail 408, tính cả stack; cộng `nNum*60` giây. Khi thời gian còn lại tính theo phút đạt ngưỡng cấp kế thì tăng đúng một cấp, trần 50; bảng ngưỡng nằm ở `GetLevelTime`. Nhánh kiểm trần cấp xảy ra sau vòng xóa item; `DelIdItem` nằm ngoài điều kiện đúng loại, nên cả item không đúng loại được giao cũng có thể bị xóa theo thân callback. Đây là rủi ro source, chưa thử thao tác (`N:60–120,122–139`; `S/ScriptFuns.cpp:21727–21733`).

`JIHUO` chỉ được thêm vào menu khi `CHECKGM()==1`; sưởi `XIUFUKAO` chỉ gọi `SetIsDoing(...,0)` rồi báo tin, chưa có phép nhân EXP hay lọc party tại callback đó (`N:18–41,44–53`). `SetNpcGuiShu(...,"50 星")` không được coi là chứng minh gán chủ hoặc nhãn sao: API C++ đang đọc tìm NPC theo tên rồi gán DWID, cho thấy cần đối chiếu phiên bản binary/API trước khi dùng (`G/script/item/huozhong.lua:84`; `S/ScriptFuns.cpp:14715–14725`).

## EXP thực sự được tính thế nào

1. **Bảng skill có sẵn:** `gouhuo.addexp_v` đang bật bảng “trung”, cấp skill 1 là 5.000, cấp 30 là 10.400, cấp 50 là 15.000; hai tham số còn lại đều `18*5=90`. Bảng thấp/cao ở dòng 6/10 bị comment. Đây là lượng cố định theo cấp skill, không phải 0,5% EXP lên cấp của người chơi (`K:4–10`).
2. **Nối effect:** `addexp_v` ghi `m_ExpState.nValue[0..2]`, đặt `nTime=nValue[1]*2`. Tick của người chơi chỉ xử lý khi lượng >0, thời hạn >0; chu kỳ dùng `_gameGlobalSet.NpcInfo.nTimeval*18`, không trực tiếp dùng tham số thứ hai của skill làm chu kỳ (`S/KNpcAttribModify.cpp:3106–3113`; `S/KNpc.cpp:1793–1817`).
3. **Chu kỳ cấu hình:** C++ nạp `[ServerConfig] GouHouTime`, mặc định 90; file `gamesetting_gs001.ini` đặt `10`. Do đó nếu đúng file/source này được dùng, callback theo nhịp 10 giây, không phải mỗi giây. Chưa đo thời gian thực hoặc tình huống nhiều aura (`S/KGameglobalSet.cpp:22,88`; `G/Settings/gamesetting_gs001.ini:502–503`; `S/KNpc.cpp:1803–1817`).
4. **Cấp EXP:** Khi `m_IsDoing==0`, server gọi `goldacition.lua/OnDoAcition`, truyền lượng cố định; Lua gọi `AddOwnExp(nExp)`. API này tới `DirectAddExp`, cộng thẳng EXP cho người nhận. Đường này không gọi hàm chia đội `AddExp` và không nhân 2 hoặc tính theo tổng EXP lên cấp (`S/KNpc.cpp:1814–1817`; `G/script/global/goldacition.lua:7–15`; `S/ScriptFuns.cpp:15908–15918`; `S/KPlayer.cpp:3232–3256`).

**Giới hạn kết luận:** Chưa xác nhận lửa thực sự áp `addexp_v` lên ai, vì chưa nối `1705/1706 → K` trong bảng skill (E02). API `SetNpcSkill` chỉ chuyển tới skill list và `SetAuraSkill`, không chứng minh skill đó tồn tại/hợp lệ (`S/ScriptFuns.cpp:11142–11154`). Không công bố mức EXP/giây thực chạy, hệ số party, phạm vi aura hoặc tổng EXP/lần đốt. Yêu cầu x2 party và +0,5%/giây chưa được chứng minh có trong chuỗi này; cần triển khai/đối chiếu riêng (`K:8`; `S/KPlayer.cpp:3244`; E02).

## Cá lấy ở đâu, nướng cá làm gì

**Đường câu cá được `fishing.lua` gọi:** `taskcontent` Include `tnlteam/cauca/lib_huyhoang.lua`, gọi `Add_DiemCauCa`; `colsetask` chỉ phát tin kết thúc, không xóa điểm câu trong thân hàm (`G/script/task/fishing.lua:1–15`). Cấu hình chọn map 539, loại 4, tối đa 15 dòng tọa độ; loader đọc map_ID/nPosX/nPosY rồi tạo NPC template 225, gán script `quahuyhoang.lua` (`G/script/tnlteam/cauca/lib_huyhoang.lua:42–49,63–89,108–118`). Bảng tọa độ literal thiếu (E03), nên chưa thể xác nhận điểm câu spawn; nhánh `TabFile_Load==0` có in lỗi rồi return (`G/script/tnlteam/cauca/lib_huyhoang.lua:64–68`). Chưa xác định lịch nào gọi `fishing.lua`.

**Điều kiện/thu hoạch theo source:** Cần item `(4,190,0)` cần câu và `(4,191,0)` mồi; đã gia nhập phái (`GetCamp()!=0`), đang chiến đấu, còn sống; loại 4 yêu cầu cấp >=120. Mở tiến độ với tham số `10,5`, callback `FnThuHoach`. Callback kiểm lại trạng thái sống/chiến đấu rồi quay ngẫu nhiên 1..1000, cấp một item `(4,randomFish,0,1,0,0)` nếu trúng (`G/script/tnlteam/cauca/quahuyhoang.lua:27–42,45–100,103–122`). Không suy đơn vị tiến độ khi chưa đọc API.

| Cá/thu hoạch | Detail ID | Trọng số trong bảng |
| --- | ---: | ---: |
| Nàng tiên cá | 198 | 0,001 |
| Cá rồng | 196 | 0,002 |
| Cá sấu | 197 | 0,003 |
| Cá mập | 195 | 0,004 |
| Cá hồng | 194 | 0,070 |
| Mực | 200 | 0,100 |
| Tôm | 201 | 0,120 |
| Cá mè | 193 | 0,150 |
| Cá cờ | 192 | 0,250 |
| Trượt | 0 | 0,300 |

ID từ `G/script/tnlteam/cauca/lib_huyhoang.lua:29–39`; tên/trọng số từ `G/script/tnlteam/cauca/quahuyhoang.lua:12–24`; tổng cá 0,700, trượt 0,300 theo phép cộng bảng, không phải đo tỷ lệ runtime. Khi trúng, callback return trước `ConsumeItem`; khi trượt mới tiêu hao 1 cần và 1 mồi. Đây là bất đối xứng cần thử/sửa riêng, chưa thay source (`G/script/tnlteam/cauca/quahuyhoang.lua:118–135`).

**Nhận cần/nướng:** NPC F có menu nhận cần: kiểm tên item rồi `AddEventItem` nếu chưa có; chưa chứng minh tên này khớp ID cần 190 của nhánh trên (`F:11–40`). `ZHUYU` hiện chỉ `Talk`, dòng mở `Give(...,"ZHUYUA",...)` bị comment. Callback `ZHUYUA` còn thân cũ đếm loại 4/408 rồi xóa item, không có lệnh thưởng thân mật/EXP đồng bạn; không coi đó là cơ chế nướng cá hoạt động (`F:48–91`). Khối tạo nồi cá trong `creatcitynpc.lua` cũng bị comment (`G/script/Pass/creatcitynpc.lua:606–608`).

**Ăn cá khác với nướng:** `item/caoyu.lua` có yêu cầu cấp >=60, cấp ngẫu nhiên 4.000–10.000 EXP bằng `AddOwnExp`; lệnh xóa item bị comment; có nhánh thưởng vật phẩm từ `diaoyu.txt`. Chưa xác minh bảng item nào gán script này cho các cá trong bảng trên. Không có tăng thân mật trong đường đã đọc (`G/script/item/caoyu.lua:3–21,42–54`). `luoica.lua` là nhánh khác, hiện có item thử và comment mở tiến độ/callback thu hoạch, không dùng nó làm bằng chứng câu cá hoàn chỉnh (`G/script/tnlteam/cauca/luoica.lua:43–62,73–96`).

## Có gắn với boss tinh anh xanh nước biển không

**Đánh dấu server:** `KNpcGold` giữ `m_nGoldType` và `m_nIsGolding`; `GetGoldType` trả 0 khi chưa golding, còn setter chấp nhận type 1..16. Nhánh sinh biến thể ngẫu nhiên được đọc chọn type 2..4; không dùng màu chuỗi tên để xác định loại (`S/KNpcGold.cpp:326–350,479–498`). Server gửi type qua `NpcEnchant` và `m_wGoldFlag`; client nhận rồi gọi `SetGoldCurrentType` (`S/KNpc.cpp:7690–7698`; `S/KNpcGold.cpp:451,587`; `C/KProtocolProcess.cpp:2224,5125`).

**Màu trong client:** Khối vẽ tên lấy `GetGoldType`: type 0 trắng khi không aura, 1 xanh lá, 2–4 RGB **100,100,255** (comment “xanh nhạt”; xanh đậm 0,0,160 chỉ là comment), 5–11 RGB 234,189,11, 12–16 RGB 255,62,62. Đây là lựa chọn màu tên trong source, chưa phải ảnh xác minh toàn thân/sprite trên client đang chạy. Không đồng nhất mọi quái xanh với boss có tên hoặc mọi boss với type 2–4 (`C/KNpc.cpp:5334–5353`).

**Liên kết với lửa:** Đường NPC bị người chơi giết gọi `golddeath.lua/OnGoldDeath`, sau đó có thể gọi action script riêng `OnDeath`. Không thấy tạo lửa trong `OnGoldDeath` đã đọc hoặc khối spawn lửa item/GM/task; phần lấy boss type trong callback này đang comment. Vì vậy **chưa có bằng chứng cơ chế tự sinh lửa khi gặp/giết boss xanh**; không kết luận tuyệt đối game không có ở script riêng/PAK (`S/KNpc.cpp:2590–2623`; `G/script/global/golddeath.lua:110–126,418–431`; `G/script/item/huozhong.lua:74–89`; E04).

## Chưa kiểm

- Runtime, bản exe/source khớp nhau, file được nạp từ đĩa hay PAK; khả năng loader xử lý tên Hán tự và tên mojibake (E01–E03).
- Nối skill 1705/1706, bảng skill trong archive/PAK, template NPC 2078 và asset lửa thực tế; chưa khẳng định NPC sinh đúng hình hoặc aura có hiệu lực (`G/script/item/huozhong.lua:71–84`; E02).
- Phạm vi/đối tượng aura, người ngoài đội có nhận EXP, x2 party, cộng dồn nhiều lửa, rời vùng/đăng xuất/qua cấp; chưa thử chống lạm dụng (`S/KNpc.cpp:1801–1817`; E02).
- Lịch runtime thực sự dùng, sự kiện câu cá có bảng tọa độ nơi khác, nguồn mua/nhận mồi 191, mapping item cá và script ăn, cú pháp/Include bắc cầu của Lua (`G/script/task/fishing.lua:1–15`; `G/script/tnlteam/cauca/quahuyhoang.lua:48–59`; E03).
- Toàn bộ death script riêng/boss khác và tài nguyên trong PAK; chưa có luật tự sinh lửa theo type xanh được nối đầy đủ (`S/KNpc.cpp:2620–2623`; E04).
- Thân mật hảo hữu và tốc độ lên cấp theo thân mật: chưa thấy trong callback nướng/ăn đã đọc; không phủ định hệ thống ở nơi khác (`F:48–91`; `G/script/item/caoyu.lua:15–21`).
- Không build/test hoặc kết nối VM/SQL/server theo task; chỉ rà tài liệu và bằng chứng tĩnh.

## Lỗi/giới hạn đã gặp và cách xử lý

| Lỗi/giới hạn | Xử lý và kết quả |
| --- | --- |
| Literal Hán tự không tồn tại | Tìm tên vật lý trong nhánh được giao, đối chiếu CP936/Latin-1, đọc K/N/F; chưa sửa nguồn, còn giới hạn loader E01. |
| `rg : The term 'rg' is not recognized...` | Một lần thử; dùng PowerShell/Node đọc và tìm văn bản trực tiếp; không cài hoặc đổi môi trường. |
| Đọc UTF-8/CP936 sai làm hỏng chữ, đầu ra quá dài bị rút gọn; một biểu thức range PowerShell bị trải phẳng | Thu hẹp đoạn đọc; chốt dòng theo byte LF trong REPL, đọc UTF-8 khi hợp lệ, CP936 cho phần Hán tự, kiểm riêng ASCII. Không dựa vào dòng bị cắt hoặc thông báo tiếng Việt hỏng để kết luận. |
| `The encoded data was not valid for encoding gbk` | Một lần kiểm decoder nghiêm ngặt cho thấy dữ liệu không thuần một encoding. Chuyển đọc theo dòng byte, giữ ASCII, không sửa file. |
| E03 `ENOENT` | Giữ nguyên file nguồn, ghi phụ thuộc thiếu và bước đối chiếu PAK; không tự tạo bảng. |
| D-01 nói `luoica.lua:12` thiếu nháy | Byte gốc có đủ 2 dấu nháy ASCII ở dòng 12 (cả dòng 21/22); `quahuyhoang.lua:13,22,23,107,111` và `lib_huyhoang.lua:55` cũng đủ. CP936 có thể nuốt dấu nháy sau byte tiếng Việt khi hiển thị. Không lặp kết luận lỗi cú pháp này; chưa chạy compiler, không sửa báo cáo D-01 ngoài phạm vi. |

## Kiểm chứng và bàn giao

Đã đọc lại báo cáo, đối chiếu các dẫn nguồn và byte ASCII cần thiết. Có đúng 5 dòng TÓM TẮT đầu file, đủ sinh lửa/hiển thị/thời hạn/EXP/cá/boss và mục Chưa kiểm. Chỉ báo cáo này và phần kết quả task được thay đổi; không có test game đạt để công bố.

Commit sẽ được thực hiện trên nhánh đã xác nhận với tiêu đề `A-08c Khao sat lua trai nuong ca va boss tinh anh`. Không push vì người dùng chỉ yêu cầu commit. SHA hoặc lỗi Git thực tế được ghi tại mục Kết quả của task.
