TÓM TẮT 1: [NGUỒN][THẤY] XD-A07 hoàn tất đối chiếu tài liệu: 9/9 nguồn nghiệp vụ, 15/15 vế có bằng chứng hoặc phần thiếu; chưa đủ cơ sở đóng A-07 (TASKS/A-07.md:22–31; TASKS/BACKLOG.md:30).
TÓM TẮT 2: [NGUỒN][TÀI LIỆU] Bảng so sánh, nghi vấn và hướng dẫn WER/cdb đã có; bước 1 ghi nhận dùng snapshot đã vá, bước 3–6 vẫn chưa làm (REPORTS/A-07-goc-re-crash-gs001.md:79–179; REPORTS/A-07-buoc1b-snapshot-da-va.md:1–12).
TÓM TẮT 3: [NGUỒN][THẤY] Đầu ra là JX1_OPS/REPORTS/XD-A07.md và mục Kết quả của task; giữ nguyên báo cáo/kết luận cũ theo phạm vi giao (TASKS/XD-A07.md:12,20–26).
TÓM TẮT 4: [CHƯA KIỂM] Chưa có bằng chứng dump/RIP/PDB xác định dòng crash gốc; xác nhận VBoxSVC/VM, Defender và PDB khớp còn thiếu (REPORTS/A-07-goc-re-crash-gs001.md:188; REPORTS/A-07-buoc1b-snapshot-da-va.md:3–12).
TÓM TẮT 5: [CHƯA KIỂM] XD-A07 không chạy build/exe/VM/mạng; không commit/push theo yêu cầu, Tổng quan nhận bàn giao; ghi .nhip ngoài workspace bị từ chối quyền (lệnh WriteAllText → Access denied, mục 7).

# XD-A07 — Đối chiếu tiêu chí đóng A-07

Loại: tổng hợp
Chủ đề: Đánh giá bằng chứng sẵn có để đóng việc điều tra crash gs001 sau log public net IP.
Từ khóa: gốc rễ lỗi, crash, gs001, A-07, Debug, PDB, VBoxSVC, HighEntropyVA, WER, cdb
Trạng thái: DONE — hoàn tất phần đối chiếu XD-A07; việc cha A-07 CHƯA ĐẠT điều kiện đóng.
Độ phủ: 9/9 tệp nguồn nghiệp vụ; 15/15 vế được đối chiếu, không đồng nghĩa 15 vế đã đạt; 4/4 đường dẫn công cụ được kiểm tra tồn tại.
Liên quan: JX1_OPS/TASKS/A-07.md; JX1_OPS/TASKS/BACKLOG.md; bảy báo cáo ở bảng nguồn; JX1_OPS/DESIGN/CHUAN-BAO-CAO.md.
Cần tôi quyết định: có — để tiếp tục A-07, chủ/PM cần xác nhận trạng thái VBoxSVC/các VM và giao bước tiếp theo; XD-A07 không thực hiện thao tác đó.

[THẤY] Ngày đối chiếu: 19/11/2026, Asia/Bangkok; lệnh Get-Date trả 2026-11-19 03:37:16 +07:00 trước khi soạn. Lệnh git status --short --branch đầu lượt trả đúng task/XD-A07 và không có thay đổi. Quyền XD-A07 chỉ là đối chiếu, không kế thừa quyền build/runtime của task cha (JX1_OPS/TASKS/XD-A07.md:19–26).

[TÀI LIỆU] Quy ước đường dẫn: TASKS/… = JX1_OPS/TASKS/…; REPORTS/… và tên báo cáo A-07*.md đứng riêng = JX1_OPS/REPORTS/… trong worktree hiện tại. Số dòng trong báo cáo này trỏ tới bản tài liệu đang đọc, không phải dòng source đã được XD-A07 kiểm lại. Nguồn nghiệp vụ do TASKS/XD-A07.md:19 chỉ định.

[THẤY] Nhãn bằng chứng: THẤY = nội dung tệp hoặc kết quả lệnh đọc trực tiếp trong lượt này; TÀI LIỆU = dữ kiện kỹ thuật/build/VM do tài liệu cũ ghi nhận; CHƯA KIỂM = thiếu bằng chứng hoặc chưa tái kiểm. Nhãn THẤY đối với văn bản không xác nhận runtime được mô tả trong văn bản đó. Cách phân biệt theo TASKS/XD-A07.md:20 và A-07-goc-re-crash-gs001.md:209–223.

## Sơ đồ chính

