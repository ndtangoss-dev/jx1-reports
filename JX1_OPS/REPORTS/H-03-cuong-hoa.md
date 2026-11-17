## TÓM TẮT 5 DÒNG

1. DONE — Hoàn tất khảo sát tĩnh H-03 ngày 17/11/2026; chỉ ghi báo cáo và mục kết quả task, không sửa source/cấu hình.
2. Gói server cũ có trần +5; tài liệu Coco ghi trần +15 và cấu hình test 100%; chưa xác minh cấu hình/binary đang chạy.
3. Lua yêu cầu một trang bị phù hợp + một vật phẩm loại 403/404/405 và 200.000 tiền; +1/+2 chắc chắn qua nhánh nguồn, từ lần lên +3 mới xét thất bại.
4. Coco chỉ sửa EnChance thành +5%/cấp trên giá trị gốc; đồ vàng/luyện hóa còn qua EnChanceRong theo công thức cũ, EnChanceBao hiện không tính gì.
5. Có bảng +0..+30, luật thất bại, đường dẫn file:dòng và đề xuất TESTER; mọi kết luận runtime, xác suất thực nghiệm và trạng thái triển khai đều [CHƯA KIỂM].

## 1. Phạm vi và quy ước bằng chứng

Thực hiện trên nhánh `task/H-03`, workspace `D:\JX-wt\H-03`. Kiểm tra Git ban đầu chỉ thấy `JX1_OPS/TASKS/H-03.md` untracked; giữ nguyên nội dung được giao và chỉ nối mục kết quả theo yêu cầu trong chính task. Không kết nối mạng/VM, không chạy game/server/exe, không build, không đọc dữ liệu tài khoản hay ghi bí mật. Python chỉ gọi bằng `python -I`; các đoạn Python dùng để đọc/lọc trực tiếp và tính bảng số học, không tạo script phụ.

Các tiền tố dưới đây là đường dẫn tuyệt đối; ký hiệu `S/KItem.cpp:3800` nghĩa là file tương ứng bên dưới, dòng 3800 tại thời điểm khảo sát:

| Ký hiệu | Đường dẫn chỉ đọc |
|---|---|
| S | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src` |
| E | `C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Engine\Src` |
| G | `C:\Jx1CocoV3\Folder\ServerNew-20260116T043145Z-3-001\ServerNew\_bin_v2_\gs` |
| C | `D:\Android\b\Client\Classes` |
| B | `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes` |
| R | `C:\Jx1CocoV3\docs-analysis\reports` |

“Gốc” trong báo cáo là gói cấu hình lưu tại G, code trước patch trong `S/KItem.cpp.bak-qh` và client baseline B. Source S hiện đã có patch Coco, không được gọi nhầm là source nguyên bản. [CHƯA KIỂM] Quan hệ giữa các file này và binary server/APK đang triển khai; không suy ra runtime từ tên thư mục hay báo cáo lịch sử.

## 2. Luồng xử lý và nguyên liệu

Luồng: callback UI → `script\System\qianghua.lua::sysqianghua` → Lua API `ItemQiangHua` → `LuaItemQiangHua` → `KItemList::QiangHua` → hàm tăng chỉ số → `SynPlayerItem` → client nhận và tính lại. Các điểm nối: `S/KProtocolProcess.cpp:9318`, `S/ScriptFuns.cpp:7925`, `S/ScriptFuns.cpp:26838`, `S/KItemList.cpp:5393`, `C/gamecore/KProtocolProcess.cpp:1642`.

| Điều kiện / nguyên liệu | Luật đọc trực tiếp | Bằng chứng |
|---|---|---|
| Tiền | Phải có ít nhất 200.000 trước khi xét vật phẩm | `G/script/System/qianghua.lua:26` |
| Số ô giao diện | Từ chối nếu `nNum > 2`; tổ hợp được nhận phải có đúng một trang bị và một đá tương ứng | `G/script/System/qianghua.lua:44`, `:160` |
| Đá cho đồ thường | Genre 4, detail 403, biến `nIsQlanShi`; ghép với trang bị xanh/vàng không thuộc hai nhóm sau | `G/script/System/qianghua.lua:88`, `:106`, `:117`, `:164` |
| Đá cho đồ văn cương | Genre 4, detail 404, biến `nIsQgangShi`; nhóm đồ được Lua phân loại qua `arr[10] > 0`, sau kiểm tra nhận dạng | `G/script/System/qianghua.lua:92`, `:103`, `:114`, `:162` |
| Đá cho đồ nhận dạng | Genre 4, detail 405, biến `nIsQbianShi`; nhóm có `arr[13] > 0` | `G/script/System/qianghua.lua:95`, `:100`, `:111`, `:160` |
| Nhóm trang bị ở C++ | `item_equip` và có GoldId hoặc IsPurple hoặc IsBlue | `S/KItemList.cpp:5397` |
| Tăng xác suất theo cấp đá | Có đọc `nBsLevel` nhưng không dùng trong phép thử; Lua đang truyền `nRank=0` cho cả ba nhóm | `S/KItemList.cpp:5412`, `:5441`; `G/script/System/qianghua.lua:161`, `:163`, `:165` |
| Trừ tiền | `Pay(200000)` gọi sau API, không kiểm tra `nGong` trước khi trừ | `G/script/System/qianghua.lua:159`, `:170` |

Các số 403/404/405 là **detail type, không phải instance ID hay ID dòng của bảng item**. Tên Việt chuẩn của đá, particular/level được bán/phát, và quy tắc stack [CHƯA KIỂM]; không gán một tuple đầy đủ từ tên biến. `Settings/ItemQuest.txt` được xem header nhưng là bảng nhiệm vụ, không chứng minh định nghĩa ba đá này. Luật kết hợp thực tế ở Lua chỉ kiểm genre/detail; không thấy ràng buộc cấp đá theo cấp +N tại đoạn này.

Tác động cần chú ý: nếu đã qua kiểm tra đầu vào Lua, việc C++ từ chối do đạt trần hoặc thất bại giữ cấp vẫn đi tới `Pay(200000)` trong source này. [CHƯA KIỂM] Tiền thực tế và thông báo ở binary triển khai. C++ gọi `Remove(nBaoshiID)` rồi `ItemSet.Remove(nBaoshiID)` ở các nhánh thành công, rớt cấp và giữ cấp (`S/KItemList.cpp:5450`, `:5473`, `:5492`); không có lệnh hủy trang bị mục tiêu tại các nhánh thất bại này. [CHƯA KIỂM] Hành vi với một stack nhiều đá, vì đây là xóa theo index chứ không thấy lệnh giảm stack một đơn vị trong đoạn cường hóa.

## 3. Cấu hình, trần cấp và xác suất

`QiangHuaRank=A,B,Nmax`, `QiangHuaSet=T`. C++ từ chối nếu cấp hiện tại `n >= Nmax` (`S/KItemList.cpp:5427`). `EnChance` riêng lẻ kẹp 0..30, `EnChanceRong` chặn phía trên về 30; đây là giới hạn hàm, không phải quyền cường hóa qua giao diện (`S/KItem.cpp:3804`, `:3863`, `:3922`).

| File / nguồn | QiangHuaRank | QiangHuaSet | Ý nghĩa và độ chắc |
|---|---|---:|---|
| `G/Settings/gamesetting.ini:460`, `:462` | `20000,40000,5` | 10 | File gói cũ; không khẳng định được nạp |
| `G/Settings/gamesetting_gs001.ini:478`, `:480` | `1000,2000,5` | 10 | File theo tên server; trần +5 |
| `G/Settings/gamesetting_gs002.ini:478`, `:480` | `1000,2000,5` | 10 | Như gs001 |
| `G/Settings/gamesetting_gs003.ini:474`, `:476` | `1000,2000,5` | 10 | Như gs001 |
| `G/Settings/gamesetting_gs004.ini:474`, `:476` | `1000,2000,5` | 10 | Như gs001 |
| `G/Settings/gamesetting_gs005.ini:474`, `:476` | `1000,2000,5` | 10 | Như gs001 |
| `G/Settings/gamesetting_gs006.ini:474`, `:476` | `1000,2000,5` | 10 | Như gs001 |
| `G/Settings/gamesetting_bin_v2_bak.ini:473`, `:475` | `1000,2000,5` | 10 | Backup, không coi là cấu hình hiệu lực |
| `R/63-yeu-cau-cuong-hoa-chi-so-ky-nang-set.md:9`; `R/65-chot-set-vu-khi-va-trang-ky-nang.md:8` | `1000,1,15` | [CHƯA KIỂM] | Tài liệu lịch sử: test 100%, chưa xác minh file đang chạy |
| `R/66-sua-set-vuot-ngoai-kiem.md:10` | `1000,2000,15` | [CHƯA KIỂM] | Giá trị đề nghị trả về; không chứng minh đã trả |

`S/KCore.cpp:262` tạo đường dẫn `\Settings\gamesetting_%s.ini` từ `nParmName`, rồi Load ở dòng 265. Vì vậy không lấy riêng `gamesetting.ini` làm cấu hình chắc chắn hiệu lực. [CHƯA KIỂM] Tham số khởi động, file trong VM và file thực tế đã được nạp.

Phép thử chính xác tại `S/KItemList.cpp:5441`:

```cpp
if (nEnChance >= 2 && g_Random(A + nRank) < g_Random(B)) {
    // thất bại
}
```

Với `nRank=0`, lên +1 và +2 không gọi phép so sánh này; từ **cấp hiện tại +2** (lần thử lên +3) mới xét thất bại. Không có bảng xác suất giảm dần theo +N trong đoạn code này. `E/KRandom.cpp:68` cập nhật cùng một seed và trả `seed % nMax` tại dòng 91; `g_Random(1)=0`, nên `A,1,15` bảo đảm điều kiện thất bại luôn sai, nếu đầu vào đã hợp lệ và chưa đạt trần.

**Không được đọc A/B là xác suất thành công.** Nếu tạm giả định hai giá trị ngẫu nhiên độc lập, đều trong `[0,A-1]`, `[0,B-1]`, thì với `B>=A`:

`P(thành công lý tưởng) = P(X>=Y) = (A+1)/(2B)`.

| Cặp A,B | Xác suất thành công theo giả định độc lập, từ lần lên +3 |
|---|---:|
| 1000,2000 | 25,025% |
| 20000,40000 | 25,00125% |
| 1000,1 | 100% theo điều kiện code, không cần giả định độc lập |

[CHƯA KIỂM] Các tỷ lệ 25,025%/25,00125% là mô hình số học để giải thích phép so sánh, **không phải tỷ lệ thật của PRNG**. Hai lần gọi dùng seed nối tiếp, có tương quan, modulo có sai lệch và thứ tự đánh giá toán hạng C++ cần đối chiếu build. Không chạy mô phỏng PRNG, không lấy mẫu runtime và không gán tỷ lệ thực nghiệm.

## 4. Thành công, rớt cấp, giữ cấp và tiêu hao

Khi thất bại với `2 <= n < T`, code làm `n -= 2`, sau đó vẫn gọi hàm tăng với `n+1`: kết quả cuối là **cấp ban đầu -1**, không phải -2 (`S/KItemList.cpp:5443`, `:5445`, `:5478`, `:5502`). Nếu `n >= T`, code xóa đá và return 0, không tái tạo chỉ số/cấp (`:5448`).

| Cấp hiện tại n | Thành công | Thất bại | Đá / tiền ở đường Lua này |
|---|---|---|---|
| 0,1, nếu dưới trần | n+1 | Không xét random | Xóa index đá; gọi Pay 200.000 |
| 2..T-1, nếu dưới trần | n+1 | n-1 | Xóa index đá; gọi Pay 200.000 |
| T..Nmax-1 | n+1 | Giữ n, API trả 0 | Xóa index đá; Lua vẫn gọi Pay 200.000 |
| n>=Nmax | API từ chối, giữ n | Không roll | C++ return trước xóa đá; Lua vẫn tới Pay nếu đã qua kiểm tra tổ hợp |

Với cấu hình gói cũ `Nmax=5,T=10`: +0→+1 và +1→+2 không roll; +2 thử lên +3 thất bại về +1; +3 thất bại về +2; +4 thất bại về +3; +5 bị chặn. Nhánh giữ cấp từ +10 không thể đạt qua cường hóa bình thường với trần +5 này.

Với `Nmax=15`: nếu T vẫn là 10 thì +2..+9 thất bại rớt một cấp, +10..+14 thất bại giữ cấp. [CHƯA KIỂM] T của cấu hình Coco thực tế. Với cấu hình test B=1, nhánh thất bại không được thực thi, nên thử 100% không nghiệm thu được luật rớt/giữ cấp.

## 5. Chỉ số: gốc, Coco và nhánh còn công thức cũ

### 5.1 Công thức gốc được bảo tồn

`S/KItem.cpp.bak-qh:3760` và `B/gamecore/KItem.cpp:3490` có `EnChance` cũ. `JIACHENG_VAL=2` (`S/KItem.h:44`). Chỉ duyệt 6 dòng `m_aryMagicAttrib`, thuộc loại có trong `ForBitEn`, và giá trị hiện tại ít nhất `2<<1 = 4`. Tính lại từ `m_TempMagicAttrib[i].nValue[0]`:

```text
x = giá trị gốc
lặp N lần:
    x = x + (x >> 2)
    nếu (x - ((x >> 2) << 2)) > 2: x = x + 1
