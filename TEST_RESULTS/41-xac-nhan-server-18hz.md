# 41 - Xác nhận server 18 Hz tự build (Phase 2, tĩnh)

**TÓM TẮT 5 DÒNG**
1. Build thành công KHÔNG đồng nghĩa tương thích: EXE gốc dựng bằng VS2010 (linker 10.00, 2025-11-20), bản mới bằng v143 (14.44).
2. Danh sách DLL import và tên export giống nhau; khác biệt export chỉ do mangling `tr1::unordered_map` và move-ctor do compiler sinh.
3. Nguồn mới hơn EXE (file sửa 2026-01-03/04): chuỗi chỉ có ở bản mới như `PasstSkillLevel`, `TestMaxLife`, `MESSAGE_SYSTEM_TONGZHI_HEAD`, `mapRefModel` -> nguồn KHÔNG khớp tuyệt đối EXE đang chạy.
4. Đã sửa lỗi mã hóa: ACP máy này 1252 làm chuỗi Trung thành `??`; dùng `/source-charset:.936 /execution-charset:.936` + đổi 3 file UTF-8 BOM sang GBK -> chuỗi byte-giống bản gốc.
5. Chưa chạy bản build ở đâu cả -> mọi kết luận về tương thích runtime là CHƯA KIỂM CHỨNG.

Cần tôi quyết định: không

## So sánh EXE
| | Gốc (đang dùng) | Tự build |
|---|---|---|
| gs001.exe | 543,232 B | 1,265,664 B |
| CoreServer.dll | 1,893,376 B | 11,801,088 B |
| Linker | 10.00 | 14.44 |
| Export Core/Engine/LuaLib | 271/831/104 | 274/865/104 |
Kích thước lớn hơn do `.data` khởi tạo tĩnh và CRT tĩnh khác; chưa đánh giá ảnh hưởng.

## Chuỗi/ký hiệu (cmp_str2/cmp_id3, nhiễu do mã máy)
- Chỉ ở bản mới (liên quan game): `PasstSkillLevel`, `TestMaxLife`, `MESSAGE_SYSTEM_TONGZHI_HEAD`, `mapRefModel`, và 3 khóa của A2 (`CmdLane`, `Enable`, `BufferBusy`, `TtlActMs`, `TtlMoveMs`). Phần còn lại là CRT/ATL khác phiên bản.
- Chỉ ở bản gốc: CRT cũ (`LC_*`, `DecodePointer`...), không có ký hiệu game.
- Hệ quả: logic nguồn có thể khác EXE gốc ở các hàm này (chưa đối chiếu hành vi).

## Rủi ro/kiểm tra còn lại
- Heaven/Rainbow chưa build/kiểm; Goddess/Bishop/Relay không build lại (vẫn dùng EXE gốc).
- Lệnh Lua gọi trực tiếp: không qua khe lệnh -> A2 không ảnh hưởng (đã đọc mã, chưa chạy).
- Cấu hình/dữ liệu (`gs\Settings`, `gs00N_cfg.ini` Ip chứa localIp, bảng DB): chưa đối chiếu bản build với dữ liệu thật.
- Cần chạy trong VM thử: khởi động, nạp bản đồ (gs001 gốc ~7 phút), đăng nhập, di chuyển+chiêu, đọc `CmdLane_stat.log`.

## Phân loại
- Đã làm: build, so sánh tĩnh, sửa mã hóa.
- Build chưa chạy: gs001.exe, CoreServer.dll, Engine.dll, LuaLibDll.dll.
- Đã test thật: không có.
- Chưa kiểm chứng: tương thích hành vi với EXE gốc, ổn định, A2 trên server thật.
