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
