# BOT hướng A — thang tải 1→5→20→50→100 trên Test-36 (#226 mục 2, 19/11/2026)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] Tạo 100 tài khoản `botld001..100` + vai `BotLd001..100` trên Test-36 (SQL qua WinRM, vai qua Bishop `bot_tao_role.py`); mật khẩu/khóa ở `D:\JX-keys\` ngoài kho.
2. [ĐÃ KIỂM] Vào được: N=1 1/1, N=5 5/5, N=20 16/20, N=50 37/50, N=100 78/100. Các Bot lỗi `timed out` ở bước đăng nhập; chỉ số lỗi lặp lại (7, 13, 18, 21, 22…) nên giống lỗi theo vai/tài khoản hơn là do tải — [CHƯA KIỂM] nguyên nhân.
3. [ĐÃ KIỂM] Phía VM (mẫu 5 s giữa mỗi bậc): gs001 CPU ~108–115% (idle trước thử đã ~114%, tức không đo được thay đổi do Bot), RAM gs001 246→257 MB, RAM trống ~3,6 GB/6,1 GB: không thấy áp lực RAM.
4. [ĐÃ KIỂM] Phía Bot: tick (khoảng cách frame S2C) trung bình 67→75 ms, p95 125→140 ms, ~95–108 kbps/Bot. Đây KHÔNG phải tick nội bộ gs001; tick trong gs001 [CHƯA ĐO] (cần log/console gs001).
5. Cần tôi quyết định: không. Chưa làm: hành vi GĐ1/GĐ3 (bán hàng, hảo hữu); Bot hiện chỉ đứng yên.

Công cụ: `TOOLS/bench/bot_ladder.py <N> <giây> <out>` (gọi `collect_bot_metrics.py` song song, cách nhau 1,2 s). Số liệu thô ngoài kho `D:\JX-build\ladder*`.
