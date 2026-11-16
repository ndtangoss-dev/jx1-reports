CẬP NHẬT ĐỊNH HƯỚNG VÀ YÊU CẦU LẬP LẠI KẾ HOẠCH DỰ ÁN JX1

Đây là chỉ thị cập nhật mới nhất của chủ dự án. Nội dung này thay thế những quyết định cũ có mâu thuẫn trong bộ tài liệu bàn giao của Fable.

1. Thay đổi cơ cấu AI


Claude Opus: Model chịu trách nhiệm nghiên cứu, phân tích kiến trúc và lập kế hoạch tổng thể.

Claude Sonnet: Trưởng dự án (Project Manager - PM), chịu trách nhiệm điều phối AI worker, phân công, giám sát, kiểm tra và tích hợp công việc.

Fable: Kết thúc nhiệm vụ, không còn vai trò trong dự án. Chỉ kế thừa và tận dụng những tài liệu, nghiên cứu, báo cáo và cấu trúc bàn giao Fable đã tạo.



Sau khi kế hoạch của Opus được chủ dự án xem xét và phê duyệt, chủ dự án sẽ chuyển kế hoạch đó cho Sonnet để tiếp quản và tổ chức triển khai.

2. Thay đổi định hướng kỹ thuật

Dự án sẽ sử dụng lại client và server JX1 gốc.

Không tiếp tục phương án xây dựng client Axmol mới và server mới độc lập như kế hoạch trước đây.

Mục tiêu:


Làm chủ hoàn toàn source code client và server.

Hiểu rõ kiến trúc, database, cấu hình, script, giao thức và toàn bộ tài nguyên.

Tận dụng tối đa các tính năng, hoạt động và tài nguyên sẵn có.

Tối ưu hiệu năng, giảm lag, cải thiện nhịp xử lý và độ ổn định.

Giữ chất gameplay JX1, không tùy tiện thay đổi cơ chế gameplay cốt lõi.



3. Cơ chế thế giới bắt buộc

Đây là đặc điểm riêng của dự án và phải được giữ nguyên trong mọi thiết kế:

Bản đồ thông thường


Người chơi thật không nhìn thấy nhân vật người chơi thật khác.

Người chơi thật tương tác với các AI Bot.

Bot là thực thể chung của thế giới, không phải bản sao riêng cho từng người chơi.

Nếu người chơi A giết một Bot thì người chơi B và những người chơi liên quan cũng phải nhìn thấy Bot đã chết.

Trạng thái, vị trí, hoạt động và vòng đời Bot phải được quản lý, đồng bộ tập trung.



Hoạt động đặc biệt


Một số hoạt động được phép hiển thị người chơi thật cho nhau.

Chủ dự án phải chủ động thiết lập hoạt động nào được phép hiển thị người chơi thật.

Có thể cấu hình số lượng người chơi thật tối đa tham gia từng hoạt động.

Cần nghiên cứu khả năng cấu hình phe, đội, bản đồ, giới hạn người tham gia và các điều kiện hoạt động.



Không được hiểu nhầm rằng dự án muốn xóa bỏ hoàn toàn khả năng nhìn thấy người chơi thật. Việc hiển thị chỉ được cho phép ở những hoạt động được thiết lập.

4. Thứ tự ưu tiên triển khai

Giai đoạn A — Khảo sát và làm chủ hệ thống gốc

Kiểm kê đầy đủ client, server, database, tài nguyên, script, file cấu hình và công cụ vận hành.

Phân tích cơ chế đăng nhập, quản lý account, nhân vật, kết nối, bản đồ, đồng bộ thực thể và các hoạt động.

Giai đoạn B — Thử nghiệm chuyển đổi server

Server hiện tại đang hoạt động theo mô hình MMORPG thông thường, người chơi nhìn thấy nhau.

Cần nghiên cứu và thử nghiệm khả năng chuyển sang mô hình:


Mặc định người chơi thật không nhìn thấy nhau.

Một số hoạt động được cấu hình cho phép nhìn thấy nhau.

Có giới hạn số người thật tham gia theo từng hoạt động.



