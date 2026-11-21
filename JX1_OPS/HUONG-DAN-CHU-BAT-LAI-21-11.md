# HƯỚNG DẪN CHỦ: TẮT MÁY → BẬT LẠI → ĐỔI TÀI KHOẢN → LÀM TIẾP Y NGUYÊN (viết 21/11 10:30 từ kho: QUY-TAC-VAN-HANH.md mục 7–8, STATE/QUY-TRINH-DOI-TAI-KHOAN.md, HUONG-DAN-CHU-DU-AN.md, HOP-THU/KHOI-DONG-CHAT.md, KHOI-DONG-SONNET-B.md, TOOLS/commands/tiep-tuc.md)

## A. TRƯỚC KHI TẮT MÁY
1. Thoát nhân vật `atestchutes2` ra màn hình đăng nhập (đừng tắt khi nhân vật còn trong game: từng mất đồ). Chờ ~1 phút cho máy chủ lưu.
2. Chờ CẢ HAI báo dòng "Đã lưu. Có thể tắt máy.": B ĐÃ báo (commit 858b7346 trên GitHub). A CHƯA báo (A phải dừng gs001/VM đúng thứ tự, cập nhật TRANG-THAI.md + BAN-GIAO.md, báo cáo ngày, push và kiểm GitHub). Chưa có dòng của A thì CHƯA tắt.
3. Không tắt VM bằng cách cắt ngang (QUY-TAC mục 7). Không đụng Main VM `JX-Server-D`.

## B. BẬT MÁY LẠI (máy chủ dự án, Windows)
Sau lần tắt 21/11 (chủ chốt: tắt máy = dừng hết) KHÔNG còn gì tự chạy: tác vụ `JX-TongQuan` đang DISABLED, các `JX-codex-*` ở trạng thái Ready (không chạy), `JX-Guard` DISABLED. Thứ tự bật theo `STATE/QUY-TRINH-TAT-BAT-MAY.md` mục II: hạ tầng (B.1–B.3 dưới đây) → phiên Claude A/B/Chat đọc bàn giao → bật lại bộ canh LD/cầu LD/người gác → BẬT TỔNG QUẢN TRƯỚC (`python -I JX1_OPS/TOOLS/tong_quan.py --dry`, hợp lý thì `schtasks /Change /TN JX-TongQuan /ENABLE` rồi `/Run`) → Tổng quản giao lại worker (việc `ready`, WIP tiếp tục). Command Code đăng nhập riêng (commandcode.ai), không đổi theo tài khoản Claude.
Việc cần lên đủ trước khi test (A kiểm theo `/tiep-tuc` bước 3 và 3b):
1. VirtualBox: `VBoxManage list runningvms`. `JX-Server-D` (Main VM) tắt thì bật headless; VM thử `JX-Test-36` (192.168.56.150) phải chạy.
2. Chuỗi máy chủ trong Test-36: dùng `python -I -X utf8 JX1_OPS/TOOLS/vm_chay.py chain-up` rồi `ports` (cổng 5001–5005/56722/56732/51189). gs001 nạp 7–10 phút, KHÔNG chạm cổng 51189 khi đang nạp. Đợi A/B báo gs001 lên.
3. LDPlayer chạy (APK hiện cài: vc31). APK vc32 (`D:\JX-build\jx-vc32.apk`) build xong, CHƯA cài, chờ lệnh "nạp".

