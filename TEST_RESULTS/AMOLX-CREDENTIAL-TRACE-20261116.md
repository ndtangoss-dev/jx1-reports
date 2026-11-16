# AMOLX-CREDENTIAL-TRACE — Tổng hợp truy tìm thông tin đăng nhập

- Ngày bàn giao: 16/11/2026, múi giờ UTC+7.
- Trạng thái truy tìm: **DONE trong phạm vi đã kiểm tra bên dưới**.
- Trạng thái xác thực AMOLX hiện tại: **BLOCKED — chưa đăng nhập thành công**.
- Báo cáo tổng hợp thực thi: [AMOLX-10-GAMEPLAY-TEST-20261116.md](AMOLX-10-GAMEPLAY-TEST-20261116.md).
- Cần người dùng quyết định: không đối với việc xuất bản báo cáo này. Việc sửa giao thức và tạo APK mới là bước tiếp theo, chưa thực hiện trong lượt bàn giao.

## Tóm tắt 5 dòng

1. Đã tìm được mật khẩu lịch sử của tài khoản testlocal trong phiên Claude Code cục bộ; không xuất giá trị hoặc hash mật khẩu.
2. Đã đối chiếu cùng phiên với log Login Success! ngày 11/11/2026 lúc 10:18:53.
3. Đã lưu thông tin khôi phục vào Windows Credential Manager và kiểm tra đọc lại khớp, không tạo file mật khẩu.
4. Đã thử đăng nhập trên APK hiện có; Bishop trả LOGIN_R_INVALID_PROTOCOLVERSION trước bước kiểm tra tài khoản/mật khẩu.
5. Chưa xác minh mật khẩu còn hợp lệ hiện tại; không reset tài khoản, tạo tài khoản mới hoặc sửa cơ sở dữ liệu.

## Phạm vi và checkpoint

Tiếp tục từ kết quả đã thu thập trước khi phiên API bị gián đoạn, không quét lại toàn bộ dữ liệu. Root chỉ đọc là C:\Users\PC\.claude. Dữ liệu Claude không bị sửa, xóa hoặc di chuyển. Lượt xuất bản chỉ dùng kết quả và bằng chứng đã có, không chạy lại truy tìm hay đăng nhập.

Không sao chép raw transcript, file OAuth, payload đăng nhập hoặc dump bộ nhớ lên repository. Nội dung bên dưới chỉ gồm vị trí nguồn, mốc thời gian, metadata và kết luận đã lọc.

## Phiên Claude và nguồn thông tin đăng nhập

Phiên chính: C:\Users\PC\.claude\projects\C--Jx1CocoV3\a0880e5a-8ede-5f1c-bcee-f7a55bccc5a3.jsonl.

Kích thước đã ghi nhận: 551.290.134 byte, 44.853 dòng. Số dòng dưới đây là số dòng JSONL trong file đó, không phải toàn bộ nội dung hội thoại được công bố.

| Vị trí | Thời gian | Nội dung đã xác minh, không chứa bí mật |
|---|---|---|
| Dòng 249, tool id toolu_017a8bdBRDVwJ9X7E5iyPznp | 10/11/2026 09:29:11 UTC+7; gốc 2026-11-10T02:29:11.288Z | Lệnh PowerShell lịch sử chứa thao tác tạo Account_Info có điều kiện cho testlocal; hai literal đầu vào HASHBYTES MD5 giống nhau. Đã khôi phục giá trị trong bộ nhớ, không công bố câu lệnh hay giá trị. |
| Dòng 250 | Liền sau lệnh trên | Kết quả tool không báo lỗi; đây là bằng chứng lịch sử, không phải thao tác SQL được chạy lại. |
| Dòng 743 và 1607 | 10/11/2026 11:13:14 và 19:26:34 UTC+7 | Claude gửi username/password qua hội thoại và nói không lưu file/Git. |
| Dòng 2857 | 11/11/2026 09:29:37 UTC+7 | Nhắc lại mật khẩu đã gửi hôm trước. |
| Dòng 3532, tool id toolu_01NBTV7kwFFHGi3T436wx9d2 | Tool result 11/11/2026 10:20:48 UTC+7; gốc 2026-11-11T03:20:48.675Z | Log chứa Login Success! của testlocal lúc 10:18:53 và Logout lúc 10:19:30 ngày 11/11/2026, Gateway fsjx tại 192.168.1.50. |

Có bằng chứng mật khẩu xuất hiện trong lệnh và hội thoại lịch sử; chưa đủ bằng chứng kết luận ai đặt mật khẩu ban đầu hoặc cách sinh mật khẩu. Không coi giá trị lịch sử là đã xác thực hiện tại.

Đối chiếu độc lập: docs-analysis/reports/19-cdn-8080-va-forwarder.md, dòng 9 và 29; bản file-history 8bf6f10213eeb7e7@v2 trong thư mục của phiên trên cũng khớp tại dòng 9 và 29. Đây là log lịch sử ngày 11/11, không phải kết quả AMOLX ngày 16/11.

## Những nguồn đã kiểm tra

