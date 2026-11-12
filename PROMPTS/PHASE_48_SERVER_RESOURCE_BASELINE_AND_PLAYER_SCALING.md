# PHASE 48 — SERVER RESOURCE BASELINE & PLAYER SCALING

## Mục tiêu
Đo tài nguyên **bên trong VM server thử nghiệm** để dự tính cấu hình VPS phù hợp. Không dùng số liệu máy Host làm dữ liệu chính vì Host còn chạy VirtualBox, LDPlayer, Claude Code và các tiến trình khác.

## Ranh giới an toàn
- Chỉ đo VM thử nghiệm JX-Test-36. Tuyệt đối không khởi động, thay đổi, đăng nhập hoặc tác động Main VM JX-Server-D.
- Không thay đổi cấu hình VM, số vCPU/RAM, cấu hình server, tick rate, dịch vụ hoặc firewall.
- Không restart/stop dịch vụ để phục vụ phép đo.
- Không cài phần mềm mới nếu chưa được duyệt. Ưu tiên công cụ sẵn có trong VM.
- Không ghi mật khẩu, token, thông tin đăng nhập, IP riêng hoặc bí mật vào log/GitHub.
- Nếu không xác định chắc VM đích, dừng và báo BLOCKED.
- Không tạo thêm tài khoản/người chơi ngoài nhân vật test đã được duyệt.
- Chỉ dùng nhân vật thử và hoạt động gameplay an toàn.

## Nguyên tắc đo
Nguồn số liệu chính phải lấy **bên trong guest VM**:
1. CPU tổng VM/guest và CPU từng tiến trình.
2. RAM guest: tổng, khả dụng, used, cache/buffers, commit nếu có.
3. RAM từng tiến trình: RSS/Working Set/Private Bytes tùy OS và công cụ có sẵn.
4. Swap/pagefile: mức sử dụng và hoạt động paging.
5. Network interface trong guest: RX/TX bytes, packets, tốc độ trung bình/peak.
6. Từng dịch vụ server: GameServer, Bishop, Goddess, PaySys và các tiến trình liên quan thực tế đang chạy.
7. Số phiên/kết nối người chơi; chỉ dùng phương pháp quan sát không gây tải hoặc làm gián đoạn kết nối.
8. GameServer tick thực tế: xác minh duy trì 36 tick/s; ghi min/avg/max và tick hụt nếu log/telemetry cho phép.
9. Uptime, số CPU core/vCPU guest được cấp, RAM guest được cấp, OS và phiên bản.
10. Timestamp đồng bộ cho mọi mẫu.

Không lấy CPU/RAM trên Host làm kết quả chính. Có thể ghi Host metadata riêng để chẩn đoán, nhưng tuyệt đối không trộn vào phép tính guest. VRAM/GPU không phải tài nguyên mặc định của game server headless; kiểm tra xem guest có GPU passthrough/3D workload hay không. Nếu không có, ghi N/A/không áp dụng, không suy diễn VRAM của LDPlayer thành VRAM server.

Không cộng RSS các tiến trình một cách máy móc để suy ra RAM tổng nếu có shared pages. Báo cáo cả guest total và process-level; giải thích khác biệt.

## Kịch bản đo theo từng mốc
Mỗi mốc:
- Chờ server ổn định sau startup/đăng nhập trước khi lấy mẫu.
- Lấy mẫu mỗi 1 giây trong 10 phút nếu khả thi; nếu công cụ/log có giới hạn, ghi rõ tần suất và thời lượng thực tế, không giả làm đủ.
- Dùng cùng cấu hình VM, cùng server build, cùng server tick 36Hz, cùng map và điều kiện càng giống nhau càng tốt.
- Ghi timestamp bắt đầu/kết thúc, số mẫu, mẫu lỗi/mất, hoạt động người chơi.
- Lưu raw CSV/JSON và log gốc đã lọc bí mật; có script phân tích nếu phù hợp.

### Mốc A — 0 user (baseline)
- Server đã chạy ổn định, không có người chơi đăng nhập.
- Đo 10 phút: guest CPU/RAM/swap/network, tiến trình, tick, kết nối.
- Ghi hoạt động nền server (AI/quái/tác vụ định kỳ) nếu quan sát được.

### Mốc B — 1 user (Sonnet)
- Sonnet đăng nhập bằng nhân vật test được duyệt trên LDPlayer.
- Ghi rõ account/character bằng alias không nhạy cảm, không ghi credential.
- Tách hoạt động thành các đoạn có timestamp:
  1. đứng yên;
  2. di chuyển/chạy/cưỡi ngựa nếu hợp lệ;
  3. chiến đấu/ra kỹ năng nếu nhân vật và điều kiện cho phép.
- Đo 10 phút hoặc báo rõ thời lượng khả thi.
- Không yêu cầu Sonnet đánh/tiêu hao vật phẩm hoặc thay đổi trạng thái nguy hiểm.

