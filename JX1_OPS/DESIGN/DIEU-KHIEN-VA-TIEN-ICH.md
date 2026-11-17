# Điều khiển và tiện ích — tổng hợp H-09

## TOM TAT 5 DONG

1. PARTIAL về độ phủ: tổng hợp 21 báo cáo hiện có thuộc H-01..H-15 và I-01..I-08; thiếu I-06, H-09 là tài liệu tổng hợp này.
2. Coco có joystick, 3 ô vật phẩm nhanh, 1 skill chính và tối đa 8 skill phụ theo source; mapping phím PC chưa được chứng minh.
3. Cài đặt, auto, cường hóa, nhiệm vụ và tương tác NPC có đường xử lý được báo cáo; chưa xác nhận tích hợp trên binary đang chạy.
4. Ưu tiên kiểm tính đúng của chỉ số ô, lưu cấu hình, ACT/MOVE và phản hồi HP trước khi thay FPS/tick hoặc mở rộng auto.
5. Chỉ tổng hợp tài liệu trong JX1_OPS; không sửa source, chạy build/test/game, dùng VM hay đọc dữ liệu đăng nhập.

## Phạm vi và cách dùng bằng chứng

Ngày tổng hợp: 17/11/2026. Đầu vào là báo cáo local, không phải source hay cấu hình đang chạy. Mọi kết luận “theo source” dưới đây là **trích lại kết quả khảo sát của báo cáo nguồn**, chưa được H-09 kiểm chứng độc lập. Đề xuất là đầu việc cho task được duyệt sau, không phải thay đổi đã thực hiện.

Ký pháp `REPORTS/tên-file.md:dòng` là vị trí trong JX1_OPS tại thời điểm tổng hợp. Link mở báo cáo tương ứng; số dòng ghi ngay cạnh để tra chính xác. Các ký hiệu C/O/S/G bên trong từng báo cáo có gốc khác nhau; phải dùng bảng nguồn riêng của báo cáo, không ghép số dòng giữa các cây hoặc suy source khớp APK/DLL.

## Độ phủ đầu vào

