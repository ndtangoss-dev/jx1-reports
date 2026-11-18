# XƯỞNG JX1 — thiết kế bản 1 (18/11/2026, theo thư #144)

## 1. Mục tiêu
Người không lập trình hiểu, chỉnh, build, vận hành và quản lý lỗi game JX1 bằng giao diện tiếng Việt. Mọi sửa đổi game chỉ áp lên bản sao và VM thử; VM chính, CSDL thật, keystore là vùng Đỏ.

## 2. Kiến trúc
- Một tiến trình Python (thư viện chuẩn), `http.server` nghe CỐ ĐỊNH `127.0.0.1` (cổng 8770, đổi bằng `XUONG_PORT`), chặn Host lạ, đăng nhập bằng mã (cookie HttpOnly, SameSite=Strict). Mã: biến `XUONG_CODE` hoặc `D:\JX-xuong\ma.txt` (tạo ngẫu nhiên, không vào kho).
- Mã nằm ở `TOOLS/xuong/` trong kho; dữ liệu game, ảnh chụp, nhật ký nằm ở `D:\JX-xuong\` (ngoài kho). Mở bằng `XuongJX1.bat`; đóng gói .exe (PyInstaller) làm sau nếu chủ muốn.
- Mỗi khu là một mô-đun (`suckhoe.py`, sau này `hieu.py`, `sua.py`, `build.py`, `vanhanh.py`, `suasau.py`); lỗi mô-đun được bắt, ghi nhật ký, hiện hộp "bấm Báo lỗi", không sập app. Tái dùng `TOOLS/jxweb` và `jxadm` cho khu Vận hành (không viết lại).
- Ghi nhật ký: `D:\JX-xuong\logs\<ngày>.log` (giờ | khu | thao tác | lỗi), lọc khóa/mật khẩu trước khi ghi.

## 3. Màn hình
Thanh trên: Sức khỏe, HIỂU, SỬA NỘI DUNG, BUILD & TRIỂN KHAI, VẬN HÀNH, SỬA SÂU, Báo lỗi. M0 có: đăng nhập, Sức khỏe (bảng xanh/vàng/đỏ), 5 khu giữ chỗ, Báo lỗi.

## 4. Định dạng dữ liệu
- Báo lỗi: `BUGS/XUONG-NNN.md` (giờ, phiên bản, trang, mô tả, 200 dòng log đã lọc); ảnh chụp lưu `D:\JX-xuong\anh\XUONG-NNN.png` (không lên kho).
- Cấu hình (M1 trở đi): `D:\JX-xuong\cauhinh.json` (đường dẫn, bật/tắt mô-đun).
- Bản cũ để quay lại: `D:\JX-xuong\ban-cu\0.N\` (giữ 3 bản).

## 5. Mốc và tiêu chí (theo #144 bảng B)
M0 khung → M1 HIỂU → M2 SỬA NỘI DUNG → M3 BUILD → M4 VẬN HÀNH → M5 SỬA SÂU. Tiêu chí đo được ghi trong thư #144; mỗi mốc xong thì Sonnet viết hướng dẫn thử ≤5 bước cho chủ và Chat kiểm độc lập.

## 6. Chuỗi suy diễn lỗi
Áp cho lỗi game: triệu chứng nguyên văn → xếp tầng (build/cài → cấu hình/mạng → dữ liệu/Lua → server C++ → client C++ → hiển thị) kèm phép thử loại trừ từng tầng → tra tri thức trước khi đọc mã → tái hiện, so A/B, nhãn [XÁC MINH]/[NGUỒN]/[GIẢ THUYẾT] → sửa nhỏ có công tắc → để lại tri thức + 1 test hồi quy. Sẽ đưa vào app thành trình hướng dẫn từng bước ở M1 (nối `QUY-TRINH-SUA-LOI.md`).

## 7. Xưởng tự sửa lỗi của chính nó
Nhật ký, nút Báo lỗi (có sẵn từ 0.1), số phiên bản + CHANGELOG, test cho mỗi mô-đun và mỗi lỗi đã sửa (`test_xuong.py`; test đỏ không giao), Sức khỏe chạy khi mở app. Lỗi chặn việc chủ → sửa ngay; còn lại gom theo mốc.

## 8. Rủi ro
| Rủi ro | Giảm thiểu |
|---|---|
| Ghi nhầm vào dữ liệu game thật | Chỉ bản sao + VM thử; mọi ghi tạo `.bak`, có nút hoàn tác; M2 trở đi |
| Lộ khóa/mật khẩu qua log/báo lỗi | `nhatky.loc()` lọc; test có kiểm; mã truy cập ngoài kho |
| Định dạng spr/pak đoán sai | Tra mã client, giao astra đọc trước (báo cáo), không đoán |
| Build C++ lệch với exe đang chạy | Ghi rõ mã nguồn có thể không khớp exe; build chỉ ra bản mới, không ghi đè exe cũ |
| Phụ thuộc ngoài làm app hỏng | Chỉ thư viện chuẩn; mô-đun cô lập |
| Chặn Host/CSRF | Chỉ loopback, cookie SameSite=Strict, chặn Host lạ |

## 9. Kế hoạch việc M0–M1 (mỗi việc ≤ nửa ngày)
- M0 (xong 0.1): khung, Sức khỏe, nhật ký, Báo lỗi, test. Còn: kiểm tay bấm đúp `XuongJX1.bat` (chủ).
- M1.a: mô-đun HIỂU hiển thị `MA-NGUON/` (cây tệp + tìm chữ). Vào: MA-NGUON/*.md. Ra: trang tra cứu. Xong khi: tìm "KNpc" ra đúng tệp.
- M1.b: bảng gói tin `goi-tin.md` thành trang lọc. Xong khi: tìm tên gói ra mã + tệp.
- M1.c: ô tìm theo lời người chơi, nối `MUC-LUC-TRI-THUC.md`, `KIEM-TRA-KIEN-THUC.md`, Graphify. Xong khi: 10 câu thử, ≥8 đúng, có file:dòng.
- M1.d: `TOOLS/quet_exe.py` (chuỗi chữ + nhập khẩu, chỉ ghi bảng chữ). Xong khi: có `MA-NGUON/exe-chuoi.md` cho 5 exe server.

## 10. Khu 6 — ĐO TỐC ĐỘ (thêm theo #147 A; xây sau M0–M1)
Phạm vi: chỉ đo JX-Test-36 + LDPlayer. Bắt gói chỉ trên card Host-only. Không đưa pcap vào kho. Kết quả ghi `D:\JX-xuong\do\`.

| # | Phép đo | Cách đo | Đầu ra |
|---|---|---|---|
| 1 | Mạng thô | ping + thời gian TCP connect từ LD tới JX-Test-36 | ms min/avg/max, mất gói |
| 2 | Vòng gói | `c2s_ping` → `s2c_replyclientping` | ms mỗi vòng, phân vị |
| 3 | Các chặng đăng nhập | Bishop → PaySys → Goddess → GS, mốc giờ từ log | giây mỗi chặng |
| 4 | Nhịp máy chủ | công cụ B-04a/H-13 | tick/giây, tick trễ |
| 5 | Một nhát đánh | từ gói tấn công tới gói kết quả | ms |
| 6 | FPS client | đọc FPS từ LD | fps trung bình/thấp nhất |
| 7 | N bot | tăng dần số bot, lặp 1–6 | đường cong tải |

Màn hình: bảng theo lần đo, so sánh hai lần, đánh dấu chậm bất thường. Dữ liệu JSON chỉ số liệu, không chứa tài khoản.
