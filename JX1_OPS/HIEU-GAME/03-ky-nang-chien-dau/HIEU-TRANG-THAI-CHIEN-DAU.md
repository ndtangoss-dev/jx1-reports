TÓM TẮT 1: [TÀI LIỆU] HG-02 yêu cầu giải thích nút đánh ngoài trạng thái chiến đấu và các điểm mainSkillattack, 0x02, SetFightMode, SetFightState (JX1_OPS/TASKS/HG-02.md:18-20).
TÓM TẮT 2: [THẤY] Bốn tệp mã nguồn task chỉ định không có trong worktree HG-02; chưa thể kết luận thứ tự gọi hoặc nguyên nhân nhân vật ngồi (JX1_OPS/TASKS/HG-02.md:23).
TÓM TẮT 3: [CHƯA KIỂM] Quan hệ giữa cờ 0x02, trạng thái chiến đấu và hoạt ảnh ngồi chỉ là giả thuyết đến khi có source thật (JX1_OPS/TASKS/HG-02.md:19,23).
TÓM TẮT 4: [TÀI LIỆU] Test-36 chỉ là đề xuất quan sát; không chạy game, VM, exe, build hoặc mạng (JX1_OPS/TASKS/HG-02.md:19,26-28).
TÓM TẮT 5: [CHƯA KIỂM] Đầu ra ở trạng thái PARTIAL; cần PM cung cấp đúng root/version source để hoàn tất (JX1_OPS/TASKS/HG-02.md:23).

# HG-02 — Hiểu game: trạng thái chiến đấu và nút đánh
Loại: tổng hợp
Chủ đề: Giải thích trạng thái chiến đấu, nút đánh và đề xuất quan sát trên Test-36.
Từ khóa: trạng thái chiến đấu, nút đánh, mainSkillattack, cờ 0x02, SetFightMode, SetFightState, Test-36
Trạng thái: PARTIAL — thiếu bốn tệp source nên chưa xác minh được luồng thực.
Độ phủ: 0/4 tệp mã nguồn được chỉ định; 1/1 đề xuất Test-36 được ghi ở mức tài liệu, chưa thực hiện.
Liên quan: JX1_OPS/TASKS/HG-02.md; JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md
Cần tôi quyết định: không

liên quan: JX1_OPS/TASKS/HG-02.md; mục lục tri thức hiện xếp phím tắt, nút và tự động chiến đấu ở JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md:13.

## Luồng cần đối chiếu
[TÀI LIỆU] Task nêu bốn điểm cần kiểm tra: `mainSkillattack`, cờ `0x02`, `SetFightMode` và `SetFightState` (JX1_OPS/TASKS/HG-02.md:19). Đây là danh sách điểm kiểm tra, chưa phải bằng chứng rằng chúng gọi nhau theo một thứ tự cụ thể.

[CHƯA KIỂM] Giả thuyết làm việc: nếu `mainSkillattack` được xử lý khi cờ `0x02` chưa biểu thị trạng thái chiến đấu, nhánh xử lý có thể không vào hoạt ảnh đánh và nhân vật rơi về hoạt ảnh ngồi. Cần đọc thân hàm, điều kiện cờ và caller/callee trong source thật để xác nhận hoặc bác bỏ; không dùng giả thuyết này làm kết luận runtime.

[CHƯA KIỂM] `SetFightMode` và `SetFightState` có thể là hai điểm chuyển/ghi trạng thái, nhưng vai trò, giá trị tham số và thứ tự thực thi chưa được xác minh vì không có `KNpcAI.cpp`, `KProtocolProcess.cpp`, `KNpc.cpp` hoặc `ScriptFuns.cpp` trong worktree.

## Đề xuất quan sát trên Test-36
[TÀI LIỆU] Chỉ đề xuất, không thực hiện: chuẩn bị một nhân vật đứng yên, ghi nhận hoạt ảnh ban đầu, bật trạng thái chiến đấu bằng thao tác gameplay đã được phê duyệt, nhấn nút đánh và quan sát có chuyển sang vung kiếm hay vẫn ngồi. Nếu có công cụ quan sát hợp lệ, ghi riêng trước/sau của trạng thái chiến đấu và cờ `0x02`; không sửa mã hoặc cấu hình.

