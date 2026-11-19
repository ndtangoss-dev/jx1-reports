# BOT GĐ0 — khảo sát hướng A (Bot ngoài server) và B (Bot trong server) (#220, 19/11/2026)

**TÓM TẮT 5 DÒNG**
1. Đề xuất hướng nhẹ nhất: **A** (Bot là phiên giao thức ngoài server, đã chạy được: đăng nhập, vào gs001 Test-36, giữ 60 s thoát 0; `REPORTS/E-01-chay-that.md`). Không sửa exe server, không cần dựng lại server từ nguồn.
2. [ĐÃ ĐO, 1 Bot] RX ~216 kbps (~27 KB/s), TX ~0 khi đứng yên; khoảng cách khung S2C TB 32,9 ms, p95 109 ms (`REPORTS/P-02-do-bot-1-nguoi.md`). Nhịp tick nội bộ gs001 KHÔNG đo được từ phía Bot.
3. [CHƯA ĐO] Số Bot gánh được và ảnh hưởng nhịp 18 Hz: mới có 1 Bot. Ngoại suy tuyến tính chỉ là ước tính: 100 Bot ≈ 21,6 Mbps RX tại host-only; cần thang thử 1→5→20→50→100 với đo tick trong VM (GĐ1).
4. Hướng B (NPC mang hình người trong server): [CHƯA KIỂM] khả thi; cần sửa mã server mà mã nguồn "có thể không khớp exe" và chưa từng dựng lại (CLAUDE.md), nên rủi ro cao; ID 77 (NPC_NORMAL) trong exe thật 223 byte, chưa xác nhận có trường ngoại hình đủ như người chơi.
5. Cần tôi quyết định: có — duyệt hướng A + thang thử tải GĐ1 trên Test-36 (không Main VM).

## So sánh
| Tiêu chí | A: Bot ngoài (giao thức) | B: Bot trong server |
|---|---|---|
| Sửa server | Không | Có (mã gs001 + dựng lại exe) [CHƯA KIỂM đường dựng] |
| Tải lên gs001 | Mỗi Bot = một phiên người chơi thật (đồng bộ thế giới đầy đủ) | Nhẹ hơn một phiên, nhưng thêm AI trong tick |
| Hình người | Có sẵn (là người chơi thật) | Chưa rõ, cần kiểm sync NPC |
| Đo được ngay | Có (1 Bot đã đo) | Không |
| Rủi ro | Tải thang lớn, cần tài khoản/nhân vật cho từng Bot | Dựng lại server, lệch exe |

Cách đo lại: `python -I -X utf8 JX1_OPS/TOOLS/bench/collect_bot_metrics.py <giây> <out.json>` (biến môi trường như `cli.py`). Tick đo trong VM cần thêm số đo phía gs001 (chưa có).
