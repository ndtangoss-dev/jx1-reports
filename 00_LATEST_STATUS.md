# 00 - Trạng thái mới nhất dự án JX1

Cập nhật: 2026-11-12. Nguồn chính: [FIX_HISTORY/45](FIX_HISTORY/45-fix36-giat-ban-do-va-36hz.md), [FIX_HISTORY/HANDOVER-FIX34](FIX_HISTORY/HANDOVER-FIX34.md), [FIX_HISTORY/28](FIX_HISTORY/28-bao-cao-trang-thai-tong-the-jx1.md), [BAI_HOC.md](BAI_HOC.md).

Ký hiệu: **[ĐÃ XÁC MINH]** = có log, số đo hoặc kiểm thử thực tế. **[GIẢ THUYẾT]** = chưa kiểm chứng. **[KẾ HOẠCH]** = việc chưa làm.
Đã lược bỏ IP, tài khoản và thông tin truy cập (ghi dạng `<LAN-IP>`, `<TAILSCALE-IP>`, `<test-account>`...).

## 000. Phase 48 (2026-11-12) – đo tài nguyên server trong guest VM (đo thăm dò)
Báo cáo: [TEST_RESULTS/48-server-resource-measurement](TEST_RESULTS/48-server-resource-measurement.md); số liệu: experiments/server-resource/.
- [VERIFIED] VM thử JX-Test-36 (4 vCPU, 6 GB, Win10), gs001 36Hz; Main VM không chạy, không đụng; không đổi cấu hình/dịch vụ.
- [VERIFIED] Mốc A (0 user, 600 mẫu): CPU guest tb 12,8% (p95 28,8%), RAM dùng 2,64 GB, tick gs001 tb 0,44 ms, 36/36.
- [VERIFIED] Mốc B (1 user Sonnet, 600 mẫu, 3 đoạn): CPU guest tb 14,4% (p95 33,6%), RAM 2,88 GB (max 3,0), gs001 WS 432–479 MB, tick tb 0,81 ms (max 32,7 ms, 1 hụt/10 phút), mạng gửi 26–58 KB/s theo hoạt động.
- [BLOCKED/UNRELIABLE] CPU từng tiến trình bằng bộ đếm Windows trong VM này; dùng CPU guest tổng + tick tự đo của gs001.
- [PENDING USER] Mốc C (2 user): chờ chủ dự án đăng nhập Xiaomi 13T Pro. Sonnet: EXPLORATION_MODE=OFF, BUG_FIX_QA_MODE=ON.
## 00. Phase 47 (2026-11-12) – nhấp nháy đối tượng khi di chuyển nhanh
Báo cáo: [FIX_HISTORY/47](FIX_HISTORY/47-dieu-tra-nhap-nhay-doi-tuong.md); kiến trúc QA mới: [QA_AUTONOMOUS_ARCHITECTURE.md](QA_AUTONOMOUS_ARCHITECTURE.md).
- [ĐÃ XÁC MINH – video điện thoại + LDPlayer] Toàn bộ lớp đối tượng (cây, đá, quái, NPC, nhân vật) biến mất 53–59 ms mỗi lần camera sang vùng mới giữa 2 nhịp logic: cây đối tượng bị xóa ở pha vẽ (`SetFocusPosition` -> `Fell`) nhưng chỉ dựng lại ở nhịp logic sau (`Preprocess`). Lỗi hồi quy từ Fix31 (có ở Fix33–36, P46), không do nạp trước P46.
- LDPlayer 30 s: 22 lần đổi vùng, 9 lần trống 45–68 ms, 18 khung 0 đối tượng; video LDPlayer 8 sự kiện khớp log.
- [ĐÃ XÁC MINH trên LDPlayer, bản THỬ P47] Sửa đã duyệt: dựng lại cây ngay trong cùng khung khi đổi vùng. 58 s/67 lần đổi vùng: 0 khung trống (trước 18/30 s), Preprocess tb 0,47 ms; camera vẫn mượt. Sonnet xác minh lại 70 s ([TEST_RESULTS/47-p47-verification](TEST_RESULTS/47-p47-verification.md)): 0 khung trống, khoảng trống max 1,6 ms, camera 1,00/0,08, p99 24,7 ms; khung dài 240–300 ms là app bị dừng ngoài vòng vẽ lúc chụp/quay màn hình ADB. Chưa thử điện thoại; hồi quy ra chiêu chưa xác nhận.
- [TẠM DỪNG theo yêu cầu chủ máy] Sonnet QA tự chủ (đã xác minh độc lập lỗi nhấp nháy, đặt FPS game 90): xác minh độc lập + hồ sơ nhân vật + thí nghiệm tiềm năng/kỹ năng ([TEST_RESULTS/47-autonomous-qa-log](TEST_RESULTS/47-autonomous-qa-log.md)).

