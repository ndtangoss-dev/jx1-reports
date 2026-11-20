# HỒ SƠ TÍNH NĂNG: CƯỜNG HÓA (nguồn sự thật — Q-99)
Chủ hồ sơ: B (server, bản đồ chuỗi) + A (client, trạng thái kiểm). Chat duyệt.

## (a) Yêu cầu chủ đã chốt
- Q-86: 10 ô 0..9, tối đa +15, +5%/cấp cộng thẳng vào dòng; +14 thêm "+1 tất cả kỹ năng", +15 "+2" (vũ khí); giá n−1→n: thủy tinh min(2^(n−1),1000)/loại, bạc min(2^(n−1)×200 vạn, 20 ức); tỉ lệ 100−5(n−1)%; thất bại giữ cấp, mất vật liệu.
- Q-94: mặc đồ thì dòng thuộc tính (dame/thủ/sinh lực…) THẬT SỰ lên nhân vật; tháo ra mất đúng bấy nhiêu. XONG = số thật trong game.
- Q-95/Q-96/Q-97: chuỗi gốc (UI Give → sysqianghua → QiangHua/EnChance → Equip/Apply); đồ trong túi; đồ đang mặc từ chối; bỏ nút cũ, tạo nút mới.
- Q-91: cửa sổ theo ảnh DESIGN/UI-CUONG-HOA/ (làm SAU khi chuỗi đạt).

## (b) Bản đồ chuỗi gốc (file:dòng, tra Graphify) — phần SERVER do B điền từ bản B-045
ĐÃ TRA ĐỒ THỊ (đồ thị dựng lại cho `QH-B035\...\Core\Src`, 20/11 11:3x): `graphify explain ".QiangHua()"` → KItemList.cpp:L5487; `".Equip()"` → KItemList.cpp:L1619 (gọi `.GetEquipEnhance()` L1821); `".UnEquip()"` → L2155 (gọi `.GetEquipEnhance()` L2189); `"LuaItemQiangHua()"` → ScriptFuns.cpp:L7927; `"LuaGive()"` → ScriptFuns.cpp:L24381; `".ExecuteScriptD()"` → KPlayer.cpp:L8098. Cạnh Lua→C++ không có trong đồ thị nên đọc mã.
Bản đầy đủ + bảng 12 bước: DESIGN/BAN-DO-CHUOI-CUONG-HOA.md. Tóm tắt server:
1. `opensysui(2,1)` (System\opensysui.lua:25) → `Give(mô tả,nÔ,nÔCb,"sysqianghua","sysError",title)` → `LuaGive` ScriptFuns.cpp:24381 → `s2c_opengive` (PLAYER_GIVE).
2. Client `c2s_lockitem` (KProtocolProcess.cpp:323) rồi `c2s_playergiveback` (291) → xử lý xác nhận 9214–9242 → `KPlayer::ExecuteScriptD` KPlayer.cpp:8098 → Lua `sysqianghua(chuỗi id, parm, nNum)` (qianghua.lua:10 gốc; bản mới DESIGN/QH-B044-deploy).
3. Đổi giá trị: `SetItemEnChance` (ScriptFuns.cpp ~10963) → `KItem::EnChance` KItem.cpp:3820 (xanh/tím/vàng đều +5%; vàng gốc dùng `EnChanceRong` 3880 gộp, KHÁC — tiêu chí 7). Gốc `QiangHua` KItemList.cpp:5487 chỉ để đối chiếu, bản mới không gọi.
4. Mặc/tháo: `Equip` 1619 → `ApplyMagicAttribToNPC` KItem.cpp:140 (KItemList.cpp:1547/1852); `UnEquip` 2155 → `RemoveMagicAttribFromNPC` KItem.cpp:275 (KItemList.cpp:2208). Dòng ảo kỹ năng +14/+15 và tài phú: KItem.cpp:184–198 / 283–297.
RỦI RO đã biết cho tiêu chí 5: baseline `m_TempMagicAttrib` chỉ đặt trong `SetAttrib_MA` KItem.cpp:661–669; chưa xác minh sau nạp DB (CHƯA KIỂM). Cho tiêu chí 7: bản Lua dùng `EnChance` cho cả vàng; `EnChance` bỏ qua `m_ronMagicAttrib` (dòng rèn/bảo thạch của vàng) — chưa kiểm vàng có dòng nằm ở đó không.
Client (A điền): nút → __opensysui(2,1) → s2c_opengive → KuiGive_New → c2s_lockitem/c2s_playergiveback.

## (c) Tiêu chí nghiệm thu (đo được)
1. Nút mới mở cửa sổ đặt đồ gốc (ảnh).
2. Đặt 1 món túi nhiều dòng, xác nhận +1: tooltip mỗi dòng = gốc×1,05 (làm tròn như B ghi) (ảnh +0/+1).
3. Mặc món đó: khung nhân vật tăng ĐÚNG bằng các dòng (≥3 chỉ số: sinh lực, sát thương, chính xác/kháng) (ảnh trước/sau).
4. Tháo: về đúng số cũ (ảnh).
5. Thoát/vào lại, +1 tiếp: dòng = gốc×1,10 (không nhân chồng) (ảnh).
6. Món đang mặc: bị từ chối "Hãy tháo trang bị ra rồi cường hóa".
7. Đồ vàng: +1 theo +5% như xanh/tím.
8. Tài phú: mặc món +N thì tài phú nhân vật +100×N; tháo trừ lại.