[CHƯA KIỂM] Tiêu chí quan sát: (1) trạng thái chiến đấu đổi trước lần nhấn; (2) lần nhấn gọi được đường đánh; (3) hoạt ảnh vung kiếm xuất hiện. Ba điểm này chỉ là kế hoạch kiểm tra, chưa có số đo hay kết quả.

## Phạm vi và độ phủ
| Phần tử phạm vi | Độ phủ | Bằng chứng / giới hạn |
|---|---|---|
| `Folder/Client2912-.../Classes/gamecore/KNpcAI.cpp` | Chưa phủ | Đường dẫn task nêu tại JX1_OPS/TASKS/HG-02.md:23; tệp không tồn tại trong worktree HG-02. |
| `Folder/Client2912-.../Classes/gamecore/KProtocolProcess.cpp` | Chưa phủ | Đường dẫn task nêu tại JX1_OPS/TASKS/HG-02.md:23; tệp không tồn tại trong worktree HG-02. |
| `gameserver/Sources/Core/Src/KNpc.cpp` | Chưa phủ | Đường dẫn task nêu tại JX1_OPS/TASKS/HG-02.md:23; tệp không tồn tại trong worktree HG-02. |
| `gameserver/Sources/Core/Src/ScriptFuns.cpp` | Chưa phủ | Đường dẫn task nêu tại JX1_OPS/TASKS/HG-02.md:23; tệp không tồn tại trong worktree HG-02. |
| `mainSkillattack`, `0x02`, `SetFightMode`, `SetFightState` | Chưa phủ | Chỉ có tên trong mục tiêu task; chưa có thân hàm, caller/callee hoặc giá trị runtime. |
| Đề xuất quan sát Test-36 | Đã ghi đề xuất | Không chạy theo giới hạn task; chưa có kết quả thực nghiệm. |

## Giải mã tên
| Tên gốc | Mã hóa | Chữ đúng / diễn giải | Nguồn file:dòng |
|---|---|---|---|
| `mainSkillattack` | ASCII, đọc như UTF-8 | tên định danh; task gọi là đường nút đánh | JX1_OPS/TASKS/HG-02.md:19 |
| `0x02` | ASCII, số hexadecimal | cờ được task yêu cầu đối chiếu; ý nghĩa bit chưa giải mã | JX1_OPS/TASKS/HG-02.md:19 |
| `SetFightMode` | ASCII, đọc như UTF-8 | định danh có nghĩa đặt chế độ chiến đấu; vai trò thực chưa kiểm | JX1_OPS/TASKS/HG-02.md:19 |
| `SetFightState` | ASCII, đọc như UTF-8 | định danh có nghĩa đặt trạng thái chiến đấu; vai trò thực chưa kiểm | JX1_OPS/TASKS/HG-02.md:19 |
| `Test-36` | ASCII, đọc như UTF-8 | tên môi trường kiểm tra được task nêu; chưa chạy | JX1_OPS/TASKS/HG-02.md:19 |

## Sắp theo cấu trúc game
| Tầng cấu trúc | Thành phần | Trạng thái |
|---|---|---|
| Ý định người chơi / nút đánh | `mainSkillattack` | Tài liệu task; chưa có code UI hoặc caller. |
| Cờ trạng thái | `0x02` | Tài liệu task; chưa biết bit thuộc enum/field nào. |
| Chuyển chế độ | `SetFightMode` | Tài liệu task; chưa biết điểm gọi. |
| Ghi trạng thái | `SetFightState` | Tài liệu task; chưa biết điều kiện và tham số. |
| Kiểm chứng thực nghiệm | Test-36 | Chỉ đề xuất; chưa chạy. |

