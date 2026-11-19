# QUY TRÌNH ĐỔI TÀI KHOẢN CLAUDE (Chat + Sonnet A + Sonnet B) — viết 19/11 15:35 theo lệnh chủ

Mục đích: khi tài khoản hết hạn mức hoặc chủ đổi tài khoản, dự án KHÔNG gãy. Chủ chỉ làm các bước đánh số; phần còn lại các bên tự đọc kho. Kho `jx1-ops` giữ MỌI trạng thái nên không mất việc.

## 0. Cái gì KHÔNG phụ thuộc tài khoản (không cần làm gì)
- Toàn bộ kho (luật, quyết định Q-xx, thư, báo cáo, bàn giao `STATE/BAN-GIAO.md`, `BAN-GIAO-B.md`).
- Tổng quản (tác vụ Windows), bộ canh LD `JX-LDCanh`, cầu LD, LD, máy ảo, Server D, khóa xingchi, đám tiểu yêu Codex đang chạy.
- Command Code: đăng nhập riêng ở trang commandcode.ai (gói Go), không đổi theo tài khoản Claude.
- Khóa/mật khẩu trên máy chủ (không bao giờ nằm trong kho).

## 1. Cái gì GẮN với tài khoản Claude (phải làm lại)
- Trí nhớ riêng của Chat (cách xưng hô, luật thường trực): tài khoản mới KHÔNG có. Xem bước 4.
- Lịch kiểm 12 phút của Chat (gắn với khung chat cũ): phải tạo lại ở khung chat mới.
- Remote Control (xem phiên trên điện thoại/web): bật lại cho từng phiên.
- Kết nối GitHub của Chat: nối lại (cần quyền đẩy vào `ndtangoss-dev/jx1-reports`).
- Bảng tiến độ (artifact) thuộc tài khoản cũ: Chat mới tạo lại bảng bằng `TOOLS/bang_tien_do.py`.

## 2. Các bước chủ làm (theo thứ tự)
1. Báo trước (không bắt buộc): nhắn Chat cũ "sắp đổi tài khoản" để Chat cập nhật `HOP-THU/NHAT-KY-CHAT.md`/`VONG.md`. Quên cũng không sao, kho đã đủ.
2. Trong ứng dụng Claude trên máy chủ: đăng xuất tài khoản cũ, đăng nhập tài khoản mới (một lần cho cả A và B vì cùng ứng dụng). Kiểm hạn mức tài khoản mới còn.
3. **Sonnet A:** mở phiên Claude Code mới trên thư mục `C:\Jx1CocoV3` (chế độ tự động như cũ), gõ `/tiep-tuc`. Hook tự nạp luật và bàn giao. Bật Remote Control nếu muốn xem điện thoại.
4. **Sonnet B:** mở phiên Claude Code mới trên thư mục `D:\JX-wt\SONNET-B` (chế độ tự động, KHÔNG tick Worktree), dán đoạn trong `HOP-THU/KHOI-DONG-SONNET-B.md`. Cấu hình B (biến `JX1_SONNET=B`) đã nằm sẵn trong thư mục nên không phụ thuộc tài khoản. Bật Remote Control nếu muốn.
5. **Chat:** mở khung chat MỚI trên tài khoản mới và dán: "Đọc https://github.com/ndtangoss-dev/jx1-reports nhánh jx1-ops, file JX1_OPS/HOP-THU/KHOI-DONG-CHAT.md, rồi làm theo." Sau đó chủ nhắc Chat cách xưng hô riêng với chủ (tài khoản mới chưa biết). Chat mới sẽ: kiểm hai Sonnet, tạo lại lịch kiểm 12 phút, dựng lại bảng tiến độ, báo chủ tình hình ngắn.
6. Khung chat cũ: chủ nói với Chat cũ "chuyển khung mới" nếu còn dùng được để nó hủy lịch kiểm cũ (nếu không hủy được thì lịch cũ tự mất khi tài khoản cũ hết, không gây hại).

## 3. Kiểm sau khi đổi (Chat mới làm, chủ chỉ đọc kết quả)
- Có nhịp tim mới của A (`HOP-THU/NHIP-TIM.md`) và B (`NHIP-TIM-B.md`) trong 10 phút.
- Hai Sonnet tiếp quản đúng việc dở theo `BAN-GIAO.md` / `BAN-GIAO-B.md`; số thật x/124 không lùi.
- Tổng quản còn chạy (`STATE/TONG-QUAN-GHI.md` có giờ mới), LD còn thu nhỏ.
- Không có thư nào bị bỏ sót: `THU-HIEN-HANH.md` khớp `CHO-SONNET.md` / `CHO-SONNET-B.md`.

## 4. Mặc định cho Sonnet khi đổi tài khoản giữa chừng
- Không dừng (Q-56). Việc đang chạy nền (build, tiểu yêu, Command Code) cứ chạy.
- Trước khi hết hạn mức: cập nhật bản bàn giao (việc dở, lệnh đang chạy, điều chưa kiểm), commit + đẩy bằng `TOOLS/dong_bo.py`.
- Nén ngữ cảnh tự động xảy ra trong cùng một phiên (hook PreCompact ghi bàn giao); đổi tài khoản là phiên MỚI nên cần bước 3–4 ở trên.
- Vùng đỏ không đổi: không tự mua, không đụng Server D, không đưa khóa/APK vào kho.
