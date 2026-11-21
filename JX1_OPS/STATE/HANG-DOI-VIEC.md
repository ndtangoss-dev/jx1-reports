# HÀNG ĐỢI VIỆC KHÔNG-ĐỎ (Chat lập 18/11/2026 22:30; Sonnet làm theo thứ tự, KHÔNG BAO GIỜ hết việc)
> 19/11 17:10: ĐÂY LÀ HÀNG ĐỢI CỦA SONNET A. Của B: `STATE/HANG-DOI-VIEC-B.md`. Việc cha của A: A-07, A-07b, A-07c, B-02, B-04, CL-01, D-02, T-04, M-01, P-01, 0-08, O-01. Chờ chủ: B-05, X-05, C02/C04/C05.

Luật (Q-52): Sonnet không gõ "xong" vì "hết việc". Hết việc đang làm thì lấy việc kế tiếp trong hàng đợi này; hàng đợi cạn thì tự đề xuất 3–5 việc "hiểu game" mới từ mục "chưa kiểm" của các báo cáo (ghi vào cuối tệp này, đánh dấu [SONNET-THÊM]) rồi làm. Mỗi việc: tạo `TASKS/<mã>.md` để Tổng quản giao tiểu yêu; việc cần sửa mã hoặc chạm vùng Đỏ thì KHÔNG làm, ghi [CAN-CHU]. Việc đọc tĩnh, viết tài liệu, kiểm chéo, và thử trên `JX-Test-36` (trong phạm vi đã duyệt) là làm được. Báo cáo viết bằng lời thường, mỗi điều ghi nhãn THẤY / TÀI LIỆU / CHƯA KIỂM, kèm file:dòng.

## Nguyên tắc chủ chốt (Q-52): HIỂU RỒI MỚI SỬA
Chủ và Chat thống nhất: hiệu ứng vũ khí sửa mãi không được vì chưa hiểu đủ. Từ giờ KHÔNG sửa mã hiệu ứng (client lẫn server) cho tới khi có tài liệu "hiểu" được Chat duyệt. Mọi lỗi hiển thị: mô tả, tái hiện được, giả thuyết có thể kiểm — rồi mới đề xuất sửa.

