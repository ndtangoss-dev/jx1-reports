# TÓM TẮT 5 DÒNG
1. DONE trong phạm vi offline: thêm `visibility`, bộ test `test_visibility.py` và fixture ba phiên A/B/Bot trong `test_tester.py`.
2. Tiêu chí 1,2,5,6,7 có đối chiếu gói ADD/REMOVE/SYNC nhận từ fixture; không coi PASS là nghiệm thu server thật.
3. Tiêu chí 3/4 có hàm TODO trả BỎ QUA, ghi rõ thiếu semantic combat và gói/mã từ chối mời đội/giao dịch/PK; tiêu chí 8 thuộc B-04.
4. TESTER 22/22 đạt; lượt xác minh visibility cuối 4/4 đạt, bao gồm tám trace lỗi chủ động và CLI `python -I`.
5. [CHƯA KIỂM] gs001/ABI/kill/cấp nhóm thật/ảnh/tick; không mạng thật/VM/exe, không thêm mật khẩu/khóa, không commit/push vì không được yêu cầu.

## Phạm vi thực hiện

Ngày 17/11/2026, worktree `D:\JX-wt\B-03`, nhánh
`task/B-03-test-2p1bot`. Kiểm status/branch một lần trước khi ghi: chỉ task
`JX1_OPS/TASKS/B-03.md` untracked; giữ nội dung đó, chỉ thêm mục Kết quả theo
chỉ thị người dùng. Các thay đổi còn lại chỉ nằm trong TESTER và báo cáo này.

Đã đọc B-01 mục 8, E-05a, E-05b, B-02c và mã TESTER/BOT liên quan. Đọc thêm
đúng bảng NPC trong E-01b để xác nhận ID/kích thước, không đọc nguồn canonical.
E-07/E-08 chưa có báo cáo khớp trong thư mục REPORTS ở checkout này; giữ TODO
theo task, không tự đoán giao thức còn thiếu hoặc kết nối để khảo sát.

## Cài đặt và đối chiếu

`TESTER/visibility.py::VISIBILITY` có tám bước; đăng ký trong `run.py`.
Mỗi lượt worker mở ba `Channel` riêng: A=101, B=102, Bot=201. `--bots bot01`
là một nhóm ba phiên; thêm bí danh tạo thêm nhóm độc lập, không phải đổi A/B
thành các worker cần đồng bộ chéo. Context lưu nhóm có `close()` để core dọn
cả ba kết nối khi xong hoặc FAIL. Watchdog và PASS/FAIL/BỎ QUA dùng core sẵn có.

`NpcView.apply` gọi `BOT.worldsync.split_records` để kiểm toàn frame trước khi
áp state. Bộ quan sát từ chối ADD lặp, SYNC chưa ADD/đã REMOVE, REMOVE chưa thấy;
đối chiếu tập NPC cuối pha và chặn mọi ADD/SYNC NPC phải ẩn, kể cả sau đó đã
REMOVE trong cùng payload. Mỗi pha ghi viewer/events/tập thấy được; packet body
được che bởi `Context.packet` như khung hiện có.

| Tiêu chí B-01 | Kiểm offline đã thực hiện | Giới hạn |
| --- | --- | --- |
| 1 | Solo: A/B chỉ thấy chính mình và Bot, cùng nhận ADD/SYNC Bot | [CHƯA KIỂM] màn hình và luật server thật |
| 2 | A gửi một C2S SKILL; A/B và phiên Bot cùng nhận REMOVE đúng Bot | [CHƯA KIỂM] sát thương/death, quan hệ nhân quả kill; REMOVE chỉ chứng minh biến mất trong trace |
| 3 | `todo_skill_visibility`: BỎ QUA/TODO | [CHƯA KIỂM] giải mã HP/hurt/death, kết quả nhắm mục tiêu/AoE; C2S SKILL 77 đã có nhưng chưa đủ; theo E-07/E-08 |
| 4 | `todo_invite_visibility`: BỎ QUA/TODO | [CHƯA KIỂM] request/response mời đội, giao dịch, PK và mã từ chối tương ứng; theo E-07/E-08 |
| 5 | Trace cùng nhóm MaxVisible=2 rồi MaxVisible=1, người thứ hai bị tách, Bot vẫn thấy | [CHƯA KIỂM] allocator/VisGroup thật; ba phiên không kiểm trần lớn hơn hai người thật |
| 6 | Cùng nhóm → tách → cùng nhóm → tách → cùng nhóm; bắt thiếu REMOVE/ADD, SYNC người ẩn | [CHƯA KIỂM] client/render và RefreshVisibility thật |
| 7 | So từng byte trace baseline gốc fixture với trace Enabled=0, cả ba viewer | [CHƯA KIỂM] bật/tắt config, capture baseline binary và ảnh thật |
| 8 | Ngoài B-03, thuộc B-04 | [CHƯA KIỂM] tick/băng thông |

