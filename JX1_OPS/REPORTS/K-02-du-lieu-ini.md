TÓM TẮT 1/5: [NGUỒN] Kiểm kê tĩnh K-02f đã đếm 2.107 tệp .txt/.ini ở server gs và 482 tệp ở client bản A.
TÓM TẮT 2/5: [NGUỒN] Server có 2.007 tệp dưới Settings. Client có 120 tệp trong hai cây data và Resources.
TÓM TẮT 3/5: [NGUỒN] Hai bản mã có KTabFile để đọc bảng Tab và KIniFile để đọc mục [Section] và cặp khóa=giá trị.
TÓM TẮT 4/5: [CHƯA KIỂM] Kiểm kê thấy một .wor dạng rời ở server. Nội dung PAK và dữ liệu mà bản chạy thực sự nạp chưa kiểm tra.
TÓM TẮT 5/5: [NGUỒN] Chỉ đọc dữ liệu và mã. Chưa build, chạy exe, VM, thử nghiệm game hoặc truy cập mạng. Tổng quan nhận để commit.

# K-02f — Kiểm kê dữ liệu .txt và .ini

Loại: khảo sát  
Chủ đề: Kiểm kê dữ liệu rời và xác định điểm đọc bảng vật phẩm, kỹ năng, nhiệm vụ và cấu hình.  
Từ khóa: vật phẩm, kỹ năng, nhiệm vụ, cấu hình, Settings, KTabFile, KIniFile, .wor  
Trạng thái: PARTIAL — đã đếm tệp, đang đối chiếu nguồn đọc.  
Độ phủ: 2.589/2.589 tệp rời tìm thấy thuộc hai phần mở rộng, theo số tệp và byte.  
Liên quan: `JX1_OPS/TASKS/K-02.md`, `JX1_OPS/REPORTS/K-01-ban-do-truyen-tin-hieu.md`, `JX1_OPS/REPORTS/K-03a.md`, `JX1_OPS/REPORTS/K-03b.md`, `JX1_OPS/REPORTS/K-03c.md`, `JX1_OPS/REPORTS/K-03d.md`.  
Cần tôi quyết định: không

```mermaid
flowchart LR
    F["Tệp rời hoặc mục trong PAK"] --> P["KPakFile"]
    P --> T["KTabFile: bảng Tab"]
    P --> I["KIniFile: nhóm và khóa"]
    T --> G["Vật phẩm, kỹ năng, nhiệm vụ"]
    I --> C["Cấu hình, danh sách hoạt động, .wor"]
```

## Phạm vi và độ phủ

| Gốc | Vị trí | Số tệp .txt | Byte .txt | Số tệp .ini | Byte .ini |
|---|---|---:|---:|---:|---:|
| G | `C:/Jx1CocoV3/Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_/gs` | 1.309 | 23.329.302 | 798 | 4.064.527 |
| A | `D:/JX-build/qh9A` | 291 | 3.039.994 | 191 | 108.940 |
| Cộng | Theo đường dẫn vật lý | 1.600 | 26.369.296 | 989 | 4.173.467 |

**ĐÃ XÁC MINH** (18/11/2026, UTC+07). Đếm đệ quy chỉ đọc metadata của hai gốc, kể cả tệp ẩn. Nhóm theo thư mục và phần mở rộng không phân biệt hoa thường rồi cộng số byte từ `FileInfo.Length`. Ghi nhận 0 lỗi duyệt và 0 điểm chuyển hướng ở mỗi gốc. Tính cả tệp rỗng, bản sao theo đường dẫn, dữ liệu trung gian và tài liệu đi kèm. Dữ liệu nhạy cảm chỉ nằm trong số tổng hợp metadata.

### Server — thư mục cấp một

