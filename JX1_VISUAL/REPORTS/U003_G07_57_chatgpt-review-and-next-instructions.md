# 57 – ChatGPT review G0–G0.6 và chỉ thị xác minh cuối trước khi triển khai U003

Ngày: 2026-11-13  
Cơ sở duyệt: báo cáo U003 51–56 và `BAI_HOC.md` trên `main`, commit `2100d820c7bae0a1faddecbccad611095aaad031`.  
Trạng thái: REVIEW + READ-ONLY TASK. Chưa cho phép tạo Unity project hoặc viết gameplay.

## 1. Phạm vi đã đọc và đối chiếu

Đã đọc toàn văn:
- `JX1_VISUAL/REPORTS/U003_G0_51_khao-sat-hoan-tat.md`
- `JX1_VISUAL/REPORTS/U003_G0_52_bo-sung-xac-minh.md`
- `JX1_VISUAL/REPORTS/U003_G0_53_che-khuat-ui-quai.md`
- `JX1_VISUAL/REPORTS/U003_G0_54_thiet-ke-kien-truc.md`
- `JX1_VISUAL/REPORTS/U003_G05_55_spr-ipotree-direction-skill375.md`
- `JX1_VISUAL/REPORTS/U003_G06_56_hit-damage-combat-verification.md`
- `BAI_HOC.md`

Đây là review tài liệu và mã nguồn đã được Claude trích dẫn; ChatGPT chưa trực tiếp mở source local hoặc chạy game để tái kiểm chứng. Những kết luận dưới đây được phân biệt theo bằng chứng trong báo cáo.

## 2. Kết luận kiến trúc đã được duyệt

### 2.1 Nền tảng và phạm vi
- **DESIGN DECISION – APPROVED:** U003 là Unity prototype độc lập, không tích hợp server trong giai đoạn này.
- **DESIGN DECISION – APPROVED:** giữ nguyên Cocos client và server hiện tại làm baseline; không sửa U001/U002.
- **DESIGN DECISION – APPROVED:** asset JX1 gốc là nguồn ưu tiên; không tự thay asset bằng đồ họa chung nếu chưa được duyệt.
- **DESIGN DECISION – APPROVED:** chọn `ani001` làm quái đầu tiên. Hai hàng NpcS cùng Kind=0, đủ sáu nhóm sprite. Dùng HP kiểm thử 1.000, không coi đây là HP cân bằng cuối.
- **DESIGN DECISION – APPROVED:** port quy tắc `KIpoTree` sang C#; không dùng Y-sort đơn giản làm giải pháp cuối.
- **DESIGN DECISION – APPROVED:** giữ điểm chân runtime `y+6` theo MPS; phép đổi MPS sang màn hình có y-scale 2:1 và z factor 887/1024 theo báo cáo 54.
- **DESIGN DECISION – APPROVED WITH LIMITATION:** lấy `Resources/package.ini` (bản A) làm cơ sở. Chưa xác minh file đang nằm trên điện thoại thật.
- **DESIGN DECISION – APPROVED:** asset extract là dữ liệu dẫn xuất, lưu ngoài Git; không đẩy PAK, APK, binary hoặc dữ liệu thô lên repo báo cáo.

### 2.2 SPR và animation
- **CONFIRMED theo báo cáo 55:** cấu trúc SPR gồm header 32 byte, palette RGB 24-bit, offset table, frame header và RLE alpha/index; đã giải mã 257/257 entry skills.pak và sáu sprite ani001.
- **TESTED theo báo cáo 55:** mẫu 2.500 entry đầu spr.pak không lỗi; còn 12.116 entry chưa quét. Không được diễn đạt là đã kiểm tra toàn bộ spr.pak.
- **CONFIRMED theo báo cáo 55:** TYPE_FRAME nén từng khung riêng chưa được `pak_extract.py` hỗ trợ; đã có script riêng giải được các entry thử. Chưa sửa công cụ chung.
- **CONFIRMED theo báo cáo 55:** interval không có một đơn vị chung: vật thể cảnh dùng ms thật; NPC/nhân vật kéo giãn theo khung logic hành động; missile dùng interval/logic frame theo Missles.
- **UNKNOWN:** blend mode cụ thể và biến thể anchor/REF_SPOT thực tế cho NPC. Anchor (160,192) hiện chỉ là suy luận từ một đường nạp ảnh, không được hard-code như sự thật cho mọi NPC.
- **DESIGN DECISION – APPROVED:** pipeline phải giữ SPR gốc, metadata và ảnh dẫn xuất; không đưa PAK vào APK.

