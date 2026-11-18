TÓM TẮT 1: [NGUỒN] [THẤY] Client bản A dành 24 chỗ cho các phần hình. Luồng cập nhật trang bị duyệt 5 nhóm, mỗi phần có thể có hình nền và hình hiệu ứng. (`G/KNpcResNode.h:23–25`, `G/KNpcRes.cpp:1705–1733`)
TÓM TẮT 2: [NGUỒN] [THẤY] Khi vẽ người, client chọn thứ tự theo động tác, hướng và khung ảnh. Dòng riêng của khung được ưu tiên hơn dòng theo hướng. (`G/KNpcResNode.cpp:1390–1474`)
TÓM TẮT 3: [NGUỒN] [THẤY] Bảng loại nhân vật trong `settings/npcres` chỉ tới bảng bộ phận, hai bảng động tác theo vũ khí và bảng INI thứ tự vẽ. (`G/CoreUseNameDef.h:30–35`, `G/KNpcResNode.cpp:69–82,319–369`)
TÓM TẮT 4: [NGUỒN] [TÀI LIỆU] Đã có bảng nữ cho 8 hướng thường dùng và 45 mục động tác. Mục INI thực tế khi đi bộ, chạy, đánh hoặc cưỡi vẫn chưa chốt. (`BANG-THU-TU-VE.md:19–25,169–209`)
TÓM TẮT 5: [CHƯA KIỂM] Không chạy build, exe hoặc VM. Kết quả giới hạn ở mã client trên đĩa và các tài liệu được giao. (`JX1_OPS/TASKS/SO-01.md:18–29`)

# SO-01 — Sổ tay nhân vật và bộ phận

Loại: tổng hợp

Chủ đề: Các phần hình nhân vật, cách chồng hình và nơi tra dữ liệu.

Từ khóa: nhân vật, bộ phận, sprite, trang bị, thứ tự vẽ, NPCRes, LineK, 动作贴图顺序表

Trạng thái: DONE (đủ phạm vi sổ tay và đối chiếu tĩnh mã client bản A).

Độ phủ: 3/3 chủ đề được giao và 4/4 tài liệu nguồn.

Liên quan: [Kiểm kê K-02](../REPORTS/K-02-nhan-vat.md), [Quy luật vẽ bộ phận](QUY-LUAT-VE-BO-PHAN.md), [Bảng thứ tự vẽ](BANG-THU-TU-VE.md), [Mục lục tri thức](MUC-LUC-TRI-THUC.md).

Cần tôi quyết định: không.

```mermaid
flowchart LR
  A["Trạng thái, vũ khí, có cưỡi ngựa?"] --> B["Chọn động tác tài nguyên"]
  C["Bảng bộ phận và trang bị"] --> D["Chọn ảnh cho từng phần"]
  B --> D
  B --> E["Tra INI theo động tác, hướng, khung ảnh"]
  D --> E
  E --> F["Bản VN có thể đổi chỗ mã 8 và 9"]
  F --> H["Gửi ảnh các phần theo thứ tự"]
```

## Phạm vi và độ phủ

| Phần cần hiểu | Độ phủ | Mở tới nguồn |
|---|---|---|
| Nhân vật gồm những phần nào | Đã phủ. [THẤY] Sức chứa và các nhóm được cập nhật. [TÀI LIỆU] Sơ đồ mã phần. | `G/KNpcResNode.h:23–25`, `G/CoreUseNameDef.h:8–24`, `K-02-nhan-vat.md:56–62` |
| Các phần chồng lên nhau ra sao | Đã phủ. [THẤY] Luật chọn thứ tự và gửi ảnh. [TÀI LIỆU] Tám hướng mặc định nữ và bảng theo động tác. | `G/KNpcResNode.cpp:1390–1474`, `V:205–214,460–493`, `BANG-THU-TU-VE.md:169–209` |
| Dữ liệu ở đâu | Đã phủ. [THẤY] Tên bảng và đường dẫn logic mà client mở. [TÀI LIỆU] Vị trí đã kiểm kê. | `G/CoreUseNameDef.h:29–50`, `G/KNpcResNode.cpp:69–82,315–369,1201–1216`, `K-02-nhan-vat.md:29–41` |

