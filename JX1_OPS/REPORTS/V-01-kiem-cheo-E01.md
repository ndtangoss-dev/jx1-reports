# V-01 — kiểm chéo báo cáo E-01 với mã thật (19/11/2026, lượt 1/5)

**TÓM TẮT 5 DÒNG**
1. [ĐÃ KIỂM] E-01 dẫn `KCore.cpp:62` cho hằng khóa client: đúng (`curMobileKey` ở dòng 62, client `Classes/gamecore/KCore.cpp`).
2. [ĐÃ KIỂM] E-01 dẫn `KProtocol.cpp:179-183` cho các ID extend độ dài biến (-1): thực tế các dòng đặt `-1` cho `s2c_extend`, `extendchat`, `extendfriend`, `extendtong`, `extendchat_new` nằm ở 180-184 (lệch 1 dòng, nội dung đúng, 5 ID chứ không phải ID 250-254 viết trực tiếp).
3. [ĐÃ KIỂM] E-01 dẫn `KgameWorld.cpp:5134` cho việc bỏ ID lạ ở đuôi: điều kiện `Msg <= s2c_clientbegin || Msg >= s2c_end || GetProtocolSize(Msg)==0` ở 5135 (lệch 1 dòng, nội dung đúng).
4. [CHƯA KIỂM] Bảng kích thước ID 70/77/220 so exe thật: cần frame thật, không đối chiếu được từ mã.
5. Cần tôi quyết định: không. Còn 4 báo cáo trong danh sách V-01 chưa kiểm.
