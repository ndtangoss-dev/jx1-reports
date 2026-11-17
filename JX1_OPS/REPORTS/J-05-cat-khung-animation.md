TÓM TẮT 5 DÒNG
1. ĐÃ XÁC MINH source client gốc: khung SPR được ánh xạ từ tick nguyên; khi tốc độ tick vượt số khung thì phép chia nguyên có thể bỏ qua khung nguồn, khi chậm hơn có thể lặp khung.
2. ĐÃ XÁC MINH: tốc độ đánh/niệm và interval tài nguyên đổi thời lượng phát; client đặt nhịp render 60 FPS, nhưng không thấy bộ bỏ tick bù theo dt trong hàm update được kiểm tra.
3. ĐÃ XÁC MINH: có cờ ẩn NPC/người/đạn, giới hạn cấu trúc dữ liệu và ẩn một số node; chưa thấy LOD tự động theo mật độ hay giới hạn tổng hiệu ứng trong phạm vi đã khảo sát.
4. CHƯA XÁC MINH: không có đo runtime hoặc dữ liệu tài nguyên để tính tỷ lệ khung bị rơi ở cảnh đứng/đi/đông; không suy ra phần trăm thực tế từ source.
5. Chỉ đọc client gốc và server source; không chạy game/exe, VM, mạng, build hay test; liên hệ H-14/H-15 được ghi riêng ở dưới.

## Phạm vi và phương pháp

- Client gốc: `C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes` (G). Đối chiếu tĩnh với `D:\JX-source\client\Classes` (C); các file animation chính có cùng số dòng và nội dung liên quan tại các vị trí nêu dưới đây.
- Server source: `D:\JX-source\server\jxOnline\gameserver\Sources` (S). Chỉ đọc mã, không chạy server. Mã cũ trong `Engine` có xử lý SPR/cache, nhưng chưa thấy bằng chứng server chạy chu kỳ render client hay bỏ khung để giảm tải.
- Tham chiếu yêu cầu liên quan: `JX1_OPS/HOP-THU/CHO-SONNET.md:436-445` (H-14), `:463-470` (H-15). Đây là mô tả lỗi/giả thuyết và kế hoạch đo, không phải kết quả xác minh runtime.

## ĐÃ XÁC MINH

### Tick, dt và ánh xạ khung

- `G/AppDelegate.cpp:119`: `setAnimationInterval(1.0f/60)` cấu hình nhịp animation/render mục tiêu 60 Hz. Đây không chứng minh FPS thật hoặc nhịp logic. `G/gamescene/KgameWorld.cpp:5059` là `update(float delta)`; thân hàm không thiết lập frame skipping theo FPS/delta (đường xử lý update lớn; chưa chứng minh mọi callback trong engine).
- `G/gamecore/KNpc.cpp:3732-3744`: `KNpc::WaitForFrame` tăng `m_Frames.nCurrentFrame` mỗi lần được gọi, so với `nTotalFrame`, rồi reset về 0; bước logic là số nguyên. Source không cho biết callback này được gọi bao nhiêu lần mỗi giây ở runtime.
- `G/gamecore/KSprControl.cpp:297-334`: `ChangeCurFrame` lấy `nDTime = currentTime - m_dwTimer`, kẹp interval tối thiểu về 1, rồi ánh xạ `nDirFrame * nDTime / m_dwInterval` bằng chia nguyên. Nếu thời gian trôi qua nhiều interval, nhánh loop đặt lại đầu hướng (`:314-321`) thay vì lặp qua từng khung trung gian; non-loop ghim khung cuối. Đây là vị trí có thể bỏ khung khi gọi muộn, nhưng cần xác nhận call site thực sự dùng hàm này.
- `G/gamecore/KSprControl.cpp:342-373`: `GetNextFrame` chỉ tăng một khung mỗi lần `m_dwCurrentTime` khác `m_dwTimer`; không dùng `m_dwInterval` để tích lũy nhiều bước, và không bắt kịp nhiều tick trễ. `G/gamecore/KNpcRes.cpp:357-409` gọi hàm này cho bóng, lớp hình, trạng thái và special SPR. Bước tăng một khung mỗi lần gọi được xác minh; tần số lời gọi thực tế chưa đo.
- `G/gamecore/KNpcRes.cpp:2772`: phép đổi frame logic sang SPR có dạng `(MAX_NPC_DIR * nFrame) / nTotalFrames`; các nhánh đồng bộ lớp ở `:265-286` dùng phép chia nguyên tương tự. Khi tổng khung nguồn lớn hơn số bước logic, một số khung nguồn không được chọn; khi ít hơn, khung được tái sử dụng. Không thể suy ra số khung trên asset cụ thể nếu không đọc và phân loại dữ liệu asset.
- Điều kiện lượng tử hóa tổng quát, không phải tỷ lệ đo: với `F` frame nguồn và `T` bước logic được phân phối đều, nếu `F>T` thì số chỉ số nguồn không được lấy mẫu xấp xỉ `F-T` trên `F`; nếu `F<=T` sẽ có khung nguồn được lặp. Đây không tính đến nhánh loop, interval, asset lỗi, culling hay mức độ frame được người chơi nhận thấy.

