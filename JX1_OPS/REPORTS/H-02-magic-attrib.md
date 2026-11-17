TÓM TẮT 1/5 — PARTIAL: khảo sát tĩnh đã xong; commit local bị chặn quyền index.lock; không sửa source, không build/chạy game, không mạng/VM.
TÓM TẮT 2/5 — Mỗi dòng gồm ID loại thuộc tính và 3 tham số; item có 7 base, 6 requirement, 6 magic, 2 yin và 6 rong.
TÓM TẮT 3/5 — Roll thường lọc tiền/hậu tố, loại đồ, ngũ hành, mức 1–10; bảng local có 369 dòng và 48 ID, gồm cả mức 11 ngoài nhánh này.
TÓM TẮT 4/5 — Tooltip dùng MagicDesc_mobile.Ini và chuyển mã Việt/Trung; nhánh chọn file _vn đang bị comment; PAK client [CHƯA KIỂM].
TÓM TẮT 5/5 — Có bảng số liệu, file:dòng và ma trận TESTER bên dưới; chưa xác minh runtime, chưa push vì task cấm mạng thật.

# H-02 — Dòng chỉ số trang bị (magic attrib)

Ngày khảo sát: 2026-11-17. Nhánh `task/H-02`, worktree `D:\JX-wt\H-02`; HEAD đầu task `a9ffca7e2aec574e8e32c672372a5a0f4a33382f` (không phải commit kết quả H-02).

## Phạm vi và cách đọc bằng chứng

- [NGUỒN] Chỉ đọc source và bảng dữ liệu local bằng PowerShell/Python `python -I`; không gọi dịch vụ ngoài, không đọc DB/dump/log tài khoản, không chạy binary của gói game.
- Chỉ tạo báo cáo này và nối mục `## Kết quả` vào task theo yêu cầu trực tiếp của task. Không sửa code/cấu hình, không cập nhật BAI_HOC hoặc trạng thái dùng chung.
- Các đường dẫn viết tắt dưới đây ghép với `file:dòng` để ra vị trí tuyệt đối. Số dòng tính từ 1, bao gồm header; số bản ghi dữ liệu loại header, chỉ đếm dòng không rỗng.
- [CHƯA KIỂM] Source có khớp binary/client được triển khai hay không. Không suy ra hành vi đang chạy từ source hoặc từ bản gói lưu local.

| Ký hiệu | Gốc tuyệt đối |
|---|---|
| S | `D:\JX-source\server\jxOnline\gameserver\Sources\Core\Src` |
| H | `D:\JX-source\server\jxOnline\header` |
| C | `D:\JX-source\client\Classes` |
| P | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client` |
| G | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs\Settings` |

## 1. Cấu trúc và các loại ID

[NGUỒN] `H\GameDataDef.h:403` khai báo `KMagicAttrib { int nAttribType; int nValue[3]; }`, constructor đặt tất cả bằng 0. `KItemNormalAttrib` là alias của cấu trúc này (`S\KItem.h:35`). Đây là 4 trường int; kích thước ABI thực tế [CHƯA KIỂM], không coi là layout gói mạng đã xác minh.

Phân biệt ba loại số dễ nhầm:

1. **ID thuộc tính**: `nAttribType` / `KMACP.nPropKind` / cột `属性调整类别`; là vị trí enum `MAGIC_ATTRIB`, không phải ID item hay số dòng bảng.
2. **Mức magic**: `pnaryMALevel[i]` trong `Gen_MagicAttrib`, nhánh thường chỉ nhận 1–10 (`S\KItemGenerator.CPP:925`).
3. **Dòng tra bảng**: nhánh tạo đồ chỉ định đọc trực tiếp `nGeneratorLevel[j]` làm số dòng (`S\KItemGenerator.CPP:779`). Bảng vàng dùng tham chiếu `*pSrc + 1` (`S\KItem.cpp:712`); bản ghi BPT zero-based được đổi thành dòng vật lý bằng `+2` (`S\KBasPropTbl.CPP:95`, `S\KItemGenerator.CPP:1035`). Không dùng chung offset giữa các nhánh.

