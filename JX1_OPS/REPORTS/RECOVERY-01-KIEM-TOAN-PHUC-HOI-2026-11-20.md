# RECOVERY-01 — Kiểm toán và chuẩn hóa bàn giao/phục hồi ngữ cảnh A/B

- Ngày kiểm tra: 20/11/2026
- Nhánh kiểm tra: `jx1-ops`
- Phạm vi: tài liệu trạng thái, hàng đợi, hộp thư và chỉ dẫn phục hồi; chỉ đọc GitHub.
- Trạng thái: `OPEN` — mới ghi nhận kiểm toán, chưa vá quy trình, chưa thử khôi phục phiên mới.
- An toàn: không sửa mã nguồn game, cấu hình, hook, worker, VM hoặc tiến trình đang chạy.

## 1. Kết luận điều hành

Có đủ tài liệu nền để lưu trạng thái A/B, nhưng chưa có bằng chứng kiểm thử đầu-cuối cho thấy một phiên mới có thể phục hồi đúng trạng thái thực tế mà không làm lại việc đã xong hoặc tiếp tục từ ghi chú lỗi thời.

Các lỗi được xác nhận dưới đây là lỗi tài liệu/liên kết/trạng thái. Chưa được coi là bằng chứng hệ thống runtime hoặc hook phục hồi đang hỏng.

## 2. Phát hiện

### REC-01 — Chỉ dẫn tới sổ đo cường hóa chưa đủ rõ

- `JX1_OPS/DESIGN/TINH-NANG/CUONG-HOA.md` có tồn tại; đây là tài liệu thiết kế tính năng.
- Kết quả đo runtime #327/#328 và các thí nghiệm liên quan được ghi rải rác trong `JX1_OPS/STATE/DANG-LAM.md` và `JX1_OPS/HOP-THU/A-B.md`.
- Trong các nội dung đã kiểm tra, chưa xác định được một sổ đo runtime độc lập, chuẩn hóa, có chỉ dẫn nguồn duy nhất.
- Vì vậy không được ghi rằng file `CUONG-HOA.md` hoàn toàn không tồn tại. Vấn đề chính là phân biệt tài liệu thiết kế với bằng chứng nghiệm thu và chuẩn hóa đường dẫn tới dữ liệu đo.

**Mức độ:** Cao — có thể khiến phiên mới đọc nhầm tài liệu thiết kế thành kết quả kiểm thử.

### REC-02 — Trạng thái bàn giao giữa các file không đồng bộ

- `STATE/DANG-LAM.md` chứa nhiều mục lịch sử theo thời gian, gồm cả trạng thái và hướng xử lý cũ.
- `HOP-THU/TU-SONNET-B.md` có ghi đã đọc đến #B-075, nhưng các đoạn mô tả hàng đợi/trạng thái phía dưới vẫn chứa trạng thái cũ như B-050/B-051 chờ A, trong khi thư #B-072..#B-075 đã thay đổi phạm vi SC-002.
- `HOP-THU/CHO-SONNET-B.md` ghi các chỉ thị nối tiếp nhau, trong đó một số chỉ thị cũ đã bị thay thế hoặc đính chính bởi chỉ thị sau. Phải áp dụng nguyên tắc quyết định mới hơn thắng, đồng thời giữ lịch sử để truy nguyên.
- Đây là độ lệch tài liệu đã quan sát được; chưa xác minh trạng thái tiến trình/worktree thực tế của A/B.

**Mức độ:** Cao — có nguy cơ giao trùng, làm lại hoặc tiếp tục nhầm đầu việc.

### REC-03 — Nhãn trạng thái chưa đủ thể hiện mức xác minh

Trong các ghi chú có cách dùng như XONG, PARTIAL, CHỜ, CHƯA CHẠY, CHƯA KIỂM và CHỜ A. Nếu chỉ đọc nhãn rút gọn hoặc một file riêng lẻ, dễ hiểu nhầm “đã viết/build” thành “đã chạy và nghiệm thu”.

**Mức độ:** Cao — có nguy cơ coi kết quả chưa kiểm chứng là hoàn tất.

### REC-04 — Chưa có kiểm thử phục hồi đầu-cuối được ghi nhận