| Báo cáo | Nội dung được đưa vào thiết kế | Bằng chứng báo cáo |
|---|---|---|
| H-01 | Ngũ hành, dòng ẩn, sai khác UI/server | [H-01](../REPORTS/H-01-ngu-hanh.md), `REPORTS/H-01-ngu-hanh.md:2` |
| H-02 | Dòng chỉ số và tooltip | [H-02](../REPORTS/H-02-magic-attrib.md), `REPORTS/H-02-magic-attrib.md:2` |
| H-03 | Cường hóa, phí và khác biệt công thức | [H-03](../REPORTS/H-03-cuong-hoa.md), `REPORTS/H-03-cuong-hoa.md:4` |
| H-04 | Mốc hiệu ứng và giới hạn bản build tham chiếu | [H-04](../REPORTS/H-04-hieu-ung-vu-khi.md), `REPORTS/H-04-hieu-ung-vu-khi.md:3` |
| H-05 | Mở/đặt/xác nhận/hủy cường hóa | [H-05](../REPORTS/H-05-ui-cuong-hoa.md), `REPORTS/H-05-ui-cuong-hoa.md:49` |
| H-06 | Ô ấn, kích hoạt và dữ liệu nâng bậc chưa đủ | [H-06](../REPORTS/H-06-he-thong-an.md), `REPORTS/H-06-he-thong-an.md:2` |
| H-07 | Trang sức, mặt nạ, phi phong và dữ liệu lệch loader | [H-07](../REPORTS/H-07-trang-suc-mat-na-phi-phong.md), `REPORTS/H-07-trang-suc-mat-na-phi-phong.md:3` |
| H-08 | Xếp hạng tiền và ý nghĩa FortuneRank | [H-08](../REPORTS/H-08-tai-phu.md), `REPORTS/H-08-tai-phu.md:2` |
| H-09 | Chính task tổng hợp, không dùng báo cáo kết quả làm bằng chứng vòng | `JX1_OPS/TASKS/H-09.md:12` |
| H-10 | Thanh nút, nơi lưu và phím PC chưa xác minh | [H-10](../REPORTS/H-10-phim-tat-thanh-nut.md), `REPORTS/H-10-phim-tat-thanh-nut.md:25` |
| H-11 | Nút hệ thống, 12 khóa local, lỗi cài đặt | [H-11](../REPORTS/H-11-nut-he-thong-cai-dat.md), `REPORTS/H-11-nut-he-thong-cai-dat.md:44` |
| H-12 | Auto client, điều kiện bật và giới hạn tiếp tế | [H-12](../REPORTS/H-12-tu-dong-chien-dau.md), `REPORTS/H-12-tu-dong-chien-dau.md:53` |
| H-13 | Tick, làn lệnh, flush và HP/số nổi | [H-13](../REPORTS/H-13-tick-do-tre-don.md), `REPORTS/H-13-tick-do-tre-don.md:43` |
| H-14 | Mất sét theo gate góc, mask, che khuất | [H-14](../REPORTS/H-14-mat-khung-hieu-ung.md), `REPORTS/H-14-mat-khung-hieu-ung.md:82` |
| H-15 | Joystick/FPS, logic missile và rủi ro collision | [H-15](../REPORTS/H-15-dan-xuyen-quai-fps.md), `REPORTS/H-15-dan-xuyen-quai-fps.md:21` |
| I-01 | Điểm nhân vật, giới hạn cấp/dữ liệu EXP | [I-01](../REPORTS/I-01-cac-loai-diem.md), `REPORTS/I-01-cac-loai-diem.md:2` |
| I-02 | Shop, giá hiệu lực và giới hạn từng UI | [I-02](../REPORTS/I-02-vat-pham-ban.md), `REPORTS/I-02-vat-pham-ban.md:86` |
| I-03 | Mục tiêu quái, template/spawn và phạm vi thống kê | [I-03](../REPORTS/I-03-khao-sat-quai-vat.md), `REPORTS/I-03-khao-sat-quai-vat.md:2` |
| I-04 | Map, chỉ đường và điều kiện chiến đấu | [I-04](../REPORTS/I-04-khao-sat-map.md), `REPORTS/I-04-khao-sat-map.md:2` |
| I-05 | NPC chức năng, script và ánh xạ vị trí còn thiếu | [I-05](../REPORTS/I-05-npc-chuc-nang.md), `REPORTS/I-05-npc-chuc-nang.md:40` |
| I-06 | Không tìm thấy báo cáo mang mã I-06 trong REPORTS; chưa thể tổng hợp | Kiểm kê tên file local, không suy nội dung từ tài liệu khác |
| I-07 | Ví tiền, phạm vi thanh toán và trạng thái nguồn BLOCKED | [I-07](../REPORTS/I-07-cac-loai-tien-te.md), `REPORTS/I-07-cac-loai-tien-te.md:3` |
| I-08 | Panel/trace nhiệm vụ, cache và giới hạn lưu task | [I-08](../REPORTS/I-08-he-thong-nhiem-vu.md), `REPORTS/I-08-he-thong-nhiem-vu.md:109` |

## Phím, joystick và thanh nút

| Thao tác | Hành vi có bằng chứng báo cáo | Điểm yếu / điều kiện thiết kế |
|---|---|---|
| Di chuyển joystick | KHRocker gọi updateMovement theo callback render; đủ distance 5 thì gọi Goto, trừ attack/magic; guard gửi move 5 tick trong đường gốc đã comment | Cần đo lệnh/s và thứ tự MOVE/ACT khi vừa chạy vừa đánh; không suy missile cũng chạy theo render. `REPORTS/H-15-dan-xuyen-quai-fps.md:33` |
| Bấm skill chính | MainAttack; gán skill trái hiện hành có c2s_skillsync | Có phản hồi động tác local, chưa đồng nghĩa server đã nhận/thực thi/trúng. `REPORTS/H-10-phim-tat-thanh-nut.md:61`, `REPORTS/H-13-tick-do-tre-don.md:45` |
| Gán/bấm skill phụ | Tối đa 8; skill thường đặt skill phải rồi UseSkill, aura qua SetAuraSkill | Không coi 8 nút là 8 skill luôn hoạt động đồng thời; kiểm cooldown/aura và thêm nút thứ 9. `REPORTS/H-10-phim-tat-thanh-nut.md:34`, `:62`, `:107` |
| Dùng vật phẩm nhanh | UI VN/core/server cùng giới hạn 3; tham chiếu theo hash tên, dùng item ở vị trí thật | Dấu hiệu idx-1 ở ô đầu; clear UI dùng hằng 9 khác refresh 3, chưa phải lỗi runtime đã tái hiện. `REPORTS/H-10-phim-tat-thanh-nut.md:29`, `:45`, `:47`, `:87` |
| Phím số/F1–F12/chuột PC | Chưa có mapping gameplay được chứng minh từ UI PC | Không tự gán 1–3/F1–F8 từ số ô. Thư mục “gốc” chứa Cocos/VN, không chứng minh là client PC độc lập. `REPORTS/H-10-phim-tat-thanh-nut.md:21`, `:92` |