**Cách đọc nguồn.** **[THẤY]** là đã mở và đối chiếu mã thật. **[TÀI LIỆU]** là kết quả dẫn lại. **[CHƯA KIỂM]** là phần còn thiếu dữ liệu hoặc chưa quan sát khi game chạy. `G/` là `D:/JX-build/qh9A/Classes/gamecore/`. `V` là `D:/JX-build/qh9A/Classes/vn/gamecore/KNpcResVN.cpp`. Tên các tài liệu rút gọn trỏ tới bốn liên kết ở trên. Mã Hán dưới đây được đọc bằng CP936 (GBK) ở nguồn client. Hai tên INI nam và nữ được dẫn lại dưới dạng Unicode.

## Giải mã tên

| Tên gốc | Mã hóa | Chữ đúng và nghĩa tiếng Việt | Nguồn file:dòng |
|---|---|---|---|
| `人物类型.txt` | GBK (CP936) | 人物类型.txt, bảng loại nhân vật | [THẤY] `G/CoreUseNameDef.h:30` |
| `部件说明文件名` | GBK (CP936) | 部件说明文件名, tên bảng mô tả bộ phận | [THẤY] `G/KNpcResNode.cpp:77` |
| `资源文件路经` | GBK (CP936) | 资源文件路经, đường dẫn tệp tài nguyên | [THẤY] `G/KNpcResNode.cpp:70` |
| `信息.txt` | GBK (CP936) | 信息.txt, hậu tố bảng thông tin ảnh | [THẤY] `G/KNpcResNode.cpp:119–125` |
| `武器行为关联表1` / `武器行为关联表2` | GBK (CP936) | Bảng nối vũ khí với động tác, lần lượt cho trường hợp không cưỡi và có cưỡi ngựa | [THẤY] `G/KNpcResNode.cpp:319–359,592–605` |
| `动作编号表.txt` | GBK (CP936) | 动作编号表.txt, bảng đánh số động tác | [THẤY] `G/CoreUseNameDef.h:50`, `G/KNpcResList.cpp:40–45` |
| `动作贴图顺序表` / `人物贴图顺序表` | GBK trong mã / tên Hán trong tài liệu UTF-8 | Cột tên bảng thứ tự vẽ. Mã bản A đọc tên thứ nhất. Tài liệu quy luật dùng tên thứ hai. | [THẤY] `G/KNpcResNode.cpp:365–369`; [TÀI LIỆU] `QUY-LUAT-VE-BO-PHAN.md:44` |
| `女主角贴图顺序表.ini` / `男主角贴图顺序表.ini` | Tên Hán trong tài liệu UTF-8, mã gốc trên đĩa chưa kiểm | Bảng thứ tự vẽ nhân vật nữ / nam | [TÀI LIỆU] `MUC-LUC-TRI-THUC.md:8`, `BANG-THU-TU-VE.md:33–39,161–167` |

## Sắp theo cấu trúc game

### Bộ phận → phần nhỏ → lớp ảnh

[THẤY] Mỗi bộ phận lớn chứa tối đa bốn phần nhỏ. Khi mở bảng bộ phận, client chỉ đếm những ô có tên. Khi cập nhật trang bị, mã duyệt năm nhóm đã đặt tên. Bảng dưới giữ cách gọi nhóm và mã của tài liệu cũ. (`G/KNpcResNode.h:23–25`, `G/KNpcResNode.cpp:89–104`, `G/CoreUseNameDef.h:8–16`, `G/KNpcRes.cpp:1705–1713`, `QUY-LUAT-VE-BO-PHAN.md:7–16`)

