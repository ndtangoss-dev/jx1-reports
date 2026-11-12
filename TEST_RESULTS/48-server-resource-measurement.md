# 48 - Đo tài nguyên server trong guest VM (Mốc A, B) – ĐO THĂM DÒ

TÓM TẮT 5 DÒNG
1. Đo trực tiếp BÊN TRONG guest VM thử JX-Test-36 (4 vCPU, 6 GB RAM, Windows 10 Pro 19045), gs001 bản tự dựng 36Hz; 1 mẫu/giây, 600 mẫu mỗi mốc, 0 mẫu thiếu. Không dùng số liệu Host.
2. Mốc A (0 user): CPU guest tb 12,8% (p95 28,8%, max 49,6%), RAM dùng ~2,64 GB/6 GB, gs001 tự đo tick tb 0,44 ms (~1,6% một lõi), 36/36 tick, 0 tick hụt.
3. Mốc B (1 user, Sonnet): CPU guest tb 14,4% (p95 33,6%), RAM ~2,88 GB (max 3,0), gs001 WS 263 -> 432–479 MB, tick tb 0,81 ms (max 32,7 ms, 1 lần hụt trong 10 phút), mạng gửi tb 43,5 KB/s (đi lại 57,8 KB/s).
4. Giới hạn VERIFIED: CPU từng tiến trình đo bằng Windows KHÔNG tin được trong VM này (Windows hầu như không ghi nhận CPU cho tiến trình); dùng CPU guest tổng + thời gian tick gs001 tự đo. gs001 commit ~6,8 GB (Private Bytes) -> guest commit ~10,5 GB > RAM.
5. Mốc C (2 user): PENDING USER – chờ chủ dự án đăng nhập Xiaomi 13T Pro. Không ngoại suy tuyến tính khi chưa có C.

Cần tôi quyết định: có (đăng nhập Xiaomi để đo Mốc C).

## 1. Xác minh môi trường (VERIFIED)
| Mục | Giá trị |
|---|---|
| VM | JX-Test-36 (VM đang chạy duy nhất trên host; Main VM JX-Server-D không chạy, không bị đụng tới) |
| Guest OS | Windows 10 Pro 10.0.19045 |
| vCPU / RAM guest | 4 / 6 144 MB (OS thấy 6 125 MB) |
| GPU/VRAM | Card ảo vboxsvga, 3D tắt, không passthrough -> **VRAM: N/A** (server headless, không dùng GPU) |
| Dịch vụ | gs001 (bản tự dựng T4, LogicFps=36), Bishop, Goddess, Sword3PaySys, SQL Server Express; S3Relay không chạy |
| Tick | SvrFPS 36/36 (log console gs001) |
| Cấu hình | Không thay đổi VM/server/dịch vụ; không restart. Chỉ tắt app game trên LDPlayer để có 0 user cho Mốc A |

## 2. Phương pháp và công cụ
- `experiments/server-resource/collect_guest_metrics.ps1`: chạy trong guest qua WinRM, `Get-Counter` 1 s × 600: CPU (_Total và từng lõi; Mốc B thêm User/Privileged/Interrupt/DPC), RAM khả dụng/commit/cache, pagefile %, pages/s, mạng (byte, gói) theo card, theo tiến trình (CPU, Working Set, Private Bytes, thread, handle) cho gs001/Bishop/Goddess/PaySys/sqlservr/wsmprovhost. Luồng thứ hai: số kết nối ESTABLISHED (gs001 cổng người chơi, Bishop) mỗi 5 s.
- Tick: `fetch_tick.ps1` đọc dòng tóm tắt mỗi phút của gs001 (SvrFPS, tick avg/max, over); epoch suy từ GameLoop (36/s), sai số ≤ 60 s.
- Phân tích: `analyze_phase48.py` -> `phase48-summary.csv` (avg/p95/p99/max cho từng mốc và từng đoạn).
- CPU guest % = phần trăm của TOÀN BỘ 4 vCPU. RAM dùng = 6 125 MB − Available. Không cộng Working Set các tiến trình để suy RAM tổng.
- Chi phí đo: tiến trình WinRM (wsmprovhost) Working Set ~70 MB; CPU không đo tin cậy được (xem mục 5).

