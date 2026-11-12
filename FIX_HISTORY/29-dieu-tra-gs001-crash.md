# 29 - Điều tra gs001 crash 0xC0000005 khi nạp

Ngày: 2026-11-11, 17:20 đến 18:10 giờ máy thật. VM: `JX-Server-D` (UUID `<uuid>`). Không sửa source, cấu hình hay dữ liệu game; không commit.

## TÓM TẮT 5 DÒNG
1. `gs001` không crash vì dữ liệu bản đồ hay script theo giờ. Nó crash vì **một kết nối TCP mở rồi đóng vào cổng 51189 trong lúc `gs001` còn đang nạp** (khoảng 7 phút đầu).
2. Bằng chứng: dump cho thấy luồng mạng của `Heaven.dll` (không phải luồng nạp bản đồ) đọc địa chỉ 0 tại `gs001.exe+0x1EF81`; mã máy tại đó là lời gọi hàm ảo qua `this+0x158` đang NULL; mã nguồn mở cổng 51189 trước khi tạo `m_pCoreServerShell`.
3. Nguồn kết nối: các lần tôi thử nối 51189 từ máy thật để "kiểm tra cổng". Buổi sáng không ai nối vào khi nạp nên chạy được.
4. Cách tránh không cần sửa gì: không nối vào 51189 (kể cả mở game trên điện thoại) cho tới khi `gs001` nạp xong. Chạy lại theo cách này thì `gs001` qua được chỗ từng crash (xem mục 6).
5. Dump chưa đưa được ra máy thật (script `lay_dump_tu_vm.ps1` chưa chạy); đã đọc dump ngay trong VM bằng PowerShell.

**Cần tôi quyết định: không.**

## 1. Log crash (sự thật đã kiểm)
- Task `JX-gs001`: `LastTaskResult = 0xC0000005` lúc chạy 17:14:14.
- `gs\gameser_log\gs001\2026_11_11\17_20_03_469.log`: bắt đầu nạp bản đồ 17:20:03, dòng cuối 17:20:27 là `中原北区\汴京\铁塔迷宫2.wor` (ID 39).
- `KSubWorld.cpp:923` ghi dòng log **trước** khi nạp `.wor`, nên dòng cuối là bản đồ đang nạp khi crash. Log sáng 09:20 qua được đúng chỗ đó (dòng kế tiếp `铁塔迷宫3.wor`) và có 809 dòng.
- Dump do chính `gs001` ghi: `gs\DumpInfo\v1.0-20261111-172027-2228-5348.dmp` (12.509.256 byte; PID 2228, TID 5348).
- Console `gs001` hiển thị chậm hơn log rất nhiều (console ở bản đồ 23 khi log đã tới 44). Đánh giá tiến độ bằng log, không bằng console.

## 2. Hướng A: script và dữ liệu (chỉ đọc trên máy thật)
- Bản đồ "thứ 45" theo yêu cầu thực tế là: dòng log 44 = `World38=39` = ID 39 `铁塔迷宫2` (Thiết Tháp tầng 2). ID 45 là `天忍教室外` (loại `Tong`, không nạp NPC).
- `MapList.ini` ID 38, 39, 40 cấu hình gần như giống nhau (Cave, cấp NPC 55, `revive5x.lua`, vàng 3000). ID 38 nạp được.
- `revive5x.lua`: chỉ đặt kỹ năng, sát thương, kháng, kinh nghiệm theo ngũ hành và loại quái vàng; **không** có điều kiện giờ, ngày hay sự kiện. `newworldscript.lua`: các hàm rỗng hoặc đã comment.
- Mã nạp NPC (`KRegion.cpp:630-782`, `KNpcSet.cpp:527-632`) dùng số ngẫu nhiên (`srand(time(NULL))` ở `KCore.cpp:251`) cho ngũ hành, cấp, quái vàng, và chạy `OnRevive` cho mỗi NPC thường. Không có nhánh theo giờ.
- Kết luận A: không có bằng chứng crash liên quan đến script hay giờ trong ngày.

