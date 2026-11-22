# BÀN GIAO PHIÊN "CHAT" — 22/11/2026 11:40 (CHỦ RA LỆNH TẠM DỪNG TẤT CẢ)
Đọc 1 lần là tiếp được. Phiên Chat mới: đọc theo thứ tự 1→8. File cũ `BAN-GIAO-CHAT-21-11.md` vẫn đúng phần vai trò/xưng hô/đường push; file này là BẢN CẬP NHẬT.

## 1. Vai trò, xưng hô (không đổi)
Chủ = "đại vương", Chat = "thuộc hạ", mở đầu "Bẩm đại vương,"; trả lời NGẮN, tiếng Việt thường (chủ dùng điện thoại, không phải lập trình viên). Kiểu này KHÔNG ghi vào kho. Chủ: thời gian và token là quý — không dài dòng, không xin lỗi dài.

## 2. Trạng thái: TẠM DỪNG (chủ 11:37)
- Đã tạo `STATE/DUNG-VONG.flag`. A/B/hook thấy cờ thì không làm tiếp. Muốn chạy lại: CHỦ nói rõ "chạy tiếp" → Chat xóa cờ + gửi thư (xem mục 7).
- A và B đã DỪNG từ ~09:59 (nhịp tim cuối 09:59:58): cầu Remote Control đứt (403 từ đêm qua) nên Chat không gõ đánh thức được; chỉ chủ gõ trực tiếp trên máy được. Việc đang làm dở ghi ở mục 4.
- Các lịch kiểm 30–40 phút của Chat (send_later/routine) vẫn có thể bắn: khi thấy DUNG-VONG.flag thì BỎ QUA, không báo chủ.

## 3. Quy tắc làm việc đang hiệu lực (STATE/LUAT-COT-LOI.md v2, 12 điều; QUYET-DINH Q-108..Q-112)
Một kênh thư; đường chính = Phi phong (STATE/DUONG-CHINH.md); làm liên tục không chờ nhau, hàng đợi ≥10; Chat kiểm mỗi 30'; ĐI TỪ GỐC LÊN (Q-112, điều 6): đọc mã gốc, ghi tệp:dòng, phân biệt "GỐC" và "DỰ ÁN TẠO", cấm sửa ngược hệ thống gốc cho hợp cái mới; chép Lua/dữ liệu lên VM: nguồn trong kho + SHA + .bak (điều 9); tiết kiệm token (Q-110): nén ngữ cảnh 20%, vòng chờ im lặng, đọc thư phần mới. Trước khi thêm luật: dò luật cũ rồi gộp (đừng thêm điều mới chồng).