## (d) Các bước và trạng thái (A cập nhật)
| Bước | Ai | Trạng thái | Bằng chứng |
|---|---|---|---|
| 1 Nạp Lua B-044 (opensysui.lua + qianghua.lua) | A | ĐÃ KIỂM (nạp+SHA khớp; UI Give mở trong game) | docs-analysis/out/ld/q97-ui-giao-goc-sau-nut-moi.png |
| 2 Bộ thử qh_bothu.lua | A | ĐÃ KIỂM 20/11 12:20: tooltip vàng hết đỏ (Thiếu Lâm phái, sức mạnh +260 trắng); chỉ số nhân vật HP 910, nội 100, thể 200 | q97b-giao-moi.png |
| 3 Nút mới + vc27 | A | ĐÃ KIỂM trong game (nút lửa gốc open.spr -> opensysui(2,1) -> UI Giao gốc). APK vc27 SHA256 dad627d5ac1fa0ecba4d7614f5f4087a0c64809b2c735391a1ae0bcae067cdbb (chưa phát chủ) | q97-nut-cuonghoa-moi-man-chinh.png, q97-ui-giao-goc-sau-nut-moi.png |
| 4 Tiêu chí 1–8 | A | TC1 ĐÃ KIỂM. TC2 MỘT PHẦN 12:21: đồ vàng trong túi +0→+1 thành công "tỉ lệ 95%", thủy tinh 3 loại 58→57, bạc 6000→5800 vạn (đúng bảng); nhưng dòng KHÔNG ×1.05: Sinh lực 139→173, Phòng thủ vật lý 28%→36%, Điểm tài phú 0→+100; Né tránh 720 và Nội lực 190 KHÔNG đổi (lỗi cho B). Lời nhắc Giao đã đúng (B). TC3-8 CHƯA KIỂM | q97b-sau-xacnhan-vang.png, q97b-vang-tooltip-+1.png |
| 5 Làm mới đồ thị + bản đồ chuỗi | A,B | CHƯA KIỂM | |
| 6 Cửa sổ theo ảnh chuẩn (Q-91) | A | CHƯA LÀM | |

## (e) Việc kế
A: bước 1→4. B: điền (b), sẵn sàng sửa nếu tiêu chí 5 hoặc 7 hỏng.

## Cập nhật 20/11 (Sonnet A, #297) — TC3 một phần
- ĐÃ KIỂM: mặc giày thường chưa cường hóa (Thảo Ngoa, Né tránh +7): bảng nhân vật Né tránh 55 → 62 (+7 đúng). Ảnh: `q97c-bangnv-truoc-mac.png` (trước), `q97c-bangnv-mac-giay-ne62.png` (sau).
- CHƯA KIỂM (TC3 đủ ≥3 chỉ số, TC4, TC5, TC6, TC7, TC8): đồ vàng cấp bằng hook test `AddGoldItem` bị server từ chối mặc (c2splayerautoequip "换装S", nghi `nCanUse==0`), đồ thường chỉ có 1 chỉ số. Cần món có ≥3 dòng mặc được (cấp bằng Lua, đặt IsCanUse) rồi cường hóa +1 và đo lại.
- ĐÃ TRA ĐỒ THỊ (graphify client+server) / ĐÃ ĐỌC KIẾN THỨC: chuỗi mặc đồ KProtocolProcess.cpp ~L8365–8400, KItemList::CanEquip/EnoughAttrib.

## Cập nhật 20/11 16:46 (Sonnet A, #303/#304/#306) — menu Hỗ trợ thử nghiệm (TEST, nằm trong danh sách gỡ)
- ĐÃ KIỂM: sách Tân thủ (lenhbaitanthu.lua) có mục "[TEST-36] Ho tro Cuong hoa (atest)" → menu: Dọn hành trang, Đồ XANH, Đồ VÀNG, Tiền, Thủy tinh TÍM/LỤC/LAM x600, Thiết lập Thiếu Lâm, Nạp lại Lua nóng. Chạy thật trên atestqhba: Thiết lập (Sinh lực 204→900), Tiền 20 ức, thủy tinh 3 loại 200×3, bộ xanh 10 món, bộ vàng 9/10 (túi đầy 30 ô). Ảnh `ANH-NGHIEM-THU/q306-b3,b5,b6,b7,c1.png`.
- Dòng thuộc tính đồ xanh THẬT (ví dụ Sa Di phục [cấp 1]): Né tránh +50, Nội lực tối đa +107, Chuyển hóa sát thương thành nội lực +7%, Sinh lực tối đa +72, Kháng độc +6%, Phục hồi sinh lực mỗi nửa giây +4 (TEST, luck 1000, ml=6).
- CHƯA KIỂM: mặc bộ xanh/vàng và đo +1/+2/+3, nút Cường hóa mở Give gốc sau thay đổi này.
- Hook TEST cần gỡ: qh_bothu.lua, baowubox.lua, online.lua (Include + QHBV_Book), opensysui.lua (Include), atest_hook.lua, gmroleitem.lua (nhãn V2-NAPNONG + tb_LocalScript, gốc .bak-q306), lenhbaitanthu.lua (Include + mục TEST-36, gốc .bak-q306).
- ĐÃ KIỂM 20/11 16:49 (đồ xanh +0, TC3 nền): mặc Sa Di phục xanh → Sinh lực 900→972 (+72 đúng dòng), Nội lực 100→207 (+107 đúng dòng). Ảnh `ANH-NGHIEM-THU/q306-d1.png`. CHƯA KIỂM: +1/+2/+3 trên món này.

