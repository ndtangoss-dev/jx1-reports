TÓM TẮT 5 DÒNG
1. PARTIAL: đã đọc tĩnh client gốc; không sửa source, chạy game/exe, kết nối VM/mạng hay đọc dữ liệu runtime.
2. KNpcRes có sức chứa 2 lớp và 24 section/6 nhóm; đường ChangeFeature hiện tại cập nhật 5 nhóm BASE, không chứng minh cánh/EFFECT đang hiện.
3. Thứ tự section tra bảng theo action, hướng và khung; source không đảm bảo một thứ tự cố định cho mọi tư thế.
4. Phi phong được gọi đích danh `Pifeng`; `ChiBang` là nhóm riêng. Cụm “phương ấy” chưa đủ căn cứ để chọn Phi Phong hay phái.
5. Trang sức shiping thay lớp vũ khí, yinjian thay lớp áo; chưa xác minh asset/SORT từng hướng hoặc runtime, J-05 chưa có file local.

## Phạm vi và phương pháp

Khảo sát tĩnh ngày 17/11/2026 theo task J-04. Nhánh ban đầu `task/J-04`, HEAD nền `f8803286227bd86cee3e542ec404f748dd99fbde`; task ban đầu là file untracked, giữ nguyên nội dung và chỉ nối mục Kết quả. Không được cung cấp commit ghim riêng cho prompt; đã đọc file task local, không tự thay bằng prompt khác.

Quy ước: O = `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client`; các tên file rút gọn trong báo cáo nằm dưới `O/Classes/gamecore/`, riêng `KNpcResVN.cpp` ở `O/Classes/vn/gamecore/`. M = `D:/JX-source/client/Classes/vn/gamecore/KNpcResVN.cpp`, là bản có glow bổ sung, tách biệt với O. S = `D:/JX-source/server/jxOnline/gameserver/Sources/Core/Src/KNpc.cpp`. Đọc thêm báo cáo [H-04](H-04-hieu-ung-vu-khi.md) và [H-14](H-14-mat-khung-hieu-ung.md); không có file khớp J-05 trong `JX1_OPS/TASKS` hoặc `REPORTS` lúc khảo sát. “Liên hệ” được thực hiện bằng dẫn chiếu/bàn giao trong báo cáo, không gửi tin cho worker khác.

Không sửa source, build/test, chạy exe/game, kết nối mạng/VM hoặc trích bảng tài nguyên dài. Python thực tế chạy bằng `python -I -`. Không tạo bảng private do không xuất bảng dài; báo cáo chỉ giữ số tham số và ánh xạ nhỏ cần cho kết luận.

Định danh SHA-256 đọc bytes: `KNpcRes.cpp` = `dec54b5aafa12ebcc12a5bfb8f1a3564bf22c63ad23f0b1f046a9470bca2665c`; `KNpcResNode.cpp` = `cd748986b6d17de50d5d9fd1d4aa3a3fbecc650db0a441d96b7694ff796fb09e`; `KNpcResVN.cpp` = `cd7a3b43e8b92ec2f803118597c227068868e865e0eb0e403b2a73e9602a3f56`; `KItemList.cpp` = `82fd49a0f14b426e78bf1bff5b157a05ff56c9c0bf97b7c6da76a7f16fb5d3ba`. Các hash không chứng minh source khớp APK đang dùng.

## ĐÃ XÁC MINH

### Mô hình lớp và section

`Classes/gamecore/KNpcResNode.h:23-26` định nghĩa 6 nhóm cơ thể, 4 section mỗi nhóm và tổng `MAX_PART=24`. Nhóm section theo các vòng lặp nạp đồ ở `Classes/gamecore/KNpcRes.cpp`:

