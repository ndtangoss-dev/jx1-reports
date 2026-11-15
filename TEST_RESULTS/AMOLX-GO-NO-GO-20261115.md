# AMOLX-03 — CÓ THỂ DÙNG LÀM NỀN / CHƯA THỂ DÙNG CHO GAMEPLAY

**Trạng thái: DONE — hoàn tất lượt đánh giá GO/NO-GO, không phải nghiệm thu client.** Ngày: 15/11/2026.

**GO có điều kiện cho phát triển tiếp; NO-GO cho thay client đang dùng hoặc chơi ngay.** Bằng chứng tĩnh cho thấy AMOLX giữ kiến trúc và luồng chuyển Bishop → game server của họ JX1, nên có cơ sở làm nền. Tuy nhiên enum/dispatch và bố cục packet còn bất tương thích. Chưa có bằng chứng build, đăng nhập hay gameplay thành công. Không có căn cứ chọn nhãn KHÔNG NÊN TIẾP TỤC chỉ từ các lỗi hiện có.

Độ tin cậy: **cao** về lệch source-level được nêu dưới đây; **trung bình** về khả năng phát triển tiếp; **chưa xác minh** khả năng chạy với executable server hiện tại. Source server không mặc nhiên đại diện production.

Prompt: `PROMPTS/AMOLX-03-GO-NO-GO-20261115.md` tại commit `0af3cc45d29183fe8c93abbd559798b2047c0490`, blob `bd9dc182b4e36944e166bbaa9b13b9c5d66b038a`. Tiếp tục checkpoint AMOLX-02 đã có trong phiên; không khởi động lại audit toàn diện. Tái sử dụng nội dung đã đọc của prompt AMOLX-02 tại `67f8497e6248c67289f33228012f4ef20db210ae` và `TEST_RESULTS/AMOLX-SESSION-HANDOVER-20261115.md` (blob `239b940edc2be1b44bc1f9a004fdc4c80f8460b8`); không fetch lại lịch sử.

## Nguồn và cách đọc bằng chứng

Các ký hiệu dưới đây nối với đường dẫn đầy đủ; `A/gamecore/KProtocolDef.h:85` nghĩa là đường dẫn gốc A cộng file đó, dòng 85.

