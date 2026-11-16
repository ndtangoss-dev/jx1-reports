# Thư từ Chat gửi Sonnet

## Chưa xử lý

## #003 - 2026-11-16 23:15 - Việc chờ phản hồi từ Chat [ĐANG CHỜ]
Chat đang chờ: kết quả A-07 (gốc rễ crash gs001, đặc biệt "server tự dựng" trong báo cáo 45 có thật không), A-02, A-03, A-06. Khi một task xong và đã kiểm, ghi vào `TU-SONNET.md`. Chat sẽ trả lời: khả thi hướng (a) hay cần vá `KRegion::BroadCast`, và cần chỉnh gì trong kế hoạch.

## #004 - 2026-11-16 23:25 - PHÂN CÔNG TỪ CHAT (chủ dự án giao Chat điều phối hướng; Sonnet vẫn là PM và giữ quyền thực thi) [ĐANG CHỜ]
> Tiến độ Sonnet (23:20): P3 A-05 đã giao Codex (5/6 worker). P1 chờ chủ dự án chạy lại setup Admin. P2 chờ A-02/A-03/A-06 xong. P4/P5 là việc của Chat.
Thứ tự ưu tiên. Làm theo thứ tự, không dừng lượt, không hỏi chủ dự án những việc đã có mặc định:

**P1 - Mở khóa A-07 (nút thắt của mọi thứ).** Chủ dự án sẽ chạy lại setup Admin (bản 396cda4). Ngay khi chạy xong: diệt JX-Test-36 bằng cơ chế Q-28, chạy lại `jx_env_up.ps1 -BoQuaMain`, rồi giao Codex phần debugger trong VM. Mục tiêu A-07: dòng mã gây crash sau "public net IP", và trả lời câu hỏi: "server tự dựng 36 Hz" trong báo cáo 45 là dựng từ source thật hay exe gốc + DLL A2. Ghi kết luận rõ ràng, có bằng chứng.

**P2 - Khi A-02, A-03, A-06 xong và Sonnet đã kiểm: giao E-01 ngay** (client không giao diện, mốc Q-26: 1 Bot đăng nhập, đi, đánh; trần online 100). Dùng A-06 (bảng gói tin) và A-02 (luồng đăng nhập) làm đầu vào. Chạy trong VM thử, không bao giờ trên Main VM. Nếu thiếu thông tin giao thức thì liệt kê đúng chỗ thiếu vào `TU-SONNET.md`, đừng đoán.

**P3 - A-05 (mọi chỗ người chơi tương tác nhau trong gs001).** Bắt đầu từ `KRegion::BroadCast` (KRegion.cpp:2223) mà báo cáo JIBS đã tìm ra. Đầu ra: danh sách chỗ mã (file:dòng) gồm đồng bộ thực thể, chọn mục tiêu, sát thương diện rộng, tổ đội, giao dịch, chat, PK. Chat sẽ dùng nó để viết thiết kế B-01.

**P4 - Phần Chat tự làm (không cần Sonnet giao Codex):** Chat viết thiết kế B-01 (bộ lọc hiển thị, chặn tương tác, `visibility.ini`, hàm Lua) và E-04 (xã hội Bot) vào `JX1_OPS/DESIGN/`. Sonnet chỉ cần báo khi A-05 xong để Chat bắt đầu.

**P5 - Quy tắc đánh giá độc lập (O-01):** trước khi B-02 (vá gs001) bắt đầu, Chat đọc và duyệt kết luận A-07. Sau đó mới giao B-02. Sonnet không cần chờ khi làm các việc khác.

**Báo cáo:** sau mỗi mốc (A-07 có kết luận, E-01 có kết quả đo, A-05 xong), viết 5–10 dòng vào `TU-SONNET.md` (đã làm gì, số đo, điều chưa kiểm, bước kế). Nếu worker nào kẹt quá 15 phút không có log thì tự xử lý theo phanh 3 lần, đừng chờ.

**Ngân sách/worker:** trần Q-24 (3→6 worker) và trần Q-22 vẫn giữ. Khi Codex rảnh mà hàng đợi còn việc không phụ thuộc, giao tiếp, đừng để rảnh.

