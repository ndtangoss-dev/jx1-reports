# B-01 - Thiết kế bộ lọc hiển thị và chặn tương tác (Chat, 2026-11-17 01:xx)

Dựa trên `REPORTS/A-05-diem-tuong-tac-gs001.md` (đọc mã tĩnh). Chưa build, chưa chạy. Mọi con số/dòng lấy từ A-05, cần kiểm lại khi cài.

## 1. Luật cần đạt (từ chỉ thị chủ dự án)
1. Bản đồ thường: **người thật không thấy nhau**, không tương tác nhau (không đánh, không giao dịch, không mời đội, không PK, không chat màn hình).
2. **Bot là thực thể chung**: ai cũng thấy; A giết Bot thì Bot chết với mọi người.
3. Một số hoạt động (ví dụ Tống Kim) cho người thật thấy nhau, **có trần số lượng thấy nhau** do cấu hình.
4. Hảo hữu cứng (thiết kế riêng): chỉ chủ và tổ đội của chủ thấy.
5. Có công tắc tổng để tắt: tắt = hành vi gốc, không đổi gì.

## 2. Khái niệm
- **VisGroup** (nhóm nhìn thấy): số nguyên gắn trên mỗi người chơi. 0 = "bong bóng riêng" (bản đồ thường). Hai người thật chỉ thấy nhau khi cùng VisGroup khác 0, hoặc cùng tổ đội (cờ cấu hình).
- **Nguồn (source)** có 4 loại: NPC/quái/đối tượng (luôn thấy theo luật gốc), Bot (cờ IsBot, luôn thấy), hảo hữu (cờ OwnerPlayer, thấy theo chủ), người thật.
- `ViewerCanSee(viewerPlayerIdx, srcNpcIdx, packetClass)`:
  - source không phải người thật hoặc là Bot: true (theo luật gốc).
  - source là hảo hữu: true nếu viewer là chủ hoặc cùng tổ đội với chủ.
  - source là người thật: true nếu viewer == source, hoặc cùng tổ đội (nếu bật), hoặc cùng VisGroup != 0 và còn trong trần `MaxVisible`.
  - công tắc tắt: luôn true.
- `CanInteract(a, b)` = ViewerCanSee(a,b) và ViewerCanSee(b,a). Dùng để chặn hành động người chơi lên người chơi.
- **Tách hai việc:** (A) lọc hiển thị = chặn gói đồng bộ, (B) chặn tương tác = chặn kết quả hành động. Không chỉ làm A, vì client có thể gửi lệnh nhắm mục tiêu theo ID (A-05 mục 2).

## 3. Cấu hình `Settings/visibility.ini`
```
[General]
Enabled=0              ; công tắc tổng, mặc định tắt
BotsVisibleToAll=1
PartyMutualVisible=0   ; đồng đội người thật có thấy nhau không (sẽ chủ dự án chốt)

[Map_<mapId>]
Mode=Solo              ; Solo | Group | Open
; Solo  = mọi người thật ở bản đồ này không thấy nhau (mặc định bản đồ thường)
; Group = chỉ người cùng VisGroup thấy nhau
; Open  = như game gốc

[Group_<id>]
MaxVisible=60          ; trần số người thật thấy nhau trong nhóm này
```
Trần: kịch bản hoạt động (Lua) gán người vào nhóm con có kích thước ≤ MaxVisible (nhóm đầy thì tạo nhóm kế tiếp). Cách này đơn giản hơn "chỉ thấy N người gần nhất" và không làm lệch giữa hai phía.

## 4. API Lua (thêm vào ScriptFuns)
`SetVisGroup(group)`, `GetVisGroup()`, `JoinActivityGroup(activityId)` (tự chọn nhóm con còn chỗ), `LeaveActivityGroup()`, `IsBotPlayer(playerIdx)`. Khi đổi nhóm phải gọi **làm mới hiển thị** (mục 6).

## 5. Điểm chèn (theo A-05), làm theo thứ tự ưu tiên
**P1 - lọc hiển thị (bao phần lớn):**
1. `KRegion::BroadCast` (Core/Src/KRegion.cpp:2223-2280): chèn ngay trước `PackDataToClient` (~2266): `if (!ViewerCanSee(viewer, source, cls)) continue;`. Đây là cửa chính cho hầu hết gói đồng bộ NPC/người/đối tượng.
2. Đường gửi thẳng: `KNpc::SendSyncData` (KNpc.cpp:7718, 7822), `KNpcSet::SyncNpc` (KNpcSet.cpp:1284-1288), `KSubWorld::BroadCasts` (KSubWorld.cpp:2371-2373), đồng bộ khi đổi bản đồ `ChangeWorld` (KNpc.cpp:14993-15030), `KObj` (KObj.cpp:1468-1621).
3. Gói xóa: **không được chặn nhầm gói xóa** (REMOVE) khi người xem đã thấy trước đó, nếu không client giữ "người ma". Quy tắc: gói REMOVE luôn gửi nếu viewer đã từng được gửi ADD (theo cờ "đã thấy" trên viewer), bất kể trạng thái hiện tại.

