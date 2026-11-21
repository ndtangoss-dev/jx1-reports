# HÀNG ĐỢI VIỆC CỦA SONNET B (Chat lập 19/11 17:10, chủ duyệt 16:37)
Luật: B không chờ thư Chat (L15). Hết việc đang làm thì lấy việc kế trong bảng này; cạn thì tự đề xuất 3–5 việc rồi làm. Việc của A ở `STATE/HANG-DOI-VIEC.md`. Muốn lấy việc ở hàng của A thì nhắn `HOP-THU/A-B.md`, ghi "ĐÃ NHẬN <mã>" ở cả hai bên để không làm trùng. Mỗi việc cha có trường chủ A hoặc B trong `TASKS/<mã>.md` (dòng `owner: A|B`).

| # | Mã | Việc | Ghi chú |
|---|---|---|---|
| 1 | CC-01 | Command Code: chạy trọn luồng, đo tốc độ/độ chính xác so với đám tiểu yêu Codex, `/usage` credits (Q-76/77; DeepSeek để sau, Q-78) | Chỉ trong `D:\JX-wt\CC-01`, mỗi vòng B duyệt |
| 2 | TS | Tester: lượt chấm tốt thứ 2 liên tiếp rồi mới mở tester02 (Q-59, Q-69); thử lại tạo vai Cctesterone, botld007 sau khi chuỗi Test-36 lên | Tên không số/space (client chặn) |
| 3 | E-01, E-09 | Bot: client Python không giao diện, chạy Bot/tester thật vào gs001 Test-36; ca tài khoản đang lỗi thử lại | Bot v1 Q-62 |
| 4 | E-04, E-05, E-06, P-03 | Bot xã hội, Bot trong hoạt động, đo tải, đường cong tải theo số Bot | Làm sau E-01; giao tiểu yêu phần mã |
| 5 | C-01 | Công cụ dòng lệnh quản lý tài khoản (thiết kế + mã offline) | Tiểu yêu làm, B duyệt |
| 6 | LD | Bộ canh cửa sổ LD: thử qua khởi động lại máy, tìm gốc rễ vì sao cửa sổ bật lên | `JX-LDCanh` |
| 7 | BOT-GD1 | Bảng giá mẫu 8 dòng chờ chủ duyệt; nhắc chủ nếu chưa trả lời | Q-62 |
| 8 | TIEUYEU | Tạo việc cho đám tiểu yêu (đang 0 con chạy): mã Bot, công cụ tài khoản, tài liệu tester | `TASKS/*.md`, owner: B |

## NẠP LẠI 22/11 00:40 (L24: luôn ≥10 việc; lấy từ bảng tiến độ + LICH-CONG-VIEC.md) — HÀNG ĐỢI CỦA B
Thứ tự: P0 → P3. Làm từ trên xuống, xong gõ `B Xong` vào khung Chat (L23). Việc 1–8 ở LICH-CONG-VIEC giai đoạn 1 không chạm gs001.
| # | Mã bảng | Việc | Ghi chú |
|---|---|---|---|
| 1 | HT-06 | Đọc nốt sổ tay còn thiếu (AI quái, QUAI-NPC-BAN-DO, BAN-DO-DANH-THUONG-LAN-LENH, S3RELAY, FIX_HISTORY 45–48, SC-004, Q-80/82), bổ sung khối HIỂU GAME | cổng LUAT-RIENG-B |
| 2 | LG-02 | Bảng tra dwID→index trong KNpcSet::SearchID + Describe chỉ khi vùng cần, trong SC-006B, build thử, KHÔNG nạp | P2 cũ, nay làm sớm |
| 3 | LG-03 | Đo tick/băng thông B-02 trước/sau (việc B-04 bị bỏ sót) bằng test đơn vị hoặc VM không người | sau #2 |
| 4 | LG-06 | Đo Obj pool 29466/30000: thành phần, ngưỡng an toàn khi thêm quái/vật phẩm | chỉ đọc |
| 5 | HG | Cập nhật `HIEU-GAME/07-server-luu-tru/SO-TAY-TICK-GS001.md` với bài học visibility.ini Enabled=1 / SearchID O(N) | cộng dồn (L20.4) |
| 6 | S-1 | Lỗi `online.lua` mỗi phút + hook `[TEST-A]` (vòng tick gs001) | sổ tay 07/06 |
| 7 | PP-01 | CHUẨN BỊ phi phong server SC-006: đọc diff build b5 → hiện tại, 11 bộ theo giới (mantle.txt/GoldItem), kế hoạch nạp + đo | chưa nạp; chờ chủ duyệt CH-04 |
| 8 | LG-05 | Kế hoạch 36 Hz + đạn mịn hơn (Q-105) bằng đọc mã/nhánh T4; chưa làm | hoãn |
| 9 | LG-04 | Chuẩn bị công cụ đo gói tin ở forwarder (không chạy) | chỉ khi giật quay lại |
| 10 | PP-03 | Kiểm kê menu/hook thử phía server cần gỡ trước server thật (menu Phi phong/GM, [TEST-A], qh_dump.log) | đọc tĩnh |
| 11 | TIEUYEU | Việc cho tiểu yêu: so 36 Hz cũ vs b11; SearchID callers còn lại | Tổng quản giao |
| 12 | E-01 | Bot client Python không giao diện vào gs001 Test-36 (khi gs001 trống) | việc cũ |

## Nạp thêm 22/11 01:50 (Chat)
| 13 | LG-03 | KẾ HOẠCH THỬ b113 (#B-114): backup, điều kiện nạp, Enabled=0→1, đo HIT/MISS, ngưỡng hoàn tác | chờ 3 bên |
| 14 | CH-03 | Tra log gs001 mất áo +9 của atestqhhai (#B-116), chỉ đọc | |
| 15 | PP-01 | HIỂU GAME phi phong server + kế hoạch nạp + đo (L21) | |
| 16 | HT | Sổ tay 07: bài học SearchID/Describe (đã làm) + kiểm lại các mục CHƯA KIỂM | |
