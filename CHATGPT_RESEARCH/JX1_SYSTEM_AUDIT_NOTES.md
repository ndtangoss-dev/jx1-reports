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