| Nhóm trong KItem | Số slot | Vai trò / bằng chứng |
|---|---:|---|
| `m_aryBaseAttrib` | 7 | Chỉ số cơ bản, `S\KItem.h:217`; lấy loại và roll khoảng, chỉ dùng `nValue[0]`, hai tham số còn lại đặt 0: `S\KItem.cpp:524` |
| `m_aryRequireAttrib` | 6 | Điều kiện mặc đồ, `S\KItem.h:218`, `S\KBasPropTbl.h:128`; không cộng như một dòng thưởng |
| `m_aryMagicAttrib` | 6 | Slot 0/2/4 trực tiếp, 1/3/5 cần kích hoạt; `S\KItem.h:219`, `S\KItem.cpp:159` |
| `m_yinMagicAttrib` | 2 | Dòng mở rộng riêng của vàng/bạch kim; `S\KItem.h:207`, `S\KBasPropTbl.h:292` |
| `m_ronMagicAttrib` | 6 | Dòng rong/nhận dạng riêng, `S\KItem.h:220`, áp dụng tại `S\KItem.cpp:222` |

Client cũng khai báo 7/6/6/2/6 slot ở `C\gamecore\KItem.h:172`–`177`. Không cộng các nhóm thành “một item có 21 dòng thưởng”: requirement và điều kiện mở từng nhóm có ý nghĩa khác nhau.

| ID | Enum server | Dòng khai báo | Key tooltip |
|---:|---|---|---|
| 30 | `magic_armordefense_v` | `S\KMagicAttrib.h:43` | `armordefense_v` |
| 59 | `magic_physicsdamage_v` | `S\KMagicAttrib.h:73` | `physicsdamage_v` |
| 85 | `magic_lifemax_v` | `S\KMagicAttrib.h:100` | `lifemax_v` |
| 115 | `magic_attackspeed_v` | `S\KMagicAttrib.h:130` | `attackspeed_v` |
| 126 | `magic_addphysicsdamage_p` | `S\KMagicAttrib.h:141` | `addphysicsdamage_p` |
| 139 | `magic_allskill_v` | `S\KMagicAttrib.h:154` | `allskill_v` |
| 166 | `magic_attackratingenhance_v` | `S\KMagicAttrib.h:181` | `attackratingenhance_v` |

[NGUỒN] Enum server và client đọc được đều có `magic_normal_end = 311` (đếm thứ tự enum, không có gán số tường minh; `S\KMagicAttrib.h:329`, `C\gamecore\KMagicAttrib.h:324`). Đây là sentinel, không phải 311 loại chỉ số trang bị hợp lệ: enum còn chứa thuộc tính skill/missile và các mốc phân nhóm. Hậu tố `v/p/b` lần lượt mô tả điểm/phần trăm/bool trong chú thích `S\KMagicAttrib.h:5`; ý nghĩa cụ thể vẫn phải theo handler.

`nValue[0..2]` là ba **tham số**, không phải mặc định min/current/max cho mọi loại. Khoảng roll nằm trong `KMACP.aryRange[3]`, mỗi khoảng có `nMin/nMax` (`S\KBasPropTbl.h:115`, `:134`). Ví dụ mô tả sát thương sử dụng tham số 1 và 3; tham số khác có thể là thời gian, cấp skill, hoặc tham chiếu sang GoldMagic. [CHƯA KIỂM] Toàn bộ handler `ModifyAttrib` của từng ID và trần cộng dồn cuối cùng của nhân vật.

## 2. Bảng tra và số liệu bản gói local

[NGUỒN] BPT server dùng gốc `\settings\item\004` (`S\KBasPropTbl.CPP:16`). Các hằng đường dẫn chính ở `S\KItem.h:39`–`43`; client lại có tiền tố `\update10\settings\item\004` (`C\gamecore\KItem.h:32`–`36`). Vì vậy bảng ở G không được coi là bản bảng thực tế bên trong client.