### Mốc C — 2 users
- Giữ Sonnet đang đăng nhập và hoạt động theo kịch bản đã ghi.
- Người dùng đăng nhập thêm từ Xiaomi 13T Pro; không yêu cầu người dùng cung cấp mật khẩu trong báo cáo.
- Người dùng chơi theo kịch bản được thống nhất; ghi timestamp các đoạn đứng yên/di chuyển/chiến đấu.
- Đo 10 phút nếu khả thi.
- Không thay đổi cấu hình server/VM giữa các mốc.

Nếu chưa thể thực hiện mốc C vì cần người dùng đăng nhập, hoàn thành A/B, lưu baseline và dừng chờ. Không giả lập số liệu C.

## Phân tích
Báo cáo cho từng mốc:
- CPU guest avg, median, P95, P99, max; nếu có nhiều vCPU, nêu rõ cách biểu diễn phần trăm.
- CPU avg/P95/max theo tiến trình.
- RAM guest used/available/total và peak.
- RAM từng tiến trình (RSS/Working Set/Private Bytes), nêu rõ loại metric.
- Swap used và paging activity.
- Network RX/TX trung bình, P95, peak; bytes và packets.
- Tick avg/min/max, số tick hụt nếu có.
- Số phiên/kết nối thực tế.
- Sự kiện bất thường và timestamp.

So sánh:
- Delta B-A = chi phí tăng thêm khi có một user (tách đứng yên/di chuyển/chiến đấu nếu đủ dữ liệu).
- Delta C-B = chi phí tăng thêm khi user thứ hai vào.
- Tách tải nền, chi phí duy trì phiên kết nối và chi phí hoạt động gameplay.
- Không giả định tải tuyến tính. Chỉ đưa ra ước lượng sơ bộ 10/50/100/500 users nếu nêu rõ giả định và độ bất định; không coi phép nhân tuyến tính là capacity test.

## Kiểm soát chất lượng
- Không gọi đây là benchmark nếu số mẫu/thời lượng không đủ; ghi “đo thăm dò”.
- Phân biệt CPU guest với CPU host; RAM guest với RAM host.
- Không dùng FPS/CPU của LDPlayer làm tải server.
- Không suy luận VRAM server từ GPU/VRAM client.
- Kiểm tra tick 36Hz không bị tụt trong các giai đoạn.
- Nêu giới hạn: VM ảo hóa không hoàn toàn tương đương VPS; cần lưu cấu hình guest và giới hạn tài nguyên.

## Sonnet và quy trình QA
- Sonnet thực hiện thao tác gameplay và thu thập dữ liệu nếu công cụ hiện có cho phép.
- Claude Code/agent có quyền đọc telemetry guest thực hiện thu thập tự động. Xác minh công cụ trước khi dùng.
- Sonnet không điều khiển cùng LDPlayer đồng thời với agent khác.
- Nếu Sonnet không có quyền đọc guest metrics, báo BLOCKED cụ thể; không tự ý cài agent vào VM.
- Sau khi hoàn tất A/B, Sonnet lưu dữ liệu và tiếp tục khám phá game theo Autonomous QA nếu còn hạn mức. Không chờ Opus giao từng thao tác.
- Opus review phương pháp, số liệu và kết luận; không sửa server trong nhiệm vụ benchmark.

## Đầu ra bắt buộc
Tạo:
- `TEST_RESULTS/48-server-resource-measurement.md` — báo cáo.
- `experiments/server-resource/phase48-raw.csv` hoặc JSON — số liệu thô.
- `experiments/server-resource/phase48-summary.csv` — số liệu tổng hợp.
- Script thu thập/phân tích nếu có, kèm hướng dẫn chạy và giới hạn.
- Cập nhật `00_LATEST_STATUS.md`.

Báo cáo phải ghi:
- VM xác minh là JX-Test-36 (không phải Main VM).
- Guest OS, vCPU, RAM, server build, tick rate.
- Mốc A/B/C đã thực sự chạy và thời lượng.
- Công cụ và nguồn metric.
- Raw data, số mẫu, missing samples.
- Avg/P95/P99/peak.
- Delta theo số user và hoạt động.
- VRAM: đo được hay N/A và lý do.
- Giới hạn, rủi ro ngoại suy và đề xuất cấu hình VPS sơ bộ.
- Trạng thái từng mục: VERIFIED / NOT TESTED / BLOCKED.

## Điều kiện hoàn thành
- A và B có số liệu guest-side có thể kiểm tra lại.
- C chỉ PASS khi người dùng thực sự đăng nhập và số liệu được thu thập; nếu chưa, ghi PENDING USER.
- Không tác động Main VM.
- Không thay đổi cấu hình hoặc dịch vụ server.
- Không commit source server.
