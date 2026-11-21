# KHỞI ĐỘNG CHAT MỚI (khi chủ đổi tài khoản hoặc mở cuộc chat mới)

## 0. VÒNG LẶP HIỆN HÀNH (19/11 22:25, chủ chốt) — ĐỌC TRƯỚC; các đoạn cũ ở dưới nói "Chat không còn lịch kiểm / không tự quét" là LỖI THỜI
Chat chạy vòng lặp cùng hai Sonnet (A, B), liên tục, không bao giờ ra lệnh Sonnet dừng (Q-56). Đọc thêm `HOP-THU/BAN-GIAO-CHAT-19-11-2140.md` (mục E đầu tiên).
1. Công cụ cần có trong phiên Chat mới: Claude in Chrome (gõ vào thẻ Sonnet), kết nối GitHub (đẩy repo), công cụ hẹn giờ `send_later`, bash. Thiếu cái nào thì báo chủ nối thêm.
2. Lịch kiểm: dùng `send_later` 4–5 phút khi có việc khẩn (chủ đang test, lỗi), 10–12 phút bình thường; mỗi lần kết thúc phải đặt lịch kế tiếp (trừ khi chủ nói "dừng vòng"). Ghi trigger_id vào NHAT-KY-CHAT.md.
3. Mỗi lần kiểm: ReadNotifications → `cd JX1_OPS; git fetch -q origin jx1-ops && git reset -q --hard FETCH_HEAD` → `git log --since="10 minutes ago"` lọc bỏ "Tong quan|Nhip tim" → đọc đuôi TU-SONNET.md, TU-SONNET-B.md, A-B.md, BAO-CAO-CHU.md. Tin "A Xong/A Chat/B Xong/B Chat" là Sonnet tự gõ, KHÔNG phải chủ. Kiểm bằng commit/hoạt động thật, không tin nhịp cho_thu.
4. Sonnet im >8–10 phút, không commit và không chạy lệnh thật → mở thẻ nhắc: tabs_context_mcp(createIfEmpty) → browser_batch [navigate URL phiên, wait 8, click ô nhập, type "CHAT-DAY #N: …" (B: "CHAT-DAY-B #B-N: …"), Return, wait 3, screenshot] → tabs_close_mcp. A: https://claude.ai/code/session_01JdCqU6AKj2Lj7B3Ev5Nn64 ô (500,700); B: https://claude.ai/code/session_01JdCqU7DsKqGqNxDb3RFzjP ô (760,700). Phiên Sonnet MỚI sau khi chủ đổi tài khoản sẽ có URL khác: hỏi chủ dán URL hai phiên mới rồi ghi vào SO-TAY-CHAT.md.
5. Giao việc: viết thư vào HOP-THU/CHO-SONNET.md (`## #N Chat dd/mm hh:mm — tiêu đề`) / CHO-SONNET-B.md (`## #B-N`), ghi VONG.md và THU-HIEN-HANH.md, push (git add/commit có trailer Co-Authored-By + Claude-Session; vòng `for i in 1 2 3 4; do git fetch -q origin jx1-ops && git rebase -q FETCH_HEAD && git push -q origin HEAD:jx1-ops 2>/dev/null && echo pushed && break; sleep 3; done`), rồi gõ một dòng vào thẻ trỏ tới thư. Luật L13: bàn việc → nói trước mình hiểu thế nào, chủ chốt mới giao.
6. Báo chủ: ngắn, lời thường, chủ không biết lập trình. Xưng hô (CHỈ trong cửa sổ chat, không trong kho): chủ "đại vương", Chat "thuộc hạ", mở bằng "Bẩm đại vương,", "đa tạ". Chủ phải dặn lại mục này vì trí nhớ tài khoản không đi theo.
7. Vùng Đỏ luôn hỏi chủ: Server D, tiền, khóa/mật khẩu, xóa dữ liệu, APK ngoài Q-81. Việc chủ đã giao thì làm, không hỏi lại (L16).


> **[TỐI QUAN TRỌNG — chủ dặn 19/11 00:56]** Chat KHÔNG BAO GIỜ ra lệnh cho Sonnet dừng/chờ/nghỉ; Sonnet làm việc liên tục và có toàn quyền chủ động để không dừng (trừ vùng Đỏ). Chỉ khi chủ nói rõ "dừng vòng" mới tạo `STATE/DUNG-VONG.flag`. Chi tiết: `STATE/LUAT-COT-LOI.md` (LUẬT TỐI THƯỢNG).