| Bộ phận | Mã phần | Độ chắc |
|---|---|---|
| Mũ, đầu | 0–3 | [THẤY] Nhóm thứ nhất trong mã. `G/CoreUseNameDef.h:8–15`, `G/KNpcRes.cpp:1708–1712` |
| Áo, thân | 4–7 | [THẤY] Nhóm thứ hai. `G/CoreUseNameDef.h:8–15`, `G/KNpcResNode.cpp:95–101` |
| Vũ khí | 8–11 | [THẤY] Nhóm thứ ba. `G/CoreUseNameDef.h:8–15`, `G/KNpcRes.cpp:1708–1712` |
| Ngựa | 12–15 | [THẤY] Nhóm thứ tư. `G/CoreUseNameDef.h:8–15`, `G/KNpcRes.cpp:1708–1712` |
| Phi phong | 16–19 | [THẤY] Nhóm thứ năm. Luồng cập nhật cần phần có tên và mã trang bị lớn hơn 0. `G/CoreUseNameDef.h:8–15`, `G/KNpcRes.cpp:1715–1726` |
| Cánh | 20–23 | [TÀI LIỆU] Đây là khoảng gắn với cánh trong sơ đồ cũ. Mã có chú thích cánh ở ô 20. [CHƯA KIỂM] Cánh được đưa lên hình bằng nhánh nào. `K-02-nhan-vat.md:58`, `G/KNpcResNode.cpp:95–101`, `G/KNpcRes.cpp:1708–1712` |

[THẤY] Mỗi phần có thể có lớp hình nền (`BASE`) và lớp hiệu ứng (`EFFECT`). Trong lượt vẽ thân nhân vật, client đi lần lượt qua các mã phần đã xếp và gửi hình nền trước hình hiệu ứng của từng phần. Lớp thiếu hình được bỏ qua. Bóng, nếu bật, đứng trước các phần thân trong danh sách này. (`G/CoreUseNameDef.h:20–24`, `V:435–493`)

[THẤY] Nhân vật ghép nhiều phần dùng bảng thứ tự riêng. NPC thuộc loại thường có lối tắt dùng một mã phần mặc định. (`G/KNpcResNode.cpp:61–68,612–630`)

### Động tác → hướng → khung ảnh

1. **[THẤY] Chọn động tác tài nguyên.** Khi vẽ, client đưa trạng thái hiện tại vào `SetDoing`. Loại vũ khí ở lớp nền và cờ có cưỡi ngựa quyết định ô cần tra cho nhân vật ghép hình. Ví dụ, trạng thái đi bộ là 3 khi chiến đấu hoặc 4 khi bình thường. Mã còn phải qua bảng liên kết vũ khí và bảng đánh số động tác mới ra mục INI. (`G/KNpc.cpp:2891–2898,6096–6097`, `G/KNpc.h:104–116,824`, `G/KNpcRes.cpp:1656–1665,1684–1698`, `G/KNpcResNode.cpp:315–359,592–605,692–722`)
2. **[THẤY] Chọn thứ tự cho khung đang vẽ.** `LineK` là một dòng dành cho khung cụ thể. Số đầu dòng là số khung tính trên cả dãy ảnh gồm nhiều hướng. Client đọc `Line1`, `Line2`… đến số đầu tiên bị thiếu. Nếu trùng số khung, dòng mang K nhỏ hơn được dùng. Trong nhánh có tiến độ khung, hàm vẽ cập nhật hướng và số khung theo từng ảnh hiện hữu rồi chuyển cặp cuối cùng vào hàm tra bảng. (`G/KNpcResNode.cpp:1271–1292,1363–1371,1422–1435,1452–1465`, `V:36–70,205`)
3. **[THẤY] Dùng dòng theo hướng khi không có dòng khớp khung.** Client lấy `DirN` riêng của động tác nếu có, sau đó dùng dòng cùng hướng trong `DEFAULT` cho chỗ thiếu. Mã đọc `Dir1` tới `Dir16`. Tài liệu dùng tám hướng từ 0 đến 7, tương ứng `Dir1` đến `Dir8`. (`G/KNpcResNode.cpp:21,1238–1267,1320–1356,1404–1414,1438–1474`; [TÀI LIỆU] `BANG-THU-TU-VE.md:45,173–184`)
4. **[THẤY] Gửi ảnh đi vẽ.** Bản VN có thể đổi chỗ mã 8 và 9 sau khi tra INI. Điều kiện là công tắc A3a bật theo tên gọi của tài liệu, hướng từ 0 đến 3, nhân vật không cưỡi và chuỗi có cả hai mã. Mã áp dụng theo các điều kiện này cho mọi động tác. Sau đó hàm duyệt danh sách theo thứ tự và gửi các ảnh có tên. (`V:205–217,460–493`; [TÀI LIỆU] `BANG-THU-TU-VE.md:70`)