## 3. Kết quả
### Mốc A – 0 user (epoch 1794471004–1794471604, 600/600 mẫu)
| Chỉ số | avg | p95 | p99 | max |
|---|---|---|---|---|
| CPU guest % | 12,8 | 28,8 | 37,9 | 49,6 |
| RAM dùng MB | 2 643 | – | – | 2 697 |
| Mạng nhận B/s | 3 067 | 5 163 | – | 41 673 |
| Mạng gửi B/s | 3 424 | 6 644 | – | 18 460 |
- Phân rã CPU (bổ sung 120 s, mốc A2): User 9,3%, Privileged 3,8%, Interrupt 0,14%, DPC 0,01% của toàn VM.
- gs001: WS 263 MB, Private 6 806 MB; tick tb (trung bình các phút) 0,44 ms, max 16,5 ms; 36/36; hụt 0.
- Bishop/Goddess/PaySys WS 3–4 MB (đã bị Windows thu hẹp WS), SQL ~100 MB. Commit guest ~10,5 GB; pagefile 14%; pages/s tb 0,6.
- Kết nối người chơi: 0.

### Mốc B – 1 user (epoch 1794472061–1794472661, 600/600 mẫu; nhân vật alias jxt36a trên LDPlayer, Sonnet thao tác)
| Đoạn | CPU guest avg/p95/max % | RAM dùng avg/max MB | gs001 WS MB | Tick tb / max (ms) | Gửi avg/p95 B/s | Nhận avg B/s | Gói gửi/nhận /s | pages/s |
|---|---|---|---|---|---|---|---|---|
| Toàn bộ | 14,4 / 33,6 / 71,9 | 2 880 / 3 002 | 432 | 0,81 / 32,7 | 43 502 / 69 740 | 5 526 | 40,5 / 42,6 | 73 |
| Đứng yên (180 s) | 12,9 / 28,9 / 44,2 | 2 767 / 2 840 | 339 | 0,68 / 6,2 | 25 736 / 35 547 | 4 397 | 24,0 / 26,7 | 5,7 |
| Di chuyển (205 s) | 16,9 / 42,2 / 71,9 | 2 879 / 2 997 | 470 | 0,78 / 17,6 | 57 824 / 73 519 | 7 070 | 59,6 / 63,0 | 157 |
| Chiến đấu (200 s) | 13,5 / 28,8 / 37,3 | 2 981 / 3 002 | 479 | 0,93 / 32,7 | 45 258 / 63 671 | 4 933 | 36,2 / 36,5 | 28 |
- Tick: 36/36 ở mọi phút trừ 1 phút 35/36 với 1 tick hụt (đoạn chiến đấu); max 32,7 ms (ngân sách 27,8 ms).
- Ghi chú hoạt động (Sonnet): nhân vật đã cưỡi ngựa khi đăng nhập nên đoạn "di chuyển" thực tế đi BỘ, đoạn "chiến đấu" trên ngựa; 217 lần nhấn đánh (Đại Lực Kim Cang Chưởng), 1 bình nội lực.

### Delta B − A (1 user so với 0 user)
| Chỉ số | Delta |
|---|---|
| CPU guest tb | +1,6 điểm % (nhiễu nền Windows lớn hơn delta; không kết luận chính xác) |
| gs001 tick tb | +0,37 ms/nhịp (0,44 -> 0,81) ≈ +1,3% một lõi; đứng yên +0,24, di chuyển +0,34, chiến đấu +0,49 ms |
| RAM guest | +237 MB tb (+305 MB max) |
| gs001 WS | +76 (đứng yên) đến +216 MB (chiến đấu) – nạp dữ liệu bản đồ/NPC vùng có người chơi |
| Mạng gửi | +22 KB/s (đứng yên) đến +54 KB/s (di chuyển) |
| Mạng nhận | +1,3 đến +4 KB/s |
| Paging | pages/s tăng mạnh khi di chuyển (157/s) – dữ liệu gs001 bị đẩy ra pagefile vì commit > RAM |