| Section | Nhóm được gắn bởi setter/nạp SPR | Bằng chứng |
|---|---|---|
| 0–3 | Mũ/đầu (`SetHelm`) | `KNpcRes.cpp:1068-1095` |
| 4–7 | Áo/thân (`SetArmor`) | `KNpcRes.cpp:1116-1147` |
| 8–11 | Vũ khí (`SetWeapon`) | `KNpcRes.cpp:1219-1231` |
| 12–15 | Ngựa (`SetHorse`) | `KNpcRes.cpp:1354-1380`; nạp theo `m_nHorseType` ở `1234-1244` |
| 16–19 | Phi phong (`SetPifeng`) | `KNpcRes.cpp:969-1017`; nạp theo `m_nPifengType` ở `1247-1258` |
| 20–23 | Cánh (`ChiBang`) | nạp theo `m_nChiBangType` ở `KNpcRes.cpp:1259-1270` |

Các section trên là sức chứa và các setter legacy vẫn có định nghĩa; không chứng minh mọi slot/layer được dùng ở entry point hiện tại. `KNpc::Activate` gọi `SetRideHorse` rồi **ChangeFeature** (`KNpc.cpp:695-698`); block gọi từng setter cũ ở dòng 699–710 là comment. `ChangeFeature` chỉ gọi `SetPartInfo(BASE, HELM/ARMOR/WEAPON/HORSE/MANTLE)` tại `KNpcRes.cpp:1703-1726`. Enum part hiện tại có 5 nhóm đó (`CoreUseNameDef.h:8-15`), trong khi sức chứa cũ vẫn có 6 nhóm/24 section. `UpdateActionNormal` lặp theo 5 nhóm và hai layer (`KNpcRes.cpp:1646-1679`); phải phân biệt nhánh này với setter legacy nạp cánh ở 20–23. Chưa chứng minh cánh hay EFFECT được kích hoạt bằng gameplay hiện tại. `m_DataRes` có kiểu `KNpcResVN` (`KNpc.h:19,816`) và `KNpc::Paint` gọi Draw với tổng/khung action (`KNpc.cpp:5853,5916`).

Trong cây server, các setter đồ ở S:1083–1095 thuộc block **#ifndef _SERVER** bắt đầu tại S:1074; không phải bằng chứng server production chạy renderer. Bằng chứng server thật về dữ liệu đồng bộ: `PLAYER_SYNC` nhận ArmorType, HelmType, MaskType, PifengType và mFaction riêng nhau (S:8021–8032); không có dữ liệu thứ tự vẽ/pixel trong đoạn đồng bộ đã đọc. Có trường phái và Phi Phong riêng cũng không giải nghĩa được cụm “phương ấy”.

Mặt nạ dùng `m_MaskType`/`ReSetRes`/`GetFrameCopyFromTemplate` (`KNpc.cpp:648-677`). Nhánh biến hình lấy `NpcResType`, Remove/Init resource và gọi `setBuWeiHide` (`KNpc.cpp:10627-10641`); nó không phải slot overlay riêng trong năm part hiện hành. `KItemList.cpp:1280-1288` chọn ID mask từ `GetItemResIdx` hoặc `GetBaseMagic`.

Trang sức có đường xác định được: enum có ring, amulet, pendant, mask, pifeng, yinjian và shiping (`KItem.h:52-69`); `GetEquipPlace` ánh xạ sang slot item tương ứng (`KItemList.cpp:1852-1901`). Trong `KItemList::Equip` (bắt đầu dòng 1157), `itempart_shiping` với resource ID dương ghi **m_WeaponType**, `itempart_yinjian` với resource ID dương ghi **m_ArmorType** (`KItemList.cpp:1318-1327`). Nghĩa là hai loại này thay appearance lớp vũ khí/áo, không thêm section độc lập trong nhánh này. Tháo shiping tra lại item vũ khí để phục hồi (`KItemList.cpp:1635-1655`). Ring/amulet/pendant là slot item có thật nhưng chưa thấy chúng gán lớp SPR trong switch đổi appearance đã đọc; không kết luận chúng không có hiệu ứng ở hệ thống khác.

