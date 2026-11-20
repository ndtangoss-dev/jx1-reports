# Hiểu game JX1 cho người không lập trình

Tài liệu này diễn giải các kết quả tĩnh đã có bằng ngôn ngữ dễ đọc. Số liệu trong báo cáo không đồng nghĩa với nội dung đang chạy trong game.

## Cách đọc nhãn

- **ĐÃ XÁC MINH (tĩnh):** số liệu hoặc quy tắc đã được ghi nhận trong báo cáo khảo sát/file dữ liệu được dẫn; chưa mặc định là đã chạy đúng trong game.
- **CHƯA XÁC MINH:** còn thiếu dữ liệu bản triển khai, asset, cấu hình được nạp hoặc kiểm tra runtime.

## Nhân vật và chỉ số

**ĐÃ XÁC MINH (tĩnh):** EXP là điểm tiến tới ngưỡng cấp tiếp theo. Bảng được khảo sát ghi 100 EXP ở cấp 1 và 2.000.000 EXP ở cấp 50. Ở nhánh lên cấp thông thường, nhân vật tăng một cấp, nhận **5 điểm tiềm năng** và **1 điểm kỹ năng**, rồi EXP được đặt về 0. Tiềm năng là điểm để phát triển thuộc tính; điểm kỹ năng dành cho kỹ năng.

**CHƯA XÁC MINH:** bảng EXP rời có 200 cấp, còn hằng số cấp tối đa trong source được báo cáo là 500 và cấu hình khác ghi 200. Chưa chứng minh các giới hạn này cùng áp dụng trên bản đang chơi; cũng chưa biết số dư EXP và các đường cộng EXP trên runtime.

Nguồn: `JX1_OPS/REPORTS/I-01-cac-loai-diem.md:23–39,71–82,126`; `JX1_OPS/REPORTS/A-08d-kinh-nghiem.md:70–75`; đối chiếu giới hạn tại `JX1_OPS/DESIGN/THE-GIOI-TONG-QUAN.md:43–52`.

## Môn phái và kỹ năng

**ĐÃ XÁC MINH (tĩnh):** bảng khai báo có **16 mục** môn phái, nhưng bảng thông tin gia nhập chỉ có **11 mục**. Vì vậy con số 16 là số mục trong cấu hình, chưa phải số phái đã chứng minh có thể chọn và chơi. Ví dụ trong catalog, Nga Mi có kỹ năng **ID 80, Phiêu Tuyết Xuyên Vân**.

**CHƯA XÁC MINH:** catalog tên kỹ năng không chứng minh kỹ năng học được hoặc dùng được trong bản triển khai. Báo cáo ghi có ID lệch tên và ID 1702 không có trong bảng Skills rời đã đọc; không tự gán các kỹ năng thiếu này cho một phái.

Nguồn: `JX1_OPS/REPORTS/A-08a-mon-phai-ky-nang.md:1–5,28,49,113–120`; ví dụ kỹ năng: `JX1_OPS/REPORTS/A-15b-ky-nang-phai-5-8.md:61–70`.

## Trang bị và cường hóa

**ĐÃ XÁC MINH (tĩnh):** một món đồ có thể chứa nhiều nhóm thông tin; điều kiện yêu cầu mặc không phải dòng thưởng chỉ số. Ví dụ, dữ liệu item **ID 126** ghi sát thương vật lý **+5 đến +10** ở mức dữ liệu 1 và **+10 đến +20** ở mức 2. Source được khảo sát cho biết cường hóa chỉ tăng một số dòng thuộc tính phép đủ điều kiện, theo **5% giá trị gốc mỗi cấp**; mức tăng không cộng lãi kép trên kết quả cấp trước.

**CHƯA XÁC MINH:** tên/nguồn đá, cấp cường hóa thực tế và cấu hình tối đa của bản đang chạy. Các tệp cấu hình được khảo sát có trần +5, trong khi tài liệu lịch sử nhắc +15; chưa xác định tệp nào được nạp.

Nguồn: `JX1_OPS/REPORTS/H-02-magic-attrib.md:28–58,86–97`; `JX1_OPS/REPORTS/H-03-cuong-hoa.md:30–43,47–62,118–145`.

## Tiền tệ và cửa hàng

**ĐÃ XÁC MINH (tĩnh):** bạc, Xu, phúc duyên, danh vọng, vinh dự và Tống Kim là các loại số dư/điểm khác nhau. Trong một nhánh mua được khảo sát, **task 2051** đại diện vinh dự và **task 192** đại diện điểm Tống Kim; Xu cũng khác điểm nạp `ExtPoint`. Ví dụ trong bảng hàng hóa: **Bạch Câu Hoàn giá 3 Xu**, còn **Bạch Mã giá 5.000 bạc trước thuế**.