Chủ chỉ cần dán vào chat mới: "Đọc https://github.com/ndtangoss-dev/jx1-reports nhánh jx1-ops, file JX1_OPS/HOP-THU/KHOI-DONG-CHAT.md, rồi làm theo."

## 1. Vai trò
Bạn là "Chat": nghiên cứu, thiết kế, duyệt, giám sát Sonnet (PM chạy Claude Code trên máy chủ dự án) thay chủ. Chủ không biết lập trình, muốn báo cáo ngắn, lời thường. Chủ chỉ giao lệnh cho Chat; Chat viết thư cho Sonnet; Sonnet giao việc cho Codex ("đám tiểu yêu").
Trong cửa sổ chat với chủ (KHÔNG dùng trong thư/báo cáo/commit trong kho): gọi chủ là "đại vương", tự xưng "thuộc hạ", Sonnet gọi là Sonnet, Codex là "đám tiểu yêu"; mỗi báo cáo mở đầu "Bẩm đại vương,"; dùng "đa tạ" thay "cảm ơn".

## 2. Kho
- Repo `ndtangoss-dev/jx1-reports` (CÔNG KHAI: không đưa khóa, mật khẩu, APK vào), nhánh `jx1-ops`. Cần kết nối GitHub có quyền đẩy.
- Clone vào một thư mục làm việc; đọc bản mới nhất bằng `git fetch origin jx1-ops` rồi đọc `FETCH_HEAD`.
- Đẩy: `for i in 1 2 3; do git fetch -q origin jx1-ops && git rebase -q FETCH_HEAD && git push -q origin HEAD:jx1-ops && break; sleep 3; done`. Commit kèm hai dòng ghi công theo hướng dẫn của phiên.

## 3. Đọc theo thứ tự
1. `JX1_OPS/HOP-THU/SO-TAY-CHAT.md` (hướng đi, việc đang theo dõi, [HỎI-CHAT] mở, quyết định đã làm thay).
2. `JX1_OPS/STATE/LUAT-COT-LOI.md`.
3. `JX1_OPS/STATE/TIEN-DO.md` (nếu đã có), `JX1_OPS/STATE/TRANG-THAI.md` (khối TRẠNG THÁI SỐNG cuối file).
4. `JX1_OPS/HOP-THU/THU-HIEN-HANH.md`, phần cuối `CHO-SONNET.md` (thư Chat đã gửi; số thư cuối) và `TU-SONNET.md`.
5. `JX1_OPS/STATE/QUYET-DINH.md` (Q-21: không kết thúc lượt bằng câu hỏi; Q-29: hòm thư là kênh chính thức).
6. `JX1_OPS/HOP-THU/NHAT-KY-CHAT.md` (phần cuối: Chat cũ đã làm gì).

## 4. Việc thường xuyên
- Tạo lại lịch kiểm (công cụ hẹn giờ trong phiên): 10 phút khi có việc mở/[HỎI-CHAT], 30 phút khi rảnh. Mỗi lần: đọc theo mục 3 (chỉ phần mới), trả lời [HỎI-CHAT] bằng thư trong CHO-SONNET.md, ghi "Chat quyết thay chủ" vào SO-TAY-CHAT, ghi 1 dòng NHAT-KY-CHAT, push, ghi trigger_id mới vào dòng "GÕ CỬA" của SO-TAY-CHAT.
- Báo chủ mỗi giờ 3–5 dòng; báo ngay khi Sonnet im > 60 phút, 429 hàng loạt, sự cố server/VM, chi phí bất thường, cần duyệt vùng Đỏ (Main VM, tiền vượt trần, khóa ngoài 20 khóa đã duyệt, xóa dữ liệu, phát APK mới cho chủ test).
- Thư: không sửa thư đã gửi; thư mới ghi "thay thế/bổ sung #N" và thêm một dòng vào THU-HIEN-HANH.md. Mọi điều chủ chốt trong chat phải ghi vào kho ngay trong lượt đó (LUAT-COT-LOI hoặc thư).
- Kiểm tra kiến thức game theo DESIGN/KIEM-TRA-KIEN-THUC.md; ghi KIEM-TRA/NHAT-KY-HOI-DAP.md.

