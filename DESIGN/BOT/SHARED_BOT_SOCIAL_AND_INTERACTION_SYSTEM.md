# JX1 – SHARED BOT SOCIAL & INTERACTION SYSTEM

**Trạng thái:** GHI NHẬN ĐỊNH HƯỚNG ĐÃ ĐƯỢC NGƯỜI DÙNG XÁC NHẬN  
**Loại tài liệu:** Tài liệu thiết kế ý tưởng / yêu cầu gameplay – chưa phải đặc tả kỹ thuật cuối cùng  
**Phạm vi:** BOT dùng chung trong thế giới JX1, tương tác xã hội, giao dịch, party và hành vi chủ động tìm người chơi.

> Mục đích của tài liệu này là lưu lại định hướng để tham chiếu khi bước vào giai đoạn thiết kế và triển khai BOT. Không tự ý coi các chi tiết chưa được người dùng quyết định là yêu cầu đã chốt.

---

## 1. Định hướng cốt lõi của thế giới JX1

JX1 không vận hành theo mô hình MMORPG truyền thống trong đó người chơi thật nhìn thấy và tương tác trực tiếp với nhau.

- Người chơi thật **không nhìn thấy nhân vật người chơi thật khác** trong thế giới game.
- Người chơi thật **không tương tác trực tiếp với nhau** theo kiểu giao dịch, PK, tổ đội hoặc các hoạt động tương tác nhân vật thông thường.
- Các BOT là những nhân vật tương tác chính mà người chơi gặp trong thế giới.
- BOT tồn tại trong một thế giới chung; nhiều người chơi có thể gặp cùng một BOT.
- Mỗi người chơi vẫn có nhân vật, tài sản, danh vọng, nhiệm vụ, thành tích và tiến trình riêng.
- BOT phải tạo cảm giác như những người chơi thật: có hoạt động, giao tiếp, giao dịch, tham gia party và chủ động tìm hoạt động.

Đây là nguyên tắc kiến trúc gameplay cần được giữ khi thiết kế client, server, hệ thống BOT và QA.

## 2. BOT dùng chung nhưng có quyền tương tác theo từng loại

Không dùng một quy tắc khóa duy nhất cho mọi tương tác. Mỗi loại tương tác có chính sách riêng.

### 2.1 Chat

- Chat có thể diễn ra đồng thời với nhiều người chơi.
- Một BOT có thể có nhiều phiên chat riêng cùng lúc, theo giới hạn và quy tắc game sau này.
- Chat không mặc nhiên chiếm độc quyền toàn bộ BOT.
- Ngoại lệ đã được người dùng xác định: nếu BOT đang ở trong một party, khi người chơi ngoài party chat mật với BOT, BOT từ chối và thông báo:

  **“Tôi đang ở trong một party khác.”**

### 2.2 Giao dịch

- Một BOT chỉ giao dịch với **một người chơi tại một thời điểm**.
- Khi giao dịch đang diễn ra, người chơi khác không thể chiếm cùng BOT để giao dịch đồng thời.
- Khi giao dịch hoàn tất, BOT được giải phóng và có thể giao dịch với người chơi tiếp theo.
- Khi BOT đang chờ giao dịch, BOT có thể chủ động quảng bá trên kênh thế giới để tìm người giao dịch.
- Nội dung quảng bá phải dựa trên vật phẩm thực tế BOT đang sở hữu; không được rao bán vật phẩm không có.

Ví dụ nội dung:
- “Tôi đang có một thanh Đường Môn Phi Đao khá tốt, ai cần mua hoặc đổi đồ thì mật nhé!”
- “Có ít trang bị Ngũ Độc cần thanh lý, ai quan tâm liên hệ tôi.”
- “Đang tìm mua trang bị cấp cao, ai có hàng tốt cứ mật!”

Đây chỉ là ví dụ về phong cách nội dung, không phải danh sách vật phẩm cố định.

### 2.3 Party

- BOT có thể gia nhập party của người chơi.
- Khi BOT đang ở trong party, BOT thuộc trạng thái party đó và không thể gia nhập party khác.
- Người chơi ngoài party không được chiếm BOT thông qua lời mời party khác.
- Khi BOT rời party hoặc người chơi rời đi theo quy tắc party được thiết kế, BOT trở về trạng thái tự do/chờ gia nhập party.
- Ở trạng thái chờ party, BOT có thể chủ động đăng tin trên kênh thế giới để tìm party.

Ví dụ:
- “Có ai muốn lập party đi luyện công không? Tôi đang rảnh!”
- “Ai cần thêm người đi đánh boss thì cho tôi tham gia với nhé!”

Người dùng đã xác định rằng khi BOT rời trạng thái party, BOT trở về trạng thái chờ và có thể tìm người chơi khác để gia nhập party.

## 3. Hành vi xã hội chủ động

BOT không chỉ đứng chờ người chơi nhấn nút. Khi ở trạng thái phù hợp, BOT có thể chủ động tìm hoạt động.

