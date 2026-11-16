# KẾ HOẠCH TỔNG THỂ JX1 – BẢN 1 (OPUS)

| | |
|---|---|
| Ngày | 2026-11-16 |
| Người lập | Claude Opus (nghiên cứu, kiến trúc, kế hoạch) |
| Người điều hành sau phê duyệt | Claude Sonnet (Project Manager) |
| Trạng thái | **CHỜ CHỦ DỰ ÁN PHÊ DUYỆT.** Chưa triển khai gì |
| Nơi lưu | Repository `ndtangoss-dev/jx1-reports`, nhánh `jx1-ops`, thư mục `JX1_OPS/` |
| Căn cứ | `owner-inputs/05` và `06` (mới nhất, ưu tiên cao nhất); bộ Fable v0.3 (`FABLE_HANDOVER_v0.3/`); toàn bộ báo cáo trên nhánh `main` |

Nhãn độ tin cậy dùng trong tài liệu này (thống nhất cho cả dự án, thay ba bộ nhãn cũ):
**[XÁC MINH]** có log, số đo, build hoặc test thật · **[NGUỒN]** đọc trong source, chưa chạy · **[BÁO CÁO]** lấy từ báo cáo cũ, chưa kiểm lại · **[GIẢ THUYẾT]** · **[CHƯA BIẾT]**.

---

## PHẦN 0. TÓM TẮT CHO CHỦ DỰ ÁN

1. **Hướng mới:** dùng lại client Cocos V3 và server JX1 gốc, làm chủ toàn bộ source, rồi chuyển server sang mô hình: người chơi thật không thấy nhau ở bản đồ thường, Bot dùng chung cho cả thế giới, một số hoạt động được cấu hình cho thấy nhau và có giới hạn số người.
2. **Khả thi cao.** Server dựng từ source đã chạy thật trên VM thử ở cả 18 Hz và 36 Hz, người chơi vào game, đi lại, đánh quái được [XÁC MINH, báo cáo 45]. Nghĩa là sửa server ở mức source là làm được. Phần chưa biết là chính xác đoạn code nào quyết định "ai thấy ai"; đó là việc nghiên cứu đầu tiên.
3. **Cách chuyển đổi đề xuất:** thêm một bộ lọc hiển thị phía server, kèm chặn tương tác giữa người chơi thật, điều khiển bằng một file cấu hình hoạt động. Bot là tài khoản được đánh dấu "bot" nên ai cũng thấy. Vì Bot là thực thể thật của server, việc A giết Bot thì B thấy Bot chết là tự nhiên đúng.
4. **Tổ chức mới:** bỏ ChatGPT, 8 phòng ban, Dispatcher. Sonnet là PM duy nhất, có toàn quyền trên máy phát triển và VM thử. Sonnet tự khởi chạy Codex và các agent con, không cần anh bấm từng task. Opus chỉ được gọi cho việc khó.
5. **Không gián đoạn:** mọi trạng thái nằm trên nhánh `jx1-ops`, đẩy lên GitHub thường xuyên. Anh gõ `/ket-thuc-ca` trước khi tắt máy và `/tiep-tuc` khi quay lại. Đổi tài khoản hay đổi model cũng chỉ cần `/tiep-tuc`.
6. **Cần anh quyết 1 việc bắt buộc:** cho phép đưa source (chỉ mã nguồn, đã lọc dữ liệu tài khoản) lên một repository GitHub **riêng tư**. Các quyết định còn lại đều có phương án mặc định; anh không trả lời thì Sonnet làm theo mặc định (Phần 11).

---

## PHẦN 1. KIẾN TRÚC VÀ HIỆN TRẠNG HỆ THỐNG JX1

### 1.1. Thành phần

