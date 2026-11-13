# U003 – G0.7: READ-ONLY VERIFICATION

## 1. Mục tiêu

Tiếp tục nghiên cứu source JX1 và các báo cáo G0 trước đó để xác minh những quy tắc còn chưa rõ trước khi bắt đầu lập trình U003.

Đọc các tài liệu:
- U003_G0_51_khao-sat-hoan-tat.md
- U003_G0_52_bo-sung-xac-minh.md
- U003_G0_53_che-khuat-ui-quai.md
- U003_G0_54_thiet-ke-kien-truc.md
- U003_G05_55_spr-ipotree-direction-skill375.md
- U003_G06_56_hit-damage-combat-verification.md
- U003_G07_57_chatgpt-review-and-next-instructions.md
- BAI_HOC.md

Dùng kết quả các báo cáo trên làm cơ sở. Không làm lại những việc đã xác minh, trừ khi cần kiểm tra chéo để giải quyết mâu thuẫn.

## 2. Các nội dung cần xác minh

### A. Hit animation của ani001

- Xác định chính xác action/frame tương ứng với Hit của ani001.
- Kiểm tra mapping giữa tên action, mã action, hướng và sprite frame.
- Xác minh `ani001_bat.spr` có thực sự là ảnh Hit hay không.
- Xác định Hit có được gọi khi nhận sát thương từ kỹ năng 375 hay không.
- Phân biệt rõ điều đã xác minh và điều chỉ mới suy luận.

### B. Attrib 1002 và luồng xử lý sát thương

- Truy ngược định nghĩa Attrib 1002.
- Xác định nơi tạo, truyền và áp dụng giá trị sát thương.
- Kiểm tra luồng xử lý liên quan đến skill 375, missile 181, skill 387 và missile 193.
- Xác định chính xác sự kiện nào làm giảm HP quái.
- Phân biệt logic phía client, source server và những gì chưa thể xác nhận về server EXE đang chạy.
- Không suy diễn rằng source server chắc chắn trùng với server EXE thực tế.

### C. Thời điểm thi triển kỹ năng

- Xác minh quy tắc kích hoạt kỹ năng tại mốc 60% tiến trình action.
- Tìm cách tính thời điểm thực tế dựa trên AttackSpeed hoặc các tham số liên quan.
- Xác định chính xác ý nghĩa và đơn vị của `nWaitTime`, `WaitTime`, `MslsGenerateData`.
- Kiểm tra cách tạo độ trễ của 16 missile 181.
- Xác minh mốc thời gian của missile 181 và missile 193.
- Nếu không xác định được đơn vị thời gian hoặc công thức, phải ghi rõ chưa xác minh; không tự gán thành mili giây.

### D. MoveKind = Stand

- Truy nguồn xử lý `MoveKind=Stand` của missile 181.
- Xác minh missile đứng tại vị trí được tạo hay có chuyển động nào khác.
- Kiểm tra điều kiện collision và cách xác định vị trí tạo missile 193.
- Không tự thiết kế đường bay homing nếu source không có.

### E. Render, blend và anchor

- Xác minh cách giải mã và hiển thị sprite có alpha.
- Kiểm tra anchor/center của ani001 trong các action cần thiết.
- Xác minh quy tắc chuyển frame theo hướng và action.
- Kiểm tra các trường hợp ảnh có thể bị lệch vị trí, viền alpha hoặc sai tỷ lệ.
- Không tự chọn anchor mặc định nếu chưa có bằng chứng.

### F. Map 45 và tọa độ

- Xác minh tính đầy đủ của dữ liệu map 45.
- Kiểm tra các file Region_C.dat và dữ liệu liên quan.
- Phân biệt tọa độ MPS tuyệt đối, tọa độ region và tọa độ local.
- Xác minh công thức chuyển đổi từ MPS sang tọa độ màn hình.
- Xác định các vùng địa hình, vật cản, cây và dữ liệu cần thiết cho việc port KIpoTree.
- Không kết luận map 45 đã hoàn chỉnh nếu chưa kiểm tra đủ các region cần thiết.

## 3. Các quy tắc thiết kế U003 đang được dùng làm giả định

Đây là quy tắc prototype U003, không được nhầm thành quy tắc gốc của JX1:

