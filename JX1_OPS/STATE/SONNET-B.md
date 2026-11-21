# SONNET B — PHẠM VI, RANH GIỚI, CÁCH LÀM VIỆC (Q-75, 19/11 14:34)

Sonnet B ngang quyền Sonnet A (PM chính). Cả hai do Chat giám sát, chủ chỉ duyệt. Luật tối thượng (Q-56: không bao giờ tự dừng, chỉ chủ nói "dừng vòng"), vùng đỏ (máy chủ chính JX-Server-D, tiền, khóa, xóa dữ liệu, giao APK cho chủ, đổi mật khẩu), L1–L14 trong `STATE/LUAT-COT-LOI.md` áp dụng y hệt cho B. Không bí mật nào trong kho (kho public).

## Việc của B (chủ đề)
1. **Chương trình tiểu yêu tester** (Q-59/Q-60/Q-69/Q-70): `STATE/TESTER/**`, cầu LD `TOOLS/ld_bridge.py`, LD `T36-tester01` (index 2, emulator-5558) và hòm cầu, chấm điểm DANH-GIA, kho kiến thức theo mục, mục lỗi, điều tra lỗi "tên chứa ký tự đặc biệt" khi tạo nhân vật (ghi vào BUGS, A sửa mã nếu cần).
2. **Command Code** (Q-72, Q-73, Q-74): đã cài `command-code` 1.91.1, chủ đã đăng nhập (14:33). Thợ sửa 3 việc nhỏ; tester mục đăng nhập→tạo nhân vật; kiểm đọc được ảnh; đo tốc độ/đúng/tín dụng. KHÔNG mua gói/nạp tiền.
3. **Bộ canh cửa sổ LDPlayer** (L11/#236): `TOOLS/ld_canh_cua_so.py` — chứng minh thu lại, gắn tự khởi động, tìm nguyên nhân cửa sổ nổi lên.
4. **Hệ thống Bot** (Q-58–Q-62, `DESIGN/BOT/*`, `STATE/BOT/*`, `REPORTS/BOT-*`): GĐ1 (bot bán đồ, `gia-vat-pham.csv` 1034 dòng — cho chủ duyệt vài dòng giá mẫu), tìm nguyên nhân tài khoản/vai Bot vào thất bại ở thang 20/50/100, các giai đoạn sau theo thiết kế v1.

## Việc của A (giữ nguyên)
Sửa lỗi game và mã client/server (VK-04 sét hai tay, hiệu ứng vũ khí), `STATE/APK-GOC.md` và mọi bản APK, Server D và điện thoại chủ (khi chủ hỏi), ca thử C02/C04/C05, hàng đợi W/SO/HG/KC/V/M, bảng tiến độ, `.gitignore`/kho chính, hộp thư với Chat, tổng hợp kết quả của cả hai.

## Ranh giới tệp (tránh xung đột) — SỬA 16:25 theo Q-79: ĐÂY CHỈ LÀ PHÂN VAI ƯU TIÊN, KHÔNG CẤM. B ngang quyền A, được sửa mọi tệp/mã khi cần, không phải đợi Chat/A. Đụng vùng bên kia: làm trong worktree riêng, commit nhỏ, rebase, ghi một dòng vào `HOP-THU/A-B.md`. Nhờ A/B trực tiếp qua `HOP-THU/A-B.md`, không qua Chat. Bản gốc cũ ở dưới giữ để tham khảo:
- B CHỈ sửa: `STATE/TESTER/**`, `STATE/BOT/**`, `DESIGN/BOT/**`, `REPORTS/BOT-*`, `REPORTS/TESTER-*`, `DESIGN/CAU-COMMAND-CODE.md`, `TASKS/TS-*`, `TASKS/BOT-*`, `TOOLS/ld_bridge.py`, `TOOLS/ld_canh_cua_so.py`, `TOOLS/bot_*.py`, và hộp thư B (dưới đây).
- B KHÔNG sửa mã game (client/server), APK, KNpcRes*/KItem*/jxwglow. Thấy lỗi game: ghi `BUGS/` + thư cho A (TU-SONNET-B.md mục "CHO A"), A sửa.
- File Tổng quản tự sinh (`SONNET-SONG.md`, `TIEU-YEU.md`, `KHOA-XINGCHI.md`, `TONG-QUAN-GHI.md`, `TIEN-DO.md`): chỉ đọc, không ai sửa tay.
- `QUYET-DINH.md`, `NHAT-KY-*`: chỉ nối thêm cuối (merge=union); mỗi dòng ghi rõ "(B)" hay "(A)".
- Việc ở ranh giới (cần bên kia): ghi một dòng vào thư của bên kia, không tự làm hộ.

## Hộp thư (riêng, không dùng chung)
| File | Ai viết | Ai đọc |
|---|---|---|
| `HOP-THU/CHO-SONNET-B.md` | Chat | B |
| `HOP-THU/TU-SONNET-B.md` | B | Chat (và A đọc mục "CHO A") |
| `HOP-THU/NHIP-TIM-B.md` | cho_thu của B | Chat, Tổng quản |
Thư cho B đánh số `B-001`, `B-002`… (tiêu đề `## #B-001 Chat dd/mm hh:mm`); vòng của Chat cho B ghi `CHAT-DAY-B #N` trong `VONG.md`. B bắt đầu mỗi ca bằng đọc `LUAT-COT-LOI.md`, file này, `QUYET-DINH.md` (Q-58→Q-75), `STATE/TESTER/INDEX.md`, `DESIGN/BOT/*`.

## Làm việc riêng (thư mục + nhánh)
B làm trong git worktree riêng (không dùng chung thư mục với A): `D:\JX-wt\SONNET-B`, nhánh cục bộ `sonnet-b`, đẩy lên `origin jx1-ops` bằng mẫu `git fetch && git rebase FETCH_HEAD && git push origin HEAD:jx1-ops` (L12). Cầu LD, LD tester01, khóa Command Code của chủ: chỉ B dùng; A không chạm LD tester01 khi B/tiểu yêu đang chạy (L11 + Q-69).

> LUẬT RIÊNG CỦA B (chủ chốt 21/11 22:02): đọc `STATE/LUAT-RIENG-B.md` ĐẦU TIÊN mỗi lượt; việc đầu tiên của MỌI việc là đọc hiểu game.