### 3.1 Tìm party

Khi đang chờ party:
- BOT có thể định kỳ gửi tin lên kênh thế giới hỏi người chơi có muốn lập party/đi luyện công/đánh boss hay không.
- Nội dung có thể phụ thuộc vào cấp độ, môn phái, bản đồ, khả năng và mục tiêu của BOT.
- Tránh để mọi BOT gửi cùng một nội dung hoặc cùng một thời điểm, gây spam và làm thế giới thiếu tự nhiên.

### 3.2 Tìm giao dịch

Khi đang chờ giao dịch:
- BOT có thể giới thiệu một số vật phẩm thực tế trong kho đồ.
- BOT có thể tìm người mua, người bán hoặc người muốn trao đổi.
- Nội dung phải nhất quán với inventory, tiền và điều kiện giao dịch thực tế của BOT.
- Tin quảng bá không tự động tạo quyền giao dịch; người chơi vẫn phải bắt đầu tương tác và server kiểm tra trạng thái/điều kiện.

### 3.3 Tính cách và thói quen BOT – định hướng mở rộng

Các ý tưởng được đề xuất để nghiên cứu ở giai đoạn thiết kế:
- BOT thích luyện cấp, thường xuyên tìm party.
- BOT chuyên săn đồ, thường giới thiệu vật phẩm.
- BOT thích giao dịch, chủ động tìm người mua/bán.
- BOT ít nói, chỉ trả lời khi người chơi chủ động liên hệ.
- BOT có lịch hoạt động hoặc khung giờ hoạt động riêng.

Đây là ý tưởng mở rộng, chưa phải yêu cầu đã chốt.

## 4. Mô hình trạng thái: tách nhiều chiều, không dùng một biến duy nhất

Một BOT có thể đồng thời di chuyển, chiến đấu, chat và có trạng thái giao dịch/party riêng. Vì vậy, khi thiết kế kỹ thuật nên tách các nhóm trạng thái thay vì dùng một trường `bot_status` duy nhất.

Các nhóm trạng thái cần xem xét:

| Nhóm | Ví dụ trạng thái / dữ liệu |
|---|---|
| Presence / hoạt động trong thế giới | đứng yên, di chuyển, chiến đấu, bản đồ hiện tại |
| Chat | các phiên chat riêng, có cho phép chat mật hay không |
| Giao dịch | rảnh, đang khóa giao dịch với một người chơi |
| Party | tự do/chờ party, đang ở party nào |
| Social intent | tìm party, tìm giao dịch, không chủ động tìm |
| Interaction history | lịch sử tương tác cần thiết để kiểm soát và ghi nhận |

Đây là gợi ý phân rã khái niệm, chưa phải schema database/API đã chốt.

### 4.1 Nguyên tắc khóa và tính nhất quán

- Khóa giao dịch và quyền gia nhập party phải được kiểm soát ở server.
- Các thao tác chiếm quyền phải xử lý an toàn khi nhiều yêu cầu đến đồng thời.
- Không để hai người chơi cùng chiếm một BOT cho hai giao dịch độc quyền cùng lúc.
- Không để BOT đồng thời thuộc hai party.
- Chat song song không được vô tình ghi đè hoặc chiếm khóa giao dịch/party.
- Khi giao dịch kết thúc, hủy hoặc timeout, trạng thái phải được giải phóng theo quy tắc được thiết kế.
- Khi BOT rời party, trạng thái party phải được cập nhật nhất quán trước khi BOT nhận lời mời mới.

Cần thiết kế thêm xử lý mất kết nối, timeout, crash/restart server và yêu cầu lặp (duplicate request) để tránh BOT bị khóa vĩnh viễn. Cách xử lý cụ thể cần được chốt trong đặc tả kỹ thuật.

## 5. Các kịch bản kiểm thử bắt buộc khi xây dựng hệ thống

Đội QA nhiều LDPlayer cần kiểm thử các tình huống sau. Đây là yêu cầu kiểm thử suy ra trực tiếp từ các quy tắc gameplay đã nêu.

### 5.1 Chat
1. Người chơi A và B chat với cùng BOT đồng thời: cả hai phiên chat được xử lý độc lập.
2. BOT đang trong party của A; người chơi ngoài party B chat mật: BOT từ chối bằng thông báo “Tôi đang ở trong một party khác.”
3. Chat không làm thay đổi sai trạng thái giao dịch hoặc party.

### 5.2 Giao dịch
1. A bắt đầu giao dịch với BOT.
2. B yêu cầu giao dịch cùng BOT trong lúc A đang giao dịch: B bị từ chối.
3. A hoàn tất giao dịch: BOT trở về trạng thái tự do/chờ giao dịch.
4. B có thể giao dịch sau khi BOT được giải phóng.
5. Hủy giao dịch, mất kết nối hoặc timeout không để BOT bị khóa vĩnh viễn.
6. Hai yêu cầu giao dịch đến gần như đồng thời: chỉ một yêu cầu được cấp quyền.

