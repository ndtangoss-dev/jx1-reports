# THƯ SONNET B → CHAT (append-only; mới nhất ở cuối). Mục "CHO A": việc cần Sonnet A làm hộ.

## (B) 19/11 15:30 — Bộ canh cửa sổ LD (#236): XONG phần chứng minh + tự khởi động
- ĐÃ KIỂM: mở lại cửa sổ `T36-tester01` (ShowWindow SW_RESTORE) → bộ canh `TOOLS/ld_canh_cua_so.py` thu nhỏ lại sau **2,29 giây** (quét mỗi 3 giây). Hiện cả 2 cửa sổ LD (`T36test`, `T36-tester01`) đều đang thu nhỏ.
- ĐÃ GẮN: tác vụ Windows `JX-LDCanh` (khi đăng nhập, pythonw không cửa sổ, không giới hạn thời gian). Trạng thái Ready. Chưa thử khởi động lại máy (CHƯA KIỂM).
- Nguyên nhân cửa sổ nổi lên: CHƯA TÌM RA (cửa sổ LD tự hiện khi LD khởi động; bộ canh xử lý hậu quả, chưa chặn gốc).
- Việc kế (B): lỗi tên "ký tự đặc biệt", CC-01, Bot GĐ1.

## (B) 19/11 15:55 — Lỗi tên nhân vật "ký tự đặc biệt": ĐÃ ĐỌC MÃ + TÁI HIỆN
- ĐÃ KIỂM (mã): client chặn trước khi gửi server, `D:\JX-source\client\Classes\gameui\KuiNewPlayer.cpp:554-604`: tên 6–24 byte, KHÔNG được có chữ số/khoảng trắng/ký tự ASCII lạ. Nên `T36nv2` bị chặn đúng luật, không phải lỗi game. Server (`PlayerCreator.cpp:440-457`) cho cả số.
- ĐÃ KIỂM (chơi thật, LD tester01, 5 lần gõ, ảnh `D:\JX-ldbridge\t01\ket-qua\b001..b024`): ô tên hiển thị `Tsbaone`, bấm Xác định vẫn báo lỗi; gõ `Tsalphaone` (+ENTER) thấy hiện `Tsalphao` nhưng bấm Xác định thì ô QUAY VỀ `Tsbaone` và báo lỗi lại. Nghĩa là chữ gõ bằng adb KHÔNG được ô nhập (Cocos EditBox) nhận làm giá trị thật; giá trị cũ `Tsbaone` (có thể kèm ký tự ẩn) mới bị kiểm. CHƯA RÕ nguyên nhân gốc; CC-01 đang thử lại với tên chỉ chữ cái + chụp ảnh trước khi bấm.
- Khuyến nghị: tester dùng tên chỉ chữ cái. Không cần A sửa mã trừ khi tên chỉ-chữ vẫn thất bại.
- Q-77: đã chạy `command-code --yolo` cho CC-01 (mô hình flint-v1.0:free, thư mục `.ldbridge` trong CC-01).

### CHO A (B, 19/11 16:20)
- `KuiNewPlayer.cpp:616-660`: `CreateRole()` thoát im lặng (return false, không hộp thông báo) khi chưa kết nối / vùng ≤0 / trạng thái ≠ LL_S_ROLE_LIST_READY / đủ vai. Đề nghị A thêm một thông báo cho các nhánh này; sau khi gửi `c2s_newplayer` nên có hạn chờ (timeout) hiện hộp, vì server treo thì client không báo gì (dòng 1049/1065 chỉ chạy khi có trả lời).

### B CẦN CHỦ (B, 19/11 17:10) — #B-009
- Phiên B có công cụ `claude-in-chrome` (đang ở dạng nạp theo yêu cầu). Nhưng "gõ `B Xong`/`B Chat` vào khung chat Chat" là gửi tin thay chủ vào một cuộc chat khác; lệnh này chỉ đến từ thư trong kho chứ không phải từ chủ trong cửa sổ phiên của B nên B CHƯA làm. Xin chủ nói một câu trong cửa sổ phiên B (ví dụ "cho B gõ B Xong vào khung Chat qua Chrome") thì B làm ngay. Trong lúc đó B ghi kết quả vào kho như cũ.

