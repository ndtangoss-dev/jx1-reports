TÓM TẮT 1: [NGUỒN] Khảo sát tĩnh asset sprite nhân vật trên client bản A `D:/JX-build/qh9A` và server `C:/Jx1CocoV3/.../gs`; không sửa byte gốc.
TÓM TẮT 2: [NGUỒN] Source client xác minh 6 nhóm × 4 section (`MAX_PART=24`), hai layer BASE/EFFECT, nạp theo action–trang bị và bảng sort theo action–hướng–khung.
TÓM TẮT 3: [NGUỒN] Client `Resources` có 949 file/78.036.052 byte, gồm 646 PNG/21.630.476 byte; không có `.spr`, `.pak`, `.mps` hoặc `.wor` rời trong phạm vi đã quét.
TÓM TẮT 4: [CHƯA KIỂM] Server có `Settings/NpcRes` 93 file/2.805.389 byte, 4 `.pak`/15.610.628 byte và chưa giải gói để đếm sprite thành viên; metadata SPR/runtime chưa đo.
TÓM TẮT 5: [CHƯA KIỂM] Không build, không chạy exe/VM/mạng; file nhịp ngoài worktree bị từ chối quyền ghi, chưa có commit/push.

# K-02a — Kiểm kê asset gốc: sprite nhân vật
Loại: khảo sát
Chủ đề: Kiểm kê bộ phận, hướng, trang bị vẽ lên và bảng thứ tự vẽ của sprite nhân vật trong client bản A, đối chiếu dữ liệu server chỉ đọc.
Từ khóa: sprite nhân vật, character, KNpcRes, MAX_PART, BASE, EFFECT, GetnSort, SPR, PAK
Trạng thái: PARTIAL — source đã đọc và thư mục đã kiểm kê; sprite đóng gói và metadata từng sprite chưa giải gói/đo.
Độ phủ: đã phủ 4/4 trục logic source và 2/2 gốc thư mục được chỉ định; asset sprite thành viên 0/1 vì chưa đọc nội dung PAK.
Liên quan: `JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md`, `JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md`, `JX1_OPS/REPORTS/J-04-lop-chong-nhan-vat.md`, `JX1_OPS/BUGS/BUG-001.md`, `JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md`
Cần tôi quyết định: có — yêu cầu trực tiếp nêu K-02a.md và thêm kết quả vào TASKS/K-02a.md, còn vung_file của task chỉ định K-02-nhan-vat.md.

```mermaid
flowchart LR
    K[KNpcResNode::Init] --> P[6 nhóm × 4 section]
    P --> R[GetFileName + SPR metadata]
    R --> E[BASE/EFFECT × part]
    E --> S[GetnSort(action, hướng, khung)]
    S --> D[KNpcRes/KNpcResVN::Draw]
    A[Client Resources: PNG/UI, không có SPR rời] -. thiếu asset .-> R
    Z[Server Settings/NpcRes + PAK] -. chưa giải gói .-> R
```

## Phạm vi và độ phủ

| Phần tử | Đã kiểm | Chưa kiểm / giới hạn | Bằng chứng |
|---|---|---|---|
| Client bản A `D:/JX-build/qh9A/Resources` | Đã đếm 949 file, 78.036.052 byte theo phần mở rộng | Không suy đây là toàn bộ asset runtime; không mở APK/build output | `D:/JX-build/qh9A/Resources` (quét read-only) |
| Client ảnh nhân vật gần nhất `Resources/avatar` | 41 PNG, 644.195 byte | Chưa chứng minh đây là sprite gameplay; không có `.spr` rời | `D:/JX-build/qh9A/Resources/avatar` |
| Client ảnh đòn đánh `Resources/attack` | 11 PNG, 130.032 byte | Chưa gắn được với `KNpcRes`/action runtime | `D:/JX-build/qh9A/Resources/attack` |
| Client UI/ảnh khác | `ui`: 371 PNG + 1 JPG + 6 PSD + 2 ZIP; `ui_vn`: 127 PNG + 1 PLIST; `selpic`: 15 PNG | Không xếp vào sprite nhân vật gameplay | `D:/JX-build/qh9A/Resources/ui`, `ui_vn`, `selpic` |
| Client định dạng sprite rời | 0 `.spr`, 0 `.pak`, 0 `.mps`, 0 `.wor` | Có thể nằm trong gói khác hoặc asset build; chưa giải nén/đọc gói | Quét toàn `D:/JX-build/qh9A` |
| Server `Settings/NpcRes` | 93 file: 91 TXT + 2 INI, 2.805.389 byte | Tên Hán hiển thị mojibake khi đọc chưa đúng mã; chưa đối chiếu từng dòng bảng | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/Settings/NpcRes` |
| Server gói `gs/pak` | 4 PAK/15.610.628 byte: `maps.pak`, `maps01.pak`, `script.pak`, `skill.pak` | Chưa đọc index/member nên chưa biết có sprite | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/pak` |
| Server mã nguồn tại root chỉ định | 0 file C++ | Root gs là cây dữ liệu/deployment; không có file mã C++ để trích dòng server | C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs (lọc *.cpp) |
| Server map/container liên quan | 3 MPS/9.900 byte; 1 WOR/111 byte | `.wor` là map container, không kết luận là sprite | `.../gs/pak`, `.../gs/maps` |
| Số frame/hướng/interval từng sprite | Loader đã xác minh trường cần đọc | Chưa đo giá trị từng asset vì không có `.spr` rời và không giải gói PAK | `D:/JX-build/qh9A/Classes/engine/KPakFile.cpp:37-90`, `:114-124`; `XPackFile.cpp:597-705` |
| Bảng thứ tự vẽ | Đã xác minh đường nạp và tra bảng | Chưa đọc bảng INI cụ thể của từng nhân vật | `D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.cpp:365-369`, `:612-630`, `:1390-1480` |