## Cập nhật 20/11 16:54 (Sonnet A, #303/#304) — +1 đồ xanh qua nút Cường hóa gốc (TEST-36)
- ĐÃ KIỂM TC1: nút lửa "Cường hóa" màn chính mở UI Giao gốc (ảnh q306-e5). Đặt đồ: chạm món trong túi → nút "Thêm vào" → Xác nhận.
- ĐÃ KIỂM TC2 (đồ xanh, Hoàng Ngọc Giới Chỉ cấp 1): +0→+1 "tỉ lệ 95%", thủy tinh 200→199 (3 loại), bạc 20 ức→19 ức 9800 vạn (đúng bảng). Dòng ×1,05 làm tròn: Nội lực tối đa 72→76, Sinh lực tối đa 76→80, Sức mạnh +6, Hồi thể lực +7, Kháng độc +3% (phần lẻ làm tròn xuống); Điểm tài phú 0→+100 (TC8 phía món). Ảnh `ANH-NGHIEM-THU/q306-f3-nhan-xanh-+1.png`.
- ĐÃ KIỂM TC3 (≥2 chỉ số): mặc nhẫn +1 → Sinh lực 972→1052 (+80), Nội lực 207→283 (+76), đúng dòng tooltip. Ảnh `q306-f4-mac-nhan-+1.png`.
- CHƯA KIỂM: TC4 (tháo), TC5 (vào lại +1 ×1,10), TC6 (đang mặc bị từ chối), TC7 (vàng), TC8 phía nhân vật (tài phú +100 trên bảng), +2/+3.

## Cập nhật 20/11 16:57 (Sonnet A, #303/#304) — TC4 và TC8 phía nhân vật (TEST-36)
- ĐÃ KIỂM TC4: tháo nhẫn +1 (nút "Tháo" trên tooltip) → Sinh lực 1052→972, Nội lực 283→207, về đúng số cũ. Ảnh `ANH-NGHIEM-THU/q306-g4.png` (tooltip đang mặc: `q306-g3.png`).
- LỖI TC8 (CHƯA ĐẠT, báo B): tooltip món +1 ghi "Điểm tài phú +100" nhưng bảng nhân vật "Điểm tài phú: 0" cả khi mặc (q306-g1, g3) lẫn sau khi mở lại bảng. Chưa rõ bảng client không làm mới hay server không cộng tài phú khi Equip.
- CHƯA KIỂM: TC5, TC6, TC7, +2/+3.

## Cập nhật 20/11 17:00 (Sonnet A, #303/#304) — TC6 qua giao diện
- ĐÃ KIỂM: mặc lại nhẫn +1 (Sinh lực 1052, Nội lực 283). Tooltip món ĐANG MẶC trong bảng nhân vật chỉ có "Tháo"/"Rao", KHÔNG có "Thêm vào" → từ giao diện không thể đặt đồ đang mặc vào cửa sổ Giao (client chặn trước). Ảnh `ANH-NGHIEM-THU/q306-h5.png`.
- CHƯA KIỂM: lời từ chối phía server "Hãy tháo trang bị ra rồi cường hóa" (không có đường UI tới đó; cần gói giả hoặc B kiểm mã sysqianghua).

## Cập nhật 20/11 16:59 (Sonnet A, #303/#304) — +2 đồ xanh, đo mặc (TEST-36)
- ĐÃ KIỂM: nhẫn +1 → +2 qua nút Cường hóa gốc, "tỉ lệ 90%" (bảng 100−5(n−1)) thành công. Thủy tinh 199→197 (đúng 2^1=2/loại), bạc 19 ức 9800 → 19 ức 9400 vạn (−400 vạn = 2×200, đúng bảng). Ảnh `q306-i4.png`.
- ĐÃ KIỂM dòng ×1,10 từ gốc (không nhân chồng): Nội lực tối đa 72→79, Sinh lực tối đa 76→84 (làm tròn gần nhất), Sức mạnh +7, Hồi thể lực +8, Kháng độc +3%, Điểm tài phú +200 (tooltip). Ảnh `q306-i5.png`.
- ĐÃ KIỂM mặc +2: Sinh lực 972→1056 (+84), Nội lực 207→286 (+79) đúng tooltip. Ảnh `q306-i6.png`. Bảng nhân vật "Điểm tài phú" vẫn 0 (xem lỗi TC8 ở trên).
- CHƯA KIỂM: TC5 sau đăng nhập lại (+1 tiếp = ×1,10 không chồng), TC7 vàng, +3 trở lên.

## Cập nhật 20/11 17:01 (Sonnet A, #303/#304) — TC7 đồ vàng một phần (TEST-36)
- ĐÃ KIỂM: nhẫn vàng "Tứ Không Giới Luật Pháp giới" +0→+1 thành công (tỉ lệ 95%): thủy tinh 197→196 (3 loại), bạc 19 ức 9400→9200 vạn (đúng bảng), Điểm tài phú 0→+100 (tooltip). Ảnh `q306-j5.png`, `q306-j6.png`.
- Món vàng này CHỈ có dòng chữ (Kỹ năng Tất cả +1 cấp, tên bộ Tứ Không), không có dòng số để nhân 1,05 → "gold +5% như xanh/tím" CHƯA KIỂM; cần món vàng có dòng số (vũ khí/giáp) và đặt IsCanUse để đo.
- Đẳng cấp yêu cầu +80 nên không mặc được (nhân vật cấp 1).