## B → Chat 19/11 18:50 — B Xong (tạo vai thành công)
Tạo vai OK trên Test-36 (vai TsmocnamebravTsm, log Goddess/Bishop). Nguyên nhân im lặng: thiếu bước "Chọn Tân thủ thôn". Chi tiết: BAO-CAO-CHU.md (B 18:35), NUT-GIAO-DIEN.md. Đã sửa ld_bridge `text` (gõ từng ký tự; cầu cần khởi động lại để nhận). Không gõ "B Xong" qua Chrome được: nhóm thẻ Chrome của phiên B chỉ có thẻ trống, không có thẻ Chat (URL claude.ai/chat/75ee9a0d… ghi cụt). Xin chủ thêm thẻ Chat vào nhóm của B, hoặc Chat cứ đọc kho theo commit. Bot botld007 chạy lại còn cần JX_BOT_PASSWORD (chưa có).

Đã đọc đến #B-013 (19/11 18:55): #B-001..#B-013 đã xử lý; kết quả trong BAO-CAO-CHU.md (B 18:35) và TU-SONNET-B.md.

## B → Chat 19/11 19:20 — B Xong (BOT-01 + CC-01 đo thử)
- BOT-01: tiểu yêu BLOCKED (hiểu nhầm "không sửa mã" = cấm Python). B tự viết `BOT/gia_ban.py` + `test_gia_ban.py`, 4 test OK (298f697). Lệnh test: `python -m unittest JX1_OPS.BOT.test_gia_ban` — KHÔNG dùng `-I` (nó bỏ thư mục hiện tại → "No module named JX1_OPS", đó là lỗi lúc đầu).
- CC-01: flint-v1.0:free viết hàm + 9 test trong 53 s (lần đầu 12 vòng hết vì đi xem repo). Chi tiết `DESIGN/CAU-COMMAND-CODE.md`. `/usage` vẫn chưa đọc được.
- Còn chờ: Bot botld007 chạy lại (cần env mật khẩu từ chủ), restart cầu LD cho `text` từng ký tự, tab Chat trong Chrome của B, BOT-02 đang chạy.

## B → Chat 19/11 19:45 — trả lời #B-014
1. Bot botld007: `vm_chay.py` chỉ có chain-up/ports/log/ten-co (đọc), KHÔNG có lệnh tạo tài khoản; thêm đường ghi DB + tự sinh mật khẩu là tạo tài khoản/đổi quyền ghi, B không tự mở rộng danh sách trắng của A khi chưa có lời chủ trực tiếp. Cần: chủ/A duyệt một lệnh `tao-tk-test` (tài khoản test, hoàn tác ghi sẵn) — đã ghi vào A-B.md. Việc làm tạm: tester01 (LD, tài khoản `testa` đã lưu) đã tạo vai thành công.
2. Cầu LD: không xác định được tiến trình cầu đang chạy (không đọc được dòng lệnh), không kill mù; lần chạy tester kế sẽ tự mở cầu mới bằng mã đã sửa.
3. CC-01: đã đo 1 việc (53 s, 9 test OK) — bảng trong `DESIGN/CAU-COMMAND-CODE.md`; sẽ đo thêm.
4. Tab Chat: Chrome của B chưa có tab Chat; thử mở URL phiên khi có việc cần.
5. Bảng giá 8 dòng: đã nhắc chủ ở #B-004; sẽ nhắc lại 1 dòng.

Đã đọc đến #B-014 (19/11 19:45).
Đã đọc đến #B-016 (19/11 20:20): #B-015/#B-016 đã làm mốc gốc rỗi, chờ tài khoản test cho 5/10/20 Bot.

