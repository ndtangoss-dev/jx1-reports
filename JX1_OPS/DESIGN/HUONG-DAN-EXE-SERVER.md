# HƯỚNG DẪN DÙNG CÁC EXE SERVER (bản 1, Chat viết 18/11/2026 16:40)

Nguồn: 5 ảnh `ANH/exe-server/` (JX-Test-36, Sonnet chụp, không bấm gì) + `DESIGN/TRUYEN-TAI-VA-EXE-SERVER.md`.
Nhãn: [THẤY] = đọc trên ảnh; [TÀI LIỆU] = từ tài liệu U-02; [CHƯA KIỂM] = đoán từ tên nút, CHƯA có ai bấm thử. Chưa nút nào được thử, nên chưa có gì ở đây được coi là xác minh chạy thật.

## 0. Quy tắc sắt (theo AGENTS.md)
- Chỉ làm trên VM thử JX-Test-36. Main VM / máy chính là vùng Đỏ, không đụng.
- Mỗi exe server và mỗi thao tác đổi trạng thái cần chủ duyệt riêng. Hộp thoại lạ: dừng, hỏi.
- Trước khi đổi gì: sao lưu (copy thư mục cấu hình/dữ liệu bản sao; không tự chụp snapshot VM). Mỗi lần chỉ đổi MỘT thứ; ghi giá trị trước, sau, giờ.
- Không bấm: Exit (Bishop), Remove Role, Copy DB to MySQL / Copy MySQL to DB, Restart, Pause (Goddess), khi chưa được duyệt.

## 1. Bức tranh: 5 chương trình, vai trò
| Exe | Việc | Nhìn/chỉnh được gì |
|---|---|---|
| PaySys | tài khoản, hạn chơi [TÀI LIỆU] | chỉ có nhật ký nhịp "Gateway … Ping 10(s)" [THẤY]; không có nút nghiệp vụ |
| Goddess | kho dữ liệu nhân vật (cổng 5001) | cửa sổ quản trị nhiều nhất (mục 2) |
| S3Relay | chat, bang, bạn bè, chuyển GS | chỉ nhật ký "update friend DB succeed" [THẤY] |
| Bishop | cổng đăng nhập, chọn GS, thông báo, lọc IP/tài khoản | cửa sổ điều khiển chính (mục 3) |
| gs001 | thế giới game | cửa sổ đen chỉ ĐỌC (mục 4). Chỉnh game không làm trong cửa sổ này |

Thứ tự bật từng dùng: SQL → PaySys → Goddess → S3Relay → Bishop → gs001 [TÀI LIỆU]. Thứ tự tắt: [CHƯA KIỂM, GIẢ THUYẾT hợp lý] ngược lại, gs001 trước để nó lưu nhân vật qua Goddess, Goddess sau cùng.

## 2. Goddess (kho nhân vật)
- Đầu cửa sổ [THẤY]: `Open port 5001`, nút `Start` (đang xám vì đang chạy), danh sách GS nối vào (192.168.56.150:50674/50677/50722).
- Khung "Thiết lập (hoạt động sau khi tắt máy chủ)" [THẤY]: `Max char create` = 3 (số nhân vật tối đa mỗi tài khoản), `Backup time` = 3, `MAX Player` = 500, chọn `Data type` DB hoặc SQL, nút `Set up database`, `<<Copy DB to MySQL>>`, `<<Copy MySQL to DB>>`, `Pause`, `Manual backup`, `Save nhat ky`, `Restart`. Ô đang xám vì đang chạy: nghĩa là phải TẮT Goddess rồi mới đổi. Ý nghĩa từng ô [CHƯA KIỂM].
- Khung "Thao tác (nhân vật offline – nạp tiền)" [THẤY]: chọn `Vang`/`Bac`, `Check online`, ô `Role`, ô `Money`, nút `Add Money`; `Nhan vat level` + nút `Remove Role`. Dùng cho nhân vật đang OFFLINE. [CHƯA KIỂM] Add Money cộng vàng/bạc cho nhân vật tên Role. Remove Role XÓA nhân vật: rủi ro cao.
- Khung "Thao tác Database (khi máy chủ GS tắt hoặc hoạt động…)" và "Một vùng (khi GS tắt, hay vận hành…)" [THẤY] gồm nhiều ô số + nút `????`, `EnterMap`/`IDMap`/`Bat dau`: nhãn tiếng Việt cắt dở, nhãn Trung bị lỗi mã (hiện `??`). [CHƯA KIỂM] Cần Sonnet đọc bằng bảng mã GBK trước khi dùng.
- Dưới cùng: `Account`, `Nhan vat`, các hộp `Body`, `Me chong`, `Kho`, `Box1–3`, `All`, nút `Backup` [THẤY]. [CHƯA KIỂM] sao lưu riêng từng nhân vật/phần túi đồ: dùng làm bảo hiểm trước khi sửa nhân vật.