| File dưới G | Dòng vật lý | Bản ghi không rỗng sau header | Cột header | Mục đích |
|---|---:|---:|---:|---|
| `item\004\magicattrib.txt` | 370 | 369 | 29 | Pool dòng thường, khoảng tham số, bộ lọc và tỷ lệ từng loại đồ |
| `item\004\GoldMagic.txt` | 4.361 | 4.360 | 12 | Tra ID + 3 khoảng tham số cho đồ vàng/mở rộng |
| `item\004\GoldItem.txt` | 5.946 | 5.945 | 65 | Base/requirement, DefMagic1–6, bộ và ExpandMagic1–2 |
| `item\004\platinaequip.txt` | 5.671 | 5.670 | 72 | Mẫu bạch kim, các cặp DefMagic theo mức và dòng mở rộng |
| `item\004\magicattriblevel_index.txt` | 49 | 48 | 6 | MAGIC_ID → khoảng chỉ mục cấp phục vụ tra mức |

Số bản ghi trên là số liệu file, không phải số item hợp lệ/nạp thành công. Chuỗi tên có byte Việt/Trung hỗn hợp; không kết luận lỗi game chỉ từ việc giải mã bảng bằng GB18030.

Schema `magicattrib.txt:1`, đối chiếu loader theo **thứ tự cột** tại `S\KBasPropTbl.CPP:1930`:

| Cột (1-based) | Nội dung |
|---|---|
| 1–3 | Tên tiền/hậu tố, `next`, `load` |
| 4–7 | Có phải tiền tố, ngũ hành yêu cầu, mức yêu cầu, ID loại thuộc tính |
| 8–13 | Min/max tham số 1, 2, 3 |
| 14 | Mô tả biên tập |
| 15–29 | `m_DropRate[15]`: vũ khí gần, ám khí, áo, nhẫn, dây chuyền, giày, đai, mũ, tay, bội, ngựa, mặt nạ, phi phong, ấn, trang sức |

`GoldMagic.txt:1` đặt ID ở cột 5, các khoảng ở 6–11; khác vị trí cột của magicattrib. `GoldItem.txt:1` có base tại 14–34, requirement tại 35–46, DefMagic tại 47–52 và ExpandMagic tại 58–59. Loader/struct liên quan: `S\KBasPropTbl.h:289`–`297`. Các cột cuối bảng không được coi là đã xác minh mọi đường nạp.

Ví dụ đủ tái kiểm, không chứa dữ liệu người chơi:

| File:dòng dưới G | ID / mức | Khoảng tham số 1 | Tham số 2 | Tham số 3 |
|---|---|---|---|---|
| `item\004\magicattrib.txt:2` | 126 / 1 | 5–10 | -1 / -1 | 0 / 0 |
| `item\004\magicattrib.txt:3` | 126 / 2 | 10–20 | -1 / -1 | 0 / 0 |
| `item\004\magicattrib.txt:73` | 85 / 1 | 5–20 | -1 / -1 | 0 / 0 |
| `item\004\magicattrib.txt:74` | 85 / 2 | 20–40 | -1 / -1 | 0 / 0 |
| `item\004\GoldMagic.txt:2` | 85 | -50–50 | -1 / -1 | 0 / 0 |
| `item\004\GoldMagic.txt:3` | 85 | 120–200 | -1 / -1 | 0 / 0 |

Trong 369 bản ghi magicattrib có 48 giá trị ID khác nhau, cột mức xuất hiện 1–11. **39 bản ghi mức 11** nằm tại `magicattrib.txt:332`–`370`; đây là vùng “max” ngoài giới hạn roll thường, không phải bằng chứng roll thường có cấp 11.

## 3. Roll thường, roll chỉ định và giới hạn

[NGUỒN] Luồng `Gen_Equipment(nPoint == 0)` gọi `Gen_MagicAttrib` rồi gán về item (`S\KItemGenerator.CPP:738`). Seed, sáu generator level, version và luck được lưu tại `:646`; nhánh client cũ đặt lại seed tại `:655`. [CHƯA KIỂM] Tái tạo giống hệt giữa phiên bản hiện hành và dữ liệu nhận qua giao thức.