~~~mermaid
flowchart TD
    T["Tiêu chí task A-07 và BACKLOG"] --> D["Đối chiếu 7 báo cáo A-07"]
    D --> E["Đã có tài liệu: so PE/CRT, nghi vấn, WER/cdb"]
    D --> H["Lịch sử build và thử snapshot đã vá"]
    H --> M["Thiếu dump, RIP, PDB khớp để chốt dòng crash"]
    D --> V["Bước 3–6: dừng chờ xác nhận VBoxSVC/VM"]
    E --> K["Chưa đủ bằng chứng đóng A-07"]
    M --> K
    V --> K
    K --> X["XD-A07 hoàn tất đối chiếu; bàn giao phần thiếu"]
~~~

## 1. Phạm vi và độ phủ

[THẤY] Danh sách nguồn được chốt từ TASKS/XD-A07.md:19 trước khi đọc nội dung liên quan. Tìm tên chỉ trong kho JX1_OPS; không quét thư mục mã nguồn. Bảy báo cáo dưới đây do Get-ChildItem trong REPORTS lọc A-07* trả về; không có XD-A07.md trước lượt này.

| Tệp nguồn nghiệp vụ | Độ phủ đọc/đối chiếu | Bằng chứng dùng |
|---|---|---|
| TASKS/A-07.md | [THẤY] Đã phủ | :22–33 mục tiêu/tiêu chí; :35–53 kết quả, phần thiếu và bàn giao. |
| TASKS/BACKLOG.md | [THẤY] Đã phủ dòng A-07 | :30 yêu cầu Debug/symbol, dump/debugger trong VM thử, so cờ/thư viện và dòng lỗi. |
| REPORTS/A-07-goc-re-crash-gs001.md | [THẤY] Đã phủ | :79–179 luồng, giả thuyết, PE/CRT, Debug và WER/cdb; :188–223 giới hạn/kết luận. |
| REPORTS/A-07-buoc1-dung-debug.md | [THẤY] Đã phủ | :1–10 dựng nguồn nguyên gốc thất bại và hướng đề xuất. |
| REPORTS/A-07-buoc1b-snapshot-da-va.md | [THẤY] Đã phủ | :1–12 snapshot, PDB, Defender và điểm dừng VBoxSVC. |
| REPORTS/A-07b-ep-con-tro.md | [THẤY] Đã phủ | :83 dòng baseline dịch; :148–209 build/link, giới hạn và Git lịch sử. |
| REPORTS/A-07c-link-gs001.md | [THẤY] Đã phủ | :70–129 audit shim, lệnh build, artifact; :133–160 cập nhật VM và giới hạn. |
| REPORTS/A-07d-breakpoint.md | [THẤY] Đã phủ | :58–150 ứng viên, RTC/timer/pointer; :152–252 kế hoạch dump và giới hạn. |
| REPORTS/A-07e-rtc.md | [THẤY] Đã phủ | :65–167 sửa P1, cờ, build/map, bộ bàn giao và các mốc VM cũ. |

[THẤY] Ngoài 9 nguồn nghiệp vụ, đã đọc chuẩn CHUAN-BAO-CAO.md, task XD-A07 và sáu SKILL.md được yêu cầu; chỉ kiểm tra tồn tại bốn tệp công cụ cụ thể tại mục 3. Không mở source, binary, dump, log runtime, registry hoặc trạng thái VM. Không đọc báo cáo 29/35/41/44 ngoài bộ nguồn: chúng chỉ được A-07-goc-re-crash-gs001.md:65,77 dẫn lại.

## 2. Giải mã tên

[TÀI LIỆU] Đây là đối chiếu điều tra máy chủ, không có tên kỹ năng, vật phẩm, quái, NPC hay bản đồ cần giải mã GBK/TCVN3. Tên dưới đây là tên kỹ thuật ASCII trong tài liệu UTF-8; giữ nguyên, không đổi kết luận cũ (TASKS/A-07.md:23–27; A-07-buoc1b-snapshot-da-va.md:4–12).

| Tên gốc | Mã hóa | Chữ đúng/ý nghĩa tiếng Việt | Nguồn file:dòng |
|---|---|---|---|
| gs001, A2T2, T1 | ASCII trong UTF-8 | Máy chủ và nhãn bộ chạy/lần lỗi; không đồng nhất các binary chỉ theo tên. | A-07-goc-re-crash-gs001.md:54–77,110–125 |
| JX-Test-36 | ASCII trong UTF-8 | VM thử được tài liệu chỉ định; không phải quyền thao tác hiện tại. | TASKS/A-07.md:19 |
| VBoxSVC, VBoxHeadless | ASCII trong UTF-8 | Tên tiến trình VirtualBox được báo cáo bước 1b nêu ở điểm dừng. | A-07-buoc1b-snapshot-da-va.md:4–12 |
| CoreServer, Engine, Common, LuaLibDll, GameServer | ASCII trong UTF-8 | Các thành phần xuất hiện trong bảng build; chưa kiểm lại artifact. | A-07e-rtc.md:108–116 |
| HighEntropyVA, ASLR, PDB, WER, cdb | ASCII trong UTF-8 | Tên cờ/cơ chế, tệp symbol và công cụ dùng trong chuỗi bằng chứng. | A-07-goc-re-crash-gs001.md:110–179 |
| MiraclLegacyStdio, ms64.lib | ASCII trong UTF-8 | Shim và thư viện legacy được audit ở A-07c. | A-07c-link-gs001.md:63–78 |

