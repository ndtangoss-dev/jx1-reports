# Thiết kế UI cửa sổ cường hóa (Q-91) — bản soạn của A, 21/11, CHƯA BUILD, CHƯA NẠP
Nguồn: DESIGN/UI-CUONG-HOA/MO-TA.md + 3 ảnh chuẩn; client `gameui/KuiGive_New.cpp` (1529 dòng); Lua `gs\script\System\qianghua.lua`. Điều kiện: chỉ làm khi chủ chốt cường hóa (thư #339), LD đang là của chủ.

## 1. Bố cục (theo ảnh chuẩn, dùng asset gốc)
- Tiêu đề "Cường hóa trang bị"; dải gợi ý "Đặt vào trang bị muốn cường hóa".
- Sơ đồ 5 ô quanh ô giữa "Trang Bị": trên + 2 dưới = "Nguyên Liệu" (xanh lá / xanh dương / tím); trái = "Bùa Bảo Hộ", phải = "Phù May Mắn" (giai đoạn 1 vẽ nhưng KHÓA, tooltip "chưa mở"; Q-91 điểm 1). Mũi tên từ ô nguyên liệu vào ô giữa.
- Dòng thông tin: "Nguyên liệu cần: N mỗi loại Thủy Tinh", "Cần Bạc X / Tỉ lệ Y%", dòng chú ý đỏ-cam.
- Phải: lưới túi 5 cột, hai thanh tiền (vàng, bạc theo Ức/Vạn), nút "Cường hóa" và nút đóng. Cửa sổ không được chồng lên túi (lỗi quan sát trên LD: kéo/vuốt làm túi dịch chồng panel Giao).
## 2. Hành vi (khớp luật server, không đổi công thức Q-86)
- Ô giữa CHỈ nhận trang bị (kind==0, xanh/tím/vàng). Chạm món trong túi → nút "Thêm vào" như cũ.
- THỦY TINH KHÔNG đặt vào ô Giao: server tự trừ 1 loại mỗi màu (c theo `qh_price`) từ TÚI. Dòng nhắc cố định: "Thủy tinh tự trừ từ túi, không cần đặt vào". Lý do: chủ đã thất bại lần đầu vì đặt đồ cùng thủy tinh vào ô Giao (lúc đó Lua đếm cnt~=1 → code 5).
- Nút "Cường hóa" xác nhận (c2s_playergiveback nKind=3 như cũ). Kết quả hiện ngay trong cửa sổ (dòng trạng thái) thay vì chỉ ở khung chat.
- Đồ đang mặc: không vào được (đường chuẩn gốc, thông báo "Hãy tháo trang bị ra rồi cường hóa").
## 3. Sửa thông báo code 2/3 in nhầm (bằng chứng LD 21/11 09:31)
- Triệu chứng: "Thiếu thủy tinh: cần mỗi loại 2000000" — 2000000 là số BẠC, số thủy tinh thật là 1.
- Nguyên nhân: Lua `qianghua.lua` dòng 55/56 gửi `[QH]|E|code|lv|rate|c|s|0|wealth` (không có ô "0" sau code) còn nhánh 0/1 gửi `code|0|lv|rate|c2|s2|wealth`. Client (`KgameWorldVN.cpp` ~3473-3480, `KuiChatList.cpp` ~345) đọc theo bố cục sau: case 2 lấy f[5], case 3 lấy f[6] qua `money()`. Với bố cục dòng 55/56, f[5]=s (bạc) và f[6]=0 → code 2 in số bạc, code 3 in "cần 0 bạc".
- Sửa nhỏ nhất (chỉ Lua, không build client): [CẬP NHẬT B080, 21/11] bản B080 đã sửa bằng cách gửi `c|c` ở dòng 55 (không dùng `|0`); đã nạp lên Test-36. Bản cũ ghi: thêm `"|0"` sau mã ở dòng 55 và 56 (các mã 3,4,5 kiểm lại cùng bố cục: 4 và 5 không dùng c/s nên không ảnh hưởng). Sau sửa: f2=0,f3=lv,f4=rate,f5=c,f6=s đúng cho mọi mã. CHƯA áp dụng (LD của chủ đang thử, không restart gs).
## 4. Việc đo cần làm sau khi build UI (đo thật, ảnh LD vào docs-analysis/out/ld/)
(1) mở cửa sổ rỗng khớp ảnh chuẩn 2; (2) đặt trang bị khớp ảnh 1; (3) cường hóa 0→1 thành công, tooltip dòng đổi; (4) thiếu 1 loại thủy tinh → thông báo đúng số 1 (không phải 2000000); (5) thiếu bạc → "cần 2.000.000 bạc"; (6) đồ đang mặc bị từ chối; (7) tài phú BẬT hiển thị đúng sau mỗi lần.
## 5. Chưa kiểm / mở
- Bố cục ô, tọa độ, asset: chưa đọc KuiGive_New.cpp kỹ, chưa có ảnh render. Ước tính việc: client ~1 ngày build+LD sau khi chủ chốt.
- Đồ trắng: chủ bỏ (#339), dòng 44 giữ nguyên.

## 6. Kết quả build vc35 (A, 21/11 17:25)
- GỐC lỗi "nhãn không hiện" vc33/vc34: bản VN dùng lớp `vn/gameui/KuiGiveVN` (kế thừa `KuiGive_New`, ghi đè `addDialogData`), không phải `KuiGive_New::addDialogData`. Sửa đặt nhãn nhắc + dòng kết quả vào `KuiGiveVN::addDialogData` (vc35).
- ĐÃ CHỤP (EVIDENCE/ui-cuonghoa): a (cửa sổ rỗng, có dòng cam nhắc "Thủy tinh tự trừ từ túi"), b (đã đặt đồ, bảng tỉ lệ/bạc/thủy tinh hiện), f0 (đồ trắng bị từ chối, thông báo đúng).
- CHƯA KIỂM: c (cường hóa 0→1 thành công), d (thiếu 1 loại thủy tinh), e (thiếu bạc), f (đồ đang mặc). Lý do: túi thử chỉ có đồ trắng hoặc +15; cần 1 món xanh/tím/vàng +0.
- Nghi vấn: bảng cho đồ +15 hiện "Cần bạc: 6553600 vạn", đơn vị "vạn" có thể sai; dòng kết quả (m_qhResult) chưa thấy vì chưa có cường hóa hợp lệ; tiêu đề cửa sổ vẫn là "Giao" (sprite).

### §6b — Ảnh c–f: KẸT, CHƯA KIỂM (21/11)
Cần món xanh/tím/vàng +0 trong túi. Menu "Bảo vật" (qh_bothu.lua) chỉ mở cho vai tên bắt đầu `atest` (vai atestqhhai, tk tkatest02); mật khẩu tk đó không có trong kho/biến môi trường của A, T36nv1 không qua được cổng tên. Đã thử 3 hướng (tìm công cụ cấp đồ, tìm mật khẩu, quy ước bot_tao_role), đều không ra. Còn CHƯA KIỂM: c (0→1 thành công), d (thiếu 1 loại thủy tinh), e (thiếu bạc), f (đồ đang mặc), đơn vị "vạn", dòng kết quả m_qhResult. Cách gỡ: chủ cấp mật khẩu tkatest02 qua biến môi trường, hoặc nới cổng tên sang `T36` (restart gs001 ~10 phút).

### §6c — vc37 (A, 21/11 22:58)
Giao diện theo atlas mới (JX1_CuongHoa_UI_Atlas.png); cửa sổ giữ mở sau khi Cường hóa (đóng rồi mở lại cửa sổ để làm mới đồ); kết quả lấy từ KuiChatList::addmsg (g_qhResultLine). Ảnh a,b,c,d,f,HUD có; e (thiếu bạc) chưa chụp.