## Sơ đồ quan hệ cần xác minh
```mermaid
flowchart LR
  UI[Nút đánh] -. cần xác minh .-> A[mainSkillattack]
  A -. cần xác minh .-> F{Cờ 0x02 / trạng thái chiến đấu}
  F -. cần xác minh .-> M[SetFightMode]
  M -. cần xác minh .-> S[SetFightState]
  S -. hoạt ảnh cần quan sát .-> V[Vung kiếm hoặc ngồi]
  T[Test-36] -. đề xuất quan sát .-> V
```

## Đã xác minh
- [THẤY] Worktree không có thư mục `Folder/` và không có bốn tên tệp nguồn khi tìm trong các thư mục mã đã định vị; không có source để đọc tĩnh.
- [TÀI LIỆU] Mục tiêu, danh sách nguồn, giới hạn không chạy và yêu cầu Test-36 được ghi trong JX1_OPS/TASKS/HG-02.md:18-29.
- [TÀI LIỆU] Mục lục tri thức yêu cầu tài liệu mới có dòng liên quan và ghi mức chắc; JX1_OPS/DESIGN/MUC-LUC-TRI-THUC.md:3-5.

## Chưa xác minh
- Ý nghĩa thật của bit `0x02`, giá trị các trạng thái và thứ tự caller/callee.
- Nguyên nhân chính xác khiến nhân vật ngồi khi nhấn nút đánh ngoài trạng thái chiến đấu.
- Kết quả quan sát vung kiếm trên Test-36.
- Build, exe, VM, mạng và runtime đều chưa chạy theo phạm vi task.

## Phát hiện khi chuẩn hóa
- Bốn đường dẫn nguồn trong task không tồn tại tại worktree HG-02; vì vậy báo cáo giữ nguyên mức `PARTIAL` và không tự suy kết luận.
- `D:\JX-wt\HG-02.nhip` không ghi được do quyền sandbox (Access denied); các mốc nhịp được nêu trong báo cáo này nhưng không thay thế được tệp ngoài worktree.
- Không sửa mã nguồn, không chạy VM/exe/mạng và không thay đổi kết luận cũ.

## Bàn giao
- File đầu ra: `JX1_OPS/DESIGN/HIEU-TRANG-THAI-CHIEN-DAU.md`.
- Test thực chạy: chưa chạy; chỉ kiểm tra tĩnh sự tồn tại đường dẫn và soạn tài liệu.
- Bước tiếp theo: PM cung cấp root/version source đúng với task để đọc bốn tệp, xác minh caller/callee, rồi cập nhật các mục CHƯA KIỂM.
- Trạng thái: PARTIAL.

Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report.
Đề xuất bổ sung mục lục: thêm HG-02 vào nhóm “Phím tắt, nút, tự động chiến đấu” sau khi source được đối chiếu.

## HG-02b — Kết quả đối chiếu bổ sung
Trạng thái bổ sung: DONE — đã đối chiếu tĩnh bốn tệp nguồn; phép thử Test-36 chỉ được đề xuất và chưa chạy.

### Luồng đã đối chiếu
```mermaid
flowchart TD
  S[Server: m_FightMode] -->|đóng gói bit 0x02| P[PLAYER_NORMAL_SYNC]
  P -->|client đọc bit| C[Client: Npc.m_FightMode]
  B[Nút đánh: mainSkillattack] --> Q{m_FightMode == 0?}
  C --> Q
  Q -->|Có| D[Gửi do_sit và SendClientCmdSit(TRUE), rồi return]
  Q -->|Không| A[Tìm mục tiêu và chọn kỹ năng]
  L[Lua SetFightState(1)] --> F[KNpc::SetFightMode]
  F --> S
```

