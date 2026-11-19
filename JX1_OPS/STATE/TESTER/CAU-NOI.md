# CẦU NỐI LDPLAYER (Q-70) — tiểu yêu KHÔNG chạy adb, chỉ thả lệnh vào hòm
Cầu `TOOLS/ld_bridge.py` chạy trên máy thật, chỉ tới ĐÚNG MỘT LD (tester của bạn), chỉ các lệnh dưới đây, mọi lệnh ghi `nhat-ky.log`.
Hòm: `<thư mục cầu>/lenh/` (bạn ghi) và `<thư mục cầu>/ket-qua/` (cầu ghi). Thư mục cầu của bạn ghi ở `PHAN-CONG.md` (cột "Hòm cầu"). Hòm nằm TRONG worktree của tiểu yêu (`<worktree>.ldbridge`, đã loại khỏi git) để sandbox ghi được; KHÔNG dùng thư mục ngoài worktree (TS-03 lượt 1 bị chặn vì vậy).

## Cách gọi
Ghi file `lenh/<id>.json` (id duy nhất, chữ-số-gạch, vd `004`). Đợi ~2 giây, đọc `ket-qua/<id>.json` (`ok`, `out`, `loi`). Chụp màn hình → `ket-qua/<id>.png`.
| Lệnh | Ví dụ nội dung |
|---|---|
| chụp | `{"cmd":"screenshot"}` |
| chạm | `{"cmd":"tap","args":[960,588]}` (màn 1920×1080) |
| vuốt | `{"cmd":"swipe","args":[400,800,400,300,300]}` (ms 50–5000) |
| gõ chữ | `{"cmd":"text","args":["ten_nhan_vat"]}` (ASCII A-Z a-z 0-9 . _ @ -, ≤64) |
| phím | `{"cmd":"key","args":["BACK"]}` (BACK HOME ENTER DEL) |
| mở/đóng game | `{"cmd":"start"}` / `{"cmd":"stop"}` |
| log | `{"cmd":"logcat","args":[200,"JXTRC"]}` |
| đặt lại DNAT | `{"cmd":"dnat"}` (56722/51189/8080 sang máy thật; làm sau khi LD khởi động lại) |
Lệnh khác bị từ chối ("không có trong danh sách trắng"). Không có shell, không có mật khẩu trong lệnh.

## Vào game (đã kiểm 19/11, tester01)
`start` → đợi ~40 s → chạm (960,588), (500,298), (840,772), (686,1016). Túi đồ (680,52). Dùng đồ: chạm 1 lần vào ô → nút "Sử dụng". Chạm ra thế giới sẽ làm nhân vật đi.
Mật khẩu/khóa: KHÔNG ghi vào lệnh hay repo; hỏi Sonnet nếu form cần nhập (dùng ô đã lưu sẵn trong LD).

## Lỗi hay gặp
- `ket-qua` không xuất hiện sau 10 s: cầu chưa chạy → ghi vào TRANG-THAI "CẦU CHẾT", báo Sonnet.
- Màn hình đen/không kết nối được: gửi `dnat`, rồi `stop`, `start`.
- `ValueError`: sai số tham số/ký tự lạ; sửa lệnh.
- Chạm trúng ngoài ý muốn làm nhân vật đi: chụp lại trước khi chạm tiếp.

## Kiểm cầu trước khi làm thật
Gửi `screenshot`, rồi `tap` 1 nút vô hại; có ảnh + `ok:true` mới được nhận việc thật.