`Gen_MagicAttrib` (`S\KItemGenerator.CPP:908`) xử lý:

1. Tối đa 6 slot, gặp mức 0 hoặc ngoài 1–10 thì dừng và xóa phần còn lại (`:925`, `:1058`). Chỉ số phía sau một slot 0 không được tiếp tục roll trong nhánh này.
2. Lấy pool theo `1 - (i & 1)`, loại trang bị, ngũ hành, mức (`:941`). `InitMAIT` chỉ đưa dòng có tỷ lệ >1 vào pool; ngũ hành -1 mở cho cả 5 hệ (`S\KBasPropTbl.CPP:247`).
3. Pool ở mức L gồm các dòng có mức yêu cầu ≤ L, do vòng chèn từ `m_nLevel` đến 10 (`S\KBasPropTbl.CPP:266`, `:282`). Không giả định mỗi mức chỉ chứa các dòng cùng mức. Dòng yêu cầu mức 11 không vào vòng chèn này.
4. Tính `nDecide = GetRandomNumber(0, 99) / (1 + nLucky * 20 / 100)`; loại dòng có `DropRate <= 1` hoặc `DropRate <= nDecide`, đã dùng, hoặc trùng `nPropKind` đã chọn (`S\KItemGenerator.CPP:959`, `:978`, `:992`). Đây là lọc ngưỡng rồi chọn một phần tử pool, không phải cộng trọng số theo DropRate.
5. Chọn vị trí bằng `GetRandomNumber(0, nSelectedCount - 1)`; roll riêng cả ba khoảng (`:1012`, `:1028`). Không có ứng viên thì dừng; hàm vẫn kết thúc với `true` sau khi xóa slot trống (`:1007`, `:1080`). Không coi `true` là bảo đảm đủ sáu dòng.
6. Nếu tham số 3 >1, dùng nó làm số dòng GoldMagic và roll lại tham số 1/3 (`:1037`). Muốn biết giá trị cuối phải xét nhánh tra tiếp này.

Các trần cấu trúc ở `S\KBasPropTbl.h:143`: 15 loại đồ × 2 tiền/hậu tố × 5 hệ × 10 mức; đây là kích thước pool, không phải trần giá trị sinh lực/sát thương. Các slot trùng loại bị loại theo ID, nhưng “cộng điểm” và “cộng %” là hai loại riêng (`S\KBasPropTbl.h:137`).

**Nhánh chỉ định khác roll thường:** `nPoint == 7` đọc trực tiếp dòng bảng, clamp luck vào 0–10 rồi nội suy nguyên `min + (max-min)*luck/10` cho ba tham số (`S\KItemGenerator.CPP:760`, `:779`, `:784`). Không áp giới hạn “mức 1–10” của nhánh chọn pool lên số dòng bảng ở đây. Các nhánh khác còn gọi random trực tiếp; chưa khẳng định tất cả đều dùng cùng cách.

Đồ vàng: `SetAttrib_MAC` đọc tham chiếu dòng `+1`, lấy ID và roll ba khoảng từ GoldMagic (`S\KItem.cpp:697`). Hai ExpandMagic được sinh tương tự rồi `SetAttrib_Yin` (`S\KItemGenerator.CPP:1380`).

[CHƯA KIỂM] Định nghĩa chính xác của helper `GetRandomNumber` (đã đọc lời gọi và KRandom, chưa truy được thân helper); tính bao gồm hai đầu, độ lệch phân phối và xử lý khoảng đảo. Công thức ngưỡng dùng phép chia nguyên; nhánh thường không thấy clamp luck như nhánh `nPoint==7`, nên đầu vào âm/biên và mẫu số 0 cần TESTER kiểm riêng. Chưa chạy các đầu vào lỗi này.

## 4. Dòng hiện, dòng ẩn và set

