# BÀN GIAO B (cập nhật 19/11 21:45, trước khi chủ đổi tài khoản)

**Luật tối cao: không tự dừng; chỉ chủ nói "dừng vòng" (STATE/DUNG-VONG.flag). Việc đầu mỗi lượt phải là gọi công cụ. Hết việc: HANG-DOI-VIEC-B.md, rồi `python JX1_OPS/TOOLS/cho_thu.py` (timeout 600000; 10 = thư mới, 11 = gộp tiểu yêu, 12 = chạy lại).**
Đẩy: `git checkout -- JX1_OPS/TOOLS/__pycache__` rồi `python -I JX1_OPS/TOOLS/dong_bo.py --push`. Lấy: `git pull -q --rebase --autostash origin jx1-ops`. Commit kết thúc `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`. Đã đọc đến #B-028 (ghi dòng `Đã đọc đến #B-N` ở `TU-SONNET-B.md`, nếu không hook chặn).
Cấm: mật khẩu (không đọc/gõ/in, kể cả qua script tôi chạy), Main VM 192.168.1.50, tiền, xóa dữ liệu, sửa tường lửa; không thả Bot khi chủ đang chơi mà chưa có lệnh Chat; không kill python lạ.

## Việc test mượt cho chủ (Q-80/81/82)
- Test-36: APK vc22, tk `tkchuvuong`, vai `chuvuongtestaa`, điện thoại xiaomi-13t-pro 100.123.183.6 qua Tailscale tới 100.95.186.86.
- #B-026: Tailscale điện thoại↔PC đi **DERP(sin) ~105–220 ms (≈120), chưa direct** → nguồn lag chính. Cách ép direct: cùng Wi-Fi LAN, tắt VPN/Private DNS, UDP 41641. Máy chủ rỗi 0,3% CPU, không nghẽn. Forwarder `C:\Jx1CocoV3\docs-analysis\scripts	cp_forwarder.py`: socket phía điện thoại NODELAY=0 → đã sửa bật hai đầu (bản gốc `.truoc-b026`). **Chủ phải chạy lại CHAY-CHUYEN-T36.bat** thì forwarder (pid 21528) mới dùng mã mới; chưa xác nhận chủ đã chạy. Chưa đọc được SvrFPS (console gs001 là phần A). Chưa có bảng "lúc chủ chạy/đánh" 10 giây trong `REPORTS/DO-MUOT-MOC-GOC.md` (chủ rời game lúc đo); khi chủ chơi lại: `vm_chay.py do-gs 10` lặp, ghi bảng.
- #B-027: gs001 khởi động lại cần **~8–10 phút nạp map** mới nối Relay/Bishop (21:29→21:37:50). Kiểm bằng `vm_chay.py chain-up | tail` thấy dòng `gs001 da noi du`. Đừng khởi động lại thêm. gs001 chỉ qua JX-ChainUp.
- Mốc đo: rỗi CPU 0,16–0,30%, RAM ~30 MB; chủ chơi 21:06–21:10 CPU 25% (tải map) rồi ~2%.
- Còn mở: Bot 5/10/20 (cần 20 tk test `tao-tk-test` + mật khẩu qua env mà B không cung cấp, và lệnh Chat), chụp túi đồ chủ (cần ai đăng nhập LD), TS-04 mở lại, khởi động lại cầu `ld_bridge` để có `text` từng ký tự, CC-01, C-01/E-01/E-09, bộ canh LD `JX-LDCanh`.

---
# (cũ) BÀN GIAO A → B (Q-75, #243, 14:50)

**Từ đây A không sửa các mảng dưới; cần gì ghi vào mục "CHO B" cuối `HOP-THU/TU-SONNET.md`.**