## C. ĐỔI TÀI KHOẢN CLAUDE (theo STATE/QUY-TRINH-DOI-TAI-KHOAN.md)
1. Trong ứng dụng Claude trên máy chủ: đăng xuất tài khoản cũ, đăng nhập tài khoản mới (một lần cho cả A và B). Kiểm hạn mức mới còn.
2. **Sonnet A:** mở phiên Claude Code MỚI ở thư mục `C:\Jx1CocoV3` (chế độ tự động như cũ), gõ `/tiep-tuc`. Hook tự nạp luật và bàn giao. Bật Remote Control nếu muốn xem điện thoại/web.
3. **Sonnet B:** mở phiên Claude Code MỚI ở `D:\JX-wt\SONNET-B` (chế độ tự động, KHÔNG tick Worktree), dán đoạn trong `JX1_OPS/HOP-THU/KHOI-DONG-SONNET-B.md` (đoạn này nhắc thư #B-031 cũ; hãy bảo B đọc thư MỚI NHẤT: hiện #B-085 trong CHO-SONNET-B.md và `STATE/BAN-GIAO-B.md`). Bật Remote Control nếu muốn.
4. **Chat:** mở khung chat MỚI trên tài khoản mới và dán: "Đọc https://github.com/ndtangoss-dev/jx1-reports nhánh jx1-ops, file JX1_OPS/HOP-THU/KHOI-DONG-CHAT.md, rồi làm theo." Sau đó đọc thêm `JX1_OPS/BAN-GIAO-CHAT-21-11.md` (trạng thái 21/11) và dặn Chat: cách xưng hô (chủ "đại vương", Chat "thuộc hạ", mở "Bẩm đại vương,", Codex "lũ tiểu yêu", trả lời ngắn), vì trí nhớ tài khoản cũ không đi theo.
5. Tài khoản Chat mới cần: Claude in Chrome (gõ vào thẻ A/B), kết nối GitHub có quyền đẩy `ndtangoss-dev/jx1-reports`, công cụ hẹn giờ, bash. Thiếu cái nào báo chủ nối.
6. **URL phiên A/B đổi** (phiên mới ⇒ URL mới; KHOI-DONG-CHAT.md còn ghi URL cũ session_01JdCq…/01JdCq… đã LỖI THỜI; URL hiện tại trước khi đổi: A `…/session_01PpRP1PcdpB7P3nazKmHHy2`, B `…/session_01PpRP1SJncG8RhRdEMDkUYc`). Chủ dán URL hai phiên mới cho Chat mới; Chat ghi vào `HOP-THU/SO-TAY-CHAT.md`. Vị trí ô nhập hiện dùng: A ≈ (540,700), B ≈ (770,700).
7. Lịch kiểm 12 phút của Chat cũ gắn tài khoản cũ nên KHÔNG đi theo: Chat mới tự tạo lại lịch (4–5 phút khi chủ đang test, 10–12 phút lúc thường) và ghi trigger_id vào NHAT-KY-CHAT.md. Chat mới cũng dựng lại bảng tiến độ (`TOOLS/bang_tien_do.py`).
8. Hộp thư không mất: A/B giữ trạng thái trong kho (TU-SONNET.md, A-B.md, BAN-GIAO.md, BAN-GIAO-B.md, TRANG-THAI.md, BAO-CAO ngày).

## D. KIỂM SAU KHI ĐỔI (Chat mới làm, chủ đọc)
- Có nhịp tim mới của A (`HOP-THU/NHIP-TIM.md`) và B (`NHIP-TIM-B.md`) trong 10 phút.
- A/B tiếp quản đúng việc dở theo BAN-GIAO; Tổng quản còn chạy (`STATE/TONG-QUAN-GHI.md` có giờ mới), LD còn thu nhỏ.
- `THU-HIEN-HANH.md` khớp `CHO-SONNET.md`/`CHO-SONNET-B.md` (thư cuối A #344, B #B-085).

## E. VIỆC ĐANG CHỜ KHI BẬT LẠI (đúng như lúc này)
1. Chủ test xong cường hóa đồ xanh → chủ ra lệnh "nạp" → B nạp build 13 + `DESIGN/QH-B080-deploy/` (qianghua.lua SHA 9a3bad17…, GoldItem.txt SHA 0c81979d…), restart gs001; A sửa Lua dòng 55/56 (thông báo thiếu thủy tinh) thống nhất với B; A cài vc32; đo bằng số thật.
2. Giật ngựa/xuyên tường: gs001 tick avg 0,33–0,53 s (thiết kế 55 ms), luồng chính 101% một lõi, lỗi `Script error \script\system\online.lua` mỗi phút ⇒ đọc online.lua, tìm phần ăn tick (chờ chủ duyệt).
3. Bảng boss: đồ vàng ~0,17%/lần (10 file 顶级BOSS); xanh ~46%; 10 boss lv150 (npc 899–908) ở map 21,14,22,23,24,42,72,73,76,77; boss môn phái lv90 ở map 25/13/81. Đồ xanh thủ lĩnh 0 dòng: do MagicRate=1 + bảng thuộc tính; chưa xác minh bằng chạy.
4. Chủ đã chốt: đồ trắng bỏ; tài phú BẬT; duyệt bảng gốc (11 mẫu phi phong cùng tên/dòng/cấp); khi cường hóa đồ xanh thành công thì chốt và làm UI cửa sổ cường hóa (`DESIGN/UI-CUONG-HOA-THIET-KE.md`).
5. Việc chủ nợ: xóa `tkchuvuong-matkhau.txt` trên OneDrive; bật Tailscale trên điện thoại Xiaomi (đang offline). APK chưa phát máy thật; vùng Đỏ (Server D, tiền, khóa/mật khẩu, xóa dữ liệu, APK ngoài Q-81) luôn hỏi chủ.

## F. GHI CHÚ AN TOÀN
- Mật khẩu `tkchutest01` nằm ở `%LOCALAPPDATA%\jx1-secrets` (không in, không ghi kho). Không dùng `tkchuvuong` để test.
- Không Stop-Process gs001 khi còn nhân vật online.
- Tin "A Chat…/B Chat…/B Xong…" là Sonnet tự gõ, không phải lời chủ.