[NGUỒN] `ApplyMagicAttribToNPC` áp base rồi sáu magic (`S\KItem.cpp:148`). Slot 0/2/4 áp trực tiếp; slot 1/3/5 lần lượt tiêu hao `nMagicActive` (`:166`). `GetEquipEnhance` đếm quan hệ ngũ hành tương sinh từ nhân vật và các vị trí đồ kích hoạt, clamp tối đa 3 (`S\KItemList.cpp:2674`). `ApplyHiddenMagicAttribToNPC(N)` dùng slot `(N << 1)-1` (`S\KItem.cpp:408`); chỉ kiểm N>0, không thấy chặn N>3 ngay trong helper. Tính an toàn caller với dữ liệu lỗi [CHƯA KIỂM].

Hai dòng yin **khác** ba hậu tố ẩn:

- Caller mặc vàng truyền `nActiveInfo[0]=3`, `nActiveInfo[1]=Item.GetLevel()` (`S\KItemList.cpp:1744`).
- `ApplyMagicAttribToNPC` mở yin đầu ở level 5–9, cả hai ở level ≥10 (`S\KItem.cpp:195`). Đây là **level item**, không phải số món trong bộ, cũng không phải mặc định cấp nhân vật.
- Tooltip bản gói dùng chính `m_CommonAttrib.nLevel` cho mốc 5/10 (`P\Classes\gamecore\KItem.cpp:2517`).

Set riêng: `nSet`, `nSetId`, `nSetNum`, `nBigSet` nằm ở `S\KItem.h:146`. `GetIfActive` đếm đồ cùng `GetSet()` và so `GetSetNum()`, đặt `m_bActiveSet` khi đủ bộ (`S\KItemList.cpp:9556`, `:9571`, `:9600`). Còn các nhánh toàn kích hoạt theo `m_CurrentAllJiHuo`, `nEquipAllActive`, `nGoldAllActive` (`:9625`, `:9644`). Hàm được gọi sau mặc đồ (`:1779`). [CHƯA KIỂM] Mọi nơi tiêu thụ `m_bActiveSet`, tất cả ngoại lệ bộ, và thay đổi buff qua mỗi chu kỳ mặc/tháo; không khẳng định đủ bộ tự cộng thêm một mảng magic mới.

[NGUỒN] Sentinel không đồng nhất giữa các tầng: header định nghĩa `INVALID_ATTRIB=-1` (`S\KMagicAttrib.h:4`), constructor/slot roll trống dùng 0, đường áp kiểm khác -1, còn formatter bỏ ID ≤0 (`C\gamecore\KMagicDesc.cpp:724`). Cần kiểm handler với ID 0; chưa coi đây là lỗi thực tế. Ngoài mảng dữ liệu, source có dòng thưởng skill riêng cho vũ khí cường hóa ≥12/≥15 (`S\KItem.cpp:183`); không khảo sát sâu vì thuộc H-03.

## 5. Tên dòng và chuỗi Việt/Trung ở client

Luồng đã đọc được:

`P\Classes\gamecore\KItem.cpp:2449` → `g_MagicDesc.GetDesc` → `g_MagicID2String(ID)` → key trong `[Descript]` → `translate` → thay tham số → gắn màu theo trạng thái kích hoạt.