`Classes/gamecore/CoreUseNameDef.h:20-24` có hai lớp sprite: `BASE` và `EFFECT`. `KNpcRes.h:118-120` lưu part info và `KSprControl` theo `[layer][part]`, vì thế mỗi section có thể có ảnh lớp gốc và lớp hiệu ứng riêng. Không thấy enum phân lớp riêng cho glow/sét trong các khai báo này; H-14 mô tả glow/sét được vẽ bổ sung tại đường render khác.

File EFFECT được nạp qua hậu tố `_effect.txt` cho tên tài nguyên và metadata (`KNpcResNode.cpp:149-171`). `SetPartInfo` truyền đúng `ePartLayer` cho cả tên ảnh/frame/hướng/interval (`KNpcRes.cpp:1780-1795`). Ngược lại các setter legacy như `SetPifeng` có truyền layer khi lấy tên ảnh nhưng bỏ đối số layer khi lấy metadata (`KNpcRes.cpp:993-994`); getter mặc định layer=0 (`KNpcResNode.h:235-241`). Đây là khác biệt tĩnh đáng kiểm nếu còn caller legacy; không gán nó thành lỗi đang xảy ra trên nhánh ChangeFeature.

### Đồng bộ hướng và khung

Trong `KNpcRes::Draw`, hướng được lượng tử hóa từ hướng đầu vào theo số hướng của từng SPR (`KNpcRes.cpp:255-287`). Nhánh `nAllFrame > 0` cũng có trong VN (`KNpcResVN.cpp:28-60`), với phép chia số nguyên:

```text
D = max(totalDirs, 1)
d = (nDir + 32/D) / (64/D); nếu d >= D thì d -= D
F = totalFrames / D
frame = d*F + F*nCurFrame/nAllFrame
```

Mọi part đã nạp nhận cùng tiến độ action từ caller nhưng **không nhất thiết cùng chỉ số frame tuyệt đối**. Ví dụ số học minh họa, không phải asset đo được: cùng d=2 và tiến độ 1/2, SPR có F=8 chọn index 20, SPR có F=16 chọn index 40. Cùng metadata chỉ đảm bảo cùng index theo công thức, không bảo đảm hình vẽ asset khớp vị trí. `KSprControl::SetCurFrame` từ chối index ngoài `[0,totalFrames)` và giữ frame cũ (`KSprControl.cpp:79-94`); metadata sai vì vậy có thể làm đứng/lệch frame, chưa chứng minh đã xảy ra. Không tự đổi miền hướng/hằng số để chữa khi chưa có metadata thực.

Nếu `nAllFrame` bằng 0, các SPR tiến frame riêng bằng `GetNextFrame` trên từng part/layer (`KNpcRes.cpp:357-377`; nhánh VN `KNpcResVN.cpp:130-150`); đầu vào âm đã return. `GetNextFrame` tăng tối đa một frame khi tick SubWorld đổi (`KSprControl.cpp:342-370`), không phải đồng hồ độc lập theo FPS mỗi layer. Các part có thể giữ cùng tick nhưng khác tổng khung/điểm bắt đầu; chưa xác định input runtime từng NPC. Action còn phụ thuộc vũ khí BASE và cờ cưỡi ngựa (`KNpcRes.cpp:1625-1641`), tra bảng on-horse/no-horse tại `KNpcResNode.cpp:592-605`, nên ngựa có thể đổi action của toàn bộ hình ghép.

### Thứ tự vẽ và các lớp hiệu ứng