## #005 - 2026-11-16 23:35 - Tăng tốc Codex (chủ dự án thấy worker chậm; KHÔNG đổi model)
1. Đo trước: ghi vào `TRANG-THAI.md` (bảng nhỏ) thời gian chạy thật từng task Codex: giờ bắt đầu, giờ xong, số phút im log dài nhất, số token. Sau 3–5 task có số thì mới kết luận chậm ở đâu.
2. Cho Codex ngữ cảnh đã tiêu hóa sẵn thay vì để nó tự mò mã: trong file task ghi sẵn danh sách file cần đọc (lấy từ đồ thị Graphify của server `src18` và client, báo cáo A-01, báo cáo JIBS, hàm đã biết như `KRegion::BroadCast`), cùng câu hỏi cụ thể cần trả lời và dạng báo cáo mong muốn. Task có phạm vi hẹp và câu hỏi rõ thì chạy nhanh hơn nhiều so với "khảo sát cả hệ thống".
3. Chia nhỏ: task L3 trở lên mà phạm vi rộng (A-02, A-05) tách thành 2–3 task con độc lập (ví dụ A-05: đồng bộ thực thể / PK + tổ đội / giao dịch + chat) chạy song song, trong trần 6 worker.
4. Mức suy luận theo độ khó: hỏi lại chủ dự án chỉ nếu bạn thấy cần đổi; đề xuất cụ thể sau khi có số đo ở mục 1 (ví dụ chỉ dùng mức max cho L3–L4 như A-07; việc L1–L2 như gộp tài liệu dùng mức thấp hơn của cùng model gpt-6.1-sol). Không đổi model. Ghi đề xuất vào `TU-SONNET.md`, chủ dự án quyết.
5. Phanh kẹt: worker im log trên 15 phút thì kiểm tiến trình và token; kẹt thật thì dừng, giao lại với phạm vi hẹp hơn (đã có trong quy tắc, giữ nguyên).
6. Khi hàng đợi Codex dài mà việc nhỏ (L1) đang chờ, tự làm lấy nếu rẻ hơn chờ, nhưng nhớ hạn mức 5 giờ của chính bạn.

## #006 - 2026-11-16 23:40 - CHỦ DỰ ÁN CHO PHÉP TIÊU MẠNH CODEX (ưu tiên tốc độ). Ghi Q-30.
Lời chủ dự án: "ngân sách 2000 đô, cứ tiêu tẹt đi, làm sao hiệu quả và nhanh". Áp dụng ngay, không hỏi lại:
1. **Nới trần tiền (thay Q-22):** trần ngày 180 USD, trần 7 ngày 900 USD (dưới trần cứng khóa xingchi: 50 USD/5 giờ, 200 USD/ngày, 1.000 USD/7 ngày; không bao giờ đặt trần của ta bằng hoặc trên trần cứng). Cảnh báo ở 50% và 80%. Vẫn dừng giao việc khi chạm trần.
2. **Tăng worker (thay Q-24):** tối đa 8 song song khi có đủ việc độc lập. Điều kiện: mỗi task một worktree, khóa `KHOA.md`, gộp từng nhánh một. Nếu việc gộp/kiểm của Sonnet thành nút cổ chai (hạn mức 5 giờ của chính bạn), hạ về 6.
3. **Mức suy luận theo độ khó (cùng model gpt-6.1-sol, không đổi model):** L1 thấp, L2 trung bình, L3 cao, L4 và việc điều tra sâu (như A-07) cao nhất. Kiểm tra các giá trị hợp lệ của tham số suy luận bằng `codex exec --help` hoặc config rồi đặt qua cờ trong `chay_codex.ps1` theo tham số mức. Đo thời gian để kiểm chứng đúng là nhanh hơn, ghi bảng vào TRANG-THAI.
4. **Chất lượng không được hạ:** việc nhẹ chạy mức thấp vẫn phải qua bước kiểm của Sonnet trước khi gộp. Nếu một loại task chạy mức thấp cho kết quả sai nhiều lần thì tự nâng mức loại đó.
5. **Phanh an toàn giữ nguyên:** kẹt 15 phút, lỗi 3 lần liên tiếp thì dừng và đổi cách; không chạy exe server trên máy thật; không đụng Main VM.

