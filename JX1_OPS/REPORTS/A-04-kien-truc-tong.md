# A-04 – Kiến trúc tổng (gộp A-01…A-03, A-05…A-07, JIBS)

**TÓM TẮT**
1. Chuỗi bắt buộc: SQL Server → `Sword3PaySys` (5002) → `Goddess` (5001) → `S3Relay` (5003-5005, 7776) → `Bishop` (56722 client, 56732 game server) → `gs001` (51189). Chi tiết: `A-01-ban-do-tien-trinh.md`.
2. Đăng nhập: client → Bishop → PaySys (tài khoản, cần `Account_Info` + `Account_Habitus` còn hạn) / Goddess (nhân vật, `roledb` Berkeley DB) → client nối gs001 bằng GUID. Chi tiết: `A-02`.
3. gs001: 500 người cứng, 1 luồng, 18 Hz; cấu hình đọc ở `KSOServer.cpp`, `KCore.cpp`; cây nguồn không chứa INI/Lua/TAB, nên mọi nội dung runtime là CHƯA KIỂM (`A-03`).
4. Hiển thị/tương tác: lọc theo ô bản đồ (`KRegion::BroadCast`), không theo bán kính; còn nhiều đường gửi khác (`A-05`). Giao thức client↔server có chỗ lệch (`A-06`).
5. Mọi thứ trong tài liệu này là KIỂM TRA TĨNH hoặc tổng hợp từ báo cáo cũ; chưa có kết luận runtime nào mới. Crash gs001 tự dựng chưa tìm ra dòng gây lỗi (`A-07`).

## Nhãn tin cậy
- **[ĐÃ KIỂM VẬN HÀNH]** chạy thật trên Main VM trước đây (BAI_HOC, báo cáo cũ): chuỗi khởi động, cổng, thứ tự.
- **[NGUỒN]** đọc mã, chưa kiểm exe đang chạy có cùng hành vi (nguồn mới hơn exe).
- **[CHƯA KIỂM]** chưa chạy, chưa đo.

## 1. Tiến trình và cổng [ĐÃ KIỂM VẬN HÀNH, lại kiểm cổng trên VM thử 16/11 23:48]
| Tiến trình | Cổng | Vai trò |
|---|---|---|
| SQL Server | 1433 | DB `account`, nội bộ VM |
| Sword3PaySys | 5002 | tài khoản |
| Goddess | 5001 | lưu nhân vật (cần bấm Start) |
| S3Relay | 5003, 5004, 5005, 7776 | transfer, chat, bang hội/bạn bè |
| Bishop | 56722, 56732 | cổng vào cho client / cho game server |
| gs001 | 51189 | game server, nạp ~7 phút; không mở kết nối khi đang nạp |
Cổng 7777 không có tiến trình nghe, ảnh hưởng chưa rõ [CHƯA KIỂM].

## 2. Luồng đăng nhập và dữ liệu [NGUỒN]
Khung gói: 2 byte độ dài, XOR khóa cuộn từ `ACCOUNT_BEGIN` (đã cài đặt và test offline ở E-01). `roledb` là B-tree, khóa là tên nhân vật; sao lưu tích hợp ghi dump theo cặp khóa/dữ liệu. Cờ `is_bot` đề xuất lưu ở bảng metadata SQL theo `cAccName` (A-02), chưa triển khai.

## 3. Cấu hình và script [NGUỒN]
Tên sinh từ tham số GS: `%s_cfg.ini`, `gamesetting_%s.ini`, `WorldSet_%s.ini`. Cây `jxOnline` có 5226 file nhưng 0 INI/Lua/TAB/PAK; cấu hình thật nằm ở bản chạy `_bin_v2_` (D-01 đã quét: 27 hoạt động, 0 có script đầy đủ; `servertimer.lua:125` thiếu dấu nháy đóng). 28 bản đồ không nạp được vì thiếu `.wor`.

## 4. Giao thức [NGUỒN]
Gateway lệch mã c2s từ 185; client thiếu 3 relay + 4 chat; 18 struct dùng chung khác khai báo; bảng độ dài client đặt nhầm một mục (A-06). A-06 ghi nhầm gói sync (enum 67) là mốc không payload, E-01 đã đính chính. Bot thiếu các record đồng bộ thế giới để vào game trọn vẹn (E-01).

## 5. Hiển thị và tương tác [NGUỒN]
`KRegion::BroadCast` (`KRegion.cpp:2223`), tối đa 100 người/ô, lọc khoảng cách bị comment. Đường gửi khác: `KNpc.cpp:7718, 7822, 14993-15030`, `KSubWorld.cpp:2366`, `KObj.cpp:1468-1621`. Điểm chèn lọc xếp theo rủi ro ở `A-05`.

## 6. Dựng lại và crash [NGUỒN, CHƯA KIỂM RUNTIME]
Exe gốc và bản tự dựng đều x64 (linker 10.00 / 14.44). Nghi vấn: `KSOServer.cpp:960`, `:4966`, `KSortScript.cpp:328`. Chưa có dump; thiếu `cdb.exe` ở host và VM. Câu hỏi "server tự dựng 36 Hz" của báo cáo 45 CHƯA TRẢ LỜI.

## Chưa kiểm (tổng)
Số online thật chịu được; nguồn có khớp exe đang chạy không; tạo hàng loạt tài khoản/nhân vật; cổng 7777; mọi hành vi Bot trên server thật.
