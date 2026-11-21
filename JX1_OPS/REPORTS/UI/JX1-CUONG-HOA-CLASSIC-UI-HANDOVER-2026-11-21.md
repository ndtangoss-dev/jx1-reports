# BÀN GIAO UI JX1 CLASSIC — CỬA SỔ CƯỜNG HÓA TRANG BỊ

- Ngày ghi nhận: 2026-11-21
- Phạm vi: concept UI, quy tắc thiết kế, asset handoff và kế hoạch tích hợp Cocos V3
- Trạng thái: **CONCEPT ĐÃ ĐƯỢC CHỦ DỰ ÁN DUYỆT; CHƯA TÍCH HỢP ASSET VÀO CLIENT**
- Kho quy trình: `ndtangoss-dev/jx1-reports`, nhánh `jx1-ops`
- Lưu ý: repo này là kho báo cáo/quy trình, không phải repo source Cocos V3.

## 1. Bối cảnh dự án và nguyên tắc nền

Chủ dự án đang phát triển JX1 Cocos V3. Client Cocos V3 hiện tại đang chạy được và phải được giữ làm baseline chuẩn. Claude đã kết nối nút Cường Hóa với chức năng hiện có; tuy nhiên asset gốc không có đủ các thành phần đồ họa để tạo ra giao diện mới theo concept.

Mục tiêu công việc là tạo tài nguyên đồ họa UI và hướng dẫn để Claude tích hợp vào Cocos V3. Đây là thay đổi **presentation/UI**, không phải viết lại gameplay.

Rào chắn bắt buộc:
1. Không sửa trực tiếp baseline đang chạy; làm trên nhánh/cây thử nghiệm riêng, có thể rollback.
2. Không thay đổi server, protocol, packet, logic chọn vật phẩm, công thức cường hóa, xác suất, trừ bạc, tiêu hao nguyên liệu, xử lý thành công/thất bại hoặc dữ liệu nhân vật.
3. Không tự thay thế icon trang bị/vật phẩm gốc nếu có thể tái sử dụng asset thật của JX1.
4. Dữ liệu động (tên vật phẩm, số lượng, bạc, tỷ lệ, thông báo) phải được render bằng Cocos Label/Text, không bake vào ảnh nền.
5. Chỉ nghiệm thu sau khi build và kiểm tra trên LDPlayer14/thiết bị mục tiêu.

## 2. Phong cách thị giác đã được duyệt

Tên phong cách: **JX1 Classic – cổ điển, bám sát client gốc**.

Đặc điểm:
- Nền bảng xanh đen/đen rêu, hoa văn chìm kiểu cổ.
- Viền kim loại cũ, đồng-vàng, hoa văn góc và họa tiết trang trí kiểu JX1.
- Thanh tiêu đề nền đá/xám cổ, chữ vàng sáng, viền tối để dễ đọc.
- Ô vật phẩm vuông, nền tối, viền vàng mảnh; ô đang chọn có viền sáng xanh/lục.
- Đường liên kết nguyên liệu phát sáng vàng.
- Nút thao tác màu vàng đồng, có viền nổi và bóng tối.
- Chữ nhỏ, mật độ thông tin cao, giống MMORPG JX1; không chuyển sang phong cách mobile MMORPG hiện đại, phẳng hoặc tối giản.
- Giữ nguyên HUD, bản đồ và cảnh game phía sau cửa sổ; cửa sổ Cường Hóa phủ lên gameplay như UI JX1.

Không được tự ý làm giao diện quá hiện đại, đổi palette, thay kiểu viền, phóng to khoảng trắng hoặc đổi bố cục đã duyệt.

## 3. Bố cục cửa sổ Cường Hóa đã chốt

### 3.1 Khung tổng thể
Một cửa sổ Cường Hóa lớn nằm trên nền gameplay. Có thanh tiêu đề “CƯỜNG HÓA TRANG BỊ” và nút đóng ở góc trên bên phải.

### 3.2 Khu vực bên trái
- Phía trên có dòng hướng dẫn: “Đặt vào trang bị muốn cường hóa”.
- Ô trang bị chính nằm ở trung tâm phía trên.
- Từ ô trang bị chính tách ra hai nhánh:
  - Bùa May Mắn.
  - Phù Bảo Hộ.
- Tầng bên dưới là ba ô đá nguyên liệu, theo thứ tự trái sang phải:
  - Đá xanh lá.
  - Đá xanh lam.
  - Đá tím.
