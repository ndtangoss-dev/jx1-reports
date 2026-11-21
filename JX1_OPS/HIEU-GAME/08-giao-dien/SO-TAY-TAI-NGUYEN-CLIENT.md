TÓM TẮT 1/5: [NGUỒN] PARTIAL — đã viết sổ tay tài nguyên client từ mã nguồn được giao, không suy rộng thành kết luận runtime.
TÓM TẮT 2/5: [NGUỒN] Client mở cấu hình gói qua `KPakList`; PAK được tìm theo danh sách và `KPakFile` có nhánh đọc file rời.
TÓM TẮT 3/5: [NGUỒN] SPR có luồng đọc header/frame; tên SPR bộ phận và thứ tự vẽ phụ thuộc bảng tài nguyên, hành động, hướng và khung.
TÓM TẮT 4/5: [CHƯA KIỂM] `docs-analysis/tools` không có trong worktree; chưa xác minh công cụ PAK, tài nguyên đóng gói và hành vi client đang chạy.
TÓM TẮT 5/5: [NGUỒN] Không chạy build/exe/VM/mạng; chưa chạy test; không commit/push theo yêu cầu; không có SHA.

# SO-17 — Sổ tay hiểu game: định dạng tài nguyên client (PAK, SPR, INI)

Loại: tổng hợp
Chủ đề: Giải thích đường đọc PAK, SPR, INI, ảnh bộ phận và âm thanh trong mã client được task chỉ định.
Từ khóa: tài nguyên client, gói PAK, sprite SPR, INI, paklist, KPakList, ảnh bộ phận, âm thanh JX1
Trạng thái: PARTIAL — phần đọc mã đã có bằng chứng file:dòng; thư mục công cụ PAK task nêu không tồn tại trong worktree và không kiểm tra runtime.
Độ phủ: 4/5 chủ đề đã được đối chiếu mã client; công cụ PAK 0/1 vì `docs-analysis/tools` không có trong worktree.
Liên quan: JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md; JX1_OPS/REPORTS/K-02-giao-dien.md; JX1_OPS/REPORTS/K-02-am-thanh.md; JX1_OPS/REPORTS/K-02-nhan-vat.md; JX1_OPS/REPORTS/K-02-quai-npc.md; JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md
Cần tôi quyết định: không

```mermaid
flowchart TD
    A[Client khởi tạo gói] --> B[KPakList đọc cấu hình Package]
    B --> C[Đường dẫn và danh sách PAK]
    C --> D[KPakFile tìm mục và đọc dữ liệu]
    D --> E[INI và ảnh PNG/JPG]
    D --> F[SPR: header, bảng offset, frame]
    F --> G[Tên SPR cho từng bộ phận]
    G --> H[Chọn thứ tự theo action, hướng, frame]
    H --> I[Vẽ nhân vật]
    J[Âm thanh] --> K[SoundManager / KMapMusic]
    K --> L[Đường dẫn âm thanh riêng]
```

## Phạm vi và độ phủ