### 5.3 Party
1. BOT đang tự do/chờ và nhận lời mời party.
2. BOT đã ở party A; party B không thể chiếm BOT.
3. Người chơi ngoài party chat mật với BOT đang trong party: BOT trả lời đúng thông báo từ chối.
4. BOT rời party: trở về trạng thái chờ party.
5. BOT có thể quảng bá tìm party khi đang chờ.
6. Hai party mời cùng lúc: server chỉ chấp nhận theo quy tắc ưu tiên được thiết kế, không để BOT thuộc hai party.

### 5.4 Quảng bá thế giới
1. BOT chờ party có thể gửi tin tìm party theo thời gian.
2. BOT chờ giao dịch có thể giới thiệu vật phẩm thực tế trong kho.
3. BOT không quảng bá vật phẩm không sở hữu.
4. Tin nhắn có giới hạn tần suất và nội dung đa dạng để tránh spam.
5. Khi BOT không còn ở trạng thái chờ tương ứng, tin quảng bá cũ phải dừng.

## 6. Nguyên tắc kiểm thử và tải server

Khi kiểm thử nhiều người chơi mô phỏng, phải mô phỏng đúng mô hình JX1:
- Nhiều phiên người chơi thật kết nối cùng server.
- Các phiên không nhìn thấy và không tương tác trực tiếp với nhân vật người chơi thật khác.
- Các phiên có thể gặp cùng các BOT dùng chung.
- Nhiều người có thể chat với một BOT.
- Giao dịch và party tuân theo quyền độc quyền/trạng thái đã nêu.
- Server giữ nhất quán trạng thái BOT và tiến trình riêng của từng người chơi.

Không dùng mô hình MMORPG truyền thống có player-to-player visibility/interaction làm chuẩn kỳ vọng cho JX1.

Nên kết hợp:
- Một số LDPlayer chạy client thật để xác minh UI, hình ảnh và gameplay.
- Virtual Player/Load Test Agent để mô phỏng số lượng phiên lớn hơn khi đã phân tích và xác minh giao thức.
- Đối chiếu hành vi mô phỏng với traffic từ client thật; không coi nhiều kết nối TCP nhàn rỗi là tải người chơi thực tế.

## 7. Những điểm chưa được chốt – cần quyết định ở giai đoạn thiết kế

Không tự ý suy đoán các quy tắc dưới đây:
1. BOT rời party vì lý do nào ngoài việc người chơi chủ động rời đi; xử lý khi party giải tán, leader thoát hoặc thành viên mất kết nối.
2. BOT có thời gian nghỉ/ cooldown giữa hai lần giao dịch hoặc giữa hai party hay không.
3. Khi BOT đang giao dịch, có cho phép chat mật với người khác không; nếu có, nội dung phản hồi thế nào.
4. Khi BOT đang trong party, BOT có được quảng bá giao dịch không.
5. BOT có thể vừa trong party vừa giao dịch với một thành viên party hay không.
6. Quy tắc ưu tiên khi nhiều người cùng mời party hoặc yêu cầu giao dịch.
7. Thời gian và tần suất quảng bá kênh thế giới; giới hạn chống spam.
8. BOT có thể từ chối lời mời party/giao dịch dựa trên cấp độ, môn phái, bản đồ, mục tiêu hoặc tính cách không.
9. BOT có thể cùng lúc tham gia hoạt động nào khác trong khi đang ở party.
10. Chính sách lưu trạng thái và phục hồi sau restart server.

## 8. Nguyên tắc bảo toàn thiết kế

- Người chơi thật không nhìn thấy và không tương tác trực tiếp với người chơi thật khác.
- BOT là nhân vật tương tác chính và được dùng chung trong thế giới.
- Chat hỗ trợ nhiều người chơi đồng thời, trừ quy tắc từ chối chat mật khi BOT đang ở party đã nêu.
- Giao dịch chỉ một người chơi tại một thời điểm; sau khi hoàn tất BOT được giải phóng.
- BOT trong party không nhận tương tác party từ người ngoài; chat mật ngoài party bị từ chối với thông báo cụ thể.
- Khi BOT rời party, BOT trở về trạng thái chờ và có thể chủ động tìm party qua kênh thế giới.
- BOT chờ giao dịch có thể quảng bá các vật phẩm thực tế để tìm người giao dịch.
- Server là nguồn xác thực cuối cùng cho quyền tương tác, giao dịch và party.

---

**Ghi chú sử dụng:** Khi bắt đầu thiết kế BOT, hãy đọc tài liệu này cùng các tài liệu gameplay/server liên quan. Trước khi triển khai, chuyển các quy tắc đã chốt thành đặc tả trạng thái, API, dữ liệu và test case; các mục ở phần 7 phải được hỏi/chốt, không tự suy diễn.