**Ba lớp lưu phải được trình bày riêng:** ô thuốc có đường lưu server qua TDBItemData.iparamb5; bố cục skill chính/phụ ghi accinfo.ini local theo nhân vật; cài đặt chung dùng jx50ai/Setting.ini với section cố định. Sync skill trái chỉ xác nhận trạng thái hiện hành, không chứng minh server lưu toàn bộ bố cục. Chưa xác nhận phục hồi sau đăng nhập/chuyển thiết bị bằng runtime. Nguồn: `REPORTS/H-10-phim-tat-thanh-nut.md:49`, `:63`, `:70`; `REPORTS/H-11-nut-he-thong-cai-dat.md:80`.

**Phản hồi chiến đấu:** chuỗi cần phân biệt là input → gửi/nhận → ACT chờ/bị thay/hết TTL → bắt đầu skill → frame phát chiêu → missile/collision → HP server → sync → số nổi. Skillcast không phải ACK trúng; số nổi hiện lấy chênh HP nên nhiều hit có thể gộp. Bản Coco được H-13 khảo sát có guard MOVE/pending skill khác bản gốc mà H-15 khảo sát; không áp kết luận spam move của gốc thành lỗi đã xác nhận ở mọi bản. Nguồn: `REPORTS/H-13-tick-do-tre-don.md:48`, `:49`, `:54`, `:76`.

## Tiện ích và yêu cầu tích hợp

