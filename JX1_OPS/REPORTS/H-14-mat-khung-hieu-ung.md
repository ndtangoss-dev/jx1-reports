# H-14 — Mất khung hiệu ứng sáng/sét khi vung kiếm

TÓM TẮT 5 DÒNG
1. PARTIAL: hoàn tất khảo sát tĩnh các file tìm được; chưa xác định APK qh đầu tiên phát sinh lỗi hoặc khung động tác thực tế bị mất.
2. Nghi vấn mạnh nhất: bộ lọc góc trong thay đổi `[clip2]` trả về trước mọi lệnh vẽ sét, có thể bỏ 10 lượt liên tiếp khi kiếm quay thật.
3. Glow và sét có đường vẽ riêng: occlusion có thể che cả hai; bộ lọc góc chỉ trực tiếp bỏ sét, không đủ giải thích glow cũng mất.
4. Shader APK qh7 khớp backup, nhưng native library APK không khớp các artifact build còn lưu; chưa chứng minh source hiện có chính là source APK.
5. Chỉ tạo báo cáo này; không sửa client/canonical/APK/task, không build, chạy game/exe, kết nối mạng/VM, commit hoặc push.

## Phạm vi, đầu vào và định danh bằng chứng

Ngày khảo sát: 17/11/2026. Nhánh được kiểm tra một lần: `task/H-14`; HEAD nền `283237e2d55932b63c716e058f24994ec8347333`. Git ban đầu có `?? JX1_OPS/TASKS/H-14.md`; giữ nguyên file này. Prompt được đọc trực tiếp từ file local; không có commit ghim riêng được cung cấp cho prompt.

Quy ước đường dẫn dùng trong toàn báo cáo:

| Ký hiệu | Đường dẫn |
|---|---|
| S | `D:/JX-source/client` |
| B | `D:/JX-backup/Client-qh7` |
| O | `C:/Jx1CocoV3/Folder/Client2912-20260116T044348Z-3-001/Client2912/Client` |
| K | `S/Classes/gamescene/KgameWorld.cpp` |
| N | `S/Classes/vn/gamecore/KNpcResVN.cpp` |
| F / V | `B/Resources/Shaders/glow.fsh` / `glow.vsh` |

`file:line` dưới đây là dòng vật lý, đánh số từ 1, không phải số dòng diff. SHA-256 được tính bằng đọc bytes; Python luôn chạy bằng `python -I -`, không tạo script phụ. Không trích bảng tài nguyên dài hay dữ liệu cá nhân.

| Đầu vào | SHA-256 / kết quả |
|---|---|
| `D:/JX-backup/qh7/jx-qh7.apk` (95.022.649 bytes) | `c117e45097a827ac122147b6fa89ec0a4c59dfbb15db0b89087a23af227f8c2b` |
| K; bản tương ứng trong B | Cùng hash `b4d016c7decb00213ff9c4b6d4c567cc5e2ed7c04ae42507bae5f97745fb40ba` |
| N; bản tương ứng trong B | Cùng hash `69a2789abb6be0acbe3f3dcaf0a72048894b5fa4651b1f3988df157723dd6311` |
| `O/Classes/gamescene/KgameWorld.cpp` | `f54571bda712c5d9f813c14ddf2cdaa75219dc75f60a10eda108c5cff6fbbfca`; bằng `B/.../KgameWorld.cpp.bak-glow` |
| `O/Classes/vn/gamecore/KNpcResVN.cpp` | `cd7a3b43e8b92ec2f803118597c227068868e865e0eb0e403b2a73e9602a3f56`; bằng `B/.../KNpcResVN.cpp.bak-glow` |
| APK `assets/Shaders/glow.fsh` | `a4574b1e5c769e05674d8777cda25e494b4fc3a6125d34656ec655254cf56448`; bytes bằng F |
| APK `assets/Shaders/glow.vsh` | `57a488145ea1031f9e5556d466b754d70b21d023b23085632ed3c94801820940`; bytes bằng V |
| APK `lib/arm64-v8a/libMyGame.so` | `35fafddc2f1c1274eb66e928c7677e0489fee72244a23876cb673ffc91075645` |
| B build `intermediates/cxx/Release/1q2q1c31/obj/arm64-v8a/libMyGame.so`; `merged_native_libs/debug/mergeDebugNativeLibs/out/lib/arm64-v8a/libMyGame.so` | Cùng `bc60a17704bc8b3f8136322be7dac439a0bc0bf83ffc8eae181aaecbd5fd65ce`; khác APK |
| B build `intermediates/stripped_native_libs/debug/stripDebugDebugSymbols/out/lib/arm64-v8a/libMyGame.so` | `6ff51e4b5331c99af7fa283a153e7e303054bb20fed59e2d79ab6ff4acc15174`; khác APK |

Khác hash native không tự chứng minh khác logic (có thể khác build/strip), nhưng không được dùng các artifact đó làm bằng chứng source ↔ APK. Không sửa hoặc giải nén file ra thư mục nguồn; chỉ đọc ZIP vào bộ nhớ. `D:/JX-source/server` không cần đọc: các cơ chế bỏ vẽ được chỉ ra nằm hoàn toàn ở client; không suy ra giá trị trang bị runtime từ source server.

## ĐÃ XÁC MINH

### 1. Đường đi của một khung render

`KNpc.h:19,824,1094` dùng `KNpcResVN` làm `m_DataRes`; `B/CMakeLists.txt:182,321` liệt kê cả `KNpcRes.cpp` và `KNpcResVN.cpp`. Vì vậy không được lấy nhánh glow đơn giản trong lớp base để thay cho override VN đang khảo sát. Việc APK gọi đúng đường này vẫn cần xác nhận runtime/build provenance.

```text
KNpcResVN::Draw(nNpcIdx,nDir,nAllFrame,nCurFrame,bInMenu)
  ├─ input âm / thiếu resource node hoặc world → return toàn Draw [N:27–31]
  ├─ chọn sprite frame theo hướng + tỷ lệ khung động tác [N:35–67]
  │  hoặc SetCurDir64/GetNextFrame nếu không có nAllFrame [N:140–151]
  ├─ GetnSort(action,dir,frame) thất bại → return toàn Draw [N:204–205]
  ├─ vẽ thường shadow + các part theo m_nSortTable [N:423–478]
  └─ chỉ NPC local, ngoài menu, cấp đã cache ≥6 [N:481–499]
     ├─ gom weapon section có tên ảnh, tối đa 8 [N:509–533]
     ├─ cấp ≥12: prepass RGB gain=0, thu rect/mask từng section [N:541–555]
     │  chọn domSec có nhiều điểm mask nhất; giữ mask/rect section đó [N:553–568]
     └─ mỗi section k [N:572–598]
        ├─ glow 9 lượt offset, cộng sáng [N:575–587]
        ├─ k==domSec && haveRect → jxDrawBolts [N:588–589]
        │  ├─ R<8 / mask<8 / grid sai / span<6 / gate góc → return
        │  └─ từng điểm sét qua JXSET (grid + dọc trục + bề ngang)
        └─ vẽ thường các part xuất hiện SAU section k để che glow/sét [N:590–597]
```