## 3. Sắp theo cấu trúc game và ma trận tiêu chí

[TÀI LIỆU] Phạm vi không phải dữ liệu gameplay để xếp theo phái/nhánh/cấp. Báo cáo xếp theo chuỗi vận hành máy chủ: nhận diện binary → dựng/cờ/ABI → đường khởi động/nghi vấn → thu dump → bàn giao, bám TASKS/A-07.md:22–33 và TASKS/BACKLOG.md:30.

[TÀI LIỆU] “Đủ tài liệu” ở ma trận chỉ xác nhận nội dung đã được viết. “Chưa đạt” là phần chưa có bằng chứng để đóng A-07. Mốc xác nhận bước 1 trong báo cáo 1b được giữ nguyên; bảng cũng nêu khác biệt giữa cấu hình Debug nguyên văn với snapshot Release/Server Release có /Od /Zi (A-07-buoc1b-snapshot-da-va.md:1,8,11; A-07e-rtc.md:96,116).

| Mã | Vế cần đối chiếu và nguồn tiêu chí | Bằng chứng hiện có | Đánh giá / phần còn thiếu |
|---|---|---|---|
| C01 | Tìm dòng mã gây 0xC0000005 sau public net IP — TASKS/A-07.md:23; TASKS/BACKLOG.md:30 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:94–104,188 còn nhiều giả thuyết, chưa có dump T1; A-07d-breakpoint.md:73,112 cũng chưa chốt lần dừng 225 giây. | [CHƯA KIỂM] Chưa đạt mục tiêu gốc; cần exception/RIP, stack, module và source/PDB đúng lần lỗi. |
| C02 | Dựng bản Debug có PDB — TASKS/A-07.md:24 | [TÀI LIỆU] A-07-buoc1-dung-debug.md:1–4 ghi 31 lỗi Common, không exe; A-07-buoc1b-snapshot-da-va.md:1–2,8–11 ghi bước 1 đạt nhờ snapshot đã vá, có PDB; A-07e-rtc.md:96,142 ghi cấu hình Release/Server Release và bộ PDB. | [CHƯA KIỂM] Giữ kết quả bước 1 đã ghi nhận, không buộc dựng lại trong XD-A07; chưa chứng minh cấu hình Debug nguyên văn và GUID/age EXE/DLL–PDB. PM cần xác nhận chấp nhận snapshot và kiểm symbol đúng bộ. |
| C03 | Tắt tối ưu hóa — TASKS/A-07.md:24 | [TÀI LIỆU] A-07e-rtc.md:116 ghi 239 lệnh compile giữ /Od /Zi /MT. | [TÀI LIỆU] Đủ bằng chứng tài liệu cho snapshot A-07e; chưa đọc tlog/build lại trong lượt này. |
| C04 | Thêm /RTC nếu có thể — TASKS/A-07.md:24 | [TÀI LIỆU] A-07c-link-gs001.md:88 có /RTC1; A-07d-breakpoint.md:97–112 nêu ứng viên; A-07e-rtc.md:65–68,116–131 ghi bỏ instrumentation và map còn symbol CRT. | [TÀI LIỆU] Điều kiện tùy khả năng đã có diễn giải; không bật lại /RTC để “đủ dấu”. [CHƯA KIỂM] Verifier exit 0 không làm tiêu chí map literal của A-07e thành đạt. |
| C05 | Ghi lệnh dựng — TASKS/A-07.md:24,33 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:131–145 tách lệnh dự kiến; A-07c-link-gs001.md:82–90 và A-07e-rtc.md:98–106 ghi lệnh lịch sử cùng vị trí commands.jsonl. | [TÀI LIỆU] Đủ tài liệu; không coi lệnh dự kiến ban đầu là build đã chạy. |
| C06 | So cờ biên dịch, /MT hay /MD — TASKS/A-07.md:25 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:110–125 so PE/cờ/CRT, nêu chưa khôi phục chắc cờ compiler gốc; A-07e-rtc.md:88–92 ghi đổi lựa chọn CRT của Engine. | [TÀI LIỆU] Đủ bảng và giới hạn suy luận. [CHƯA KIỂM] Cờ gốc chính xác, allocator/ABI qua DLL chưa được xác nhận runtime. |
| C07 | So thư viện — TASKS/A-07.md:25,31 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:115–123 so DLL/import/export; A-07b-ep-con-tro.md:156–160 ghi link ms64.lib lỗi; A-07c-link-gs001.md:70–78 ghi shim cho 97 mẫu gọi cụ thể. | [TÀI LIỆU] Đủ nội dung so sánh; audit shim có giới hạn, không chứng minh ABI mọi thư viện vendor. |
| C08 | Kiểu 32/64-bit, PE, import/export, linker và nghi vấn VS2010 x86/x64 — TASKS/A-07.md:25 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:104,112–125 ghi O và R đều x64/PE32+, linker 10.00 và 14.44, width 8/4 byte, import/export. | [TÀI LIỆU] Đủ bảng để bác bỏ giả định khác kiến trúc theo tài liệu; linker 10.00 không chứng minh toàn bộ tùy chọn/toolchain gốc. |
| C09 | Đọc đường sau log, liệt kê NULL/cắt pointer/long/DWORD có dòng — TASKS/A-07.md:26 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:83–104 có QueryInterface :944, CoreGetServerShell :952, OperationRequest :960, callback :4966, _findfirst :328; A-07b-ep-con-tro.md:83 cảnh báo dòng/snapshot đã đổi. | [TÀI LIỆU] Đủ danh sách nghi vấn của source lịch sử. [CHƯA KIỂM] XD-A07 không mở lại source; không gán các dòng này cho binary khác. |
| C10 | Giả thuyết xếp hạng và cách kiểm từng cái — TASKS/A-07.md:29 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:96–102 có 5 hạng và phép kiểm; A-07d-breakpoint.md:101–112,240–248 bổ sung P1/P2 và cách phân loại stack. | [TÀI LIỆU] Đủ tài liệu; ứng viên tĩnh chưa phải dòng lỗi đã chứng minh. |
| C11 | Script WER LocalDumps — TASKS/A-07.md:27,31 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:149,187 ghi enable-wer-localdumps.ps1, backup/restore và parser; A-07d-breakpoint.md:158–179 nêu custom handler có thể chặn WER. [THẤY] Test-Path của script trả True. | [TÀI LIỆU] Có tệp và mô tả. [CHƯA KIỂM] Chưa đọc lại nội dung/chạy parser hoặc registry; chưa chứng minh WER thu dump thành công. |
| C12 | Script/lệnh cdb hoặc WinDbg và cách đọc dump — TASKS/A-07.md:27,31 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:151–179,187 mô tả debug-gs001.ps1; A-07d-breakpoint.md:181–248 có first-chance, context và cách đọc. [THẤY] Test-Path của debug-gs001.ps1 và README.md trả True. | [TÀI LIỆU] Đủ hướng dẫn, chưa thực thi trong XD-A07. [CHƯA KIỂM] Cần EXE/DLL/PDB đúng bộ và dump thực; đề xuất của lượt này chỉ dùng symbol local, không mạng. |
| C13 | Báo cáo A-07 có 5 dòng tóm tắt — TASKS/A-07.md:31 | [THẤY] A-07-goc-re-crash-gs001.md:1–5 có đủ 5 dòng; :52–58 bảo toàn tóm tắt gốc. | [THẤY] Đạt về cấu trúc văn bản. |
| C14 | Commit trên nhánh việc cha, tiêu đề bắt đầu A-07 — TASKS/A-07.md:31 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:190–197 và TASKS/A-07.md:42–50 ghi stage bị chặn, lệnh commit chưa thành công. | [CHƯA KIỂM] Bộ nguồn không có bằng chứng commit A-07 hoàn tất; cần Tổng quan xác nhận SHA/tiêu đề/nhánh. XD-A07 không stage/commit theo yêu cầu hiện tại; không lấy HEAD của việc con hay commit R-01 thay thế. |
| C15 | Bật dump/chạy debugger trong VM thử để đạt dòng lỗi — TASKS/BACKLOG.md:30; TASKS/A-07.md:19,23,27 | [TÀI LIỆU] A-07e-rtc.md:162–167 có thử sống qua các mốc lỗi; A-07-buoc1b-snapshot-da-va.md:5,11–12 vẫn ghi chưa runtime, PDB khớp và dừng bước 3–6. | [CHƯA KIỂM] Các mốc thử không thay bằng chứng dump/debugger đúng lần crash. Cần gỡ điểm dừng có phê duyệt, đủ điều kiện an toàn rồi thu bằng chứng; XD-A07 không làm thật. |