| Ký hiệu | Đường dẫn gốc |
|---|---|
| A — AMOLX | `C:\JX1\jx1client-axmol-main\jx1client-axmol-main\Source` |
| C — Cocos canonical được giao | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes` |
| G — GameServer | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver` |
| B — Gateway/Bishop | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gateway` |

C là bản canonical được task chỉ định để so sánh, không khẳng định là APK mới nhất đã phát hành. Header G/B là source-level evidence; không đối chiếu binary đang chạy, không truy cập VM. AMOLX-02 chưa có báo cáo cuối/commit; kết quả trong checkpoint không được gọi là audit đã nghiệm thu.

## Phán quyết theo hạng mục

| Hạng mục | Bằng chứng | Mức độ | Kết luận |
|---|---|---|---|
| Làm nền client mới | A/gameui/KSelPlayer.cpp:996–1061 nhận handoff và tạo logic-login; G/Sources/MultiServer/GameServer/KSOServer.cpp:5044–5082 nhận cùng lệnh và GUID | Kiến trúc tương ứng; chưa đo runtime | CÓ THỂ DÙNG LÀM NỀN, sau khi chuẩn hóa contract |
| Gameplay S2C | `s2c_skillcast` A=95, C/G/B=96; dispatch A/gamecore/KProtocolProcess.cpp:71–72,201–207 theo byte ID | Chặn ngay tương thích gameplay | CHƯA THỂ DÙNG CHO GAMEPLAY với contract source tham chiếu |
| C2S mở rộng | A thiếu 14 symbol so với G; `c2s_rolecheckname_result` 184/192, `c2s_msginfo` 185/193 | Lệnh mở rộng có thể bị hiểu sang lệnh khác | CẦN ĐIỀU CHỈNH; lệnh đi bộ/skill cốt lõi vẫn cùng ID |
| Bishop handoff | `tagNotifyPlayerLogin` A dự kiến 120 B, C 184 B theo pack(1); G/B dùng cùng field/macro với C, giá trị macro server chưa xác minh trong lượt | Chặn/đe dọa chuyển server ngay cả trước gameplay | KHÔNG TƯƠNG THÍCH layout A↔C; không nhận login sẽ chạy được |
| Logic-login | `tagLogicLogin` = byte command + GUID, dự kiến 17 B; command 66 ở A/C/G/B | Một thành phần tương ứng | TƯƠNG THÍCH ở mức định nghĩa đã đọc; chưa chứng minh end-to-end |
| Build Android | Checkpoint handover: yêu cầu Axmol 2.1.5/AX_ROOT chưa sẵn sàng | Chặn build theo bằng chứng trước | CHƯA KIỂM THỬ; không dò lại/cài toolchain trong task này |
| Bảo mật tài khoản | A/gamescene/MainLogin.cpp:127–136 ghi `strPas` vào `accinfo.ini` | Không dùng tài khoản thật trước khi xử lý | CẦN ĐIỀU CHỈNH lưu mật khẩu; không trích dữ liệu người dùng |
| Executable/server hiện tại | Chưa có đối chiếu source↔binary; VM thử nghiệm chưa được xác minh theo checkpoint | Giới hạn nghiệm thu runtime | CHƯA ĐỦ BẰNG CHỨNG; không kết nối thử |

## Enum: vị trí lệch và tác động

Đã trích/tính giá trị enum theo explicit assignment, implicit +1 và alias trong bốn header. Kết quả gồm cả marker/alias, không phải số packet hoạt động: S2C A=181, C/G/B=190; C2S A=153, C/G=167, B=163. Không có nhánh conditional compile bên trong hai enum được đọc. `g_nGlobalProtocolType=31`; các mốc explicit và alias được giữ khi tính.

**Điểm va chạm đầu tiên ở ID 95:** C/G/B định nghĩa `s2c_npcsettmpcamp=95`, A không có symbol đó mà đặt `s2c_skillcast=95`. Symbol chung đầu tiên lệch là `s2c_skillcast`, A=95 (A/gamecore/KProtocolDef.h:85), C=96 (:84), G/B=96 (Headers/KProtocolDef.h:85). Trước đó `s2c_npcchgcamp=94` vẫn khớp (A:84, C:82, G/B:83).

| S2C thiếu trong A | ID C/G/B | Dòng C/gamecore/KProtocolDef.h | Dòng G/B Headers/KProtocolDef.h |
|---|---:|---:|---:|
| `s2c_npcsettmpcamp` | 95 | 83 | 84 |
| `s2c_npcstand` | 145 | 133 | 134 |
| `s2c_gm_synroleaction` | 215 | 204 | 205 |
| `s2c_queryiteminfo` | 216 | 205 | 206 |
| `s2c_returnitemlock` | 217 | 206 | 207 |
| `s2c_findpath_state` | 218 | 207 | 208 |
| `s2c_refitemsync` | 219 | 208 | 209 |
| `s2c_chestpwsync` | 220 | 209 | 210 |
| `s2c_extendchat_new` | 253 | 213 | 215 |

Có **120 symbol chung lệch giá trị**, gồm marker cuối: 49 mục từ C/G/B ID 96–144 bị lùi 1; 69 mục từ 146–214 bị lùi 2. Sáu symbol 215–220 bị thiếu ở cuối vùng thường nên không tạo thêm vùng symbol chung lệch trước mốc relay. Explicit assignment 250/251/252 đưa `s2c_extend/extendchat/extendfriend` về cùng ID; không được kết luận mọi mục phía sau đều lệch 9. A đặt `s2c_extendtong=253`, C/G/B=254; A `s2c_end=254`, C/G/B=255. Nguồn đuôi: A:204–208, C:204–215, G/B:205–217.

**Không chỉ thiếu tính năng:** A/gamecore/KProtocolProcess.cpp:40 khởi tạo bảng về 0, :71 gán handler skill tại ID 95, :72 đặt handler ID 96 thành NULL, :201–207 dispatch trực tiếp theo byte đầu, không dịch ID. Do đó theo các source này, server gửi ID 95 có thể vào nhầm `NetCommandSkill` (hàm :739–765 ép `NPC_SKILL_SYNC`); server gửi skill ID 96 sẽ bị bỏ qua tại dispatcher nếu tới được đây. G/Sources/Core/Src/KNpc.cpp:572,3307,3693 thực sự tạo các lệnh tmpcamp/stand/skill, không chỉ khai enum.

Các ID 215–220 không được đăng ký handler ở A; bảng mặc định NULL nên bị bỏ qua nếu tới dispatcher. C có handler tmpcamp, stand, returnitemlock, findpath, refitemsync, chestpwsync tại C/gamecore/KProtocolProcess.cpp:75,125,197–200; hai mục GM/queryiteminfo vốn NULL (:195–196), vì vậy không mô tả mọi mục thiếu là một handler đã hoạt động. Relay 253 bị A diễn giải thành Tong (:194); Tong 254 bị chặn bởi ngưỡng `>=s2c_end` (:204). Tác động đến chat/bang hội là dự kiến từ source, chưa thử runtime.

Framing cũng có rủi ro: A/gamecore/KProtocol.cpp:14–49 giữ bảng size theo thứ tự, `CoreShell.cpp:1842–1846` tra bằng `ID-65`; A/network/SocketClient.cpp:336–354 dùng size đó để đi tiếp trong buffer hoặc đọc length biến thiên. ID lệch có thể làm bước qua sai packet, ngoài việc bỏ qua/gọi nhầm handler. Không tuyên bố đã tái hiện crash hoặc đọc vượt buffer.

C2S: nhóm nền `login=65` (C dùng tên `c2s_login`, A/G/B dùng `c2s_login_fhgyrinhkmvnsheypo`), logic-login=66, chọn nhân vật=108, walk=75, skill=77 vẫn khớp. A thiếu nhóm C/G ID 184–191 (`lockitem`, `gmcommand`, `findpath_state`, `create_ref_item`, `remove_ref_item`, `apply_mask_lock`, `player_combine_item`, `playercommand`) và 194–198 (`msginfo_all`, `gm_synroleaction`, `gm_synroleaction_result`, `item_synaction`, `item_synaction_result`), cùng `extendchat_new=253`. Vì vậy `rolecheckname_result` A=184/C/G=192 và `msginfo` A=185/C/G=193; `extendtong` A=253/C/G/B=254. Nguồn A:361–370, C:368–391, G:370–394. B thiếu thêm 4 symbol so với G; `rolecheckname_result` B=188, `msginfo` B=189 (B:371–389). Đây là mâu thuẫn giữa hai source server, không được chọn một header bất kỳ làm chuẩn production.

## Hai packet được xác nhận có chọn lọc

Chỉ chọn `tagNotifyPlayerLogin` và `tagLogicLogin`; các struct cha/GUID được đọc để tính layout, không mở rộng audit packet khác. Kích thước/offset là phép tính tĩnh với BYTE/bool=1, UINT=4, unsigned short=2, GUID=16 và pack(1); chưa compile/đo sizeof.

| Packet | AMOLX | Cocos / server source | Kết luận và bằng chứng |
|---|---|---|---|
| `tagNotifyPlayerLogin` (ID 52) | Header 1 + GUID 16 + ba tên 32 + bool 1 + IP 4 + port 2 = 120 B; offset account=49, permit=113, IP=114, port=118 | C dùng tên role 64, account 32, role thứ hai 64: 184 B; account=81, permit=177, IP=178, port=182. G/B field và thứ tự dùng NAME_LENGHT/ACC_LENGTH tương ứng; chưa truy được giá trị macro server trong phạm vi đọc này, giữ công thức `24+2*NAME_LENGHT+ACC_LENGTH` | A/gamecore/KProtocol.h:11,19–24,1413–1418,1486–1515; C/gamecore/GameDataDef.h:152–153, KProtocol.h:11,1557–1586; G Headers/KProtocol.h:1625–1654; B:1613–1642. Layout A↔C lệch đủ để đọc sai cờ/IP/cổng; chưa gán kích thước server thành sự thật runtime |
| `tagLogicLogin` (ID 66) | Header byte + GUID, dự kiến 17 B | C/G/B cùng field dưới pack(1), dự kiến 17 B với GUID Windows chuẩn 16 B | A KProtocol.h:1622–1625; C:1694–1698; G:1770–1774; B:1758–1762. A KSelPlayer.cpp:1055–1061 tạo/gửi; G KSOServer.cpp:5044–5082 kiểm lệnh, ép struct và AttachPlayer bằng GUID |

Bishop dựng/gửi handoff tại B/Sources/MultiServer/Bishop/GameServer.cpp:1007–1081; AMOLX parse trực tiếp, kiểm tên/cờ rồi dùng IP/port tại A/gameui/KSelPlayer.cpp:996–1061. Luồng tương ứng giúp đánh giá có thể làm nền, nhưng không bảo đảm vượt qua layout handoff đang lệch.

## Khả năng khắc phục, giới hạn và bước tiếp theo

Các lỗi có vẻ khắc phục được bằng nhóm thay đổi có giới hạn, **chỉ đề xuất, chưa sửa**: A/gamecore/KProtocolDef.h (ID/reserved/alias), KProtocol.h (field/width/packing), KProtocol.cpp (size/framing), KProtocolProcess.cpp/.h (handler hoặc bỏ qua an toàn), gameui/KSelPlayer.cpp (parse handoff), gamescene/MainLogin.cpp (không lưu mật khẩu rõ); rà network/SocketClient.cpp khi đồng bộ contract. Không chỉ chèn 9 enum rồi xem client tương thích. Không sửa Cocos hoặc server để chiều theo AMOLX trong lượt này.

Build/runtime: tái sử dụng checkpoint thiếu Axmol 2.1.5/AX_ROOT và chưa xác minh VM thử nghiệm; không kiểm lại môi trường. Chưa build APK, cài/chạy LDPlayer 14, đăng nhập, vào world, gameplay hay kết nối server; asset, Android ABI/toolchain và tương ứng binary vẫn chưa được nghiệm thu. Không kết luận chỉ cần build là chạy ngay.

**Bước tiếp theo duy nhất, ưu tiên cao nhất:** chốt contract protocol có phiên bản của bộ client/Bishop/GameServer thử nghiệm được chọn, giải quyết lệch Gateway↔GameServer và xác nhận liên hệ với binary thử nghiệm bằng artifact/báo cáo có sẵn. Đây là điều kiện để giao một patch AMOLX tối thiểu trên bản sao riêng; chưa triển khai patch/build hay truy cập VM trong AMOLX-03.

## Kiểm chứng, lỗi trong lượt và Git

Đã chạy trích xuất số enum bằng Python `-I`, tìm symbol/dòng với `rg`, đọc chọn lọc các vùng source liệt kê trên, kiểm tra Git status trước ghi và diff báo cáo trước công bố. Không chạy test/build/preflight, không kiểm tra hoặc thay đổi model/config Sol Max, không dùng Dispatcher/Scheduler, không thực hiện kết nối game/VM hoặc packet capture. GitHub chỉ dùng để đọc prompt và bàn giao báo cáo được yêu cầu.

Lỗi nhỏ: lần in vùng struct gặp `UnicodeEncodeError` vì stdout Python cp1252; đã đặt stdout UTF-8 chỉ trong tiến trình trích xuất rồi đọc thành công, không sửa cấu hình hệ thống/CLI. Một đường dẫn ứng viên C/engine/KEngineBase.h không tồn tại; định nghĩa cần dùng đã tìm được trực tiếp ở C/gamecore/GameDataDef.h:152–153. Truy vấn macro trong các vùng header/Core/MultiServer server đã chọn không cho kết quả; không mở rộng tìm toàn repo, ghi CHƯA XÁC MINH giá trị macro server. Không có blocker ngăn phán quyết source-level; blocker build/runtime vẫn như bảng trên.

Git local bắt đầu ở `master`, HEAD đã xác nhận `2f7aa0c39be94b86cbd077bf85e24b4855873e27`; có thay đổi BAI_HOC.md và nhiều file untracked từ trước, giữ nguyên. Chỉ tạo `C:\Jx1CocoV3\TEST_RESULTS\AMOLX-GO-NO-GO-20261115.md`. Chỉ báo cáo này được đưa vào commit trên `ndtangoss-dev/jx1-reports`, nhánh `main`, bằng connector; không gom/stage thay đổi khác, không đổi remote/credential. SHA và URL được xác nhận trong bàn giao cuối; không nhúng SHA chứa chính file vào file. Bản local báo cáo có thể vẫn untracked vì repository source local và repository báo cáo GitHub là hai lịch sử riêng.