### 2.3 Hướng và che khuất
- **CONFIRMED/TESTED theo báo cáo 55:** mapping logic dir64 sang sprite 8/16 hướng đã được tái dựng và kiểm thử script/ảnh ani001.
- **CONFIRMED theo báo cáo 55:** ani001 là NPC_RES_NORMAL một sprite/hành động, không cần bảng sort bộ phận MainMan.
- **CONFIRMED theo báo cáo 55:** bảng sort MainMan tra theo chỉ số hướng sprite 0-based; LineN khớp số frame tuyệt đối.
- **DESIGN DECISION – APPROVED:** port KIpoTree, gồm SM_* hình học, Tree/Line/Point, Clone cắt nhánh, thứ tự painter và runtime leaf được pluck/reinsert khi tọa độ đổi.
- **UNKNOWN / NOT TESTED:** chưa có ảnh client gốc hoặc reference renderer để chứng minh thứ tự vẽ C# tương đương 100%; các cảnh hai nhánh giao nhau, cùng chân, Clone cần test đối chiếu.
- **DESIGN DECISION – APPROVED:** Above vẫn là lớp riêng ngoài cây; giữ lớp ground/cover/object/above/in-front theo thứ tự báo cáo.

### 2.4 Combat và Skill 375
- **CONFIRMED theo báo cáo 55:** skill 375 tạo 16 missile 181 theo lưới 4×4 (ChildSkillNum=4 được dùng làm hai vòng lặp), với thời điểm xuất hiện lệch nhau theo RANDONORDER. Báo cáo 55 ghi độ trễ dạng `WaitTime(2) + k*5 ± random`, nhưng giá trị nWaitTime đầu vào của lần cast người chơi còn UNKNOWN.
- **CONFIRMED theo báo cáo 55:** missile 181 có MoveKind=0 (Stand), kiểm tra va chạm nhóm; không được tự dựng thành đạn homing bay theo quỹ đạo nếu source không chứng minh. Khi va chạm, skill 387 tạo missile 193 tại vị trí missile 181.
- **CONFIRMED theo báo cáo 55:** vùng kiểm tra của missile 193 là hình vuông 3×3 ô theo DmgRange=2 (theo phân tích code được báo cáo).
- **CONFIRMED theo báo cáo 56:** client không tự trừ HP hoặc phát Hit từ va chạm missile; `ProcessDamage` phía client rỗng. Hit đến từ gói server `s2c_npchurt`.
- **CONFIRMED theo báo cáo 56:** bảng Skills có DoHurt=0 cho skill 375 và 387; theo source server đã đọc, Lôi Động Cửu Thiên không kích hoạt animation Wound/Hit. Death có thể ghi đè Hit; Hit không chồng, không restart/kéo dài khi có đòn mới.
- **HYPOTHESIS theo báo cáo 56:** nguồn sát thương gốc có thể đến từ Attrib 1002 của skill 375/missile 181; cần đọc định nghĩa Attrib và luồng Lua/server đầy đủ để xác minh. Không được kết luận 193 gây sát thương gốc chỉ vì nó là vùng AOE hiển thị.
- **DESIGN DECISION – APPROVED:** U003 giữ 16 missile 181 và các missile 193 tại vị trí va chạm; mỗi vị trí 193 tạo AOE độc lập. Vùng AOE chồng lấn được phép cộng dồn.
- **DESIGN DECISION – APPROVED:** mỗi AOE có hai tick tại +500 ms và +1000 ms kể từ lúc AOE được kích hoạt; mỗi tick gây 20 damage cho từng quái còn sống trong vùng. Một quái nằm trong nhiều vùng tại cùng tick nhận đủ damage từ từng vùng.
- **DESIGN DECISION – APPROVED:** HP quái test = 1.000; hiển thị riêng từng lần damage, không gộp; death khi HP <= 0; respawn theo luật U003 đã định.
- **DESIGN DECISION – RECOMMENDATION:** không phát Hit/Wound cho skill 375 ở cấu hình mặc định, để giữ hành vi gốc theo source; chỉ hiển thị thay đổi HP và damage number. Không bật Hit chỉ vì muốn phản hồi hình ảnh rõ hơn. Nếu sau này muốn Hit, phải là một lựa chọn thiết kế riêng.
- **DESIGN DECISION – APPROVED:** cast duration 1.000 ms; cooldown U003 1.000 ms tính từ lúc bắt đầu cast, kết thúc cùng lúc cast kết thúc. Đây không phải cooldown gốc của skill 375.
- **DESIGN DECISION – APPROVED:** damage number U003 phát một nhãn cho mỗi lần áp dụng damage; tham chiếu font đỏ JX1 `number_16_r`, nhưng cách sống/di chuyển dùng timer thực, không phụ thuộc số lần Paint.