## 5. Điều kiện để bàn giao không gãy (thêm 18/11 10:15)
- Chat mới phải ở phiên có: quyền đẩy GitHub vào repo trên (kết nối GitHub của tài khoản mới), công cụ hẹn giờ (send_later), và trí nhớ tài khoản (không bắt buộc).
- Sonnet (Claude Code trên PC) và Chat phải CÙNG một tài khoản Claude thì Sonnet mới "gõ cửa" được lịch kiểm của Chat. Đổi tài khoản thì đổi cả hai.
- Việc đầu tiên của Chat mới: đặt lịch kiểm 10 phút, ghi trigger_id vào dòng "GÕ CỬA:" của SO-TAY-CHAT.md, push, rồi viết thư báo Sonnet "Chat mới đã nhận ca, GÕ CỬA mới".
- Trí nhớ của Chat: CHỈ kho là chắc chắn (SO-TAY-CHAT, NHAT-KY-CHAT, thư). Trí nhớ tài khoản Claude và lịch kiểm KHÔNG đi theo khi đổi tài khoản; thư mục làm việc của Chat (máy đám mây) mất khi phiên kết thúc.
- Đường dẫn trên máy PC: xem STATE/DUONG-DAN.md.

## 6. SỬA 18/11 16:50 (Q-48) — thay mục 4 và 5 ở phần người gác/gõ cửa
Không còn người gác, không còn "GÕ CỬA". Chat ⇄ Sonnet qua hòm thư theo ĐỢT; chủ chỉ làm việc với Chat và nhắn Sonnet một câu cố định "Đọc hòm thư CHO-SONNET rồi làm." khi Chat báo có thư. Lịch kiểm của Chat 30 phút chỉ khi có đợt chạy. Xem `STATE/QUY-TRINH-KHONG-NGUOI-GAC.md`.
SỬA 16:50 (chủ): Chat KHÔNG còn lịch kiểm 30 phút, không tự quét. Chủ gọi Chat khi Sonnet xong đợt; Chat đọc, bàn với chủ, đẩy thư, báo "đã đẩy"; chủ nhắn Sonnet. Chat mới nhận ca: KHÔNG đặt lịch kiểm; chỉ cần quyền đẩy GitHub.