```

Đây là tăng khoảng 25% cộng dồn, với hiệu chỉnh số nguyên **sau phép cộng**, không đơn giản bằng làm tròn `gốc*1,25^N`. Nguồn: `S/KItem.cpp.bak-qh:3770`, `:3774`, `:3778`; công thức tương tự còn chạy trong `S/KItem.cpp:3860` (`EnChanceRong`).

`G/Settings/ForbititMap.txt:1` là bảng tab có cột `ForBitEn`; dòng 2..11 lần lượt: **135,101,102,103,104,105,114,160,135,85**. Có 10 hàng nhưng **9 ID khác nhau**, 135 lặp hai lần. `S/KItem.cpp:3985` trả 1 khi tìm thấy ID: dù tên cột có “ForBit”, nhánh cũ đang dùng các ID đó như danh sách cho phép tăng. File được nạp qua `S/KCore.cpp:602`.

### 5.2 Công thức Coco trong EnChance

`S/KItem.cpp:3795`, `:3800` và `C/gamecore/KItem.cpp:3511`, `:3515` cùng dùng:

```text
N = clamp(cấp yêu cầu, 0, 30)
V = V0 + trunc_toward_zero((V0*5*N + (V0>=0 ? 50 : -50))/100)
```

Lấy lại từ giá trị gốc; với số dương, phần tăng được làm tròn gần nhất, nửa đơn vị lên. Đây là **+5% giá trị gốc/cấp**, không nhân 1,05 theo lần nâng. Code return sớm ở `S/KItem.cpp:3818`, `C/gamecore/KItem.cpp:3529`; phần `ForBitEn` cũ còn bên dưới nhưng không chạy qua đường này.

Giới hạn áp dụng:

- Chỉ 6 dòng `m_aryMagicAttrib` có type nằm trong `JxQhScalable`; không tăng toàn bộ mọi trường của vật phẩm. Không thấy nhân `m_aryBaseAttrib`, `m_ronMagicAttrib`, `m_BaoShiMagicAttrib` trong nhánh mới này.
- Nhân `nValue[0]`; chỉ type 59..64 và `m_TempMagicAttrib[q].nValue[2]>0` mới nhân thêm `nValue[2]`; không nhân `nValue[1]` (`S/KItem.cpp:3812`, `C/gamecore/KItem.cpp:3523`).
- Allowlist S dòng 3782..3793 và C dòng 3499..3509 trùng các nhóm ID: 56..57,59..65; 85,86,88,89,90,92,93,94,96; 101..105,109,113..126,129..138; 145..147,150..152,161..173; 183,185,186,213..218,224,225,227,237; 243..254,256,301,302; và 58,66,67,70,97..100,106,108,110,111,190,209..212,220..222,233,239,259,265..271,276..285.
- [CHƯA KIỂM] Giá trị âm, tràn số nguyên và khởi tạo đầy đủ bản gốc `nValue[2]`. `S/KItem.cpp:3756` chỉ sao lưu `nValue[0]` trong `SetBackUpMagicAttrib`; chưa kết luận thiếu khởi tạo ở mọi đường sinh item.

### 5.3 Nhánh trang bị quyết định công thức thực sự

| Trang bị được C++ chấp nhận | Hàm server trong thao tác cường hóa | Kết quả tĩnh ở source hiện tại |
|---|---|---|
| Xanh thường, không Rong/IsWhere | `EnChance` | Công thức mới +5%/cấp |
| Tím | `EnChance` | Công thức mới, nếu thực sự vào được qua đường gọi; Lua gói cũ chỉ nhận nhóm xanh/vàng, nên không coi là UI đã hỗ trợ tím |
| Xanh có Rong hoặc IsWhere | `EnChanceRong` | Công thức cũ cho dòng thường và dòng Rong, lọc ForBitEn |
| GoldId>0 | `EnChanceRong` rồi `EnChanceBao` | Rong vẫn công thức cũ; Bao không làm gì |

Nguồn: `S/KItemList.cpp:5471`, `:5495`, `:5500`, `:5505`; client đồng bộ chọn đúng các nhánh tương ứng tại `C/gamecore/KProtocolProcess.cpp:1642`, `:1650`. Vì vậy tuy báo cáo 63 nói đã sửa “mọi chỉ số”, source hiện tại **không đủ căn cứ áp câu đó cho đồ vàng/xanh luyện hóa**. Cần test từng nhóm, không lấy một kiếm xanh thường đại diện.

### 5.4 Bảng chỉ số theo từng cấp

Bảng tính số học bằng Python -I, không gọi source game, không phải test runtime. Cột “Coco gốc 100” chỉ cho type thuộc allowlist ở nhánh `EnChance`; “cũ gốc 100” chỉ cho type thuộc ForBitEn ở `EnChance` backup/`EnChanceRong`. Hai cột không hàm ý cùng một item đi qua cả hai nhánh. Cấp 6..30 không đạt được qua cấu hình gói cũ trần +5; 16..30 vượt cấu hình test được tài liệu ghi là +15, chỉ mô tả khả năng hàm tính.

| Cấp | Tăng trên gốc của nhánh mới | Coco gốc 100 | Cũ gốc 100 | Coco gốc 70 | Coco gốc 32 | Coco gốc 24 | Bonus kỹ năng vũ khí |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0% | 100 | 100 | 70 | 32 | 24 | 0 |
| 1 | 5% | 105 | 125 | 74 | 34 | 25 | 0 |
| 2 | 10% | 110 | 156 | 77 | 35 | 26 | 0 |
| 3 | 15% | 115 | 196 | 81 | 37 | 28 | 0 |
| 4 | 20% | 120 | 245 | 84 | 38 | 29 | 0 |
| 5 | 25% | 125 | 306 | 88 | 40 | 30 | 0 |
| 6 | 30% | 130 | 382 | 91 | 42 | 31 | 0 |
| 7 | 35% | 135 | 477 | 95 | 43 | 32 | 0 |
| 8 | 40% | 140 | 596 | 98 | 45 | 34 | 0 |
| 9 | 45% | 145 | 745 | 102 | 46 | 35 | 0 |
| 10 | 50% | 150 | 932 | 105 | 48 | 36 | 0 |
| 11 | 55% | 155 | 1165 | 109 | 50 | 37 | 0 |
| 12 | 60% | 160 | 1456 | 112 | 51 | 38 | +1 |
| 13 | 65% | 165 | 1820 | 116 | 53 | 40 | +1 |
| 14 | 70% | 170 | 2276 | 119 | 54 | 41 | +1 |
| 15 | 75% | 175 | 2845 | 123 | 56 | 42 | +2 |
| 16 | 80% | 180 | 3556 | 126 | 58 | 43 | +2 |
| 17 | 85% | 185 | 4445 | 130 | 59 | 44 | +2 |
| 18 | 90% | 190 | 5556 | 133 | 61 | 46 | +2 |
| 19 | 95% | 195 | 6945 | 137 | 62 | 47 | +2 |
| 20 | 100% | 200 | 8681 | 140 | 64 | 48 | +2 |
| 21 | 105% | 205 | 10852 | 144 | 66 | 49 | +2 |
| 22 | 110% | 210 | 13565 | 147 | 67 | 50 | +2 |
| 23 | 115% | 215 | 16956 | 151 | 69 | 52 | +2 |
| 24 | 120% | 220 | 21196 | 154 | 70 | 53 | +2 |
| 25 | 125% | 225 | 26496 | 158 | 72 | 54 | +2 |
| 26 | 130% | 230 | 33120 | 161 | 74 | 55 | +2 |
| 27 | 135% | 235 | 41400 | 165 | 75 | 56 | +2 |
| 28 | 140% | 240 | 51750 | 168 | 77 | 58 | +2 |
| 29 | 145% | 245 | 64688 | 172 | 78 | 59 | +2 |
| 30 | 150% | 250 | 80860 | 175 | 80 | 60 | +2 |

### 5.5 Kỹ năng và mô tả đá

Server `ApplyMagicAttribToNPC` thêm `magic_allskill_v` khi item là vũ khí cận chiến/tầm xa, cấp >=12: +1 ở 12..14, +2 từ 15; `RemoveMagicAttribFromNPC` trừ tương ứng (`S/KItem.cpp:140`, `:184`, `:265`, `:273`). Tooltip VN hiển thị ở `C/vn/gameui/KuiItemdescVN.cpp:465`. Đây là bonus riêng khi áp trang bị, không phải nhân phần trăm các thuộc tính kỹ năng. [CHƯA KIỂM] Cộng dồn, tháo/lắp, cấp kỹ năng vượt bảng và mọi chỉ số kỹ năng thực sự thay đổi trên binary hiện tại.

`EnChanceBao` cả S và C có toàn bộ phần tính nằm trong `/* ... */`, chỉ `return 1` (`S/KItem.cpp:3941`, `:3943`, `:3980`; `C/gamecore/KItem.cpp:3635`, `:3673`). Không được lấy công thức trong comment làm luật đá đang chạy.

`BaoShiGetDesc` là **hàm của KMagicDesc**, không phải hàm tính cường hóa của KItem: đổi `nAttribType` thành khóa và lấy mẫu `[Descript]` trong `g_MagicBaoshiDesc`, thay các placeholder bằng `nValue[0..2]` (`S/KMagicDesc.cpp:647`, `:659`, `:660`, `:684`). File mẫu `G/Settings/BaoShiMagicDesc.ini` được nạp qua `S/KCore.cpp:590`. Đoạn gọi mô tả BaoShi trong `S/KItem.cpp:2911` và `C/gamecore/KItem.cpp:2659` nằm trong block comment kết thúc lần lượt dòng 2922/2670. [CHƯA KIỂM] Các đường UI đá khác; sự có mặt hàm không chứng minh đá được hiển thị hay tăng chỉ số.

## 6. Đối chiếu Coco với gốc và báo cáo 61–67

| Hạng mục | Gốc / bằng chứng được bảo tồn | Coco / mức xác minh hiện có |
|---|---|---|
| Trần thao tác | Gói cấu hình G theo server: +5 | Tài liệu 63/65 ghi +15; runtime [CHƯA KIỂM] |
| Tỷ lệ | Hai số random, không phải 50% từ 1000/2000 | Tài liệu ghi B=1 để test; chưa chứng minh đã hoàn nguyên |
| EnChance | ~25% cộng dồn, ForBitEn, ngưỡng 4 | +5% trên gốc, allowlist rộng hơn, clamp 0..30 |
| EnChanceRong | Công thức cũ | Source hiện tại vẫn công thức cũ; không đồng nhất với EnChance |
| BaoShi | Code tồn tại nhưng phần tính bị comment | Vẫn no-op; không có bằng chứng sửa tăng đá |
| Bonus kỹ năng vũ khí | Patch mới được ghi nhận trong report 63 | Source S có +1/+2 ở +12/+15 và tooltip VN |
| Hiệu ứng | Report 61 thử vòng dưới chân >=10/15/20/25 | Report 62 đổi sang glow vũ khí +6 trắng, +12 vàng, +15 xanh; không phải công thức chỉ số |
| Sét | Report 64: +12 hai tia, +15 bốn tia | Report 65: bốn/sáu tia; report 66 sửa clipping; các báo cáo không chứng minh APK hiện đang dùng |

Nguồn lịch sử: `R/61-hao-quang-cuong-hoa.md:7`; `R/62-kiem-sang-theo-cuong-hoa.md:17`; `R/63-yeu-cau-cuong-hoa-chi-so-ky-nang-set.md:3`; `R/64-hieu-ung-set-vu-khi.md:6`; `R/65-chot-set-vu-khi-va-trang-ky-nang.md:4`; `R/66-sua-set-vuot-ngoai-kiem.md:6`. Report 67, mục 2–4 và 7, phân biệt client baseline với bản ngoài repo và ghi thiếu artifact qh3/qh5/qh6 khi kiểm kê ngày 14/11. Đó là ghi nhận lịch sử; phiên này không kiểm kê APK hay xác minh lại việc thiếu file.

## 7. Đề xuất test TESTER — chưa chạy

Chỉ thực hiện trong phiên kiểm thử được giao riêng, trên bản copy và môi trường được duyệt. H-03 không thực hiện các test dưới đây.

| Mã | Dữ liệu / thao tác cần thử | Kết quả cần đối chiếu |
|---|---|---|
| T01 | Manifest source/binary/config của bản test, file gamesetting theo tham số khởi động | Chốt A,B,Nmax,T thật trước khi diễn giải xác suất; không dùng file generic thay file được nạp |
| T02 | Mỗi tổ hợp đá 403/404/405, ghép sai nhóm, thiếu tiền, thiếu/đủ hai ô, stack nhiều đá | Xác nhận quy tắc nhận đồ, tên/tuple item và số lượng tiêu hao thật |
| T03 | Cấp 0,1,2; cấu hình có thể thất bại, đủ tiền/đá | 0→1,1→2 không roll; từ cấp 2 mới xét roll |
| T04 | Thất bại có kiểm soát tại n=2,T-1,T,Nmax-1; không dùng B=1 để test thất bại | Rớt đúng một cấp dưới T, giữ cấp từ T; giữ trang bị, đá/tiền đúng một lượt |
| T05 | Thử item đạt trần Nmax qua Lua | Xác minh cảnh báo, không mất đá; xác nhận/đánh giá việc vẫn trừ 200.000 theo source |
| T06 | Xanh thường, xanh Rong/IsWhere, vàng, tím; cùng ID thuộc tính và giá trị gốc | Đối chiếu từng nhánh bảng mục 5.3; kiểm tím có vào được UI hay cần API test riêng |
| T07 | Giá trị 70/32/24 tại +0,+1,+12,+15; lên/hạ/lên và đăng nhập lại | Nhánh mới phải khớp 70/32/24 →74/34/25 →112/51/38 →123/56/42, không tăng cộng dồn khi tính lại |
| T08 | Thuộc tính ngoài allowlist, type 59..64 có min/max, giá trị 0/âm/nhỏ, item có nhiều nhóm thuộc tính | Chốt phạm vi tăng thực; phát hiện lỗi khởi tạo max/range hoặc tooltip lệch server |
| T09 | Vũ khí +11/+12/+14/+15, tháo/lắp, hai nguồn bonus, hạ cấp qua mốc | Bonus kỹ năng 0/+1/+1/+2, trừ đúng khi tháo; kiểm chỉ số kỹ năng và giới hạn cấp |
| T10 | Chuỗi đủ dài từ +2, cố định manifest và ghi tổng số thử/thành công/thất bại | Đo xác suất thật cùng khoảng tin cậy; đối chiếu PRNG nối tiếp, không mặc định 25,025% |
| T11 | Đá socket/BaoShi trên các loại trang bị, tooltip VN, đồng bộ sau login | Phân biệt đá tiêu hao nâng cấp với thuộc tính đá socket; xác nhận EnChanceBao no-op có đúng thiết kế |
| T12 | Mốc +5/+6/+11/+12/+14/+15 trên thiết bị mục tiêu | Kiểm glow/sét riêng với chỉ số; không coi ép hiệu ứng render là nâng cấp thật |

## 8. Kiểm tra, lỗi công cụ và bàn giao

- Đã đọc trực tiếp các symbol/đoạn source, cấu hình cường hóa đã lọc, Lua và báo cáo tham chiếu; bảng số liệu là tính toán số học, không phải build/test game. Đã phân biệt code thực thi và code comment.
- `rg` không có trong PATH: lỗi gốc `The term 'rg' is not recognized as the name of a cmdlet, function, script file, or operable program.` Chuyển sang PowerShell/Python đọc trực tiếp; không cài công cụ hay thay PATH.
- Lần đọc prompt đầu bị mojibake vì encoding mặc định; đọc lại UTF-8 để hiểu đúng task. Khi lọc nguồn chứa legacy text chỉ dựa vào symbol ASCII/số; không dùng phần chữ lỗi encoding để khẳng định tên đá.
- Một truy vấn Python dùng regex có chữ Việt qua pipeline PowerShell lỗi `re.error: nothing to repeat at position 26`; thay truy vấn bằng regex ASCII và đọc được tham chiếu 62/64/65/66. Không sửa source và không tạo parser/script phụ.
- Kiểm tra văn bản ban đầu báo `AssertionError` vì đếm cả chuỗi tên mục được trích trong prompt; đổi sang đếm tiêu đề nguyên dòng và đạt đúng một mục kết quả. Đã rà diff một lượt, kiểm tra UTF-8, đủ 5 dòng tóm tắt và tính lại toàn bộ 31 hàng số liệu thành công. `git diff --no-index` trả exit 1 do có khác biệt, không phải lỗi thao tác Git.
- Không có blocker cho khảo sát tĩnh. [CHƯA KIỂM] Cấu hình/binary/APK triển khai, runtime, xác suất PRNG thật, toàn bộ bảng item nguồn/asset và test TESTER. Không chạy build, unit test, integration test, kết nối VM hay mạng vì ngoài phạm vi.
- Commit SHA: không có commit mới; không stage/commit vì task không yêu cầu. Chưa push vì không được yêu cầu và phiên này cấm mạng; không phát sinh lỗi push, không tuyên bố đã công bố lên GitHub.
- Trạng thái cuối **DONE cho phạm vi khảo sát tĩnh**. Bàn giao báo cáo này và mục `## Kết quả` trong task; các phần [CHƯA KIỂM] là giới hạn bằng chứng được ghi rõ, không phải kết quả runtime đạt.