ID/độ dài theo E-01b: NPC_SYNC=76 (42..106), NPC_NORMAL_SYNC=77 (227),
NPC_REMOVE=84 (9). **Offset identity (3 cho 76, 1 cho 77/84) là hợp đồng fixture,
[CHƯA KIỂM] với source field/ABI binary thật.** Không trình bày parser này như
decoder đã xác nhận dùng được với gs001. Không sửa BOT hoặc guard của BOT.

## Fixture và độ tin cậy của test

Mở rộng `test_tester.fake_server(..., visibility=True)`; smoke mặc định giữ
hành vi cũ. Fixture chỉ bind `127.0.0.1` cổng ngẫu nhiên. Script sự kiện theo
viewer/phase được viết riêng, không gọi luật/bộ quan sát visibility để sinh
đáp án. Dùng framing/XOR hiện có và phân mảnh gửi từng bảy byte. HELLO/vector
tổng hợp có sẵn của tester được dùng trong RAM; không thêm mật khẩu/khóa vào
source hay báo cáo, không đọc credential thật. Không gửi login, không chạy game.

RUN x=phase/y=viewer/map=1 là **điều khiển fixture**, không phải giao thức đổi
nhóm server. Fixture kiểm phase tăng đúng thứ tự, viewer giữ nguyên và một
SKILL từ A sau pha Solo. Script này kiểm khả năng phát hiện trace sai của tester,
không chứng minh implementation visibility của server đúng.

Bốn test mới kiểm:

- Luồng dương: đúng ba phiên, chín phase/phiên, một SKILL, 6 PASS + 2 BỎ QUA;
  hai TODO đều có `[CHƯA KIỂM]` và E-07/E-08.
- Tám trace âm: SYNC người ẩn; ADD rồi REMOVE người ẩn; thiếu REMOVE Bot ở B;
  lộ người vượt trần; lọc nhầm Bot theo trần; thiếu REMOVE khi đổi nhóm; thiếu
  ADD khi vào lại; Enabled=0 lệch một byte. Tất cả FAIL đúng bước dự kiến,
  không do timeout/ngoại lệ socket; fixture không có lỗi.
- Frame có ADD hợp lệ rồi REMOVE bị cắt: ProtocolError, không áp state nửa frame.
- CLI subprocess `python -I .../run.py --scenario visibility --bots bot01`:
  exit 0, ba phiên, báo cáo có gói/TODO/BỎ QUA, không sinh BUG. Báo cáo chạy test
  và BUG nằm trong thư mục tạm, không ghi ngoài vùng task trong repository.

## Kiểm chứng đã chạy

```text
python -I -m unittest discover -s JX1_OPS/TESTER -v
Ran 22 tests in 36.805s
OK; exit 0

python -I -m unittest discover -s JX1_OPS/TESTER -p test_visibility.py -v
Ran 4 tests in 2.682s
OK; exit 0
```

Lượt riêng cuối xác minh phần bổ sung chặn ADD rồi REMOVE người ẩn. Không chạy
lại toàn bộ suite sau bổ sung này vì thay đổi chỉ ở visibility/nhánh fixture
tương ứng; suite đầy đủ đã đạt, lượt riêng kiểm hành vi cuối đã đạt. BOT không
sửa và không chạy lại suite BOT. Không build, không chạy exe hay kết nối VM,
DNS hoặc mạng thật; socket duy nhất là fixture loopback.

## Lỗi công cụ và bàn giao

PowerShell đọc task lượt đầu sai dấu; đọc lại UTF-8, không sửa encoding file.
`rg : The term 'rg' is not recognized ...`: chuyển sang Get-ChildItem/
Select-String có phạm vi. Một lượt đọc nhầm `BOT/world.py` báo `Cannot find path`;
đã đọc đúng `BOT/worldsync.py`. Một đầu ra gộp dài bị cắt, đọc bổ sung phần cần.
Không có test thất bại, không cài công cụ, đổi quyền/cấu hình hay vượt sandbox.

Trạng thái **DONE cho bộ kịch bản/kiểm chứng offline**. Nghiệm thu server thật
vẫn **[CHƯA KIỂM]** theo các giới hạn trên. Không có commit SHA mới hoặc link
GitHub: task không yêu cầu stage/commit/push và cấm mạng; kết quả giữ local để
rà soát. Không sửa tài liệu bài học hoặc tác động nguồn canonical.
