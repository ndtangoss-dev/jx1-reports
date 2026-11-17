# smoke_login — 2026-11-17

gs001 thật: **chưa kiểm**. Chỉ máy chủ giả cục bộ; không đăng nhập thật.

Nhánh: task/E-05a-tester; commit: e4f16af5e0fe0410a01c0e182078a44ab04f548d

| Bot | connect_fake | sync_fake | close_fake |
| --- | --- | --- | --- |
| bot02 | PASS (0.000s) | FAIL (0.000s) | BỎ QUA (0.000s) |

## bot02 / connect_fake

Đạt kỳ vọng

Log:
- Đã nhận ACCOUNT_BEGIN tổng hợp; không lưu khóa
Gói tin lỗi (tối đa 256 byte/gói; body đã che bằng 00):
- Không có gói tin lỗi quan sát được

## bot02 / sync_fake

ProtocolError: Gói GS chưa hỗ trợ: ID=255; xem E-01b-thieu-giao-thuc.md

Log:
- Không có log
Gói tin lỗi (tối đa 256 byte/gói; body đã che bằng 00):
- nhận; ID=0xff; 401 byte; hex=ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

BUG: [BUG-002.md](BUG-002.md)

## bot02 / close_fake

Bot đã dừng sau lỗi bước trước

Log:
- Không có log
Gói tin lỗi (tối đa 256 byte/gói; body đã che bằng 00):
- Không có gói tin lỗi quan sát được
