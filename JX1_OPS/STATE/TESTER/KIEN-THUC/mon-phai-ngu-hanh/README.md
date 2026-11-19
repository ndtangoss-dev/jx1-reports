# KIẾN THỨC: mon-phai-ngu-hanh
## Cần làm gì (từng bước, ai đọc cũng làm lại được)
Muốn test môn phái nào thì tra bảng dưới, tạo nhân vật đúng NGŨ HÀNH của hệ đó (tạo nhân vật chọn ngũ hành trước, môn phái gia nhập sau trong game theo `gianhapmonphai`).
## Đã biết (kèm nguồn: ảnh/log/file:dòng)
Nguồn: `REPORTS/A-08a-mon-phai-ky-nang.md` (đọc từ `Settings/faction/MonPhai.ini`, `faction.ini`, nguồn tĩnh). 11 môn đầu (ID 0–10) có trong bảng gia nhập; ID 11–15 chỉ khai báo, chưa có trong bảng 11 mục.

| ID | Môn phái | Hệ | Trong bảng gia nhập | Nguồn |
|---|---|---|---|---|
| 0 | Thiếu Lâm / 少林派 | Kim | Có, dòng 6 | G/Settings/faction/MonPhai.ini:6–9; G/Settings/faction/faction.ini:7–9 |
| 1 | Thiên Vương / 天王帮 | Kim | Có, dòng 7 | G/Settings/faction/MonPhai.ini:11–14; G/Settings/faction/faction.ini:14–16 |
| 2 | Đường Môn / 唐门 | Mộc | Có, dòng 8 | G/Settings/faction/MonPhai.ini:16–19; G/Settings/faction/faction.ini:21–23 |
| 3 | Ngũ Độc / 五毒教 | Mộc | Có, dòng 9 | G/Settings/faction/MonPhai.ini:21–24; G/Settings/faction/faction.ini:28–30 |
| 4 | Nga My / 峨嵋派 | Thủy | Có, dòng 10 | G/Settings/faction/MonPhai.ini:26–29; G/Settings/faction/faction.ini:35–37 |
| 5 | Thúy Yên / 翠烟门 | Thủy | Có, dòng 11 | G/Settings/faction/MonPhai.ini:31–34; G/Settings/faction/faction.ini:42–44 |
| 6 | Cái Bang / 丐帮 | Hỏa | Có, dòng 12 | G/Settings/faction/MonPhai.ini:36–39; G/Settings/faction/faction.ini:49–51 |
| 7 | Thiên Nhẫn / 天忍教 | Hỏa | Có, dòng 13 | G/Settings/faction/MonPhai.ini:41–44; G/Settings/faction/faction.ini:56–58 |
| 8 | Võ Đang / 武当派 | Thổ | Có, dòng 14 | G/Settings/faction/MonPhai.ini:46–49; G/Settings/faction/faction.ini:63–65 |
| 9 | Côn Lôn / 昆仑派 | Thổ | Có, dòng 15 | G/Settings/faction/MonPhai.ini:51–54; G/Settings/faction/faction.ini:70–72 |
| 10 | Hoa Sơn / 华山派 | Thủy | Có, dòng 16 | G/Settings/faction/MonPhai.ini:56–59; G/Settings/faction/faction.ini:77–79 |
| 11 | Lý Tầm Hoan / 李寻欢 | Mộc | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:61–64; G/Settings/faction/faction.ini:84–86 |
| 12 | Đào Hoa Đảo / 桃花岛 | Thủy | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:66–69; G/Settings/faction/faction.ini:89–91 |
| 13 | Minh Giáo / 明教 | Hỏa | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:71–74; G/Settings/faction/faction.ini:94–96 |
| 14 | Đoàn Thị / 段氏 | Thổ | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:76–79; G/Settings/faction/faction.ini:99–101 |
| 15 | Tự sáng môn phái / 自创门派 | Kim | Không có trong bảng 11 mục | G/Settings/faction/MonPhai.ini:81–84; G/Settings/faction/faction.ini:104–106 |

Trạng thái: [CHƯA KIỂM] bằng client thật (mới đọc nguồn tĩnh); tester xác nhận khi tạo nhân vật.
## Chưa hiểu
- Khung tạo nhân vật của client mobile cho chọn những ngũ hành/môn nào: CHƯA KIỂM.