| Nguồn trong .claude | Phạm vi đã kiểm | Kết quả liên quan |
|---|---|---|
| sessions | 2 file metadata | Không tìm thấy đăng nhập ngày 11/11. |
| projects | 55 file trong phạm vi truy tìm; 3 JSONL lớn đã đọc tuần tự đến cuối | Tìm được phiên chính, nguồn mật khẩu và log thành công lịch sử. |
| file-history | 372 file | Tìm được bản báo cáo/log tương ứng; không tìm được literal mật khẩu trong phạm vi này. |
| session-env | 3 thư mục, 0 file | Không có file biến môi trường để đối chiếu. |
| backups | 5 bản .claude.json | Không tìm được mật khẩu game. |
| history.jsonl | 7 entry | Không có testlocal. |
| .credentials | Không tồn tại | Không có nguồn để đọc. |
| .credentials.json | Đã kiểm có kiểm soát | Dữ liệu OAuth Claude, không phải credential game; không xuất giá trị. |
| settings.json | Đã kiểm | Có model/modelSettings/autoUpdatesChannel/theme; không thấy cấu hình đăng nhập game. |
| .claude.json ở root | 1 file | Không tìm được mật khẩu game. |
| shell-snapshots | 2 file | Không tìm được nguồn bổ sung cho mật khẩu game. |
| cache | 5 file | Không tìm được nguồn bổ sung cho mật khẩu game. |
| bridge-spawn, downloads, spares | 0 file trong phạm vi đã kiểm | Không có dữ liệu để đối chiếu. |

Giới hạn: chưa OCR 39 binary uploads; không đọc từng byte của toàn bộ package plugins/skills vì nằm ngoài lịch sử cần truy tìm. Không tuyên bố đã đọc mọi byte trong root .claude. Sau khi có chuỗi bằng chứng trực tiếp và log lịch sử khớp, không mở rộng sang dữ liệu không liên quan.

## Windows Credential Manager

Đã đọc vault thật trong phiên người dùng bằng quyền đã được duyệt. Lỗi 1168 khi kiểm tra trong môi trường hạn chế trước đó không chứng minh vault thật rỗng.

| Target đã đối chiếu | Kết quả |
|---|---|
| JX-Test-36-game-testlocal | Không tồn tại trong vault thật đã kiểm. |
| JX-Test-36-game-jxtest36 | Có nhưng là tài khoản/VM khác; không dùng. |
| JX-Server-D-ldtest | Có, user jxld01; không phải testlocal. |
| JX-Server-D-admin | Có, tài khoản quản trị VM; không dùng để đăng nhập game. |

Thông tin lịch sử đã khôi phục được lưu tại target **JX1-AMOLX-testlocal-recovered-20261116**, username testlocal, Generic Type 1 / Persist 2. Đã kiểm tra đọc lại khớp trong bộ nhớ; không ghi đè target có sẵn và không lưu plaintext vào file.

Cách truy xuất an toàn cho bước tiếp theo: nạp wrapper C:\Jx1CocoV3\docs-analysis\scripts\jxlab_cred.ps1, rồi gọi [CredMgr]::Read với đúng target trên và giữ kết quả trong biến bộ nhớ. Không in object trả về, password hoặc hash; không đưa giá trị vào dòng lệnh/log. Target này chứa credential lịch sử được khôi phục, **chưa xác minh còn hợp lệ bằng đăng nhập hiện tại**.

## Kết quả thử trên AMOLX hiện có

- Thiết bị test đã xác định: LDPlayer 9, ADB serial emulator-5554, package com.kull.jx1client.
- Đã nhập testlocal và mật khẩu khôi phục trên APK đang cài; không build/cài lại trong lượt truy tìm tiếp tục.
- Đã làm sạch ô nhập sau một lần thao tác Enter gây lỗi ký tự; nhập lại không Enter. Không coi lỗi thao tác đó là blocker cuối.
- Đã mở lại riêng ứng dụng và thử kết nối mới để loại trừ trạng thái luồng nhận cũ; không clear data hay reset emulator.
- TCP và handshake đạt. Runtime trả s2c_login, message id 65, struct 146 byte, Param 0x0005000a, mã 10 = LOGIN_R_INVALID_PROTOCOLVERSION.
- AMOLX đang cài dùng KLoginAccountInfo 142 byte, thiếu nEnterMapIdx. ProtocolVersion lệch 4 byte so với Cocos/Bishop và phản hồi thực tế.
- Xử lý Bishop tham chiếu kiểm tra version trước tài khoản. Phản hồi từ chối sớm không khớp account/password echo; AMOLX kiểm echo trước mã lỗi nên bỏ qua thông báo lỗi.

Việc echo không khớp trong phản hồi lỗi không chứng minh mật khẩu sai. Không có bằng chứng đăng nhập thành công ngày 16/11, chưa chọn nhân vật hoặc vào bản đồ.

Bằng chứng đã lọc: amolx-work/AMOLX-04-20261115/build/amolx10-login-protocol-metadata.json, ghi lúc 2026-11-16T07:21:35.641Z (14:21:35 UTC+7). Không lưu payload/mật khẩu/hash cùng metadata. Chi tiết size/offset và đường dẫn source nằm trong báo cáo tổng hợp AMOLX-10.

## Trạng thái bàn giao và Git

- Hoàn tất truy tìm credential lịch sử trong phạm vi nêu rõ; không reset testlocal, tạo account hoặc sửa SQL.
- BLOCKED ở đăng nhập AMOLX do layout protocol; tính hợp lệ hiện tại của credential còn CHƯA XÁC MINH.
- Chưa khảo sát lại AMOLX, chưa sửa source hoặc build APK trong lượt xuất bản này.
- Workspace nguồn C:\Jx1CocoV3: nhánh master, HEAD 2f7aa0c39be94b86cbd077bf85e24b4855873e27; có thay đổi dở dang từ trước, được giữ nguyên.
- Xuất bản cùng báo cáo AMOLX-10 lên ndtangoss-dev/jx1-reports/main; commit cha đã kiểm là 39b97e0b0fa061bae2e847c462b8f0e0158dfa9e. SHA commit chứa hai báo cáo được xác minh và cung cấp trong lời bàn giao; không thể chèn SHA tự tham chiếu vào chính nội dung commit đó.
- Chỉ hai file Markdown được đưa vào commit. Không đẩy source, APK, backup, log thô, transcript hay credential.