## 3. Hướng B: dump
- Không có công cụ debug trên máy thật (`cdb`, `windbg`, `dumpchk` không có; Python không có `minidump`, `pefile`, `capstone`). Không cài thêm.
- Đưa dump ra máy thật: đã soạn `docs-analysis/scripts/lay_dump_tu_vm.ps1` (hỏi mật khẩu `<vm-admin>` bằng `Get-Credential`, chép qua WinRM tới `D:\JX-dump`, so SHA256). **Chưa được chạy** nên dump vẫn chỉ ở trong VM.
- Đã đọc dump trực tiếp trong VM bằng PowerShell (đọc byte theo định dạng minidump, không ghi gì):

| Mục | Giá trị |
|---|---|
| Streams | 0, 3, 4, 5, 6, 7, 15, 21, 22 |
| Ngoại lệ | `0xC0000005`, **đọc** địa chỉ `0x0` |
| Vị trí | `gs001.exe+0x1EF81` (RIP `7FF747B5EF81`), luồng 5348 |
| Thanh ghi | Rax, Rbx, Rcx, Rdx, Rdi, Rbp = 0; Rsi `793C970` |
| Module | 42; `gs001.exe` 64 bit, `Engine.dll`, `CoreServer.dll`, `LuaLibDll.dll`, `libdb181.dll`, `Heaven.dll`, `Rainbow.dll` |
| Luồng | 16; luồng đầu (chính) là 2552, **luồng crash 5348 không phải luồng chính** |

- Ngăn xếp luồng 5348 (địa chỉ trả về tìm thấy, từ trong ra ngoài): `gs001.exe+0x321D4`, `+0x1EDCD`, `+0xF96F`, `+0x7F038`, `+0xF8F9`, `Heaven.dll+0x717E`, `+0x7767`, `+0x7892`, `+0x19497`, `+0x1952B`, `+0x505D0`, `kernel32+0x17374`, `ntdll+0x4CC91`. Tức là một luồng do `Heaven.dll` (thư viện mạng phía server) tạo, gọi callback của `gs001`.
- `gs001.exe` trong VM trùng SHA256 với bản trong repo (`DD44D425E205FD48…`). Byte tại RVA `0x1EF81` trong file:
  ```
  48 8B 4C 24 50          mov rcx,[rsp+50h]     ; this
  48 8B 89 58 01 00 00    mov rcx,[rcx+158h]    ; thành viên tại 0x158
  48 8B 00                mov rax,[rax]          ; <- crash, rax = 0 (đọc vtable)
  8B 54 24 34             mov edx,[rsp+34h]      ; tham số int
  FF ..                   call [rax+...]
  ```
  Đây là lời gọi hàm ảo `con_trỏ->Hàm(int)` khi con trỏ thành viên NULL.

## 4. Đối chiếu mã nguồn
- `KSOServer.cpp:856-860`: `m_pServer->Startup()`, `RegisterMsgFilter(..., ServerEventNotify)`, `OpenService(INADDR_ANY, m_nServerPort)` mở cổng 51189.
- `KSOServer.cpp:951-952`: sau đó mới `m_pCoreServerShell = ::CoreGetServerShell(...)` (nạp script và bản đồ, khoảng 7 phút). Trước đó `m_pCoreServerShell = NULL` (`:324`).
- `ServerEventNotify` (`:153-185`): kết nối mới → `SetNetStatus(id, enumNetConnected)` (thêm nút); kết nối đóng → `SetNetStatus(id, enumNetUnconnect, true)`.
- `SetNetStatus` (`:4932-4984`): khi đóng, nếu trạng thái chưa phải đang chơi thì gọi `m_pCoreServerShell->PreparePlayerForLoginFailed(nIndex)` (`:4966`). Nếu shell còn NULL thì đọc vtable tại 0, khớp dump.
- Mã nguồn có thể không khớp hoàn toàn với exe; nhưng mẫu mã máy, luồng mạng và thứ tự khởi tạo đều khớp.