| Phần tử của câu hỏi | Kết quả | Trạng thái | Bằng chứng / giới hạn |
|---|---|---|---|
| Client lấy tài nguyên từ PAK hay file rời | Mã client mở danh sách cấu hình gói, tìm mục trong PAK; `KPakFile` có chế độ ưu tiên gói hoặc ưu tiên file tùy mode | Đã đối chiếu tĩnh | `gamescene/KUpdateLayer.cpp:822–831`; `engine/KPakList.cpp:136–205`; `engine/KPakFile.cpp:19–31,256–305`. Chưa xác minh cấu hình và mode của bản client đang chạy. |
| Công cụ PAK ở `docs-analysis/tools` | Thư mục không tồn tại trong worktree hiện tại | Chưa phủ nội dung công cụ | Đã kiểm tra đúng đường dẫn; không mở/chạy công cụ thay thế. |
| SPR và ảnh động | Mã nhận diện đuôi `.spr`, gọi bộ nhớ ảnh để lấy header/frame; metadata chứa số frame, hướng, interval và kích thước/offset frame | Đã đối chiếu tĩnh | `engine/Kgetinidata.cpp:100–153`; `engine/KbugInfo.h:238–269`. Không đọc asset SPR thực. |
| Ảnh bộ phận và thứ tự vẽ | Node tài nguyên tra tên file theo part/action/equip; renderer hỏi bảng sort theo action, hướng, frame. Với NPC thường có nhánh part cố định; nhánh NPC đặc biệt dùng bảng sort | Đã đối chiếu tĩnh | `gamecore/KNpcResNode.cpp:547–627`; `gamecore/KNpcRes.cpp:241–287,415–423`; `JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md:18–43`. Bảng dữ liệu thật và hành vi từng asset chưa kiểm. |
| Âm thanh | `SoundManager` tìm âm trong thư mục ghi được hoặc đường dẫn thẻ; `KMapMusic` đọc bảng nhạc và chuyển đường dẫn cho phát nhạc | Đã đối chiếu tĩnh | `manager/SoundManager.cpp:85–168`; `gamecore/KMapMusic.cpp:92–116,261–283`. Chưa xác minh asset nào được dùng khi chạy. |

## Cách hiểu cho người chơi và người làm nội dung

### PAK, đường dẫn và INI

[THẤY] Ở điểm khởi tạo gói trong mã client, `KUpdateLayer` truyền `data/package.ini` cho danh sách gói (`gamescene/KUpdateLayer.cpp:822–831`). `KPakList::Open` đọc mục `Package`, lấy `Path`, rồi thử các khóa đánh số và mở những gói hợp lệ (`engine/KPakList.cpp:136–205`). Vì vậy danh sách cấu hình cho biết nơi tìm PAK và tên các gói; đường dẫn này thuộc mã nguồn, chưa chứng minh tệp cấu hình đó của một bản cài cụ thể.

[THẤY] `KPakFile::Open` có hai nhánh: một nhánh thử file rời rồi mới tra gói, nhánh kia tra gói trước rồi mới thử file rời (`engine/KPakFile.cpp:256–277`). Biến mode được khởi tạo bằng `1`, nhưng có hàm thay mode (`engine/KPakFile.cpp:19–31`); không thể kết luận mode hiệu lực của binary hoặc lần chơi cụ thể chỉ từ source.

[THẤY] Khi đường dẫn trỏ vào mục trong gói, `KPakFile::Read` chuyển việc đọc qua `KPakList`; nếu không có tham chiếu gói thì đọc từ file mở trên đĩa (`engine/KPakFile.cpp:286–305`). Kiểm tra tồn tại chung cũng dò gói trước rồi mới kiểm file rời (`engine/KFilePath.cpp:446–468`). `KIniFile::Load` mở dữ liệu qua `KPakFile`, nên INI có thể được đọc từ gói hoặc file theo nhánh mode trên (`engine/KIniFile.cpp:71–119`).

### PNG/JPG và SPR

[THẤY] Nhánh `Kgetinidata::findinidata_new` phân PNG/JPG khỏi SPR. PNG/JPG đi qua `getpicPath`; đường này chuẩn hóa tên, hỏi `KPakList` và đưa dữ liệu ảnh tìm được vào texture cache (`engine/Kgetinidata.cpp:59–96,570–590`). Đoạn mã đã xem xác nhận nhánh tra gói; nó không xác nhận mọi ảnh của game đều nằm trong PAK.

[THẤY] SPR đi qua bộ đọc riêng. Hàm kiểm đuôi `.spr`, yêu cầu đủ header/frame và bảng offset khi không dùng chế độ nạp một frame; sau đó đưa thông tin header và kích thước, offset frame vào cấu trúc kết quả (`engine/Kgetinidata.cpp:100–153`). Source mô tả header gồm kích thước, tâm, số frame, màu, hướng, interval; mỗi frame có offset, kích thước và dữ liệu sprite (`engine/KbugInfo.h:238–269`). Đây là mô tả format trong source, không phải kiểm tra nội dung gói PAK.

