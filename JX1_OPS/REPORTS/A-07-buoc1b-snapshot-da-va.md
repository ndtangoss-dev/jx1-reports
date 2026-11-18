TÓM TẮT 1/5: [NGUỒN] Bước 1 đạt bằng cách dùng bản Debug dựng sẵn từ snapshot ĐÃ VÁ (A-07e), chép sang `D:\JX-build\a07b` (a07 cũ giữ làm checkpoint lỗi).
TÓM TẮT 2/5: [NGUỒN] gs001.exe SHA-256 `988175A7...2FF48A91`; kèm 3 DLL và 5 PDB; danh sách đủ ở `D:\JX-build\a07b\SHA256.txt`. Mã gốc không bị sửa.
TÓM TẮT 3/5: [NGUỒN] Quét Defender trên máy thật KHÔNG chạy được ("Product/Feature disabled"). Điều kiện "quét Defender" của Q-19 chưa đạt; có thể quét trong VM thử.
TÓM TẮT 4/5: [NGUỒN] Bước 2: JX-Test-36 chạy, nic1 host-only, ping 192.168.56.150 thông, chưa có snapshot. DỪNG trước bước 3: có 2 tiến trình VBoxSVC (14/11 và 18/11 21:11) và 6 VBoxHeadless đang chạy — bất thường so với dự kiến.
TÓM TẮT 5/5: [CHƯA KIỂM] Bước 3–6 chưa làm. Cần tôi quyết định: có (xác nhận VBoxSVC/6 VM đang chạy là bình thường, hoặc cho dọn).

# A-07 bước 1 (làm lại từ snapshot đã vá) và bước 2
- Nguồn bản dựng: `D:\JX-wt\A-07c\server\jxOnline\gameserver\Sources\A07b\checkpoint-a07e-final\out` (verifier exit 0 theo `A-07e-rtc.md`: /Od /Zi /MT, không có /RTC). Không dựng lại vì đã có, đã kiểm, cùng nguồn đã vá; dựng thêm không thêm bằng chứng. [TỰ QUYẾT]
- Thư mục đích mới `D:\JX-build\a07b` (script gốc buộc `a07` và từ chối thư mục có sẵn).
- Hoàn tác: xóa `D:\JX-build\a07b`.
- Điều chưa kiểm: runtime; PDB khớp exe (chỉ cùng thư mục build).
- Lý do dừng ở bước 3 (theo thư #175): trạng thái VBoxSVC "bất thường". Việc cần chủ/Chat xác nhận: 6 VBoxHeadless (3 khởi động 16/11 21:02, 3 khởi động 16/11 23:41) là những VM nào và có để nguyên không (quy tắc: không bật hai VM cùng lúc, Main VM là vùng Đỏ).
