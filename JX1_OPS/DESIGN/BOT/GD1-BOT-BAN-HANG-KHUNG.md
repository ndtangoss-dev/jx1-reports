# GĐ1 — Bot bán hàng (hướng A, ngoài server qua giao thức): bằng chứng nguồn và khung (Sonnet 19/11/2026)

**Nhãn:** [NGUỒN] đọc từ mã nguồn; [CHƯA KIỂM] chưa chạy trên exe thật (nguồn có thể lệch exe, xem E-01).

## Điều thấy trong nguồn
- [NGUỒN] Gian hàng người chơi ("bãi tan") có thật: cờ `Npc.m_BaiTan`, tên gian hàng lưu bằng `SetstrInfo(STR_SHOP_NAME, ...)`. Bật tại `gameserver/Sources/Core/Src/KPlayer.cpp:12264` khi nhận `PLAYER_START_TRADE` với `m_bSet != 0` **và** `GetTradeCount() > 0` (phải có món trong ô bán); trước đó gọi Lua `PermitTrade` (khoảng dòng 12240–12255), trả 0 thì không bày được.
- [NGUỒN] Người mua gửi `c2s_playertradebuyitem` (định nghĩa `gameserver/Headers/KProtocolDef.h:333`), cấu trúc `PLAYER_TRADE_BUY_ITEM_COMMAND` (`Headers/KProtocol.h:3535-3547`: `m_Idx` id món, `m_PlayerId` id người bán, `m_Place/X/Y`, `m_MapID`...). Xử lý ở `KProtocolProcess.cpp:8834` (`c2sTradeBuy`): người bán phải còn trong tầm nhìn (`FindAroundPlayer`) và `m_BaiTan` bật, món còn tồn tại.
- [NGUỒN] Bày bán mở bằng `c2s_playerstarttrade` (`KProtocolDef.h:331`, handler `StartTrade` `KProtocolProcess.cpp:8005`); `c2s_tradeapplystateopen/close` (`KProtocolDef.h:299`) là giao dịch trực tiếp hai người (khác).
- Mua ở shop NPC dùng `c2s_playerbuyitem` (`KProtocolProcess.cpp:5743`), không phải đường này.

## Khung Bot bán hàng (hướng A)
1. Vào game như Bot hiện có (E-01), đứng một chỗ ở thành (vd Ba Lăng Huyện).
2. Đưa món vào ô bán (giao thức di chuyển vật phẩm vào phòng giao dịch: **CHƯA KIỂM**, cần dò gói).
3. Gửi `c2s_playerstarttrade` với `m_bSet=1`, tên gian hàng; chờ s2c xác nhận.
4. Giá và danh mục lấy từ `STATE/BOT/gia-vat-pham.csv` (`gia_san_mac_ca` là sàn); cổng duyệt giá theo thiết kế v1.
5. Chỉ hành động trong Test-36; không đụng tiền thật; mọi gói qua `BOT/packets.py` (đã có khung kiểm tra biên).

## Chặn/chưa làm (không bịa)
- Số nguyên của các ID `c2s_playerstarttrade` / `c2s_playertradebuyitem` phải đếm từ enum `KProtocolDef.h` và đối chiếu bằng gói thật từ client (cần bắt gói LD bày bán): [CHƯA KIỂM]. Bố cục byte `PLAYER_START_TRADE` chưa đọc (cấu trúc ở Headers); exe thật có thể khác nguồn (bảng E-01).
- Cần nhân vật Bot có vật phẩm (tạo bằng SQL/Lua trên Test-36) và qua `PermitTrade`.
- Bước kế đề xuất: client LD bày một gian hàng, bắt gói trên forwarder, so với `PLAYER_START_TRADE`; rồi mới viết `packets.start_stall()` + test đơn vị.
