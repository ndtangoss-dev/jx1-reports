# P-02 / B-04 — số đo thật đầu tiên từ 1 Bot trên Test-36 (#216, 19/11/2026)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] Thu 60 s từ 1 Bot đã vào game: 1824 frame S2C, tick (khoảng cách hai frame liên tiếp) trung bình 32,9 ms, p50 32 ms, p95 109 ms, lớn nhất 125 ms; phân bố hai cụm ~0 ms và ~50 ms (frame đến theo cụm, phù hợp nhịp ~18–20 Hz tách thành 2 lần đọc TCP).
2. [ĐÃ KIỂM] RX của socket Bot ~216 kbps (13 cửa sổ 5 s); TX ~0 vì Bot chỉ đứng yên, không có lệnh.
3. Đây là **đo phía Bot một người**, KHÔNG phải tick nội bộ gs001, không phải interface guest, không có FPS client. `jx1_bench.py` từ chối đầu vào vì `frame_samples` rỗng (cần client thật); số trên tính bằng tay từ `P-02-bot-metrics.json`.
4. Chưa đo B-04 trước/sau (Enabled=0 so với Enabled=1) và chưa có 100 Bot + 20 người, nên **P-02 và B-04 chưa đóng**.
5. Cần tôi quyết định: không.

Thu bằng `JX1_OPS/TOOLS/bench/collect_bot_metrics.py <giây> <out.json>` (biến môi trường như `cli.py`; không có bí mật trong tệp xuất).