- Skill 375 tạo 16 missile 181 theo bố cục 4×4.
- Missile 181 kích hoạt chuỗi xử lý dẫn tới missile 193.
- Missile 193 có vùng ảnh hưởng 3×3 ô logic theo dữ liệu đã nghiên cứu.
- Mỗi vùng AOE có hai lần gây sát thương, tại +500ms và +1000ms tính từ thời điểm vùng AOE được kích hoạt.
- Mỗi lần gây 20 sát thương lên từng quái còn sống trong vùng.
- Các vùng AOE chồng lấn được phép cộng dồn sát thương.
- HP quái thử nghiệm là 1.000.
- Mỗi lần sát thương tạo một sự kiện số damage riêng, không gộp nhiều lần thành một số.
- Thời gian thi triển là 1 giây.
- Cooldown là 1 giây tính từ lúc bắt đầu thi triển; đây là quy tắc U003, không phải cooldown gốc đã xác minh của skill 375.
- Do các missile có thể kích hoạt trễ và nhiều lần thi triển có thể chồng lấn, mỗi lần cast phải có ID riêng để không trộn sự kiện giữa các lần thi triển.

Các quy tắc trên là cơ sở thiết kế tạm thời. Nếu phát hiện bằng chứng source mâu thuẫn, báo cáo phải nêu rõ để ChatGPT và người dùng quyết định, không tự ý thay đổi thiết kế.

## 4. Phạm vi và giới hạn bắt buộc

Đây là nhiệm vụ READ-ONLY.

Được phép:
- Đọc source, PAK và dữ liệu đã trích xuất.
- Viết script kiểm tra tạm thời trong workspace U003 nếu cần.
- Chạy công cụ phân tích không làm thay đổi dữ liệu gốc.
- Chụp ảnh hoặc tạo dữ liệu minh chứng trong workspace U003.
- Đối chiếu các báo cáo cũ.

Không được phép:
- Tạo hoặc chỉnh sửa Unity project.
- Viết gameplay code hoặc bắt đầu triển khai U003.
- Build APK.
- Cài package, thư viện, model AI hoặc công cụ mới.
- Chỉnh sửa source client/server gốc.
- Chỉnh sửa PAK hoặc dữ liệu gốc.
- Chỉnh sửa `pak_extract.py`.
- Thay đổi database, VM, cấu hình server, firewall hoặc Tailscale.
- Khởi động lại, dừng hoặc thao tác với Goddess hay bất kỳ EXE server nào.
- Chỉnh sửa U001 hoặc U002.
- Xóa, di chuyển, ghi đè dữ liệu hoặc thay đổi những công việc chưa được giao.

Nếu gặp vấn đề cần hành động ngoài phạm vi READ-ONLY, dừng lại và báo cáo, không tự mở rộng phạm vi.

## 5. Báo cáo đầu ra

Tạo báo cáo:

`JX1_VISUAL/REPORTS/U003_G07_58_g07-hit-attrib-cast-anchor-map-verification.md`

Báo cáo phải có:

1. Tóm tắt kết quả.
2. Kết quả riêng cho từng mục A–F.
3. Đường dẫn file, tên hàm, class, dòng code hoặc dữ liệu làm bằng chứng.
4. Phân biệt ba mức:
   - Đã xác minh bằng source/dữ liệu.
   - Có bằng chứng nhưng chưa đủ kết luận.
   - Chưa xác minh được.
5. Ảnh hoặc dữ liệu minh chứng nếu cần.
6. Những điểm mâu thuẫn với báo cáo trước.
7. Những quyết định thiết kế U003 cần người dùng phê duyệt.
8. Danh sách việc còn thiếu trước khi bắt đầu G1.

Nếu có bài học mới, bổ sung vào `BAI_HOC.md`. Không viết lại hoặc xóa các bài học cũ.

## 6. Git và bàn giao

Sau khi hoàn thành:

- Kiểm tra `git status`.
- Chỉ đưa báo cáo 58 và thay đổi liên quan trực tiếp đến `BAI_HOC.md` vào commit.
- Không stage hoặc commit các file khác.
- Không reset, clean, force push hoặc ghi đè lịch sử.
- Push bình thường lên branch `main`.
- Nếu push gặp conflict, dừng và báo cáo; không tự giải quyết bằng force push.
- Cung cấp commit SHA, đường dẫn file và link GitHub.
- Ghi rõ các kiểm tra đã thực hiện và những phần chưa hoàn thành.

Hoàn thành báo cáo thì dừng, chờ ChatGPT đọc và review. Không tự chuyển sang G1 hoặc bắt đầu lập trình.
