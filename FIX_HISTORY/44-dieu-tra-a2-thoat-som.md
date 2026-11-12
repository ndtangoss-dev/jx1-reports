# 44 - gs001 A2 thoát ngay sau dòng IP: nguyên nhân và cách chạy A2

## TÓM TẮT 5 DÒNG
1. Lỗi không do thay đổi A2 (CoreServer/Engine/LuaLibDll): gs001 gốc + DLL A2 qua được khởi tạo và sống >60 s (T2).
2. Lỗi nằm ở `gs001.exe` tự build từ source GameServer (phần A2 không sửa): cùng DLL gốc vẫn thoát với mã `0xC0000005` (access violation) ngay sau dòng "public net IP" (T1).
3. Chưa xác định dòng mã cụ thể. Hướng nghi ngờ nhất: `KSOServer.cpp` `InitServer` đoạn 941-960 (QueryInterface và OperationRequest) và sai lệch header `IServer.h` (bản Interface 2018 có 5 tham số `SetEnvironment`, bản Headers 2022 có 4). Chưa kiểm chứng.
4. Đã chạy A2 thử bằng gs001 gốc + DLL A2 (tác vụ `JX-gs001-A2T2`, thư mục `C:\JX\Bisect\T2`). Chưa có bằng chứng server đã nạp xong.
5. Không rebuild, không sửa source, không đụng JX-Server-D.

**Cần tôi quyết định: không.**

## Bằng chứng
| Thử | exe | DLL | Kết quả |
|---|---|---|---|
| Gốc (ServerNew) | gốc | gốc | Nạp đủ, đã chạy trước đó (báo cáo 29) |
| A2 đầy đủ | tự build | tự build | Thoát ngay sau "public net IP" |
| T1 | tự build | gốc | Thoát ngay, mã 0xC0000005 |
| T2 | gốc | tự build (A2) | Sống >60 s, qua khởi tạo |

- Mã thoát lấy qua `cmd /c` (`-1073741819`). Lần trước dùng `%errorlevel%` trong cùng dòng lệnh là sai (cmd mở rộng biến trước khi chạy), nên bỏ qua kết quả đó.
- Không có minidump mới trong `DumpInfo` và không có sự kiện Application Error/WER. Bộ lọc unhandled exception của `GameServer.cpp` không ghi dump trong lần chạy này: cần điều tra thêm.
- Kiến trúc: cả hai `gs001.exe` đều x64 (PE32+), nên không phải lỗi cắt con trỏ 64→32 bit.
- GUID `IID_IIOCPServer` và `IID_IServerFactory` có mặt đúng trong cả hai exe.
- Chuỗi "virtual IP" và "public net IP" in ra đúng ở cả hai exe, nên lỗi xảy ra sau khi đã khởi tạo mạng.

## Đối chiếu với báo cáo 29
- Báo cáo 29 ghi crash `0xC0000005` đọc địa chỉ 0 trong luồng Heaven.dll, khi cổng 51189 có kết nối. Lần này cũng là `0xC0000005` nhưng xảy ra sớm hơn và không có kết nối nào vào 51189 (đã kiểm: không có client, chỉ có kết nối nội bộ PaySys→SQL dùng cổng nguồn 51189, đã loại bằng excludedportrange).
- Cùng lớp lỗi (truy cập NULL/vtable trong vùng IIOCP/Heaven) nhưng khác thời điểm. Nghi ngờ cùng gốc: `m_pServer`/`pCloneServer` từ `QueryInterface` không khớp vtable của Heaven.dll đang nạp.

## Đã loại trừ
- Thay đổi A2 (`KNpc`, `KProtocolProcess`, `CoreServerShell`): loại trừ, vì T2 chạy được với DLL A2.
- Thiếu `CmdLane.ini`: loại trừ (đã thử đổi tên, vẫn thoát).
- Bị `TerminateProcess` từ `KForBitGua`/`KNpc.cpp:1192`: không chạy, các đoạn đó nằm trong khối comment.
- `exit(0)` ở `KProtocolProcess.cpp:8235`: chỉ chạy với lệnh GM "TatGS".
- Cắt con trỏ 64→32 bit: có trong cả hai bản (đã kiểm `pCloneServer` truyền qua `unsigned int`), không phân biệt được hai bản.

## Việc tiếp theo (chưa làm)
1. Đọc `gs001.pdb` tự build để map RVA của lỗi (cần tên module + địa chỉ exception; chưa có dump).
2. So header: dùng `Headers\IServer.h` (2022) hay `MultiServer\Heaven\Interface\IServer.h` (2018) cho `KSOServer.cpp`. Chỉ thử sau khi có bằng chứng từ bước 1, vì cần rebuild.
3. Dùng gs001 gốc + DLL A2 làm đường chạy A2 tạm thời (đang thử).

## C?p nh?t 02:40 - NGUYÊN NHÂN ĐĂ XÁC Đ?NH
TÓM T?T 5 D̉NG
1. gs001 A2T2 ch?t ~2,5 phút sau khi ch?y do `long dir = _findfirst(...)` (KSortScript.cpp:328, LoadScriptInDirectory) c?t c?t handle 64 bit; `_findnext` ghi d?a ch? rác 0xFFFFFFFFB4D86390 (b?ng ch?ng: b? g? l?i nh? + file .map, dump trong VM).
2. Không ph?i do patch A2; k?t lu?n "T1 ch?t do gs001.exe t? d?ng" v?n là m?t l?i riêng chua x? lư.
3. S?a `intptr_t`, d?ng l?i CoreServer.dll, ch?y l?i: s?ng >10 phút, n?p h?t b?n d?, nghe 51189, n?i Goddess 5001 và Bishop 56732, c?ng qua d?a ch? Tailscale m? du?c t? máy th?t.
4. Chua ki?m tra: di?n tho?i vào game; A2 th?c s? gi?m tr? (CmdLane_stat.log chua có v́ chua có ngu?i choi); S3Relay v?n t?t nên gs001 báo reconnect Tong/Chat/Transfer.
5. Task WER LocalDumps không b?t du?c v́ gs001 t? x? lư ngo?i l?; dùng b? g? l?i `patches/fix-findfirst/minidbg.cs`.

C?n tôi quy?t d?nh: không