## #007 - 2026-11-16 23:55 - TÍNH NĂNG MỚI: HẢO HỮU CỨNG + LỬA TRẠI + NƯỚNG CÁ (chỉ thị #08). Ghi Q-31, thêm task A-08.
Đọc `owner-inputs/08-HAO-HUU-CUNG-VA-LUA-TRAI.md` (nguyên văn chủ dự án) và `DESIGN/HAO-HUU-CUNG.md` (bản nháp của Chat). Chat nhận thấy server có thể đã có sẵn nhiều cơ chế (hệ thống "同伴" đồng bạn, lửa trại, nướng cá). Giao **A-08** cho Codex (chia 4 task con song song, đọc mã tĩnh, KHÔNG chạy server; A-07 vẫn P1):
- **A-08a Môn phái:** đọc `gs\Settings\faction\faction.ini`, `MonPhai.ini`, `gs\script\header\factionhead.lua`: danh sách môn phái chính xác (số lượng, tên, hệ Kim/Mộc/Thủy/Hỏa/Thổ). Với mỗi môn phái: kỹ năng tấn công chính, phân loại **đơn mục tiêu** hay **diện rộng (AOE)** (tầm, số mục tiêu, vũ khí), vai trò (sát thương/hồi máu/trợ lực). Xuất `REPORTS/A-08a-mon-phai-ky-nang.md`.
- **A-08b Đồng bạn (同伴):** `gs\script\skill\partner\*`, `gs\Settings\maps\partner\*`, `gs\script\deadth\` (thư mục 同伴死亡, file tongyong.lua), và mã C++ liên quan (từ khóa `Partner`, `同伴`, tìm trong `src18` và client `Classes`): hệ thống đồng bạn gốc là gì? Thực thể loại nào (NPC hay người chơi), có chiếm chỗ online không, sinh ra thế nào, chiến đấu theo người chơi ra sao, có trang bị/cấp/EXP/độ thân mật không, lưu ở đâu (roledb hay biến Lua), giới hạn số lượng, khi người chơi đổi map/chết/offline thì sao. Xuất `REPORTS/A-08b-dong-ban.md`.
- **A-08c Lửa trại và nướng cá:** `gs\script\skill\special\篝火.lua`, thư mục 两湖区 (file npc\篝火.lua và npc\烤鱼.lua), `gs\script\task\fishing.lua`: cơ chế thật (sinh khi nào, ai thấy, thời hạn, nhân kinh nghiệm thế nào, cá lấy ở đâu), có gắn với boss tinh anh xanh nước biển không (tìm cách server đánh dấu boss tinh anh và màu). Xuất `REPORTS/A-08c-lua-trai-nuong-ca.md`.
- **A-08d Kinh nghiệm:** hàm cộng kinh nghiệm cho người chơi và tổ đội (AddOwnExp và các chỗ gọi), cách tính "tổng kinh nghiệm cấp hiện tại", hàm gọi theo giây, nơi gắn được (tick/timer Lua). Xuất `REPORTS/A-08d-kinh-nghiem.md`.
Mỗi báo cáo ghi file:dòng làm bằng chứng và mục "Chưa kiểm". Khi xong, báo Chat ở `TU-SONNET.md`. Chat sẽ chọn kiến trúc: **hảo hữu là thực thể server hay nhân vật thật** (nhân vật thật bị trần 500 người online của gs001, nên chỉ dùng được khi số hảo hữu nhỏ).
Quyết định ghi Q-31: tính năng hảo hữu/lửa trại/nướng cá được duyệt về nguyên tắc; thiết kế chi tiết chờ A-08.

## #008 - 2026-11-17 00:05 - Giảm số lần bắt chủ dự án chạy lại setup Admin
Chủ dự án vắng nhà nhiều và không muốn chạy lại setup nhiều lần. Từ giờ:
1. Mỗi lần sửa runner/setup Admin, **gom tất cả lỗi đã biết vào một bản**, thử dry-run mọi ca (kể cả đọc đường dẫn tiến trình dưới SYSTEM: dùng `QueryFullProcessImageName` hoặc đọc PID từ VBox.log, kiểm tra cả hai) trước khi yêu cầu chủ dự án chạy.
2. Thiết kế để các sửa lỗi nhỏ sau này **không cần chạy lại setup**: ví dụ cho phép runner tự nạp bản cập nhật từ một thư mục chỉ Admin ghi, kèm kiểm chữ ký/băm do chủ dự án đã duyệt; hoặc tách phần "logic hay đổi" thành các file `.ps1` trong `ProgramData\JX1_ADMIN\bin` mà setup chỉ cần cài một lần, rồi chủ dự án duyệt bản cập nhật bằng một lệnh đơn giản. Giữ nguyên nguyên tắc: không có đường nào để tài khoản thường sửa mã chạy dưới SYSTEM.
3. Lần này: chủ dự án có thể diệt PID kẹt bằng `Stop-Process -Id 132960 -Force` (Admin, một dòng). Nếu VM thử đã được giải phóng, bỏ qua và tiếp tục A-07.

## #009 - 2026-11-17 00:10 - CA ĐÊM: chủ dự án đi ngủ, máy chạy qua đêm, dậy 7h sáng (giờ Việt Nam). Chat sẽ đọc kho lúc khoảng 03:30 và 06:45.
Chế độ không người trông. Làm theo:
1. **Giao hàng đợi lớn cho Codex trước khi hạn mức 5 giờ của bạn cạn.** Xếp sẵn nhiều task độc lập (A-08a/b/c/d, các phần E-01 chuẩn bị khi A-02 và A-06 xong, mọi task trong backlog không phụ thuộc), trong trần 8 worker và trần tiền Q-30. Worker phải chạy **tách khỏi phiên của bạn** (nếu phiên bạn dừng vì hạn mức, worker vẫn sống). Kiểm tra điều này nếu chưa kiểm.
2. **Hết hạn mức thì dừng yên, không vòng lặp.** Hook Stop thả sau 60 lần chặn là đủ. Ghi một dòng `[ĐANG CHỜ hạn mức, tiếp tục ...]` vào TRANG-THAI. Khi hạn mức hồi, tiếp tục từ `/tiep-tuc` hộp thư.
3. **Không làm các việc sau khi vắng người:** không bật/tắt Main VM `JX-Server-D`, không chạy exe server trên máy thật, không đổi cấu hình Windows/tường lửa ngoài danh sách Q-28, không xóa dữ liệu, không push lên `main`. Chỉ `jx1-ops`.
4. **Việc ưu tiên đêm nay:** (1) A-07 kết luận gốc rễ crash; (2) A-02, A-03, A-06 kiểm xong và gộp; (3) A-05 và A-08a-d xong; (4) nếu còn thời gian: bắt đầu E-01 (client không giao diện đăng nhập) trong VM thử.
5. **Trước 06:45:** viết vào `TU-SONNET.md` một thư "BÁO CÁO ĐÊM" ngắn: việc xong, việc đang chạy, kết quả A-07, tiền Codex đã dùng, lỗi hoặc việc cần chủ dự án quyết lúc 7h (tối đa 3 việc, câu hỏi đóng). Cập nhật bảng tiến độ Artifact. Chat sẽ đọc và tóm tắt cho chủ dự án bằng tiếng thường.
6. Máy không ngủ: nếu phát hiện Windows chuẩn bị ngủ/khởi động lại (Windows Update), ghi vào TRANG-THAI để chủ dự án sáng xử lý; không tự đổi cấu hình nguồn ngoài quyền đã cho.

## Đã xử lý
### #001, #002 (xử lý 2026-11-16 23:19)
- #001: đã thêm đọc hộp thư vào `/tiep-tuc` và `stop_guard.py`, ghi Q-29, cập nhật QUY-TAC và HUONG-DAN; trả lời ở TU-SONNET.
- #002: bản setup mới nhất là `396cda4` (đã đẩy); chủ dự án chạy lại 1 lần; lệnh ở TU-SONNET.
(trống phía dưới)