| Nhóm | Có gì theo báo cáo | Yêu cầu cho thiết kế / phần còn thiếu |
|---|---|---|
| Cài đặt hệ thống | Bánh răng mở KuiOptions; 3 slider hiện, 8 checkbox hiện, 4 nút hành động trong game. Lưu ngay theo event; Đóng lại không rollback | Phân biệt lưu cài đặt, reset skill local, đăng xuất và yêu cầu rời mạng ủy thác. Reset có KickOutGame/cảnh báo, chưa chứng minh logout ngay. `REPORTS/H-11-nut-he-thong-cai-dat.md:31`, `:35`, `:38`, `:68`, `:110` |
| Ẩn/đồng nhất hình ảnh | Có cờ ẩn NPC/player/tên/kỹ năng/cảnh, cùng player và cùng skill | IsHidePlayer chặn vẽ local, có thể che đồng đội/bot; không suy giảm gói/slot server. IsHideMis gán nhầm biến và IsShowSameSkill chưa có consumer được chứng minh. `REPORTS/H-11-nut-he-thong-cai-dat.md:54`, `:57`, `:60`, `:89`, `:101` |
| Tự động chiến đấu | Chọn mục tiêu theo quan hệ/range, đi/đánh, hỗ trợ, nhặt, thuốc, phù; có chuỗi VLMap tiếp tế | Auto phụ thuộc client update, tài nguyên/profile và sync cờ. Không có bằng chứng vòng chiến đấu server khi tắt client; full auto quay bãi chưa được chứng minh. `REPORTS/H-12-tu-dong-chien-dau.md:55`, `:65`, `:87`, `:156`, `:160` |
| Cường hóa | Nút VN gửi yêu cầu script; server trả UI give; đặt item khóa ID; xác nhận kind=3 tối đa 24 ID; hủy kind=0 | Cần trạng thái chờ/kết quả, chống xác nhận lặp và kiểm unlock khi timeout/mất kết nối/túi đầy. Không coi đóng UI là thành công. `REPORTS/H-05-ui-cuong-hoa.md:53`, `:58`, `:60`, `:63`, `:101` |
| Tooltip/trang bị | H-01/02 mô tả ngũ hành, dòng ẩn và MagicDesc_mobile; H-06/07 có ấn/mặt nạ/phi phong và ô đeo | Đối chiếu client/server trước preview chỉ số; không suy “có ô” thành nâng bậc/nguồn nhận hoàn chỉnh. Dữ liệu Mask thiếu header và liên kết kích hoạt thứ ba lệch. `REPORTS/H-01-ngu-hanh.md:4`, `REPORTS/H-02-magic-attrib.md:4`, `REPORTS/H-06-he-thong-an.md:4`, `REPORTS/H-07-trang-suc-mat-na-phi-phong.md:5` |
| Hiệu ứng cường hóa | H-04 ghi mốc +6/+12/+15, chỉ self; H-14 phân tích Draw VN, gate góc/mask/occlusion | Mốc là kết quả tài liệu/source, chưa xác minh APK đang dùng. Không tăng tia/alpha để che mất khung; phân biệt không gửi draw và bị phủ sau draw. `REPORTS/H-04-hieu-ung-vu-khi.md:3`, `:5`; `REPORTS/H-14-mat-khung-hieu-ung.md:71`, `:84`, `:88`, `:182` |
| Điểm và xếp hạng | EXP/kỹ năng/tiềm năng/danh vọng có lưu và sync; nhánh DB H-08 xếp tiền túi+rương, Xu riêng | Không gắn FortuneRank phi phong thành điểm tài phú trang bị. EXP có 200 mục nhưng MAX_LEVEL=500; chưa dùng làm trần cấp hiệu lực. `REPORTS/I-01-cac-loai-diem.md:2`, `:3`; `REPORTS/H-08-tai-phu.md:2`, `:4` |
| Shop và ví tiền | Có các đường shop, tiền túi/rương/XU và điểm; DynamicShop số lượng 1, UI thường 150, SuperShop 30 | Hiển thị đúng ví dùng để trả: tổng túi+rương không chứng minh Pay dùng được cả hai. Giá trống không phải miễn phí; hạn UI không phải hạn server. Bạc khóa riêng chưa được xác minh. `REPORTS/I-02-vat-pham-ban.md:90`, `:91`, `:109`; `REPORTS/I-07-cac-loai-tien-te.md:31`, `:32`, `:39` |
| Map/NPC/chỉ đường | MapTraffic có 342 cạnh có hướng; script có chuyển map, cường hóa, kho/shop; quest trace có map/x/y | Graph client không chứng minh tuyến đi được; City/Country không đủ xác định an toàn PK. Thiếu ánh xạ NPC thường trú tới ID/map/tọa độ/script. `REPORTS/I-04-khao-sat-map.md:3`, `:4`; `REPORTS/I-05-npc-chuc-nang.md:45`, `:48`; `REPORTS/I-08-he-thong-nhiem-vu.md:118` |
| Nhiệm vụ | Có panel/trace, cache task và NPC/menu/script; task ID 0..9999, mảng UI 20 | GetTask có thể trả cache cũ; SET handler đặt 0, không phải API nhận/thưởng quest. Bot chưa có pipeline nhận/trả và correlation/ACK. `REPORTS/I-08-he-thong-nhiem-vu.md:1`, `:115`, `:126`, `:133`, `:148` |

Quái làm mục tiêu auto phải gắn **ID, quan hệ, cấp/spawn và map hợp lệ**, không chỉ nhãn Kind=0 hoặc tổng số template. I-03 ghi 2.435 template, 1.412 hàng Kind=0 và 94.098 bản ghi spawn trên 195 map; đây không phải số quái đang sống hay số mục tiêu được phép săn. Nguồn: `REPORTS/I-03-khao-sat-quai-vat.md:2`, `:3`; bộ lọc quan hệ auto: `REPORTS/H-12-tu-dong-chien-dau.md:55`.

## Điểm yếu và khác biệt giữa các báo cáo