| Thư mục | .txt (tệp) | .txt (byte) | .ini (tệp) | .ini (byte) |
|---|---:|---:|---:|---:|
| `(gốc)` | 2 | 3.060 | 9 | 5.635 |
| `DataFiles` | 2 | 3.269 | 0 | 0 |
| `GameData` | 0 | 0 | 3 | 1.445 |
| `Logs` | 47 | 597.363 | 0 | 0 |
| `maps` | 0 | 0 | 14 | 71.841 |
| `Msg` | 1 | 931 | 0 | 0 |
| `script` | 10 | 33.550 | 3 | 4.952 |
| `Settings` | 1.240 | 22.690.963 | 767 | 3.977.025 |
| `TongSet` | 7 | 166 | 2 | 3.629 |
| **G, tổng** | **1.309** | **23.329.302** | **798** | **4.064.527** |

### Server — chi tiết dưới Settings

Mỗi dòng thư mục gồm cả các thư mục con. `Settings/(gốc)` chỉ gồm các tệp trực tiếp trong `Settings`.

| Thư mục | .txt (tệp) | .txt (byte) | .ini (tệp) | .ini (byte) |
|---|---:|---:|---:|---:|
| `Settings/(gốc)` | 49 | 3.661.839 | 33 | 799.453 |
| `Settings/Ai` | 2 | 1.316 | 0 | 0 |
| `Settings/battles` | 249 | 278.923 | 0 | 0 |
| `Settings/dropitem` | 9 | 5.254 | 0 | 0 |
| `Settings/droprate` | 0 | 0 | 201 | 862.417 |
| `Settings/event` | 6 | 139.097 | 0 | 0 |
| `Settings/faction` | 0 | 0 | 3 | 2.558 |
| `Settings/FsJinMai` | 1 | 4.305 | 0 | 0 |
| `Settings/item` | 117 | 11.712.175 | 4 | 14.244 |
| `Settings/JishouShop` | 2 | 202 | 0 | 0 |
| `Settings/lang` | 10 | 191.803 | 0 | 0 |
| `Settings/mapdroprate` | 0 | 0 | 496 | 2.013.497 |
| `Settings/mapmovepos` | 3 | 223 | 0 | 0 |
| `Settings/MapPos` | 61 | 243.818 | 0 | 0 |
| `Settings/maps` | 518 | 1.046.612 | 0 | 0 |
| `Settings/Marketshop` | 2 | 183 | 0 | 0 |
| `Settings/meridian` | 2 | 6.002 | 0 | 0 |
| `Settings/music` | 1 | 4.122 | 1 | 2.034 |
| `Settings/npc` | 10 | 36.393 | 4 | 910 |
| `Settings/NpcRes` | 91 | 2.786.458 | 2 | 18.931 |
| `Settings/obj` | 3 | 154.819 | 2 | 820 |
| `Settings/player` | 0 | 0 | 11 | 11.853 |
| `Settings/ReBorn` | 1 | 784 | 0 | 0 |
| `Settings/RoleVip` | 1 | 698 | 0 | 0 |
| `Settings/Task` | 66 | 348.165 | 4 | 15.515 |
| `Settings/Tong` | 0 | 0 | 1 | 99 |
| `Settings/trap` | 4 | 2.036 | 0 | 0 |
| `Settings/Ver` | 0 | 0 | 2 | 600 |
| `Settings/vn` | 32 | 2.065.736 | 1 | 232.312 |
| `Settings/Weather` | 0 | 0 | 2 | 1.782 |
| **Settings, tổng** | **1.240** | **22.690.963** | **767** | **3.977.025** |

### Client bản A — thư mục cấp một

| Thư mục | .txt (tệp) | .txt (byte) | .ini (tệp) | .ini (byte) |
|---|---:|---:|---:|---:|
| `(gốc)` | 5 | 38.149 | 0 | 0 |
| `cocos2d` | 110 | 212.236 | 0 | 0 |
| `data` | 12 | 887 | 41 | 14.773 |
| `proj.android` | 146 | 2.782.698 | 100 | 62.778 |
| `Resources` | 17 | 5.327 | 50 | 31.389 |
| `Up testflight` | 1 | 697 | 0 | 0 |
| **A, tổng** | **291** | **3.039.994** | **191** | **108.940** |