## 1. Tiểu yêu tester (TS)
- TS-03 lượt 3 đã gộp: ĐẠT MỘT PHẦN (11 lệnh thật qua cầu thứ hai). Lượt 2 = 0 lệnh. Xem `STATE/TESTER/DANH-GIA.md`.
- Khóa/LD: T36-tester01 = emulator-5558, một LD một người điều khiển (Q-69). Hiện có BA cầu `ld_bridge.py` cùng chạy trên 5558: `D:\JX-ldbridge\t01` (của A), `D:\JX-wt\TS-03\.ldbridge` (đã xong, có thể tắt), `D:\JX-wt\CC-01\.ldbridge` (Command Code, xem mục 2). Tắt cái không dùng trước khi giao việc mới.
- Kiến thức: `STATE/TESTER/KIEN-THUC/dang-nhap/{README,NUT-GIAO-DIEN}.md` (tọa độ nút, tật "chạm hai lần").
- Lỗi mở: tạo nhân vật bị báo "ký tự đặc biệt" với tên T36nv2, Tsbaone (đã thử 2 lần). Thử tên khác/đọc mã client lọc tên (`gameui/KSelPlayer.cpp`).

## 2. Command Code
- Đã cài: Node v26.13.1 portable `D:\JX-node\node-v26.13.1-win-x64`, command-code 1.91.1 ở `D:\JX-node\npm-global`; PATH phiên: `D:\JX-node\npm-global;D:\JX-node\node-v26.13.1-win-x64`. Chủ đã đăng nhập 14:33. Free: `flint-v1.0:free`. `status` không in tín dụng.
- Đọc ảnh: ĐÃ KIỂM OK (`D:\JX-cmdc-test`). Ghi chú: `DESIGN/CAU-COMMAND-CODE.md`.
- CC-01 (tester đăng nhập→tạo nhân vật): worktree `D:\JX-wt\CC-01` (nhánh task/CC-01), hòm `.ldbridge` + `NHIEM-VU.md` sẵn, cầu đã chạy. KẸT: không có `--yolo` thì nó không ghi được file lệnh; `--yolo` bị bộ phân loại Claude Code chặn. Cần chủ cho phép (đã ghi BAO-CAO-CHU) hoặc luật quyền Bash; ĐỪNG lách.
- Ba việc sửa nhỏ định giao Command Code: CHƯA chọn (A chưa làm). Gợi ý: sửa tài liệu/nút giao diện, không đụng KNpcRes*/KItem*/jxwglow, không đưa mã private ngoài các file layout/nút.

## 3. Bộ canh cửa sổ LD
- `TOOLS/ld_canh_cua_so.py` (pythonw PID 141016 đang chạy, không tự khởi động khi đăng nhập, chưa gắn vào đường mở LD). Còn thiếu: chứng minh thu lại cửa sổ, tự khởi động, tìm nguyên nhân nổi lên.

## 4. Bot
- Chạy qua `JX1_OPS/BOT/`, `TOOLS/bench/{collect_bot_metrics,bot_ladder}.py`. Đo 1 Bot: `REPORTS/P-02-do-bot-1-nguoi.md`; E-01: `REPORTS/E-01-chay-that.md`.
- GĐ1 bán đồ: `STATE/BOT/gia-vat-pham.csv` (1034 dòng, hệ số bán 0,5 và giá sàn là GIẢ ĐỊNH; cột do_hiem/thanh_thi_ban/nhom_kho_hom_nay trống) + README.
- Tài khoản/vai Bot: `botld001..N`/`BotLdNNN` (tạo bằng `bot_tao_role.py`); mật khẩu, khóa client chỉ qua biến môi trường `JX_BOT_PASSWORD`, `JX_BOT_CLIENT_KEY`. Thất bại vào game ~22% ở thang tải, chưa rõ nguyên nhân.

## 5. Dọn khi xong (Test-36)
Task `JX-Lietke`, `JX-Gui`; CDN tạm `out/cdn-t36.pid`; forwarder PID 190524; `iptables -t nat -F OUTPUT` trong LD; luật tường lửa `JX1-AUTO-T36-56722-51189-host`; `/sdcard/jxtrace`; tắt Test-36 khi hết việc. `D:\JX-node` GIỮ.

## 6. Đồng bộ git (#244)
Dùng `python -I JX1_OPS/TOOLS/dong_bo.py --push` trong worktree của mình (commit trước; script dừng nếu còn file sửa dở). Không `git add -A` các file Tổng quản sinh. Không xóa stash khi chưa `git stash show -p`.