## Giải mã tên

| Tên gốc / mã | Mã hóa | Chữ đúng | Nguồn file:dòng |
|---|---|---|---|
| `emNPCRES_PART_HELM` | ASCII identifier | Mũ/đầu | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:8-10` |
| `emNPCRES_PART_ARMOR` | ASCII identifier | Áo/thân | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:8-11` |
| `emNPCRES_PART_WEAPON` | ASCII identifier | Vũ khí | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:8-12` |
| `emNPCRES_PART_HORSE` | ASCII identifier | Ngựa | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:8-13` |
| `emNPCRES_PART_MANTLE` | ASCII identifier | Phi phong | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:8-14` |
| `emNPCRES_PART_LAYER_BASE` | ASCII identifier | Lớp nền | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:20-23` |
| `emNPCRES_PART_LAYER_EFFECT` | ASCII identifier | Lớp hiệu ứng | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:20-24` |
| Tên file trong `Settings/NpcRes` và literal `NPC_RES_KIND_FILE_NAME` | Tên Hán legacy; cần GBK, hiện hiển thị mojibake khi đọc sai mã | Chưa giải mã; không tự đổi tên | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:29-30`; `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs/Settings/NpcRes` |

## Sắp theo cấu trúc game

1. **Bộ phận → section:** source dành 6 nhóm, mỗi nhóm 4 section, tổng 24 (`MAX_BODY_PART=6`, `MAX_BODY_PART_SECT=4`, `MAX_PART=24`). Bản đồ section kế thừa từ báo cáo J-04: `0–3` mũ/đầu, `4–7` áo/thân, `8–11` vũ khí, `12–15` ngựa, `16–19` phi phong, `20–23` cánh; các slot legacy không đồng nghĩa tất cả đều active trong nhánh hiện hành (`D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.h:23-26`; `JX1_OPS/REPORTS/J-04-lop-chong-nhan-vat.md:55-66`).
2. **Layer:** mỗi section có thể có BASE và EFFECT; EFFECT đổi hậu tố `_effect.txt` khi dựng tên resource (`D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:20-24`; `KNpcResNode.cpp:147-171`).
3. **Trang bị → resource:** `SetPartInfo` nhận part/layer/type, rồi gọi `GetFileName`, `GetTotalFrames`, `GetTotalDirs`, `GetInterval` cho từng section (`D:/JX-build/qh9A/Classes/gamecore/KNpcRes.cpp:1791-1860`). Nhánh action hiện hành lặp 5 part enum và 2 layer (`KNpcRes.cpp:1705-1730`), nên phải tách sức chứa 6 nhóm legacy khỏi nhóm đang cập nhật.
4. **Hướng → khung → thứ tự vẽ:** `Draw` lượng tử hóa hướng theo số hướng metadata và chọn khung theo tổng frame (`D:/JX-build/qh9A/Classes/gamecore/KNpcRes.cpp:247-294`). `GetnSort` trả bảng mặc định/riêng theo action, hướng, khung; `Draw` lặp bảng đó và từng layer để đưa ảnh vào danh sách vẽ (`KNpcResNode.cpp:612-630`, `KNpcResNode.cpp:1390-1480`, `KNpcRes.cpp:427-428`, `:669-685`).
5. **VN override:** nhánh VN hiện có hoán đổi section 8↔9 sau `GetnSort` trong source bản A; đây là code hiện có, không phải kết quả kiểm runtime (`D:/JX-build/qh9A/Classes/vn/gamecore/KNpcResVN.cpp:205-217`).