- Các ô được nối bằng đường liên kết vàng phát sáng. Bố cục phải thể hiện rõ quan hệ từ trang bị chính tới hai vật phẩm hỗ trợ và ba loại đá.
- Phía dưới tầng ba loại đá là bảng thông tin, theo đúng thứ tự:
  1. Nguyên liệu cần.
  2. Cần bạc.
  3. Tỉ lệ thành công.
  4. Chú ý.
- Nút “Cường Hóa” đặt phía dưới bảng thông tin, căn giữa vùng trái.

### 3.3 Khu vực bên phải
- Là **lưới trang bị riêng để chọn món cần cường hóa**, không phải cửa sổ Hành Trang.
- Lưới trang bị nằm bên phải trong cùng cửa sổ Cường Hóa.
- Không thêm tiêu đề/nhãn “Lưới trang bị”.
- Không mở hoặc hiển thị cửa sổ Hành Trang riêng khi cửa sổ Cường Hóa đang mở.
- Ngay bên dưới lưới trang bị là hai vùng hiển thị tiền tệ (hai loại tiền), có icon và số dư.
- Không đưa các nút “Sắp xếp”, “Bày bán” hoặc thanh “Đóng” của cửa sổ Hành Trang vào khu vực này, trừ khi chủ dự án yêu cầu riêng.

### 3.4 Những thứ không thuộc cửa sổ Cường Hóa
- Không có menu chức năng dọc bên trái gồm Cường Hóa/Bảo Hộ/Trang Bị/Phù/May Mắn. Chủ dự án đã đánh dấu yêu cầu bỏ menu này.
- Không có cửa sổ Hành Trang riêng. Ảnh Hành Trang được chủ dự án bật ban đầu chỉ để tham khảo phong cách UI gốc và bố cục.
- Tooltip/thông tin vật phẩm như “Tiếu Ngạo Giang Hồ Lục” là một cửa sổ nổi riêng, có thể đè lên UI khi người chơi rê/chọn vật phẩm; nó **không phải thành phần** của cửa sổ Cường Hóa và không được gộp vào panel Cường Hóa.

## 4. Những lần hiệu chỉnh và kết luận của chủ dự án

1. Concept đầu tiên quá hiện đại, không giống JX1. Chủ dự án yêu cầu bám sát client JX1 thực tế.
2. Chủ dự án gửi ảnh client JX1 Mobile có cửa sổ Hành Trang và tooltip nổi. Đã làm rõ tooltip “Tiếu Ngạo Giang Hồ Lục” là cửa sổ độc lập.
3. Chủ dự án gửi các ảnh UI Cường Hóa nhiều trạng thái. Bố cục cường hóa gốc có trang bị ở trung tâm, vật phẩm hỗ trợ và các loại đá, bảng nguyên liệu/bạc/tỷ lệ/chú ý.
4. Chủ dự án yêu cầu bỏ menu chức năng bên trái; lưới trang bị phải ở bên phải. Cửa sổ Hành Trang không được coi là lưới trang bị.
5. Chủ dự án làm rõ khi bật cửa sổ Cường Hóa thì cửa sổ Hành Trang biến mất; ảnh Hành Trang chỉ để tham khảo giao diện gốc.
6. Chủ dự án duyệt hướng kết hợp: khu vực cường hóa ở trái, lưới chọn trang bị ở phải, tiền tệ đặt ngay dưới lưới, bảng thông tin nguyên liệu/bạc/tỷ lệ/chú ý đặt dưới các ô nguyên liệu.
7. Chủ dự án chốt lại: không cần chữ “Lưới trang bị”; chỉ cần lưới item ở bên phải và tiền tệ bên dưới.

## 5. Asset đã tạo trong phiên

Đã tạo một atlas PNG concept:
- Tên: `JX1_CuongHoa_UI_Atlas.png`
- Kích thước: 1536 × 1024
- Định dạng: PNG RGBA
- SHA-256: `170edfeb7fde4563fd2eebb81a486dae836cab02389773d580d4bd4086f5d98f`

Đã tạo gói ZIP:
- Tên: `JX1_CuongHoa_UI_Asset_Pack.zip`
- Thành phần: atlas PNG và `README_Cocos_Integration.txt`
- SHA-256: `62dc9bdebd65cca99717eec89d4a7c32fadf29210ba1a17c1cd28790dae633b6`