## 0. Phase 46 (2026-11-12) – tóm tắt
Báo cáo: [FIX_HISTORY/46](FIX_HISTORY/46-phase46-giat-ban-do-va-ky-nang.md), kế hoạch QA [TEST_RESULTS/46-qa-plan](TEST_RESULTS/46-qa-plan.md), tri thức game [knowledge/](knowledge/README.md).
- [ĐÃ XÁC MINH trên LDPlayer] Giật màn hình khi di chuyển = nội suy răng cưa 18 Hz (fix33). Kịch bản chuẩn Phong Lăng Độ -> 162/186: tỉ lệ tốc độ camera khung-sau-nhịp 0,45 -> 0,98; biến thiên vận tốc 0,43 -> 0,09.
- [ĐÃ XÁC MINH] Khung cực chậm khi di chuyển (dựng ẩn bảng Tự động ~700 ms, giải mã texture vùng mới, glyph tên NPC): khởi động nguội, khung đang di chuyển max 755–939 ms -> 39–69 ms, không còn >= 100 ms.
- [ĐÃ XÁC MINH] Giật khi ra chiêu (bóng mờ vẽ cả phần trong suốt): ra chiêu liên tục p95 103 -> 45 ms, khung >= 100 ms 58 -> 0.
- [ĐÃ XÁC MINH] Đạn: vị trí vẽ đổi 43–59 lần/s, hết răng cưa. Khung hình sprite ~17/s do asset (không phải 36 hình/s). Chỉ đo 1 kỹ năng; kỹ năng khác BỊ CHẶN (hạn chế vũ khí).
- [CHƯA KIỂM THỬ] Chủ máy chưa thử APK P46 trên điện thoại. Server không đổi (36Hz trên VM thử).

## 1. Client mới nhất
- Bản mới nhất: **P46** (APK `jx-tailscale-8080-p46.apk`, SHA256 `235DBD37F35C2B266588B209733E578D7D6528363DD19158F8ECD80BCCB3B847`). Chỉ khác Fix36 ở `libMyGame.so`, ký cùng khóa. [ĐÃ XÁC MINH] ([46](FIX_HISTORY/46-phase46-giat-ban-do-va-ky-nang.md))
- Bản trước: Fix36 (`jx-tailscale-8080-fix36.apk`, SHA256 `9ABDF095…1F66`) – dùng để rollback.
- P46 giữ nguyên Fix31, Fix33 (đã sửa phần nội suy), Fix34, Fix35, Fix36.

## 2. Các bản fix
| Bản | Nội dung | Trạng thái | Báo cáo |
|---|---|---|---|
| Fix31 | Làm mượt nhịp xử lý phía client | Đã dựng, đã thử | [CLIENT/31](CLIENT/31-toi-uu-nhip-xu-ly-client.md) |
| Fix33 | Chặn lỗi kỹ năng/sát thương, độ mượt | Đã dựng, đã thử | [FIX_HISTORY/33](FIX_HISTORY/33-fix-skill-damage-and-smoothness.md) |
| Fix34 | Nội suy đạn bay, tối ưu độ mượt | Đã dựng, đã thử | [FIX_HISTORY/34](FIX_HISTORY/34-toi-uu-toan-dien-do-muot.md), [HANDOVER](FIX_HISTORY/HANDOVER-FIX34.md) |
| Fix35 | Client: `KSubWorld::FindRegion` chặn khi chưa có region. Server: `KPlayer.cpp:7606` sửa format thiếu tham số; `KSortScript.cpp:328` dùng `intptr_t` cho `_findfirst` | Chủ máy đã thử trên điện thoại với server gốc [ĐÃ XÁC MINH] | [45](FIX_HISTORY/45-fix36-giat-ban-do-va-36hz.md), [44](FIX_HISTORY/44-dieu-tra-a2-thoat-som.md) |
| Fix36 | Hết giật bản đồ: chỉ dọn texture khi cache > 384 MB, kiểm tra mỗi 10 s | QA trên LDPlayer [ĐÃ XÁC MINH]; chủ máy chưa thử trên điện thoại | [45](FIX_HISTORY/45-fix36-giat-ban-do-va-36hz.md) |
| P46 | Hết răng cưa camera/đạn; nạp trước texture vùng; hoãn dựng bảng Tự động tới lúc đứng yên; nạp trước glyph tên NPC; bóng mờ chỉ vẽ phần nhìn thấy; nội suy Z đạn, khung sprite nửa nhịp, hiệu ứng bám NPC theo vị trí vẽ | QA LDPlayer [ĐÃ XÁC MINH]; điện thoại [CHƯA KIỂM THỬ] | [46](FIX_HISTORY/46-phase46-giat-ban-do-va-ky-nang.md) |