## Cách đọc và mức hiểu

- **Cách đọc source:** PowerShell `Get-Content`/`Select-String` trên file hiện tại; đối chiếu dòng thật trong `gamecore`, `vn/gamecore`, `engine` của bản A. Không chạy Graphify, build, exe, VM hay mạng.
- **Cách đọc resource:** chỉ đếm file và byte theo thư mục/phần mở rộng. Không giải nén PAK, không đọc DB/dump, không mở file có thể chứa tài khoản/credential.
- **Mức hiểu source:** 4/4 trục logic yêu cầu (bộ phận, hướng, trang bị vẽ lên, bảng thứ tự vẽ) đã có anchor source hiện tại = 100% phạm vi logic tĩnh.
- **Mức phủ asset sprite:** 0/1 loại sprite đóng gói đã xác nhận nội dung = 0%; mẫu PNG `avatar`/`attack` chỉ là ảnh rời chưa chứng minh là SPR gameplay.
- **Mức phủ file đã đếm:** client Resources 949/949; server Settings/NpcRes 93/93; server `pak` 7/7 file container và `maps` `.wor` 1/1. Phần member bên trong PAK chưa tính.

## MỤC SỔ THÔNG SỐ

| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn (CÓ/CẨN THẬN/KHÔNG) | Nguồn đo |
|---|---|---|---:|---|---|---|---|
| Cấu trúc | `MAX_BODY_PART` | `D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.h:23` | 6 | nhóm | Sức chứa nhóm part | KHÔNG | Đọc source tĩnh |
| Cấu trúc | `MAX_BODY_PART_SECT` | `D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.h:24` | 4 | section/nhóm | Số section mỗi nhóm | KHÔNG | Đọc source tĩnh |
| Cấu trúc | `MAX_PART` | `D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.h:25` | 24 | section | Kích thước bảng part/sort | KHÔNG | Tích 6×4 từ source |
| Layer | `emNPCRES_PART_LAYER_COUNT` | `D:/JX-build/qh9A/Classes/gamecore/CoreUseNameDef.h:20-24` | 2 | layer | BASE và EFFECT | KHÔNG | Enum source |
| Asset | `Settings/NpcRes` | `C:/Jx1CocoV3/.../gs/Settings/NpcRes` | 93 / 2.805.389 | file / byte | Bảng mô tả part/resource server | CẨN THẬN | Quét file read-only |
| Asset | Client `Resources` | `D:/JX-build/qh9A/Resources` | 949 / 78.036.052 | file / byte | Tập ảnh/âm thanh/UI của root | CẨN THẬN | Quét file read-only |
| Asset | `.spr` rời | Hai root được chỉ định | 0 | file | Chưa có header/frame rời để đo | KHÔNG | Quét theo phần mở rộng |
| Container | Server `.pak` | `C:/Jx1CocoV3/.../gs/pak` | 4 / 15.610.628 | file / byte | Có thể chứa member sprite | CẨN THẬN | Quét file read-only, chưa giải gói |
| Metadata | `nTotalDir`, `nTotalFrame`, `nInterval` | `D:/JX-build/qh9A/Classes/gamecore/KNpcRes.cpp:117-118`; `KNpcResNode.cpp:559-586` | lấy từ resource, fallback 16/0 tùy getter | hướng / frame / interval | Chọn frame và hướng khi vẽ | CẨN THẬN | Source; giá trị asset cụ thể chưa đo |

## ĐÃ XÁC MINH / CHƯA XÁC MINH

### Đã xác minh

- `KNpcResNode::Init` đọc bảng loại NPC, bảng part, sau đó nạp mô tả resource cho tối đa `MAX_PART` và cả layer EFFECT (`D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.cpp:37-118`, `:142-171`).
- Tên bảng thứ tự vẽ lấy từ trường tương ứng trong bảng loại NPC; `CSortTable::GetkTable` đọc `DEFAULT/Dir*` và section action (`D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.cpp:365-369`, `:1219-1268`).
- `GetnSort` dùng bảng riêng nếu là NPC đặc biệt, còn NPC thường trả part mặc định; `GetSort` có nhánh fallback theo hướng và khung (`D:/JX-build/qh9A/Classes/gamecore/KNpcResNode.cpp:612-630`, `:1390-1480`).
- `KNpcRes::Draw` đưa ảnh theo bảng sort và duyệt cả hai layer (`D:/JX-build/qh9A/Classes/gamecore/KNpcRes.cpp:427-428`, `:669-685`).
- Loader SPR kiểm tra header `SPR_COMMENT_FLAG`, đọc palette/offset/frame; PAK dùng `XPackFile::GetSprHeader`/`GetSprFrame` cho member nén (`D:/JX-build/qh9A/Classes/engine/KPakFile.cpp:37-90`, `:114-124`; `XPackFile.cpp:597-705`).
- `KNpcResVN.cpp` bản A có nhánh đổi section 8↔9 sau `GetnSort`; không kết luận đó là sửa đúng runtime (`D:/JX-build/qh9A/Classes/vn/gamecore/KNpcResVN.cpp:205-217`).
- Root server gs được task chỉ định có 0 file *.cpp; vì vậy báo cáo không gán các dòng C++ client thành bằng chứng mã server.