`GetnSort` chuyển tiếp tới `m_cSortTable.GetSort(action,dir,frame,...)` tại `S/Classes/gamecore/KNpcResNode.cpp:612–630`. Do đó thứ tự che thực sự phụ thuộc hướng/khung động tác, không có một thứ tự z cố định cho mọi khung. Chưa đọc bảng động tác/SPR của đúng kiếm bị lỗi vì prompt không nêu item/action cụ thể.

| Trạng thái khung | Glow được gửi vẽ? | Sét được gửi vẽ? | Điều kiện mất/giảm |
|---|---|---|---|
| NPC khác, trong menu, cấp <6 | Không | Không | Chủ định, N:481,499 |
| Cấp 6–11, có section hợp lệ | 9 lượt/section | Không | `domSec=-1`; prepass chỉ chạy từ cấp 12 |
| Cấp ≥12, không có section/tên ảnh | Không | Không | N:513,528–533 |
| Có section nhưng texture frame không lấy được | Section đó không vẽ | Có thể không có rect/mask đủ | K:8959–8962,8991–8997 |
| Cấp ≥12, mask/rect hợp lệ, góc qua gate | Có | Có ứng viên; còn bị clip từng điểm | K:15044–15106,15146–15239 |
| Cấp ≥12, đổi góc vượt ngưỡng trong chuỗi gọi liên tục | Có | Không, return toàn hàm | K:15098; không giữ/replay hình sét cũ |
| Weapon section nằm trước part khác trong sort | Có trước lượt che | Có trước lượt che | N:592–597 có thể phủ lại một phần/toàn bộ vùng hiệu ứng |
| mask/grid/span không đạt | Glow vẫn độc lập | Không | K:15044,15050,15059,15089 |

Đây là sơ đồ điều kiện theo khung, không phải danh sách frame SPR cụ thể đã đo. Không thể đánh số khung động tác mất chỉ từ nhãn bản backup.

### 2. Nghi vấn ưu tiên và phép phân biệt

**P1 — Gate góc chủ động tạo khoảng trống sét.** `K:15092–15099` chuẩn hóa chênh góc PCA theo trục không hướng rồi bỏ lượt nếu đã có mẫu trước, khoảng cách lần gọi <400.000 µs, lệch >0,25 rad (~14,32°), và đã bỏ <10 lượt. Nhánh return cập nhật `s_lastUs` nhưng không cập nhật `s_refTh`. Vì vậy 400 ms là khoảng cách giữa các lần gọi, không phải hạn chót tính từ lúc bắt đầu mất sét. Khi kiếm đổi tư thế thật, cùng điều kiện này vẫn kích hoạt; không có kiểm tra action để phân biệt dữ liệu lỗi với chuyển động hợp lệ.

Mô phỏng số học trực tiếp điều kiện, bằng Python cô lập: trạng thái đã nhận trục 0, góc mới cố định 0,5 rad, cadence 60 lượt/s → lượt 1–10 `SKIP`, lượt 11 `DRAW`. Khoảng trống lý thuyết từ frame cuối được vẽ đến frame kế là 11/FPS giây: khoảng 183,3 ms ở 60 FPS, 366,7 ms ở 30 FPS, 733,3 ms ở 15 FPS nếu có đúng một lần gọi đủ điều kiện mỗi frame. Đây là hệ quả thuật toán, không phải số đo FPS/LDPlayer. Nếu các guard trước đó làm giãn khoảng gọi hoặc góc trở lại gần tham chiếu, kết quả sẽ khác. Comment “giữ tia hiện tại” không có cơ chế lưu rồi vẽ lại tia cũ trong hàm; immediate draw trước đó không đảm bảo tồn tại ở khung sau.

**P2 — Occlusion phủ lại hiệu ứng theo hướng/khung.** `N:590–597` vẽ lại mọi part sau section đang xét, gồm section vũ khí tiếp theo. Điều này có thể che đúng phần kiếm ở sau thân, nhưng cũng có thể làm glow/sét biến mất khi sort hoặc mask không phản ánh đúng phần nhìn thấy. Không có ngưỡng che riêng dạng alpha-test trong khối occl; mức che đến từ alpha texture và normal blend `SRC_ALPHA, ONE_MINUS_SRC_ALPHA` (`K:14959`). Cần phân biệt “không gửi draw” với “đã vẽ rồi bị phủ”. Sét chỉ gắn vào dominant section: nếu phần đó ở sau thân nhưng phần kiếm trước thân thuộc section khác, sét không tự chuyển sang phần nhìn thấy. Đây là giả thuyết cần dữ liệu khung.

**P3 — Clip và dữ liệu neo có thể triệt tiêu mọi điểm.** `K:15071` chỉ gửi draw khi tâm chấm nằm trong grid, tiến độ dọc trục [-0,04;1,04], và khoảng cách ngang ≤band. Grid 200×200, giãn mask 3 pixel; mask lấy từ alpha ≥60 và biên có hàng xóm alpha <40 (`K:8712–8715`). `gok=false` hiện return toàn hàm; bản clip cũ cho đi qua khi grid sai. Kiếm hẹp/ngắn, ảnh >512×512, FBO không complete hoặc mask <8 có thể bỏ sét. Cache theo GLuint lưu cả `ok=false` và không thử lại tới khi cache bị xóa (`K:8687–8725`); texture ID tái sử dụng/context thay đổi là rủi ro cần log, chưa chứng minh đã xảy ra. Mẫu mask cắt ở 600 điểm; dominant được chọn theo số điểm sau lấy thưa, không theo số pixel nhìn thấy sau che. Trường hợp đồng hạng giữ section đầu tiên do so sánh `>` (`N:553`).

Neo không dùng attachment chỉ rõ chuôi/mũi của asset: PCA trên mask, đầu gần tâm màn hình cộng 10 pixel Y là chuôi (`K:15074–15090`). Có thể đổi đầu khi tư thế/camera thay đổi, gây dịch/nhảy tia; không mặc nhiên chứng minh thiếu frame. `nCurDirNo/nCurFrameNo` được cập nhật khi duyệt các part (`N:59–67,150–151`) rồi dùng cho sort; cần log từng layer nếu tài nguyên có số hướng/khung khác nhau.

**P4 — Không thấy đường return rò `g_jxAdditive` trong khối khảo sát.** Prepass hoàn lại false ở `N:555`; glow hoàn lại false ở `N:586`. Các guard return của sét đều trước `K:15108` bật cờ; sau bật cờ chỉ có continue nội vòng, rồi false ở `K:15242`. Normal draw chọn lại shader ở `K:9008–9031` và blend ở `K:14959`. Không chứng minh có lỗi “cờ true bị bỏ quên”. Tuy nhiên GL blend thực còn additive sau draw sét cuối đến normal draw kế; boolean false không tự gọi GL. Ngoài ra sét thay đổi RGB và cuối hàm chỉ reset alpha=1, không trả đủ màu ban đầu (`K:15236–15243`); section glow sau sét có thể nhận RGB trắng dù trước đó vàng/xanh, vì `N:583` chỉ đặt alpha. Đây là sai khác màu tiềm năng, không phải bằng chứng mất toàn bộ hiệu ứng. Chưa kiểm driver/context hoặc các caller ngoài phạm vi.