Tài liệu vận hành có quy trình `/tiep-tuc` và thứ tự đọc, nhưng trong phạm vi lần kiểm toán này chưa tìm thấy biên bản kiểm thử phiên mới thực hiện đủ chuỗi: đọc nguồn chuẩn → đối chiếu Git/worktree/runtime → xác định task hiện hành → chứng minh không lặp bước đã xong.

**Mức độ:** Cao — chưa thể kết luận cơ chế phục hồi hoạt động tốt chỉ từ việc có hook hoặc file bàn giao.

## 3. Nguồn đã kiểm tra

- `JX1_OPS/README.md`
- `JX1_OPS/STATE/HANG-DOI-VIEC.md`
- `JX1_OPS/STATE/HANG-DOI-VIEC-B.md`
- `JX1_OPS/STATE/DANG-LAM.md`
- `JX1_OPS/HOP-THU/CHO-SONNET-B.md`
- `JX1_OPS/HOP-THU/TU-SONNET-B.md`
- `JX1_OPS/HOP-THU/A-B.md`
- `JX1_OPS/STATE/DO-HIEU-QUA-QUY-TRINH.md`
- `JX1_OPS/TASKS/BACKLOG.md)
- `JX1_OPS/DESIGN/TINH-NANG/CUONG-HOA.md)

## 4. Hướng cải thiện đề xuất

1. Tạo một checkpoint ngắn cho mỗi Sonnet, mỗi lần chỉ có một trạng thái hiện hành, gồm: task ID, trạng thái, người giữ việc, worktree/branch, commit gần nhất, tiến trình đang chạy, việc đã xác minh, việc chưa xác minh, lệnh/bước tiếp theo và phụ thuộc.
2. Giữ hộp thư append-only làm lịch sử; không dùng thư cũ làm trạng thái hiện tại nếu đã có chỉ thị mới hơn. Checkpoint phải trỏ tới thư/quyết định làm căn cứ.
3. Chuẩn hóa trạng thái task tối thiểu: `READY`, `RUNNING`, `BLOCKED`, `PARTIAL`, `DONE_UNVERIFIED`, `DONE_VERIFIED`, `CANCELLED`. Chỉ dùng `DONE_VERIFIED` khi có bằng chứng nghiệm thu phù hợp.
4. Tách tài liệu thiết kế khỏi nhật ký đo runtime. Tạo sổ nghiệm thu cường hóa riêng hoặc mục lục đo lường rõ ràng; mỗi kết quả phải có ID test, môi trường, phiên bản APK/EXE, bước tái hiện, số đo, ảnh/log và trạng thái xác minh.
5. Thêm kiểm tra liên kết trước khi bàn giao: mọi đường dẫn được nhắc phải tồn tại; phân loại rõ thiết kế / báo cáo / bằng chứng / checkpoint.
6. Thực hiện diễn tập phục hồi trên phiên mới theo chế độ chỉ đọc trước. Không sửa hook, prompt, queue, cấu hình hoặc worker trong lúc diễn tập baseline.

## 5. Tiêu chí nghiệm thu RECOVERY-01

- [ ] A và B mỗi bên có checkpoint hiện hành, không mâu thuẫn với task/hộp thư mới nhất.
- [ ] Mọi task đang làm có owner, trạng thái, branch/worktree và commit căn cứ.
- [ ] Mọi kết luận runtime có liên kết tới bằng chứng đo cụ thể.
- [ ] Các đường dẫn trong chỉ dẫn bàn giao đều tồn tại và đúng loại tài liệu.
- [ ] Phiên mới phục hồi đúng việc tiếp theo, không lặp việc đã xác minh xong và không bỏ qua việc đang chạy.
- [ ] Diễn tập có biên bản gồm thời gian phục hồi, lỗi phát hiện, bước bị lặp/bỏ sót và kết quả đạt/không đạt.

## 6. Ranh giới

Đây là đề xuất cải thiện dựa trên kiểm toán tài liệu. Chưa được phép tự động sửa hook, prompt, quy trình vận hành, trạng thái worker hoặc chạy lại task. Mọi thay đổi vận hành chỉ thực hiện theo quy trình và quyền phê duyệt hiện hành trong `QUY-TAC-VAN-HANH.md`.

## 7. Trạng thái lần kiểm toán

`DOCUMENT_AUDIT_ONLY` — đã đọc tài liệu GitHub; chưa truy cập runtime Windows/Claude Code, chưa kiểm worktree/worker trực tiếp, chưa chạy diễn tập phục hồi.