### Phạm vi và độ phủ HG-02b
| Phần tử | Trạng thái | Bằng chứng / giới hạn |
|---|---|---|
| Client `KNpcAI.cpp`: nút đánh | Đã phủ | `mainSkillattack` kiểm `m_FightMode`; khi bằng 0 dọn mục tiêu, gửi `do_sit`, gọi `SendClientCmdSit(TRUE)` rồi `return` (C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KNpcAI.cpp:1326-1423). |
| Client `KProtocolProcess.cpp`: nhận trạng thái | Đã phủ | `SyncPlayerMin` đọc bit `0x02` và gán `Npc[nIdx].m_FightMode` (C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KProtocolProcess.cpp:3147-3150). |
| Server `KNpc.cpp`: phát bit và setter | Đã phủ | Đóng gói `m_FightMode` thành `0x02`; setter ghi trường và gọi `CloseAll()` cho player phía server (C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:7806-7814, 15328-15335). |
| Server `ScriptFuns.cpp`: API Lua | Đã phủ | `LuaSetFightState` gọi setter; `LuaGetFightState` trả trạng thái (C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\ScriptFuns.cpp:21133-21151). |
| Đề xuất Test-36 | Đã ghi đề xuất, chưa chạy | Chưa xác minh có điểm gọi script được phê duyệt; luật bản đồ cũng có thể ép trạng thái. |

### Giải thích cho người chơi
[THẤY] Khi nhân vật chưa ở chế độ chiến đấu, `mainSkillattack` đi vào nhánh `m_FightMode == 0`. Nhánh này xóa mục tiêu đang chọn, gửi lệnh ngồi đến máy chủ và phía client, rồi thoát hàm. Vì thoát sớm, lần bấm đó chưa đến đoạn tìm mục tiêu hay chọn kỹ năng. Đây là lý do trực tiếp trong mã cho việc nhân vật ngồi khi bấm nút đánh ngoài trạng thái chiến đấu (C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KNpcAI.cpp:1406-1423).

[THẤY] Server dùng bit `0x02` trong `m_btSomeFlag` để truyền `m_FightMode`; `SyncPlayerMin` ở client đọc bit đó thành trạng thái cục bộ. Đây là bit của trạng thái chiến đấu, không phải bit hoạt ảnh ngồi (C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:7806-7814; C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KProtocolProcess.cpp:3147-3150).

[THẤY] Hàm Lua `SetFightState` đổi số đầu vào khác 0 thành true rồi gọi `KNpc::SetFightMode`. Setter ghi `m_FightMode`; phía server, với player, nó gọi `m_cPK.CloseAll()` (C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\ScriptFuns.cpp:21133-21141, 26147; C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:15328-15335).

[THẤY] Đường tạo gói đồng bộ có thể bật hoặc tắt trạng thái theo `m_nWFight` và điều kiện bảo hộ bản đồ; bản ghi bit và các điều kiện này xuất hiện trong cùng đoạn mã, nhưng trạng thái cuối/hoạt ảnh trên Test-36 chưa được quan sát (C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:8210-8221).

### Đề xuất kiểm tra trên Test-36
[TÀI LIỆU] Nếu Test-36 có điểm chạy script Lua kiểm thử đã được phê duyệt, có thể gọi `SetFightState(1)` cho nhân vật thử, đọc `GetFightState()`, bấm nút đánh và quan sát hoạt ảnh. Chỉ thử trong môi trường riêng phù hợp vì setter gọi `CloseAll()` cho player, và chính sách bản đồ có thể đặt lại trạng thái. Có thể cân nhắc khôi phục `SetFightState(0)` sau phép thử nếu trạng thái trước đó và thủ tục đã được xác nhận.

[CHƯA KIỂM] Chưa xác nhận Test-36 có điểm chạy Lua phù hợp, chưa thực hiện thao tác, và chưa quan sát vung kiếm/ngồi runtime. Không chạy build, exe, VM hoặc mạng.