**P5 — Timer wall clock, không tích lũy dt.** `JxPerfNowUs()` dùng `steady_clock` (`S/Classes/gamecore/JxPerf.h:12`); `fr=(nowUs/50000)%16` (`K:15048`). Chu kỳ 800 ms, 20 pha/s. FPS thấp có thể nhảy pha; không có bộ làm mới tia theo dt trong hàm. Arc 9–14 pha tuổi thọ và 12% hình không có đoạn; runner luôn được xét ở cả 16 pha vì `t>=16` là bất khả thi khi modulo 16 (`K:15200`), trái comment “4 khung nghỉ”. Hạt nhỏ đã tắt bằng `j<0` (`K:15111`). Không được quy toàn bộ khoảng trống hiện tại cho comment nghỉ pha.

### 3. Đối chiếu snapshot trước qh7

Hậu tố `.bak-X` không đảm bảo file đã chứa thay đổi X; thực tế các cặp dưới đây cho thấy thường là bản trước thao tác mang tên đó. Mốc chắc chắn là nội dung giữa hai file, không phải ngày phát hành. Bảng chỉ ghi phần liên quan, không chép toàn diff hoặc bảng asset.

| File trong B | Bằng chứng / thay đổi so với mẫu trước đã đọc |
|---|---|
| `KgameWorld.cpp.bak-glow`; `KNpcResVN.cpp.bak-glow` | Bằng canonical O, chưa có khối glow bổ sung |
| `KgameWorld.cpp.bak-bolt:8675,8933,14875` | Có global additive/shader glow, chưa có `jxDrawBolts` |
| `KgameWorld.cpp.bak-bolt2:14909` | Có sét theo rect; refresh 70 ms và bỏ ngẫu nhiên 30% mỗi tia; có thể nhấp nháy chủ ý từ sớm |
| `KgameWorld.cpp.bak-bolt3:14908` | Biến thể hạt + sét, refresh 90 ms, xác suất bỏ khác theo cấp; chưa có mask PCA |
| `KgameWorld.cpp.bak-bolt5:8680` | Có thu mask FBO; vẫn có fallback neo khi mask ít |
| `KgameWorld.cpp.bak-bolt6:14977,15041` | Có 16 pha/10 arc/96 spark, PCA và return khi mask <8; khác biệt giữa các frame texture bắt đầu có khả năng bỏ toàn bộ sét ở đây trong tập mẫu hiện có |
| `KgameWorld.cpp.bak-bolt7:15149–15156` | Thêm runner 3/2, nghỉ 4/16 pha cho từng runner; không phải cả bộ cùng nghỉ (đếm toán học tối thiểu 2/1 runner được xét mỗi pha) |
| `KgameWorld.cpp.bak-bolt8:15149–15156` | Runner 6/4, bỏ nghỉ, tail 0,9, biên độ 5,5; hạt vẫn bật |
| `KgameWorld.cpp.bak-clip:15065` | Khác bolt8 đúng một dòng: tắt hạt `j<JX_NSPK` → `j<0`; CHƯA có grid clip |
| `KgameWorld.cpp.bak-clip2:15042–15061` | So với bak-clip: thêm grid, GRD=4, `!gok` vẫn cho draw; CHƯA có gate góc/band |
| `KgameWorld.cpp.bak-pfl:15046–15097` | So với bak-clip2: GRD 4→3, grid sai → return, thêm clip dọc/ngang và gate góc 0,25 rad/10 lượt/400 ms. Mốc mạnh nhất cho lỗi bỏ sét khi vung |
| `KgameWorld.cpp:11224–11253` | So với bak-pfl chỉ sửa quản lý sprite `PaintPifeng` (12 dòng thêm/3 dòng bỏ); khối sét không đổi ngoài dịch số dòng |
| `KNpcResVN.cpp.bak-bolt` → `.bak-bolt3` | Thêm capture rect và gọi sét; glow ban đầu vẽ các section cùng lượt |
| `KNpcResVN.cpp.bak-occl:533,537` | Đã reset mask và chỉ thu mask ở lượt glow trung tâm; chưa có redraw occluder |
| `KNpcResVN.cpp.bak-occl2:552` | So với bak-occl: thêm vẽ lại part sau section vũ khí cuối; mốc che phủ mới đầu tiên tìm thấy |
| `KNpcResVN.cpp.bak-occl3:529` | So với bak-occl2: chủ yếu thêm SORT/WG log; chưa có per-section flow hiện tại |
| `KNpcResVN.cpp.bak-clip2:509–583` | So với bak-occl3: per-section glow, prepass chọn dominant, vẽ lại part sau từng section; mask vẫn hợp nhiều section |
| `KNpcResVN.cpp.bak-ring:544–568` | Thêm giữ riêng mask/rect dominant section; nội dung `[clip2]` đã có tại đây |
| `KNpcResVN.cpp:538` | So với bak-ring đúng một dòng: bán kính glow `1+3*s` → `0,8+1*s`; giảm độ lan, không tắt khung bằng timer |

Không tìm thấy `.bak-bolt1` (có `.bak-bolt`), `.bak-bolt4`, `.bak-wglow1..7`, `.bak-qh1..7` trong cây B và các file backup liên quan dưới canonical O đã duyệt; tìm tên qh/wglow có giới hạn thêm ở `D:/JX-build` sâu 2 cấp cũng không ra. Không khẳng định chúng không tồn tại ở nơi khác. Chỉ có APK qh7 được task chỉ rõ. Vì thiếu snapshot và provenance, **không kết luận “APK qhN đầu tiên lỗi”**; chỉ kết luận gate có mặt từ khoảng nội dung `bak-clip2 → bak-pfl` và occlusion từ `bak-occl → bak-occl2` trong các mẫu này.

`pfl` hiện chỉ đổi vòng đời sprite nhãn phi phong, không đổi gate sét; `PaintPifeng` add child z=1 tại `K:11252`. Khả năng nhãn/node che vùng kiếm chỉ là giả thuyết phụ, cần ảnh/log thứ tự node; không nên rollback pfl trước khi đo gate và occl.

## CHƯA XÁC MINH

- Native APK qh7 có đúng gate/logic và source tương ứng nào; thiếu manifest build/source hash, artifact native còn lưu không khớp APK.
- Frame/action/hướng/item cụ thể bị mất, mức cường hóa thật, phần kiếm nào trước/sau thân; chưa có clip triệu chứng hoặc tên SPR/item trong prompt.
- Mask FBO, alpha theo frame, số edge, trạng thái texture/context, dominant section, actual GL blend/uniform, phần bị che thực trên LDPlayer.
- FPS/dt, chi phí readback/draw/log, tỷ lệ mất khung và khác biệt giữa APK qh1..qh7; chưa chạy build/test/runtime nào.
- Giá trị đọc thực từ `npcbobo.ini`, hoặc trang bị server. Các giá trị fallback ở mục sổ là source, không phải cấu hình đã đo.