### Ảnh bộ phận và lỗi sai thứ tự vẽ

[THẤY] Với nhân vật ghép nhiều phần, `KNpcResNode::GetFileName` là điểm tra tên SPR theo phần và điều kiện tài nguyên (`gamecore/KNpcResNode.cpp:547–605`). `KNpcRes::Draw` tính hướng/frame cho ảnh bộ phận rồi yêu cầu `GetnSort` với hành động, hướng và frame hiện tại (`gamecore/KNpcRes.cpp:241–287,415–423`). Node trả một part cố định cho NPC thường; nhánh NPC đặc biệt lấy thứ tự từ bảng sort (`gamecore/KNpcResNode.cpp:612–630`).

[TÀI LIỆU] Bảng phủ trong `QUY-LUAT-VE-BO-PHAN.md` ghi rõ thứ tự che không cố định cho mọi tư thế; dữ liệu nữ/đứng được dẫn lại từ BUG-001, còn các tổ hợp khác chưa đo (`JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md:18–43`). [THẤY] Mã lấy thứ tự theo action, hướng và frame (`gamecore/KNpcRes.cpp:422`; `gamecore/KNpcResNode.cpp:612–630`). Nếu tra sai tổ hợp trạng thái hoặc bảng sort không khớp, thứ tự part được chọn sẽ khác với thứ tự cần cho trạng thái đó. [CHƯA KIỂM] Chưa có bằng chứng xác định tổ hợp hoặc dòng bảng nào gây ra một ca lỗi cụ thể; không thể gán lỗi cho một file SPR hay thiết lập riêng.

### Đối chiếu bộ đọc gói phía server

[THẤY] Source server tại `C:/Jx1CocoV3/SwordOnline/SwordOnline/jxOnline/gameserver/Sources` cũng có `KPakList::Open` đọc mục `Package`, trường `Path` và các khóa số để mở các gói (`Engine/Src/KPakList.cpp:121–188`). `KPakFile` phía server đọc từ tham chiếu mục gói hoặc từ file đã mở (`Engine/Src/KPakFile.cpp:245–305`). Điều này cho thấy hai source tree có lớp đọc gói tương tự; không dùng server để suy đường dẫn client hoặc xác nhận bản chạy.

### Âm thanh

[THẤY] `SoundManager::PlaySound` tìm tệp âm trong thư mục `ogg` dưới đường dẫn ghi được trước khi nạp và phát; `MyPlaySound` ghép tên với đường dẫn thẻ nhớ/cấu hình rồi kiểm tra tệp (`manager/SoundManager.cpp:85–168`). Đây là một đường âm thanh riêng, không phải bằng chứng cho vị trí mọi âm trong PAK.

[THẤY] `KMapMusic::LoadSetFile` nạp bảng dữ liệu nhạc; các nhánh phát gọi trình phát với biến đường dẫn nhạc đã ghép (`gamecore/KMapMusic.cpp:92–116,261–283`). Tên asset, vị trí cài đặt và việc có fallback nào trong binary cụ thể chưa được kiểm tra.

## Giải mã tên

| Tên gốc | Mã hóa | Chữ đúng | Nguồn file:dòng |
|---|---|---|---|
| PAK, SPR, INI | Ký tự Latin/ASCII; tên định dạng | Giữ nguyên PAK, SPR, INI | `engine/KbugInfo.h:238–283`; `engine/KIniFile.cpp:71–119` |
| Cocos2d-x / CCTextureCache | Tên thư viện và lớp, ký tự Latin/ASCII | Giữ nguyên tên kỹ thuật | `engine/Kgetinidata.cpp:59–96,570–590` |
| FMOD | Tên thư viện âm thanh, ký tự Latin/ASCII | Giữ nguyên FMOD | `manager/SoundManager.cpp:52–60,85–114` |
| Tên kỹ năng, trang bị, quái, NPC hoặc bản đồ | Không có tên thực thể được đọc trong phạm vi này | Chưa áp dụng | Chỉ đọc mã nạp tài nguyên và báo cáo dẫn; không giải mã dữ liệu nội dung game. |