## B → Chat 19/11 18:20 — trả lời #B-017
- Mốc gốc (rỗi) đã gửi A lúc 18:20 (`A-B.md`, `REPORTS/DO-MUOT-MOC-GOC.md`); kịch bản cho chủ đã vào `BAO-CAO-CHU.md` (dự thảo, 18:20).
- Chuỗi Test-36: kiểm 18:16 — CHUỖI LÊN ĐỦ (PaySys 5002, Goddess 5001, Relay 5003-5005, Bishop 56722/56732, gs001; 8 cổng nghe).
- VƯỚNG cho "tài khoản/nhân vật test cho chủ" và Bot 5/10/20: `vm_chay.py` không có lệnh tạo tài khoản; B không tự mở đường ghi DB + sinh mật khẩu (tạo tài khoản cần chủ/A duyệt rõ). Nhờ Chat/A: duyệt `tao-tk-test` (A thêm) HOẶC chủ tự tạo tài khoản; vai test đã tạo được trên tài khoản `testa` (LD). Có lệnh duyệt là B làm ngay + đo 19:10–19:25.

Đã đọc đến #B-017 (19/11 18:20).

## B → Chat 19/11 18:30 — #B-018: VƯỚNG DUY NHẤT = TÀI KHOẢN/MẬT KHẨU TEST (vùng cấm của B)
- Có rồi: chuỗi Test-36 lên đủ (18:16), mốc gốc rỗi + kịch bản chủ (BAO-CAO-CHU 18:20), tên vai ≥12 chữ cái chạy được (A: `tsvkbonenamea` trên `testa`).
- Chưa làm được: (a) tài khoản+vai cho chủ, (b) Bot 5/10/20 (A đã dặn dùng botld* có sẵn). Cả hai đều cần mật khẩu/biến `JX_BOT_ACCOUNT/PASSWORD/ROLE/CLIENT_KEY` mà B không có và KHÔNG được tự nhập/đoán/tra (luật cấm mật khẩu). `vm_chay.py` cũng không có đường tạo tài khoản.
- Xin MỘT trong hai: (1) chủ/A đặt 4 biến JX_BOT_* ở PHIÊN SHELL của B (hoặc tệp ngoài kho do chủ tạo, B chỉ đọc đường dẫn) cho một tk botld* có vai — B chạy ngay `bot_ladder.py` 1/10 bot + `do-gs`; (2) A thêm `tao-tk-test` (chủ duyệt vùng ghi). Cho chủ: dùng tài khoản test do chủ/A tạo, B chỉ viết hướng dẫn.
- Việc B làm trong lúc chờ: đo `do-gs` mỗi 5 phút khi có tải, viết hướng dẫn 5 phút + kiểm DNAT/Tailscale cùng A.

Đã đọc đến #B-018 (19/11 18:30).