## Bản log thử đề xuất — CHƯA SỬA / CHƯA DỰNG

Nếu được duyệt task triển khai riêng, làm trên copy; ghi local, không tài khoản/IP/token/chat hay full path tài nguyên. Mỗi frame local có `renderSeq`, `nowUs`, `dtUs`, action, `nDir`, input frame/allFrame; từng layer ghi frame/dir và hash tên SPR thay vì nguyên tên. Không dùng riêng `nCurDirNo` còn sót sau vòng part làm định danh kiếm.

| Điểm đặt log | Trường bắt buộc / mục đích |
|---|---|
| N:27,30,204,481,499,533 | Một reason khi skip ngoài: INVALID_INPUT, NO_RESOURCE, SORT_FAIL, NON_LOCAL_OR_MENU, LEVEL_LOW, NO_SECTION |
| N:549–568 | Section id/sort index; nG; mask bắt đầu/kết thúc; edge count; haveRect, rect; dominant và lý do đổi dominant |
| K:8687–8728 | Cache hit/miss, texture generation/id local, w/h, FBO status, mc.ok, tổng điểm/stride/truncated; log lúc đổi trạng thái |
| K:15044,15050,15059,15089,15098 | Một reason cho từng return: SMALL_RECT, MASK_LOW, GRID_INVALID, SPAN_LOW, ANGLE_REJECT; th/ref/dth, bad trước/sau, gapUs, gw/gh, span |
| K:15071 | Đếm candidate/accepted và loại theo dọc trục/band/grid/out-of-bounds; xác định thứ tự phân loại để không cộng trùng |
| K:15150,15152,15165,15219 | Đếm arc bỏ vì tuổi/hình/không edge và runner segment bị đứt; tách active entity khỏi số draw thực |
| N:584,589,597; K:14950–14970 | Số draw glow/sét/occluder, shader id, uniform location, RGBA, boolean additive; kiểm blend thực ở mốc chuyển nếu bật chế độ chẩn đoán |
| Cuối Draw | Tổng hợp reason, draw counts, `g_jxAdditive`, `g_jxCapRect`, maskN, thời gian mask/bolt/occlusion; assert mềm/log khi flag không về trạng thái mong đợi |

Đề xuất buffer vòng RAM 300 frame, chỉ flush khi skip thay đổi hoặc thao tác đánh dấu lỗi; đây là tham số log mới đề xuất, chưa tồn tại. Xuất đầy đủ mỗi frame trong cửa sổ đo ngắn để không bỏ xung 1 frame. Log `SEC` hiện có chỉ khoảng 1 giây/lần (`N:571`), `WR` khoảng 2 giây và `GU` mỗi 200 draw (`K:14956`) không đủ chứng minh khung mất. Đo overhead bằng cùng cảnh bật/tắt log; không bật query GL mọi chấm vì có thể làm thay đổi FPS.

## Ca test cho TESTER và cách đo trên LDPlayer — CHỈ LÀ KẾ HOẠCH

Chưa bật LDPlayer, ADB, cài APK, tạo file trace hay kết nối server trong task này. Thực hiện ở lượt đã được duyệt riêng, môi trường test cô lập, bản copy, không server production. Giữ hash APK và cấu hình render/độ phân giải/FPS cố định giữa các lượt. Nếu thiếu cảnh offline tương đương thì ghi blocker, không tự đăng nhập/mở mạng.

| Ca | Thao tác dự kiến | Dấu hiệu cần đo / phân biệt |
|---|---|---|
| T1 | Cấp 5/6/11/12/15, đứng yên, ngoài menu; NPC local và NPC khác | Ranh glow/sét đúng thiết kế, loại nhầm đối tượng/cấp; chờ qua chu kỳ cache cấp |
| T2 | Cùng kiếm, đứng → di chuyển → vung, từng hướng có trong asset; lặp ít nhất 20 chu kỳ mỗi tổ hợp | Phân bố theo action/frame/dir; số lượt ANGLE_REJECT và chuỗi skip tối đa |
| T3 | Đứng yên đổi hướng nhanh rồi giữ hướng mới | Kiểm mẫu 10 lượt bỏ rồi vẽ; log th/ref/dth và mask đủ |
| T4 | Lặp T2 ở mục tiêu 60/30/15 FPS, ghi FPS/dt thực | Gate theo lượt tăng thời gian mất; so với pha sét 50 ms; không dùng FPS mục tiêu thay FPS đo |
| T5 | Bộ phận kiếm trước/sau thân, có/không cưỡi ngựa, có/không phi phong | Vẽ sét/glow trước occl và vùng cuối bị che; so sánh dominant section với phần đang nhìn thấy |
| T6 | Frame kiếm ngắn/hẹp, đổi vũ khí trong cảnh test, lần đầu texture xuất hiện và cache ấm | MASK_LOW/GRID_INVALID/FBO fail/texture id reuse; lỗi có cố định theo frame SPR hay không |
| T7 | Một thời điểm wall clock đủ vòng 16 pha, kiếm đứng yên | Counts accepted theo pha; xác nhận không tự nghỉ 4 pha trong runner hiện tại |
| T8 | Bản log đối chứng; từng biến thể riêng sau phê duyệt: replay/gate motion-aware; clip; occl; cuối cùng pfl | Chỉ đổi một cơ chế mỗi lần, không trộn nhiều thay đổi; kiểm lại tràn tia/kiếm sau thân |

Ghi capture theo frame tại tốc độ đủ cho FPS thực, căn `renderSeq/nowUs` bằng overlay chẩn đoán trên bản thử. Chỉ đếm frame game mới, loại frame video lặp. Tách ROI phần lưỡi kiếm nhìn thấy khỏi phần bị thân che; đo glow và sét riêng, dùng normal-weapon đối chứng cùng tư thế để tránh nhầm nền sáng. Các đại lượng: frame đủ điều kiện (local, cấp, section và lưỡi kiếm nhìn thấy), frame không có hiệu ứng, tỷ lệ mất, chuỗi mất dài nhất, số `ANGLE_REJECT`/guard/accepted=0, draw occluder, p50/p95 thời gian khung và CPU từng khối. Khớp từng frame mất với reason log; có draw nhưng mất ảnh thì kiểm occl/blend, không gán gate.

Tiêu chí đạt đề xuất: không còn frame mất ngoài chủ ý khi phần lưỡi kiếm nhìn thấy và đủ điều kiện; không vẽ xuyên thân/tràn xa kiếm; không rò cờ, không tăng p95 thời gian khung vượt ngân sách được duyệt. Chưa có baseline nên không đặt phần trăm cải thiện tùy ý. A/B phải dùng cùng input và cảnh; nếu qh cũ chỉ có APK thì cần duyệt chạy riêng và ghi hash từng APK trước khi lập kết luận phiên bản.

## ĐỀ XUẤT TỐI ƯU