## 3. Các mâu thuẫn/giới hạn cần giữ rõ

1. Báo cáo 51–54 từng ghi 4 missile; báo cáo 55 đã sửa thành 16. Dùng 16 là kết luận mới nhất.
2. Báo cáo 51/52 từng nói chưa tìm thấy projectile; báo cáo 52 đã xác nhận 181/193. Dùng kết luận mới.
3. Báo cáo 52 từng nói chưa thấy cooldown UI; báo cáo 53 xác nhận cơ chế UI cooldown tổng quát. Tuy nhiên TimePerCast=0 ở skill 375 nghĩa là không có cooldown gốc có thời lượng để hiển thị.
4. Báo cáo 54 còn một số thông số timer và combat cũ; báo cáo 56 thay thế bằng luật U003 được chốt trong mục 2.4.
5. 18 Hz của client vẫn chưa xác minh. Không quy đổi frame sang giây như sự thật.
6. Báo cáo 56 chưa chạy game/server và nguồn server có thể không khớp EXE đang chạy. Mọi kết luận server phải giữ giới hạn này.
7. Báo cáo 55 nói 181 MoveKind=Stand. Cần phân biệt logic spawn/activation/collision với hình ảnh sprite; không tự diễn giải là chuyển động vật lý.
8. 16 missile có độ trễ nhiều nhịp, có thể kéo dài tới khoảng 81 logic frame theo công thức đang phân tích. Vì cooldown U003 là 1 giây, nhiều cast có thể chồng các đợt missile/aoe. Mỗi cast phải có ID riêng để không trộn event/timer giữa các lần cast.

## 4. Chỉ thị tiếp theo cho Claude – G0.7 READ-ONLY

Mục tiêu: đóng các UNKNOWN còn ảnh hưởng trực tiếp đến tính đúng đắn của U003. Không tạo project Unity, không viết gameplay.

### A. Hit action và animation ani001
1. Đọc `npc动作表.txt` và đường nạp action name; xác minh index 7/cdo_hurt thực tế ánh xạ tới action nào và sprite `ani001_bat.spr` có đúng là Wound.
2. Xác minh các trạng thái Hit/Death của ani001, hướng và thời lượng logic. Không cần nghiên cứu đòn đánh thường ngoài phạm vi.
3. Ghi rõ U003 mặc định không phát Hit cho skill 375; không tự thêm hiệu ứng Hit.

### B. Attrib 1002 và sát thương gốc
1. Truy định nghĩa Attrib 1002 từ enum/bảng tới nơi server áp dụng damage.
2. Truy luồng skill 375 → missile 181 → collision event 387 → missile 193 → ReceiveDamage/CalcDamage.
3. Xác định chính xác missile nào áp dụng damage gốc, skill nào cung cấp Attrib, 193 có damage riêng hay chỉ tạo vùng/effect.
4. Đọc `kunlun.lua` đầy đủ phần `leidong_jiutian` và callback liên quan; chỉ đọc.
5. Phân biệt source server với EXE server đang chạy; không thử kết nối hay thao tác VM.

