# U002 — JX1 Animation Lab: đánh thường hướng 6, 18 khung gốc so với 36 khung nội suy

Ngày: 2026-11-13. Trạng thái: **HOÀN THÀNH MỘT PHẦN, CHƯA KẾT LUẬN VỀ ĐỘ ĐẸP KHI PHÁT LIÊN TỤC.**
Chỉ báo cáo văn bản. Không có ảnh, asset game, binary, APK hay project Unity trong repo này.

## TÓM TẮT
1. Đã dựng màn hình so sánh đồng bộ ORIGINAL 18 khung và UPGRADE 36 khung trong Unity (scene riêng, project riêng cho bản Android). Hai bản chạy chung một đồng hồ, **cùng tổng thời lượng 1,000 s**; bản 36 khung không chậm hơn.
2. 18 khung gốc giữ **nguyên byte** (SHA256 khớp nguồn). 18 khung trung gian tạo bằng **nội suy chuyển động cổ điển viết bằng C# (luồng ảnh quang học + chiếu điểm ảnh)**. Đây **không phải AI**; môi trường không có công cụ AI tạo khung.
3. Kiểm định đa tiêu chí (silhouette, giải phẫu từng bộ phận, vị trí, thời gian, vũ khí) kèm kiểm bằng mắt trên ảnh tĩnh: **16/18 khung PASS, 2/18 FAIL** (idx 11 và idx 27). Ô FAIL giữ nguyên khung gốc, không dùng khung lỗi.
4. Nguyên nhân hai khung FAIL: dữ liệu gốc **nhảy tư thế đột ngột** giữa hai khung liên tiếp (tay/đầu dịch 21–47 px trong một khung, bình thường 1–9 px; tay giơ cao → tay vung ra, thân xoay). Không có chuyển động liên tục để nội suy. Nội suy theo từng bộ phận cũng thất bại (tay và đầu bay rời thân).
5. APK Android thử nghiệm đã build thành công (13,5 MB). **Chưa cài lên điện thoại, chưa đánh giá chuyển động liên tục bằng mắt.** Kết luận về phương pháp nội suy phải chờ người dùng xem trực tiếp trên điện thoại.

## 1. Kết luận tạm về phương pháp (theo tiêu chí của người dùng)
Mục tiêu của dự án không phải đạt 36 khung bằng mọi giá, mà là làm nhân vật JX1 chuyển động đẹp hơn và giữ nguyên thần thái gốc.
- **Cái đã chứng minh được:** ở đoạn chuyển động liên tục (16 vị trí), khung nội suy khớp hình dáng, vị trí chân và trọng tâm với hai khung kề, không có bóng ma, không có màu ngoài bảng màu gốc.
- **Cái chưa chứng minh được:** chuyển động đẹp khi phát liên tục. Mọi kiểm định ở đây là trên ảnh tĩnh và số đo; chưa có người xem chuyển động ở tốc độ thật.
- **Cái đã chứng minh là không làm được:** tại điểm đổi tư thế đột ngột, phương pháp này không tạo được khung đạt chất lượng (2/18 ở động tác này).
- **Khuyến nghị:** không áp dụng phương pháp này cho toàn bộ game ở thời điểm này. Cần biết người dùng đánh giá chuyển động trên điện thoại ra sao; nếu không đạt, chuyển sang nghiên cứu nội suy bằng AI chuyên tạo khung trung gian hoặc nội suy theo từng bộ phận có hiểu tư thế (mục 9). Chưa đo trên animation nào khác ngoài đánh thường hướng 6 tay không, nên không thể ước lượng tỉ lệ điểm nhảy tư thế ở các animation còn lại.

## 2. Dữ liệu đầu vào và bảo toàn khung gốc
- Đối tượng: động tác đánh thường hướng 6, tay không, nhân vật nam, 18 khung. Mỗi khung là ảnh đã ghép 4 bộ phận (thân, tay trái, tay phải, đầu); thiếu vai và tóc vì không có trong gói dữ liệu cho bộ trang phục này. Thứ tự lớp là thứ tự tạm, chưa theo bảng thứ tự vẽ gốc.
- 18 khung gốc đã sao chép sang thư mục riêng `Original18` và so SHA256 từng khung với nguồn: 18/18 khớp. Công cụ sinh khung dừng nếu SHA256 khác, và không ghi đè khung gốc. Ô giữ chỗ cho khung FAIL là bản sao nguyên byte của khung gốc, có so byte.
- Scene và cài đặt build của U001 trước và sau đều có SHA256 giống nhau (`U001_CombatDemo.unity`, `EditorBuildSettings.asset`, `ProjectSettings.asset`).