## Sắp theo cấu trúc game

| Cấu trúc | Thứ tự hiểu | Mức xác minh |
|---|---|---|
| Gói tài nguyên | Cấu hình Package → thư mục gốc → các mục PAK → đường dẫn tài nguyên | Đã xác minh luồng source; chưa kiểm cấu hình/PAK của bản cài. |
| Ảnh | PNG/JPG qua nhánh ảnh; SPR qua header → bảng offset → frame | Đã xác minh nhánh source; chưa kiểm asset cụ thể. |
| Nhân vật ghép bộ phận | Loại NPC → tên SPR của part → action → hướng → frame → sort/draw | Đã xác minh lời gọi và giới hạn từ DESIGN; chưa đối chiếu bảng dữ liệu thật. |
| Âm thanh | Âm hiệu qua SoundManager; nhạc bản đồ qua KMapMusic | Đã xác minh lời gọi source; chưa lập danh sách asset thực tế. |

## Đã xác minh / Chưa xác minh

### Đã xác minh
- Client được đọc theo root trong task: `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes`; bằng chứng tĩnh nằm ở các file:dòng trong bảng trên.
- Mã client có đường mở danh sách gói, đọc mục PAK, đường đọc INI, nhánh nạp PNG/JPG và SPR, tra tên ảnh bộ phận, yêu cầu sort, và hai đường âm thanh như trích dẫn trên.
- Đã đối chiếu source server `KPakList`/`KPakFile` với client và báo cáo DESIGN về giới hạn thứ tự bộ phận; không đổi kết luận hiện có.

### Chưa xác minh
- Nội dung và thứ tự thật của từng PAK/`package.ini`/`paklist.ini`, các asset SPR thực tế, và thư viện/công cụ PAK ở `docs-analysis/tools`.
- Bản client nào đang dùng cấu hình hoặc mode nào; source có khớp binary/cấu hình được cài không; thứ tự vẽ của từng asset khi runtime.
- Tệp âm thanh nào được nạp trong game và nguồn lưu của chúng ở bản chạy cụ thể.
- Build, test, exe, VM, mạng và đo runtime không thực hiện theo giới hạn task.

### Phạm vi công cụ và nhịp
- `rg` không khả dụng trong môi trường; dùng `Get-ChildItem`/`Select-String` giới hạn theo thư mục và tên tệp, hoàn tất tìm kiếm cần thiết.
- Thử ghi `D:/JX-wt/SO-17.nhip` theo yêu cầu nhưng hệ thống từ chối quyền ghi; nhịp không được lưu. Không đổi quyền hoặc ghi ra ngoài worktree.
- Không có lỗi đọc source nào cần retry; không chạy test/build vì task chỉ duyệt đọc tĩnh và tạo tài liệu.

## Bàn giao

Không commit/push theo yêu cầu; SHA không có. Bước tiếp theo: PM có thể chỉ định đường dẫn đúng của công cụ PAK hoặc đưa thư mục đó vào worktree để hoàn tất phần còn thiếu. Tài liệu mới cần PM gộp vào mục lục:

| Chủ đề | Báo cáo / tài liệu | File, hàm chính | Độ chắc |
|---|---|---|---|
| Tài nguyên client PAK/SPR/INI, ảnh bộ phận và âm thanh | `SO-17` | `KPakList`, `KPakFile`, `Kgetinidata`, `KNpcResNode`, `KNpcRes`, `SoundManager`, `KMapMusic` | Khảo sát tĩnh; PARTIAL |

liên quan: JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md; JX1_OPS/REPORTS/K-02-giao-dien.md; JX1_OPS/REPORTS/K-02-am-thanh.md; JX1_OPS/REPORTS/K-02-nhan-vat.md; JX1_OPS/REPORTS/K-02-quai-npc.md; JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md

Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report

## Bổ sung khi tiếp tục SO-17 — 19/11/2026

### Quy ước đọc nguồn