| Ưu tiên / đề xuất cho task sau | Lợi ước tính (chưa đo) | Rủi ro | Cách đo lại |
|---|---|---|---|
| 1. Gate nhận biết đổi action/hướng; nếu mask đáng tin thì nhận tư thế mới, hoặc lưu hình học tương đối để replay tại neo mới thay vì return trắng | Loại được tối đa 10 lượt skip do riêng gate trong tình huống đã phân tích; chưa biết tỷ trọng ngoài thực tế | Replay sai neo/vẽ xuyên thân; bỏ gate mù có thể trả lại tia bay lung tung | T2–T4, ratio ANGLE_REJECT, accepted, khoảng mất và điểm tràn ROI |
| 2. Log coverage/occlusion và chọn section nhìn thấy, giữ thứ tự che từng part | Có thể hết mất khi dominant bị thân che; chưa định lượng | Tia sang sai phần kiếm, phá che đúng | T5, ảnh trước/sau occl theo cùng frame |
| 3. Cache mask theo danh tính/generation texture có invalidation; retry lỗi FBO có kiểm soát | Giảm nguy cơ mask âm lưu lâu, tránh readback lặp không cần | Retry làm tăng stall, invalidation sai vòng đời | T6, cache hit/fail, glReadPixels latency p95 |
| 4. Clip điều chỉnh theo kích thước và độ tin cậy mask, có fallback giới hạn tại neo mới | Giảm accepted=0 và grid quá lớn | Tràn tia nếu nới mù 200/band/GRD | T6–T8, accepted/candidate, pixel ngoài ROI |
| 5. Phục hồi đủ RGBA/trạng thái GL tại ranh lượt, giảm 9 pass chỉ sau khi có baseline | Màu ổn định giữa section; tiết kiệm draw có thể có nhưng chưa đo | Hình glow mỏng/khác mỹ thuật; state query gây chậm | T1,T5,T8, ảnh màu và draw count/p95 |

Không tự tăng alpha, số tia hoặc bỏ occlusion để che triệu chứng. Không đề xuất rollout/build hiện tại; mọi sửa mã và test runtime thuộc task sau được duyệt.

## Kết quả

- Trạng thái: **PARTIAL** do thiếu snapshot qh/wglow, item/SPR triệu chứng và liên kết source ↔ native APK. Phần khảo sát tĩnh các file tìm được, sơ đồ skip, đối chiếu, sổ thông số và kế hoạch log/test đã hoàn tất.
- Chỉ tạo `JX1_OPS/REPORTS/H-14-mat-khung-hieu-ung.md`. Yêu cầu trong prompt về thêm `## Kết quả` vào file task xung đột với `vung_file: [none, JX1_OPS/REPORTS/H-14-*.md]` và chỉ thị người dùng chỉ ghi vùng file; đặt kết quả ở đây, giữ nguyên task đang untracked.
- Đã kiểm: đọc source/diff snapshot, SHA-256, đọc ZIP shader/native, tính số học gate/runner bằng `python -I`. Không chạy build/unit test/game/VM/LDPlayer/mạng; không nhận các kiểm tra đó là đạt.
- Lỗi công cụ: `rg : The term 'rg' is not recognized...` (hai tìm kiếm độc lập đầu lượt); chuyển sang `Get-ChildItem/Select-String`, không cài công cụ. Đọc prompt mặc định bị sai encoding; đọc UTF-8 đã khôi phục đúng. Canonical ban đầu thiếu tầng `Client` nên `Cannot find path ...`; đã sửa đường dẫn bằng danh sách thư mục trực tiếp. Hai tên header suy đoán `KNpcResDef.h`, `KNpcVN.h` không tồn tại; chuyển sang header được include/định nghĩa thực `CoreUseNameDef.h`, `KNpcResNode.h`, `KNpc.h`. Một diff tổng hợp bị cắt output; đọc lại đúng cặp liên quan với output giới hạn, không dùng phần mất làm bằng chứng. Kiểm heading lần đầu bằng literal Unicode qua stdin PowerShell cho số đếm 0 do encoding của pipeline, không phải file hỏng; đọc UTF-8 và in escape xác nhận các heading đúng, không có ký tự thay thế. Kiểm bảng tiếp theo gặp `StopIteration` do giả định heading nằm sau dòng 200; sửa cách tìm theo heading không phụ thuộc vị trí. Không thử một lỗi quá ba lần.
- Commit SHA của thay đổi: không có; không được yêu cầu commit. HEAD nền nêu ở đầu báo cáo không phải commit báo cáo. Chưa push vì task chỉ khảo sát local, không yêu cầu công bố; không có liên kết GitHub mới.
- Bước tiếp tục: tìm snapshot/build manifest qh1..qh7, wglow và bolt4 do chủ dự án chỉ định; sau đó task riêng triển khai log trên copy và đo T2/T3/T5 trước. Không suy diễn phiên bản đầu tiên hoặc nguyên nhân runtime từ source.

## MỤC SỔ THÔNG SỐ

Nguồn đo `TĨNH` = literal/công thức trong source nêu ở cột file:dòng, chưa đo runtime; `DIFF` = cặp snapshot tương ứng trong B. Một vector RGB/offset là một tham số có cấu trúc. Giá trị dẫn xuất được ghi rõ. Không coi chỉ số mảng, hằng toán học/PRNG, mã enum hay số byte định dạng là nút chỉnh mỹ thuật; đổi các cấu trúc đó cần sửa mã đồng bộ. Các thông số vô hiệu do `j<0` được đánh dấu để tránh hiểu là đang chạy. Cột an toàn không phải cấp quyền đổi; toàn bộ task chỉ đọc.

