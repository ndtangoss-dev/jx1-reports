# AMOLX-03 — Kết luận nhanh có dùng được làm client JX1 không

Task ID: AMOLX-03-GO-NO-GO-20261115
Executor: Codex CLI trực tiếp, giữ nguyên cấu hình Sol Max hiện tại.
Timebox: tối đa 10 phút cho một lượt. Mục tiêu là kết luận ra quyết định, không phải hoàn thành audit toàn diện.

## Câu hỏi cần trả lời

Source AMOLX tại `C:\JX1\jx1client-axmol-main\jx1client-axmol-main` có thể dùng làm nền để thay client Cocos JX1 hiện tại hay không? Phải phân biệt:
- Có thể tiếp tục phát triển làm client mới.
- Có tương thích protocol với Cocos canonical và JX1 server source.
- Có thể build/chạy/đăng nhập/gameplay ngay ở trạng thái hiện tại.
Không gộp ba ý này thành một kết luận.

## Nguồn/checkpoint

Đọc đúng hai tài liệu:
- `PROMPTS/AMOLX-02-PROTOCOL-AUDIT-20261115.md`
- `TEST_RESULTS/AMOLX-SESSION-HANDOVER-20261115.md`

Checkpoint đã có: khảo sát các luồng login/chọn server/chọn nhân vật/vào game; phát hiện thiếu 9 enum S2C và lệch thứ tự từ vùng `s2c_skillcast`; AMOLX ghi mật khẩu rõ vào `accinfo.ini`; chưa build do thiếu Axmol 2.1.5/`AX_ROOT`; chưa có VM thử nghiệm xác minh. Không làm lại các phần đã có bằng chứng.

## Việc phải làm trong lượt này

Chỉ đọc source, ưu tiên kết luận có tính quyết định:
1. Mở `Source/gamecore/KProtocolDef.h` của AMOLX và header protocol tương ứng trong Cocos canonical cùng server source được chỉ ra trong handover.
2. Tính/đọc giá trị số thực tế tại vùng enum bắt đầu từ `s2c_skillcast`, xác định chính xác điểm lệch đầu tiên và kiểm tra 9 enum S2C bị thiếu có làm dịch ID các mục sau hay không. Không chỉ so tên.
3. Kiểm tra C2S có dấu hiệu lệch nghiêm trọng không; kiểm tra các handler S2C tương ứng trong `KProtocolProcess.cpp` để biết lệnh bị thiếu sẽ bị bỏ qua, xử lý sai hay không được hỗ trợ.
4. Chọn tối đa 2 packet cốt lõi để xác nhận cấu trúc login/Bishop/logic-login từ bằng chứng đã có. Không mở rộng thành rà soát toàn bộ project.
5. Dựa trên các bằng chứng đã có, phân loại các trở ngại thành:
   - Chặn ngay việc tương thích gameplay.
   - Có thể sửa bằng đồng bộ protocol/handler.
   - Chặn build/toolchain.
   - Rủi ro bảo mật cần xử lý trước khi dùng tài khoản thật.

## Quy tắc thực thi

- Giữ nguyên Sol Max. Không kiểm tra hoặc sửa model/provider/reasoning/CLI config.
- Tiếp tục từ checkpoint; không chạy lại phần đã hoàn tất.
- Tập trung giải quyết mục tiêu đến cùng trong 10 phút. Nếu gặp lỗi đọc/tìm file, tự thử cách khắc phục an toàn trong cùng lượt; không dừng để viết báo cáo lỗi trung gian. Không quá 3 lần cho cùng một lỗi.
- Chỉ đọc source. Không sửa/format/generate source; không build, Gradle, cài APK, chạy client/server, kết nối socket, packet capture, truy cập VM hoặc thực hiện network.
- Không sửa Cocos canonical, server source, Main VM hay production.
- Không đọc lại toàn bộ lịch sử hoặc toàn repo. Không thực hiện các việc Dispatcher/Scheduler.
- Không commit từng bước, không báo tiến độ cho từng phát hiện. Hoàn thành lượt rồi tạo đúng một báo cáo tổng hợp cuối.
- Nếu không đủ thời gian cho audit đầy đủ, vẫn phải đưa ra phán quyết thực dụng dựa trên bằng chứng đã xác minh, nêu rõ độ tin cậy và các điểm chưa xác minh; không giả vờ đã kiểm tra phần chưa đọc.

## Đầu ra duy nhất

Tạo:
`TEST_RESULTS/AMOLX-GO-NO-GO-20261115.md`

Báo cáo tiếng Việt, ngắn gọn, bắt buộc có:
1. **Phán quyết ngay đầu báo cáo:** `CÓ THỂ DÙNG LÀM NỀN` / `CHƯA THỂ DÙNG CHO GAMEPLAY` / `KHÔNG NÊN TIẾP TỤC`, có thể chọn nhiều nhãn cho các cấp độ khác nhau.
2. Bảng: hạng mục, bằng chứng, mức độ, kết luận.
3. Điểm lệch enum đầu tiên với giá trị số AMOLX/Cocos/server và tác động dự kiến.
4. Có thể khắc phục không, cần sửa nhóm file nào (chỉ đề xuất, không sửa).
5. Build/runtime: điều kiện còn thiếu và điều gì chưa được kiểm chứng.
6. Lỗi đã gặp trong lượt này, cách đã thử, kết quả; blocker còn lại và hướng xử lý cụ thể.
7. Khuyến nghị bước tiếp theo duy nhất, ưu tiên cao nhất.

Mọi kết luận quan trọng phải kèm file, symbol và line/range nếu lấy được. Phân biệt source-level với runtime; source server không mặc nhiên đại diện executable production.

Sau khi hoàn tất, commit và push duy nhất báo cáo trên lên `ndtangoss-dev/jx1-reports` nhánh `main`. Không stage/commit file khác. Nếu không push được, ghi đúng lỗi và giữ trạng thái chưa push.

## Điều kiện hoàn tất

Trong tối đa 10 phút, giao một phán quyết go/no-go có căn cứ, không chỉ là kế hoạch hoặc danh sách việc cần làm. Báo cáo cuối ghi `DONE`, `PARTIAL` hoặc `BLOCKED`, commit SHA/link nếu có.