## 4. Trạng thái
| Mục | Trạng thái |
|---|---|
| Xác minh VM, guest config, không đụng Main VM | VERIFIED |
| Mốc A | VERIFIED (600/600) |
| Mốc B | VERIFIED (600/600, 3 đoạn) |
| Mốc C (2 user) | PENDING USER |
| CPU từng tiến trình (Windows counters) | BLOCKED/UNRELIABLE (xem mục 5) |
| gs001 CPU qua tick tự đo | VERIFIED (độ phân giải 1 phút) |
| VRAM | N/A (không có GPU workload) |
| Sonnet: EXPLORATION_MODE=OFF, BUG_FIX_QA_MODE=ON | Ghi trong TEST_RESULTS/SONNET_CHECKPOINT.md |

## 5. Giới hạn
- **CPU từng tiến trình không đo được tin cậy trong guest này:** tổng thời gian CPU mọi tiến trình đo trong 20 s chỉ ~0,6% một lõi trong khi bộ đếm hệ thống báo ~52% một lõi thời gian người dùng; `\Process(*)` gần 0. Windows trong VM VirtualBox hầu như không gán CPU cho tiến trình. Đây là giới hạn công cụ, không phải số 0 thật.
- Tick log 1 dòng/phút -> không có phân phối tick theo giây; epoch dòng tick sai số ≤ 60 s.
- CPU guest bao gồm tác vụ nền Windows (cập nhật, tìm kiếm, Defender…) – nhiễu ~12–13% ngay cả khi 0 user.
- Thời lượng mỗi mốc 10 phút, 1 lần đo -> "đo thăm dò", không phải benchmark.
- VM VirtualBox trên máy cá nhân ≠ VPS (CPU host dùng chung với LDPlayer, Claude Code).
- Đoạn đi/cưỡi ngựa bị đảo so với kế hoạch (xem ghi chú B).

## 6. Ước lượng sơ bộ (KHÔNG phải capacity test, chờ Mốc C)
- Không ngoại suy tuyến tính từ 1 user. Một số chi phí theo vùng bản đồ (nạp dữ liệu, AI quái) chỉ tăng khi có thêm vùng hoạt động; chi phí đồng bộ mạng tăng theo số người nhìn thấy nhau (có thể hơn tuyến tính).
- Nếu tick tăng ~0,3–0,5 ms/người chơi như Mốc B mà không giảm dần, gs001 (một luồng chính) sẽ chạm ngân sách 27,8 ms/nhịp ở cỡ vài chục người chơi đang hoạt động -> cần đo C và nhiều user hơn trước khi kết luận.
- Đề xuất VPS SƠ BỘ cho thử nghiệm ít người (≤ 10): 4 vCPU xung nhịp đơn lõi cao, RAM ≥ 12 GB (commit gs001 ~6,8 GB + SQL + OS, tránh paging thấy ở Mốc B), SSD, băng thông ≥ 10 Mbit/s cho ≤ 10 người (gửi ~25–60 KB/s/người đang hoạt động). Cần xác nhận lại sau Mốc C.

## 7. Dữ liệu
`experiments/server-resource/`: phase48-raw-A.csv, phase48-raw-A2.csv, phase48-raw-B.csv (thô 1 s), phase48-conn-A/B.csv (kết nối 5 s), phase48-segments-B.csv, phase48-tick.txt (dòng tick gs001), phase48-summary.csv, collect_guest_metrics.ps1, fetch_tick.ps1, analyze_phase48.py.
Chạy lại: `.\collect_guest_metrics.ps1 -Milestone C -Seconds 600 -Cred <cred> -Guest <guest> -OutDir .` ; `.\fetch_tick.ps1 ...` ; `python -I analyze_phase48.py . phase48-tick.txt A B C`.
