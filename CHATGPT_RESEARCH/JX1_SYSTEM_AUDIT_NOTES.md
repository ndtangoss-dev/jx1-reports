# JX1 — GHI CHÉP NGHIÊN CỨU ĐỘC LẬP CỦA CHATGPT

- Ngày lập: 2026-11-20
- Nhánh lưu trữ: `chatgpt-research/jx1-system-audit-2026-11-20`
- Nhánh nguồn được đọc: `jx1-ops`
- Nhánh nền của nhánh ghi chép này: `main` (nhánh lịch sử), KHÔNG phải `jx1-ops`
- Mục đích: chống trôi ngữ cảnh, lưu lại hiểu biết và các giả thuyết cần kiểm chứng trước khi đo một nhiệm vụ độc lập.
- Tính chất: ghi chép nghiên cứu; không phải quy tắc vận hành; không phải trạng thái runtime; không có quyền chỉ đạo hệ thống.

## 0. Cảnh báo về nguồn sự thật và độ mới

README hiện hành của `JX1_OPS` nói rõ: `jx1-ops` là nơi duy nhất giữ quy trình, kế hoạch, trạng thái và tiến độ của đội AI JX1. Không dựa vào lịch sử chat hoặc Memory để thay thế nguồn này.

README cũng nói `main` chứa lịch sử báo cáo để tra cứu; các quy tắc cũ trên `main` (AGENTS.md, WORKFLOW_JX1.md, PROMPTS/*, 00_PROJECT_CONTROL/*) đã hết hiệu lực.

Vì vậy:
- Khi làm việc với dự án, phải đọc nguồn hiện hành trên `jx1-ops`.
- Nhánh ghi chép này chỉ là sổ nghiên cứu độc lập của ChatGPT, không được xem là nguồn trạng thái của đội.
- Mọi chi tiết có thể thay đổi phải xác minh lại trước khi sử dụng.
- Phân biệt: [XÁC MINH TRONG FILE] / [FILE GHI NHẬN] / [SUY LUẬN] / [CHƯA KIỂM TRA RUNTIME].

## 1. Đính chính kiến trúc — điểm quan trọng nhất

Đã đọc `JX1_OPS/README.md` và `JX1_OPS/QUY-TAC-VAN-HANH.md` trên `jx1-ops` ngày 2026-11-20.

Kiến trúc vận hành được tài liệu hiện hành mô tả:
- **Chủ dự án:** quyết định các vấn đề thuộc phạm vi cần chủ duyệt và vùng Đỏ.
- **Sonnet (PM):** phiên Claude Code chính trên máy Windows `C:\Jx1CocoV3`; đầu mối duy nhất; tự chia việc, khởi chạy worker, kiểm tra, sửa, merge, quản lý môi trường thử, lưu trạng thái và báo cáo.
- **Opus:** được Sonnet gọi cho việc L4–L5 và lỗi khó; không điều hành.
- **Codex CLI:** worker chính, thực hiện phần lớn viết code, nghiên cứu source, build và review chéo; chạy nền trong worktree theo task.
- **Agent con Sonnet/Haiku:** việc song song và việc nhẹ.
- **ChatGPT, 8 phòng ban, Dispatcher, hàng đợi thăm dò GitHub:** quy tắc hiện hành ghi rõ không còn trong kiến trúc vận hành.

ĐÍNH CHÍNH GHI CHÉP CŨ:
Các mô tả trước đây trong hội thoại về chuỗi “ChatGPT → Sonnet A/B → Tổng quản → tiểu yêu/Codex” không được dùng làm mô hình hiện hành. Chúng có thể phản ánh một giai đoạn/thiết kế cũ, nhưng trái với README và quy tắc vận hành hiện hành đã đọc ngày 20/11. Phải lấy file hiện hành làm chuẩn, không tự hòa giải bằng suy đoán.

## 2. Quy tắc vận hành đã đọc

Nguồn: `JX1_OPS/QUY-TAC-VAN-HANH.md`, phiên bản 1.1, ngày 2026-11-16.

### 2.1 Vòng làm việc Sonnet
Lấy task tiếp theo từ `TASKS/BACKLOG.md` → tạo task/branch/worktree → giao worker hoặc tự làm → trong lúc chờ làm việc khác → kiểm tra build/test/diff → đạt thì merge, không đạt thì trả lại với lỗi cụ thể → cập nhật trạng thái và điểm lưu → lặp.

Tài liệu nêu:
- Task mục tiêu 15–60 phút, có kết quả kiểm chứng được.
- Không ngồi chờ worker nếu có việc khác.
- Không kết thúc lượt chỉ để báo cáo.
- Báo cáo thường ghi vào file trạng thái; báo cáo cho chủ dự án thường một lần mỗi ngày, trừ sự cố nghiêm trọng hoặc cần quyết định.

### 2.2 Quyền hạn và vùng Đỏ
Sonnet có quyền tự xử lý các việc thông thường trên máy phát triển, repo, VM thử JX-Test-36 và LDPlayer theo quy tắc.

Vùng Đỏ gồm các thao tác cụ thể liên quan Main VM/dữ liệu thật, xóa dữ liệu không thể khôi phục, đưa source/dữ liệu lên dịch vụ ngoài chưa được duyệt, phát sinh chi phí, thay đổi tài khoản thật/mạng/tường lửa, và bật VM bridged. Phải đọc nguyên văn mục 3 trước khi đánh giá một hành động cụ thể; không rút gọn thành “Sonnet có toàn quyền”.

Các rào chắn được tài liệu nhấn mạnh:
- Không chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe`.
- Không chạy exe gói game trên máy thật; chỉ chạy trong VM.
- Không ghi mật khẩu, token, IP riêng vào Git/báo cáo.
- Không dừng ReportServer.
- Không bật hai VM có MAC trùng cùng lúc.
- Không snapshot khi VM đang chạy.
- Không hồi quy các Fix31, Fix33–36, P46, P47; sửa client phải chạy lại bộ kiểm tra liên quan.

### 2.3 Bằng chứng và nghiệm thu
Tài liệu quy định bằng chứng task gồm commit + kết quả test + vài dòng ở mục “Kết quả” trong file task. Dùng nhãn tin cậy:
- [XÁC MINH]
- [NGUỒN]
- [BÁO CÁO]
- [GIẢ THUYẾT]
- [CHƯA BIẾT]

Không được kết luận “đã sửa” chỉ dựa trên lời báo; phải test lại.

### 2.4 Chống quên ngữ cảnh
Mục 11 quy định Sonnet không giao việc từ trí nhớ. Trước mỗi lần giao việc, merge hoặc báo cáo, phải đọc lại trạng thái, khóa và task liên quan. Hook nhắc sau nén ngữ cảnh phải được kiểm chứng thực tế; không mặc định hook hoạt động chỉ vì tài liệu mô tả.

### 2.5 Điểm lưu và phục hồi
Mục 6 quy định điểm lưu là file trạng thái đã cập nhật + commit + push lên `jx1-ops`; code task lưu ở branch task. Mục 7 mô tả /ket-thuc-ca và /tiep-tuc, bao gồm kiểm tra trạng thái thực tế so với file và build/test lại phần chưa xác nhận.

## 3. Công cụ Tổng quản — những gì đã thấy trong mã

Nguồn: `JX1_OPS/TOOLS/tong_quan.py` trên `jx1-ops`.

Các chi tiết đọc được:
- Mô tả đầu file: mỗi vòng do Task Scheduler gọi khoảng 3 phút; theo dõi worker sống/im/treo/chết, commit khi xong, restart theo chính sách, giao task ready và sinh trạng thái worker/tiến độ.
- `MAXALL = 20`: trần worker đồng thời trong snapshot mã đã đọc.
- `MAXKEY = 4`; có `KEY_CAP` riêng cho JX-K5/JX-K6; `KEY_ORDER` quy định thứ tự phân phối.
- `IM, TREO = 20, 60`: ngưỡng phút trong mã cho trạng thái im/treo.
- `ensure_worktree(i)` tạo worktree branch `task/<ID>` từ `jx1-ops`.
- `run_launch(i,key)` gọi `TOOLS/chay_codex.ps1`, chuyển effort từ metadata task nếu hợp lệ và ghi model worker vào file trạng thái.
- Mã có logic đọc PID, Task Scheduler, transcript và thời điểm hoạt động; heartbeat đơn lẻ không đủ để khẳng định worker đang làm việc có ích.

Lưu ý: đây là giá trị trong file được đọc, không phải xác nhận cấu hình đang chạy trên máy. Phải kiểm tra runtime và phiên bản file thực tế trước khi sử dụng số liệu.

## 4. Những điểm bất nhất / rủi ro dữ liệu đã thấy

### 4.1 Trạng thái task có thể không đồng nhất
Trong snapshot nghiên cứu trước đó:
- `STATE/TIEU-YEU.md` ghi SC-001/SC-002 ở trạng thái chờ gộp.
- `TASKS/SC-002.md` ghi status running.
- `REPORTS/SC-002.md` ghi PARTIAL, chưa có thay đổi code/build.
- `STATE/TIEN-DO.md` và `STATE/DANG-LAM.md` thể hiện các trạng thái/việc tiếp theo khác nhau.

Đây là ví dụ cần tái kiểm tra trên dữ liệu mới; không được mặc định vẫn còn đúng hôm nay.

### 4.2 Tiền điều kiện worktree
Báo cáo hiệu quả Q-102 ghi SC-002 bị PARTIAL vì worktree thiếu `KItem.cpp` và `KPlayerDBFuns.cpp`, đồng thời worktree không được cắt từ nhánh source đúng. Đây là dấu hiệu cần đo preflight trước dispatch: file nguồn, branch base, dependency và phạm vi file phải tồn tại.

### 4.3 Token/cost chưa có số liệu đầy đủ
`DO-HIEU-QUA-QUY-TRINH.md` ghi rõ token Codex chưa đo ở mốc Q-102. Không được tự ước lượng rồi trình bày như số thực. Nếu hệ thống có log token/chi phí, cần xác định nguồn và cách cộng; nếu không, đánh dấu không đo được.

### 4.4 Truyền đạt sai kênh
Ghi nhận lịch sử trước đó có tình huống thông điệp “A Chat” được nhập vào cửa sổ Claude Code thay vì Chrome Chat, nên không tới đúng người nhận. Đây là bài học lịch sử; mô hình A/B hiện không được xem là kiến trúc hiện hành nếu không có tài liệu mới chứng minh.

### 4.5 Nguồn gốc kết luận và lan truyền giả thuyết
Trong sự cố mất item, từng có kết luận quy nguyên nhân cho hook Lua online.lua dựa trên ngữ cảnh trước đó; thử nghiệm sau đó cho thấy tắt Lua hook vẫn mất item, và khôi phục bundle .orig-a07c thì item trở lại. Bài học: mọi kết luận kỹ thuật phải ghi nguồn, bằng chứng, giả thuyết cạnh tranh và phép thử loại trừ; không để một tác nhân biến giả thuyết thành sự thật rồi các tác nhân khác lặp lại.

## 5. Mốc đo hiệu quả lịch sử — chỉ dùng tham khảo

Nguồn: `JX1_OPS/STATE/DO-HIEU-QUA-QUY-TRINH.md`.

### 5.1 Mốc 06:59–11:52 ngày 20/11 (trước vá quy trình)
- 12 quyết định Chat trong khoảng 5 giờ.
- 4 lần đổi hướng lớn.
- Khoảng 20 thư Chat→A/B.
- Ít nhất 4 lần restart gs001, ước tính 40–60 phút chờ.
- Tiêu chí cường hóa đạt bằng số thật: 0/8.
- Tiểu yêu chạy: 0 tại mốc được ghi.

### 5.2 Q-102 tới 21:35 ngày 20/11
- SC-001: BLOCKED, khoảng 1 giờ 20; thiếu đầu vào.
- SC-002: PARTIAL, khoảng 1 giờ 50; worktree thiếu file và chưa có diff.
- SC-003: hủy.
- SC-004: hủy sau khi kiểm tra patch không áp sạch.
- Kết luận trong tài liệu: 0 diff mã từ các task Codex được giao ở mốc đó; 2/4 task bị chặn vì thiếu đầu vào, 2/4 bị hủy.
- Token Codex: chưa đo.

Các con số này thuộc một giai đoạn cụ thể, không phải baseline cho nhiệm vụ đo sắp tới.

## 6. Kế hoạch đo nhiệm vụ độc lập sắp tới

Trạng thái tại thời điểm lập tài liệu: CHƯA BẮT ĐẦU. Chỉ bắt đầu sau khi chủ dự án giao nhiệm vụ và thông báo.

Nguyên tắc:
1. Ghi nhận yêu cầu nguyên văn, thời điểm bắt đầu, tiêu chí nghiệm thu và trạng thái ban đầu.
2. Quan sát quy trình đang vận hành theo đúng kiến trúc hiện hành; không áp mô hình A/B/Tổng quản cũ nếu runtime không có.
3. Không can thiệp, không nhắn chỉ thị, không sửa cấu hình hoặc hàng đợi trong giai đoạn baseline.
4. Theo dõi từng lần handoff, thời gian chờ, thời gian làm thực, retry, lỗi, rework, thay đổi phạm vi, context reload và quyết định.
5. Kiểm chứng kết quả bằng commit/diff/test/build/runtime phù hợp; phân biệt lời báo cáo với bằng chứng.
6. Thu thập token/chi phí chỉ khi có nguồn đo tin cậy.
7. Không lấy số liệu lịch sử ở mục 5 làm số liệu của nhiệm vụ mới.

Đầu ra sau nhiệm vụ:
- Timeline end-to-end.
- Thời gian theo từng giai đoạn và thời gian chờ.
- Số lần giao việc/retry/rework.
- Chất lượng và bằng chứng nghiệm thu.
- Điểm nghẽn có bằng chứng.
- Đề xuất cải tiến có thứ tự ưu tiên, lợi ích, chi phí, rủi ro, phương án quay lui và tiêu chí đo sau cải tiến.

## 7. Giao thức tiếp tục nghiên cứu sau khi ngữ cảnh bị nén

Khi mở lại ghi chép này:
1. Đọc file này để khôi phục bản đồ khái niệm.
2. Đọc lại `JX1_OPS/README.md` trên `jx1-ops`.
3. Đọc lại các file nguồn liên quan trên `jx1-ops` (ít nhất quy tắc vận hành, trạng thái bàn giao/trạng thái hiện tại, task đang chạy, báo cáo hiệu quả).
4. Nếu cần nói về trạng thái runtime, yêu cầu bằng chứng runtime; không suy ra từ Git.
5. Cập nhật ghi chép này bằng commit mới trên nhánh riêng; ghi ngày, nguồn đã đọc và điều gì thay đổi.
6. Không đưa file này vào `jx1-ops`, không merge vào nhánh hệ thống, không dùng nó thay thế state của dự án.

## 8. Nguồn đã đọc trực tiếp trong lần nghiên cứu

Tất cả các đường dẫn dưới đây được đọc từ ref `jx1-ops` vào ngày 2026-11-20:
- `JX1_OPS/README.md`
- `JX1_OPS/QUY-TAC-VAN-HANH.md`
- `JX1_OPS/STATE/BAN-GIAO.md`
- `JX1_OPS/STATE/QUYET-DINH.md`
- `JX1_OPS/TOOLS/tong_quan.py`
- `JX1_OPS/STATE/DO-HIEU-QUA-QUY-TRINH.md`

Một số tài liệu trong lần đọc chứa thông tin lịch sử hoặc bàn giao nhiều ngày trước; mọi trạng thái có tính thời điểm phải đọc lại trước khi sử dụng.

---
**Nguyên tắc của sổ nghiên cứu:** Nhớ để định hướng; đọc nguồn để xác minh; quan sát runtime để kết luận.

---

## 9. Cập nhật nghiên cứu: bàn giao và phục hồi phiên khi nén/chuyển phiên (đọc lại 20/11/2026)

**Phạm vi:** chỉ cập nhật sổ nghiên cứu trên nhánh riêng `chatgpt-research/jx1-system-audit-2026-11-20`. Không ghi bất kỳ nội dung nào vào `jx1-ops`; không thay đổi trạng thái vận hành, hàng đợi, hook, prompt, worker hay máy đang chạy.

### 9.1 Nguồn vận hành mới nhất đã đối chiếu

Đọc trực tiếp từ `jx1-ops`:
- `JX1_OPS/README.md` — SHA blob `98c08dbfe33969a4065b3e86f1a82e04fe9363b9`.
- `JX1_OPS/STATE/BAN-GIAO.md` — SHA `807c1161dd70a231c83aa3a6fec3285db0edf677`.
- `JX1_OPS/STATE/TRANG-THAI.md` — SHA `a8a7787e1f0f07cdf4d14b89baeea0a98e5e635d`.
- `JX1_OPS/STATE/KHOA.md` — SHA `9c0a780454e2b92a69dc071077666b2d5ed1073b`.
- `JX1_OPS/STATE/DANG-LAM.md` — SHA `e841a6573b5702ad9aecb5448455d6268c9511a1`.
- `JX1_OPS/HOP-THU/CHO-SONNET-B.md` — đã đọc phần cuối, có các chỉ thị #B-060 đến #B-075.
- `JX1_OPS/HOP-THU/TU-SONNET-B.md` — SHA `990254493182a77402c590273c7e05e4d883a523`.
- `JX1_OPS/HOP-THU/A-B.md` — SHA `b7abe5677447212444d566ef21e85bf1fcd22706`.
- `JX1_OPS/STATE/HANG-DOI-VIEC.md` — SHA `689200bb9a89d66917a27505824b99d048771df3`.
- `JX1_OPS/STATE/HANG-DOI-VIEC-B.md` — SHA `2a5099c1acd3408ca44a4eb8229d6dffa4446fc0`.
- `JX1_OPS/QUY-TAC-VAN-HANH.md` — SHA `c2459509e9a6bd68e84a448aacf0db734b3e446c`.

Các SHA là dấu nhận dạng blob tại thời điểm đọc; không chứng minh runtime trên máy đồng bộ với Git.

### 9.2 Ảnh chụp bàn giao theo dấu thời gian trong tài liệu

**Sonnet A — mốc #334, 20/11 23:05, ghi trong `STATE/DANG-LAM.md`:**
- Hạn mức sắp hết; chỉ thị lưu trạng thái và chờ Chat đánh thức sau 23:50.
- P0: đo cường hóa đồ vàng +1, lúc đó CHƯA ĐO; thao tác menu sách/GM trên LD chưa ổn định. Tài liệu nêu các phương án chuẩn bị đồ: lệnh GM “Nhận Thẻ GM”, AddGoldItem qua ReloadScript menu, hoặc cấp đồ khi tạo tài khoản riêng.
- P1: tạo tài khoản riêng cho chủ, chuẩn bị một lần bộ 10 đồ xanh + thủy tinh + bạc + đồ vàng + sách; CHƯA LÀM. Không dùng tài khoản tkchuvuong/atestvaihero.
- P2: kiểm tra giật lag vc28, đo 5 lần +2 (tài liệu ghi khoảng 95%).
- Đã đo đồ xanh +1..+3; kết quả và sai lệch/spec được ghi ở `CUONG-HOA.md`. Đã gỡ hook QHBV_Book khỏi online.lua trên Test-36, nhưng chưa xác minh relog sau restart gs001.
- APK vc28 đã cài LD, CHƯA phát cho chủ; chủ CHƯA được mời test.
- Lệnh tiếp: đọc hộp thư #335 trở đi; không restart gs001/build APK khi sắp hết hạn mức.

**Sonnet B — mốc #B-075, 20/11 22:45, ghi trong `STATE/DANG-LAM.md`:**
- Hạn mức 5 giờ chung được ghi là 93%; cần lưu trạng thái ngay và tiếp tục sau khi được đánh thức.
- Thư đã đọc đến #B-075; `A-B.md` ghi đã trả lời #B-074, commit tham chiếu `390e0742`.
- P0: SC-002 ở trạng thái ready, chờ Tổng quản giao Codex. Phạm vi lúc lưu: thêm loại thuộc tính 28/29/30 vào `JxQhScalable`; loại 40 còn CHƯA XÁC MINH; giữ EnChanceRong +5%; giữ JxQhScale ±50 theo Q-104; pItemData++ ưu tiên thấp. Khi có diff, B đọc, duyệt/trả lại và báo A nạp + đo.
- P1: review diff client của A (EnChanceRong, tooltip `KuiItemdescVN.cpp`, và các bản vá lag 31/33/34/47 trên qh9A).
- P2: SC-005 Ký Trân Các, chờ A gửi type.txt và dữ liệu buysell/goods thật từ PAK; chưa giao Codex khi cường hóa chưa xong.
- P3: backlog gồm Phòng thủ%, GoldMagic vàng, và dọn hook thử trước khi lên server thật.
- Hướng dẫn tiếp tục được ghi: fetch-poll hộp thư, khi có thư thì đọc, trả lời ở A-B.md + TU-SONNET-B.md, cập nhật marker, commit/push và gửi tín hiệu “B Xong #...”. Đây là hướng dẫn trong tài liệu, chưa phải xác minh poller vẫn đang chạy.

**Bản bàn giao tổng quát `STATE/BAN-GIAO.md`:**
- Mốc hiện tại mà file tự ghi là 20/11 22:14 (hook PreCompact), đang chạy SC-002, thư cuối #157; chỉ dẫn PM mới đọc các file cốt lõi và lấy chi tiết bước dở từ dòng cuối TRANG-THAI.md.
- Mốc 22:14 cũ hơn các ghi nhận A #334 (23:05) và B #B-075 (22:45) trong DANG-LAM. Vì vậy không dùng riêng BAN-GIAO.md làm trạng thái mới nhất; cần đối chiếu timestamp và trạng thái theo từng phiên/worker.
- README chỉ định PM đọc BAN-GIAO, TRANG-THAI, KHOA, quy tắc, backlog/task active, quyết định và báo cáo mới nhất. Worker chỉ đọc đúng phần quy tắc và task được giao.
- Quy tắc vận hành mục 11 yêu cầu không giao việc từ trí nhớ; trước dispatch/merge/report phải đọc lại TRANG-THAI, KHOA và task liên quan. Hook sau compact phải được kiểm tra thực tế, không giả định hoạt động chỉ vì có mô tả.

### 9.3 Những điểm cần giữ tách biệt khi phục hồi

1. **Bàn giao tổng thể khác checkpoint của từng phiên.** BAN-GIAO.md là entry point cho PM, nhưng A và B có checkpoint riêng nằm trong DANG-LAM, hộp thư và A-B.md. Khi timestamp lệch, phải ghi rõ nguồn nào mới hơn; không tự ghi đè mốc cũ bằng suy đoán.
2. **Mốc Git không phải trạng thái runtime.** “running”, “ready”, “đang poll”, “đã build”, “đã cài” trong tài liệu cần được xác minh bằng task file, process/log, branch/worktree, commit và test tương ứng trước khi tuyên bố vẫn đang đúng.
3. **Trạng thái hoàn thành phải gắn mức xác minh.** Phân biệt đã viết/đã đọc mã/đã build/đã chạy trên Test-36/đã nghiệm thu bởi chủ. Ví dụ trong mốc A #334, vc28 đã cài trên LD nhưng chưa phát chủ test; hook đã gỡ nhưng chưa xác minh relog sau restart.
4. **Bàn giao cần chỉ rõ bước tiếp theo có thể thực thi.** Với từng việc: ID, owner, status, branch/worktree, commit hoặc artifact mới nhất, tiến trình/tài nguyên đang dùng, bước kế tiếp, điều kiện chờ, lệnh/đường dẫn phục hồi và điều tuyệt đối không được làm.
5. **Giới hạn phiên/hạn mức là tín hiệu lưu checkpoint, không phải tín hiệu dừng tùy tiện.** Ghi lại phần đã làm, phần chưa kiểm, việc nền, hạn mức được báo trong nguồn và điều kiện tiếp tục; không tự khởi động lại tiến trình hoặc tiêu thụ thêm tài nguyên nếu không có quyền.
6. **Không hợp nhất lịch sử A/B thành kiến trúc hiện hành.** README và quy tắc vận hành xác định Sonnet là PM/PM kế nhiệm; các ghi chú A/B được dùng như dữ liệu lịch sử hoặc checkpoint cụ thể trong tài liệu. Cần xác minh ai đang chạy ở runtime trước khi áp dụng các chỉ thị A/B.

### 9.4 Đề xuất cải tiến cho nhánh nghiên cứu — chưa áp dụng vào vận hành

- Tạo mẫu checkpoint chuẩn theo phiên/worker với trường bắt buộc: timestamp + timezone, session/owner, task IDs, state, branch/worktree, HEAD commit, process/PID và tài nguyên đang giữ, artifacts, verified/unverified, inbox cursor, next action, blockers, resume command, safety boundaries.
- Duy trì một “handoff index” chỉ trỏ tới checkpoint mới nhất của mỗi vai trò; không sao chép toàn bộ lịch sử vào một file và không để một timestamp cũ được hiểu nhầm là trạng thái mới nhất.
- Khi resume, thực hiện đối chiếu ba chiều: checkpoint → Git/task/inbox → runtime. Ghi rõ kết quả từng chiều: MATCH / DRIFT / UNKNOWN.
- Tạo recovery drill có kiểm soát trên phiên thử hoặc bản sao an toàn: phiên mới đọc đúng entry point, xác định đúng task và bước kế tiếp, không dispatch trùng, không bỏ qua blocker, không chạm vùng Đỏ. Ghi thời gian phục hồi, sai lệch và lỗi.
- Chỉ sau khi có số liệu drill mới đề xuất thay đổi hook, prompt, quy tắc hoặc cấu trúc checkpoint. Không tự thay đổi chúng từ nhánh nghiên cứu.

### 9.5 Giới hạn xác minh

Đây là **đọc tài liệu GitHub**, không phải kiểm tra máy Windows, Claude Code, tiến trình poller, Codex workers, VM, LDPlayer hay runtime. Không kết luận SC-002 đang thực sự chạy; không kết luận A/B còn tồn tại như hai phiên đang hoạt động; không kết luận các tác vụ A #334/B #B-075 đã được tiếp tục hoặc hoàn tất sau các mốc ghi trong tài liệu.

**Trạng thái cập nhật:** `RESEARCH_NOTES_UPDATED`; chỉ lưu kiến thức và đề xuất cải tiến trên nhánh nghiên cứu riêng. Không thay đổi `jx1-ops`.



## 10. Cập nhật giám sát nhiệm vụ đêm 20–21/11/2026 — chỉ đọc nguồn vận hành, không can thiệp

**Phạm vi cập nhật:** ghi nhận lệnh mới của chủ dự án và phản hồi Sonnet trên Git; đối chiếu task/report liên quan để lập ảnh chụp trạng thái ban đầu cho đợt theo dõi. Chỉ sửa sổ nghiên cứu ở nhánh `chatgpt-research/jx1-system-audit-2026-11-20`. Không tạo/sửa task, không gửi lệnh, không commit/push vào `jx1-ops`, không thay đổi worker, worktree, runtime, VM, LDPlayer, cấu hình hoặc queue.

### 10.1 Dấu vết Sonnet đã nhận lệnh

Đã đọc trực tiếp hai commit trên `jx1-ops`:

- `a997df0a6efee510b00164934e9e32a5efc84e1e` — commit message `Chat: lenh dem #335/#B-076 cuong hoa hoan chinh, lag, phi phong`; thời gian GitHub ghi `2026-11-20T16:59:09Z` (23:59 ngày 20/11 giờ Việt Nam). Diff bổ sung:
  - #335 cho A: chuẩn bị tài khoản thử riêng, đo đồ vàng +1 và +2, đo UI theo ảnh Q-91, port bản vá lag 31/33/34/47 và build APK vc28, kiểm phi phong trên LD; ghi từng mốc và bằng chứng số thật.
  - #B-076 cho B: SC-002, task phi phong mới (SC-006), review diff client của A; nghiệm thu trên LD và báo theo mốc.
  - Cập nhật hộp thư và dòng lịch sử cho thấy đây là lệnh được ghi vào kênh vận hành.
- `e47370ee0301a9517db7799a38cd3e75356ac09a` — commit message `B: SC-006 phi phong, tra loi #B-076`; thời gian `2026-11-20T17:00:27Z` (00:00 ngày 21/11 giờ Việt Nam). Diff tạo task SC-006 và ghi phản hồi của B.

**Kết luận có giới hạn:** [XÁC MINH TRONG GIT] lệnh #335/#B-076 đã được ghi vào hộp thư/kênh vận hành và có commit phản hồi của B. Điều này chứng minh dấu vết giao tiếp Git, không chứng minh Sonnet còn đang suy nghĩ, Codex đã được khởi chạy, hoặc bất kỳ worker/runtime nào đang hoạt động.

### 10.2 Ảnh chụp task và báo cáo liên quan

Đã đọc lại các file hiện hành trên `jx1-ops`:

| Nguồn | SHA blob tại thời điểm đọc | Nội dung/trạng thái ghi trong file | Mức xác minh |
|---|---|---|---|
| `JX1_OPS/TASKS/SC-006.md` | `6cfd5f7573eca70364ab92b54e34cbcdfa9e8b0b` | `ready`, L3, owner B, agent Codex, branch `task/SC-006`, worktree `D:\\JX-wt\\SC-006`, depends_on SC-002; phạm vi KItemList.cpp/KItem.cpp và GoldMagic/GoldItem | [XÁC MINH TRONG FILE], không xác minh worker/worktree thực |
| `JX1_OPS/TASKS/SC-002.md` | `89739f0fc1166eee4a1b674b4d59f0cfe2448c18` | `done`; mô tả JxQhScalable 28/29/30, +40 chưa xác minh, giữ EnChanceRong +5%, làm tròn gần nhất; phần pItemData++ ưu tiên thấp | [XÁC MINH TRONG FILE], chưa kiểm diff/build/merge/runtime |
| `JX1_OPS/REPORTS/H-05-ui-cuong-hoa.md` | `fbb5ab7bc0333562f1dfec2aba3491ceebfb4803` | DONE khảo sát tĩnh UI; chưa build/chạy game; Lua nghiệp vụ, SPR, UI runtime và kết quả cường hóa chưa xác minh; 0/11 ca đề xuất đã chạy | [BÁO CÁO], không phải nghiệm thu tính năng |
| `JX1_OPS/REPORTS/H-03-cuong-hoa.md` | `df9d49679953d76ef7d0018935eb48622c783094` | DONE khảo sát tĩnh; cấu hình/binary thực nạp, xác suất runtime và trạng thái triển khai chưa xác minh | [BÁO CÁO], không phải nghiệm thu tính năng |

SC-006 ghi rõ:
- Mục tiêu phi phong: đủ dòng thuộc tính; cấp cao tăng hơn cấp thấp; tài phú theo Q-90; đổi ngoại hình cạnh tên ngay; mặc tăng chỉ số thật và tháo thì mất; tài phú thiếu thì tự tháo.
- B đã ghi nhận qua đọc mã rằng `QhCheckPifeng` không được gọi ở đường `LuaSetItemEnChance`, nên khi hạ +N làm tài phú giảm, phi phong có thể vẫn đang mặc. Đây là phát hiện đọc mã trong task, chưa phải phép thử runtime.
- Đường ngoại hình đang có nghi vấn cấp >10 dùng `level%10`, có thể làm cấp 11 trùng hình cấp 1; cần kiểm tra mapping tài nguyên và đồng bộ server/client.
- Task yêu cầu test sáu kịch bản trên LD; nhưng task hiện vẫn ghi `ready`, không có bằng chứng test nào được chạy.

### 10.3 Phạm vi đêm được giao và chuỗi phụ thuộc

**Cường hóa/UI**
- #335 yêu cầu A đo đồ vàng +1, +2; làm UI cửa sổ cường hóa theo ảnh Q-91 (đồ + 3 đá, tỷ lệ, nút xác nhận/đóng, thông báo thành công/thất bại); ảnh LD trước/sau.
- H-05 chỉ chứng minh luồng tĩnh: nút → `c2s_runscript` → Lua mở `s2c_opengive` → `KuiGive_New` → khóa item → xác nhận `c2s_playergiveback`. Chưa chứng minh cửa sổ có đầy đủ các trường/nhãn/hiển thị mà #335 yêu cầu, cũng chưa có test tương tác.
- SC-002 có status `done` trong task file mới đọc, trong khi SC-006 vẫn `ready` và khai báo phụ thuộc SC-002. Cần theo dõi xem Sonnet đã xác nhận dependency và giao Codex thật chưa; không suy luận từ status đơn lẻ.

**Lag/quái vật**
- #335 ghi A port các bản vá lag 31/33/34/47 vào `D:\\JX-build\\qh9A`, build APK vc28, đo FPS trước/sau trên LD.
- Tại thời điểm cập nhật này chưa đọc được diff port, build log, APK hash mới, FPS đo lặp hoặc bằng chứng riêng về lỗi quái vật. Không kết luận lag/quái vật đã sửa.

**Phi phong**
- SC-006 là task code server phía B; #335 giao A kiểm trên LD sau khi có phần sửa.
- Cần theo dõi riêng kết quả build server, test từng tiêu chí, đồng bộ ngoại hình ở góc nhìn người chơi khác, chỉ số trước/sau mặc-tháo, ngưỡng tài phú và ca giảm +N khi đang mặc.
- Báo cáo static không thay cho kiểm tra chỉ số chiến đấu và relogin.

### 10.4 Những gì đã và chưa được thực hiện bởi ChatGPT trong lượt giám sát

Đã thực hiện:
- Đọc commit #335/#B-076 và commit phản hồi SC-006.
- Đọc task SC-006, SC-002 và báo cáo H-05, H-03 từ `jx1-ops`.
- Ghi nhận trạng thái, dependency, điểm nghi vấn và khoảng trống bằng chứng trong sổ nghiên cứu riêng.

Không thực hiện:
- Không gửi thêm lệnh cho Sonnet/B/Codex và không tạo task.
- Không đọc/ghi các worktree hoặc truy cập máy Windows, tiến trình Claude Code, Codex, VM, LDPlayer.
- Không build APK/server, không chạy test, không đo FPS, không xem runtime log.
- Không sửa bất kỳ file nào trên `jx1-ops`; không thay đổi queue/lock/config/hook/worker.
- Không khẳng định đang giám sát liên tục nền; ảnh chụp này chỉ phản ánh dữ liệu Git được đọc trong lượt.

### 10.5 Mốc baseline và cách tiếp tục

Mốc quan sát Git đầu tiên của lệnh đêm: commit #335 lúc 23:59 ngày 20/11 giờ Việt Nam; phản hồi B và task SC-006 xuất hiện lúc 00:00 ngày 21/11. Đây là mốc ghi nhận lệnh trong Git, **không phải** thời điểm chắc chắn Sonnet bắt đầu suy nghĩ hoặc Codex bắt đầu làm việc.

Ở lần kiểm tra kế tiếp, chỉ đọc các bằng chứng mới trên Git: task/report, commit, diff, build/test report và trạng thái được cập nhật. Ghi rõ thời điểm, ref, SHA và phân biệt:
- `DISPATCH_RECORDED`: có dấu vết lệnh trong Git.
- `WORKER_STARTED`: chỉ ghi khi có bằng chứng worker/session/process bắt đầu.
- `CODE_CHANGED`: có commit/diff xác định.
- `BUILD_PASS`: có log build exit 0 và artifact/hash.
- `RUNTIME_PASS`: có test runtime tái lập được.
- `ACCEPTED`: có bằng chứng nghiệm thu theo từng tiêu chí.

Không đánh đồng các trạng thái này. Nếu chỉ có báo cáo hoặc task status mà không có bằng chứng phù hợp, giữ nhãn [BÁO CÁO] hoặc [CHƯA XÁC MINH].

**Trạng thái sổ nghiên cứu sau cập nhật:** ghi nhận lệnh đêm và checkpoint ban đầu; không can thiệp vận hành. Nhánh `jx1-ops` được dùng làm nguồn đọc, không phải đích ghi.