| Thành phần | Mô tả | Trạng thái |
|---|---|---|
| Client Cocos V3 | Cocos2d-x, C++. Bản có đủ các bản vá nằm ở `D:\Android\b\Client\Classes` (P46/P47), không phải cây gốc `C:\Jx1CocoV3\Folder\Client2912…` | Đang chơi được, APK P46 mới nhất [XÁC MINH] |
| Server gameplay | `gs001` + `CoreServer.dll`, `Engine.dll`, `LuaLibDll.dll`. Source ≈ 425 nghìn dòng C/C++ ở `SwordOnline/.../gameserver`. Bản đã sửa (A2, fix36, 36 Hz) ở `D:\JX-build\src18` | Tự dựng được (MSVC v143, x64), chạy 18/36 Hz trên VM thử [XÁC MINH] |
| Gateway, dịch vụ | `Sword3PaySys` (5002), `Goddess` (5001), `S3Relay` (5003–5005, 7776), `Bishop` (56722) | Chạy được bằng exe gốc [XÁC MINH]; source ≈ 279 nghìn dòng có sẵn [NGUỒN] |
| Script | Lua trong `gs\script\…` (ví dụ Tống Kim `missions\宋金战场pk战\`) | Có, đã đọc một phần [NGUỒN] |
| Dữ liệu tài khoản | SQL Server 2019 Express, DB `account` (`Account_Info`, `Account_Habitus`) | [XÁC MINH] |
| Dữ liệu nhân vật | `roledb` do `Goddess` quản lý; server liên kết thư viện `libdb181` | Định dạng Berkeley DB [GIẢ THUYẾT, suy từ thư viện liên kết] |
| Tài nguyên | 44 file `.pak` ≈ 3,3 GB, phục vụ qua CDN cổng 8080 | [XÁC MINH] |
| Đường mạng | Điện thoại → Tailscale → forwarder trên máy thật (56722, 51189) → VM | [XÁC MINH] |
| VM | `JX-Server-D` (Main VM, không đụng), `JX-Server` (archive), `JX-Test-36` (VM thử) | [BÁO CÁO] |
| Client thứ hai | AMOLX (bản port Axmol): đang thử, chưa vào được gameplay | [XÁC MINH, AMOLX-09] |

### 1.2. Những gì đã làm được
- Client: Fix31 (nội suy), Fix33 (mất sát thương), Fix34 (đạn), Fix35 (crash vùng), Fix36 (giật bản đồ), P46 (răng cưa camera, giật ra chiêu), P47 (nhấp nháy đối tượng).
- Server: A2 Command Lane, 7 struct gói khớp client 2912, sửa crash x64, nhánh 36 Hz.
- Đo tài nguyên server (Phase 48): 1 người chơi thêm khoảng 0,2–0,3 ms mỗi nhịp và khoảng 35–40 KB/s băng thông gửi [XÁC MINH].
- Khảo sát Bot: giao thức đăng nhập, mã hóa gói, lệnh đi, đánh, tổ đội, chat đã đọc được trong source [NGUỒN, báo cáo 16].

### 1.3. Điểm yếu cần biết
- Source không ở trong Git có quản lý phiên bản; các bản đã sửa nằm rải trên máy (`D:\Android\b`, `D:\JX-build\src18`, `C:\JX\Bisect\T4`). Mất máy là mất việc.
- Source server và exe gốc chưa chứng minh là cùng phiên bản [CHƯA BIẾT]; đã dùng bản tự dựng nên rủi ro này giảm.
- Kho dự án có dữ liệu nhạy cảm (file SQL tài khoản, dump, khóa trong `paklist.ini`) [BÁO CÁO]: phải lọc trước khi đưa lên GitHub.
- Ba bộ quy tắc cũ mâu thuẫn nhau; bộ này thay thế tất cả (Phần 9).

---

## PHẦN 2. BÁO CÁO KHẢ THI CHUYỂN ĐỔI SERVER

### 2.1. Mục tiêu
Mặc định người chơi thật không thấy nhau ở bản đồ thường; Bot là thực thể chung ai cũng thấy; hoạt động được cấu hình thì cho thấy nhau, có giới hạn số người.

### 2.2. Căn cứ khả thi
| Điều kiện | Có chưa |
|---|---|
| Sửa và dựng lại `gs001` từ source | Có [XÁC MINH] |
| Chạy bản sửa trên môi trường cô lập | Có, VM thử `JX-Test-36` [XÁC MINH] |
| Script Lua điều khiển hoạt động, tạo NPC, đặt phe | Có `AddNpc`, `SetNpcCurCamp`… [NGUỒN] |
| Thế giới chia vùng (`KRegion`, `KSubWorld`), đồng bộ thực thể theo vùng | Có cấu trúc [NGUỒN]; đường đi cụ thể của gói đồng bộ người chơi chưa đọc [CHƯA BIẾT] |
| Sửa client nếu cần | Có, đã làm nhiều đợt [XÁC MINH] |

**Kết luận: KHẢ THI**, với mức tin cậy trung bình–cao. Rủi ro chính không nằm ở việc "có sửa được không" mà ở **số chỗ trong code giả định người chơi thấy nhau** (tổ đội, giao dịch, PK, kỹ năng diện rộng, bảng xếp hạng, script đếm người xung quanh). Nghiên cứu A-05 sẽ liệt kê đủ trước khi sửa.

### 2.3. Các phương án đã xét

| Phương án | Cách làm | Đánh giá |
|---|---|---|
| **1. Lọc hiển thị phía server** (đề xuất) | Khi server gửi danh sách thực thể quanh một người chơi, bỏ qua người chơi thật khác trừ khi cả hai cùng nhóm hoạt động được phép. Đồng thời chặn mọi tương tác giữa hai người không thấy nhau. | Chắc chắn, không gian lận được bằng client sửa. Cần nghiên cứu kỹ. Mức L4. |
| 2. Lọc ở forwarder | Forwarder trên máy thật giải mã gói (mã hóa XOR đã biết) và bỏ gói về người chơi khác | Không cần sửa server, làm thử nhanh; nhưng không chặn được sát thương diện rộng hay tương tác. Chỉ dùng để xem trước cảm giác chơi nếu cần. |
| 3. Ẩn ở client | Client không vẽ người chơi khác | Nhanh nhất nhưng dễ bị vượt; không chặn tương tác. Loại làm giải pháp chính. |
| 4. Mỗi người một bản đồ riêng | Sao bản đồ cho từng người | **Loại**: phá yêu cầu Bot dùng chung. |

### 2.4. Phần cấu hình được, phải sửa source, phải xây thêm

| Loại | Nội dung |
|---|---|
| Cấu hình (sau khi xây xong) | Danh sách hoạt động cho thấy nhau; bản đồ thuộc hoạt động; số người thật tối đa; phe; đội; bật/tắt từng hoạt động |
| Sửa source C++ | Bộ lọc gửi thực thể; kiểm tra quyền tương tác (mời đội, giao dịch, PK, chọn mục tiêu, sát thương diện rộng, chat mật); cờ `is_bot` trên tài khoản hoặc nhân vật; hàm Lua mới |
| Sửa Lua | Script hoạt động gọi hàm vào/ra nhóm hiển thị, kiểm tra số người |
| Xây thêm | File cấu hình và trình đọc; công cụ quản trị (Phần 6); bộ test tự động hai người chơi |
| Sửa client (có thể) | Ẩn phần giao diện liệt kê người chơi khác (danh sách quanh đây, bảng xếp hạng) nếu server vẫn gửi dữ liệu đó |

### 2.5. Thử nghiệm chứng minh (giai đoạn B)
1. Hai tài khoản thật trên VM thử, cùng bản đồ: **không** thấy nhau, không tổ đội, giao dịch, đánh nhau được.
2. Cùng hai tài khoản đó vào một hoạt động được bật: thấy nhau, tương tác được.
3. Vượt số người tối đa: người thứ N+1 bị từ chối.
4. Một Bot (tài khoản cờ bot) đứng cạnh cả hai: cả hai cùng thấy; A đánh chết thì B thấy chết.
5. Đo tick và băng thông trước và sau khi bật bộ lọc.

---

## PHẦN 3. KẾ HOẠCH QUẢN LÝ ACCOUNT (giai đoạn C)

- **Làm rõ:** luồng đăng nhập client → `Bishop` → `PaySys`/`Goddess` → `gs001`; bảng nào trong SQL giữ gì; `roledb` lưu nhân vật thế nào, sao lưu ra sao.
- **Công cụ quản trị tối thiểu (dòng lệnh trước, giao diện sau):** tạo, khóa, mở khóa tài khoản; đặt lại mật khẩu; xem danh sách nhân vật; xem ai đang online; đánh dấu tài khoản bot; sao lưu và khôi phục dữ liệu nhân vật.
- **Tài khoản bot:** tạo hàng loạt theo mẫu, có cờ `is_bot`, mật khẩu do máy sinh và lưu trong Windows Credential Manager (cơ chế dự án đang dùng), không ghi vào Git.
- **Bảo mật cơ bản:** client AMOLX lưu mật khẩu dạng rõ trong `accinfo.ini` [NGUỒN]; client Cocos cần kiểm tra tương tự trước khi có người chơi thật.
- **Web Admin / Mobile Admin:** làm sau khi công cụ dòng lệnh ổn định; một trang web nội bộ chạy trên máy thật, xem được từ điện thoại qua Tailscale là đủ cho cả hai nhu cầu.

---

## PHẦN 4. DANH MỤC HOẠT ĐỘNG VÀ TRẠNG THÁI THỰC TẾ (giai đoạn D)

Chưa có danh mục; đây là việc phải làm. Mỗi hoạt động được xếp vào một trong năm trạng thái của chỉ thị: **đang hoạt động · có trong source chưa kích hoạt · có code nhưng lỗi hoặc chưa xong · chỉ có giao diện/dữ liệu · chưa xây**.

Mỗi dòng ghi: tên, script Lua, NPC kích hoạt, lịch, điều kiện vào, phần thưởng, bản đồ, có người thật tham gia không, Bot có thể tham gia thế nào, trạng thái, bằng chứng.

Danh sách khởi đầu từ quảng cáo source (cần xác minh từng mục): Dã Tẩu, Boss Sát Thủ 2x–9x, Tiểu/Đại Hoàng Kim, Nhiệm Vụ Hoàng Kim, Câu cá, Vận tiêu, Tống Kim Sơ/Trung/Cao, Hạt Huy Hoàng, Thuyền Phong Lăng Độ, Vượt Ải, Liên Đấu, Hoa Đăng. Đã biết: Tống Kim có script tạo lính hai phe [NGUỒN]; 33 file Lua gọi `PARTNER_*` nhưng server không đăng ký hàm đó [NGUỒN].

Cách làm: Sonnet giao một worker quét `gs\script\` và bảng cấu hình, rồi thử trên VM thử bằng GM; mỗi hoạt động một mục, bằng chứng ảnh hoặc log.

---

## PHẦN 5. THIẾT KẾ CƠ CHẾ HIỂN THỊ THEO HOẠT ĐỘNG

### 5.1. Quy tắc
Hai thực thể X, Y. Y thấy X khi và chỉ khi:
- X không phải người chơi thật (NPC, quái, **Bot**), hoặc
- X là chính Y, hoặc
- X và Y đều là người chơi thật và cùng thuộc một nhóm hiển thị đang mở.

Tương tác (chọn mục tiêu, sát thương, mời đội, giao dịch, PK, chat mật) chỉ được phép khi hai bên thấy nhau. Áp cùng một hàm kiểm tra cho cả hiển thị và tương tác, để không lệch nhau.

### 5.2. Nhóm hiển thị
- Mỗi người chơi có `VisGroup` (0 = không nhóm).
- Script hoạt động gọi `JX_JoinVisGroup(activityId)` khi người chơi vào hoạt động và `JX_LeaveVisGroup()` khi rời (tên hàm là đề xuất).
- Server từ chối vào nhóm nếu đã đủ số người thật tối đa của hoạt động.

### 5.3. File cấu hình (đề xuất `visibility.ini`)
```
[TongKim_So]
enabled = 1
maps = <danh sách id bản đồ>
max_real_players = <anh đặt>
sides = 2
max_per_side = <anh đặt hoặc để trống>
bots_fill = 1
```
Mặc định khi giao hàng: **mọi hoạt động tắt**. Anh tự bật và đặt số; Sonnet hướng dẫn bằng một bảng đơn giản.

### 5.4. Trường hợp cần xử lý (tìm đủ ở A-05)
Tổ đội đang có từ trước; bảng xếp hạng; danh sách người chơi quanh đây; minimap đánh dấu người chơi; thư, bang hội, chợ; kỹ năng diện rộng và đạn bay; script đếm số người chơi trong vùng; kênh chat thế giới (Phần 11, D5).

---

## PHẦN 6. HỆ THỐNG CẤU HÌNH VÀ QUẢN TRỊ

| Lớp | Nội dung | Ai dùng |
|---|---|---|
| File cấu hình trong repo source | `visibility.ini`, cấu hình Bot (số lượng mỗi bản đồ, cấp, phái), lịch hoạt động | AI đọc, anh sửa qua Sonnet hoặc trang quản trị |
| Lệnh quản trị dòng lệnh | Tài khoản, nhân vật, bot, sao lưu, khởi động và dừng môi trường thử | Sonnet và worker |
| Trang quản trị web nội bộ | Xem online, bật tắt hoạt động, đổi giới hạn, xem tình trạng server, dùng được trên điện thoại | Anh |
| Lệnh GM trong game | Đã có Lệnh bài GM; giữ danh sách mục an toàn trong `knowledge/gm-token/` | QA |

Mọi thay đổi cấu hình qua trang quản trị đều ghi lịch sử và hoàn tác được.

---

## PHẦN 7. LỘ TRÌNH TỐI ƯU HIỆU NĂNG

| Bước | Nội dung | Điều kiện xong |
|---|---|---|
| P1 | Chốt bản client P46/P47 và server 36 Hz bằng thử trên điện thoại thật | Anh xác nhận chơi mượt, hoặc có danh sách lỗi |
| P2 | Bộ đo chuẩn tự động: tick server, băng thông, khung hình client (đã có công cụ từ Phase 46–48) | Chạy một lệnh ra một bảng số |
| P3 | Đo đường cong tải: 0, 1, 10, 50, 100… Bot trên VM thử | Có biểu đồ tick và RAM theo số Bot |
| P4 | Tối ưu điểm nóng theo số đo (AI quái, đồng bộ, lưu nhân vật lúc thoát gây hụt nhịp [GIẢ THUYẾT, Phase 48]) | Mỗi tối ưu có số đo trước/sau |
| P5 | Đạn bay 36 Hz nếu cần | Theo số đo P1 |

Chỉ tiêu quy mô (bao nhiêu người, bao nhiêu Bot) chưa có. Sonnet đo đường cong P3 rồi đề xuất con số để anh chốt; không tự đặt.

---

## PHẦN 8. LỘ TRÌNH XÂY BOT CHUNG (giai đoạn E)

Chỉ bắt đầu sau khi bộ lọc hiển thị qua thử nghiệm 2.5.

| Bước | Nội dung |
|---|---|
| E1 | **Bot = tài khoản thật cờ `is_bot`, chạy bằng client không giao diện** (Python, giao thức đã đọc ở báo cáo 16). Vì là người chơi thật trên server, Bot tự có cấp, trang bị, túi đồ, kỹ năng, lưu trữ, tổ đội, giao dịch. Một Bot đứng yên trên VM thử. |
| E2 | Hành vi theo luật: đi, săn quái, dùng kỹ năng, hồi máu, đổi bản đồ, làm nhiệm vụ đơn giản |
| E3 | Bộ điều phối dân số: số Bot mỗi bản đồ, giờ hoạt động, luân phiên |
| E4 | Xã hội theo `DESIGN/BOT/SHARED_BOT_SOCIAL_AND_INTERACTION_SYSTEM.md` (chat, giao dịch một người một lúc, khóa party) |
| E5 | Bot trong hoạt động (Tống Kim lấp chỗ trống theo cấu hình) |
| E6 | Đo tải. Nếu client không giao diện quá nặng ở quy mô cần, chuyển phần điều khiển vào trong server (Bot vẫn là đối tượng người chơi nhưng không qua socket) |

Lý do chọn E1 trước: nhanh có kết quả, dùng lại toàn bộ gameplay sẵn có, và tự thỏa mãn yêu cầu Bot đồng bộ cho mọi người. Chi phí mỗi Bot sẽ đo ở E6; số đo Phase 48 (một người thêm 0,2–0,3 ms mỗi nhịp) cho thấy vài chục Bot là trong tầm, vài trăm thì phải đo.

---

## PHẦN 9. MÔ HÌNH TỔ CHỨC AI

### 9.1. Vai trò
| Vai trò | Ai | Làm gì |
|---|---|---|
| Chủ dự án | Anh | Mục tiêu, quyết định trong Phần 11, xem kết quả, đọc báo cáo ngày |
| Project Manager | **Claude Sonnet**, phiên Claude Code chính trên máy Windows | Toàn quyền điều hành: chia việc, khởi chạy worker, kiểm tra, sửa lỗi, tích hợp, merge, quản lý VM thử và môi trường, lưu trạng thái, báo cáo |
| Chuyên gia | **Claude Opus** | Sonnet gọi khi cần: thiết kế mức L4–L5 (bộ lọc hiển thị, kiến trúc Bot), lỗi khó, review độc lập việc quan trọng |
| Worker thực thi | **Codex CLI** (`codex exec`), agent con Sonnet | Viết code, build, test theo task |
| Việc nhẹ | Agent con Haiku | Tóm tắt log, đối chiếu checklist, soạn nháp báo cáo |

**Bỏ:** ChatGPT, 8 phòng ban, Dispatcher, quy trình anh bấm chạy từng prompt.

### 9.2. Cách chạy không cần Dispatcher
Sonnet là vòng lặp điều hành duy nhất. Sonnet tự gọi `codex exec` (đã chạy được không tương tác ở báo cáo Dispatcher [XÁC MINH]) hoặc agent con, chạy nền trong worktree riêng, rồi đọc kết quả khi worker xong. Không ai thăm dò GitHub định kỳ, không có báo cáo trung gian. Worker chỉ cập nhật file task của mình.

### 9.3. Phân cấp độ khó (giữ từ Fable, rút gọn)
| Cấp | Ví dụ | Làm | Kiểm tra |
|---|---|---|---|
| L0–L1 | Tóm tắt, tài liệu, script nhỏ | Haiku / Sonnet | Tự động |
| L2 | Một module, một công cụ | Codex / Sonnet con | Test + agent khác xem |
| L3 | Nhiều module, tích hợp | Codex / Sonnet | Sonnet PM kiểm tra phần quan trọng |
| L4–L5 | Bộ lọc hiển thị, kiến trúc Bot, giao thức | Opus thiết kế | Agent khác nhà cung cấp review + test |

Song song tối đa ban đầu: 3 worker. Một LDPlayer và một VM thử chỉ do một agent điều khiển tại một thời điểm.

---

## PHẦN 10. QUY TRÌNH GITHUB, ĐỒNG BỘ, REVIEW, KIỂM THỬ, BÀN GIAO

### 10.1. Hai repository
| Repository | Nội dung | Nhánh |
|---|---|---|
| `jx1-reports` (đã có) | Kế hoạch, quy tắc, trạng thái, task, báo cáo | **`jx1-ops`**: nhánh vận hành duy nhất của đội AI. `main` giữ nguyên làm lịch sử |
| `jx1-source` (mới, **riêng tư**, cần anh duyệt) | Source client, server, Lua, cấu hình đã lọc, công cụ | `main` = bản đã kiểm chứng; `integration` = tích hợp hằng ngày; `task/<ID>` cho từng việc |

Không đưa lên `jx1-source`: file `.pak`, APK, exe, dll, dump, log, DB, file SQL tài khoản, khóa, mật khẩu. File lớn để trên máy; nếu cần quản lý phiên bản thì dùng Git LFS sau.

### 10.2. Kết nối
- Trên máy Windows: Claude Code và Codex dùng chung Git Credential Manager đã có [XÁC MINH, báo cáo Dispatcher].
- Phiên Claude trên web và điện thoại: dùng kết nối GitHub đã liên kết với tài khoản `ndtangoss-dev`.
- Đổi tài khoản Claude không ảnh hưởng Git; chỉ cần kết nối lại GitHub cho tài khoản Claude mới nếu dùng phiên web.

### 10.3. Quy trình một task
1. Sonnet tạo task trong `JX1_OPS/TASKS/` và branch `task/<ID>`, worktree `D:\JX-wt\<ID>`.
2. Worker làm, tự sửa lỗi theo thang 9 bước của Fable, commit lên branch, cập nhật file task.
3. Sonnet kiểm tra: build, test, diff. L4 trở lên có review độc lập.
4. Sonnet merge vào `integration`, chạy bộ test tích hợp trên VM thử.
5. Cuối mốc, Sonnet merge `integration` → `main` và gắn tag phiên bản (`v0.1-visibility`…).
6. Mỗi bản dựng client hoặc server lưu SHA-256 và đường dẫn trong file task. Luôn giữ bản trước để quay lại.

### 10.4. Kiểm thử
- Không phá các bản vá đã có (Fix31–36, P46, P47): mỗi lần sửa client chạy lại bộ mô phỏng và kiểm tra LDPlayer đã có.
- Bộ test tự động hai người chơi + một Bot cho bộ lọc hiển thị (2.5).
- Bộ đo hiệu năng chuẩn (P2).
- LDPlayer khác điện thoại thật: mốc quan trọng cần anh thử trên điện thoại, Sonnet báo trước trong báo cáo ngày.

### 10.5. Bàn giao và liên tục
Theo `QUY-TAC-VAN-HANH.md` mục 6–8: điểm lưu thường xuyên, `/ket-thuc-ca`, `/tiep-tuc`, phục hồi khi bị ngắt, đổi tài khoản, đổi model.

---

## PHẦN 11. RỦI RO, PHỤ THUỘC, QUYẾT ĐỊNH CẦN PHÊ DUYỆT

### 11.1. Quyết định

| # | Câu hỏi | Mặc định nếu anh không trả lời |
|---|---|---|
| **D1** | Đưa source (mã nguồn, Lua, cấu hình đã lọc; **không** dữ liệu tài khoản, PAK, exe) lên repository GitHub riêng tư `jx1-source`? | **Không có mặc định, cần anh đồng ý.** Chưa đồng ý thì Sonnet dùng Git cục bộ trên máy (vẫn chạy được, nhưng mất máy là mất source và phiên web không đọc được source) |
| D2 | Client AMOLX (Axmol): tạm dừng, chỉ dùng client Cocos V3? | Tạm dừng, giữ báo cáo để dùng sau |
| D3 | Nền thử chuyển đổi: VM thử `JX-Test-36` với server tự dựng 36 Hz; Main VM không đụng | Như vậy |
| D4 | Hoạt động nào cho người thật thấy nhau, bao nhiêu người | Giao hàng với tất cả tắt; anh bật sau |
| D5 | Ở bản đồ thường, người chơi thật có chat kênh thế giới với nhau không? (Tổ đội, giao dịch, PK, chat mật đều chặn theo thiết kế Bot đã duyệt) | Giữ kênh thế giới như game gốc |
| D6 | Mức quyền của Sonnet trên máy: danh sách cho phép (an toàn hơn) hay bỏ qua mọi hỏi đáp | Danh sách cho phép + danh sách cấm (`TOOLS/settings.mau.json`) |

### 11.2. Rủi ro

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Nhiều chỗ trong code giả định người chơi thấy nhau | Cao | A-05 liệt kê hết; cùng một hàm kiểm tra cho hiển thị và tương tác; test hai người chơi |
| Source chỉ nằm trên một máy | Cao | D1; trong lúc chờ, Git cục bộ + sao lưu sang ổ khác |
| Dữ liệu nhạy cảm lọt lên GitHub | Cao | `.gitignore` chặt, quét trước mỗi lần đẩy, repository riêng tư |
| Hết hạn mức Claude giữa chừng | Trung bình | Điểm lưu thường xuyên; Codex làm tiếp; kế nhiệm theo `QUY-TAC-VAN-HANH.md` mục 8 |
| Bot không giao diện quá nặng khi đông | Trung bình | Đo ở E6; có phương án điều khiển trong server |
| Bản quyền: client, server, tài nguyên JX1 thuộc chủ sở hữu gốc; nguồn gói server không rõ | Cao nếu phát hành | Giữ repository riêng tư; quyết định phát hành là của anh; nên hỏi tư vấn pháp lý trước khi kinh doanh |
| Máy tắt thì việc cần VM, LDPlayer dừng | Thấp | Đã tính trong quy trình tạm dừng/tiếp tục; việc đọc source có thể chạy trên phiên web nếu D1 = đồng ý |
| Exe trong gói game không rõ nguồn gốc | Trung bình | Chỉ chạy trong VM, giữ các lệnh cấm cũ |

### 11.3. Phụ thuộc chính
A (khảo sát) → B (chuyển đổi hiển thị) → E (Bot). C (account) và D (hoạt động) chạy song song sau A. Hiệu năng P1–P2 chạy song song từ đầu. D1 ảnh hưởng tất cả.

---

## PHẦN 12. GIAI ĐOẠN, VIỆC LÀM NGAY, VIỆC PHẢI THỬ

| Giai đoạn | Mục tiêu | Thoát khi |
|---|---|---|
| **0. Dựng đội** (ngày đầu Sonnet) | Cài lệnh `/tiep-tuc`, `/ket-thuc-ca`, quyền, Graphify; xác minh Codex chạy được từ Sonnet; repository source (D1); script bật/tắt môi trường thử một lệnh | Sonnet giao và nhận được một task Codex hoàn chỉnh; tắt máy rồi `/tiep-tuc` được |
| **A. Khảo sát, làm chủ** | Bản đồ kiến trúc, luồng đăng nhập, đường đồng bộ thực thể, danh mục script | Tài liệu A-04…A-07 có bằng chứng |
| **B. Thử chuyển đổi server** | Bộ lọc hiển thị + chặn tương tác + cấu hình | Qua 5 thử nghiệm ở 2.5 |
| **C. Account** | Công cụ quản trị, tài khoản bot | Tạo, khóa, xem online, đánh dấu bot bằng một lệnh |
| **D. Kiểm kê hoạt động** | Bảng hoạt động 5 trạng thái | Mọi hoạt động trong danh sách có trạng thái và bằng chứng |
| **E. Bot** | E1 → E6 | Theo Phần 8 |
| **P. Hiệu năng** | P1 → P5 | Theo Phần 7 |

**Làm ngay sau khi duyệt:** giai đoạn 0; A-04 (tổng hợp kiến trúc từ báo cáo có sẵn); A-05 (đường đồng bộ thực thể, Opus); P1 (anh thử APK P46/P47 và server 36 Hz trên điện thoại khi tiện).
**Phải thử nghiệm trước khi tin:** bộ lọc hiển thị; Bot không giao diện kết nối được bản server tự dựng; tải nhiều Bot.
**Cần anh quyết:** D1 (bắt buộc), D2–D6 (có mặc định).

Danh sách việc chi tiết: `TASKS/BACKLOG.md`.

---

## PHỤ LỤC. NỘI DUNG FABLE v0.3 BỊ THAY THẾ

| Nội dung cũ | Nay |
|---|---|
| Client Axmol mới, server mới độc lập (INV-02…05, roadmap M0–M9) | Dùng lại client Cocos V3 và server gốc |
| Opus là Project Manager | Sonnet là PM; Opus là chuyên gia |
| Kế hoạch thử 7 ngày | Bỏ; thay bằng giai đoạn 0 và A |
| Cấu trúc `project-state/`, `tasks/` ở gốc repo | Gộp vào `JX1_OPS/` trên nhánh `jx1-ops` |
| Đánh giá công cụ để trống | `TOOLS/CONG-CU.md` |

**Vẫn giữ:** quy tắc thế giới Bot dùng chung; yêu cầu thay thế AI không gián đoạn; thang tự sửa lỗi 9 bước; giảm báo cáo nội bộ; phân cấp L0–L5; báo cáo ngày 7 câu; không làm Secret Vault.