- `C\gamecore\KMagicDesc.cpp:17` chứa bảng key `MAGIC_ATTRIB_STRING[][64]`; `:986` tra theo ID, ngoài miền trả key sentinel. Không lấy tên tooltip trực tiếp từ cột tên tiền/hậu tố của magicattrib.
- `C\gamecore\KMagicDesc.cpp:11` khai báo `\settings\MagicDesc_mobile.Ini`; `:12` có tên `_vn`, nhưng điều kiện chọn `_vn` ở `:378` bị comment, thực tế source nạp file thường tại `:381`. Đã kiểm `P\Classes\gamecore\KMagicDesc.cpp:375` cùng nội dung.
- `GetDesc` lấy `[Descript]` theo key rồi gọi `translate` (`C\gamecore\KMagicDesc.cpp:726`, `:730`). `#d1/#d2/#d3` đọc ba tham số; các mã 4/7 còn tách low/high word của tham số đầu (`:761`). Do đó không tự đổi thứ tự hoặc format bảng mà chưa đối chiếu parser.
- `C\vn\Translate.cpp:37` là chuyển mã, không phải từ điển dịch ngữ nghĩa: CN gọi UTEXT, ngôn ngữ khác gọi V2U và visualFallbackFix. Macro tại `C\engine\KGbktoUtf8.h:22`–`25` ánh xạ GBK→UTF-8 và TCVN→UTF-8. Tiếng Việt phải có trong byte đầu vào; gọi translate không tự biến câu Trung thành câu Việt.
- Các nhãn phụ ngũ hành dùng `language_mobile` qua XML (`C\gamecore\KMagicDesc.cpp:805`). [CHƯA KIỂM] Tệp XML được chọn trong cấu hình ngôn ngữ đang triển khai.
- Màu dòng magic hoạt động/ẩn được chọn ở `P\Classes\gamecore\KItem.cpp:2454`, `:2472`; dòng rỗng bị bỏ tại `:2450`. Yin dùng mốc level tại `:2518` và `:2531`.

**Bản chuỗi tìm thấy trên đĩa:** `G\MagicDesc.ini:1` và `G\MagicDesc_mobile.ini:1` đều có `[Descript]`. File thứ nhất chứa chuỗi Trung; file mobile chứa byte Việt legacy. Ví dụ key `lifemax_v` nằm ở file Trung dòng 92 và file mobile dòng 103; `armordefense_v` tại 35/43; `physicsdamage_v` tại 65/76. Đây là bằng chứng vị trí dữ liệu ngôn ngữ trong **bản gói server local**, không phải xác nhận nội dung PAK client.

[CHƯA KIỂM] Không tìm thấy file rời MagicDesc/magicattrib/GoldMagic/GoldItem khi tìm đúng các tên này trong `P\Resources` và `P\data`. Có danh sách PAK tại `P\Resources\paklist.ini:1` và `P\data\data\paklist.ini:1`, nhưng không thấy file `.pak` trực tiếp ở `P\data` hoặc `P\data\data`. Chưa giải PAK, chưa xác minh file nào thắng theo ưu tiên package/update. Không sao chép nội dung cấu hình tài khoản/khóa từ gói vào báo cáo.

Đối chiếu byte toàn file: `C\gamecore\KItem.h` và `KMagicDesc.cpp` giống bản dưới `P\Classes\gamecore`; `KItem.cpp` khác (4.156 so với 4.116 dòng). Đã đọc trực tiếp các đoạn tooltip của bản P và dùng đúng số dòng P ở trên; không giả định toàn client source giống nhau.

## 6. Ma trận test đề xuất cho TESTER

**Chưa chạy bất kỳ test runtime/build nào.** Chỉ thực hiện trong môi trường thử đã được PM cho phép, dữ liệu tổng hợp; không dùng tài khoản thật, không thực hiện trên Main VM trong task này.