Renderer lấy bảng sort qua `GetnSort(action, direction, frame)`; bảng đặc biệt chuyển tiếp sang `CSortTable::GetSort` (`KNpcResNode.cpp:612-630`). Bộ tra cứu kiểm tra action/hướng và dùng frame để chọn dòng override; nếu không có override sẽ lấy thứ tự mặc định theo hướng (`KNpcResNode.cpp:1390-1446`). Tên file bảng sort lấy từ bảng `KindFile` được nạp tại `KNpcResNode.cpp:365-370`; metadata SPR lấy từ file thông tin part/layer (`KNpcResNode.cpp:140-180,232-239`). Sau đó renderer lặp theo thứ tự bảng và lặp lớp BASE/EFFECT cho mỗi section (`KNpcResVN.cpp:439-471`; bản base `KNpcRes.cpp:663-695`). Vì vậy thứ tự section có thể đổi theo hướng và khung, và hai lớp của một section được phát cùng lượt theo thứ tự layer. Dữ liệu bảng sort thực tế mới quyết định kết quả cho nhân vật/action cụ thể; chưa có tài nguyên đó để dựng sơ đồ thứ tự cụ thể. Một chi tiết cần lưu ý khi thiết kế log: `nCurDirNo/nCurFrameNo` bị cập nhật trong vòng lặp trên mọi part/layer SPR đang tồn tại, rồi cặp giá trị cuối được truyền vào `GetnSort` (`KNpcResVN.cpp:45-60,197`); do đó chỉ log `nDir/nCurFrame` bên ngoài chưa đủ để xác nhận khóa sort cuối cùng.

Trình tự lớp ở O: các state/special phía sau → shadow (nếu bật) → từng section theo sort, BASE trước EFFECT nếu có tên ảnh → state phía trước. Bằng chứng gửi draw trước shadow tại `KNpcResVN.cpp:374-414`, shadow/section tại `416-471`, state trước tại `509-546`. Một khối cũ dùng `DrawPrimitives/EQ_PART_*` tại dòng 623 trở đi nằm trong comment, không dùng khối đó để khẳng định thứ tự runtime. `getIniDataForGame` duyệt primitives theo thứ tự, lấy texture theo frame và bỏ texture thiếu (`O/Classes/gamescene/KgameWorld.cpp:8876-8899`). Chưa dựng ma trận thứ tự cho từng hướng khi thiếu bảng đã nạp.

Đối chiếu trực tiếp M, tách với O: glow bổ sung chỉ xét NPC local và ngoài menu (M:481), cache cấp weapon rồi từ +6 mới vào (M:483-499). Nó duyệt section weapon theo sort, lấy đúng frame đang có ở mỗi layer (M:509-531), vẽ 9 lượt glow/section, gọi sét trên dominant section có rect rồi vẽ lại các part nằm sau section để che hiệu ứng (M:572-597). Đây là ảnh chụp lại khung weapon đã chọn, không phải một SPR glow có action frame chung; timer sét riêng được H-14 phân tích. Với shiping thay weapon appearance nhưng cấp glow vẫn đọc itempart_weapon (M:489-490), có khả năng lớp hình và nguồn cấp cường hóa khác nhau; cần kiểm item cụ thể trước khi gọi đây là lỗi. Các gate góc/clip/mask của `jxDrawBolts` có thể bỏ sét theo H-14; không suy ra glow chắc chắn mất theo cùng gate.

Phi Phong còn có **nhãn UI**, khác body section 16–19: `O/Classes/gamescene/KgameWorld.cpp:11137-11165` (`PaintPifeng`) lấy ảnh từ `Ui/npcbobo.ini`, giữ node đã có theo tag và add child z=1. Nhãn này không đi qua GetnSort; không nên nhầm nó với sprite áo choàng hoặc thứ tự che thân theo hướng.

## CHƯA XÁC MINH

- Bảng sort đã nạp cho nhân vật, action và hướng cụ thể; thứ tự occlusion chính xác theo từng khung SPR.
- Số frame, số hướng, frame interval và sự tương ứng pixel giữa các file SPR cụ thể. Source nạp các giá trị metadata theo từng resource; giá trị mặc định truyền vào hàm tra cứu không phải phép đo metadata.
- Hình thực tế shiping/yinjian, hiệu ứng ring/amulet/pendant ngoài switch Equip; asset nào đưa vào template khi bật `m_MaskType`.
- Glow/sét gắn vào trang bị nào ngoài trường hợp H-14 đã khảo sát; kết quả khi nhiều section weapon hoặc nhiều lớp EFFECT cùng hiện diện.
- Ý nghĩa của “phương ấy” trong thư #064: có thể là Phi Phong hoặc “phái”; không đủ bằng chứng ngôn ngữ/ngữ cảnh để chọn một nghĩa.
- Trạng thái sprite của ngựa/phi phong/cánh trong runtime, và liệu mọi lớp có nhận cùng action/frame input hay không.