### Tốc độ đánh/niệm và thời lượng

- `G/gamecore/KNpc.cpp:2377-2399` (`DoOrdinSkill`): lấy hệ số tốc độ từ `_gameGlobalSet.NpcInfo`; với đánh vật lý tính `m_AttackFrame * naAttackSpeed / (nbAttackSpeed + m_CurrentAttackSpeed)` tại `:2381`, với phép tính `m_CastFrame * naAttackSpeed / (m_CurrentCastSpeed + nbAttackSpeed)` tại `:2399`. Chia nguyên có thể đổi số tick tổng và do đó bỏ/lặp khung qua ánh xạ trên. Giá trị mặc định 100 không phải giá trị runtime đã xác minh.
- `G/gamecore/KNpc.cpp:2254-2260`: thời điểm thi triển kế tiếp được đặt bằng thời gian hiện tại cộng `GetHorsePerCast()` hoặc `GetDelayPerCast()`. Đây là cooldown/niệm tối thiểu theo tick, không phải tự thân là cắt khung animation.
- Không thấy kết luận được về ngưỡng thời gian niệm tối đa chung; giá trị phụ thuộc loại skill/cấu hình và cần truy vết riêng theo từng kỹ năng.

### Ẩn/culling, số lượng và pool

- `G/gamecore/KNpc.cpp:5889-5905`: các điều kiện `nIsHideNpc`, `nIsHidePlayer` và cờ trên NPC người chơi trả sớm khỏi một nhánh xử lý hiển thị. Đây là ẩn theo cờ/chủ động, không phải LOD tự động khi đông.
- `G/gamecore/CoreDrawGameObj.cpp:167`: cờ `m_bIsHideMissle` trên người chơi điều kiện hóa nhánh vẽ missile. `KNpc.cpp:268` khởi tạo cờ về FALSE; source không xác định người dùng/setting nào thay đổi nó.
- `G/gamecore/KgameWorld.cpp:12416`: kiểm tra node missle và chỉ số `nIndex` trong miền `1..MAX_MISSLE-1` trước khi xử lý node. `G/gamecore/KMissle.h:6` định nghĩa `MAX_MISSLE 30000`. Đây là dung lượng chỉ số/pool, không phải ngân sách số hiệu ứng đang hiển thị hoặc cơ chế loại bỏ hiệu ứng khi quá tải.
- `G/gamecore/GameDataDef.h:132` đặt `MAX_SKILL_STATE 18`; là giới hạn slot trạng thái kỹ năng/NPC, không đồng nghĩa giới hạn 18 hiệu ứng toàn màn hình.
- Có nhiều đoạn tắt node phụ bằng `setVisible(false)` trong `G/gamescene/KgameWorld.cpp` (ví dụ node NPC phụ tại `:9293-9310`, và node missle ở khoảng `:12416-12559`). Chưa xác minh có phép thử giao hình chữ nhật với viewport để cull chính sprite NPC/skill. Không tìm thấy bằng chứng đủ chắc về culling ngoài màn hình tổng quát hoặc LOD theo mật độ.