| Ca | Chuẩn bị / thao tác đề xuất | Bằng chứng cần ghi |
|---|---|---|
| T01 — cấu trúc/ID | Mẫu từng ID 30, 59, 85, 126; ba tham số phân biệt | ID, key tooltip, ba giá trị trước/sau format; xác minh không nhầm ID với row |
| T02 — khoảng roll | Fixture min=max và min<max, gồm giá trị âm như GoldMagic dòng 2 | Giá trị cuối thuộc khoảng; kiểm hai đầu theo helper thực tế; không suy xác suất từ vài mẫu |
| T03 — số dòng | Mảng mức `[1,0,1,1,1,1]`, toàn 0, sáu mức 10 | Slot sau 0 được xóa; đủ/thiếu ứng viên và return code; không coi true là đủ 6 |
| T04 — mức 11 | So nhánh roll thường và tạo chỉ định dòng 332/342 | Roll thường từ chối/không nạp level 11; chỉ định dùng row nào, offset bao nhiêu |
| T05 — pool/luck | Cùng loại đồ/hệ/mức, DropRate 0/1/2/100; luck hợp lệ rồi kiểm biên bằng harness | Pool sau lọc, nDecide, lựa chọn, trùng ID; kiểm mẫu số trước khi chạy trường hợp âm |
| T06 — hậu tố ẩn | Item đủ 6 magic; thay ngũ hành nhân vật/đồ để kích hoạt 0/1/2/3 | Slot 1/3/5 cộng và gỡ đúng; màu client khớp chỉ số server |
| T07 — yin và set | Đồ vàng level 4/5/9/10; riêng bộ thiếu/đủ ngưỡng GroupNum | Yin mở theo level, cờ set theo số món; mặc/tháo không cộng lặp hoặc sót buff |
| T08 — liên kết GoldMagic | Tham số 3 >1 và các tham chiếu DefMagic/ExpandMagic có min=max | Dòng tra thật, ID/giá trị trước sau lần tra thứ hai; lỗi thiếu dòng xử lý ra sao |
| T09 — Việt/Trung | Giải đúng PAK của bản client thử, kiểm key life/defense/damage; đổi locale | Tên file thắng, hash bản dữ liệu, byte encoding, ảnh tooltip có dấu và thứ tự tham số |
| T10 — trần/đồng bộ | Lưu/đăng nhập lại, mặc/tháo; giá trị sát trần handler | Seed/version/row và giá trị tái tạo; trần resistance/damage thật, overflow/ID lỗi qua harness |

## 7. Kiểm tra đã làm, lỗi công cụ và phần chưa xác minh

- Đã xác nhận worktree/branch một lần trước ghi; task có trong `TASKS/BACKLOG.md:89`; đọc nội dung task bằng UTF-8 và giữ nguyên phần task có sẵn.
- Đã trích trực tiếp cấu trúc, enum, roll, loader, caller kích hoạt và formatter; thống kê 5 bảng bằng `csv.reader` trong lệnh `python -I`, không tạo parser/script phụ trên đĩa.
- Lỗi công cụ: PowerShell mặc định hiển thị sai dấu khi đọc task; đọc lại với `-Encoding UTF8` khắc phục. `rg` không được nhận diện (`The term 'rg' is not recognized`), chuyển sang công cụ sẵn có. Python ban đầu gặp `UnicodeEncodeError: 'charmap' codec can't encode characters`, đã đặt stdout UTF-8 cho các lần đọc sau.
- Một số đường dẫn suy từ tên chưa tồn tại (`Folder` ngay worktree, `KCoreDef.h` và đường dẫn Engine ban đầu); đã bám các root xác nhận để tìm đúng nguồn. Không sửa/chạy công cụ cài thêm.
- `Get-ChildItem -LiteralPath ... -Include ...` trong phiên này trả danh sách rộng hơn mẫu dự kiến; đã đổi sang lọc tên chính xác bằng pathlib và chỉ dùng file liên quan. Có lần trích output vượt giới hạn; các đoạn dùng làm kết luận đã đọc lại trong khoảng dòng hẹp.
- [CHƯA KIỂM] Binary đang chạy, DB, mạng/VM, PAK client, độ tương ứng source↔gói thực thi, handler/trần từng ID, toàn bộ nhánh sinh đồ và giao thức đồng bộ. Không có kết quả build/test runtime để tuyên bố đạt.
- Trạng thái khảo sát: **PARTIAL** về điểm lưu Git; nội dung khảo sát tĩnh đã hoàn tất, các mục [CHƯA KIỂM] là việc xác nhận tiếp của TESTER/PM.
- Commit kết quả: **BỊ CHẶN – CHƯA PUSH**. Lệnh `git add`/`git commit` không tạo được `D:/jx1-reports/.git/worktrees/H-02/index.lock`: `Permission denied`; đã không thử vượt quyền. Kết quả vẫn lưu local. Chưa push và không thử push vì người dùng cấm mạng thật trong task. PM nhận hai file để review và đưa vào điểm lưu được phép.