**CHƯA XÁC MINH:** giá và thuế đang áp dụng, vật phẩm shop có được nạp hay không và giao dịch thực tế. Báo cáo I-07 ghi `GetMoney` cộng bạc trong túi và rương, trong khi `Pay` ở nhánh khảo sát thường chỉ trừ bạc trong túi; tổng nhìn thấy vì vậy không bảo đảm đủ số bạc có thể chi ngay.

Nguồn: `JX1_OPS/REPORTS/I-02-vat-pham-ban.md:26–37,45–65`; `JX1_OPS/REPORTS/I-07-cac-loai-tien-te.md:31–39`; đối chiếu tại `JX1_OPS/DESIGN/THE-GIOI-TONG-QUAN.md:54–73`.

## Quái và bản đồ

**ĐÃ XÁC MINH (tĩnh):** catalog có **2.435 mẫu NPC/quái**, đây là số mẫu dữ liệu chứ không phải số quái đang sống. Ví dụ hai mẫu quái ở cấp 30 có HP tính từ dữ liệu là **570** và **2.850**, cùng EXP cơ sở **290**. Catalog bản đồ gốc có **993 ID**; ví dụ **ID 53 là Ba Lăng Huyện**, được ghi loại Country.

**CHƯA XÁC MINH:** số quái đang xuất hiện, sức mạnh cuối sau các ghi đè và bản đồ thật sự được nạp. WorldSet có 872 mục nhưng trường Count là 800; con số này mô tả giới hạn vòng tải trong source đã khảo sát, chưa chứng minh có 800 bản đồ tải thành công.

Nguồn: `JX1_OPS/REPORTS/I-03-khao-sat-quai-vat.md:2–6,44–50,80–88,219`; `JX1_OPS/REPORTS/I-04-khao-sat-map.md:30–38,61–69`; đối chiếu tại `JX1_OPS/DESIGN/THE-GIOI-TONG-QUAN.md:75–95`.

## Nhiệm vụ

**ĐÃ XÁC MINH (tĩnh):** một kho trạng thái có thể dùng khóa **0–9999**, nhưng khóa này còn phục vụ tiền/điểm, bộ đếm thời gian và phần chơi khác; không phải có 10.000 nhiệm vụ. Một mẫu TASKSYS đi qua các trạng thái **0 → 1 (bắt đầu) → 2 (hoàn tất) → 3 (nhận thưởng)**.

**CHƯA XÁC MINH:** không phải mọi loại nhiệm vụ dùng cùng trạng thái; việc engine nạp script, ghi dữ liệu và trao thưởng trong bản đang chạy chưa được thử. Không lấy một mẫu TASKSYS làm quy luật chung cho toàn bộ quest.

Nguồn: `JX1_OPS/REPORTS/I-08-he-thong-nhiem-vu.md:34–36,82–90,104`; đối chiếu tại `JX1_OPS/DESIGN/THE-GIOI-TONG-QUAN.md:97–105`.

## Hiệu ứng vũ khí

**ĐÃ XÁC MINH (ghi nhận trong báo cáo lịch sử):** các mốc hiệu ứng được báo cáo là **+6** bắt đầu phát sáng, **+12** sáng mạnh hơn và có sét, **+15** sáng mạnh nhất với nhiều tia hơn. Đây là mô tả hiệu ứng hình ảnh, không phải công thức tăng sát thương.

**CHƯA XÁC MINH:** các mốc này có còn đúng trong client hiện tại hay không; báo cáo H-04 nói phần sét chưa được xác nhận trên điện thoại và mã hiện tại chưa được đối chiếu với APK mốc. Không dùng báo cáo cũ để cam kết hiệu ứng sẽ xuất hiện trên mọi nhân vật hoặc thiết bị.

Nguồn: `JX1_OPS/REPORTS/H-04-hieu-ung-vu-khi.md:1–5,9–19`; tách hiệu ứng hình ảnh khỏi chỉ số cường hóa: `JX1_OPS/REPORTS/H-03-cuong-hoa.md:193–206`.

## Phạm vi xác minh

Các mục trên tổng hợp báo cáo tĩnh trong worktree; không chạy game, VM, executable, build hay kết nối mạng. Trong worktree này chưa tìm thấy `人物类型.txt`, `KNpcResNode.cpp`, `THONG-SO-GAME.md` hoặc `BASELINE-001`. Vì vậy quy luật vẽ bộ phận và một số nội dung phụ thuộc bản triển khai còn được đánh dấu **CHƯA XÁC MINH**; xem `JX1_OPS/DESIGN/QUY-LUAT-VE-BO-PHAN.md`.