## 3. Bishop (cổng đăng nhập + thông báo)
- Tab `Status` [THẤY]: IP/cổng PaySys 192.168.56.150:5002, Goddess 192.168.56.150:5001, `Client Port 56722`, `game Server Port 56732`; ô số: `Reset character rebirth m` = 53, `Send to client to detect ve` = 50.50, `Whether to enable limiting th` = 3; hộp `all IPs are prohibited…`; nút `Startup`, `Update`, `connect`, `save setting`. Tab `Information` CHƯA chụp.
- Khung `Announcer` [THẤY]: 3 kiểu lệnh: "Notify all player" (thông báo toàn server), "Notify game server to close safely *" (báo GS tắt an toàn), "Notify and warning all player to quit this game *" (đuổi người chơi thoát); ô nhập tối đa 260 ký tự; nút `Send`. Dấu * = kiểu mạnh, chỉ dùng khi đã duyệt. [CHƯA KIỂM] kiểu 1 là cách thử an toàn đầu tiên.
- Các danh sách bên phải [THẤY]: `GameServer Information` (hai GS), `Unrestricted`, `VIP account, no restrictions`, `Client IP information` + `Add to filter list`, `Filter account list`, `Filter IP list`, `Limit IP multiple opening`. [CHƯA KIỂM] dùng để chặn/cho phép IP và tài khoản.
- Dưới cùng [THẤY]: `Birth role setting`, `Cap`, `Silver`, `gold`, `other`, `Exit`. [CHƯA KIỂM] cấp độ + tiền của nhân vật mới tạo. `Exit` TẮT Bishop: không bấm.
- Khung `Information output` [THẤY]: nhật ký. Có dòng nạp `maps\WorldSet_gs001.ini` rồi `Ban Do loaded(0:1)… ok`: cho thấy bản đồ do gs001 nạp từ tệp ini, tức chỉnh nội dung game nằm ở TỆP cấu hình/dữ liệu, không ở cửa sổ này.

## 4. gs001 (chỉ đọc)
Mỗi phút một dòng [THẤY]: `NetCount`, `GameLoop`, `SvrFPS= 18/18` (khỏe), `tick avg=~550us max=…`, `over=` (số lần tick quá hạn; thấy một lần over=1, max=88950us lúc 16:05), `Online= 0`. Dùng làm đồng hồ sức khỏe và đo tốc độ (khu 6 Xưởng). Không có nút.

## 5. "Chỉnh server" nằm ở đâu (đừng nhầm)
| Muốn | Chỗ làm | Mức chắc |
|---|---|---|
| Thông báo cho người chơi, chặn IP/tài khoản, cổng, giá trị khởi đầu nhân vật mới | Bishop | CHƯA KIỂM |
| Số nhân vật/tài khoản, số người tối đa, sao lưu, cộng tiền offline, xóa nhân vật | Goddess (tắt trước khi đổi ô thiết lập) | CHƯA KIỂM |
| Bản đồ, quái, vật phẩm, kỹ năng, giá | TỆP dữ liệu/ini của server + bảng K-03 (không phải cửa sổ exe); sửa trên bản sao | tài liệu, chưa thử |
| Đổi cấu trúc/tốc độ tick, gói tin | mã nguồn C++ (Xưởng khu Sửa sâu, M5) | chưa làm |

## 6. Cách thử an toàn (thứ tự đề xuất, mỗi bước chủ duyệt)
1. Chỉ đọc: chụp nốt tab `Information`; giải mã nhãn `??` của Goddess bằng GBK.
2. Bishop → `Announcer` → "Notify all player" gửi 1 câu thử (ảnh hưởng thấp), xem Online/nhật ký.
3. Sao lưu Goddess (Manual backup), kiểm có tệp sinh ra.
4. Đổi một ô thấp rủi ro (vd Max char create 3→4 trên bản sao, tắt/bật Goddess), thử tạo nhân vật, ghi trước/sau, hoàn tác.
5. Chỉ sau đó mới tính tới Add Money (nhân vật test) rồi các nút mạnh.
Mỗi nút đã thử được ghi vào bảng `DESIGN/BANG-NUT-EXE-SERVER.md` (nút | tác dụng thật | rủi ro | cách hoàn tác | ngày thử).