## 3. Phương pháp tạo 18 khung trung gian
Với mỗi cặp khung (A = khung k, B = khung k+1; cặp cuối: khung đánh cuối → khung đứng cùng hướng, đây là giả định):
1. Tính luồng ảnh hai chiều A→B và B→A bằng Horn–Schunck đa phân giải (4 mức, warp, lọc median) trên đặc trưng gồm alpha và độ sáng.
2. Chiếu từng điểm ảnh của A và B tới vị trí giữa (nửa luồng); điểm chuyển động nhanh hơn che điểm chậm hơn.
3. Hai nguồn trùng nhau và màu gần nhau: lấy màu trung bình rồi **ép về màu gần nhất trong bảng màu của A∪B**; màu khác xa: lấy theo điểm chuyển động nhanh hơn. Không làm mờ chồng ảnh, không sao chép khung, không thêm màu mới.
4. Lấp khe nứt do chiếu, xóa điểm cô lập.
5. **Cắt tỉa về đúng diện tích** (thêm sau vòng kiểm định đầu): bỏ điểm biên chỉ có một nguồn hoặc điểm lấp khe cho đến khi diện tích khung nội suy ≈ trung bình hai khung kề (+1%).
- Lý do bước 5: số đo chuỗi cho thấy khung nội suy lớn hơn hai khung kề khoảng 6% một cách có hệ thống, làm silhouette "phồng lên" theo nhịp 18 Hz khi phát liên tục (số lần đổi chiều diện tích 28/34 so với 5/16 ở bản gốc). Sau bước 5 tỉ lệ diện tích là 1,009–1,010 (trừ khung FAIL) và số lần đổi chiều còn 17/34 (ngẫu nhiên).

## 4. Chẩn đoán idx 11 và idx 27
Dữ liệu từng bộ phận (xuất lại chỉ-đọc từ gói dữ liệu): bước dịch tâm giữa hai khung liên tiếp, đơn vị px.
| Chỗ nhảy | Thân | Tay trái | Tay phải | Đầu |
|---|---|---|---|---|
| Khung gốc 5 → 6 (idx 11) | 10 | 6 | **37** | **21** |
| Khung gốc 13 → 14 (idx 27) | 7 | **47** | 9 | **27** |
| Các cặp còn lại | 0–4 (thường) | ≤ 10 | ≤ 10 | ≤ 10 |
- Hai khung kề là **hai tư thế khác hẳn nhau** (tay giơ cao trên đầu → tay vung ra trước, thân xoay). Không có chuyển động liên tục giữa chúng; đây là chỗ cắt tư thế của hoạt ảnh gốc.
- Đã thử 4 cách sửa trên hai cặp này: (1) nội suy trên ảnh ghép mặc định; (2) tầm bắt chuyển động rộng hơn, làm trơn mạnh hơn; (3) nội suy từng bộ phận rồi ghép; (4) từng bộ phận kèm tầm rộng. Kết quả: cách 1–2 làm rách hình; cách 3–4 làm tay và đầu bay rời thân thành mảnh. Dừng theo quy tắc không thử quá 3 lần cùng một lỗi.
- **Kết luận:** không tạo được khung trung gian đạt chất lượng bằng phương pháp này. Ô được đánh FAIL và giữ nguyên khung gốc (khung 5 và khung 13) để đối chiếu; ảnh thử lỗi lưu ở thư mục riêng `Rejected` để xem, không dùng trong chuỗi phát.
- Việc phép đo màu đã qua ngưỡng ở hai khung này trong vòng kiểm định đầu là **lỗi của bộ kiểm định ban đầu**, không phải bằng chứng khung tốt. Hai khung chỉ bị bắt sau khi thêm kiểm định giải phẫu từng bộ phận và đối chiếu hai phương pháp.