| Nhóm | Tên/hằng số | file:line | Giá trị hiện tại | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Điều kiện | glow min level | N:499 | 6 | cấp | Bật glow local | CẨN THẬN | TĨNH |
| Điều kiện | bolt min level | N:541 | 12 | cấp | Bật prepass/dominant/sét | CẨN THẬN | TĨNH |
| Điều kiện | high level | N:502; K:15045 | 15 | cấp | Màu/cường độ/mật độ cao | CẨN THẬN | TĨNH |
| Trang bị | s_wNext interval | N:487 | 2.000.000 | µs | Trễ cập nhật cấp vũ khí | CẨN THẬN | TĨNH |
| Chẩn đoán | ép cấp trace | N:494 | 1..31; lấy file đầu tồn tại | cấp | Ghi đè cấp thật khi trace bật | CẨN THẬN | TĨNH |
| Glow | s | N:502 | 0,35 / 0,65 / 1 | hệ số | Theo mốc 6/12/15 | CẨN THẬN | TĨNH |
| Glow | pulse base | N:503 | 0,9 | hệ số | Độ sáng nền của nhịp | CẨN THẬN | TĨNH |
| Glow | pulse amplitude | N:503 | 0,1 | hệ số | Nhịp dao động 0,8..1, không về 0 | CẨN THẬN | TĨNH |
| Glow | pulse rate | N:503 | 0,006 | rad/ms | Chu kỳ khoảng 1.047 ms | CẨN THẬN | TĨNH, dẫn xuất |
| Glow | RGB high | N:504 | (0,55;0,8;1) | RGB | Sắc xanh điện | CẨN THẬN | TĨNH |
| Glow | RGB medium | N:505 | (1;0,8;0,35) | RGB | Sắc vàng | CẨN THẬN | TĨNH |
| Glow | RGB low | N:506 | (1;1;1) | RGB | Sắc trắng | CẨN THẬN | TĨNH |
| Glow | alpha/gain base | N:507 | 0,15 | hệ số RGB | Cộng vào gain | CẨN THẬN | TĨNH |
| Glow | alpha/gain slope | N:507 | 1,05 | hệ số RGB/s | Gain trước pulse | CẨN THẬN | TĨNH |
| Glow | số pass | N:576 | 9 | lượt/section | Độ lan và chi phí | CẨN THẬN | TĨNH |
| Glow | jxDX | N:536 | [0;1;-1;0;0;0,7;-0,7;0,7;-0,7] | hệ số R | Offset X, bị ép int | CẨN THẬN | TĨNH |
| Glow | jxDY | N:537 | [0;0;0;1;-1;0,7;-0,7;-0,7;0,7] | hệ số R | Offset Y, bị ép int | CẨN THẬN | TĨNH |
| Glow | jxR base | N:538 | 0,8 | pixel tọa độ vẽ | Bán kính nền | CẨN THẬN | TĨNH |
| Glow | jxR slope | N:538 | 1 | pixel/s | R hiện 1,15/1,45/1,8 | CẨN THẬN | TĨNH, dẫn xuất |
| Glow | jxR trước ring | B/Classes/vn/gamecore/KNpcResVN.cpp.bak-ring:538 | Lịch sử 1+3*s; hiện 0,8+1*s | pixel | Giảm độ lan, không gate thời gian | CẨN THẬN | DIFF |
| Glow | gain trung tâm | N:583 | 0,8 | hệ số jxA0 | Glow chính | CẨN THẬN | TĨNH |
| Glow | gain offset | N:583 | 0,45 | hệ số jxA0 | Tám lượt phụ | CẨN THẬN | TĨNH |
| Prepass | gain đo | N:545 | 0 | RGB gain | Vẫn thu mask nhưng không cộng RGB | KHÔNG | TĨNH |
| Section | cap secIdx/secPj | N:525,531 | 8 | section | Giới hạn lưu; asset weapon có 4 phần ×2 layer | KHÔNG | TĨNH |
| Resource | MAX_BODY_PART | S/Classes/gamecore/KNpcResNode.h:23 | 6 | loại part | Cấu trúc sort | KHÔNG | TĨNH |
| Resource | MAX_BODY_PART_SECT | S/Classes/gamecore/KNpcResNode.h:24 | 4 | section/part | Weapon range [8,12) theo enum 2 | KHÔNG | TĨNH |
| Resource | MAX_PART | S/Classes/gamecore/KNpcResNode.h:25 | 24 | section | Độ dài sort | KHÔNG | TĨNH |
| Resource | emNPCRES_PART_LAYER_COUNT | S/Classes/gamecore/CoreUseNameDef.h:20–24 | 2 | layer | BASE/EFFECT | KHÔNG | TĨNH |
| Hướng | quantization | N:62 | offset 32/nGetDir; chia 64/nGetDir | đơn vị hướng | Chọn dir/frame; cấu trúc tài nguyên | KHÔNG | TĨNH |
| Mask | cap global | K:8680,8728 | 600 | điểm | Có thể cắt mẫu section sau | CẨN THẬN | TĨNH |
| Mask | cache clear threshold | K:8690 | size >1500 | texture entry | Xóa toàn cache trước insert mới | CẨN THẬN | TĨNH |
| Mask | max texture W/H | K:8692 | 512 mỗi chiều | pixel texture | Lớn hơn → cache không ok | CẨN THẬN | TĨNH |
| Mask | alpha nội | K:8712 | ≥60 | mức 0..255 | Điểm đủ đậm | CẨN THẬN | TĨNH |
| Mask | alpha biên | K:8713–8714 | hàng xóm <40 | mức 0..255 | Xác định edge neo arc | CẨN THẬN | TĨNH |
| Mask | lấy thưa nội | K:8715 | (x+3*y)%5==0 | pixel | Mật độ, hướng mẫu | CẨN THẬN | TĨNH |
| Mask | mục tiêu mẫu/texture | K:8727 | 260; stride=cnt/260+1 khi cnt>260 | điểm | Giảm số điểm thực thu | CẨN THẬN | TĨNH |
| Bolt | JX_FR | K:14986 | 16 | pha | Vòng hoạt ảnh | CẨN THẬN | TĨNH |
| Bolt | JX_NARC | K:14986 | 10 | arc ứng viên | step chọn theo cấp | CẨN THẬN | TĨNH |
| Bolt | JX_NSPK | K:14986 | 96 | hạt khởi tạo | Hiện không được vẽ | CẨN THẬN | TĨNH |
| Bolt | seed khởi tạo | K:14998 | 20261114 | seed | Mẫu ngẫu nhiên xác định | CẨN THẬN | TĨNH |
| Bolt | E.life base | K:15003 | 9 | pha 50 ms | Tuổi arc tối thiểu | CẨN THẬN | TĨNH |
| Bolt | E.life range | K:15003 | int(JXR*6); comment 9..14 tổng | pha | Mẫu RNG có thể đạt 1, cần lưu ý endpoint lý thuyết | CẨN THẬN | TĨNH |
| Bolt | E.born jitter | K:15004 | int(JXR*2) | pha | Rải sinh ngoài a*16/10 | CẨN THẬN | TĨNH |
| Bolt | E.side split | K:15005 | 0,5 | xác suất | Chọn mép | CẨN THẬN | TĨNH |
| Bolt | E.rel spread | K:15005 | (JXR-0,5)*0,9 | rad | Hướng arc lệch trục | CẨN THẬN | TĨNH |
| Bolt | E.spd | K:15005 | 1 | hệ số | Khởi tạo nhưng không dùng trong draw arc hiện tại | CẨN THẬN | TĨNH |
| Bolt | shape empty | K:15009 | JXR<0,12 | xác suất | Không vẽ arc đó/pha đó | CẨN THẬN | TĨNH |
| Bolt | A.n | K:15009 | 4+int(JXR*3) | đoạn | Thường 4..6; mảng có 7, RNG endpoint có thể ra 7 | CẨN THẬN | TĨNH |
| Bolt | shape length | K:15010 | 6+9*JXR | pixel | Chiều dài mẫu | CẨN THẬN | TĨNH |
| Bolt | A.sl | K:15011 | len/5*(0,6+0,8*JXR) | pixel | Độ dài từng đoạn | CẨN THẬN | TĨNH |
| Bolt | A.dv | K:15011 | 0,5+0,7*JXR | rad | Góc ziczac | CẨN THẬN | TĨNH |
| Texture sét | s_dot | K:15024–15036 | 8×8; tâm 3,5; bán kính 4; alpha sqrt(max(0,1-d))*255 | pixel/alpha | Chấm lõi mềm; lỗi cấp phát/init → return | CẨN THẬN | TĨNH |
| Guard | R min | K:15044 | 8 | pixel | Nhỏ hơn bỏ sét | CẨN THẬN | TĨNH |
| Bolt | step high/low | K:15046 | 1 / 2 | arc index | 10 / 5 arc được xét trước guard | CẨN THẬN | TĨNH |
| Bolt | inten high/low | K:15047 | 1 / 0,6 | gain | Độ sáng sét | CẨN THẬN | TĨNH |
| Timer | pha refresh | K:15048 | 50.000 | µs | 20 pha/s, chu kỳ 800 ms | CẨN THẬN | TĨNH, dẫn xuất |
| Guard | nm min | K:15050 | 8 | điểm | Dưới ngưỡng bỏ sét | CẨN THẬN | TĨNH |
| Clip | grid cap W/H | K:15052,15058 | 200 mỗi chiều | pixel | Vượt → return | CẨN THẬN | TĨNH |
| Clip | GRD | K:15055 | 3; lịch sử 4 tại bak-clip2:15046 | pixel | Giãn vuông quanh mask | CẨN THẬN | TĨNH/DIFF |
| Clip | grid origin padding | K:15056 | -GRD-1 | pixel | Biên grid | CẨN THẬN | TĨNH |
| Clip | grid extent padding | K:15057 | +2*GRD+3 | pixel | Biên grid và guard cap | CẨN THẬN | TĨNH |
| Clip | tiến độ min/max | K:15071 | -0,04 / 1,04 | tỷ lệ chiều kiếm | Chặn vượt chuôi/mũi | CẨN THẬN | TĨNH |
| Neo | refy offset | K:15084 | +10 | pixel | Chọn đầu gần nhân vật làm chuôi | CẨN THẬN | TĨNH |
| Guard | span min | K:15089 | 6 | pixel | Trục quá ngắn → return | CẨN THẬN | TĨNH |
| Gate góc | gap max | K:15098 | <400.000 | µs giữa hai gọi | Giữ gate hoạt động khi gọi liên tục | CẨN THẬN | TĨNH |
| Gate góc | dth max | K:15098 | >0,25 | rad | Kích hoạt bỏ lượt | CẨN THẬN | TĨNH |
| Gate góc | s_bad cap | K:15098 | 10 | lượt | Tối đa chuỗi bỏ do gate nếu các guard trước đều qua | CẨN THẬN | TĨNH |
| Clip ngang | pm margin | K:15106 | +3 | pixel | Nới band từ mask | CẨN THẬN | TĨNH |
| Clip ngang | band min | K:15102,15106 | 7 | pixel | Nửa bề ngang tối thiểu | CẨN THẬN | TĨNH |
| Clip ngang | band max | K:15106 | 12 | pixel | Nửa bề ngang tối đa | CẨN THẬN | TĨNH |
| Hạt TẮT | K.u / K.rel | K:15017 | JXR / (JXR-0,5)*2 | mẫu/hệ số | Không vẽ do j<0 | CẨN THẬN | TĨNH |
| Hạt TẮT | K.spd | K:15017 | 22+60*JXR | pixel/s | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | K.len | K:15017 | 3+5*JXR | pixel | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | K.life / born | K:15018 | 6+int(JXR*8) / int(JXR*16) clamp 15 | pha | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | loop bound | K:15111 | 0 | hạt vẽ | Tắt hoàn toàn | CẨN THẬN | TĨNH |
| Hạt TẮT | chọn neo | K:15119–15121 | 3 lần; K.u*977+tr*0,371 | mẫu | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | tuổi/thành phần ngang | K:15126–15128 | age*0,05; ngang*0,25 | s/hệ số | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | giới hạn/fade mũi | K:15130–15132 | 1,02; fade sau 0,8 chia 0,22 | tỷ lệ | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | fade tuổi | K:15131 | tăng 0,15; giảm 0,85 | tỷ lệ life | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | warm split/RGB | K:15134–15135 | 0,12; (1;0,8;0,9) / (0,85;0,97;1) | tỷ lệ/RGB | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | gain | K:15136 | (0,5+1,3*fade)*inten | hệ số | Không vẽ | CẨN THẬN | TĨNH |
| Hạt TẮT | vệt | K:15137–15140 | 3 chấm; sz=1,6-0,35*d; khoảng K.len*d*0,5 | pixel | Không vẽ | CẨN THẬN | TĨNH |
| Arc | scale sc | K:15145 | clamp(R/30;0,6;1) | hệ số | Co mẫu theo kiếm nhỏ | CẨN THẬN | TĨNH |
| Arc | sT offset | K:15153 | age+0,5 | pha | Tiến độ neo trong life | CẨN THẬN | TĨNH |
| Arc | phạt sai mép | K:15162 | 0,25 | điểm cost | Chọn edge cùng phía | CẨN THẬN | TĨNH |
| Arc | bestd ban đầu | K:15155 | 9 | điểm cost | Ngưỡng nhận điểm neo | CẨN THẬN | TĨNH |
| Arc | fade cuối | K:15167 | sau 0,82, chia 0,18 | tỷ lệ life | Mờ ở mũi | CẨN THẬN | TĨNH |
| Arc | fade đầu | K:15167 | trước 0,08, chia 0,08 | tỷ lệ life | Mờ ở chuôi | CẨN THẬN | TĨNH |
| Arc | sampling step | K:15176 | sl/1+1 | pixel | Mật độ chấm | CẨN THẬN | TĨNH |
| Arc | sz halo/core | K:15179 | 2,8 / 1,3 | pixel | Độ dày hai pass | CẨN THẬN | TĨNH |
| Arc | RGB halo/core | K:15180–15181 | (0,35;0,9;0,85) / (0,95;1;1) | RGB | Màu sét | CẨN THẬN | TĨNH |
| Arc | gain halo/core | K:15180–15181 | 0,16 / 1,25 ×inten×fade | hệ số | Độ sáng | CẨN THẬN | TĨNH |
| Runner | amp | K:15195 | 5,5 | pixel | Dao động ngang | CẨN THẬN | TĨNH |
| Runner | nRun high/low | K:15196 | 6 / 4 | tia | Tia dọc thân | CẨN THẬN | TĨNH |
| Runner | t gate/head | K:15200–15201 | t>=16; head=(t+1)/16 | pha/tỷ lệ | Gate không đạt trong modulo16 | CẨN THẬN | TĨNH |
| Runner | sTail length | K:15202 | 0,9 | tỷ lệ kiếm | Độ dài đuôi | CẨN THẬN | TĨNH |
| Runner | phase spacing | K:15203 | 2,1 | rad/tia | Độ lệch giữa runner | CẨN THẬN | TĨNH |
| Runner | NP | K:15204 | 16 | đoạn | Độ mịn quỹ đạo | CẨN THẬN | TĨNH |
| Runner | wave rate | K:15209 | 14,137 | rad/chiều kiếm | Số vòng uốn | CẨN THẬN | TĨNH |
| Runner | jitter amplitude | K:15211 | 2,4 | pixel | Nhiễu ngang | CẨN THẬN | TĨNH |
| Runner | endFade | K:15216 | sau 0,85 chia 0,15; sàn 0,1 | tỷ lệ/gain | Mờ ở cuối nhưng không về 0 | CẨN THẬN | TĨNH |
| Runner | đoạn đứt | K:15219 | (k+fr)%5>=3 | chỉ số | Giữ 3/5 residue đoạn | CẨN THẬN | TĨNH |
| Runner | br | K:15220 | 0,35+0,65*k/NP | gain | Sáng dần theo đoạn | CẨN THẬN | TĨNH |
| Runner | sample step | K:15222 | chiều dài/1+1 | pixel | Mật độ draw | CẨN THẬN | TĨNH |
| Runner | sz halo/core | K:15225 | 3,78 / 1,8 | pixel | Độ dày | CẨN THẬN | TĨNH |
| Runner | RGB halo/core | K:15226–15227 | (0,35;0,9;0,9) / (0,95;1;1) | RGB | Sắc tia | CẨN THẬN | TĨNH |
| Runner | gain halo/core | K:15226–15227 | 0,30 / 1,12 ×br×inten×endFade | hệ số | Sáng tia | CẨN THẬN | TĨNH |
| Runner head | RGB halo/core | K:15236,15238 | (0,5;0,95;1) / (1;1;1) | RGB | Màu đầu tia | CẨN THẬN | TĨNH |
| Runner head | gain halo/core | K:15236,15238 | 0,5 / 1,8 ×inten×endFade | hệ số | Sáng đầu tia | CẨN THẬN | TĨNH |
| Runner head | kích thước/offset | K:15237,15239 | 9 (offset4,5) / 3,96 (offset1,98) | pixel | Tâm đầu tia | CẨN THẬN | TĨNH |
| Blend | g_jxAdditive mặc định/reset | K:8676,15242 | false; bật true tại15108 | boolean | Chọn cộng sáng hay normal | KHÔNG | TĨNH |
| Blend | additive / normal | K:14952,14959 | SRC_ALPHA,ONE / SRC_ALPHA,ONE_MINUS_SRC_ALPHA | GL enum | Cộng sáng/che phủ | KHÔNG | TĨNH |
| Shader | glow gain | F:6,10 | RGB nhân u_glow.rgb*u_glow.a; alpha giữ c.a | công thức | u_glow.a không nhân alpha texture; vẫn bị SRC_ALPHA | KHÔNG | TĨNH |
| Shader | transform | V:7 | CC_PMatrix*a_position | ma trận | Không có gate theo frame/time | KHÔNG | TĨNH |
| State | RGBA mặc định / alpha cuối sét | K:8677,15243 | (1;1;1;1) / alpha=1 | hệ số | Không khôi phục RGB cũ | KHÔNG | TĨNH |
| Log | SEC interval | N:571 | >1.000.000 | µs | Không bắt được mọi frame mất | CẨN THẬN | TĨNH |
| Log | GU sampling | K:14956 | mỗi 200 draw xét trong trace | lượt draw | Lấy mẫu uniform | CẨN THẬN | TĨNH |
| Log đề xuất | buffer vòng | Mục bản log thử | 300 | frame | Cửa sổ chứng cứ trước/sau lỗi | CÓ | ĐỀ XUẤT, chưa tồn tại |
| PFL | nTime fallback | K:11238,11241 | 20 | chưa xác nhận nơi dùng | Không thấy dùng nTime tiếp trong PaintPifeng | CẨN THẬN | TĨNH |
| PFL | count fallback | K:11240 | 11 | loại | Clamp loại nhãn | CẨN THẬN | TĨNH, không phải INI đã đo |
| PFL | position X | K:11251 | -20 | pixel node | Dịch nhãn phi phong | CẨN THẬN | TĨNH |
| PFL | child z-order | K:11252 | 1 | local z | Thứ tự node nhãn; khác sort part kiếm | CẨN THẬN | TĨNH |
| Lịch sử | refresh bolt đầu | B/Classes/gamescene/KgameWorld.cpp.bak-bolt2:14939 | Lịch sử 70.000; hiện 50.000/pha | µs | Nhịp đổi mẫu | CẨN THẬN | DIFF |
| Lịch sử | bỏ ngẫu nhiên bolt đầu | B/Classes/gamescene/KgameWorld.cpp.bak-bolt2:14946 | Lịch sử 0,30/tia | xác suất | Có thể tất cả tia ứng viên cùng bị bỏ | CẨN THẬN | DIFF |
| Lịch sử | refresh bolt3 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt3:14979 | Lịch sử 90.000 | µs | Nhịp đổi mẫu | CẨN THẬN | DIFF |
| Lịch sử | bỏ ngẫu nhiên bolt3 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt3:14984 | Lịch sử hi0,25/low0,45 | xác suất | Nhấp nháy chủ ý đời cũ | CẨN THẬN | DIFF |
| Lịch sử | runner amp trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15149 | Lịch sử min(pmax+2,5;14); hiện 5,5 | pixel | Độ văng ngang | CẨN THẬN | DIFF |
| Lịch sử | runner count trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15150 | Lịch sử 3/2; hiện 6/4 | tia high/low | Mật độ | CẨN THẬN | DIFF |
| Lịch sử | runner phase shift trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15153 | Lịch sử r*5; hiện r*16/nRun | pha | Rải tia theo vòng | CẨN THẬN | DIFF |
| Lịch sử | runner nghỉ trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15154–15155 | Lịch sử t>=12, head chia12; hiện t>=16, chia16 | pha | Nghỉ 4 pha mỗi runner đời cũ | CẨN THẬN | DIFF |
| Lịch sử | runner tail trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15156 | Lịch sử 0,42; hiện 0,9 | tỷ lệ kiếm | Độ dài đuôi | CẨN THẬN | DIFF |
| Lịch sử | runner wave trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15163 | Lịch sử 9,4; hiện 14,137 | rad/chiều kiếm | Số vòng uốn | CẨN THẬN | DIFF |
| Lịch sử | runner đứt trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15173 | Lịch sử %4==3; hiện %5>=3 | residue | Tỷ lệ đoạn giữ lại | CẨN THẬN | DIFF |
| Lịch sử | runner size trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15179 | Lịch sử 4,2/2; hiện 3,78/1,8 | pixel | Độ dày halo/core | CẨN THẬN | DIFF |
| Lịch sử | runner core gain trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15181 | Lịch sử 1,6; hiện 1,12 | hệ số | Độ sáng lõi | CẨN THẬN | DIFF |
| Lịch sử | runner head size trước bolt8 | B/Classes/gamescene/KgameWorld.cpp.bak-bolt7:15191,15193 | Lịch sử 10/4,4; hiện 9/3,96 | pixel | Kích thước halo/core đầu tia | CẨN THẬN | DIFF |