### C. Thời gian missile và cast
1. Truy ngược đối số `nWaitTime` đầu vào của lần cast từ người chơi; không dừng ở công thức RANDONORDER.
2. Xác minh 60% action event và thời điểm CastZone bắt đầu.
3. Xác định ý nghĩa MoveKind=Stand đối với missile 181: vị trí spawn, sprite hiển thị, collision query, lifetime; không tự gọi nó là projectile bay.
4. Xác định khoảng trễ thực tế của 16 vị trí theo đơn vị logic frame; giữ nguyên giá trị frame, không quy đổi giây nếu chưa xác minh client Hz.

### D. SPR/asset và map – chỉ những gì trực tiếp cần cho prototype
1. Xác định cách NPC thực sự gọi hàm render ảnh và cờ blend/anchor (REF_SPOT) áp dụng cho ani001.
2. Nếu không thể xác minh bằng source, đánh dấu UNKNOWN và ghi rõ cần ảnh chụp client gốc; không đoán.
3. Kiểm tra map 45 có đủ Region_C.dat cho vùng dự kiến và tọa độ buildin là local hay absolute. Không cần quét toàn bộ bản đồ.
4. Không cần quét toàn bộ 12.116 entry spr.pak còn lại; chỉ quét các PAK/entry có liên quan trực tiếp đến asset U003 trong manifest.

### E. Pak extractor
Không sửa `pak_extract.py` trong G0.7. Đường TYPE_FRAME đã được chứng minh bằng script riêng; trước tiên chỉ lập test specification cho việc bổ sung sau này. Chỉ sửa công cụ khi có chỉ thị triển khai riêng.

### F. Ranh giới an toàn
- Chỉ đọc source, bảng dữ liệu và asset hiện có.
- Không tạo Unity project, không viết code gameplay, không build APK.
- Không cài package/model.
- Không sửa PAK, source gốc, server, DB, VM hoặc cấu hình.
- Không dừng/restart Goddess hay EXE.
- Không đụng U001/U002.
- Không push bất kỳ file asset thô, PAK, APK, credential, IP riêng hoặc dữ liệu nhạy cảm nào.
- Không force push, reset, clean hoặc ghi đè thay đổi không thuộc U003.

### G. Báo cáo và bàn giao
Tạo:
`JX1_VISUAL/REPORTS/U003_G07_58_g07-hit-attrib-cast-anchor-map-verification.md`

Báo cáo phải:
- Nêu file/hàm/dòng code cụ thể.
- Gắn nhãn CONFIRMED / TESTED / HYPOTHESIS / DESIGN DECISION / UNKNOWN.
- Liệt kê mọi kết luận cũ bị thay thế, không xóa lịch sử.
- Có bảng sự kiện timeline của cast và 16 missile (đơn vị logic frame).
- Nêu rõ phần nào là nguồn gốc JX1 và phần nào là luật U003.
- Đưa ra blocker còn lại trước khi tạo Unity project.
- Cập nhật mục U003 trong BAI_HOC.md nếu có bài học mới, không viết lại các mục lịch sử không liên quan.

Commit và push báo cáo cùng BAI_HOC.md lên `ndtangoss-dev/jx1-reports` / `main` theo quy trình an toàn đã dùng ở commit 2100d82. Trước khi push: kiểm tra branch, status, diff và chỉ đưa đúng file U003 liên quan; tuyệt đối không stage/push các script sửa dở, patches, VM tools, credential hoặc báo cáo chưa duyệt khác. Không force push. Sau push cung cấp SHA, danh sách file và link GitHub.

Sau khi bàn giao, DỪNG. Chưa tạo Unity project hoặc build APK. Chờ ChatGPT đọc toàn văn và duyệt.

## 5. Điều kiện để ChatGPT duyệt bắt đầu Unity
- Không còn UNKNOWN gây sai asset, sai thời điểm cast, sai vùng damage hoặc sai cách render ani001; hoặc UNKNOWN được chấp nhận bằng văn bản.
- Luật Combat U003 trong mục 2.4 được giữ nguyên.
- Các test tối thiểu T-SPR, T-DIR, T-IPOT có kế hoạch kiểm thử rõ; các điểm chưa có ảnh gốc phải được ghi là hạn chế, không tuyên bố tương đương đã kiểm chứng.
- Sau G0.7 mới lập kế hoạch triển khai từng giai đoạn. Không tự động chuyển sang code.