## 3. Server 18Hz
- Server gốc (exe của gói) chạy 18Hz trên VM thử, đủ PaySys, Goddess, Bishop, gs001. S3Relay tắt. [ĐÃ XÁC MINH] ([41](TEST_RESULTS/41-xac-nhan-server-18hz.md))
- Bản tự dựng từ nguồn ở 18Hz (có A2 Command Lane): vào game, HUD 204/204, đi lại được, tick khoảng 0,8 ms, lệnh di chuyển qua A2 trễ trung bình 8 ms. [ĐÃ XÁC MINH] ([45](FIX_HISTORY/45-fix36-giat-ban-do-va-36hz.md), [PATCH_NOTES/39](PATCH_NOTES/39-a2-command-lane.md))
- Server gốc 18Hz được giữ làm phương án dự phòng.

## 4. Server 36Hz
- Đặt `LogicFps=36` trong `gs001_cfg.ini` [GameServer]. Server chạy đủ 36/36 nhịp mỗi giây, mỗi nhịp mất 0,6–0,8 ms trong ngân sách 27,8 ms. [ĐÃ XÁC MINH]
- Cách làm: nhịp lẻ chỉ đi nửa bước và gửi đồng bộ vị trí, nhịp chẵn chạy đủ logic 18Hz. Kỹ năng, hồi chiêu, trạng thái, AI và Lua vẫn giữ đơn vị thời gian 18Hz.
- 2026-11-12: VM thử đã chuyển sang bản 36Hz cho chủ máy thử trên điện thoại. Log khởi động có `[fix36] LogicFps=36` và `SvrFPS= 36/36`. [ĐÃ XÁC MINH] Kết quả chủ máy thử trên điện thoại: **chưa có**.
- Đạn bay vẫn cập nhật 18 lần/s. [KẾ HOẠCH: làm 36Hz cho đạn bay nếu cần]

## 5. Lỗi đã sửa
- Giật bản đồ: client gọi `removeUnusedTextures()` mỗi giây; khung kế tiếp mất 84–120 ms; 106/106 khung giật rơi đúng mốc đó. Sau khi sửa, trên LDPlayer:
  - Khung > 40 ms: 197 → 12.
  - Khung ≥ 100 ms: 15 → 1.
  - FPS: 56 → 58,8.
  [ĐÃ XÁC MINH]
- HUD 0/0: 7 struct gói client lệch bố cục so với client 2912 (int64 so với int, thiếu hoặc thừa trường). Đã sửa. [ĐÃ XÁC MINH]
- Crash khi đăng nhập: exe cắt con trỏ IServer xuống 32 bit. Đã đổi tham số sang `uintptr_t`. [ĐÃ XÁC MINH]
- Crash x64 do `_findfirst` (`KSortScript.cpp`) và lỗi format ở `KPlayer.cpp:7606`. [ĐÃ XÁC MINH] ([44](FIX_HISTORY/44-dieu-tra-a2-thoat-som.md))
- Đã loại giả thuyết minimap/camera gây giật: khung đổi vùng không trùng khung giật. [ĐÃ XÁC MINH]