[TÀI LIỆU] Các đường dẫn `engine/...`, `gamecore/...`, `gamescene/...`, `manager/...` trong sổ tay thuộc root client `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Classes`; mục đối chiếu server có root riêng ghi ngay tại đó (`JX1_OPS/TASKS/SO-17.md:23–25`). `[THẤY]` là đọc trực tiếp mã nguồn; `[TÀI LIỆU]` là dẫn tài liệu hoặc diễn giải dựa trên nguồn được nêu; `[CHƯA KIỂM]` là chưa có bằng chứng. Đọc source không xác nhận bản game đang chạy. Phần trước và trạng thái PARTIAL được giữ nguyên.

### Gói tài nguyên và hai danh sách INI

[TÀI LIỆU] Có thể hiểu PAK là kho chứa nhiều tệp; SPR là dữ liệu các khung ảnh; INI là bảng thiết lập theo mục và khóa. Cách diễn giải này dựa trên cấu trúc PAK/SPR và lời gọi đọc `Package`/`Path` trong source, không phải đã giải một gói thực (`engine/KbugInfo.h:238–291`; `engine/KPakList.cpp:140–176`).

[THẤY] Source khai báo đầu PAK có dấu nhận diện `PACK`, số mục, vị trí bảng chỉ mục và vị trí dữ liệu; từng mục chỉ mục có mã tệp, vị trí, kích thước gốc và trường kích thước/kiểu nén (`engine/KbugInfo.h:273–291`). [CHƯA KIỂM] Chưa xác minh header, CRC hoặc nội dung của PAK thực trong SO-17; không coi PAK là ZIP hoặc mặc định một công cụ ZIP đọc được.

[THẤY] Có hai tên INI phục vụ hai chỗ khác nhau. `PAKLIST_FILE` trỏ `data/paklist.ini`; nhánh chuẩn bị tải đọc mục `list`, khóa `count`, `isopen`, `pak_0...`, `pak_0_r...`. Nhánh mở gói sau đó truyền `data/package.ini` (dấu phân cách thay theo nền tảng) cho `KPakList::Open`, nơi đọc mục `Package`, khóa `Path` và các khóa số (`gamescene/KUpdateLayer.cpp:40,762–830`; `engine/KPakList.cpp:136–205`). [CHƯA KIỂM] Chưa đọc hai INI triển khai, chưa biết danh sách gói hiệu lực; không đồng nhất hai tên hoặc mở cấu hình nguyên tệp chứa trường ngoài phạm vi.

[THẤY] Có giới hạn nền tảng ngay khi đọc `Path`: trong nhánh không định nghĩa `WIN32`, đoạn mã ghi lại đường dẫn thành `/data` trước khi giải đường dẫn đầy đủ (`engine/KPakList.cpp:149–155`). [TÀI LIỆU] Vì vậy không suy rằng chỉ đổi khóa `Path` là đổi nơi đọc gói trên mọi nền tảng. [CHƯA KIỂM] Chưa xác nhận macro build và đường dẫn hiệu lực của bản game đang cài.

[THẤY] Vòng mở duyệt khóa số tăng dần; chỉ gói mở thành công mới được đưa vào danh sách. Vòng tìm tài nguyên duyệt từ đầu danh sách và dừng ở gói đầu tiên tìm thấy mã tài nguyên (`engine/KPakList.cpp:66–77,171–198`). [TÀI LIỆU] Vì vậy thứ tự cấu hình có ý nghĩa trong luồng source này; không mặc định gói thêm cuối luôn đè gói trước. [CHƯA KIỂM] Chưa thử tài nguyên trùng, va chạm mã tên hoặc thứ tự gói thực nạp.

[THẤY] Ngoài nơi lưu, mã hóa tên cũng ảnh hưởng các nhánh tìm: có nhánh thử nguyên tên, UTF-8 → GBK hoặc GBK → UTF-8 tùy kiểu chuyển được truyền vào (`engine/KPakList.cpp:234–295`). [TÀI LIỆU] Khi điều tra “có tệp nhưng không tìm thấy”, cần đối chiếu tên/đường dẫn, kiểu chuyển mã, danh sách gói và mode, thay vì chỉ kiểm tệp có trên đĩa (`engine/KPakFile.cpp:256–277`; `engine/KPakList.cpp:234–295`). [CHƯA KIỂM] Chưa xác định một lỗi ảnh cụ thể do mã hóa.