### Chưa xác minh

- Member/path cụ thể của sprite trong 4 PAK server; chưa giải gói vì task chỉ đọc và không có công cụ offline được duyệt.
- Metadata `Frames`, `Directions`, `Interval`, kích thước frame và số asset theo nam/nữ, action, hướng.
- Bảng INI sort thực tế được nạp cho từng tên nhân vật trong `Settings/NpcRes`; tên file Hán cần đọc đúng GBK.
- `Resources/avatar` và `Resources/attack` có phải sprite gameplay, ảnh UI hay ảnh thử nghiệm; chưa có provenance nối tới `KNpcRes`.
- Tương ứng client–server của từng asset, trạng thái runtime, FPS, độ trễ và độ đầy đủ khung.
- Bất kỳ kết luận nào từ APK/build artifact hoặc `.git_old`; các thư mục đó không thuộc phép đếm asset gốc của báo cáo.

## Phát hiện khi chuẩn hóa

- `JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md` và J-04 đã cảnh báo bảng sort/asset chưa được đối chiếu; báo cáo này giữ nguyên giới hạn đó và bổ sung số đếm hai root được task chỉ định.
- Tên legacy trong `Settings/NpcRes` và comment/literal source hiển thị sai khi đọc bằng UTF-8; chưa tự chuyển mã GBK hoặc sửa tên file.
- `D:/JX-build/qh9A` có APK/build artifact và `.git_old`; chúng bị loại khỏi thống kê asset sprite để không trộn nguồn sinh ra với `Resources`.
- Không tạo bảng chỉ mục `_CHIMUC` vì task giới hạn `vung_file` chỉ có báo cáo này.

## ĐỀ XUẤT TỐI ƯU

- Nếu có task riêng được duyệt, dùng một parser offline đã được kiểm soát để đọc **index** PAK, ghi manifest `path/member/size/hash/header` không chứa payload hay thông tin truy cập; sau đó đối chiếu `GetFileName` với member path.
- Đọc đúng mã GBK của `Settings/NpcRes` và lập bảng tên–mã–chữ đúng trước khi điền ma trận nam/nữ × action × hướng × frame.
- Chỉ đo runtime sau khi được cấp phạm vi VM/build/test; không dùng số đếm tĩnh thay cho FPS, kích thước frame hoặc độ đủ khung.

## Kiểm chứng, lỗi và bàn giao

- Phương pháp: đọc chuẩn báo cáo, mục lục, hướng dẫn tra cứu, báo cáo K-01/J-01/J-04/H-04 và BUG-001; kiểm file thật trong client `qh9A` và server `gs`; đếm file/byte bằng PowerShell; đọc dòng source hiện tại.
- Không chạy exe cấm, không build, không VM, không mạng, không giải nén PAK, không đọc DB/dump và không sửa mã nguồn/byte gốc.
- `rg` không có sẵn trong môi trường; đã dùng PowerShell giới hạn thư mục như AGENTS.md yêu cầu.
- Ghi nhịp `D:\JX-wt\K-02a.nhip` bị `Access denied`; không thể tạo/ghi ở ngoài worktree. Đây là blocker của yêu cầu nhịp, không phải blocker của khảo sát.
- Báo cáo được ghi UTF-8 không BOM tại `JX1_OPS/REPORTS/K-02-nhan-vat.md`. Chưa stage/commit/push theo yêu cầu không commit.
- **Kết quả cuối task:** hoàn tất phần kiểm kê tĩnh theo `vung_file`; trạng thái `PARTIAL` vì chưa xác định member sprite trong PAK và chưa đo metadata/runtime.
- **Kỹ năng đã dùng:** `jx1-retrofit`, `jx1-read-server`, `jx1-read-client`, `jx1-parameters`, `jx1-knowledge`, `jx1-report`.
- liên quan: `JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md`, `JX1_OPS/REPORTS/J-01-animation-nhan-vat-tran.md`, `JX1_OPS/REPORTS/J-04-lop-chong-nhan-vat.md`, `JX1_OPS/BUGS/BUG-001.md`, `JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md`