| Điểm cần giữ riêng | Kết luận được phép | Cách xử lý tiếp |
|---|---|---|
| Script cường hóa | H-05 chưa có Lua trong cây source đã đọc; I-05 có script trong gói GS, H-03 có luật nguyên liệu/phí | Bổ sung tham chiếu chéo, không đổi thành tuyên bố runtime hoàn chỉnh. Chưa chứng minh script đóng gói khớp binary. `REPORTS/H-05-ui-cuong-hoa.md:86`; `REPORTS/I-05-npc-chuc-nang.md:43`; `REPORTS/H-03-cuong-hoa.md:5` |
| Số liệu shop | I-02 đếm 160 dòng shop, 2.644 ô dương, 474 goods ID; I-05 ghi 105 dòng, 2.649 ô không rỗng, 479 mã duy nhất | Tập đếm/tiêu chí khác; chưa đủ bằng chứng quy về một catalog hay kết luận một bên sai. Chốt file/phiên bản/định nghĩa ô trước khi thiết kế hạn mua. `REPORTS/I-02-vat-pham-ban.md:3`; `REPORTS/I-05-npc-chuc-nang.md:33` |
| Spawn map | I-04 còn thiếu spawn PAK; I-03 đã có thống kê hai PAK và còn 38 ID không khớp .wor | Dùng I-03 bổ sung độ phủ tĩnh, không khẳng định đã có ánh xạ NPC chức năng hoặc runtime đầy đủ. `REPORTS/I-04-khao-sat-map.md:1`; `REPORTS/I-03-khao-sat-quai-vat.md:3`, `:6` |
| Tick/FPS | H-13/15 cùng có 18 logic đầy đủ, 36 outer xen nửa bước; UI render không tự đổi tick server | Không gọi 36 là combat 36 Hz; không suy FPS cao chắc gây xuyên đạn. H-15 chưa đối chiếu H-13/14 trong checkout của nó, H-09 chỉ nối bằng chứng tài liệu. `REPORTS/H-13-tick-do-tre-don.md:31`; `REPORTS/H-15-dan-xuyen-quai-fps.md:38`, `:56`, `:63` |
| Cường hóa/ngoại hình | H-03 có trần gói cũ +5, tài liệu Coco +15, EnChance khác EnChanceRong; H-04 có các mốc hiệu ứng | Không đồng nhất trần nghiệp vụ với mốc hình ảnh, không coi bảng thử +30 là trần thật. `REPORTS/H-03-cuong-hoa.md:4`, `:6`, `:7`; `REPORTS/H-04-hieu-ung-vu-khi.md:3` |
| Trạng thái I-07 | Nguồn tự ghi BLOCKED do điều kiện backlog, đồng thời có kết quả đọc tĩnh | Chỉ dùng kết quả có giới hạn và dẫn nguồn; không sửa trạng thái nguồn hoặc coi phần thiếu đã xong. `REPORTS/I-07-cac-loai-tien-te.md:3`, `:7` |

## MUC SO THONG SO

Không thay giá trị nào. “Cẩn thận” là đánh giá cho task sau; mọi sửa code/cấu hình cần phạm vi duyệt riêng. Các số dưới đây là số liệu báo cáo/source, không phải đo runtime H-09.