### SPR, chuyển đổi và cache

- `G/engine/Kgetinidata.cpp:570`: `findinidata_new` nhận SPR, chỉ số frame và trả texture/metadata. Đường này chứng minh chuyển/nạp tài nguyên để hiển thị; chưa đủ bằng chứng về lấy mẫu khung, gộp atlas, nén hoặc giảm kích thước ở bước chuyển SPR→Coco.
- `G/gamecore/ImgRef.cpp:44`: `IR_NextFrame` là helper đổi frame theo interval; `G/gamecore/KNpc.cpp:5506-5550` cập nhật frame các SPR trạng thái qua helper. Điều kiện/timing chi tiết nằm ở helper, không tương đương quality LOD.
- `G/gamescene/KScenePlaceC.cpp:1083-1091`: khi dọn ảnh mặt đất vùng, gọi `FreeImage`, xóa handle rồi `CCTextureCache::removeUnusedTextures()`. `G/gamescene/KgameWorld.cpp:2411` cũng gọi removeUnusedTextures ở đường dọn scene. Đây là giải phóng tài nguyên không còn dùng, không phải cơ chế cắt khung.
- `S/Engine/Src/KBmp2Spr.cpp:33-56, 200-240`: bộ chuyển bitmap sang SPR tìm bounding rectangle tối thiểu và mã hóa theo dòng; không thấy giảm số frame trong đoạn kiểm tra này. `S/Engine/Src/KSpriteCache.cpp:31-56`: cache nạp `KSprite`, khi giải phóng node gọi `Free` và delete. Đây là xử lý định dạng/cache ở engine cũ, không chứng minh pipeline Coco hiện đại hay chính xác file đầu vào của client.

### Tỷ lệ khung theo cảnh

| Cảnh | Kết luận tĩnh | Tỷ lệ thực tế |
|---|---|---|
| Đứng | Nếu frame nguồn > bước logic, phép ánh xạ nguyên có thể bỏ mẫu; nếu bước logic > nguồn, frame lặp. Số frame/timing phụ thuộc asset. | CHƯA XÁC MINH; không có đếm frame hoặc asset thống kê. |
| Đi/chạy | Cơ chế ánh xạ/tick như trên; logic di chuyển và animation có thể được gọi ở nhịp khác nhau. | CHƯA XÁC MINH; không có FPS/dt/capture đồng bộ. |
| Chiến đấu đông | Cờ ẩn thủ công/pool hữu hạn tồn tại; không thấy bằng chứng tự hạ LOD theo mật độ. Tải cao có thể làm update/render trễ nhưng không thể kết luận frame loss chỉ từ source. | CHƯA XÁC MINH; không đo tải, số sprite/skill, frame được vẽ hay bị bỏ. |

Không gán 0% cho trường hợp chưa đo. Phần trăm bỏ frame thực nghiệm phải đếm chỉ số frame SPR duy nhất được hiển thị so với frame asset dự kiến trong cùng đoạn ghi hình, phân tầng theo action/hướng/nhân vật và ghi FPS/dt; giữ riêng khung lặp và khung bị culling.

## Liên hệ H-14 và H-15

- H-14 (`CHO-SONNET.md:436-449`) mô tả glow/sét mất khung khi nhân vật di chuyển/vung kiếm ở APK qh7, đặt giả thuyết về clip/occlusion, trạng thái shader/batch, anchor và dt. J-05 chỉ xác nhận có các đường ánh xạ/tick/ẩn nêu trên; không xác định nguyên nhân glow, không đối chiếu qh1-qh7/.bak, không chạy LDPlayer hay đo log. Cần đo đúng bản qh7 và từng khung/hướng/trạng thái theo chỉ dẫn H-14.
- H-15 (`CHO-SONNET.md:463-470`) mô tả skill/đạn xuyên quái khi FPS cao; các nguyên nhân client/server còn là giả thuyết. `WaitForFrame` tăng bước logic nguyên và missile có pool client, nhưng phần khảo sát này chưa truy vết mô phỏng, hit event/gói tin và server collision đủ để kết luận quan hệ với FPS. Không chạy Main VM, server, bot hay tái hiện; cần task đo riêng được phê duyệt.