Atlas là **concept asset sheet**, chưa phải Cocos SpriteFrame atlas hoàn chỉnh. Hình minh họa bao gồm khung cửa sổ, vùng nền, khung slot, lưới item, đường liên kết, bảng thông tin, banner, nút, icon tiền tệ và họa tiết. Không mặc định mọi thành phần đã được crop chuẩn hoặc alpha hoàn hảo; phải kiểm tra từng crop ở kích thước gốc.

Hướng dẫn tích hợp:
1. Crop các thành phần thành PNG sprite độc lập; giữ alpha, trim khoảng trong suốt.
2. Tạo Cocos SpriteFrame atlas và file `.plist`/texture tương ứng theo pipeline hiện có của project.
3. Dùng 9-slice/nine-patch cho panel, thanh tiêu đề, nút và slot nếu cấu trúc sprite phù hợp.
4. Tái sử dụng icon trang bị, đá, bùa, phù và vật phẩm thật từ asset Cocos V3 khi tìm thấy. Không dùng icon minh họa trong atlas thay cho icon game thật nếu có asset gốc.
5. Dựng các nhãn và số liệu động bằng Cocos Label/Text.
6. Đảm bảo lưới bên phải và hai vùng tiền tệ bên dưới có thể cập nhật theo dữ liệu inventory/currency thật.
7. Đường liên kết vàng có thể là sprite tĩnh hoặc ghép từ các đoạn ngang/dọc/góc; không để lệch khi scale theo độ phân giải.
8. Không dùng toàn bộ ảnh concept làm một ảnh nền duy nhất. UI phải gồm các thành phần có thể tương tác và cập nhật.

## 6. Cấu trúc thành phần đề xuất

Tên dưới đây là đề xuất kiến trúc, không khẳng định các class này đã tồn tại trong source:
- `EnhancementWindow`: root panel, title bar, close button.
- `EnhancementEquipmentSlot`: slot trang bị chính.
- `LuckyCharmSlot`: slot Bùa May Mắn.
- `ProtectionCharmSlot`: slot Phù Bảo Hộ.
- `CrystalSlotGreen`, `CrystalSlotBlue`, `CrystalSlotPurple`: ba slot đá (hoặc một class MaterialSlot dùng data/config).
- `MaterialConnector`: đường nối vàng giữa các slot.
- `EnhancementInfoPanel`: nguyên liệu cần, bạc cần, tỷ lệ thành công, chú ý.
- `EnhancementActionButton`: nút Cường Hóa.
- `EquipmentSelectionGrid`: lưới trang bị ở bên phải; tên nội bộ, không hiển thị thành tiêu đề UI.
- `CurrencyDisplayA`, `CurrencyDisplayB`: hai vùng tiền tệ ngay dưới lưới.

Các tên trên chỉ là cách chia module để Claude khảo sát và ánh xạ vào kiến trúc thật của Cocos V3. Không tạo class trùng nếu source đã có class tương đương.

## 7. Kế hoạch giao Claude/Codex

### Giai đoạn A — khảo sát (không sửa source)
- Tìm chính xác class/layer/scene đang tạo cửa sổ Cường Hóa.
- Tìm luồng mở/đóng UI và callback của nút Cường Hóa đã được kết nối.
- Tìm cách chọn trang bị, đọc inventory, render item icon và số lượng.
- Tìm logic server/protocol của yêu cầu Cường Hóa; chỉ đọc để bảo toàn.
- Kiểm kê asset frame, font, button, texture, icon hiện có.
- Báo cáo đường dẫn file, class, hàm, dữ liệu và điểm tích hợp cụ thể.

### Giai đoạn B — chuẩn bị asset
- Crop atlas thành sprite PNG riêng.
- Kiểm tra alpha/viền/độ phân giải.
- Tạo SpriteFrame atlas theo đúng pipeline đang dùng.
- So sánh asset mới với screenshot concept và UI gốc.
- Không chỉnh gameplay.

### Giai đoạn C — triển khai presentation
- Tạo cửa sổ theo layout đã duyệt.
- Nối các control vào callback/data binding hiện có.
- Dùng icon item thật.
- Dynamic labels cho số lượng, tiền, tỷ lệ, nguyên liệu, thông báo.
- Không tự tạo lại công thức cường hóa.