| Thông số | Giá trị / đơn vị | Tác động và mức đổi | Bằng chứng báo cáo |
|---|---|---|---|
| Ô vật phẩm nhanh VN | 3 ô; index hợp lệ [0,3) | Đổi phải khớp UI/core/server/save; cẩn thận | `REPORTS/H-10-phim-tat-thanh-nut.md:29`, `:45` |
| Skill chính/phụ | 1 / tối đa 8 nút | Local layout khác skill hiện hành; cẩn thận | `REPORTS/H-10-phim-tat-thanh-nut.md:33`, `:34`, `:63` |
| Tùy chọn local | 12 khóa; 3 slider + 8 checkbox hiện | 4 khóa AAAA, 8 BBBB; không đồng bộ server được chứng minh | `REPORTS/H-11-nut-he-thong-cai-dat.md:67`, `:68`, `:80` |
| LimitFPS | UI 30–90, fallback/reset 60; callback clamp 30–120 FPS | Miền không thống nhất; sửa schema/validation trước mở rộng | `REPORTS/H-11-nut-he-thong-cai-dat.md:53`, `:108`; `REPORTS/H-15-dan-xuyen-quai-fps.md:100` |
| Nhịp client logic | 18 tick/s; tối đa 128 lượt bù/frame render | Không đổi riêng để khớp render; cần đối chiếu hitch/resume | `REPORTS/H-15-dan-xuyen-quai-fps.md:26` |
| Server outer/full | Chọn 18 hoặc 36 vòng/s; full logic vẫn đơn vị 18 Hz ở nhánh khảo sát | Không tăng toàn bộ tick nếu chưa quy đổi dữ liệu | `REPORTS/H-13-tick-do-tre-don.md:27`, `:31`, `:33` |
| Nhận gói client gốc | custom_update 0,1 giây/lượt theo source | Pha cập nhật có thể khác thời điểm damage; chưa đo độ trễ | `REPORTS/H-15-dan-xuyen-quai-fps.md:34` |
| Cast action | 60% khung logic, so sánh bằng sau chia nguyên | Không bỏ wait/thay trigger đồng loạt; cẩn thận | `REPORTS/H-13-tick-do-tre-don.md:50`, `:96` |
| Joystick distance | 5 đơn vị UI | Ngưỡng gọi Goto, không phải 5 tick hoặc giới hạn gói/s | `REPORTS/H-15-dan-xuyen-quai-fps.md:108` |
| ACT bảo vệ ở Coco | Guard 3 lượt cập nhật | Chưa quy thành ms; cần đo cùng command lane server | `REPORTS/H-13-tick-do-tre-don.md:76` |
| Auto HP/MP default file | Life1/Mana1=50, Life2/Mana2=20 (% theo nhánh xử lý); interval 1000 ms cấu hình | Counter quy đổi *60/1000, phụ thuộc update; chưa là chu kỳ thực | `REPORTS/H-12-tu-dong-chien-dau.md:99`, `:100`, `:108` |
| Auto tầm đánh/nhặt | RadiusEdit=800, FightNearEdit=75; PickUpRange=400 đơn vị cấu hình | Không quy pixel/mét; fallback nhặt 800 khác file | `REPORTS/H-12-tu-dong-chien-dau.md:103`, `:104`, `:106` |
| Auto tiếp tế | AIFullAutoCK=0 trong default | Không bật mặc định khi chưa xác nhận vòng quay bãi | `REPORTS/H-12-tu-dong-chien-dau.md:102`, `:160` |
| Give cường hóa | Tối đa 24 ID, xác nhận kind=3 | Kiểm biên/khóa/túi đầy; không suy 24 ô nhìn thấy | `REPORTS/H-05-ui-cuong-hoa.md:47`, `:60`, `:101` |
| Phí/nguyên liệu cường hóa gói khảo sát | 200.000 tiền; vật phẩm loại 403/404/405 | Chưa xác nhận cấu hình đang chạy; không đưa thành giá hiệu lực trên UI | `REPORTS/H-03-cuong-hoa.md:5` |
| Mốc glow/sét | +6 / +12 / +15 | Mốc tài liệu; chỉ self, cần đối chiếu build | `REPORTS/H-04-hieu-ung-vu-khi.md:3` |
| Gate góc sét | >0,25 rad; khoảng gọi <400.000 µs; tối đa 10 lượt skip | 400 ms không phải timeout toàn khoảng mất; cẩn thận | `REPORTS/H-14-mat-khung-hieu-ung.md:84`, `:86` |
| Missile speed cap | 32 đơn vị speed/tick ở nhánh đã đọc | Không đổi theo render dt; chưa biết kích thước mục tiêu thực | `REPORTS/H-15-dan-xuyen-quai-fps.md:28`, `:40`, `:55` |
| Shop quantity UI | DynamicShop 1; KuiShop 150; SuperShop 30 | Ba đường UI, không phải hạn server toàn cục | `REPORTS/I-02-vat-pham-ban.md:91` |
| Level/EXP | MAX_LEVEL=500; bảng EXP 200 mục; lên cấp +5 tiềm năng/+1 kỹ năng | Lệch độ phủ; không suy trần runtime | `REPORTS/I-01-cac-loai-diem.md:3`, `:4` |
| Task state | ID 0..9999; count save BYTE cần biên 255/256; UI 20 mục | Không coi là 10.000 quest hay 20 quest tối đa; cẩn thận | `REPORTS/I-08-he-thong-nhiem-vu.md:1`, `:2`, `:115` |

## DE XUAT TOI UU

Thứ tự dưới đây là đề xuất tổng hợp theo rủi ro tính đúng và khả năng đo, chưa phải backlog triển khai đã duyệt. Không có số tiết kiệm CPU/ms/FPS được đo trong H-09.