[THẤY] Kiểm tra chỉ sự tồn tại, không mở/chạy tệp: Test-Path -LiteralPath <đường_dẫn> -PathType Leaf trả True cho JX1_OPS/TOOLS/a07/build-debug-a07.ps1, enable-wer-localdumps.ps1, debug-gs001.ps1 và README.md (4/4). Nội dung và cú pháp công cụ chỉ được dẫn từ A-07-goc-re-crash-gs001.md:129,149–151,187; không nhận parser lịch sử là test mới.

## 4. Diễn tiến cần giữ nguyên khi xét đóng việc

| Mốc/bộ bằng chứng | Điều tài liệu ghi nhận | Giới hạn khi dùng để đóng A-07 |
|---|---|---|
| Khảo sát gốc và phụ lục 17/11/2026 01:25 | [TÀI LIỆU] A-07-goc-re-crash-gs001.md:188 chưa có dòng T1; :200–206 ghi thử HighEntropyVA và nghi cắt pointer. | [CHƯA KIỂM] Không biến kết quả so cờ thành dump/stack xác định dòng lỗi; chính :221–223 yêu cầu giữ khác biệt mức bằng chứng. |
| A-07b | [TÀI LIỆU] A-07b-ep-con-tro.md:156–188 ghi DLL build được, gs001 chưa link do ms64.lib, chưa runtime. | [CHƯA KIỂM] Không lấy hash exe của việc khác bù cho bản chưa link. |
| A-07c, 17/11/2026 03:05 và 03:30 | [TÀI LIỆU] A-07c-link-gs001.md:133–142 ghi AV khoảng 40 giây, sau đó breakpoint khoảng 225 giây và phục hồi bộ cũ. | [CHƯA KIỂM] Hai mã lỗi/bộ chạy không tự có cùng nguyên nhân; không chốt timer hoặc pointer chỉ từ thời gian lặp. |
| A-07d | [TÀI LIỆU] A-07d-breakpoint.md:73,103–112 ghi 4 P1 nhưng chưa biết có chạy lúc lỗi; :152–248 là kế hoạch dump. | [CHƯA KIỂM] Danh sách ứng viên và 619 token assertion không phải stack runtime. |
| A-07e, 17/11/2026 04:13 và 04:35 | [TÀI LIỆU] A-07e-rtc.md:162–167 ghi bản đã sửa P1/bỏ instrumentation sống qua 40/225 giây; HEVA bật chạy hơn 10 phút, còn phải thử lâu/có tải. | [CHƯA KIỂM] Không suy ra đã tìm dòng gốc hay đã chữa triệt để; giới hạn map literal vẫn còn ở :118–131,183–184. |
| Dựng bước 1 ngày 18/11/2026 khoảng 19:50 | [TÀI LIỆU] A-07-buoc1-dung-debug.md:1–10 ghi nguồn nguyên gốc lỗi asm/include, 31 lỗi, không exe. | [TÀI LIỆU] Không xóa thất bại này vì snapshot đã vá từng build thành công. |
| Báo cáo bước 1b | [TÀI LIỆU] A-07-buoc1b-snapshot-da-va.md:1–12 ghi tái dùng snapshot A-07e, Defender chưa chạy được, bước 3–6 chưa làm do VBoxSVC/VM. | [CHƯA KIỂM] Không có thời điểm kiểm mới; trạng thái tiến trình/VM hiện tại chưa được đọc trong XD-A07. |