## 5. Kiểm định chất lượng (ngưỡng đặt trước khi chạy, không chỉnh theo kết quả)
| Nhóm | Tiêu chí | Ngưỡng |
|---|---|---|
| S1 Silhouette | IoU(khung giữa, A) và IoU(khung giữa, B) so với IoU(A,B); mảnh rời | không thấp hơn IoU(A,B) quá 0,02; không có mảnh lớn thừa, ≤ 3 mảnh nhỏ thừa |
| S2 Biến dạng | tỉ lệ bbox rộng/cao; tỉ lệ diện tích so với trung bình A,B | 0,90–1,10; 0,90–1,12 |
| A Giải phẫu | từng bộ phận (thân, tay trái, tay phải, đầu): tách rời, lệch tâm, diện tích; đồng thuận hai phương pháp | không tách rời; lệch tâm ≤ 3 px; diện tích 0,75–1,30; IoU hai phương pháp ≥ 0,80 |
| W Vũ khí | cong, nhòe, đổi dạng | **N/A**: đây là đòn tay không, không có lớp vũ khí (vật màu cam ở cổ tay là vòng tay thuộc bộ phận tay) |
| P Vị trí | chân (X,Y), trọng tâm | ≤ 1 px; ≤ 2 px |
| T Thời gian | điểm bóng ma (ngoài 6 px quanh A∪B), lỗ hổng/nhấp nháy, nhịp (Δ(A,giữa)/Δ(giữa,B)), kích thước | ≤ 25 điểm; ≤ 1% diện tích; 0,6–1,65; ±4% (tiêu chí kích thước thêm sau phát hiện hiện tượng "phồng theo nhịp") |
| Mắt | xem ảnh tĩnh 3× của từng khung cùng hai khung kề | không rách, không tách rời, không méo |

**Kết quả từng khung** (idx = vị trí trong chuỗi 36; k = cặp khung gốc):
| k | idx | S | A | W | P | T | Mắt | Kết quả |
|---|---|---|---|---|---|---|---|---|
| 0–4 | 1,3,5,7,9 | PASS | PASS | N/A | PASS | PASS | PASS | **PASS** |
| 5 | 11 | FAIL | FAIL | N/A | PASS | PASS | FAIL | **FAIL** — nhảy tư thế (mục 4) |
| 6–12 | 13,15,…,25 | PASS | PASS | N/A | PASS | PASS | PASS | **PASS** |
| 13 | 27 | PASS | FAIL | N/A | PASS | PASS | FAIL | **FAIL** — nhảy tư thế, tay trái tách thành mảnh rời |
| 14–17 | 29,31,33,35 | PASS | PASS | N/A | PASS | PASS | PASS | **PASS** (k=17 là nội suy tới khung đứng, theo giả định) |

Số đo chính của các khung PASS: diện tích so với trung bình hai khung kề 1,009–1,010; lệch chân X/Y nhỏ hơn 0,5 px; điểm bóng ma 0; lỗ hổng tối đa 0,96%; tỉ lệ nhịp 0,81–1,10; đồng thuận hai phương pháp 0,96–0,99; 0 điểm có màu ngoài bảng màu gốc.

**Giới hạn của kiểm định (phải đọc):**
- Mọi đánh giá bằng mắt là trên **ảnh tĩnh**. Không có đánh giá chuyển động liên tục ở tốc độ thật, nên "giật, rung, nhấp nháy, bóng ma khi phát" mới chỉ được kiểm bằng số đo, chưa bằng mắt.
- Số đo gia tốc tâm của chuỗi bị nhiễu do làm tròn toạ độ khoảng 0,3 px, nên không dùng làm bằng chứng mượt hay không mượt. Chuỗi 36 khung bỏ các cửa sổ gần ô FAIL: gia tốc tâm X 632, Y 486 px/s²; bản gốc 18 khung: X 1388, Y 323.
- Tại ô FAIL, hai khung liên tiếp giống hệt nhau (khung giữ), tức đòn đánh khựng 1/36 s hai lần trong chuỗi.
- Nhân vật thiếu vai và tóc nên "thần thái" so với bản gốc đầy đủ chưa đánh giá được.
- Khung nội suy cuối (về khung đứng) dựa trên giả định về khung đích.

## 6. Màn hình so sánh đồng bộ
- Hai vùng cạnh nhau (ORIGINAL 18 / UPGRADE 36), cùng nền, cùng điểm đặt chân, cùng kích thước và hướng quay; có đường kẻ chân và trục.
- Điều khiển: Play/Pause, Restart, tốc độ, kéo thanh thời gian, tiến/lùi 1 khung (một bước = 1/36 thời lượng), zoom (thanh trượt, pinch, chuột lăn), chọn vùng phóng to, Overlay (đỏ = bản gốc, lục lam = bản nâng cấp, trắng = trùng), hiển thị khung hiện tại và thời gian, lặp, bật/tắt xem khung nội suy lỗi.
- Giao diện thích ứng điện thoại: ngang = bảng điều khiển bên phải; dọc = bảng ở dưới (hai nhân vật xếp dọc); nút cao 42 dp; ưu tiên chế độ ngang khi khởi động, có nút đổi Auto/Ngang/Dọc.
- Kiểm chứng Play Mode tự động: 0 lỗi, 0 cảnh báo, các phép thử đạt: ô FAIL giữ khung gốc; bước khung; thời lượng 1× = 1,000 s; tốc độ 2× = 0,500 s; lặp 2 vòng không lỗi; hai bản kết thúc cùng thời điểm; bố cục 12 kích thước màn hình (6 ngang, 6 dọc) không ô nào ra ngoài màn hình, không nút chồng nhau, nút ≥ 32 dp. Phép thử bố cục phát hiện một lỗi thật (nút Tốc độ/Zoom tràn khỏi màn hình ngang) và đã sửa.
- **Chưa kiểm chứng:** hình dạng thật của giao diện IMGUI (chế độ tự động không chụp được lớp giao diện), font tiếng Việt trên điện thoại, thao tác chạm thật, pinch-zoom thật. Cần xem trên máy.

