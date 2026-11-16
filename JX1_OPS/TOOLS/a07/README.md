# A-07 – build tĩnh và debugger trong VM thử

**Chưa chạy build/debugger; chỉ kiểm cú pháp script.**

## Build tĩnh trên máy phát triển

~~~powershell
& .\JX1_OPS\TOOLS\a07\build-debug-a07.ps1
~~~

Cần quyền ghi D:\JX-build\a07. Script từ chối thư mục đã có, giữ checkpoint; copy source cần thiết, dựng Common + GameServer Debug x64 /MT /Od /Zi /RTC1, gs001.exe/PDB/map và logs\commands.txt. Không dựng DLL/chạy exe. Core dùng Server Debug, không gọi Core với Configuration=Debug.

Nếu link __imp___iob_func từ ms64.lib, xem log/báo cáo 35; chỉ dùng -IobShimObject khi object/ABI đã kiểm riêng. Không tự mô phỏng FILE khác CRT. Build thành công không xác nhận runtime.

## VM JX-Test-36

VM đang treo; A-07 không bật/reset. Người vận hành kiểm đúng guest VirtualBox JX-Test-36, mạng Host-only/NAT đúng phạm vi, không bridged/port-forward, quét Defender thành công và lưu log/audit trước khi chạy. Không dùng dữ liệu/tài khoản thật. -VmName xác nhận tên VM; guard còn kiểm hãng/model VirtualBox, không đoán từ COMPUTERNAME.

Copy exe + PDB mới vào **bản copy package thử** có đầy đủ DLL/config/dữ liệu giả. Không chạy từ out chỉ có exe. Hash được script lưu local; không tự trộn DLL khác phiên bản.

## WER / hoàn tác (PowerShell Admin x64 trong VM)

~~~powershell
& .\enable-wer-localdumps.ps1 -VmName JX-Test-36
& .\enable-wer-localdumps.ps1 -VmName JX-Test-36 -Disable
~~~

Giữ cùng StateRoot khi hoàn tác: D:\JX-build\a07\wer-state; dump: D:\JX-build\a07\dumps. Restore cả key cũ nếu có, không xóa dump/backup. Bộ lọc riêng có thể ngăn WER; ưu tiên cdb first-chance.

## cdb x64 (chỉ trong VM)

Ví dụ đường dẫn, phải thay bằng package thử/cdb thực đã kiểm:

~~~powershell
& .\debug-gs001.ps1 -VmName JX-Test-36 -ExePath 'D:\JX-Test\A07\gs\gs001.exe' -SymbolPath 'D:\JX-build\a07\out' -CdbPath 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe' -IsolationAndDefenderChecked
# Them -ProgramArguments @('gs001') CHI neu day la tham so da xac nhan cua package.
~~~

Capture theo timestamp gồm hash, cdb.log, first-av.dmp. cdb chỉ dùng PDB local, bắt AV trước bộ lọc riêng, lưu dump rồi dừng cho người vận hành; không tự continue qua lỗi hoặc dừng server khác.

WinDbg mở dump, hoặc cdb -z <dump> -y <PDB local>, rồi:

~~~text
.lines -e
.reload /f
.exr -1
.ecxr
kv
lmvm gs001
lmvm CoreServer
!analyze -v
ln @rip
ub @rip L10
bu gs001!KSwordOnLineSever::InitServer
bu gs001!KSwordOnLineSever::SetNetStatus
bu CoreServer!CoreGetServerShell
~~~

Dùng source breakpoint sau QueryInterface tại KSOServer.cpp:944 và trước OperationRequest :960 với PDB đúng. Ghi HRESULT, pCloneServer đầy đủ, m_pCoreServerShell, thread, g_pServer. Nếu Core gốc không có PDB, ghi module+RVA/disassembly; không gán source line bằng PDB khác GUID/age. Dump/log giữ local, không đưa vào Git/dịch vụ ngoài.
