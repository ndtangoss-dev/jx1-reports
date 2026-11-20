# HỒ SƠ TÍNH NĂNG: CƯỜNG HÓA (nguồn sự thật — Q-99)
Chủ hồ sơ: B (server, bản đồ chuỗi) + A (client, trạng thái kiểm). Chat duyệt.

## (a) Yêu cầu chủ đã chốt
- Q-86: 10 ô 0..9, tối đa +15, +5%/cấp cộng thẳng vào dòng; +14 thêm "+1 tất cả kỹ năng", +15 "+2" (vũ khí); giá n−1→n: thủy tinh min(2^(n−1),1000)/loại, bạc min(2^(n−1)×200 vạn, 20 ức); tỉ lệ 100−5(n−1)%; thất bại giữ cấp, mất vật liệu.
- Q-94: mặc đồ thì dòng thuộc tính (dame/thủ/sinh lực…) THẬT SỰ lên nhân vật; tháo ra mất đúng bấy nhiêu. XONG = số thật trong game.
- Q-95/Q-96/Q-97: chuỗi gốc (UI Give → sysqianghua → QiangHua/EnChance → Equip/Apply); đồ trong túi; đồ đang mặc từ chối; bỏ nút cũ, tạo nút mới.
- Q-91: cửa sổ theo ảnh DESIGN/UI-CUONG-HOA/ (làm SAU khi chuỗi đạt).

## (b) Bản đồ chuỗi gốc (file:dòng, tra Graphify) — B điền/duyệt lại từ bản B-045
(B chép phần server; A chép phần client: nút → __opensysui(2,1) → s2c_opengive → KuiGive_New → c2s_lockitem/c2s_playergiveback)

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
| 2 Bộ thử qh_bothu.lua | A | MỘT PHẦN: cấp đồ vàng ĐÃ KIỂM; môn phái/sức mạnh CHƯA áp (tooltip côn đỏ) | q97-tooltip-con-vang-+0-yeu-cau-do.png |
| 3 Nút mới + vc27 | A | ĐÃ KIỂM trong game (nút lửa gốc open.spr -> opensysui(2,1) -> UI Giao gốc). APK vc27 SHA256 dad627d5ac1fa0ecba4d7614f5f4087a0c64809b2c735391a1ae0bcae067cdbb (chưa phát chủ) | q97-nut-cuonghoa-moi-man-chinh.png, q97-ui-giao-goc-sau-nut-moi.png |
| 4 Tiêu chí 1–8 | A | TC1 ĐÃ KIỂM; TC2: Xác nhận -> sysError (côn đơn và côn+đá lục), đang tra; TC3-8 CHƯA KIỂM | q97-giao-xac-nhan-thieu-da-thong-bao-sysError.png |
| 5 Làm mới đồ thị + bản đồ chuỗi | A,B | CHƯA KIỂM | |
| 6 Cửa sổ theo ảnh chuẩn (Q-91) | A | CHƯA LÀM | |

## (e) Việc kế
A: bước 1→4. B: điền (b), sẵn sàng sửa nếu tiêu chí 5 hoặc 7 hỏng.
