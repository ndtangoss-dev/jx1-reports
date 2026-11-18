# BACKLOG

Sonnet lấy việc từ trên xuống, theo phụ thuộc. Khi bắt đầu một việc, tạo file `TASKS/<ID>.md` từ `_MAU-TASK.md`. Sonnet được thêm, sửa, chia, gộp việc; không được bỏ mục tiêu.

## Giai đoạn 0 – Dựng đội (ngày đầu)

| ID | Việc | Cấp | Ai | Xong khi |
|---|---|---|---|---|
| 0-01 | Tạo bản sao làm việc nhánh `jx1-ops`; chép `TOOLS/commands/*` vào `C:\Jx1CocoV3\.claude\commands\`; áp quyền từ `TOOLS/settings.mau.json` (kiểm cú pháp với bản Claude Code đang dùng; theo D6); chạy Claude Code Setup một lần để rà cấu hình | L1 | Sonnet | `/tiep-tuc` và `/ket-thuc-ca` hiện trong danh sách lệnh |
| 0-02 | Kiểm tra môi trường thật so với `STATE/TRANG-THAI.md`: VM nào tồn tại, VM thử chạy được server tự dựng 36 Hz, LDPlayer, APK hiện tại, Codex CLI, Git Credential Manager. Tạo và điền `JX1_OPS/ENVIRONMENT.md` (dựa trên khung `FABLE_HANDOVER_v0.3/docs/ENVIRONMENT-AND-TOOLS.md`) | L2 | Sonnet | Bảng môi trường có trạng thái thật |
| 0-03 | Thử vòng giao việc: Sonnet gọi `codex exec` chạy nền trong một worktree, với một task nhỏ có ích (ví dụ script sinh bảng trạng thái từ `TASKS/`); đọc kết quả; đo thời gian và hạn mức | L2 | Sonnet + Codex | Một task Codex xong không cần chủ dự án bấm |
| 0-04 | Cài Graphify và dựng đồ thị cho source server và client (bản đã vá); thử các công cụ "có thể cài sau" nếu thấy cần; điền cột kết quả trong `TOOLS/CONG-CU.md` | L2 | Sonnet | Agent tra cứu được đồ thị; bảng có kết quả thật |
| 0-05 | **D1 đã đồng ý:** tạo repository riêng tư `jx1-source`; `.gitignore` chặn PAK, APK, exe, dll, pdb, obj, dump, log, `.sql`, DB, `accinfo.ini`, file cấu hình có mật khẩu; nhập client `D:\Android\b\Client\Classes`, server `D:\JX-build\src18`, Lua và cấu hình đã lọc; quét bí mật; tag `baseline-20261116` | L3 | Sonnet + Codex | Dựng lại được client và server từ repository |
| 0-06 | Trên nhánh `main` của `jx1-reports`: thay `AGENTS.md` bằng con trỏ sang `JX1_OPS/QUY-TAC-VAN-HANH.md` (giữ rào chắn an toàn); ghi chú hết hiệu lực vào `WORKFLOW_JX1.md`, `PROMPTS/00_CODEX_START_HERE.md`, `00_PROJECT_CONTROL/README.md`. **Bỏ hẳn AMOLX (Q-11):** đóng phiên Codex AMOLX nếu còn chạy, ghi trạng thái cuối vào `REPORTS/AMOLX-DONG.md`, không giao thêm việc AMOLX. Giữ nguyên file và báo cáo cũ (không xóa) | L1 | Sonnet | Codex mới mở không còn đọc quy tắc cũ |
| 0-07 | Script một lệnh bật và tắt môi trường thử (VM `JX-Test-36` → dịch vụ theo đúng thứ tự → `gs001` 36 Hz → kiểm tra cổng), kèm kiểm tra sức khỏe; thử qua một lần tắt bật máy | L2 | Codex | Sau khởi động máy, một lệnh đưa môi trường thử về sẵn sàng. Thêm (Q-18): bước đầu script gọi `docs-analysis/scripts/jx_mainvm_ensure.ps1` (bật `JX-Server-D` headless nếu tắt, chờ chuỗi server lên, chỉ đọc) trước khi làm tiếp |
| 0-09 | Dựng các biện pháp mục 11–12: áp hook nhắc sau nén ngữ cảnh và kiểm tra nó chạy thật; thử Codex với `--sandbox workspace-write` trong worktree không ghi được ra ngoài; tạo quy trình khóa `STATE/KHOA.md` | L2 | Sonnet | Thử ghi ra ngoài worktree bị chặn; hook in được lời nhắc (hoặc ghi rõ không hỗ trợ) |
| 0-10 | Đo chi phí Codex thật trên 3–5 task mẫu; đặt trần ngày; ghi vào `STATE/TRANG-THAI.md` mục Ngân sách | L1 | Sonnet | Có số đo hoặc ghi "không có dữ liệu" và trần tạm | [XONG 17/11: số đo trong TRANG-THAI]
| 0-08 | Thử trọn vòng tạm dừng: `/ket-thuc-ca`, đóng Claude Code, mở lại, `/tiep-tuc` | L1 | Sonnet | Làm tiếp đúng việc đang dở |

## Giai đoạn A – Khảo sát, làm chủ

| ID | Việc | Cấp | Ai | Phụ thuộc |
|---|---|---|---|---|
| A-01 | Bản đồ tiến trình server: PaySys, Goddess, S3Relay, Bishop, gs001; cổng; thứ tự khởi động; file cấu hình; log. Tổng hợp từ báo cáo `SERVER/*` có sẵn và kiểm lại trên VM thử | L2 | Sonnet-sub | 0-02 |
| A-02 | Luồng đăng nhập và tài khoản: client → Bishop → PaySys/Goddess → gs001; bảng SQL; `roledb` (định dạng, cách sao lưu) | L3 | Codex | 0-04 |
| A-03 | Kiểm kê cấu hình và script: `gs\script\`, file `.ini`, bảng dữ liệu; mã hóa GBK | L2 | Codex | 0-04 |
| A-04 | Tài liệu kiến trúc tổng (một file) gộp A-01…A-03 và báo cáo cũ, có nhãn tin cậy | L2 | Sonnet | A-01…A-03 |
| A-05 | **Đường đồng bộ thực thể và mọi chỗ người chơi tương tác nhau** trong gs001: gói đồng bộ NPC/người chơi theo vùng, chọn mục tiêu, sát thương diện rộng, tổ đội, giao dịch, PK, chat, xếp hạng, hàm Lua đếm người chơi. Đầu vào cho giai đoạn B | L4 | **Opus** | 0-04 |
| A-06 | Đồng bộ tài liệu `KProtocolDef.h` giữa client và server, ghi bảng gói tin | L2 | Codex | 0-04 |
| A-07 | Gốc rễ crash gs001 tự dựng sau dòng "public net IP": dựng Debug có symbol, bật crash dump / chạy dưới debugger (chỉ trong VM thử), so cờ biên dịch và thư viện với A2T2 chạy được; mục tiêu là dòng mã gây lỗi | L4 | Codex | 0-04 |

## Giai đoạn B – Thử chuyển đổi server

| ID | Việc | Cấp | Ai | Phụ thuộc |
|---|---|---|---|---|
| B-01 | Thiết kế chi tiết bộ lọc hiển thị + chặn tương tác + `visibility.ini` + hàm Lua (theo kế hoạch Phần 5) | L4 | Opus | A-05 |
| B-02 | Cài đặt trong gs001 (branch riêng), dựng, chạy VM thử | L4 | Codex, Opus review | B-01 |
| B-03 | Bộ test tự động hai người chơi + một Bot (5 thử nghiệm ở kế hoạch 2.5), chạy bằng client không giao diện | L3 | Codex | B-02, E-01 sơ bộ |
| B-04 | Đo tick và băng thông trước/sau | L2 | Sonnet-sub | B-02 |
| B-05 | Bật thử Tống Kim với giới hạn do chủ dự án đặt (D4) | L3 | Codex | B-03 |

## Giai đoạn C – Account

| ID | Việc | Cấp | Ai | Phụ thuộc |
|---|---|---|---|---|
| C-01 | Công cụ dòng lệnh: tạo, khóa, mở, đặt lại mật khẩu, xem nhân vật, xem online, đánh dấu bot, sao lưu nhân vật | L3 | Codex | A-02 |
| C-02 | Cờ `is_bot` (vị trí lưu do A-02 quyết) | L3 | Codex | A-02, B-01 |
| C-03 | Trang quản trị web nội bộ, xem được trên điện thoại qua Tailscale | L3 | Codex | C-01 |

## Giai đoạn D – Hoạt động

| ID | Việc | Cấp | Ai | Phụ thuộc |
|---|---|---|---|---|
| D-01 | Bảng hoạt động 5 trạng thái từ script và cấu hình | L2 | Codex | A-03 |
| D-02 | Thử từng hoạt động trên VM thử bằng GM, bổ sung bằng chứng | L2 | Sonnet-sub (LDPlayer) | D-01 |

## Giai đoạn E – Bot (chỉ sau khi B-03 đạt)

| ID | Việc | Cấp | Ai |
|---|---|---|---|
| E-01 | Client không giao diện Python: đăng nhập, vào game, đứng yên (bản sơ bộ dùng cho B-03). **Mốc đầu của Bot (Q-26): 1 Bot đăng nhập, đi, đánh; trần online ban đầu 100** | L3 | Codex |
| E-02 | Hành vi: đi, săn quái, kỹ năng, hồi máu, đổi bản đồ | L3 | Codex |
| E-03 | Bộ điều phối dân số theo bản đồ và giờ | L3 | Codex |
| E-04 | Xã hội theo `DESIGN/BOT/SHARED_BOT_SOCIAL_AND_INTERACTION_SYSTEM.md` | L4 | Opus thiết kế, Codex làm |
| E-05 | Bot trong hoạt động | L3 | Codex |
| E-06 | Đo tải; quyết định có chuyển điều khiển Bot vào trong server không | L4 | Opus |
| E-09 | Chạy BOT/TESTER thật vào gs001 trên VM thử (Config cho phép đúng IP 192.168.56.150, tài khoản thử trong DB VM), kịch bản login→role→vào game; Enabled=1 Solo bằng 2 phiên + bot | L3 | Codex + Sonnet (VM) | E-07, E-08, B-02c |

## Hiệu năng (song song)

| ID | Việc | Cấp | Ai |
|---|---|---|---|
| P-01 | Nhắc chủ dự án thử APK P46/P47 và server 36 Hz trên điện thoại khi tiện; ghi kết quả | L0 | Sonnet |
| P-02 | Bộ đo chuẩn một lệnh (tick, băng thông, khung hình) | L2 | Codex |
| P-03 | Đường cong tải theo số Bot | L3 | Codex (sau E-01) |

## Kiểm tra định kỳ

| ID | Việc | Cấp | Ai | Khi nào |
|---|---|---|---|---|
| O-01 | Phiên Opus mới, chỉ đọc kế hoạch, `QUYET-DINH.md`, backlog và task đã làm; báo việc lệch hướng, task không có mã backlog, quyết định bị làm trái. Ghi `REPORTS/KIEM-TRA-DOC-LAP-YYYY-MM-DD.md` | L4 | Opus | Khoảng 3 ngày một lần, và trước mỗi lần gộp vào `main` |

## Hàng chờ giao khi có chỗ trống (Chat #042, thêm 11:50)
- A-16 khảo sát hoạt động Tống Kim / JoinActivityGroup / trần hiển thị (tĩnh)
- A-17 bảng rơi đồ boss + trang bị theo cấp/giới (tĩnh)
- A-15d..k tách tiếp các phái còn lại nếu A-15a/b/c quá lớn
- T-01..T-07 mỗi kịch bản TESTER một task (đăng nhập, di chuyển, đánh, nhặt, giao dịch, đổi bản đồ, thoát/vào lại)
- E-04 bot xã hội, E-03 nối server
- H-02 dòng chỉ số trang bị; H-03 cường hóa; H-04 gom ghi chép cũ hiệu ứng vũ khí (#046); H-05 UI cường hóa; H-06 ấn; H-07 trang sức/mặt nạ/phi phong; H-08 tài phú; H-09 tổng hợp (#045)
- H-10 phím tắt (đã giao); H-11 nút/cài đặt hệ thống; H-12 tự động chiến đấu; H-09 thêm phần điều khiển và tiện ích (#050)

- J-01 animation nhân vật trần; J-02 animation quái/NPC; J-03 animation kỹ năng (nhóm); J-04 lớp phụ chồng nhân vật; J-05 cơ chế cắt/bỏ khung; J-06 khả năng làm mượt/khung giữa (thư #064); I-06 tổng hợp THE-GIOI-TONG-QUAN (thêm I-07, I-08, mục Animation); H-09 tổng hợp; BASELINE-001 (chờ E-05)

## Hàng chờ chủ chốt (17/11 22:40, chủ duyệt: làm SAU khi hiểu cách vẽ)
- BUG-001 lỗi 1: lớp vũ khí/thân sai thứ tự khi đi bộ (A3a: chỉ đúng hướng chính diện). Chờ DESIGN/QUY-LUAT-VE-BO-PHAN.md hoàn chỉnh (đo bảng đi bộ/chạy/đánh, kiểm khung tuyệt đối vs LineK, kiểm nam). Hoán đổi 8↔9 trong A3a giữ nguyên.
- BUG-002 lỗi 2: khung hiệu ứng set/sét nhảy xa (chưa tái hiện được trên LD).
- A3: xBRZ ×2/×3 (công tắc /sdcard, cache có trần, đo RAM/FPS máy thật), nội suy camera theo giờ vẽ, trộn khung SPR, đo từng phase `Paint()` (H-15). Theo #091: dừng nhánh đồ hoạ sau khi chủ test xBRZ.
- Tổng hợp hiểu game → tối ưu đường truyền → hiểu exe → (chỉ khi truyền ổn) tick/H-15/đồ hoạ nâng cao (#091).

- U-01 (hiểu game), U-02 (truyền tải + exe), U-03 (bảng thứ tự vẽ bộ phận) đang chạy song song (Codex, chỉ đọc). Sau đó mục 8 chỉ khi U-02 kết luận truyền ổn; mục 9 xen kẽ.

## Nhóm bổ sung (17–18/11, #170)

| ID | Việc | Cấp | Ai | Phụ thuộc |
|---|---|---|---|---|
| N-01 | Nghiên cứu nút Bishop Announcer | L2 | Codex/Sonnet | — |
| N-02 | Nghiên cứu Bishop danh sách lọc/VIP/IP | L2 | Codex/Sonnet | — |
| N-03 | Nghiên cứu Bishop Birth role setting | L2 | Codex/Sonnet | — |
| N-04 | Nghiên cứu Goddess Max char, danh sách nhân vật | L2 | Codex/Sonnet | — |
| N-05 | Nghiên cứu Goddess Add Money/EnterMap/Remove/Backup/Restart | L2 | Codex/Sonnet | — |
| N-06 | Nghiên cứu liên kết PaySys-Bishop-Goddess-S3Relay-gs001-client | L2 | Codex/Sonnet | — |
| N-07 | BANG-NUT-EXE-SERVER và thử nút trong VM thử (#161/#162) | L2 | Codex/Sonnet | — |
| K-02 | Kiểm kê asset gốc (chia K-02a..g) | L2 | Codex/Sonnet | — |
| K-03 | Bảng tra cứu (K-03a..e) | L2 | Codex/Sonnet | — |
| R-01 | Chuẩn hóa báo cáo (R-01..R-07) | L2 | Codex/Sonnet | — |
| X-05 | Xưởng JX1 vận hành | L2 | Codex/Sonnet | — |
| V-01 | Vòng tự động Chat⇄Sonnet (Q-48/Q-49) | L2 | Codex/Sonnet | — |
| CL-01 | Thử client C01..C05 | L2 | Codex/Sonnet | — |

## Bổ sung đêm 18–19/11 (#196)

| ID | Việc | Cấp | Ai | Phụ thuộc |
|---|---|---|---|---|
| W-01 | Hiểu đường hiệu ứng vũ khí (xong) | L2 | Codex/Sonnet | — |
| W-02 | Quan sát tái hiện hiệu ứng trên Test-36 | L2 | Sonnet | W-01 |
| SO-01..SO-06 | Sổ tay hiểu game theo mảng (thay G-01..G-06; G-01 cũ đã dùng) | L3 | Codex | — |
| KC-01, KC-02 | Kiểm chéo chất lượng báo cáo (thay V-01; V-01 cũ đã dùng) | L3 | Codex | — |
| HG-01..HG-05 | Hiểu game: đăng nhập, chiến đấu, cấp cường hóa Lua, bảng sort/item, điều chưa kiểm | L3 | Codex | — |
| TK-01 | Theo dõi token/429 (thay T-01; T-01 cũ đã dùng) | L3 | Codex | — |
| M-01 | Bảo trì mục lục/bảng/TASKS | L2 | Sonnet | — |

## Hiểu game (#196, thêm vào bảng 19/11 theo #202)

| ID | Việc | Cấp | Ai | Xong khi |
|---|---|---|---|---|
| SO-01 | Sổ tay hiểu game: nhân vật | L3 | Codex | Có `DESIGN/SO-TAY-*.md`, nhãn nguồn, đã gộp |
| SO-02 | Sổ tay hiểu game: kỹ năng | L3 | Codex | như trên |
| SO-03 | Sổ tay hiểu game: trang bị và bảng item | L3 | Codex | như trên |
| SO-04 | Sổ tay hiểu game: quái, NPC và bản đồ | L3 | Codex | như trên |
| SO-05 | Sổ tay hiểu game: nhiệm vụ và Lua | L3 | Codex | như trên |
| SO-06 | Sổ tay hiểu game: kinh tế (tiền, cửa hàng, rơi đồ) | L3 | Codex | như trên |
| HG-01 | Hiểu game: đăng nhập và vào game | L3 | Codex | Có `DESIGN/HIEU-*.md`, nhãn nguồn, đã gộp |
| HG-02b | Hiểu game: trạng thái chiến đấu và nút đánh (lần 2, có nguồn tuyệt đối) | L3 | Codex | như trên |
| HG-03b | Hiểu game: vì sao cấp cường hóa từ Lua không tới client (lần 2) | L3 | Codex | như trên |
| HG-04 | Hiểu game: bảng item/cường hóa Lua | L3 | Codex | như trên |
| HG-05 | Hiểu game: gộp điều CHƯA KIỂM từ mọi báo cáo | L3 | Codex | như trên |
| KC-01 | Kiểm chéo chất lượng 5 báo cáo đã gộp | L3 | Codex | `REPORTS/KIEM-CHEO-01.md` có đúng/sai/thiếu |
| KC-02 | Kiểm chéo chất lượng thêm 5 báo cáo khác | L3 | Codex | `REPORTS/KIEM-CHEO-02.md` |
| SO-07 | Sổ tay hiểu game: Tống Kim, bang hội và hoạt động | L3 | Codex | `DESIGN/SO-TAY-TONG-KIM-BANG-HOI.md` có nhãn nguồn, đã gộp |
| SO-08 | Sổ tay hiểu game: PK, chết, hồi sinh, hồi máu | L3 | Codex | `DESIGN/SO-TAY-PK-CHET-HOI-SINH.md` |
| SO-09 | Sổ tay hiểu game: đồng bạn và thú cưỡi | L3 | Codex | `DESIGN/SO-TAY-DONG-BAN.md` |
| SO-10 | Sổ tay hiểu game: thời gian, lịch, sự kiện Lua | L3 | Codex | `DESIGN/SO-TAY-THOI-GIAN-SU-KIEN.md` |
| SO-11 | Sổ tay hiểu game: giao diện client | L3 | Codex | `DESIGN/SO-TAY-GIAO-DIEN.md` |
| SO-12 | Sổ tay hiểu game: gói tin client–server | L3 | Codex | `DESIGN/SO-TAY-GOI-TIN.md` |
| HG-06 | Hiểu game: trạng thái, buff, thời gian hiệu lực | L3 | Codex | `DESIGN/HIEU-BUFF-TRANG-THAI.md` |
| HG-07 | Hiểu game: chợ, giao dịch, kho đồ | L3 | Codex | `DESIGN/HIEU-GIAO-DICH-KHO-DO.md` |
| HG-08 | Hiểu game: công thức sát thương | L3 | Codex | `DESIGN/HIEU-CONG-THUC-SAT-THUONG.md` |
| HG-09 | Hiểu game: nạp và chuyển bản đồ | L3 | Codex | `DESIGN/HIEU-NAP-VA-CHUYEN-BAN-DO.md` |
| SO-13 | Sổ tay hiểu game: tài khoản và thanh toán (PaySys) | L3 | Codex | `DESIGN/SO-TAY-TAI-KHOAN-PAYSYS.md` |
| SO-14 | Sổ tay hiểu game: Goddess lưu nhân vật | L3 | Codex | `DESIGN/SO-TAY-GODDESS-LUU-NHAN-VAT.md` |
| SO-15 | Sổ tay hiểu game: S3Relay | L3 | Codex | `DESIGN/SO-TAY-S3RELAY.md` |
| SO-16 | Sổ tay hiểu game: tệp cấu hình gs/Settings | L3 | Codex | `DESIGN/SO-TAY-TEP-CAU-HINH-GS.md` |
| SO-17 | Sổ tay hiểu game: tài nguyên client | L3 | Codex | `DESIGN/SO-TAY-TAI-NGUYEN-CLIENT.md` |
| SO-18 | Sổ tay hiểu game: vòng lặp server | L3 | Codex | `DESIGN/SO-TAY-VONG-LAP-SERVER.md` |
| HG-10 | Hiểu game: cấp, kinh nghiệm, điểm tiềm năng | L3 | Codex | `DESIGN/HIEU-CAP-KINH-NGHIEM.md` |
| HG-11 | Hiểu game: môn phái và kỹ năng khởi đầu | L3 | Codex | `DESIGN/HIEU-MON-PHAI.md` |
| HG-12 | Hiểu game: quái hồi sinh và vật phẩm rơi | L3 | Codex | `DESIGN/HIEU-QUAI-HOI-SINH-VAT-PHAM-ROI.md` |
| HG-13 | Hiểu game: lệnh GM và công cụ quản trị | L3 | Codex | `DESIGN/HIEU-LENH-GM.md` |