## 5. Nguồn kết nối vào 51189 lúc nạp
- Tường lửa VM chỉ cho máy thật `<LAN-IP>` vào 51189. Trên máy thật chỉ có forwarder (khi điện thoại nối) và các lệnh thử của tôi.
- `forwarder.log` không có dòng `NHAN`/`TU CHOI` nào từ 15:30 tới khi viết báo cáo: điện thoại không nối vào.
- Các lần tôi thử cổng 51189 từ máy thật (`TcpClient` mở rồi đóng): trên `JX-Server` (archive) lúc 16:34, 16:39, 16:45 – mỗi lần ngay sau đó `gs001` mất; trên `JX-Server-D` một lần ngay khi vòng theo dõi kết thúc (khoảng 17:20). Đồng hồ VM và máy thật có thể lệch vài giây nên thứ tự chính xác ở lần cuối chưa kiểm chứng, nhưng không có nguồn kết nối nào khác.
- Buổi sáng `gs001` nạp lúc 09:15-09:22, forwarder chỉ có từ 10:10; không ai nối vào lúc nạp.

## 6. Kết quả chạy lại (không sửa gì, không chạm 51189 khi nạp)
- 17:58:27 chạy task `JX-gs001` (exe SHA256 `DD44D425E205FD48…`, trùng repo). Chỉ theo dõi bằng ảnh chụp màn hình, không nối vào 51189; `forwarder.log` không có kết nối mới.
- Qua bản đồ 39-40 (chỗ từng crash), bản đồ 88-89 lỗi `.wor` như đã biết (nhóm 28 bản đồ).
- 18:04:48 `End of Init, Game Started`; nối Database 5001, Transfer 5003, Chat 5004, Tong 5005, Gateway 56732; `Server start succeeded`; `[Online= 0]`, `SvrFPS= 18/18`. Tổng thời gian khoảng 6,5 phút.
- Máy thật: CDN `<TAILSCALE-IP>:8080` (PID 4612), forwarder 56722/51189 (PID 16736) đang nghe; `JX-Server-D` là VM duy nhất đang chạy.

## 7. Có bằng chứng / giả thuyết
- **Có bằng chứng:** crash là đọc NULL trong luồng mạng `Heaven.dll` khi xử lý sự kiện kết nối của cổng client, trước khi `m_pCoreServerShell` được tạo; không liên quan tới dữ liệu bản đồ 39.
- **Có bằng chứng gián tiếp:** kết nối gây crash là lệnh thử cổng của tôi (thời điểm trùng, không nguồn khác).
- **Giả thuyết đã loại:** script phụ thuộc giờ (không tìm thấy); thiếu bộ nhớ (RAM trống 3,5 GB, không phải lỗi cấp phát); khác biệt giữa hai VM (crash giống nhau, cùng exe).
- **Chưa kiểm chứng:** tên chính xác của hàm tại `gs001.exe+0x321D4`/`+0x1EDCD` (không có PDB, không có trình dịch ngược); dump chưa phân tích trên máy thật.

## 8. Phòng tránh về sau (đề xuất, chưa làm)
- Quy trình: sau khi chạy `gs001`, không thử cổng 51189 và không mở game cho tới khi log có đủ bản đồ (dòng "Map Load Sucessed") và `gs001` đã nối gateway.
- Kiểm tra sẵn sàng bằng cách đọc trong VM (`Get-NetTCPConnection` tới 56732/5001), không nối vào 51189.
- Sửa gốc (chỉ khi chủ máy muốn dựng lại exe): kiểm tra `m_pCoreServerShell != NULL` trong `SetNetStatus`, hoặc mở cổng sau khi nạp xong.