## 7. Bản Android thử nghiệm
- Dùng **project Unity riêng**, không động tới U001: cấu hình riêng (IL2CPP, ARM64, OpenGL ES 3, API tối thiểu 23, API đích tự động, ký bằng khóa debug, xoay tự do).
- Unity có sẵn đủ Android Build Support, SDK, NDK (r27.2), OpenJDK 17; **không cài thêm gì**.
- Kết quả build: thành công, 0 lỗi, 0 cảnh báo, thời gian khoảng 3 phút. APK 13.502.268 byte (13,5 MB), gói `com.jx1lab.animlab`, một kiến trúc `arm64-v8a`, API đích 36 (kiểm bằng aapt2).
- APK nằm ở máy nghiên cứu, **không đưa lên repo này**. Chưa cài lên điện thoại, chưa chạy thử trên máy thật.
- Thiết bị thử của người dùng: Xiaomi 13T Pro (Android, kiến trúc arm64 phù hợp). Cài bằng cách cho phép cài ứng dụng từ nguồn không rõ cho ứng dụng dùng để mở file; HyperOS có thể cảnh báo "Play Protect", chọn tiếp tục cài. Hướng dẫn chi tiết nằm ở máy nghiên cứu.
- Chuyển file sang điện thoại qua mạng riêng Tailscale đã được chuẩn bị (máy chủ HTTP chỉ nghe trên giao diện Tailscale, chỉ nhận kết nối từ điện thoại), **chưa chạy**, chờ người dùng duyệt mở cổng.

## 8. Bảo vệ dữ liệu
- Không sửa source Cocos, PAK gốc, asset gốc, server, database. Không commit source game. Không đẩy ảnh, asset, binary lên repo công khai này.
- Khung gốc không bị sửa hay ghi đè. Khung nội suy lỗi được chuyển sang thư mục riêng, không xóa.
- Báo cáo này không chứa mật khẩu, token, khóa, địa chỉ IP riêng, thông tin tài khoản.

## 9. Việc tiếp theo (theo hướng người dùng nêu)
1. Người dùng cài APK lên Xiaomi 13T Pro, xoay ngang, xem chuyển động liên tục hai bản cạnh nhau và overlay; ghi nhận giật, rung, nhấp nháy, bóng ma, "thần thái" so với bản gốc. Kết quả này quyết định có tiếp tục nội suy cổ điển hay không.
2. Nếu không đạt: nghiên cứu (a) mô hình AI nội suy khung (loại RIFE/FILM) chạy trên GPU NVIDIA của máy nghiên cứu, trên **từng bộ phận riêng** rồi ghép theo bảng thứ tự vẽ gốc, ép màu về bảng màu gốc; (b) nội suy theo từng bộ phận có hiểu tư thế (khớp, xoay) thay cho luồng ảnh điểm ảnh; (c) vẽ tay hoặc dựng khung chủ chốt riêng tại các chỗ nhảy tư thế. Cài môi trường AI cần tải từ Internet nên phải được người dùng duyệt trước.
3. Trước khi mở rộng: thêm vai và tóc, áp bảng thứ tự vẽ gốc cho đủ 8 hướng, đo số điểm nhảy tư thế ở các animation khác để biết nội suy tự động áp dụng được cho bao nhiêu phần trăm animation.

## 10. Dựng lại (máy nghiên cứu)
Sinh khung → dựng scene → kiểm chứng → kiểm định chất lượng → chốt kết quả, mỗi bước là một hàm Editor chạy bằng Unity batchmode; công cụ xuất bộ phận là một script Python chỉ-đọc. Chi tiết lệnh và đường dẫn nằm ở máy nghiên cứu (`D:\JX1_Unity_U001_work\animlab\ANIMLAB_REPORT.md`).
