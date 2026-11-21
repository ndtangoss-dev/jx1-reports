# Sổ tay: cửa sổ Cường hóa (client qh9A, vc37/vc38)
Nguồn: `D:\JX-build\qh9A\Classes\vn\gameui\KuiGiveVN.cpp`, `gameui\KuiGive_New.cpp`. Đã thử trên LD (Test-36), 22/11/2026.

## Cấu trúc
- Giao diện vẽ trong `KuiGiveVN::buildQhPanel` (dựng một lần), `refreshQhPanel` (đọc túi đồ, vẽ lưới, bảng 4 dòng, thanh tiền), `qhTick` (chạy mỗi nhịp), `qhTouch` (chạm). Tọa độ tính bằng macro QX/QY, tỉ lệ s = PW/1132.
- Đặt trang bị vào ô giữa: `g_pCoreShell->OperationRequest(GOI_ADDITEM_CLIENT, KUiObjAtContRegion{Obj, Region, UOC_ITEM_TAKE_WITH}, room_give)`. Túi đồ đọc bằng `GetGameData(GDI_ITEM_TAKEN_WITH)`, lưu ở `m_qhBag`.
- Nút Cường Hóa gọi `KuiGive_New::okCallBackFunc` (đường cũ gửi vật phẩm lên server).

## Kết quả từ server
- Server (Lua) gửi `Msg2Player("[QH]|E|...")`, mã: 0 thành công, 1 thất bại, 2 thiếu thủy tinh, 3 thiếu bạc, 4 đã tối đa, 5 không hợp lệ.
- Client không nhận qua `AMessageArrival` mà qua `KuiChatList::addmsg`, nơi đặt `g_qhResultLine/Seq/Tm`; `qhTick` thấy `Seq` đổi thì hiện banner trên đầu cửa sổ.

## Giữ cửa sổ mở (vc37) và giữ trang bị ở ô giữa (vc38)
- Cờ `m_qhKeepOpen` trong `okCallBackFunc`: sau khi gửi, không đóng mà bỏ các ô giữ (`UpdateGiveItem(...,0)`), khiến ô giữa trống.
- vc38: trước khi bỏ ô, lưu tên và vị trí trang bị vào `g_qhWantName/H/V/Seq/Tm`. `qhTick` đợi `m_qhBag` có lại trang bị cùng tên (ưu tiên cùng vị trí), rồi đặt lại bằng GOI_ADDITEM_CLIENT; hết 20 giây thì bỏ. Kết quả: dù thành công hay thất bại, trang bị ở lại ô giữa và bảng hiện cấp kế (+N → +N+1).
- Không cần sửa server/Lua.

## Bẫy đã gặp
- Chữ tiền trái phải cỡ nhỏ hơn (19 thay vì 24) khi chuỗi dài hơn 12 ký tự, nếu không đè icon xu.
- Thứ tự túi đồ đổi sau mỗi lần cường hóa (đồ bị bỏ ra rồi đặt lại): kiểm ảnh trước khi chạm theo tọa độ.