[TÀI LIỆU] “Bước 3” ở báo cáo 1b là bước của quy trình thử được báo cáo dẫn theo thư #175; không phải mục tiêu 3 đọc mã trong TASKS/A-07.md:26. Toàn văn thư/quy trình 3–6 không nằm trong bộ nguồn đã giao, nên không tự dựng lại hoặc tuyên bố các bước đó đã đạt (A-07-buoc1b-snapshot-da-va.md:5,12).

## 5. Chưa kiểm — phần thiếu và cách làm an toàn

[TÀI LIỆU] Các bước dưới đây là bàn giao, không phải lệnh đã chạy hay quyền mới. Rào chắn căn cứ TASKS/XD-A07.md:23–26; TASKS/A-07.md:18–20,49–53; A-07-goc-re-crash-gs001.md:149–179.

| Phần còn thiếu | Bằng chứng phải bổ sung | Cách tiếp tục an toàn, chưa thực hiện |
|---|---|---|
| Điểm dừng VBoxSVC và bước 3–6 | [CHƯA KIỂM] Chủ/PM xác nhận 2 VBoxSVC và 6 VBoxHeadless của mốc cũ thuộc VM nào, có bình thường không; lấy quy trình được duyệt còn thiếu. Nguồn: A-07-buoc1b-snapshot-da-va.md:4–5,12. | [TÀI LIỆU] Giữ nguyên trạng thái; khi được giao, kiểm kê chỉ đọc đúng phiên VirtualBox, phân biệt VM thử/Main VM. Không kill/dọn tiến trình, không bật/tắt/reset hoặc snapshot VM để gỡ điểm dừng. Thao tác đổi trạng thái phải được duyệt riêng. |
| Defender, mạng, log/audit trước khi chạy | [CHƯA KIỂM] Cần kết quả quét hợp lệ; báo cáo 1b:3 ghi Product/Feature disabled. Chưa kiểm điều kiện hiện tại. | [TÀI LIỆU] Chủ/PM bố trí phiên có thể quét hợp lệ; không tắt/bypass bảo vệ. Trước từng EXE server được duyệt trong VM thử, lưu SHA-256, bằng chứng cô lập mạng đúng phạm vi và log/audit; không mở Internet hoặc Main VM (TASKS/A-07.md:19,52; A-07-goc-re-crash-gs001.md:151). |
| Nguồn dựng, bộ EXE/DLL/PDB và cấu hình Debug | [CHƯA KIỂM] Chấp nhận snapshot đã vá hay yêu cầu Debug nguyên cấu hình; đối chiếu manifest/hash, module, GUID/age PDB. Nguồn: A-07-buoc1b-snapshot-da-va.md:8–11; A-07e-rtc.md:96,116,142–148. | [TÀI LIỆU] Tái dùng artifact có bằng chứng, không tự dựng lại; chỉ build trên copy trong phiên có quyền nếu được giao riêng. Không trộn DLL/PDB gốc với snapshot mới, không sửa canonical hoặc ép PDB mismatch (A-07-goc-re-crash-gs001.md:179; A-07d-breakpoint.md:238). |
| Dòng crash T1 và phân biệt AV/breakpoint | [CHƯA KIỂM] Exception code, thread/RIP, stack, module/hash/PDB/source cùng phiên và caller/giá trị liên quan. Nguồn: A-07-goc-re-crash-gs001.md:98–102,188; A-07d-breakpoint.md:238–248. | [TÀI LIỆU] Sau đủ phê duyệt/điều kiện VM, người vận hành chọn WER hoặc debugger first-chance; dùng symbol local, không tự tải symbol qua mạng. Phân biệt breakpoint attach với lỗi, AV 0xC0000005 với 0x80000003; lưu bằng chứng trước khi tiếp tục; dump/log nhạy cảm giữ local. Không tắt HEVA/RTC rồi coi như chứng minh dòng lỗi. |
| Độ ổn định sau sửa và ABI | [CHƯA KIỂM] Thời lượng dài/có tải, đường tương tác và allocator sau đổi CRT; map literal còn symbol. Nguồn: A-07e-rtc.md:92,120–131,161–167. | [TÀI LIỆU] Giao kiểm thử riêng trên đúng bộ đã nhận diện; ghi điều kiện/thời lượng/tải; không biến hơn 10 phút sống thành kiểm thử dài hạn hoặc kết luận một nguyên nhân duy nhất. |
| Commit đóng việc cha | [CHƯA KIỂM] SHA, tiêu đề bắt đầu A-07 và đúng nhánh nếu đã được Tổng quan commit. Nguồn: TASKS/A-07.md:31,42–50. | [TÀI LIỆU] Tổng quan xác nhận trong phiên có quyền Git; XD-A07 không thử stage/commit/push, không sửa quyền/credential/config. |