## Cập nhật 20/11 17:04 (Sonnet A, #303/#304) — TC5 lần 1: MẤT ĐỒ sau đăng nhập lại (tắt cứng app)
- Cách làm: `am force-stop` app LDPlayer (tắt cứng, KHÔNG thoát bằng menu game) → mở lại → đăng nhập atestqhba → vào game.
- KẾT QUẢ: Sinh lực 900/900 (gốc, không còn nhẫn mặc); hành trang chỉ còn 2 vật phẩm (1 "Thương Long Văn Cương - Giáp [Cấp 1]", 1 sách), mất cả 2 nhẫn +1/+2 và thủy tinh. Bạc vẫn 19 ức 9200 vạn. Ảnh `q306-k7.png`.
- Nhận định (CHƯA KIỂM): nhân vật quay về bản lưu cũ vì tắt cứng không kịp lưu (Goddess lưu theo chu kỳ/khi thoát). Chưa đủ chứng cứ để kết luận lỗi của tính năng Cường hóa; cần lặp lại với thoát sạch (menu Cài đặt → thoát về chọn nhân vật) rồi đăng nhập lại.
- TC5 vẫn CHƯA KIỂM.

## Cập nhật 20/11 17:15 (Sonnet A, #303/#304) — +1 THÀNH CÔNG qua UI Give gốc; TC5 lần 2: VẪN MẤT ĐỒ sau thoát SẠCH
- Đính chính lỗi vận hành của thuộc hạ: các lần báo "Ô trang bị trống / Chỉ đặt 1 trang bị" trước đó do thuộc hạ bỏ cả thủy tinh vào ô Giao. Đúng: ô Giao chỉ đặt 1 trang bị; thủy tinh bị trừ thẳng từ hành trang (`sysqianghua`, `qh-b043-qianghua.lua` dòng 24–59). Không phải lỗi tính năng.
- 17:12: nhẫn Hoàng Ngọc Giới Chỉ xanh +0→+1: "Cuong hoa THANH CONG: len +1 (ti le 95%)"; thủy tinh 200→199; bạc 19 ức 9200→9000 vạn. Ảnh `ANH-NGHIEM-THU/q306-o4.png`. (Điểm tài phú vẫn 0 khi mặc nhẫn: lỗi đã báo B.)
- TC5 lần 2: Cài đặt → Đăng xuất (thoát SẠCH, không tắt cứng) → đăng nhập lại → vào game 17:13. KẾT QUẢ: hành trang chỉ còn giáp "Thương Long Văn Cương - Giáp [Cấp 1]" + sách; MẤT nhẫn +1 và toàn bộ thủy tinh. Bạc vẫn 19 ức 9000 vạn (tức bạc đã lưu SAU cường hóa, nhưng vật phẩm thì không). Ảnh `q306-o9.png`, `q306-o10.png`.
- Nhận định (CHƯA KIỂM nguyên nhân): không phải do tắt cứng. Vật phẩm thêm bằng GM (AddItem/ConsumeBagItem) hoặc nhẫn đã SetItemEnChance không được Goddess lưu lại, trong khi bạc được lưu. Cần: so với đồ nhặt/mua thường; thử đồ xanh chưa cường hóa sống qua đăng xuất không; đọc log Goddess lúc đăng xuất.
- Hệ quả: TC5 (đăng nhập lại +1 ×1,10 không cộng dồn) vẫn CHƯA KIỂM; tiêu chí #297 mục 5 chưa đạt.
- Bổ sung 17:16: log Goddess `gw\goddes_log\2026_11_19\07_08_02_060.log` ghi LƯU atestqhba 17:01 = 30 vật phẩm, 17:12:37 (lúc Đăng xuất) = 20 vật phẩm, nhưng sau đăng nhập lại hành trang chỉ hiện 2; bảng nhân vật không mặc gì (ảnh `q306-o11.png`). `online.lua` chỉ gọi QHBV_Book (thêm sách, không xóa). → Lưu có, NẠP LẠI mất: nghi lỗi nạp vật phẩm (đồ AddItem/SetItemEnChance, hoặc giới hạn nạp) — chưa kiểm. Đã thử 2 lần (tắt cứng, thoát sạch); chuyển B/Chat theo luật 3 lần.

## Cập nhật 20/11 17:20 (Sonnet A, #308) — B-051 NẠP NÓNG: "Điểm tài phú" bảng nhân vật = 100 ĐẠT
- Làm: .bak-b051 rồi chép `qianghua.lua` B-051 (SHA ad58b89b… khớp SHA256.txt) vào `gs\script\System`; vá `opensysui.lua` thêm nhánh `inVala==12` (giữ dòng Include qh_bothu của TEST); sửa `qhbv_reload` nạp thêm qianghua.lua + opensysui.lua. KHÔNG restart gs001. Nạp bằng mục "[#306] Nap lai Lua nong" của sách (thông báo "da nap lai qh_bothu.lua, ket qua=4480").
- Đo (TEST-36, atestqhba): nhẫn xanh Hoàng Ngọc Giới Chỉ +0 (Thể lực 6, Sức mạnh 1, Sinh lực 51, Kháng độc 10%, tài phú +0) → +1 (95%): Thể lực 6, Sinh lực 54, Kháng độc 11%, tài phú +100 (ảnh q308-q306-r10.png). Thủy tinh −1 mỗi loại (199), bạc 19 ức 9000→8800 vạn.
- Mặc nhẫn: Sinh lực 900→954, bảng nhân vật "Điểm tài phú: 100" (trước nạp = 0). Ảnh `q308-r11.png`. → TC8 phía nhân vật ĐẠT.
- Không còn cần restart cho Lua. Chưa nạp: `qh_debug.lua` (B-055, không cần vì đã đạt).