## ĐỀ XUẤT TỐI ƯU

1. Dùng một nhân vật và một action cố định; trích metadata SPR của sáu nhóm cùng hai layer (BASE/EFFECT), gồm file, tổng hướng, tổng frame và interval. So sánh index được chọn tại từng `nCurFrame` để xác định các layer có cùng tiến độ nhưng khác frame index.
2. Với action cần kiểm, xuất bảng sort đã nạp thành ma trận `hướng × frame → thứ tự section`; đối chiếu tối thiểu đứng, đi và vung vũ khí. Chỉ kết luận che khuất sau khi biết bảng resource thực tế.
3. Kiểm tra shiping có thay đúng weapon appearance, yinjian có thay đúng armor và có phục hồi khi tháo; không thêm slot render để giải quyết một appearance override. Kiểm mask bật/tắt riêng với ngựa/Phi Phong.
4. Phối hợp H-14 bằng đúng item/action glow và J-05 bằng định danh resource/action trước khi thử thay đổi. Báo cáo này không đề nghị sửa client khi chưa có kết quả đo và test hồi quy.

## Kiểm chứng, lỗi công cụ và bàn giao

- Trạng thái PARTIAL: hoàn thành bản khảo sát cơ chế source; chưa có item/action/bảng sort cụ thể để chốt thứ tự cho từng hướng và phần hình quan sát được. Không có blocker quyền cần vượt; giữ các điểm chưa xác minh ở trên, không kéo dài thành khảo sát toàn repo.
- `Folder` trong worktree không tồn tại: lần đọc đầu báo Cannot find path; dùng đường client gốc từ tham chiếu H-14 và xác nhận tồn tại. Tìm thư mục ổ D quá rộng đã ngắt; không dùng kết quả đó để chọn source.
- `rg` báo không được nhận diện trong PATH: chuyển đọc bằng PowerShell/Python chuẩn. Python lượt đầu gặp `UnicodeEncodeError` do stdout cp1252; sửa bằng `sys.stdout.reconfigure(encoding='utf-8')`, lượt sau thành công. Một lượt đọc dùng nhầm `Classes/gamecore/KNpcResVN.cpp` gây FileNotFoundError; dùng đúng `Classes/vn/gamecore/KNpcResVN.cpp` ở các lượt đọc sau. Không lỗi nào được thử quá 3 lần.
- Kiểm tra tiêu đề bằng chuỗi tiếng Việt trong Python qua pipe PowerShell bị sai so sánh và IndexError dù nội dung UTF-8 đọc ra đúng; chuyển phép kiểm tra chuỗi sang PowerShell native để tránh mã hóa đầu vào pipe. Không sửa nội dung báo cáo để chiều theo phép kiểm sai.
- Bản nháp đã lưu vào chính file báo cáo trong phiên và cập nhật khi phát hiện branch/comment legacy. Phân biệt đường active với comment bằng đọc ngữ cảnh, không chỉ kết quả tìm symbol.
- Kiểm định chỉ bằng đọc source/file:dòng, SHA-256 và kiểm tra định dạng Markdown; `git diff --check` không báo lỗi nhưng hai file đang untracked nên không coi lệnh đó là kiểm tra toàn nội dung mới. Không chạy test/build/runtime vì task cấm chạy game/exe và chỉ khảo sát tĩnh.
- Bàn giao H-14: cần ma trận sort và frame weapon từng layer, thêm trường nguồn appearance shiping và nguồn cấp weapon; đối chiếu gate sét với frame đang có. Bàn giao J-05: cần task/resource/action được chỉ rõ để gắn sơ đồ này vào tài nguyên, chưa có file local nên chưa đối chiếu được.
- Chỉ ghi báo cáo này và nối `## Kết quả` vào task. Không commit/push vì không được yêu cầu; SHA commit mới: không có. SHA nền ở phần đầu không phải commit kết quả; không có bằng chứng GitHub và không dùng mạng theo yêu cầu.