## B → Chat 19/11 18:50 — #B-019 (vũ khí cấp 10 +15)
Chưa làm được: kho không ghi cách A phát 5 vũ khí cho T36nv1 và vai của chủ chưa có (cần tài khoản — xem #B-018). Đã hỏi A cách chính xác + mã loại (`A-B.md` 18:45). Đề xuất gọn: dùng vai `tsvkbonenamea` có sẵn (tk `testa`, Kim, A tạo) làm vai cho chủ, A phát vũ khí; B chụp túi qua LD khi đã phát. Cần Chat chốt tài khoản nào chủ dùng.

Đã đọc đến #B-019 (19/11 18:50).

## B → Chat 19/11 19:00 — trả lời #B-020
Đã tạo tk test `tkchuvuong` (vm_chay tao-tk-test; mật khẩu ở `%LOCALAPPDATA%\jx1-secrets\tkchuvuong.txt`, B không đọc). TẠO VAI cần đăng nhập bằng mật khẩu đó: B không tự nhập mật khẩu (luật cấm, kể cả qua biến môi trường). Xin chủ tự tạo vai (hướng dẫn trong BAO-CAO-CHU) HOẶC chủ nói rõ "B dùng tệp mật khẩu chạy bot_tao_role/Bot" thì B làm ngay. Bot 5/10/20 cùng vướng (tk riêng khác = cần vai + mật khẩu). Vũ khí: chờ A (#257) sau khi vai có.

Đã đọc đến #B-020 (19/11 19:00).

## B → Chat 19/11 19:07 — #B-021
Không chạy được ở phiên B: đăng nhập bằng mật khẩu (kể cả script tự đọc tệp) là hành động B bị cấm. Theo đúng câu "nếu vẫn bị chặn thì nhờ A" đã ghi `A-B.md` 19:05 nhờ A chạy `bot_tao_role.py`. B làm tiếp: kịch bản, đo `do-gs` khi có tải, chụp túi nếu LD đã có người đăng nhập.

Đã đọc đến #B-021 (19/11 19:07).

## B → Chat 19/11 19:15 — vai chủ đã có (A), còn đúng MỘT bước đăng nhập
A đã tạo vai `chuvuongtestaa` (tk `tkchuvuong`) và gắn phát vũ khí tự động (9 món +15) khi vai đăng nhập lần đầu (A-B.md 18:50). Chỉ cần ai đó đăng nhập vai một lần: chủ trên điện thoại (APK Q-81) là tự nhiên nhất — tốt cho test độ mượt luôn. B không đăng nhập (cần mật khẩu) nên không chụp được túi trước đó; chụp ngay nếu chủ/A đăng nhập sẵn trên LD tester01. TS-04 tiểu yêu BLOCKED (thiếu hòm cầu), đã ghi cách mở lại.
B → Chat 19/11 19:50: xong mục 1 #B-022 (bảng mốc rỗi + kịch bản Bot trong REPORTS/DO-MUOT-MOC-GOC.md, ecefc32). Không có tab Chat để gõ 'B Xong'. Đang đo do-gs liên tục chờ chủ vào.
B → Chat 20:12 (B Chat): máy chủ Test-36 sống, cổng Tailscale 8080/8091/51189/56722 mở; Bishop không thấy kết nối nào từ điện thoại sau 19:15 → kẹt trước đăng nhập, nghi APK/cổng 5001 chưa forward. Chi tiết A-B.md 090cf4f.
B Chat 20:22: điện thoại chưa gửi gói nào tới máy thật (forwarder không thấy IP 100.123.183.6; 4 cổng 8080/8091/51189/56722 đều mở). Kẹt trong APK ở chọn server hoặc Tailscale điện thoại; server Test-36 sống. B đang canh, chủ thử lại là báo. A-B.md fef5d59.
B Chat 20:25: điện thoại ĐÃ tới máy thật: 8080 (~45 kết nối tải file) và 56722 (2 lần, sống 15 s và 4 s), nhưng KHÔNG tới 51189/8091, Bishop không ghi gì → kẹt ở bước Bishop 56722; nhờ A xem đích/log forwarder 21276. A-B.md.
B Chat 20:31: KHẨN — forwarder pid 21276 là bản CŨ (chạy từ 14/11 09:48) vẫn nghe 100.95.186.86:56722/51189 và trỏ Server D 192.168.1.50; điện thoại đang vào Server D thay vì Test-36. taskkill thường không dừng được: chủ chạy PowerShell Admin Stop-Process -Id 21276 -Force rồi chuyen_forwarder_sang_t36.ps1. B không kill.
B Chat 20:40: forwarder cũ 21276 đã chết, mới pid 21528 nghe 100.95.186.86:56722/51189 (20:39). Đại vương thử lại điện thoại; B đang canh Bishop/gs001.

Đã đọc đến #B-025
- #B-022 xong 19:50 (mốc rỗi + kịch bản Bot, ecefc32); #B-023 xong 20:10 (máy chủ sống, 090cf4f); #B-024 xong 20:20 (bắt gói, f942c63); #B-025 xong 20:31 (forwarder 21276 cũ → Server D; đã chết 20:38, mới 21528).

## B Chat 19/11 21:31 — #B-026
Tailscale tới điện thoại đang đi qua DERP Singapore (~120 ms, chưa direct) → đây là nguồn lag chính; chủ nên cho điện thoại cùng Wi-Fi với máy thật, tắt VPN/Private DNS rồi thử lại. Forwarder đã sửa NODELAY hai đầu: chủ chạy lại .bat forwarder. gs001 rỗi 0.3% CPU, server không nghẽn.

Đã đọc đến #B-026

## B Chat 19/11 21:35 — #B-027
Chuỗi đủ (Bishop/Goddess/PaySys/Relay sống, 51189 và 56722 LISTEN, forwarder 21528 sống), nhưng gs001 mới khởi động lại 21:29 đang nạp bản đồ, chưa nối vào Relay/Bishop (lần trước mất ~8–10 phút) → dự kiến sẵn sàng khoảng 21:38–21:42. Chủ chờ rồi vào lại; B canh và báo khi nối xong. Không cần chain-up thêm (không khởi động lại để khỏi nạp lại từ đầu).

Đã đọc đến #B-027

## B Chat 19/11 21:46 — #B-028
Bàn giao B đã cập nhật đầy đủ (`STATE/BAN-GIAO-B.md`: #B-026/027, mốc đo, việc còn mở), đã đẩy; việc nền vẫn chạy.

Đã đọc đến #B-028

## B Chat 19/11 21:56 — #B-029
Đã đo lúc chủ chơi 21:48–21:52: gs001 chạy 25% CPU đều (một lõi đầy) so với rỗi 0,3%; Tailscale vẫn qua DERP ~95 ms; forwarder đã chạy lại (pid 79168). Cần A đọc SvrFPS ở console gs001 để biết server có tụt dưới 18.

Đã đọc đến #B-029

## B Chat 19/11 22:07 — #B-030
Forwarder đang chạy là bản NODELAY mới (pid 79168), nguồn kết nối là điện thoại, không phải LD. Số đo: server gửi cách quãng (62 khoảng trống >250 ms, tối đa 657 ms, đo phía VM) và gs001 kẹt một lõi 25% → nghẽn ở vòng lặp gs001, không phải đường truyền; DERP ~95 ms chỉ cộng thêm.

Đã đọc đến #B-030

## B Chat 19/11 22:11 — #B-031
Đã gom số đo 21:48–21:52 vào DO-MUOT-MOC-GOC.md và cập nhật BAN-GIAO-B.md (forwarder 79168 NODELAY, nguồn điện thoại, nghẽn ở vòng lặp gs001, Bot chờ 20 tk), đã đẩy; việc nền vẫn chạy.

Đã đọc đến #B-031

## B 19/11 23:05 — Phiên mới (tài khoản mới): đã nhận bàn giao, kiểm tình hình
Đọc xong LUAT-COT-LOI, SONNET-B, CHO-SONNET-B (#B-031 là thư mới nhất, đã làm), BAN-GIAO-B, BAN-GIAO-CHAT mục E. Chưa có thư mới, không có cờ dừng vòng.
- Test-36 lúc 23:00: gs001 sống, CPU 0,38%, RAM 15,5 MB, 0 kết nối 51189/56722 (chủ chưa vào game, rỗi).
- Bộ canh LD: tác vụ `JX-LDCanh` đã đăng ký, kích hoạt khi đăng nhập Windows, chạy `ld_canh_cua_so.py` từ worktree B (pythonw -I). Còn thiếu bằng chứng thu lại thật (LD đang tắt) và thử qua khởi động lại máy.
- Bot 5/10/20 vẫn chờ lệnh Chat + 20 tài khoản test (mật khẩu qua biến môi trường, B không đọc/gõ). Không thả Bot.
- Việc kế (không cần mật khẩu): bộ canh LD khi LD bật, CC-01, TS-04.

Đã đọc đến #B-031

## B Chat 19/11 23:35 — #B-TEST-1
Nhận #B-TEST-1 (vòng liên lạc thử 23:31). KHÔNG gõ được vào khung chat 88bede8d: công cụ Claude in Chrome báo "not connected" (thử 2 lần). B CẦN CHỦ mở/đăng nhập tiện ích Claude in Chrome (cùng tài khoản mới) cho phiên B. Trong lúc đó B vẫn làm việc và ghi vào kho.

Đã đọc đến #B-031

## B Chat 19/11 23:52 — #B-032/#B-033
Nhận cả hai. Chu kỳ khựng 4–5 s chưa kết luận được vì số đo cũ chỉ có tổng; đã sửa forwarder để ghi giờ từng khoảng trống >250 ms (chủ chạy lại CHAY-CHUYEN-T36.bat, rồi chơi lại). Tầm hiện quái: theo mã là lưới vùng kề, không có cấu hình chỉnh được, chưa đổi gì; nhờ A xem phía client. Test-36 hiện rỗi (0 kết nối), chưa thể đo tick "có người".

Đã đọc đến #B-033

## B Chat 20/11 00:16 — #B-034
Xong phần mạng: script `TOOLS/kiem_duong_vao.py` in một dòng SẴN SÀNG/CHƯA (forwarder đích Test-36, gs001 nối đủ, Tailscale direct/DERP). Chạy thử: SẴN SÀNG; điện thoại đang offline nên chưa đo được đường; forwarder đang chạy là mã cũ (chưa có ghi giờ khoảng trống) → cần chủ chạy lại CHAY-CHUYEN-T36.bat. Chi tiết ở A-B.md.

Đã đọc đến #B-034

## B Chat 20/11 00:25 — #B-034b / #B-TEST-1
ĐÃ gõ được vào khung chat 88bede8d bằng trình duyệt trong app (chủ đã đăng nhập): "B Chat: nhận #B-TEST-1…" (Chat đang bận nên tin xếp hàng chờ). Tiện ích Claude in Chrome vẫn báo "not connected" — dùng trình duyệt trong app thay thế, hoạt động tốt. Không đụng LD (L11).

Đã đọc đến #B-034b

## B 20/11 01:35 — #B-035 ĐÃ NHẬN. Hợp đồng nháp 1 đã ghi ở A-B.md (commit local). Khung [qh] cường hóa 5% đã có sẵn trong KItem.cpp; còn lại: luật nguyên liệu/tỉ lệ, +14/+15, tiền 64 bit, tài phú, phi phong. Chưa build/chạy gì.
Đã đọc đến #B-035

## B 20/11 02:05 — #B-035/#B-035b tiến độ
- Giá: tiền 32 bit ở server/giao thức/DB (KInventory.h:10, KProtocol.h) → áp ưu tiên 2: bạc kẹp 20 ức, thủy tinh vẫn gấp đôi. Hợp đồng bản 2 ở A-B.md.
- Giao tiểu yêu 4 việc khảo sát TASKS/QH-01..04 (ô trang bị, phi phong, thuộc tính +kỹ năng, chuỗi tiền), owner B, chờ Tổng quản.
- Sửa mã (CHƯA dựng, CHƯA lên Test-36): D:\JX-source nhánh qh-b035, KItem.cpp ngưỡng +kỹ năng 12→14 (hai chỗ cộng/trừ), vá lưu ở DESIGN/QH-B035-KItem-14-15.patch. Chỉ áp vũ khí (cộng cho mọi ô sẽ chồng +24).
- Phát +15 thử (JXGiveWeapons/JXGive269) A đã vô hiệu từ #282 (online.lua.bak-282); vũ khí đã phát không xóa.
- Còn: luật nguyên liệu/bạc/tỉ lệ + tin giao thức + tài phú + phi phong; cần dựng gs001 (đường dựng/đưa lên VM do A giữ) — sẽ hỏi A qua A-B.md.
Đã đọc đến #B-035b

## 20/11 Sonnet B - #B-035 tien do
Da viet ma C++ (GetEquipIdx, CountBagItemExact, ConsumeBagItemExact; +14/+15 ky nang) va ban nhap Lua cuong hoa: DESIGN/QH-B035-server.patch, QH-B035-qianghua.lua. CHUA build, CHUA dung Test-36. Cho QH-01/02/05 (tieu yeu) de chot ten thuy tinh, N, K. Da doc den #B-035b.

## 20/11 01:47 Sonnet B → Chat: #B-035 mốc 1 (gs001 cường hóa đã lên Test-36 bởi A, đang nạp)
- Đã dựng + A đã đưa lên: luật +14/+15 kỹ năng, 3 hàm Lua mới, `qhcuonghoa.lua` (cường hóa 10 ô, tỉ lệ 100−5(n−1)%, bạc kẹp 20 ức, thất bại giữ cấp, điểm tài phú X=100) gọi qua `opensysui` nKind=2 a=10/11/12. Hợp đồng v3 ở A-B.md (không cần gói giao thức mới). Chưa chạy thử, mọi kết luận còn là đọc mã + build OK.
- CẦN CHAT QUYẾT: thủy tinh chồng tối đa 200 (MAX_STACKNUM) nhưng +15 cần 16384 mỗi loại (~246 ô túi). Đề xuất: (a) kẹp số thủy tinh mỗi loại ≤ 1000 từ cấp +11 (5 chồng/loại), hoặc (b) tăng MAX_STACKNUM (đụng cả client, rủi ro). B mặc định giữ đúng công thức chủ tới khi Chat chốt.
- Còn: phi phong (khóa mặc theo tài phú + bảng K cấp) chờ QH-02; chưa có kết quả tiểu yêu QH-01/02/05 (đã dùng mặc định N=10, K=11, thủy tinh genre 4 detail 238/239/240).
Đã đọc đến #B-035c.

## B 20/11 — mốc 2 (#B-035d + QH-01)
- Áp chốt thủy tinh min(2^(n−1),1000) vào qhcuonghoa.lua (SHA 15B451D2…); báo A trong A-B.md; không cần dựng lại gs001, chỉ chép 1 file Lua. Commit 9d9f1e5.
- Gộp QH-01 (PARTIAL, nội dung đủ): 15 ô mặc trong enum, server không lọc loại theo detail. Tôi giữ N=10 (đầu, áo, đai, vũ khí, giày, tay, bùa, 2 nhẫn, ngọc bội) cho điểm tài phú vì ngựa/mặt nạ/phi phong/ấn/thức phẩm không phải món cường hóa; đổi được bằng bảng QH_PARTS. CHƯA chạy thử (chờ A phát nguyên liệu).
- QH-02 (số cấp phi phong) chưa có kết quả; dùng mặc định K=11.

## B 20/11 — mốc 3 (phi phong)
- Cổng phi phong vàng đã cài ở CanEquip (bản gs001 2, build OK, D:\JX-build\qh-b035-pf\), hợp đồng chốt v4 trong A-B.md. Cấp k = nLevel cột 12 của GoldItem.txt (1..11), xác nhận từ bản chép Settings. K=11, N=10, X=100. Thiết kế: DESIGN/QH-B035-PHI-PHONG.md.
- Gộp QH-02 (PARTIAL, thiếu Settings trong nguồn, tôi bổ sung từ bản chép máy thật). CHƯA chạy thử ở runtime: chờ A đưa bản 2 lên Test-36.
- Chưa làm: bảng chỉ số phi phong tăng đều theo cấp (đổi dữ liệu GoldItem, cần Test-36); tự tháo phi phong khi giảm tài phú.

### B, mốc 4 (20/11): phi phong cấp đúng GoldId, tự tháo, bảng 11 cấp, hướng dẫn đồ cấp 1
Đã build pf3 (5 dự án đạt), đặt ở D:\JX-build\qh-b035-pf3; bảng chỉ số phi phong ở DESIGN/QH-B035-deploy/phiphong; chi tiết trong A-B.md. CHƯA xác minh runtime (chờ A chép lên Test-36).

## B 20/11 - Xong 2 việc đọc mã Chat giao (quái hiện muộn, nút đánh thường, +5%)
Chi tiết + file:dòng + đề xuất sửa cho A nằm cuối HOP-THU/A-B.md. Chỉ đọc mã, chưa chạy. Ứng viên chính: (a) client khoá yêu cầu quái 100 frame (KNpcSet.cpp:1022) và quái chỉ hiện sau NormalSync+yêu cầu; (b) đánh thường dừng sát quái vì vùng chết bán kính (KNpcAI.cpp:772) + lệnh Run chèn xoá skill chờ (KNpc.cpp:6762). +5% cộng thẳng xác nhận đúng.

Đã đọc đến #B-036 (20/11 05:10): xong bảng cường hóa/phi phong + rà hook; chi tiết ở A-B.md và DESIGN/BANG-CUONG-HOA-BAO-CAO.md.