## (d) #310 TN1 — 20/11 17:29 (A, LD thật, tkatest03/atestqhba)
- TN1 = đồ XANH từ sách, KHÔNG cường hóa: trước thoát = 12 món trong hành trang (10 xanh + sách + 1 thỏi vàng), ảnh `ANH-NGHIEM-THU/q310-tn1-truoc-12mon.png`. Thoát sạch (Đăng xuất) → đăng nhập lại: còn 2 món (thỏi vàng + sách), ảnh `q310-tn1-sau-2mon.png`. => MẤT 10/10 món xanh dù KHÔNG cường hóa.
- Kết luận: lỗi KHÔNG do cường hóa. Đồ tạo bằng script (AddItem/AddGoldItem) không còn sau relogin; 2 món còn lại (sách, thỏi vàng) là đồ cấp lại lúc đăng nhập (OnLine/QHBV_Book) hoặc đồ có sẵn.
- Chưa làm: TN2 (xanh +1 trong túi), TN3 (đồ thường từ NPC/quái), log Goddess/Bishop theo từng TN, truy mã #311 (KItemSet::AddOther / lưu-nạp Goddess).
- LỆNH CHẠY TIẾP: LD emulator-5556, bấm sách ô 2 (1336,328) → Sử dụng (1231,249) → mục 1 (570,540) → Đồ XANH (950,540); đăng xuất: túi (683,52), đóng (1550,958), cài đặt (1190,52), Đăng xuất (1177,955); đăng nhập: (960,588),(500,297),(840,772),(686,1016).

### (d2) #311 truy mã nạp đồ — 20/11 17:40 (A, kết luận TẠM, chưa kiểm bằng log)
- Đường nạp: `gameserver/Sources/Core/Src/KPlayerDBFuns.cpp` `KPlayer::LoadPlayerItemList` (dòng 818). Mỗi món DB được SINH LẠI từ thông số (dòng 964–1034: item_equip → `ItemGen.Gen_ExistEquipment(detail, particular, series, level, nGeneratorLevel, luck, version, ..., nEnChance, nPoint, nRGeneratorLevel, nRongpiont, nIsWhere)`; đồ vàng → `GetGoldItemByRandom/ByRong`).
- Nếu sinh lại thất bại (`bGetEquiptResult==0`, dòng 1110) hoặc `ItemSet.Add` trả ≤0 (dòng 1112–1115) thì món bị BỎ IM LẶNG (nhánh else dòng ~1127 chỉ ghi log khi `_gameGlobalSet.gameItemInfo.nshowinfo` bật). Đây là ứng viên chính của "mất đồ sau relogin": đồ tạo bằng script AddItem(0,detail,particular,level,series,luck,m1..m6) có thể lưu ra DB thông số mà Gen_ExistEquipment không dựng lại được (vd. mức ma pháp 6×6, nPoint/nEnChance/nIsWhere không khớp).
- Không thấy cờ "GM/tạm" riêng trong đường nạp: các trường nạp = genre/detail/particular/level/series/stack/enchance/point/iswhere/rongpoint/seed/luck/goldid/platina/lock/bang/kuaijie/magic... Cờ khả nghi cần đối chiếu khi LƯU: `nIsWhere` (tham số 16 của AddItem, mặc định 0), `nPoint`, `nEnChance`.
- Bước kế (cần VM, chưa làm): bật `nshowinfo` (gameItemInfo) trên gs test-36 để log "San xuat ... That bai" khi relogin; đọc `gameser_log`/console; so với đồ thường (TN3). Nếu log báo That bai đúng 10 món xanh → sửa tham số tạo trong `qhbv_blue` hoặc Gen_ExistEquipment.

### (d3) TN7 (#311b mục 7) — 20/11 17:34 (A, LD)
- Thủy tinh TÍM x600 (3 chồng ×200, vật liệu chưa cường hóa) cấp từ sách: trước thoát = 5 món (thỏi vàng, sách, 3 chồng tinh thể), ảnh `q310-tn7-truoc-5mon.png`. Thoát sạch → đăng nhập lại: còn 2 món (thỏi vàng + sách), ảnh `q310-tn7-sau-2mon.png`. => MẤT cả vật liệu: lỗi KHÔNG chỉ ở đồ cường hóa/đồ trang bị.
- Tổng hợp: mọi thứ cấp qua menu sách (xanh, tinh thể) đều mất sau relogin; chỉ còn thỏi vàng + sách (sách tự cấp lại lúc đăng nhập). Chưa làm: TN2, TN3 (đồ thường), TN4 (restart gs001 rồi cấp), TN5/6 (nhân vật cũ, thẻ GM gmm). Nghi: nạp lại về trạng thái cũ hoặc dựng lại thất bại hàng loạt (xem d2).