**P2 - chặn tương tác (player-origin only, KHÔNG sửa đường AI/NPC):**
- `NpcSkillCommand` (KProtocolProcess.cpp:5581-5606) và `CastInitiativeSkill` (KSkills.cpp:3348-3415): từ chối nếu mục tiêu là người thật mà `!CanInteract`.
- AoE: `KMissle::ProcessCollision` (KMissle.cpp:1785-1867): trước `ProcessDamage`, nếu launcher là người thật và target là người thật mà `!CanInteract` thì bỏ qua target. Không áp lên đường dame của AI/quái.
- `FindAroundPlayer/FindAroundNpc*` (KPlayer.cpp:2361-2480) và `LuaFindAroundPlayer` (ScriptFuns.cpp:19852-19900): biến thể "người chơi gọi" lọc theo CanInteract; giữ biến thể AI.
- Mời đội/bang/bạn: `KPlayerTeam::InviteAdd` (KPlayerTeam.cpp:397-426), `KPlayerTong` (413-476, 525-593).
- Giao dịch/xem trang bị/sạp: `c2sViewEquip` (KProtocolProcess.cpp:8058-8101), `TradeApplyStart` (KPlayer.cpp:6563-6633, 7054-7115), `KItemList` chuyển vật phẩm.
- PK: `EnmityPKOpen`, `ExercisePKOpen` (KPlayerPK.cpp:128-312), `c2sPKApplyEnmity` (KProtocolProcess.cpp:6211-6238).
- Chat màn hình đi qua BroadCast nên tự lọc; chat riêng/nhóm giữ nguyên ý định chủ dự án (chốt sau).
- Không sửa `GetRelation` (KNpcSet.cpp:1813-2042): thêm guard ở caller (A-05 đánh giá rủi ro rất cao).

**P3 - vệ sinh slot offline:** thêm kiểm `m_nNetConnectIdx >= 0` ở các vòng PlayerSet trong chat/hệ thống (A-05 mục 6) - việc dọn tách riêng, không bắt buộc cho luật.

## 6. Làm mới hiển thị khi đổi nhóm
Khi `SetVisGroup` đổi (vào/ra Tống Kim, tổ đội lập/giải tán): với mỗi người bị đổi quan hệ nhìn thấy, gửi REMOVE tới bên mất thấy và ADD/SYNC tới bên mới thấy. Cần hàm `RefreshVisibility(playerIdx)` duyệt region hiện tại + 8 ô lân cận. Đây là chỗ dễ lỗi nhất (A-05: "đổi vị trí" và "ChangeWorld" rủi ro rất cao); test kỹ.

## 7. Hiệu năng
`ViewerCanSee` chạy cho mỗi người xem x mỗi nguồn x mỗi gói. Chỉ so số nguyên (nhóm, cờ, id chủ) và đọc cờ trong bộ nhớ, **không đọc file/DB**. Đo tick trước/sau (B-04). Trần 500 người online, 18 Hz: khối lượng thêm nhỏ nếu hàm đơn giản.

## 8. Tiêu chí nghiệm thu (bộ test B-03, 2 người chơi + 1 Bot)
1. Bản đồ Solo: A và B cùng chỗ, không thấy nhau trên màn hình; cả hai thấy Bot.
2. A giết Bot: Bot chết với B (Bot chung).
3. A thả AoE/skill lên vị trí B: B không bị thương; A không chọn được B làm mục tiêu.
4. A mời đội/giao dịch/PK B: bị từ chối (server).
5. Cùng VisGroup (hoạt động): thấy nhau đến trần MaxVisible; người thứ MaxVisible+1 vào nhóm con khác.
6. Đổi nhóm giữa chừng: không còn "người ma" ở client, không mất ADD.
7. `Enabled=0`: hành vi giống hệt bản gốc (so gói tin/ảnh chụp).
8. Tick/băng thông không tăng đáng kể (B-04).

## 9. Rủi ro và phụ thuộc
- **Phụ thuộc A-07:** gs001 phải dựng và chạy được để test. Mã vá có thể viết và build trước, chưa chạy.
- Người ma ở client, đường gửi thẳng bị sót (A-05 liệt kê nhiều đường), gói REMOVE bị chặn nhầm, cạnh tranh quái/tài nguyên (Bot chung nên ổn).
- Sửa nhỏ, có công tắc, nhánh riêng `feature/visibility` trong `jx1-source`. Duyệt (Chat) trước khi gộp.