## 6. Kiểm thử đã đạt
| Hạng mục | 18Hz gốc + Fix36 | Tự dựng 18Hz | Tự dựng 36Hz |
|---|---|---|---|
| Vào game, HUD | Đạt | Đạt (204/204) | Đạt |
| Đi lại | Đạt | Đạt | Đạt |
| Đánh quái mất máu | Đạt (quái chết, lên cấp) | Chưa đánh | Đạt (máu giảm, lên cấp) |
| Tốc độ chạy phải/trái 10 s | 7/7 ô | - | 6/6 ô |
| Crash | Không | Không | Không |

Nguồn: [45](FIX_HISTORY/45-fix36-giat-ban-do-va-36hz.md). QA chạy trên LDPlayer qua ADB.
- Kích thước 351 struct chung giữa client (NDK arm64) và server (MSVC x64): toàn bộ gói server→client có kích thước cố định đều khớp. [ĐÃ XÁC MINH]

## 7. Kiểm thử chưa làm
- Kỹ năng tầm xa, AOE, liên hoàn: nhân vật thử mới cấp 1–2, chưa lấy được lệnh bài GM.
- Cưỡi ngựa, nhiều người chơi, bang hội, giao dịch trên bản tự dựng.
- Chủ máy chạy Fix36 trên điện thoại thật, qua nhiều vùng.
- Chủ máy thử bản 36Hz trên điện thoại.
- Khởi động lại máy thật hoặc VM để xem forwarder, CDN và exe có tự lên không.

## 8. Lỗi và rủi ro còn tồn tại
- Tốc độ chạy ở 36Hz là 6 ô/10 s, ở 18Hz là 7 ô/10 s. Chưa xác định được chênh 1 ô là do sai số đọc tọa độ hay chậm thật. [GIẢ THUYẾT: do sai số đo]
- NPC dừng giữa hai nhịp có thể đi lố tối đa nửa bước (≤ 15 đơn vị). [GIẢ THUYẾT, chưa đo]
- Còn khoảng 270 chỗ ép con trỏ 32 bit trong CoreServer chưa rà, phần lớn là mã phía client.
- S3Relay đang tắt nên chat, bang hội và bạn bè không hoạt động; console báo reconnect Tong/Chat/Transfer thất bại.
- Ở Ba Lăng Huyện, đi bộ qua cổng không bật được trạng thái chiến đấu.
- 28 bản đồ của gs001 không nạp được vì thiếu `.wor` ([SERVER/05](SERVER/05-c2-chay-server.md)).

## 9. Phiên bản tương ứng (không đưa binary lên đây)
| Thành phần | Phiên bản |
|---|---|
| APK | `jx-tailscale-8080-fix36.apk` (Fix36); dự phòng Fix35, Fix34 |
| Server gốc | gs001 gốc của gói, 18Hz |
| Server tự dựng | bộ `fix36-bin` (exe + CoreServer.dll + A2 CmdLane), `LogicFps` 18 hoặc 36 |

## 10. Việc ưu tiên tiếp theo [KẾ HOẠCH]
1. Lấy kết quả chủ máy thử Fix36 và 36Hz trên điện thoại.
2. QA nhận lệnh bài GM ở NPC Lễ Quan, rồi thử từng nhóm kỹ năng ở cả 18Hz và 36Hz.
3. Thêm log vị trí phía server để đo chính xác tốc độ chạy ở 36Hz.
4. Rà các chỗ ép con trỏ 32 bit còn lại; làm 36Hz cho đạn bay nếu cần.
5. Dọn dẹp vận hành: forwarder/CDN, các tác vụ tạm, dữ liệu nhạy cảm trong lịch sử git của repo nguồn.

## 11. Báo cáo chi tiết
- [CLIENT/](CLIENT/): dựng APK, CDN, nhịp xử lý client.
- [SERVER/](SERVER/): dựng và vận hành server, VM, mạng, nghiên cứu 36Hz, Command Slot.
- [TEST_RESULTS/](TEST_RESULTS/): thử client thật, đối chiếu kỹ năng, mô phỏng, xác nhận 18Hz.
- [FIX_HISTORY/](FIX_HISTORY/): tổng kết trạng thái, điều tra crash, Fix33–Fix36.
- [PATCH_NOTES/](PATCH_NOTES/): mô tả các patch (không có mã nguồn).
- [BAI_HOC.md](BAI_HOC.md): bài học vận hành.