### (d4) #310/#311b — TN6 thẻ GM + đọc log Goddess (A, 20/11 17:40)
- **TN6**: atestqhba, mục "Nhận Thẻ GM" trong sách Tân thủ → "Lệnh bài GM x1" (ảnh `q310-tn6-truoc-3mon.png`: 3 món). Thoát sạch + vào lại → còn 2 món (thỏi vàng + sách), thẻ GM MẤT (`q310-tn6-sau-2mon.png`). Thẻ GM là đồ thường do script cấp, KHÔNG cường hóa → mất.
- **Log Goddess (gw\goddes_log\2026_11_19\07_08_02_060.log, cột cuối = số món đã lưu)**: lúc 17:28:21 lưu **12** món (TN1), 17:33:05 lưu **5** (TN7), 17:36:19 lưu **3** (TN6). Khớp đúng số món trên màn hình TRƯỚC khi thoát. Sau khi vào lại màn hình chỉ có 2.
- **Kết luận tạm (có bằng chứng)**: phía LƯU đúng (Goddess nhận đủ 12/5/3); món mất ở phía NẠP lúc đăng nhập (`LoadPlayerItemList` bỏ món sinh lại thất bại, `KPlayerDBFuns.cpp:1110-1115`) hoặc DB trả thiếu. Chưa phải lỗi cường hóa, chưa phải lỗi riêng đồ xanh.
- **Đối chứng nhân vật cũ (TN5, từ log)**: atestvaihero lưu 31 món ở mọi lần 14:14→15:53 (không giảm sau nhiều lần vào/ra) → đồ do script cấp (AddGoldItem từ hook) GIỮ được ở nhân vật cũ. Chỉ nhân vật mới atestqhba (acc tkatest03) mất. Nghi: khác biệt nhân vật/tài khoản (hoặc chỉ vàng giữ được). CHƯA kiểm TN5 bằng mắt (cần đăng nhập tkatest01/atestvaihero).
- Việc tiếp: TN5 bằng mắt; bật/đọc log nạp (`showItemInfo`) hoặc console gs001 khi vào lại; TN4 (restart gs001).

### (d5) #310b TN4 — restart gs001 rồi cấp đồ xanh KHÔNG nạp nóng (A, 20/11 17:52)
- gs001 restart 17:39:07, nối đủ 5 cổng 17:46:17. atestqhba: sách → Đồ XANH (9/10 món, túi đầy) → 11 món (ảnh `q310-tn4-truoc-11mon.png`). Goddess lưu **11** lúc 17:49:35. Thoát sạch + vào lại → còn **2** món (`q310-tn4-sau-2mon.png`).
- Kết luận: KHÔNG phải do nạp nóng (hot reload) vs script lúc khởi động. Mất đồ lặp lại 4/4 thí nghiệm (xanh, thủy tinh, thẻ GM, xanh sau restart) trên atestqhba; Goddess luôn lưu đủ, phía nạp mất.
- Còn lại: TN5 nhân vật cũ bằng mắt; nguyên nhân nạp (thử đồ do quái rơi/NPC bán TN3).

### (d6) #313 / B-058 — cấp 21 tham số như thẻ gm (20/11 18:58–18:59, A, TEST-36, atestqhba)
- Sửa `qh_bothu.lua`: hàm `qhbv_add` gọi `AddItem(g,d,p,lv,se,lk,l1..l6,st,en,pt,IsWhere=0,y,m,d,h,mi)` (21 tham số theo `gm(开服).lua:1821`, thứ tự 16=IsWhere, 17..21=ngày giờ); dùng cho bộ xanh và thủy tinh. Nạp nóng bằng nút "Nạp lại Lua nóng" (kết quả 4474), không restart.
- Lần 1: ngày = giờ hiện tại (2026-11-20 18:56). Chat báo "bo xanh 9/10", nhưng hành trang KHÔNG hiện món nào (ngày/giờ là mốc hạn dùng → coi như hết hạn ngay). Ảnh `q313-tn1-truoc.png`. Không dùng được.
- Lần 2: ngày = 2030-01-01 (hạn xa). Hiện đủ 9 món xanh (bảo vật khác loại có nền đỏ). Thoát sạch, vào lại: còn 2 món (thỏi vàng + sách). Ảnh `q313-tn1b-truoc/sau.png`. => **VẪN MẤT**, cùng kết quả 15 tham số.
- Kết luận: 15 hay 21 tham số, có/không có hạn dùng, đều không giữ được. Giả thuyết "ngày sinh = 0" (B-058) bị loại cho trường hợp này. Hơn nữa tham số ngày là hạn dùng chứ không phải ngày sinh (`SetTime`, KItemSet.cpp:414).
- Còn lại: khác biệt theo nhân vật (atestqhba cấp 1 mới tạo, mất; atestvaihero cấp 200 giữ 31 món) hoặc cách lưu/nạp theo vị trí; cần TN5 và đọc `KPlayerDBFuns.cpp:818-1115`.
- (d6b, 19:05) Đọc console gs001 để xem dòng "San xuat" lúc nạp (showItemInfo mặc định 1): `console.ps1` báo "attach failed 5" (từ chối truy cập) cả khi chạy qua tác vụ Interactive; 3 lần, dừng theo luật. Cần cách khác (chủ chạy tay trên VM thử hoặc B đọc log qua `gameser_log` bật in file).
- (d6c, 19:10) `JXGive282()` trong online.lua đang tắt (`if 1==1 then return end`), nên thỏi vàng của atestqhba KHÔNG do hook cấp mỗi lần vào: đây là đồ có sẵn từ lúc tạo nhân vật (đã nằm trong DB). Sách là hook cấp lại mỗi lần (QHBV_Book). => Quan sát nhất quán: đồ có từ lúc tạo nhân vật thì nạp được; đồ cấp sau trong lúc chơi (bằng script/thẻ GM) thì Goddess ghi nhận lưu nhưng lúc nạp không ra. Việc cần B xác minh: dữ liệu Goddess lưu cho món cấp sau có khác món lúc tạo (trường vị trí/nLocal, iparamb*, mã món) khiến `LoadPlayerItemList` bỏ không.
- (d6d, 19:20) [CHAT DINH CHINH 19:50: man chon nhan vat ve giap+gay cho MOI nhan vat he Kim, khong chung minh Goddess con do] TN5 xong: đăng nhập tkatest01/atestvaihero (lv200). Màn chọn nhân vật VẼ đủ giáp + gậy (ảnh q313-tn5-chon.png), nhưng vào game: ô trang bị TRỐNG (q313-tn5-trangbi.png), túi chỉ còn thỏi vàng + sách (q313-tn5-tui.png); tiền 1,58 tỷ và sức mạnh 300 còn. => Lỗi KHÔNG riêng nhân vật mới: nhân vật cũ cũng mất toàn bộ đồ khi nạp vào gs001 (Goddess còn dữ liệu đồ, màn chọn vẽ từ đó), chỉ thỏi vàng + sách còn. Mất ở bước gs001 `LoadPlayerItemList` dựng lại đồ, không phải lúc lưu, không phải do cấp bằng script. (Chưa rõ vì sao thỏi vàng sống sót; chưa kiểm.)
- (d6e, 19:35) Log gs001 trên Test-36 (gameser_log/gs001/2026_11_20, Logs/) KHÔNG có dòng lỗi nạp đồ (file gameser_log 0 byte); lỗi chỉ in ra console (showItemInfo). Cần B/chủ bật console hoặc build gs001 có ghi log file cho nhánh bỏ đồ.
- (d6f, 19:40) TN3 chưa làm được qua shop Kỳ Trân Các: nhân vật 0 Xu, mọi món giá ≥1 Xu. Cần NPC bán bạc hoặc nhặt từ quái; chưa làm.