### Giai đoạn D — kiểm thử
- Build trên cây thử nghiệm riêng.
- Cài và chạy LDPlayer14.
- Kiểm tra mở/đóng, chọn item, thay item, đủ/thiếu nguyên liệu, tiền, tỷ lệ, bùa/phù, nút Cường Hóa, kết quả thành công/thất bại.
- Kiểm tra không có regression với inventory, equipment, server và các cửa sổ khác.
- Chụp ảnh đối chiếu với concept.
- Chỉ sau khi chủ dự án duyệt mới tính đến việc đưa thay đổi vào baseline.

## 8. Prompt khởi động cho Claude

> Đọc tài liệu `JX1_OPS/REPORTS/UI/JX1-CUONG-HOA-CLASSIC-UI-HANDOVER-2026-11-21.md` trước khi làm. Đây là đặc tả đã được chủ dự án duyệt cho UI Cường Hóa JX1 Classic.
>
> Bước đầu chỉ khảo sát source Cocos V3 và asset; không sửa file. Xác định cửa sổ Cường Hóa hiện có, callback nút đã kết nối, dữ liệu inventory/equipment/currency và luồng protocol. Báo cáo đường dẫn/class/function chính xác.
>
> Giữ nguyên logic cường hóa và server. UI phải theo đúng layout: bên trái là slot trang bị chính, nhánh Bùa May Mắn và Phù Bảo Hộ, ba slot đá, dưới đó là Nguyên liệu cần/Cần bạc/Tỉ lệ thành công/Chú ý và nút Cường Hóa; bên phải là lưới trang bị chọn đồ, không có tiêu đề “Lưới trang bị”, hai vùng tiền tệ đặt ngay dưới lưới. Không menu dọc bên trái, không cửa sổ Hành Trang riêng, không gộp tooltip “Tiếu Ngạo Giang Hồ Lục” vào panel.
>
> Dùng asset atlas được bàn giao làm nguồn crop, nhưng ưu tiên icon game gốc. Tách sprite, tạo atlas Cocos theo pipeline dự án; dynamic text/values phải là Cocos labels. Làm trên nhánh thử nghiệm, baseline giữ nguyên. Chỉ triển khai sau khi chủ dự án duyệt báo cáo khảo sát.

## 9. Phạm vi mở rộng phong cách

Chủ dự án có thể yêu cầu thiết kế thêm các cửa sổ JX1 khác theo cùng phong cách. Khi làm cửa sổ mới, phải tái sử dụng một UI kit chung:
- Palette xanh đen/đen rêu + đồng vàng cổ.
- Cùng ngôn ngữ viền, góc, hoa văn, thanh tiêu đề.
- Cùng style slot, button, tab, tooltip, info panel.
- Cùng quy tắc chữ nhỏ, tương phản cao, mật độ thông tin kiểu JX1.
- Giữ HUD/gameplay phía sau và cách xếp cửa sổ theo client gốc.
- Không tự ý thêm menu hoặc thay đổi semantics khi chưa có yêu cầu.

Mỗi cửa sổ mới cần có: concept được duyệt, layout spec, atlas/sprite source, danh sách trạng thái UI, data bindings, prompt handoff, kiểm thử và rollback.

## 10. Trạng thái hiện tại / việc chưa làm

- [x] Chốt phong cách JX1 Classic.
- [x] Chốt layout Cường Hóa.
- [x] Làm rõ lưới chọn trang bị bên phải khác với Hành Trang.
- [x] Làm rõ tooltip vật phẩm là cửa sổ độc lập.
- [x] Tạo concept atlas PNG và ZIP handoff.
- [x] Lưu quyết định vào Memory.
- [ ] Đưa atlas/ZIP vào kho GitHub.
- [ ] Claude khảo sát source Cocos V3 (chưa thực hiện trong phiên này).
- [ ] Crop sprite/kiểm alpha/tạo plist.
- [ ] Tích hợp UI vào nhánh thử nghiệm.
- [ ] Build và kiểm thử LDPlayer14.
- [ ] Chủ dự án duyệt trước khi đưa vào baseline.

**Cảnh báo độ chắc chắn:** Chưa có source Cocos V3 mở trong phiên này để kiểm chứng class/path/callback; các tên module ở trên chỉ là đề xuất. Không được coi báo cáo này là xác nhận rằng UI đã được tích hợp hoặc build thành công.