### Khung ảnh và nhân vật ghép bộ phận

[TÀI LIỆU] “Header” là phần mô tả chung; “frame” là một khung ảnh; “offset” là độ lệch để xác định dữ liệu hoặc vị trí khung. Mỗi khung có kích thước và độ lệch riêng, nên chỉ nhìn kích thước chung chưa đủ đối chiếu ảnh từng bộ phận (`engine/KbugInfo.h:238–269`; `engine/Kgetinidata.cpp:142–151`). [CHƯA KIỂM] Chưa đo khung thật, bảng màu, thời lượng hiển thị hoặc chất lượng sau chuyển đổi SPR.

[THẤY] Cùng một bộ phận có tên ảnh và dữ liệu theo hành động/trang bị; mã chọn hành động còn xét trạng thái cưỡi ngựa. Thứ tự lớp được hỏi theo hành động, hướng và khung (`gamecore/KNpcResNode.cpp:547–605,612–630`; `gamecore/KNpcRes.cpp:422`). [TÀI LIỆU] Vì vậy một ảnh đúng tên vẫn có thể bị che khác mong muốn nếu chọn sai tổ hợp trạng thái/bảng sort. Đây là cách khoanh vùng từ luồng mã; DESIGN cũ vẫn thiếu ma trận nam/nữ × hành động × hướng (`JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md:18–46`). [CHƯA KIỂM] Chưa gán nguyên nhân cho ca lỗi cụ thể hoặc bổ sung số đo vào ma trận cũ.

### Âm thanh có thể đi từ PAK ra tệp rời

[THẤY] `KNpcRes::PlaySound` gọi `g_StrCopy` trước khi chọn `playEffect` hoặc `SoundManager::MyPlaySound` (`gamecore/KNpcRes.cpp:2512–2551`). Nếu tệp đích đã có, `g_StrCopy` trả về; nếu chưa có và tra được trong PAK, mã đọc dữ liệu gói rồi ghi thành tệp đích (`engine/KStrBase.cpp:829–873`). [TÀI LIỆU] Vì vậy trình phát nhận đường dẫn tệp rời không đủ chứng minh âm đó vốn nằm ngoài PAK. [CHƯA KIỂM] Không gọi hàm này, không tạo tệp âm, không phát thử hoặc xác nhận nhánh hiệu lực trên thiết bị.

### Công cụ PAK còn thiếu nguồn

[TÀI LIỆU] Báo cáo kiểm kê cũng nhắc cần công cụ PAK ở `docs-analysis/tools` (`JX1_OPS/REPORTS/K-02.md:29`). [CHƯA KIỂM] `Test-Path -LiteralPath 'docs-analysis/tools'` trả `False` trong worktree SO-17. Chưa xác định được tên, phiên bản, mã, cách dùng, kiểu nén hỗ trợ hoặc mức an toàn của công cụ; không có dòng văn bản để dẫn cho một thư mục vắng mặt. Không lấy công cụ ở cây khác thay thế, không tải hoặc chạy trình giải gói. PM cần chỉ định nguồn để hoàn tất nhóm này; kết luận PARTIAL cũ không đổi.

### Mục sổ thông số

[THẤY] Bảng chỉ ghi khai báo/mặc định source, không phải giá trị đo trên gói hoặc bản game đang chạy. Mức đổi không cấp quyền chỉnh mã/cấu hình.

| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn (CÓ/CẨN THẬN/KHÔNG) | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Ưu tiên đọc | m_nPakFileMode | engine/KPakFile.cpp:19–31,262–275 | Mặc định source 1; nhánh 0 thử đĩa trước, nhánh khác thử PAK trước | Mã chế độ | Nơi thử đọc đầu tiên | CẨN THẬN — chưa kiểm mode runtime/tài nguyên trùng | Đọc tĩnh, chưa đo runtime |
| Danh sách gói | MAX_PAK | engine/KPakList.h:44–46; engine/KPakList.cpp:171–198 | 50; xét khóa 0..49 | Vị trí gói/khóa | Giới hạn trong lớp này, không phải số PAK đang có | CẨN THẬN — chưa kiểm nơi phụ thuộc | Đọc tĩnh |
| Hoạt ảnh | SPRHEAD.Frames | engine/KbugInfo.h:245; engine/Kgetinidata.cpp:142,153 | Theo asset, chưa đọc giá trị | Khung ảnh | Tổng khung từ header | KHÔNG — thiếu asset/cặp đối chiếu | Đọc schema, chưa đo |
| Hướng | SPRHEAD.Directions | engine/KbugInfo.h:247 | Theo asset, chưa đọc giá trị | Hướng | Số hướng trong header; chưa gán bằng ma trận tám hướng cũ | KHÔNG — thiếu asset/cặp đối chiếu | Đọc schema, chưa đo |

### Đề xuất tối ưu

[CHƯA KIỂM] Chưa có số đo để đề nghị đổi hiệu năng, nén gói, cache hoặc asset. Bước tiếp theo là chỉ định nguồn công cụ và cặp tài nguyên đúng bản, rồi giao task riêng cho phép kiểm cần thiết. [TÀI LIỆU] Một ca sai ảnh cần đối chiếu cấu hình gói/mode, tên part, hành động, hướng và khung với bảng sort; không thay kết luận bằng ảnh chụp đơn lẻ (`engine/KPakFile.cpp:256–277`; `engine/KPakList.cpp:66–77`; `gamecore/KNpcRes.cpp:422`; `gamecore/KNpcResNode.cpp:547–630`).

### Phát hiện khi chuẩn hóa

[TÀI LIỆU] Các báo cáo K-02 về giao diện/âm thanh đã đọc dùng root `D:/JX-build/qh9A`; SO-17 chỉ đối chiếu lại các điểm cần bổ sung trong root client task chỉ định. Không đưa số lượng/byte asset hoặc dòng source của qh9A thành số đo của root SO-17 (`JX1_OPS/REPORTS/K-02-giao-dien.md:100–106,124`; `JX1_OPS/REPORTS/K-02-am-thanh.md:37–45`; `JX1_OPS/TASKS/SO-17.md:25`).

[THẤY] Source có comment legacy dùng GBK/CP936 hoặc trộn mã; đọc sai encoding có thể làm lệch điểm định vị. Riêng đường sao âm đã chốt bằng dòng LF vật lý và symbol ASCII tại `engine/KStrBase.cpp:829–873`; không sửa encoding/source và không tự giải nghĩa tên asset chưa đọc. Chi tiết kiểm tài liệu và giới hạn nhịp bàn giao ở `JX1_OPS/REPORTS/SO-17.md`.

liên quan: JX1_OPS/REPORTS/SO-17.md; JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md; JX1_OPS/REPORTS/K-02-giao-dien.md; JX1_OPS/REPORTS/K-02-am-thanh.md; JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md

## Tài nguyên UI cường hóa

[ĐÃ XÁC MINH] Phần này đối chiếu bản copy `D:/Android/b/Client` với ba JPG trong `JX1_OPS/DESIGN/UI-CUONG-HOA/`. Ảnh 1–2 cho cửa sổ cường hóa, ảnh 3 cho tooltip và hành trang (`MO-TA.md:2–3`). Mọi đường dẫn `Resources/` và `Classes/` bên dưới tính từ root bản copy.

```mermaid
flowchart LR
    A["Hộp đặt đồ VN"] --> B["taskbox.spr và nút xác nhận"]
    A --> C["Hành trang VN"]
    C --> D["ui_item.png và nhãn tiền, xu"]
```