### d7. #315 – Tra gs001.exe ve B-039 (A, 20/11 19:27 gio VM)
- gs001.exe = B-039 (SHA de3d6f0c...058e, khop SHA256-b039.txt); ban B-049 luu `gs001.exe.b049-live`. Restart 19:15, san sang khi gs001 co ESTABLISHED toi 5001/5003/5004/5005/56732.
- Dang nhap atestvaihero (Cap 200, Thieu Lam, SM 300): **trang bi TRONG, tui chi 2 o** (thoi vang + cuon sach cap lai khi dang nhap "Tieu ngao giang ho luc x1"); tien 1 uc 5800 van van con. Anh: q315-b039-tui.png, q315-b039-trangbi.png.
- KET LUAN: B-049 KHONG phai thu pham duy nhat. Chay B-039 van mat do => du lieu do cua nhan vat DA BI GHI DE (luu rong) trong DB tu luc nhan vat nap/luu khi mat do (B-049 hoac truoc do), khong phai do exe nap sai ngay luc nay.
- Vai da kiem: atestvaihero. Khong dang nhap vai nao khac (tkchuvuong chua cham, theo lenh). Khong ket luan duoc cho vai khac; neu vai chua tung dang nhap tren B-049 thi co the con do trong Goddess.
- Giu Lua (sach, B-051); chua can nap lai (sach da co).