| Ưu tiên | Đề xuất cụ thể | Lợi ích kỳ vọng / rủi ro | Cách xác nhận trong task sau |
|---|---|---|---|
| P0 | Chốt binary/source/data của từng phép đối chiếu; bổ sung I-06 và giải thích tập đếm shop | Tránh thiết kế theo dữ liệu khác phiên bản; chưa có lợi ích hiệu năng định lượng | Ghi danh tính build/dataset đã lọc; đối chiếu phạm vi/định nghĩa đếm. Nguồn: bảng khác biệt ở trên |
| P1 | Rà chỉ số ô thuốc, cap give 24, unlock và trạng thái chờ/kết quả cường hóa | Giảm nguy cơ thao tác sai/mất trạng thái; chưa có lỗi mất đồ runtime được chứng minh | Ô 1/2/3, index ngoài miền trên harness được duyệt; xác nhận/hủy/lặp/mất kết nối/túi đầy. `REPORTS/H-10-phim-tat-thanh-nut.md:104`; `REPORTS/H-05-ui-cuong-hoa.md:101` |
| P1 | Thống nhất handler ẩn kỹ năng với consumer; chuẩn hóa miền/default/reset FPS và âm lượng, báo lỗi lưu | Cài đặt phản ánh đúng tác dụng, tránh reset gây hiểu nhầm; đổi UI phải kiểm file cũ | Đối chiếu nhãn/biến/file sau toggle/reopen/reset, audio độc lập, lỗi ghi trên bản thử. `REPORTS/H-11-nut-he-thong-cai-dat.md:76`, `:107`, `:108`, `:111` |
| P1 | Đo ACT/MOVE và chuỗi damage→HP→paint; xác minh sentinel flush trước tối ưu nhịp | Phân biệt lệnh bị loại với trễ hiển thị; đổi flush có thể tăng write/fan-out | Metadata recv/consume/expire/overwrite, damage/enqueue/flush/receive/paint, p95 và CPU/bytes/s; không thu raw packet/log đăng nhập. `REPORTS/H-13-tick-do-tre-don.md:56`, `:64`, `:126`, `:130` |
| P2 | Định thời auto bằng thời gian đơn điệu, kiểm tài nguyên/profile, guard HP/MP và điều kiện tiếp tế | Hạn chế lệch nhịp theo FPS và vòng tiếp tế chưa sẵn sàng; thay timing có thể đổi gameplay | Cùng skill/thuốc tại 30/60 FPS, nền/resume/reconnect; kiểm inventory và ACK, không suy gửi lệnh là thành công. `REPORTS/H-12-tu-dong-chien-dau.md:108`, `:157`, `:158`, `:160` |
| P2 | Sửa gate sét theo action/hướng đáng tin, kiểm coverage/occlusion, invalidation mask, khôi phục RGBA | Giảm khoảng mất do skip/che/cache và sai màu; nguy cơ tia sai neo/vẽ xuyên thân | Log lý do reject và accepted/candidate, ảnh cùng frame/hướng, ROI ngoài kiếm, draw count và p95. `REPORTS/H-14-mat-khung-hieu-ung.md:176` |
| P2 | Giữ fixed-step logic; nếu chứng minh tunneling thì thiết kế collision quét đoạn theo hitbox đúng đơn vị | Bắt mục tiêu giữa hai bước; cần bảo toàn xuyên nhiều mục tiêu và damage lặp có chủ đích | Ma trận FPS 20/30/45/60/90/120, ≥30 phát/mức, cùng skill/data; đo HP/hit/event và quỹ đạo. Đây là kế hoạch, chưa chạy. `REPORTS/H-15-dan-xuyen-quai-fps.md:67`, `:68`, `:69`, `:75`, `:76` |
| P2 | Tích hợp quest/shop/NPC qua trạng thái server mới, ghi rõ ví và trạng thái pending | Tránh cache cũ, nhầm tổng tiền, nhầm death thành kill hoặc nhận thưởng lặp | Nhận→làm→trả, reconnect, túi đầy, mua theo từng ví, state mới/ACK; chốt NPC ID/map/script trước tự dẫn đường. `REPORTS/I-07-cac-loai-tien-te.md:32`; `REPORTS/I-08-he-thong-nhiem-vu.md:133`, `:148`, `:150` |

## Giới hạn và bàn giao

H-09 chỉ đối chiếu báo cáo, không xác nhận source độc lập, ABI/opcode wire, asset/PAK/APK/DLL, hiệu lực cấu hình, tỷ lệ thành công, vị trí NPC runtime hoặc lợi ích tối ưu. Không dùng kết quả test được nguồn nhắc lại làm test mới của H-09. Các ca kiểm thử ở trên chưa chạy; mọi VM/exe/network/runtime phải có task và phạm vi phê duyệt riêng.

Đầu vào chưa đủ: I-06; mapping PC; danh tính binary/data đang dùng; ánh xạ NPC thường trú; thống nhất tập đếm shop. Phần tổng hợp 21 báo cáo hiện có đã hoàn thành. Báo cáo thực hiện và trạng thái Git nằm tại [REPORTS/H-09.md](../REPORTS/H-09.md).