## MỤC SỔ THÔNG SỐ

Các số dưới đây là thông số cấu trúc hoặc mặc định thấy trong đường render/nạp asset; không phải kết quả đo runtime. Dòng có nguồn định nghĩa constant ghi rõ đó là cấu hình biên dịch, không phải giá trị từng asset.

| Nhóm | Tên/hằng số | File:line | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---:|---|---|---|---|
| Cấu trúc | `MAX_BODY_PART` | `KNpcResNode.h:23` | 6 | nhóm | Số nhóm lớn | KHÔNG | Hằng số source |
| Cấu trúc | `MAX_BODY_PART_SECT` | `KNpcResNode.h:24` | 4 | section/nhóm | Slot render trong mỗi nhóm | KHÔNG | Hằng số source |
| Cấu trúc | `MAX_PART` | `KNpcResNode.h:25` | 24 | section | Kích thước sort/part | KHÔNG | Tích 6×4 từ source |
| Cấu trúc | `emNPCRES_PART_COUNT` | `CoreUseNameDef.h:8-15` | 5 | nhóm active | Giới hạn UpdateActionNormal, khác sức chứa 6 nhóm | KHÔNG | Enum source |
| Cấu trúc | `emNPCRES_PART_LAYER_COUNT` | `CoreUseNameDef.h:20-24` | 2 | layer | BASE và EFFECT | KHÔNG | Enum source |
| Cấu trúc | `MAX_ACTION` | `KNpcResNode.h:27` | 128 | action tối đa | Giới hạn CSortTable | KHÔNG | Hằng số source |
| Điều hướng | `nGetDir` fallback | `KNpcRes.cpp:259-263` | 1 | hướng | Tránh chia theo 0; không đại diện metadata thực | CẨN THẬN | Source |
| Điều hướng | Hướng đầu vào | `KNpcRes.cpp:261-263` | 64 | đơn vị hướng logic | Lượng tử hóa hướng theo số hướng SPR | CẨN THẬN | Biểu thức source |
| Điều hướng | Bù lượng tử hóa hướng | `KNpcResVN.cpp:55` | 32 | đơn vị hướng logic | Làm tròn về hướng SPR | KHÔNG | Biểu thức 32/D; phụ thuộc miền 64 |
| Asset | Mặc định `total frames` | `KNpcRes.cpp:994` | 16 | frame | Giá trị fallback khi đọc metadata Phi Phong | CẨN THẬN | Đối số fallback source; chưa đo asset |
| Asset | Mặc định `total dirs` | `KNpcRes.cpp:994` | 16 | hướng | Giá trị fallback khi đọc metadata Phi Phong | CẨN THẬN | Đối số fallback source; chưa đo asset |
| Asset | Mặc định `interval` | `KNpcRes.cpp:994` | 0 | tick theo engine | Giá trị fallback khi đọc metadata Phi Phong | CẨN THẬN | Đối số fallback source; chưa đo asset |
| Asset | Fallback frame lúc parse | `KNpcResNode.cpp:232,235` | 16 | frame | Mặc định khi đọc bảng | CẨN THẬN | Source; chưa đo asset |
| Asset | Fallback hướng lúc parse | `KNpcResNode.cpp:232,237` | 8 | hướng | Khác fallback 16 hướng của setter | CẨN THẬN | Source; chưa đo asset |
| Asset | Fallback interval lúc parse | `KNpcResNode.cpp:232,239` | 1 | tick | Khác fallback 0 của setter | CẨN THẬN | Source; chưa đo asset |
| Asset | Getter mặc định layer | `KNpcResNode.h:235-241` | 0 | layer | Setter legacy thiếu layer sẽ đọc BASE | CẨN THẬN | Đối số mặc định source |
| Timer | Interval tối thiểu | `KSprControl.cpp:350-351` | 1 | tick | Chuẩn hóa interval; nhánh này tăng khi tick đổi | CẨN THẬN | Source |
| Phi Phong item | Ngưỡng cấp | `KItemList.cpp:1302,1309` | 10 | cấp | Chọn cách tra appearance | CẨN THẬN | Source; chưa đo item |
| Phi Phong item | Modulus cấp cao | `KItemList.cpp:1305,1313` | 10 | cấp | Lấy level modulo để chọn appearance | CẨN THẬN | Source; chưa đo item |
| Phi Phong UI | `FortuneRank/count` fallback | `O/Classes/gamescene/KgameWorld.cpp:11151` | 11 | loại | Giới hạn ID ảnh nhãn | CẨN THẬN | Source; chưa đọc ini |
| Phi Phong UI | `nTime` fallback | `O/Classes/gamescene/KgameWorld.cpp:11149,11152` | 20 | chưa rõ | Đọc vào local, chưa thấy dùng tiếp trong hàm | CẨN THẬN | Source |
| Phi Phong UI | Nhãn X | `O/Classes/gamescene/KgameWorld.cpp:11162` | -20 | tọa độ node | Lệch ngang nhãn, không phải body attachment | CẨN THẬN | Source |
| Phi Phong UI | Nhãn local z | `O/Classes/gamescene/KgameWorld.cpp:11163` | 1 | local z | Thứ tự node UI, khác bảng sort thân | CẨN THẬN | Source |
| Glow sửa đổi | Cache cấp weapon | `M:487` | 2000000 | µs | Trễ cập nhật cấp sau đổi đồ | CẨN THẬN | Source M; không đo runtime |
| Glow sửa đổi | Ngưỡng glow | `M:499` | 6 | cấp | Bắt đầu vẽ bổ sung | CẨN THẬN | Source M |
| Glow sửa đổi | Ngưỡng vừa | `M:501-502` | 12 | cấp | Chọn mức glow/sét | CẨN THẬN | Source M |
| Glow sửa đổi | Ngưỡng mạnh | `M:501-502` | 15 | cấp | Chọn mức glow/sét | CẨN THẬN | Source M |
| Glow sửa đổi | Cường độ dưới ngưỡng | `M:502` | 0 | hệ số | Giá trị nhánh fallback, khối ngoài đã gate cấp | CẨN THẬN | Source M |
| Glow sửa đổi | Cường độ nhẹ | `M:502` | 0.35 | hệ số | Mức glow nhẹ | CẨN THẬN | Source M |
| Glow sửa đổi | Cường độ vừa | `M:502` | 0.65 | hệ số | Mức glow vừa | CẨN THẬN | Source M |
| Glow sửa đổi | Cường độ mạnh | `M:502` | 1 | hệ số | Mức glow mạnh | CẨN THẬN | Source M |
| Glow sửa đổi | Pulse nền | `M:503` | 0.9 | hệ số | Nền dao động cường độ | CẨN THẬN | Source M |
| Glow sửa đổi | Biên độ pulse | `M:503` | 0.1 | hệ số | Biên độ dao động | CẨN THẬN | Source M |
| Glow sửa đổi | Tốc độ pulse | `M:503` | 0.006 | rad/ms | Chu kỳ dao động | CẨN THẬN | Source M |
| Glow sửa đổi | Cấp ép thử tối đa | `M:494` | 31 | cấp | Chỉ nhánh trace/ép cấp, chưa chạy | CẨN THẬN | Source M |
| Glow sửa đổi | Sức chứa section | `M:525,531` | 8 | section | Dung lượng thu weapon sections | CẨN THẬN | Source M |
| Glow sửa đổi | Số lượt glow | `M:576` | 9 | lượt/section | Chi phí và hình quầng sáng | CẨN THẬN | Source M |
| Glow sửa đổi | Alpha trung tâm | `M:583` | 0.8 | hệ số alpha | Mức glow lượt giữa | CẨN THẬN | Source M |
| Glow sửa đổi | Alpha biên | `M:583` | 0.45 | hệ số alpha | Mức glow các lượt lệch | CẨN THẬN | Source M |
