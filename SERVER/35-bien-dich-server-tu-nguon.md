# 35 - Biên dịch thử server từ mã nguồn (nhánh 18 Hz)

## TÓM TẮT 5 DÒNG
1. Đã dựng được `gs001.exe`, `CoreServer.dll`, `Engine.dll`, `LuaLibDll.dll` (Release x64, MSVC 14.44, toolset v143) từ bản copy `D:\JX-build\src18`. Chưa chạy exe nào.
2. Kết quả nằm ở `D:\JX-build\_bin_v2_\gs\`, tách hẳn khỏi server đang dùng. Bản gốc, `JX-Server-D`, CDN không bị đụng.
3. Chưa có toolset v140 (chỉ v143), nên phải sửa 3 chỗ trên bản copy và thêm 1 shim; mã trong repo không đổi.
4. Khác biệt đáng chú ý so với exe gốc: `CoreServer.dll` tự dựng 11,8 MB so với 1,9 MB gốc; `gs001.exe` 1,27 MB so với 0,54 MB. Cùng danh sách DLL phụ thuộc. Chưa biết mã nguồn có khớp exe đang chạy hay không.
5. Bước kế (cần duyệt): so sánh hành vi trong VM thử riêng, rồi nghiên cứu khe lệnh đơn và nhánh 36 Hz.

Cần tôi quyết định: có - có tạo VM thử riêng (clone, MAC/IP/DB mới) để chạy bản tự dựng không.

## 1. Cách dựng (có thể lặp lại)
MSBuild của VS 2022, từng project riêng (sln ánh xạ cấu hình sai: `Release|Win32` trỏ sang `Template|x64`). Cờ chung: `/p:Configuration=...;Platform=x64;PlatformToolset=v143;WindowsTargetPlatformVersion=10.0.19041.0`. Thứ tự: Engine (`Release`), Common (`Release`), Core (`Server Release`), GameServer (`Release`); LuaLibDll cũng dựng được (bước hậu kỳ `copy` lỗi vì đường dẫn, bỏ qua). `gs001.exe` gốc là x64 (đọc header PE), nên dùng x64.
Log: `D:\JX-build\logs\`.

## 2. Các chỗ phải sửa (chỉ trên bản copy; mã trong repo giữ nguyên)
| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| `C1189` macro `vsnprintf`/`snprintf` | `Engine/Src/acc/acc_auto.h` định nghĩa lại hàm chuẩn | đổi tên macro (14 dòng) |
| `C2956` `operator delete(void*, size_t)` | quy tắc xóa có kích thước của trình biên dịch mới | cờ `/Zc:sizedDealloc-` qua `D:\JX-build\src18\Directory.Build.props` |
| `LNK2005 _Xlength_error` | trộn CRT tĩnh và động trong Engine | `/NODEFAULTLIB:libcpmt.lib`, chỉ cho Engine (áp cho Core thì hỏng) |
| `LNK1181 libdb181.lib...` | tôi đã bỏ `Lib\release` lúc copy | chép lại 21 file từ bản gốc sang bản copy (chỉ đọc bản gốc) |
| `LNK2001 __imp___iob_func` | `ms64.lib` (thư viện có sẵn, rất cũ) cần CRT cũ | shim `D:\JX-build\shim\iob_shim.cpp` |
Có `CoreServer.lib` bản chép từ gốc, tôi đã xóa để dùng bản tự dựng. Cảnh báo biên dịch chưa rà.

## 3. Điều chưa biết
- Mã nguồn có khớp exe đang chạy không: chưa so hành vi. Kích thước khác nhiều (có thể do tùy chọn tối ưu, thư viện tĩnh, hoặc mã khác phiên bản).
- Toolset v143 so với v140 có thể đổi hành vi (căn chỉnh, thứ tự đánh giá): chưa kiểm.
- Bản dựng chưa từng chạy; chưa biết nạp được dữ liệu `gs\` hay không.

## 4. Hướng tiếp (cần duyệt)
1. VM thử riêng: clone từ `JX-Server` lưu trữ hoặc dựng mới, MAC/IP mới, DB riêng. Chủ máy đã nói "chưa tạo VM", nên đây là câu hỏi mới.
2. Chạy bản tự dựng 18 Hz trong VM thử, so với exe gốc (cổng, nạp bản đồ, 18 Hz, khe lệnh).
3. Nghiên cứu khe lệnh đơn (`KNpc::ProcCommand`/`SendSerCommand`, `NpcRunCommand`/`NpcSkillCommand`) bằng đọc mã, không cần VM; làm được ngay.
4. Nhánh 36 Hz theo báo cáo 34 mục 5, chỉ sau bước 2.

## 5. Không làm
Không chạy exe nào, không đụng VM, `JX-Server-D`, CDN, forwarder, repo, không commit. Thêm ngoài repo: `D:\JX-build\_bin_v2_`, `shim`, `logs`, `src18\Directory.Build.props`.