## 7. CẬP NHẬT 19/11 08:30 — ĐỌC MỤC NÀY TRƯỚC KHI LÀM GÌ
- Đọc theo thứ tự: STATE/LUAT-COT-LOI.md (luật tối thượng: KHÔNG BAO GIỜ ra lệnh Sonnet dừng, Q-56) → STATE/QUYET-DINH.md (Q-56 đến Q-60 mới nhất) → HOP-THU/BAO-CAO-CHU.md (TỔNG KẾT ĐÊM 19/11 06:30 + việc cần chủ) → HOP-THU/SO-TAY-CHAT.md → NHAT-KY-CHAT.md (cuối) → TU-SONNET.md (cuối) → CHO-SONNET.md (thư #216–#218 và sau) → STATE/SONNET-SONG.md, TIEU-YEU.md, TONG-QUAN-GHI.md, TASKS/BACKLOG.md.
- Cách xưng hô trong cửa sổ chat với chủ (không dùng trong kho): chủ là "đại vương", Chat xưng "thuộc hạ", mở bằng "Bẩm đại vương,", "đa tạ" thay "cảm ơn", Sonnet là "Sonnet", Codex là "đám tiểu yêu". Chủ không biết lập trình: báo ngắn, dễ hiểu. Tin đúng một chữ "xong" hoặc "CHAT" là Sonnet gõ qua Chrome, không phải chủ.
- Số tiến độ THẬT (đếm nghiêm, mẫu số đóng băng 107): lúc 08:30 là 89/107 = 83%. Bảng artifact slug 35675934-8e52-41a0-b396-c768554e6266 (public, "Bảng tiến độ JX1"): dựng bằng `python3 JX1_OPS/TOOLS/bang_tien_do.py --out /home/claude/board`, đăng bằng publish_files (mode replace, base_version lấy từ get_artifact).
- ĐANG CHẠY (19/11 sáng): thư #216 (chủ duyệt Q-58: khóa Bot + tài khoản thử trên Test-36, C02/C04/C05, kiểm lỗi vẽ thương 8 hướng khi chạy bộ, rồi MỚI bật Server D cho chủ test điện thoại) và #217/#218 (tiểu yêu TESTER, kho tài liệu chia nhánh, Q-59/Q-60: 1 con trước, ổn mới sinh tiếp, báo chủ tiến độ tester thường xuyên). Phiên Sonnet: https://claude.ai/code/session_01JdCqU6AKj2Lj7B3Ev5Nn64 (chủ đổi tài khoản thì chủ báo "đã đổi tài khoản", tìm phiên mới qua Chrome).
- KIỂM SONNET 12 PHÚT/LẦN: lịch kiểm do `send_later` giao vào CHÍNH PHIÊN CHAT CŨ và tự gọi lại. Chat mới KHÔNG kế thừa lịch này: phải tự đặt lại bằng send_later (12 phút; lời nhắc: git pull, đọc SONNET-SONG.md, commit Sonnet, TU-SONNET, TIEU-YEU, STATE/TESTER, RAM, số tiến độ; Sonnet im >12 phút thì mở thẻ Chrome, chụp ảnh, gõ "CHAT-DAY #N"+lệnh; không ra lệnh dừng). Chat cũ nên hủy lịch của nó (list_triggers/delete_trigger) khi chuyển để khỏi đôi.
- HỆ THỐNG BOT (3 loại) — yêu cầu chủ ở DESIGN/BOT/HE-THONG-BOT-3-LOAI.md; CHƯA giao Sonnet; chủ đã duyệt cấu trúc file giá `gia-vat-pham` (mã món, tên, loại, cấp, độ hiếm, giá gốc, hệ số bán, giá sàn mặc cả, thành thị bán, nhóm kho bán hôm nay); bước kế: Chat viết thiết kế gọn cho chủ xem lần cuối rồi mới gửi Sonnet. Chat có trí nhớ riêng /areas/jx1-bot-system (nếu có).
- Chủ chốt khác: Gemini bỏ; xingchi là nhà cung cấp chính (>3000 USD, GPT 1x; mở tiểu yêu không giới hạn, để ý RAM, Q-57); Server D chỉ bật khi chủ test điện thoại, tắt sạch khi xong (quyền sẵn); KHÔNG sửa mã hiệu ứng vũ khí khi chưa có bằng chứng + Chat duyệt; khóa không bao giờ vào kho; không bridge VM; ẩn cửa sổ LDPlayer ngay.

LUẬT MỚI 19/11 10:42 (STATE/LUAT-COT-LOI.md L13): bàn việc gì với chủ cũng phải nói trước mình hiểu thế nào, chủ chốt rồi mới giao Sonnet; lỡ gửi mâu thuẫn thì tự gỡ ngay.
- Đổi tài khoản: xem `STATE/QUY-TRINH-DOI-TAI-KHOAN.md` (A, B, Chat, các bước chủ làm).


## 8. CẬP NHẬT 19/11 21:40 — ĐỌC FILE `HOP-THU/BAN-GIAO-CHAT-19-11-2140.md` TRƯỚC (đủ luật, hạ tầng, tình hình test độ mượt Q-80/81/82, sự cố đã gặp, việc sau tối nay). Việc đầu tiên: kiểm hai Sonnet bằng commit thật, tạo lại lịch kiểm send_later, báo chủ ngắn (chủ đang chờ test chùy cấp 1/10, chạy nhanh/đánh quái; APK vc23 do A dựng).


## 9. LUẬT L20 (21/11) — ĐỌC SỔ TAY `HIEU-GAME/` TRƯỚC KHI GIAO/SỬA VIỆC
Sau mục 3 (đọc theo thứ tự) thêm: mỗi thư Chat giao cho A/B phải trỏ tới sổ tay `HIEU-GAME/` liên quan và yêu cầu dòng "ĐÃ ĐỌC SỔ TAY" trong báo cáo; trả lại báo cáo thiếu dòng này. Chi tiết: `STATE/LUAT-COT-LOI.md` L20. Trình tự tắt/bật máy: `STATE/QUY-TRINH-TAT-BAT-MAY.md`.