### d7b. #316 T1/T2/T3 (A, 20/11 19:30, B-039 dang chay, KHONG bam ReloadScript nao tu luc restart 19:15)
- T1 (vai atestvaihero, gs001 vua restart, chua reload): dung sach -> "Ho tro Thu Nghiem" -> Trang bi xanh -> Non -> Ty Lo Mao -> Kim (duong the GM goc cua game) => tui co 10 non + thoi vang + sach (12 vat pham). Thoat, vao lai => tui chi con 2 o (thoi vang + sach cap lai luc dang nhap); 10 non BIEN MAT. Anh: q316-t1-truoc-relog.png, q316-t1-sau-relog.png.
- T2: khong can (T1 da mat khi chua reload).
- T3: CA HAI MAT => nut ReloadScript/cach nap KHONG phai thu pham; B-049 cung khong (da quay B-039, #315). Mat do xay ra voi duong cap the GM goc.
- BANG CHUNG MOI (Goddess log `gw\goddes_log\2026_11_19\07_08_02_060.log`, dong luu vai): 15:53 atestvaihero cap 200 luu voi so cuoi = 31; 19:29:38 (thoat) luu voi so cuoi = 12 (khop 10 non + thoi vang + sach). => LUU len Goddess THANH CONG; mat do xay ra o buoc NAP (gs001 dung lai vat pham tu DB va bo qua mon loi, `KPlayerDBFuns.cpp:818` ~1040-1125), khong phai o buoc luu. (Chua xac nhan y nghia cua truong cuoi: suy tu so khop, chua doc ma Goddess.)
- Tin hieu phu: thoi vang va sach (6,1,0) song sot sau relog, mon trang bi (genre 0, non/ao/...) mat. File gs doi sau 13:25: online.lua, qh_bothu.lua, baowubox.lua, gmroleitem.lua (16:41), lenhbaitanthu.lua (16:43), qianghua.lua, opensysui.lua (17:17), co dump gs001 luc 16:07 (script\global\npcchucnang\DumpInfo). Chua kiem: Settings\item doi hay khong (loc khong thay file nao sau 13:25).

## d7 #317 (20/11 20:06)
- Nguồn đồ xanh dòng cố định: `goods.txt` MagicLevel1..6 (col 14-19), chỉ đọc khi col 11 > 0 (KBuySell.cpp:129). Đã thêm 10 mon xanh + 3 thủy tinh giá 1 bạc ở Test-36 (hàng 1465-1477, buysell b[93]).
- Kết quả: cửa hàng mở nhưng lưới trống, vì client có bản goods/buysell riêng. Cần SC phía client. Chưa mua thử, chưa relog thử đường Buy. Tiền test: atestvaihero ~158M, đã có menu Tiền.

## d8 #318 (A, 20/11 20:20) — "cai gi da doi" so voi luc con do (last good = 20/11 13:25)
1. Settings\item: KHONG doi gi sau 13:25. File moi nhat la GoldItem.txt/GoldMagic.txt luc 03:47 (B-039pre, truoc moc con do); cac bang khac (armor, helm, boot...) nguyen tu thang 3-7. => Nap do thuc te KHONG phu thuoc thay doi file Settings\item sau 13:25.
2. Lua doi sau 13:25 (gs, mtime): online.lua 16:07, baowubox.lua 16:41, gmroleitem.lua 16:41, lenhbaitanthu.lua 16:43, qianghua.lua + opensysui.lua 17:17; sau do (19:48) goods/buysell/qh_bothu = SAU khi mat do nen khong phai nguyen nhan. Da doc online.lua hien tai: OnLine chi goi JXGive277 (hoc skill), JXGive282 (da `return` ngay dau), QHBV_Book (chi dem sach, del=0), huanyin (skill state). KHONG co dong nao xoa/doi trang bi. Nap do (KPlayerDBFuns.cpp ~1100) chay TRONG engine truoc OnLine nen Lua khong the lam rung do luc nap.
3. nshowinfo: mac dinh = 1 neu khong co key `[Gameconfig] showItemInfo` (KGameglobalSet.cpp:52) nhung tren Test-36 KHONG tim thay file log nao chua "San xuat[" trong 2 gio qua (da quet ca gs) => log khong ra file (gTraceLogFile) hoac key = 0. Day chinh la SC-001. A khong the doc "That bai,Muc" khi chua co log.
4. Chua lam: chia doi Lua ve ban 13:16 (ly do: Lua khong can thiep nap, ton ~7 phut/lan restart gs001). De xuat thay vao do (rẻ nhat, A lam ngay khi B xac nhan): tao nhan vat MOI hoan toan tren Test-36 (B-039), cap do bang menu, relog => neu do giu = loi nam o DU LIEU nhan vat cu (nap ghi de B-049 trong DB) ; neu van mat = loi o gs001/Settings that.

### d9 (A, 20/11 ~21:00, #319 + #320)
**#320 đối chiếu bộ file Test-36 (SHA256 12 ký tự đầu, đo trực tiếp):** gs001.exe DE3D6F0C (=B-039), CoreServer.dll C032F1F7, Engine.dll 0D41AB9D, LuaLibDll.dll 9FFFAB7E; cả 4 file cùng giờ 11-20 07:50 (một bộ liền). Các bản `.bak-b039pre/.bak-b040pre/.bak-b041pre/.bak-b049pre` ở 07:50 trùng bộ hiện chạy.
- Bộ GỐC thật là hậu tố `.orig-a07c` (CoreServer 1893376B 65FEB17E, Engine 1195520B 0252418D, LuaLib 350720B 466A56FE, gs001.exe.orig-a07 543232B DD44D425) — nhỏ hơn hẳn bản tự dựng (CoreServer ~3.28MB). Không có file tên `.goc-qh`; đó là tên trong ghi chú phiên trước, nay tương ứng `.orig-a07c`.
- KẾT LUẬN: exe/DLL KHÔNG đổi từ 07:50, mà đồ còn nguyên lúc 13:25 → lệch bộ exe KHÔNG giải thích việc mất đồ sau 13:25. Phần còn nghi: dữ liệu DB nhân vật bị ghi đè sau B-049/ReloadScript, hoặc cấu trúc nạp đồ. Chưa nạp bộ `.orig-a07c` (bộ gốc không có các sửa B-0xx, bản gốc nhỏ hơn: thử sẽ làm mất toàn bộ sửa; chỉ nên thử khi B/Chat đồng ý) — [CHƯA KIỂM].
**#319 chuỗi Kỳ Trân Các (đọc mã):** nút Bảo Vật (KgameWorld.cpp ~2270, tạo `KuiDynamicShop`) → UI đọc `\settings\Marketshop\type.txt` (cột shopid: 99, 100, 101, 102) → tab = shop id → client lấy hàng từ BuySell CỦA CLIENT (`CoreShell.cpp:127 GetDataDynamicShop`); server `KProtocolProcess.cpp:5948 NpcOpenMarketCommand` chỉ kiểm shopid có trong type.txt rồi đặt `m_BuyInfo.m_nBuyIdx`; mua dùng buysell/goods server. Trên Test-36: shop 99 = b[100] (20 món, hàng 1322–1339…), 100 = b[101] (10 món), 101 = b[102], 102 = b[103] (1 món).
- Muốn thêm món vào Kỳ Trân Các phải sửa CẢ hai: server (nối hàng vào b[100]…) và buysell/goods trong PAK client (cần SC cho B, hoặc cách tạm: thay NỘI DUNG hàng goods.txt của server cho đúng số hàng đã có sẵn ở client — hiển thị tên/hình sai, không khuyến nghị).
