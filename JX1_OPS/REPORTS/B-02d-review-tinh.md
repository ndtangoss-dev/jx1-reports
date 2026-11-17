# TÓM TẮT 5 DÒNG
1. DONE — hoàn tất review tĩnh B-02c tại commit `026c628f7aff8e4d0af65251569b53a47c05d5b8`; chưa đủ bằng chứng nghiệm thu O-01/B-01 hoặc gộp bản chính.
2. Luật REMOVE hai điều kiện và dọn viewer/nguồn đã có; gửi REMOVE lỗi rồi xóa bookkeeping còn rủi ro mất dấu client.
3. P2 có ba guard nhắm/skill/collision, nhưng bỏ qua người ẩn đầu ô có thể làm Bot/quái cùng ô không trúng; giao dịch, đội, PK và truy vấn quanh người còn thiếu guard.
4. Chat màn hình qua relay vẫn gửi thẳng ở `CoreServerShell.cpp:3009`; các đường NPC/object/world đã móc phải phân biệt với đường tương tác còn sót của A-05.
5. [CHƯA KIỂM] đối chứng Enabled=0, Solo/nhóm/Bot, REMOVE/chuyển map và hiệu năng 100 Bot + 20 người; lượt này không build, chạy game/server, dùng VM hay mạng.

## Phạm vi và bằng chứng

