TÓM TẮT 1: Chạy `TOOLS/a07/build-debug-a07.ps1` trên máy dev (18/11 ~19:50): KHÔNG dựng được; MSBuild Common báo 31 lỗi, 0 exe sinh ra.
TÓM TẮT 2: Lỗi chính: mã nguồn `Common` có `__asm` x86 (Buffer.cpp:282/292/465, IniFile.cpp:24/35/90/97/108, NodeList.cpp:22/47, Utils.cpp:226...) mà x64 không hỗ trợ (C4235/C2059); thêm C1083 thiếu `..\heaven\serverstage.h` (SocketServer.cpp:9).
TÓM TẮT 3: Không phải lỗi cấu hình sửa 3 lần được: nguồn gốc cần vá asm/include; các bản A-07c/A-07e trước đó dựng được vì dùng snapshot ĐÃ VÁ (xem REPORTS/A-07c, A-07e), không phải nguồn gốc nguyên.
TÓM TẮT 4: Chỉ ghi vào `D:\JX-build\a07` (log `logs\Common-debug.log`, `commands.txt`); không chạy exe, không đụng VM, mã gốc không đổi. Không có SHA-256 vì không có exe.
TÓM TẮT 5: Cần quyết định: không (đề xuất: dùng lại snapshot đã vá của A-07e `D:\JX-build\a07e` làm gốc, hoặc vá asm; làm khi chủ duyệt hướng A-07).

# A-07 bước 1 — dựng Debug trên máy dev
- Lệnh: script gốc, không `-IobShimObject`. Chưa tới bước link nên chưa cần shim.
- Bằng chứng: `D:\JX-build\a07\logs\Common-debug.log` (31 Error(s), 53 Warning(s), 26 giây).
- Đường ra [GIẢ THUYẾT, chưa kiểm tra]: tái dùng cây đã vá của A-07e/c (có shim MiraclLegacyStdio), hoặc cho script nhận nguồn đã vá thay vì nguồn gốc. Thư mục `D:\JX-build\a07` giữ nguyên làm checkpoint (script từ chối ghi đè).