## Hàng đợi (thứ tự ưu tiên)
| # | Mã | Việc | Đầu ra | Ghi chú |
|---|---|---|---|---|
| 1 | W-01 (XONG 18/11 23:40: a-d đã gộp, `DESIGN/HIEU-HIEU-UNG-VU-KHI.md`) | **Hiểu trọn đường hiệu ứng vũ khí:** từ dữ liệu vật phẩm/ini → client nạp → NPC res → thứ tự vẽ → glow (+6/+12/+15) → sét dọc → khung/animation. Gộp H-04, H-14, BUG-002, L-01..L-03, J-01..J-05, K-02-* | `DESIGN/HIEU-HIEU-UNG-VU-KHI.md`: sơ đồ mermaid, bảng "ai vẽ cái gì, theo thứ tự nào, đọc tệp nào", danh sách giả thuyết lỗi mỗi giả thuyết có cách kiểm | KHÔNG sửa mã. Chia 3–4 tiểu yêu theo khúc (dữ liệu, nạp/res, vẽ/thứ tự lớp, animation) rồi gộp |
| 2 | W-02 (XONG phần quan sát 19/11) | Kế hoạch tái hiện lỗi mất khung/nhảy khung trên Test-36 (LDPlayer) khi C01 đã chạy: các bước, ảnh/quay màn hình, số đo | `DESIGN/KE-HOACH-TAI-HIEN-HIEU-UNG.md` | Chạy sau C01; chỉ quan sát |
| 3 | SO-01..SO-06, HG-01..HG-05, KC-01, KC-02 (thay G-01..G-06; #196) | **Sổ tay hiểu game theo mảng** (nhân vật, kỹ năng, trang bị, đăng nhập, chiến đấu, bảng item, cường hóa Lua). 19/11 00:30: SO-01..03, HG-01, HG-04 đã gộp; **HG-02b, HG-03b** (làm lại có đường dẫn nguồn tuyệt đối), HG-05, KC-01, KC-02, SO-04..06 đang chạy | `DESIGN/SO-TAY-*.md`, `HIEU-*.md` | Tiểu yêu làm; Sonnet gộp khi XONG-CHO-GOP |
| 4 | V-01 | **Kiểm chéo chất lượng:** chọn 5 báo cáo đã gộp (ưu tiên H-04, A-05, K-02-nhan-vat, N-0x, R-07a), đối chiếu từng khẳng định có file:dòng với mã thật, đếm sai/thiếu | `REPORTS/KIEM-CHEO-01.md` | Phát hiện báo cáo sai trước khi tin tiếp |
| 5 | TK-01 (thay T-01; XONG 19/11: 7 nhật ký, 0 lần 429, 7 Upstream, token vào TB 2,71 triệu) | Theo dõi giảm token sau Q-51/#195 | `REPORTS/TIEU-YEU-TOKEN-THEO-DOI-01.md` | Lặp lại mỗi sáng nếu còn đáng đo |
| 6 | M-01 | Bảo trì: cập nhật mục lục tri thức, bảng tiến độ, dọn TASKS lệch trạng thái | commit nhỏ | Mỗi đợt |
| 7 | C-02..C-05 | Ca thử client C02, C04, C05 | — | CHƯA duyệt; chỉ làm khi Chat báo chủ duyệt |

## Việc Sonnet tự thêm
Làm được ngay (Sonnet, không chờ tiểu yêu): (a) #193 còn lại: SHA APK trong T36test, quay video H4/H5; (b) V-01 kiểm chéo 5 báo cáo; (c) M-01 mục lục/bảng tiến độ mỗi đợt; (d) gộp XONG-CHO-GOP khi có; (e) #199 các đề xuất bằng mã.
Chờ tiểu yêu: HG-02b, HG-03b, HG-05, KC-01, KC-02, SO-04..06 (8 việc đang chạy, tối đa 2/khóa, 5 khóa).
Chờ chủ duyệt: C-02, C-04, C-05; #134; Xưởng JX1; nhân vật thứ 4.
- V-01 lượt 2/5 (H-04): KIEM-CHEO-03.md, 4/4 đúng (đã sửa ghi nhầm lệch dòng).
- V-01 lượt 3/5 (A-05): REPORTS/KIEM-CHEO-04.md, 6/6 đúng. Còn K-02-nhan-vat, R-07a.
- V-01 lượt 4/5 (K-02-nhan-vat): REPORTS/KIEM-CHEO-05.md, 3/3 mốc đúng. Còn R-07a.
- V-01 XONG 5/5 (19/11): KIEM-CHEO-06.md (R-07a đúng); tổng không sai nội dung, lệch dòng chỉ ở E-01.

## Thêm 21/11 17:05 (A, #347): lấp chỗ thiếu HIEU-GAME cho tiểu yêu (1 con trước, Q-59/60)
| # | Việc | Đầu ra |
|---|---|---|
| S-1 | Vòng tick gs001 + `online.lua` mỗi phút lỗi + giật ngựa (sổ tay 07/06 chưa có) | HIEU-GAME/07-server-luu-tru/SO-TAY-TICK-GS001.md |
| S-2 (XONG 21/11, SO-TAY-NHAN-CAP.md) | Nhãn "[cấp N]" trên tooltip trang bị/phi phong lấy từ đâu (client) | HIEU-GAME/01-trang-bi-cuong-hoa/SO-TAY-NHAN-CAP.md |
| S-3 (XONG 21/11, bảng lệch mục 5) | Glow vũ khí: đối chiếu qh9A vs Client2912 (HIEU-HIEU-UNG-VU-KHI vs HG-03c) | sửa HIEU-HIEU-UNG-VU-KHI.md thêm bảng lệch |
| S-4 (XONG 21/11) | Mục CHƯA KIỂM/chỉ-đọc-mã của DO-CHAC.md: cường hóa, phi phong, ngựa/giật, boss rơi đồ | cập nhật DO-CHAC.md |

## NẠP LẠI 22/11 00:40 (L24: luôn ≥10 việc; lấy từ bảng tiến độ + LICH-CONG-VIEC.md) — HÀNG ĐỢI CỦA A
Thứ tự theo lịch (Q-107: cường hóa trước, phi phong sau). Làm từ trên xuống, xong gõ `A Xong` vào khung Chat (L23); dưới 10 việc thì tự báo Chat nạp thêm.
| # | Mã bảng | Việc | Ghi chú |
|---|---|---|---|
| 1 | CH-03 | 4 việc nhỏ UI cường hóa: giữ trang bị ở ô giữa sau cường hóa; chữ thanh tiền chồng icon xu; ảnh e (thiếu bạc); ghi link APK | thư #364 |
| 2 | CH-03 | Ghi URL tải APK vc37 (Tailscale 8080/8091) + 3 dòng cài đặt vào BAO-CAO-CHU.md, kiểm tải được từ máy chủ | Chat không thấy artifact "Link APK vc37" |
| 3 | CH-02 | Rebuild vc38 nếu sửa UI; giữ SHA256 | sau #1 |
| 4 | LG-07 | Đo khung >40 ms trên LD khi đi map 15 phút; xác nhận [fix36] dọn texture đúng trong vc37 | không chạm gs001 lâu — XONG 1 bản đồ 22/11 (08-giao-dien/LG-07-DO-KHUNG-HINH-LD.md); fix36 chưa xác nhận |
| 5 | HG | Retest #359 (sách hỗ trợ cường hóa) bằng vai khác atest; #354 bot/relog tự chạy chưa kiểm | |
| 6 | HG | Cập nhật sổ tay `HIEU-GAME/08-giao-dien/` với cơ chế cửa sổ cường hóa vc37 (KuiGiveVN/buildQhPanel, banner qua KuiChatList) | công sức cộng dồn (L20.4) |
| 7 | PP-03 | Kiểm kê menu/hook thử phía client + Lua cần gỡ trước server thật (hotrotanthu, qh_bothu, baowubox, [SC-006]) | đọc tĩnh, ghi danh sách — XONG 22/11 (HIEU-GAME/09-cong-cu-gm/PP-03-KIEM-KE-HOOK-THU.md) |
| 8 | PP-02 | CHUẨN BỊ phi phong client (đọc SO-TAY-NHAN-CAP, PaintPifeng KgameWorld.cpp:11189, 11 bộ theo giới); chưa sửa | sau chủ duyệt CH-04 mới sửa — CHUẨN BỊ XONG 22/11 (08-giao-dien/PP-02-CHUAN-BI-PHI-PHONG-CLIENT.md) |
| 9 | LG-04 | Chuẩn bị bật jx_netlog/JXPERF ghi thời điểm nhận s2c / gửi c2s (không chạy) | chỉ dùng khi giật quay lại |
| 10 | FX-01 | Khảo sát nâng cấp hiệu ứng hình ảnh: danh sách hiệu ứng thiếu/xấu, ưu tiên, ước tính (đọc HIEU-HIEU-UNG-VU-KHI) | sau cường hóa/phi phong mới làm |
| 11 | HG | Ảnh d (thiếu thủy tinh) cập nhật cho vc37; chụp bộ ảnh nghiệm thu cuối a–f + HUD | |

## Nạp thêm 22/11 01:50 (Chat, đủ ≥10 việc mở)
| 8 | PP-02 | Đọc client phi phong: slot phi phong, mantle/ảnh theo giới, tooltip [cấp N]; ghi kế hoạch sửa UI/hiển thị | đọc tĩnh + sổ tay |
| 9 | PP-02 | Làm cửa sổ/hiển thị Phi phong theo kế hoạch (worktree riêng, khóa LD/APK theo LICH-CONG-VIEC) | sau B có PP-01 |
| 10 | CH-03 | Lỗi mất áo +9 khi gỡ khỏi ô giữa: tìm nguyên nhân (log B-116), sửa nếu là lỗi client | #366/#368 |
| 11 | CH-03 | Ảnh e (thiếu bạc) bằng hook trừ bạc atestqhhai, hoàn bạc 8 Ức 3400 Vạn | #368 |
| 12 | HG | Cập nhật sổ tay 08-giao-dien bằng cơ chế vc38 (giữ trang bị ở giữa) | cộng dồn L20.4 |
| 13 | FX-01 | Khảo sát nâng cấp hiệu ứng hình ảnh (glow, sét), chỉ đọc | |
| 14 | HT | Danh sách hook thử client cần gỡ + kế hoạch gỡ có kiểm chứng (từ PP-03) | |
| 15 | LG-07 | Đo lại fps/frame >40 ms khi đi nhiều map để xác nhận fix36 | |