## ĐỀ XUẤT TỐI ƯU

1. Đo và log frame index, hướng, action, tick logic, `delta`, interval và FPS thật trên client gốc; định lượng riêng frame bị bỏ do lấy mẫu, frame do trễ update, frame lặp và draw bị culling. Không đổi timing trước khi có baseline.
2. Đối với H-14, giữ qh7 làm baseline theo thư #063; log điều kiện vẽ từng lớp glow/sét và vùng clip/occlusion, không gộp kết quả với phép đo frame character.
3. Đối với H-15, truy dấu riêng bước missile, hit event và xử lý collision server ở source tương ứng; mọi tái hiện runtime cần môi trường/test được duyệt.
4. Trước đề xuất SPR→Coco, lập kiểm kê asset theo action và so số khung, interval, kích thước/byte trước-sau; mã converter tĩnh hiện có không đủ xác nhận khâu atlas/compression/resampling.

## MỤC SỔ THÔNG SỐ

| nhóm | tên/hằng số | file:line | giá trị | đơn vị | ảnh hưởng | đổi an toàn (CÓ/CẨN THẬN/KHÔNG) | nguồn đo |
|---|---|---|---|---|---|---|---|
| Render | `setAnimationInterval` | G/AppDelegate.cpp:119 | `1.0f/60` | giây/khung mục tiêu | nhịp gọi animation/render; không bảo đảm FPS thật | CẨN THẬN | source tĩnh; chưa đo runtime |
| Logic | `MAX_SKILL_STATE` | G/gamecore/GameDataDef.h:132 | 18 | slot/NPC | giới hạn slot trạng thái skill; không phải tổng hiệu ứng | KHÔNG | define source tĩnh |
| Pool | `MAX_MISSLE` | G/gamecore/KMissle.h:6 | 30000 | chỉ số/pool | miền chỉ số missile; không phải ngưỡng LOD | KHÔNG | define source tĩnh |
| Đánh/niệm | `naAttackSpeed`, `nbAttackSpeed` | G/gamecore/KNpc.cpp:2377-2399 | đọc `_gameGlobalSet.NpcInfo`; local khởi tạo 100 trước khi đọc | hệ số | thay đổi tick tổng đánh/niệm và ánh xạ frame | KHÔNG | source; giá trị chạy chưa xác minh |
| SPR | `m_dwInterval` | G/gamecore/KSprControl.cpp:304-330 | tối thiểu 1; giá trị lấy từ resource | tick/thời gian engine | tốc độ frame và nhánh loop/non-loop khi trễ | CẨN THẬN | source tĩnh; giá trị theo asset chưa đo |

## Kiểm chứng và giới hạn

- Đã đọc source gốc bằng trích xuất chỉ đọc với Python chạy `python -I`; đối chiếu file trọng tâm với bản C. Không chạy game, exe, build/test, mạng hay VM theo giới hạn task.
- Kiểm tra lại các vị trí đại diện trên client gốc trong lượt này: `KSprControl.cpp:297-330,342-373`, call site `KNpcRes.cpp:357-409`, `KNpc.cpp:2377-2399,3732-3744` và `AppDelegate.cpp:119`; kết quả phù hợp với mô tả tĩnh ở trên. Dùng `Select-String`; không chạy Python ở lượt này.
- Chưa có capture/FPS/dt, kiểm kê asset, bảng số đo cảnh hoặc số liệu RAM/texture. Tỷ lệ frame rơi và nguyên nhân H-14/H-15 vẫn CHƯA XÁC MINH.
- Báo cáo là kết quả khảo sát tĩnh trong vùng file được giao. Chưa commit/push.