Phải xác định rõ phần nào có thể cấu hình, phần nào phải sửa source và phần nào cần xây dựng bổ sung.

Giai đoạn C — Làm chủ hệ thống tài khoản

Nghiên cứu và xây dựng khả năng quản lý tập trung account, nhân vật, đăng nhập, trạng thái hoạt động và các công cụ quản trị cần thiết.

Giai đoạn D — Kiểm kê toàn bộ gameplay và hoạt động

Phân loại từng hoạt động:


Đã hoàn thiện và đang hoạt động.

Có trong source nhưng chưa kích hoạt.

Có code nhưng lỗi hoặc chưa hoàn thiện.

Chỉ có giao diện hoặc dữ liệu, chưa có logic.

Chưa được xây dựng.



Xác định vị trí logic xử lý, dữ liệu, cấu hình, điều kiện kích hoạt, lịch hoạt động và phần thưởng.

Giai đoạn E — Tối ưu và xây dựng hệ thống Bot

Chỉ triển khai hệ thống Bot sau khi mô hình server mới được thử nghiệm và kiểm chứng.

Bot phải là thực thể chung được server quản lý và đồng bộ trên toàn thế giới.

5. Yêu cầu lập kế hoạch của Opus


Đọc toàn bộ bộ bàn giao Fable v0.3, bắt đầu từ START-HERE.md, cùng toàn bộ tài liệu đầu vào của chủ dự án.

Đối chiếu những quyết định cũ với chỉ thị mới. Không tự động kế thừa những nội dung đã bị thay thế.

Khảo sát repository, source code và môi trường thực tế. Phân biệt rõ điều đã kiểm chứng, điều mới suy luận và điều chưa biết.

Đánh giá tính khả thi và rủi ro của việc chuyển đổi server JX1.

Đề xuất kiến trúc kỹ thuật phù hợp, tận dụng hệ thống gốc tối đa.

Đề xuất quy trình Git và cách kết nối repository Private cho Opus, Sonnet và các AI worker.

Đề xuất phân công công việc, tiêu chí nghiệm thu, kế hoạch kiểm thử, quản lý phiên bản và cơ chế bàn giao.

Xác định rõ những việc có thể làm ngay, những việc phải thử nghiệm và những việc cần chủ dự án quyết định.



6. Giới hạn trong giai đoạn lập kế hoạch


Không thay đổi cấu hình server đang chạy.

Không thực hiện thao tác có nguy cơ mất dữ liệu.

Không triển khai các tính năng game trước khi chủ dự án phê duyệt kế hoạch.

Được phép đọc, kiểm kê, phân tích và thực hiện kiểm tra an toàn, không phá hoại.

Mọi kết luận quan trọng phải có bằng chứng hoặc chỉ rõ mức độ chưa xác minh.



7. Kết quả cần bàn giao

Opus phải lập một kế hoạch tổng thể mới, bao gồm:


Kiến trúc và hiện trạng hệ thống JX1.

Báo cáo khả thi chuyển đổi server.

Kế hoạch quản lý account.

Danh mục hoạt động và trạng thái thực tế.

Thiết kế cơ chế hiển thị người chơi theo hoạt động.

Thiết kế hệ thống cấu hình và quản trị.

Lộ trình tối ưu hiệu năng.

Lộ trình xây dựng Bot chung.

Mô hình tổ chức Opus, Sonnet và AI worker.

Quy trình GitHub, đồng bộ, review, kiểm thử và bàn giao.

Các rủi ro, phụ thuộc và quyết định cần chủ dự án phê duyệt.



Đây là giai đoạn lập lại kế hoạch. Sau khi hoàn tất, hãy trình bày kết quả để chủ dự án xem xét. Không tự coi kế hoạch là đã được phê duyệt.

Nguyên tắc cuối cùng: Tận dụng và làm chủ JX1 gốc; giữ chất gameplay JX1; chuyển đổi cơ chế thế giới theo mô hình người chơi thật tương tác với Bot chung; người chơi thật chỉ nhìn thấy nhau trong những hoạt động được chủ động cho phép và giới hạn số lượng.