## 6. Mục sổ thông số

[TÀI LIỆU] Chỉ ghi thông số dùng để đối chiếu tiêu chí; mọi giá trị dưới là tài liệu lịch sử, chưa đo lại. “KHÔNG” ở cột đổi an toàn nghĩa là không được tự đổi trong XD-A07; không cấp quyền sửa/chạy (TASKS/XD-A07.md:23).

| Nhóm | Tên/thông số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Dựng nguyên gốc | Lỗi Common | A-07-buoc1-dung-debug.md:1–4,9 | 31 lỗi; không exe | lỗi build | Phân biệt thất bại nguồn nguyên gốc với snapshot đã vá. | KHÔNG | TÀI LIỆU, chưa đọc log gốc |
| Cờ snapshot | Compile/object đã kiểm | A-07e-rtc.md:108–131 | 239 lệnh /Od /Zi /MT, không /RTC; 240 object không UNDEF _RTC_ | lệnh/object | Không tương đương map hoàn toàn không có _RTC_. | KHÔNG | TÀI LIỆU, chưa chạy verifier |
| Mốc lỗi lịch sử | AV/breakpoint | A-07c-link-gs001.md:134–141 | khoảng 40 / 225 | giây | Cần phân biệt bộ binary, mã lỗi và nguyên nhân. | KHÔNG | TÀI LIỆU, chưa tái hiện |
| Mốc thử A-07e | HEVA bật | A-07e-rtc.md:166–167 | hơn 10 | phút | Chỉ qua mốc lỗi cũ, chưa có tải/dài hạn. | KHÔNG | TÀI LIỆU PM, chưa đo lại |
| Điểm dừng quy trình | VBoxSVC / VBoxHeadless | A-07-buoc1b-snapshot-da-va.md:4–5,12 | 2 / 6 | tiến trình | Cần xác nhận VM và trạng thái trước khi tiếp tục. | KHÔNG | TÀI LIỆU mốc cũ, không phải kiểm kê hiện tại |
| Nhận diện | gs001 snapshot A-07e | A-07e-rtc.md:137 | 1.286.656 | byte | Gắn artifact với manifest/hash, không dùng chỉ tên exe. | KHÔNG | TÀI LIỆU, chưa đọc binary |