### Giải mã tên — bổ sung HG-02b
| Tên gốc | Mã hóa | Chữ đúng / diễn giải | Nguồn file:dòng |
|---|---|---|---|
| `mainSkillattack` | ASCII | Hàm xử lý nút đánh | C:\Jx1CocoV3\Folder\Client2912-20260116T044348Z-3-001\Client2912\Client\Classes\gamecore\KNpcAI.cpp:1326 |
| `m_FightMode` | ASCII | Trường trạng thái chiến đấu | C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:7809-7810 |
| `0x02` | ASCII, hexadecimal | Bit chiến đấu trong `m_btSomeFlag` | C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:7809-7811 |
| `SetFightMode` | ASCII | Hàm ghi chế độ chiến đấu | C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\KNpc.cpp:15328-15335 |
| `SetFightState` / `GetFightState` | ASCII | Hàm Lua đặt / đọc chế độ chiến đấu | C:\Jx1CocoV3\SwordOnline\SwordOnline\jxOnline\gameserver\Sources\Core\Src\ScriptFuns.cpp:21133-21151, 26147-26148 |
| `Test-36` | ASCII theo tên task | Môi trường kiểm thử được nêu; chưa chạy | JX1_OPS/TASKS/HG-02b.md:20 |

### Sắp theo cấu trúc game — bổ sung HG-02b
| Tầng | Thành phần | Vai trò đã thấy |
|---|---|---|
| Nút giao chiến client | `mainSkillattack` | Điểm xử lý nút đánh. |
| Trạng thái nhân vật | `m_FightMode` | Nhánh nút đánh đọc trạng thái này. |
| Đồng bộ client/server | `m_btSomeFlag & 0x02` | Server phát, client đọc lại chế độ chiến đấu. |
| Điều khiển script | `SetFightState` → `SetFightMode` | API Lua gọi setter ở server. |
| Nhánh tắt chiến đấu | `do_sit` và `SendClientCmdSit(TRUE)` | Gửi lệnh ngồi rồi thoát khỏi hàm nút đánh. |
| Kiểm thử | Test-36 | Chỉ đề xuất, chưa chạy. |

### MỤC SỔ THÔNG SỐ — HG-02b
| Nhóm | Tên/hằng số | file:dòng | Giá trị | Đơn vị | Ảnh hưởng | Đổi an toàn | Nguồn đo |
|---|---|---|---|---|---|---|---|
| Trạng thái chiến đấu | `m_FightMode` | KNpc.cpp:7809-7810, 15328-15335 | 0 = tắt; tham số Lua khác 0 thành bật | boolean | Nhánh nút đánh và đồng bộ trạng thái | CẨN THẬN | Đọc tĩnh; chưa đo runtime |
| Bit đồng bộ | `m_btSomeFlag & 0x02` | KNpc.cpp:7806-7811; KProtocolProcess.cpp:3147-3150 | Bit đặt khi chế độ bật | bit mask | Chuyển trạng thái server sang client | CẨN THẬN | Đọc tĩnh; chưa đo runtime |
| Tham số Lua | `SetFightState` tham số 1 | ScriptFuns.cpp:21133-21141 | số khác 0 = true; 0 = false | số đầu vào | Gọi setter trạng thái cho người chơi hiện tại | CẨN THẬN | Đọc tĩnh; chưa đo runtime |

### Xác minh và bàn giao HG-02b
- [THẤY] Đã đối chiếu đủ bốn tệp nguồn được task chỉ định; file:dòng được liệt kê trong bảng phạm vi.
- [CHƯA KIỂM] Runtime, Test-36, build, exe, VM và mạng chưa chạy theo phạm vi task.
- Trạng thái phần phân tích tĩnh HG-02b: DONE; thử nghiệm Test-36 vẫn chưa xác minh.
- Bước tiếp theo: người kiểm thử xác nhận điểm gọi Lua và điều kiện bản đồ trước khi thử.
- Đề xuất mục lục: nhóm “Phím tắt, nút, tự động chiến đấu” | tài liệu trạng thái chiến đấu và nút đánh | `mainSkillattack`, `m_FightMode`, `0x02`, `SetFightState` | khảo sát tĩnh, chưa thử Test-36.
- Kỹ năng đã dùng: jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report.