### Bảng nữ và nam để tra

[TÀI LIỆU] Đây là tám dòng `DEFAULT` của bảng nữ do U-03 trích, trước bước đổi chỗ 8 và 9. Tài liệu cũ ghi cùng các chuỗi cho mẫu nữ đứng `act=38`. Chuỗi đọc từ trái sang phải theo thứ tự gửi hình đi vẽ. Chẳng hạn, ở hướng trái mã vũ khí 9 đứng trước mã áo 4, còn ở hướng phải mã 9 đứng sau mã 4. ([Bảng đầy đủ theo động tác](BANG-THU-TU-VE.md#9-bảng-đầy-đủ-từng-hành-động-nữ), `BANG-THU-TU-VE.md:39–45,119–125,169–209`, `QUY-LUAT-VE-BO-PHAN.md:20–35`)

| Hướng | Khóa | Thứ tự hình | Nguồn [TÀI LIỆU] |
|---|---|---|---|
| 0 xuống | `Dir1` | `14,16,13,1,4,9,7,5,6,12,8,0` | `BANG-THU-TU-VE.md:175` |
| 1 xuống trái | `Dir2` | `14,16,13,9,7,4,1,5,12,6,8,0` | `BANG-THU-TU-VE.md:176` |
| 2 trái | `Dir3` | `9,7,12,13,14,5,16,4,1,0,6,8` | `BANG-THU-TU-VE.md:177` |
| 3 lên trái | `Dir4` | `9,7,12,13,5,14,16,4,1,0,8,6` | `BANG-THU-TU-VE.md:178` |
| 4 lên | `Dir5` | `12,13,8,6,5,14,16,4,1,0,7,9` | `BANG-THU-TU-VE.md:179` |
| 5 lên phải | `Dir6` | `8,6,12,13,5,14,16,4,1,0,9,7` | `BANG-THU-TU-VE.md:180` |
| 6 phải | `Dir7` | `8,6,12,13,14,5,16,4,1,0,9,7` | `BANG-THU-TU-VE.md:181` |
| 7 xuống phải | `Dir8` | `14,16,13,4,1,8,6,5,12,0,9,7` | `BANG-THU-TU-VE.md:182` |

[TÀI LIỆU] Bảng nữ có 45 mục động tác, với các họ tên như `Free`, `MeleeW`, `RangeW`, `DoubleW`, `Ride`. Mỗi dòng dữ liệu mang 12 mã phần. Ví dụ, `FreeRun` có `Line11` nhưng thiếu `Line10`, nên bộ nạp dừng trước `Line11`. [CHƯA KIỂM] Động tác nào trong bảng được bản cài dùng cho từng loại vũ khí, và mỗi lúc có bao nhiêu phần hình thật sự được vẽ. (`BANG-THU-TU-VE.md:21–25,39–43,59–68,101–111,205–209,768–769`)

[TÀI LIỆU] Bảng nam được mô tả là chỉ có `DEFAULT`. [THẤY] Nếu đúng như mô tả, các động tác dùng thứ tự mặc định của từng hướng. [CHƯA KIỂM] Nội dung file nam và từng dòng hướng. (`BANG-THU-TU-VE.md:161–167`, `G/KNpcResNode.cpp:1249–1256,1404–1414`)

### Dữ liệu ở đâu

| Cần tìm | Tra ở đâu |
|---|---|
| Nhân vật dùng bảng nào? | [THẤY] Mở hàng tương ứng trong `settings/npcres/人物类型.txt`. Tại đây client lấy tên bảng bộ phận, hai bảng nối vũ khí với động tác, thư mục ảnh và tên INI. Các tên bảng được ghép với `settings/npcres`. `G/CoreUseNameDef.h:30–35`, `G/KNpcResNode.cpp:47–82,319–369,1201–1214` |
| Động tác số mấy và tên gì? | [THẤY] Tra bảng tương ứng với vũ khí và tình trạng cưỡi, rồi đối chiếu `settings/npcres/动作编号表.txt`. Mã lấy chỉ số dòng dữ liệu từ 0 và bỏ qua hàng tiêu đề. `G/CoreUseNameDef.h:50`, `G/KNpcResList.cpp:40–45`, `G/KNpcResNode.cpp:319–359,692–722` |
| Ảnh của mũ, áo, vũ khí nằm ở đâu? | [THẤY] Bảng của mỗi phần và lớp tra theo trang bị và động tác để lấy tên SPR. Client ghép tên với đường dẫn ảnh, đọc bảng thông tin đi kèm để lấy tổng số khung, hướng và khoảng nhịp. Bảng nền thường có cặp `.txt` và `信息.txt`, còn nhánh hiệu ứng ghép hậu tố `_effect.txt`. `G/KNpcResNode.cpp:108–125,144–207,212–239,547–586`, `G/KNpcRes.cpp:1835–1854` |
| Có mở được ảnh rời hay ảnh đóng gói? | [THẤY] Bộ đọc SPR thử tra ảnh trong danh sách gói rồi dùng nhánh mở theo tên nếu không tìm được qua bước tra gói. [TÀI LIỆU] K-02 đã kiểm kê `Resources` của client bản A và `Settings/NpcRes` cùng các gói của server. [CHƯA KIỂM] SPR cụ thể nằm ở gói nào, và các ảnh PNG trong `Resources/avatar` có được dùng làm hình nhân vật trong trận hay không. `D:/JX-build/qh9A/Classes/engine/KPakFile.cpp:37–74,114–125`, `K-02-nhan-vat.md:29–41,98–105` |

## Đã xác minh / Chưa xác minh

- **[THẤY]** Đã xác minh trên mã bản A đường từ trạng thái tới động tác, từ trang bị tới tên ảnh, rồi từ bảng thứ tự tới danh sách vẽ. (`G/KNpcRes.cpp:1684–1733,1791–1854`, `G/KNpcResNode.cpp:592–630,1201–1216,1390–1474`, `V:205–217,460–493`)
- **[TÀI LIỆU]** Quy luật cũ để trống phần lớn ma trận nam/nữ và động tác. U-03 thêm dữ liệu bảng nữ cùng điều kiện áp dụng, còn phép nối từ động tác khi chơi tới mục INI vẫn bỏ ngỏ. (`QUY-LUAT-VE-BO-PHAN.md:20–46`, `BANG-THU-TU-VE.md:19–25,85–111,205–209`)
- **[CHƯA KIỂM]** File INI và các bảng của bản đang cài, số khung thật của từng SPR, các thành viên trong PAK và hình ảnh thực tế khi game chạy. Phạm vi SO-01 là đọc tĩnh. (`K-02-nhan-vat.md:98–105`, `BANG-THU-TU-VE.md:111,141–167`, `JX1_OPS/TASKS/SO-01.md:25–29`)

## Bàn giao

[TÀI LIỆU] Báo cáo thao tác, sổ thông số và đề xuất dòng mục lục nằm tại [SO-01.md](../REPORTS/SO-01.md). Tổng quan phụ trách commit.