- Ngày: 2026-11-17. Yêu cầu: `JX1_OPS/TASKS/B-02d.md`; chuẩn đối chiếu: `JX1_OPS/REPORTS/O-01-duyet-B-02.md`, `JX1_OPS/DESIGN/B-01-LOC-HIEN-THI.md`, bản đồ điểm gọi `JX1_OPS/REPORTS/A-05-diem-tuong-tac-gs001.md`.
- Source chỉ đọc: `D:\JX-wt\B-02c`, nhánh `feature/visibility-c`, HEAD `026c628f7aff8e4d0af65251569b53a47c05d5b8`. Diff chính `c85cc1a..026c628`: 7 file, 73 dòng thêm/15 dòng xóa. Đọc thêm diff nền P1 `a52791d..c85cc1a` và đúng các caller liên quan trong A-05; không kiểm kê toàn repository.
- Working tree source không có sửa tracked; có sẵn `B-02c-KETQUA.md` untracked, chỉ đọc. Báo cáo đó nói chưa commit là checkpoint cũ; HEAD thực tế đã chứa bản vá. Không sửa/reset/stage bất kỳ file nào ở B-02c.
- Quy ước `K*.cpp:dòng` dưới đây là đường dẫn tính từ `D:\JX-wt\B-02c\server\jxOnline\gameserver\Sources\Core\Src\`; phía client ghi đường dẫn riêng. Dòng là bản HEAD hiện tại, không dùng nguyên số dòng cũ của A-05.
- Đây là kết luận luồng điều khiển từ source. Kịch bản tác động bên dưới là test cần có, không phải kết quả chạy.

## Phát hiện cần xử lý

### F1 — CAO: người ẩn đầu ô làm mất mục tiêu Bot/quái hợp lệ cùng ô

`KMissle.cpp:1847` gọi `KRegion::FindNpc`, hàm này trả ngay ứng viên đầu phù hợp tại `KRegion.h:426-427`. Guard mới `KMissle.cpp:1851-1852` gặp người thật ẩn thì `continue` vòng ô ở dòng 1833; không duyệt tiếp ứng viên trong cùng ô. Vì thế nếu B ẩn đứng trước Bot/quái C trong danh sách và cả hai phù hợp relation của đòn, AoE của A bỏ luôn C. Miễn Bot trong `CanInteract` không giúp vì C chưa được xét. Đây là thay đổi khi bật bộ lọc, vi phạm yêu cầu Bot chung/không ảnh hưởng đường đánh Bot; không phải bằng chứng người ẩn vẫn nhận damage.

- Hướng sửa: lọc ứng viên trong biến thể tìm dành cho player-origin hoặc tiếp tục duyệt cùng ô sau ứng viên bị cấm; giữ semantics tìm của AI.
- Test: A thật, B thật ẩn, C Bot rồi quái cùng ô, đổi thứ tự danh sách; A không tác động B nhưng vẫn tác động C như trường hợp không có B. Kiểm hit count, relation ally/enemy và launcher AI/Bot.

### F2 — CAO: P2 của B-01 chưa phủ các hành động ngoài ba guard chiến đấu

`KPlayer::FindAroundPlayer` tại `KPlayer.cpp:2366-2386` và `FindAroundNpc` tại dòng 2414-2444 vẫn tìm theo vùng/ID, không kiểm `CanInteract`. Các caller sau giữ đường xử lý cũ:

| Điểm thiếu guard | Hệ quả khi điều kiện gameplay cũ thỏa | Test cần có |
|---|---|---|
| `KPlayerTeam.cpp:405`, `:417`, `:426` | Người ẩn vẫn được đưa vào invite list và nhận lời mời đội direct. | A/B Solo ẩn, đội mở; gửi yêu cầu bằng ID đã biết, không tạo invite/sync ngoài chính sách được chốt. |
| `KPlayer.cpp:6619`, `:6630`, `:6637` | Trade target quanh vùng và mở menu vẫn được lưu `m_nApplyIdx`, gửi yêu cầu trực tiếp. | A/B ẩn, B mở trade; không tạo trạng thái giao dịch; kiểm cả phiên trade đang mở khi mất visibility. |
| `KProtocolProcess.cpp:8076-8081`, `:8090-8094`, `:8853-8855`; `KPlayer.cpp:11982` | Xem trang bị/sạp và vào nhánh mua sạp còn theo ID/vùng, không có visibility guard ở cửa vào. | Request xem/mua với ID B ẩn: không lộ dữ liệu hay thực hiện mua; kiểm item/tiền không đổi. [CHƯA KIỂM] toàn bộ phần chuyển item sau cửa vào. |
| `KProtocolProcess.cpp:6236-6242`; `KPlayerPK.cpp:205-226`, `:291-310` | Enmity/exercise vẫn đổi trạng thái hai phía và gửi PK sync dù hai người không thấy nhau. Guard damage không chặn mutation PK. | Request hợp lệ theo ràng buộc ID/PK cũ, A/B ẩn: không mở PK, không gửi sync đối phương. |
| `KPlayerTong.cpp:435`, `:465-476`, `:527`, `:575-582` | Xin/mời bang theo ID quanh vùng vẫn có đường direct. | A/B đủ camp/level/trạng thái, ẩn nhau: không phát lời mời/xin ngoài chính sách. |
| `ScriptFuns.cpp:19884-19900` (`LuaFindAroundPlayer`) | Danh sách Lua vẫn đưa người ẩn cùng map/bán kính vào bảng kết quả. | Biến thể player-origin không trả B ẩn; giữ API thống kê/AI theo semantics riêng. |

Đây là thiếu sót so với **toàn bộ B-01**, không quy kết B-02c đã nhận sửa hết P2: checkpoint B-02c đã nêu chỉ vá ba điểm chiến đấu. O-01 mục 4 để chủ dự án chốt chat/mời đội/giao dịch theo tên; chưa có quyết định mới trong tài liệu được giao. Cần ghi rõ ngoại lệ được duyệt trước nghiệm thu, không tự coi việc đi vòng bằng ID là đã được chấp thuận.

### F3 — CAO: đường chat màn hình relay đi vòng lọc hiển thị

Nhánh `tgtcls_scrn` tại `CoreServerShell.cpp:2916` lấy NPC nguồn ở dòng 2924, dựng `s2c_extendchat` tại 2959 và gửi thẳng tại 3009, chỉ lọc khoảng cách/blacklist ở 3007-3008. Không qua `KRegion::BroadCast` hoặc `PackVisibilityData`. Vì vậy khẳng định của B-01 rằng chat màn hình tự được lọc qua BroadCast chưa đúng cho đường này. Khác với chat riêng/nhóm được để chốt sau ở O-01, đây là đường nearby/screen cụ thể.

- Hướng sửa: kiểm viewer với người gửi đã xác định tại caller này, giữ khoảng cách và blacklist; không chỉ thêm loại packet ở helper vì caller hiện bỏ qua helper.
- Test: A/B Solo ẩn, không blacklist và đứng gần; thử riêng chat screen cũ và screen qua relay. B không nhận nội dung màn hình từ A; đối chứng Open/cùng đội theo cấu hình vẫn nhận. [CHƯA KIỂM] UI thực tế hiển thị gói relay ở đâu và toàn bộ tuyến KSOServer đến caller này.

### F4 — TRUNG BÌNH: xóa dấu đã thấy dù REMOVE gửi lỗi ở thời điểm hủy nguồn

`RemoveKnown` tại `KVisibility.cpp:81-82` chỉ xóa khi đóng gói thành công. Tuy nhiên `RemoveVisibilitySource` gọi nó tại dòng 313 rồi **luôn** `erase(id)` tại 314, kể cả gửi lỗi hoặc không có server. Với viewer đang kết nối ngoài chín region hoặc đường `KNpcSet::Remove(..., FALSE)`, không có đảm bảo một broadcast tiếp theo sẽ chữa lại. Source bị hủy, record đã mất, `RefreshViewer` cũng không còn record để retry. Điều này đạt mục tiêu dọn source slot nhưng chưa chứng minh tiêu chí không người ma khi lỗi gửi.

- Hướng sửa: giữ dấu cần xóa/retry bằng ID độc lập vòng đời NPC, hoặc quy định rõ cơ chế phục hồi/disconnect/resync khi transport lỗi; không giữ con trỏ slot đã tái dùng.
- Test: ép lỗi `PackDataToClient` đúng REMOVE của một viewer known, hủy source và tái dùng slot; kiểm client không giữ NPC cũ và không xóa NPC mới. [CHƯA KIỂM] contract lỗi/queue transport có tự phục hồi hoặc ngắt kết nối hay không, nên đây là rủi ro có điều kiện, chưa phải lỗi runtime đã tái hiện.

### F5 — TRUNG BÌNH: chi phí REMOVE/refresh lớn hơn mô tả “chỉ so số nguyên”

`KVisibility.cpp:173-181` duyệt toàn `MAX_PLAYER` mỗi lần REMOVE đi qua một `KRegion::BroadCast`. Caller `KNpc.cpp:14435`, `:14441-14446` và `KNpcSet.cpp:1022-1030` phát tối đa chín region: tối đa chín vòng toàn mảng cho một REMOVE, kèm tra `std::map::count`. Viewer known ở region khác có thể nhận lần đầu toàn cục, rồi lần nữa khi vòng đến region của họ nếu policy hiện còn cho thấy sau khi record đã xóa. Đây không phải cam kết chín lần gửi cho mỗi viewer.

`RefreshAllVisibility` tại `KVisibility.cpp:166` gọi `RefreshViewer` cho mọi slot; mỗi viewer quét chín danh sách NPC (`:104-117`). Mỗi ADD trực tiếp còn dò lại viewer bằng vòng `MAX_PLAYER` (`:204-205`, `KNpc.cpp:7961`). Refresh toàn cục khi đổi đội có ở `KPlayerTeam.cpp:500`, `:850`, `:885` theo diff nền. Cấu hình chỉ đọc trong `InitVisibility` (`KVisibility.cpp:123-155`), không thấy đọc file/DB trong policy mỗi gói; tuy vậy không thể kết luận chi phí nhỏ từ source.

- Hướng xử lý: đo trước; cân nhắc thực hiện global-known REMOVE một lần mỗi sự kiện, index client→viewer và giới hạn refresh đúng tập ảnh hưởng.
- Test: 100 Bot + 20 người, cùng hoạt cảnh Enabled=0/1; tick trung vị/p95/p99, CPU, số lần policy/lookup, số gói/byte, peak khi rời/giải tán đội và hủy hàng loạt NPC. [CHƯA KIỂM] toàn bộ số đo, chưa kết luận có hồi quy thực tế.

## Đối chiếu từng điều kiện O-01

| Điều kiện | Kết quả tĩnh / bằng chứng | Phần còn phải xác minh |
|---|---|---|
| 1. REMOVE chỉ chặn khi chưa ADD **và** hiện không thấy; client bỏ ID lạ | Có tại `KVisibility.cpp:67-72`, `:278-280`: known→gửi; unknown nhưng thấy→gửi; unknown và ẩn→chặn; nguồn không resolve/sai ID→gửi. Broadcast bổ sung viewer đúng region ngoài tập known (`:179-181`). | Client `client/Classes/gamecore/KProtocolProcess.cpp:629-642`, `KPlayer.cpp:801-805`: ID lạ tìm ra 0 bị ConformIdx loại; khi own index khác 0 thì không FreeAllSprite. Nếu own index cũng 0 và còn game world, nhánh else có thể FreeAllSprite. [CHƯA KIỂM] đăng nhập/chuyển map, Rv TRUE/FALSE, gửi trùng và F4. Unknown ADD đã đi vòng rồi trở thành ẩn vẫn có thể bị chặn REMOVE đúng theo luật hai điều kiện; không suy ra bookkeeping đã đầy đủ. |
| 2. Dọn viewer vào game/đổi map/thoát; dọn source | Vào game `KPlayer.cpp:995` gọi world sync; `KSubWorld.cpp:1783-1785` clear sau Pack thành công. Đổi map `KNpc.cpp:15341`, `:15404` gọi cùng hàm. `KPlayer::Release` clear ở `KPlayer.cpp:106`; caller release có `KPlayerSet.cpp:1120`, `:1162`, `:1231`. `KNpc::Remove` dọn viewer và source trước Init (`KNpc.cpp:10235-10239`); `KNpcSet.cpp:1037`, `:1051` gọi trước tái dùng slot. `KVisibility.cpp:309-314` purge cả viewer offline. | [CHƯA KIỂM] world sync gửi lỗi, timeout/reconnect và tái dùng slot; chưa truy vết đầy đủ nhánh LoginTimeOut đến Release. Dọn source đạt tĩnh nhưng F4 còn tồn tại. |
| 3. Không sát thương giữa hai người thật không thấy nhau; Bot/quái miễn | `RealPlayer` kiểm IsPlayer, player↔NPC khớp, !IsBot (`KVisibility.cpp:59-64`). `CanInteract` đối xứng, chỉ áp khi cả hai là người thật (`:191-197`). Guard ở `KProtocolProcess.cpp:5602`, `KSkills.cpp:3395` trước damage/state/immediate và `KMissle.cpp:1851` trước hit count/damage. | F1; thiếu các caller F2 của B-01. [CHƯA KIỂM] mọi cơ chế damage gián tiếp, phản damage/DoT, slot launcher tái dùng, người thật→companion và runtime hai chiều. Không nhận ba guard là bằng chứng bao phủ mọi damage. |
| 4. Chat/mời đội/giao dịch theo tên là quyết định để chốt | Các đường còn giữ được liệt kê F2 và bảng A-05 dưới đây. | [CHƯA KIỂM] quyết định cuối của chủ dự án; F3 screen không tự thuộc ngoại lệ private/name. |
| 5. Đo 100 Bot + 20 người so Enabled=0 | Có guard tắt nhanh và không I/O mỗi lần policy, nhưng có chi phí F5. | [CHƯA KIỂM] tick/băng thông/CPU; chưa đạt điều kiện đo. |
| 6(a). Enabled=0 giống gốc | Guard mới short-circuit khi tắt; `DescribeVisibilityPacket` trả sớm tại `KVisibility.cpp:235`; `KRegion.cpp:2298-2301` và các direct hook về Pack cũ. Khởi tạo mặc định false, cấu hình mặc định 0 tại `KVisibility.cpp:125`, `:135`. | [CHƯA KIỂM] so packet/ảnh và đăng nhập/đi/đánh/nhóm đối chứng bản gốc. Thêm field/reset bookkeeping/chi phí gọi helper không phải “không thay byte nào”; chỉ xác nhận nhánh gửi/gameplay đã đọc. |
| 6(b). Solo ẩn, cùng đội thấy | `ViewerCanSee` Solo không cho group thường; party chỉ được miễn khi `partyVisible` tại `KVisibility.cpp:227`. Default `PartyMutualVisible=0` (`:137`), nên bài thử “cùng đội thấy” cần cấu hình 1 hoặc chủ dự án chốt lại với B-01. | [CHƯA KIỂM] hai client thực, cả hai giá trị cờ; không dùng default 0 để tuyên bố test cùng đội đã đạt. |
| 6(c). Bot thấy bởi tất cả | Exemption tại `KVisibility.cpp:225`, với `BotsVisibleToAll=1`; owner có ưu tiên trước tại `:218-221`. | [CHƯA KIỂM] Bot chung chết với mọi viewer, F1, việc gắn cờ Bot thực tế. |
| 6(d). Rời/vào đội, không người ma | Có RefreshAllVisibility ở điểm vào/rời/giải tán đội trong diff nền; RefreshViewer remove trước, ADD sau (`KVisibility.cpp:89-117`). | [CHƯA KIỂM] đủ mọi tuyến đội, chín region, chuyển nhóm khi projectile đang bay, F4 và lỗi WorldSync. |

## Đối chiếu các phần còn lại của B-01

- P1: BroadCast có policy và bookkeeping; direct full NPC sync `KNpc.cpp:7959-7963`, `:8018-8020`, `:8124-8126`, request `KNpcSet.cpp:1287`, world broadcast `KSubWorld.cpp:2386-2396`, object add `KObj.cpp:1454-1461` đã được móc trong diff nền. Không có cơ sở gọi toàn bộ các điểm này là “chưa móc” chỉ vì số dòng A-05 đã đổi.
- Group/Open, self, party, Bot và owner có nhánh tại `KVisibility.cpp:218-229`; owner kiểm player ID chống tái dùng slot. SetVisGroup đếm trần người thật trước gán (`:329-341`); JoinActivityGroup tạo nhóm con và sao limit (`:345-373`). Lua API đăng ký tại `ScriptFuns.cpp:25723-25727`. [CHƯA KIỂM] trần N/N+1, đổi cờ Bot khi nhóm đầy, owner đổi slot/đội, mọi hoạt động Lua thực tế và lạm dụng API.
- P2: có ba guard tối thiểu, chưa hoàn tất danh sách B-01 mục 5 (F1/F2/F3). Không sửa GetRelation toàn cục trong diff B-02c; không thấy guard cưỡng ép lên cặp Bot/quái trong helper đã đọc.
- Refresh: có remove known ngoài vùng và add trong chín vùng; group/owner/party hook đã hiện diện. [CHƯA KIỂM] tính đầy đủ của mọi đường đổi đội/owner/di chuyển, không chứng minh bằng việc chỉ thấy tên helper.
- P3 offline là hạng mục tách riêng, không dùng thiếu connection guard ở thông báo hệ thống làm lý do bác ba sửa đổi tối thiểu B-02c.
- Bộ nghiệm thu B-01: test 1–2 (Solo/Bot), 3 (AoE/nhắm), 4 (mời đội/trade/PK), 5 (trần), 6 (đổi nhóm), 7 (tắt), 8 (hiệu năng) đều **[CHƯA KIỂM] runtime** trong lượt review; test 3–4 có vấn đề tĩnh F1/F2 phải xử lý hoặc chốt phạm vi trước.

## Các đường gửi thẳng của A-05: đã móc, còn sót và giới hạn

| Tuyến A-05 / vị trí hiện tại | Trạng thái và ý nghĩa |
|---|---|
| SendSyncData NPC/người (`KNpc.cpp:8018`, `:8124`) + SyncNpc (`KNpcSet.cpp:1287`) | Đã lọc viewer và vùng trước gửi, đã ghi visAdd cho full NPC. Không đánh dấu sót đường này. |
| ChangeWorld (`KNpc.cpp:15315`, `:15341`, `:15404`) | REMOVE qua near-region; WORLD_SYNC direct là dữ liệu world cho chính người đổi map, có clear viewer ở callee. Không phải một ADD người khác chưa lọc. [CHƯA KIỂM] toàn bộ chuỗi sau AddPlayer/chuyển server. |
| KSubWorld::BroadCasts (`KSubWorld.cpp:2386-2396`) | Đã gọi Describe/Pack khi bật. REMOVE ở đây chỉ duyệt người cùng world; [CHƯA KIỂM] caller nào cần global-known ngoài world. |
| KObj::SyncAdd (`KObj.cpp:1454-1461`), state/dir/remove/trap qua region | Object được giữ shared bằng visObject, phù hợp B-01 cho object chung; không tự thêm policy owner vào object. [CHƯA KIỂM] mọi ownership object/script. |
| Direct self SendSerCommand (`KNpc.cpp:16357`) | Trả lệnh cho chính source; không mặc định là rò sang viewer khác. [CHƯA KIỂM] mọi gói self khác trong A-05. |
| Đội, trade, xem đồ/sạp, PK, bang | **Còn sót policy tại caller**, vị trí và test ở F2; chúng không qua bộ lọc NPC chỉ vì có NPC ID trong payload. |
| Screen relay (`CoreServerShell.cpp:2916-3009`) | **Còn sót**, F3. Screen cũ `KPlayerChat.cpp:497` có đi SendDataToNearRegion; không gộp hai đường. |
| Chat all/private (`KPlayerChat.cpp:468`, `:547`) | Vẫn gửi direct, không visibility helper. Chat riêng/nhóm/theo tên cần quyết định O-01; không coi mọi thông báo all/system phải bị ẩn. |
| Relay generic (`KNewProtocolProcess.cpp:167-179`) | Vẫn direct mọi PlayerSet ở dòng 175, không connection/visibility check. Chỉ xác nhận cửa này; **[CHƯA KIỂM]** payload/caller cụ thể có chứa ADD/update người ẩn không, nên không khẳng định đã tìm thêm một ADD bypass. |
| KItemList transfer, friend resend/offline, mission/rank, KSOServer Chat/Tong queues | **[CHƯA KIỂM]** thân từng tuyến trong lượt này; A-05 là bản đồ tiếp tục, không phải bằng chứng chúng đã được vá ở HEAD. Guard mutation/policy cần đặt đúng caller, giữ cleanup và thông báo hệ thống hợp lệ. |

## Kiểm tra, lỗi công cụ và bàn giao

- Đã chạy `git diff --check c85cc1a 026c628` ở source: exit 0, không output. Đây chỉ là kiểm tra whitespace diff, không phải build/test logic.
- `JX1_OPS/REPORTS/B-02c-build-va-thu.md` báo PM đã build 5 project exit 0 và server Enabled=0 sống ít nhất 207 giây. Chỉ dẫn lại tài liệu có sẵn; không xác minh binary/log/VM, không biến smoke test đó thành đối chứng hành vi gốc.
- Lỗi đọc đầu: PowerShell mặc định hiển thị UTF-8 sai; đã đọc tài liệu lại bằng `-Encoding UTF8`. `rg : The term 'rg' is not recognized` nên dùng Select-String/Get-Content trên các file cụ thể, không tạo parser/script phụ.
- Git source ban đầu báo `fatal: detected dubious ownership in repository at 'D:/JX-wt/B-02c'`. Đã dùng `git -c safe.directory=D:/JX-wt/B-02c -C ...` cho thao tác đọc đúng worktree đã được giao; không sửa config toàn cục, credential hay quyền filesystem. Các lệnh đọc sau thành công. Không còn blocker cho review tĩnh.
- Không dùng Python; không build/test runtime, chạy exe game/server, kết nối mạng/VM hoặc ghi thông tin bí mật. Không sửa source B-02c, canonical, cấu hình hoặc tài liệu khác ngoài hai file đầu ra task.
- **Trạng thái task: DONE** (review tĩnh và báo cáo hoàn tất). **Kết luận nghiệm thu bản vá: chưa đủ điều kiện**; ưu tiên F1/F2/F3, sau đó kiểm F4/F5 và thực hiện chuỗi O-01 bằng quyền test riêng. Phần chưa xác minh đã đánh dấu [CHƯA KIỂM].
- Commit được review: `026c628f7aff8e4d0af65251569b53a47c05d5b8`. Commit báo cáo: chưa tạo; người dùng không yêu cầu commit/push. Chưa push, không truy cập GitHub/mạng theo phạm vi task, nên không có link công bố.