| Phần của cửa sổ trong ảnh 1–2 | Kết quả và tài nguyên gần nhất |
|---|---|
| Nền và tiêu đề | **KHÔNG TÌM THẤY** nền đúng ảnh. `KuiGiveVN::init` nạp `\ui\task\taskbox.spr` frame 0. `KuiGive_New::init` nạp `\Spr\Ui3\给予界面\给予.spr` frame 0 và gắn tiêu đề `LabelTTF`. Nhánh VN có dòng gắn tiêu đề đang bị comment. `Classes/vn/gameui/KuiGiveVN.cpp:35–44,540–545`, `Classes/gameui/KuiGive_New.cpp:83–92,590–594`. |
| Dải gợi ý bo tròn | **KHÔNG TÌM THẤY** viền đúng ảnh. `KuiGiveVN::addDialogData` dựng chữ bằng `RichText`. Nền vùng cuộn là `Resources/loadingStart.png` (40 × 3 px), opacity 0. `Classes/vn/gameui/KuiGiveVN.cpp:76–84,517–536`. |
| Khung ô có chóp thoi | **KHÔNG TÌM THẤY** khung đúng ảnh. `Resources/ui/gameworld/mau_equip1.png` là nền ô có viền mảnh, 58 × 46 px. Điểm nạp trong hộp đặt đồ chưa xác định. |
| Ô giữa Trang Bị | **KHÔNG TÌM THẤY** khung trung tâm. `KuiGiveVN::AddGiveObject` gọi `Item[].GetImagePath`, lấy frame 0 qua `findinidata_one` và có ảnh dự phòng `\spr\others\问号.spr`. `Classes/vn/gameui/KuiGiveVN.cpp:717–745`. |
| Mũi tên xuống, ngang, chéo | **KHÔNG TÌM THẤY** bộ mũi tên đúng ảnh. `Resources/ui/main/next.png` là ảnh mũi tên đơn sang phải 47 × 61 px. Điểm nạp trong hộp cường hóa chưa xác định. |
| Khung ô nguyên liệu | **KHÔNG TÌM THẤY** khung trang trí riêng. `KuiGiveVN::AddGiveObject` dựng màu nền ô qua `KuiEffect` và số lượng bằng `LabelTTF`. Header khai báo ô 40 × 40 đơn vị UI. `Classes/vn/gameui/KuiGiveVN.h:7`, `Classes/vn/gameui/KuiGiveVN.cpp:754–757,777–794`. |
| Lưới túi | **KHÔNG TÌM THẤY** lưới riêng của cửa sổ. Ảnh rời `Resources/ui/gameworld/UiItem/ui_item.png` có lưới 5 cột × 6 hàng, 336 × 511 px, gần với hành trang trong ảnh 3. `KuiItemVN::init` dùng `CCSprite::create`. `Classes/vn/gameui/KuiItemVN.cpp:65–69`. |
| Hai thanh vàng/bạc | **KHÔNG TÌM THẤY** hai thanh đặt ngang đúng ảnh. Ảnh `ui_item.png` có hai thanh nền, `KuiItemVN` gắn nhãn tiền và xu lên đó ở `Classes/vn/gameui/KuiItemVN.cpp:110–122,1283–1314`. |
| Nút Cường hóa | **KHÔNG TÌM THẤY** nút đúng ảnh. `KuiGiveVN::setcoloseButton` nạp `\ui\task\btn_confirm_small.spr` frame 0/1 bằng `findinidata_one` để dựng nút xác nhận. `Classes/vn/gameui/KuiGiveVN.cpp:549–571`. |

[CHƯA XÁC MINH] `ui.pak` và `spr.pak` có trong `Resources/package.ini:24,29`. Không tìm thấy gói ở các vị trí đã kiểm, kể cả trong chỉ mục hai APK sẵn có. Chưa có PAK để kiểm vị trí, ID và kích thước các SPR. Kích thước nêu trong bảng là số đo của PNG rời hoặc đơn vị UI được khai báo trong mã.

Liên quan: [XD-UI01](../../REPORTS/XD-UI01.md), [mô tả ảnh chuẩn](../../DESIGN/UI-CUONG-HOA/MO-TA.md).