## 7. Đã xác minh / Chưa xác minh, lỗi và kiểm tra thực chạy

**ĐÃ XÁC MINH — THẤY:** Đã đọc chuẩn và nguồn đúng danh sách, đối chiếu đủ 15 vế, kiểm tra tồn tại 4/4 tệp công cụ bằng Test-Path. Các bảng/mốc/dòng dẫn là văn bản hiện có trong các nguồn ở mục 1, không phải kiểm chứng runtime mới. Chỉ tạo báo cáo này và thêm mục Kết quả của TASKS/XD-A07.md theo yêu cầu.

**CHƯA XÁC MINH — CHƯA KIỂM:** Chưa kiểm lại source/binary/checkpoint/log/dump/PDB gốc, build/verifier/parser script, WER/registry/cdb, Defender, mạng, VM/VBoxSVC, gameplay hoặc tính tương thích CRT. Không có test chạy EXE/DLL/runtime trong lượt XD-A07. Những kết quả lịch sử được gắn TÀI LIỆU ở ma trận C01–C15.

| Lỗi/kiểm tra thực chạy | Cách thử và kết quả | Trạng thái tiếp tục |
|---|---|---|
| Git đầu lượt | [THẤY] git status --short --branch → task/XD-A07, sạch. | Không lặp kiểm tra status/branch; không stage/commit/push. |
| Hiển thị tiếng Việt | [THẤY] Get-Content mặc định hiển thị sai UTF-8; đọc lại hai tệp đầu bằng -Encoding UTF8 và Console.OutputEncoding UTF-8 hiển thị đúng. | Không sửa tệp nguồn vì lỗi hiển thị. |
| Thiếu rg | [THẤY] Gọi rg --files với bộ lọc A-07* → CommandNotFoundException. | Báo một lần, chuyển Get-ChildItem/Select-String giới hạn kho và tên tệp, không cài công cụ. |
| Đầu ra lệnh dài | [THẤY] Lần gộp đầu bị cắt phần hiển thị; đọc phần nguồn chưa hiển thị theo đoạn, các kết quả sau lưu trong phiên để xem từng phần. | Không tạo parser/script phụ hoặc quét source. |
| Tệp công cụ | [THẤY] Test-Path -PathType Leaf với đúng 4 đường dẫn mục 3 → True cả 4. | Không chạy hoặc nhận nội dung/cú pháp là đã tái kiểm. |
| Kiểm tra đầu ra | [THẤY] Đọc lại hai tệp bằng bộ giải mã UTF-8 nghiêm ngặt: báo cáo không BOM, không ký tự thay thế; đủ 5 dòng tóm tắt, 15 hàng C01–C15, 1 Mermaid, mục Chưa kiểm và kết luận cuối. Task có 1 mục Kết quả, 4 dòng nội dung. | Nội dung báo cáo đọc lại khớp bản soạn; không có TODO/TBD/FIXME. Đây là kiểm tra tài liệu, không phải test game. |
| Nhịp bắt đầu ngoài workspace | [THẤY] System.IO.File.WriteAllText vào D:\JX-wt\XD-A07.nhip → Access to the path … is denied; chưa ghi được mốc bắt đầu. | BỊ CHẶN — CHƯA GHI NHỊP. Không thử lại/vượt sandbox; các mốc hoàn tất đối chiếu và sắp xong được thông báo trong phiên, chưa ghi được vào .nhip. |
| Build/test vận hành | [CHƯA KIỂM] Không chạy MSBuild, Python helper/verifier của game, exe, DLL, VM, mạng, WER, debugger hay lệnh trong nguồn. | Đúng phạm vi chỉ đọc của XD-A07; không tuyên bố kiểm thử runtime đạt. |