## 4. Phi phong — tình hình
- XONG: nút nhận 15000 tài phú trong Hỗ trợ test (không cổng tên; thay mục #370 en9, hàm `qhbv_tp15000`, cộng +15 cho món đang mặc); nhãn [cấp N] đúng (bản APK **vc44**, sửa `KItemGenerator.cpp` GetGoldItemByIndex/ByRong, đã đạt trên LDPlayer, ảnh `REPORTS/385/pa2_vc44_cap.png`); dữ liệu 11 bộ B làm xong: `DESIGN/QH-B128-deploy/phiphong/GoldItem.txt` (SHA dbd525b8…, tên có dấu, nLevel 1,1,2,3,3,4,4,4,5,5,5) + `GoldMagic.txt` (có 55 dòng QHPP, SHA e676190a…); server có sẵn Lua `SetTestWealth(n)` (chỉ Test-36).
- CHƯA NẠP gs001 (đang cũ từ 22:15 21/11): chủ ĐÃ DUYỆT restart (Q-111) lúc 09:54 và đã thoát game; B chưa kịp nạp vì dừng. Nạp = checkpoint-b119c (CoreServer.dll, nhánh sc-006b) + GoldItem + GoldMagic QHPP, MỘT lần (thư #B-130/#B-131). Sao lưu .bak-130 trước, kiểm không còn người online, giữ Server D, tick ổn định ~0.85–1 ms, lỗi thì trả .bak.
- ĐANG CHỜ, CHƯA LÀM: (a) tooltip đủ dòng thuộc tính 10 bộ (cần nạp); (b) tên "Ngạo tuyết" có dấu (cần nạp); (c) nhãn xanh `<Phá quân>` cạnh tên nhân vật khi đổi phi phong — chủ nói danh hiệu LUÔN gắn cùng phi phong theo logic gốc. A đề xuất 11 dòng `playertitle.txt` + server đặt title theo bộ mặc (A-B 10:50, TU-SONNET 09:59) — Chat CHƯA DUYỆT: chủ yêu cầu đi từ gốc; đã hỏi A (#391) và B (#B-133): danh hiệu/phi phong gốc có nối nhau thế nào, và mọi thứ A/B làm từ 21/11 là GỐC hay DỰ ÁN TẠO (ghi `REPORTS/391-GOC-PHI-PHONG.md`, `REPORTS/B133-GOC-PHI-PHONG.md`). Chưa có câu trả lời.
- Điều Chat tra được (chưa đọc mã gốc, mã nằm trên máy chủ không ở kho): GỐC = 11 dòng GoldItem 3467–3477, ảnh pifeng_01..11, nLevel, yêu cầu loại 36=60; bản gốc CHỈ dòng Lăng Vân có 6 mã GoldMagic, 10 dòng sau trống. DỰ ÁN TẠO = điểm tài phú ảo 100×tổng cấp cường hóa 10 món + ngưỡng 6000…15000 (QH-B035/B039, `QhCheckPifeng`), 55 dòng QHPP, bản B080 chép 6 mã cho cả 11 dòng. Báo cáo H-08:144: gốc không có luật "đủ X tài phú → phi phong cấp Y". Quyết định chủ còn treo: `QH_PIFENG_ALL_LINES` (0 = luật gốc dòng 1/3/5 theo nActive).

## 5. Hạ tầng (đã xác minh)
VM Test-36 (192.168.56.150), gs001 tick ổn (visibility.ini Enabled=0); forwarder Tailscale 100.95.186.86 (APK cổng 8091). KHÔNG khuyên chủ tắt VPN (là Tailscale). Server D (Main VM) TUYỆT ĐỐI không đụng. APK mới nhất: vc44 (chưa ra máy thật; chủ tự cài; vc42 link artifact https://claude.ai/artifact/AHTk5zbr5Ycxs4nrMgxsur). Cài đặt nén: A đã áp (DISABLE_1M gỡ, hook do_context); B bị hệ thống chặn tự sửa `settings.json` → CHỦ tự áp mẫu `TOOLS/settings.mau.json` cho cửa sổ B (nén 20%). Nhớ đổi 30→20 ở A (thư #388).

## 6. Việc chủ phải làm (tay chủ)
1. Gõ vào cửa sổ B: `Đọc thư #B-130, #B-131, #B-133 rồi nạp gs001 ngay (chủ đã thoát game).` — chỉ khi chủ nói "chạy tiếp".
2. Gõ vào cửa sổ A: `Đọc thư #389, #390, #391 rồi làm tiếp.` Ô "Cửa sổ ngữ cảnh đã đầy" → bấm "Nén phiên" (không bấm "Tua lại").
3. Remote Control đứt: đăng xuất/đăng nhập lại app Claude (tuỳ chọn, chưa chắc hiệu quả). Đừng làm khi A/B đang lưu việc.
4. Hộp thoại "Windows PowerShell Credential Request" từ 192.168.56.150: bấm Cancel; chủ KHÔNG nhập mật khẩu qua Chat. Sửa: `TOOLS/chep_lua_vm.ps1` phải báo lỗi thay vì hỏi (thư #387, chưa rõ đã sửa).
5. Quyết định chờ: `QH_PIFENG_ALL_LINES` 0/1; nạp b119c (đã duyệt, chưa làm); xóa/ cất thư cũ (CHO-SONNET 513 KB, A-B 411 KB, TU-SONNET 268 KB) sau Phi phong.

## 7. Chạy lại (khi chủ nói "chạy tiếp")
`git fetch -q --depth=50 origin jx1-ops && git reset -q --hard FETCH_HEAD`; `git rm STATE/DUNG-VONG.flag`; sửa `STATE/DUONG-CHINH.md` (tạm dừng → Phi phong tiếp); gửi thư ngắn A/B; nhắc chủ gõ 2 câu ở mục 6. Đẩy: sau commit (trailer `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>` + `Claude-Session: …`) → tối đa 4 lần `git fetch … && git rebase -q FETCH_HEAD && git -c push.negotiate=true push -q origin HEAD:jx1-ops`. Bảng tiến độ: `python3 -I TOOLS/bang_tien_do.py --root <kho>/JX1_OPS --out /home/claude/board`, rồi `get_artifact` lấy `base_version`, `publish_files` index.html vào slug `28a7bee8-01e2-4cc2-be1e-b09c40d3b600` (link xem trên điện thoại https://claude.ai/artifact/62BEjdHFr4icZMErbcH7io).

## 8. Điều tuyệt đối không làm
Nhập/xử lý mật khẩu, khóa API; để khóa/email vào kho (kho CÔNG KHAI); đụng Server D/Main VM; khuyên tắt Tailscale; ra lệnh A/B dừng khi chủ chưa nói; gọi "XONG" khi chưa có ảnh/số; né quyền khi hệ thống chặn (delete_trigger bị chặn, computer-use không mở được app Claude — không vòng qua). Vùng Đỏ luôn hỏi chủ: Server D bật/tắt, tiền/VPS, khóa/mật khẩu, xóa dữ liệu, APK ra máy thật ngoài lệnh chủ, Main VM.
