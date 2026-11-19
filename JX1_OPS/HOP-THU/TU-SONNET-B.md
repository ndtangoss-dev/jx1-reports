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