## 8. Phát hiện khi đối chiếu và đề xuất tối ưu

- [TÀI LIỆU] Task cha vẫn active, status_note dừng trước VBoxSVC; phần Kết quả còn phản ánh lỗi sandbox/build ban đầu. Các báo cáo bước 1/1b và A-07e cung cấp mốc bổ sung nhưng không tự đổi trạng thái task cha (TASKS/A-07.md:4,14,36–53; A-07-buoc1-dung-debug.md:1–10; A-07-buoc1b-snapshot-da-va.md:1–12). Đề xuất Tổng quan cập nhật tiến độ từ bằng chứng, giữ riêng trạng thái “đã có báo cáo” với “đã tìm dòng crash”.
- [TÀI LIỆU] Khuyến nghị /RTC1 ban đầu, phân tích P1 sau đó và thay đổi A-07e là diễn tiến có chủ đích; không sửa lặng kết luận cũ. Không coi verifier exit 0 là đạt điều kiện map literal (A-07-goc-re-crash-gs001.md:221–223; A-07e-rtc.md:118–131,183–184).
- [TÀI LIỆU] Không mở rộng điều tra client/server hoặc thu thập tham số game: task là đối chiếu hồ sơ, nguồn đủ để liệt kê điều thiếu; đọc source không bù được dump/RIP đang thiếu (TASKS/XD-A07.md:19–23; A-07-goc-re-crash-gs001.md:188).
- [THẤY] Chuẩn yêu cầu chỉ mục TSV, nhưng vung_file chỉ có báo cáo và prompt cho phép thêm Kết quả task. Không tạo REPORTS/_CHIMUC/XD-A07.tsv hoặc sửa MUC-LUC-TRI-THUC.md ngoài vùng; đề xuất Tổng quan gộp dòng chỉ mục ở mục 9 (JX1_OPS/DESIGN/CHUAN-BAO-CAO.md:25–31; TASKS/XD-A07.md:12,26).

## 9. Bàn giao

[THẤY] Bàn giao đúng hai đường dẫn: JX1_OPS/REPORTS/XD-A07.md; JX1_OPS/TASKS/XD-A07.md, chỉ thêm mục Kết quả 3–5 dòng. Không sửa báo cáo cha, BACKLOG, source, công cụ game hoặc cấu hình. Không có commit SHA XD-A07 vì không được yêu cầu commit; không stage/push. Tổng quan nhận phần commit theo yêu cầu hiện tại.

[TÀI LIỆU] Bước tiếp theo: Tổng quan dùng ma trận C01–C15 để xét đóng, xác nhận điểm dừng VBoxSVC và quyền cho việc vận hành riêng; ưu tiên bằng chứng EXE/DLL/PDB–dump–source cùng bộ. Không dùng trạng thái DONE của XD-A07 để đóng A-07 (TASKS/XD-A07.md:19–20; TASKS/A-07.md:23,31; A-07-buoc1b-snapshot-da-va.md:5,11–12).

[TÀI LIỆU] Dòng chỉ mục đề xuất để Tổng quan gộp; chưa ghi sang tệp khác:

| file | loại | chủ đề | từ khóa | trạng thái | độ phủ | liên quan |
|---|---|---|---|---|---|---|
| JX1_OPS/REPORTS/XD-A07.md | tổng hợp | Đối chiếu tiêu chí đóng A-07 | gốc rễ lỗi, gs001, A-07, Debug, PDB, VBoxSVC, WER, cdb | DONE đối chiếu; A-07 chưa đạt | 9/9 nguồn, 15/15 vế có đối chiếu | TASKS/A-07.md; TASKS/BACKLOG.md; 7 báo cáo A-07* ở mục 1 |

[THẤY] Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report. Đã nạp đủ sáu SKILL.md từ .agents/skills theo yêu cầu; áp dụng bảo toàn kết luận, nguồn/dòng, nhãn độ chắc, sơ đồ và sổ thông số. Không kích hoạt khảo sát source/client hoặc mở thêm tài liệu ngoài bộ nguồn nghiệp vụ.

CHƯA ĐẠT vì A-07 chưa có bằng chứng chốt dòng gây crash gốc theo đúng bộ binary/PDB/dump; bước 3–6 còn dừng chờ xác nhận VBoxSVC/VM và điều kiện thử, commit A-07 chưa có bằng chứng hoàn tất trong bộ nguồn; XD-A07 đã hoàn tất phần đối chiếu.
