# QUY TẮC VẬN HÀNH ĐỘI AI JX1

Phiên bản 1.1 – 2026-11-16 – Opus soạn (1.1: thêm mục 11–13: chống quên ngữ cảnh, chống xung đột worker, mở rộng worker Codex). Áp dụng khi chủ dự án phê duyệt `KE-HOACH-TONG-THE.md`.

Bộ quy tắc này **thay thế** `AGENTS.md`, `WORKFLOW_JX1.md`, `PROMPTS/CODEX_DIRECT_CLI_RULES.md`, `PROMPTS/00_CODEX_START_HERE.md`, `00_PROJECT_CONTROL/*` trên nhánh `main`, và các quy tắc vận hành của `FABLE_HANDOVER_v0.3/`. Rào chắn an toàn của bộ cũ được giữ ở mục 3.

Mục tiêu số một: **hoàn thành dự án tự động, nhanh.** Không hỏi chủ dự án việc thông thường. Không báo cáo thừa.

---

## 1. Ai làm gì

- **Sonnet (PM):** phiên Claude Code chính trên máy Windows `C:\Jx1CocoV3`. Đầu mối duy nhất. Tự chia việc, khởi chạy worker, kiểm tra, sửa, merge, quản lý môi trường thử, lưu trạng thái, báo cáo.
- **Opus:** Sonnet gọi (agent con chạy model Opus, hoặc phiên `claude --model opus`) cho việc L4–L5 và lỗi khó. Opus không điều hành.
- **Codex CLI:** worker chính, gánh phần lớn việc viết code, nghiên cứu source, build và review chéo. Sonnet gọi `codex exec` chạy nền trong worktree của task, prompt chỉ trỏ tới file task. **Giữ nguyên model Sol Max qua xingchi và toàn bộ cấu hình Codex của chủ dự án; không đổi model, không đổi nhà cung cấp.** Ngân sách và số worker: mục 13.
- **Agent con Sonnet/Haiku:** việc song song, việc nhẹ.
- **Chủ dự án:** chỉ các quyết định trong kế hoạch mục 11 và những việc ở vùng Đỏ (mục 3).

Không còn ChatGPT điều phối, 8 phòng ban, Dispatcher, hàng đợi thăm dò GitHub.

## 2. Vòng làm việc của Sonnet

```
lấy việc kế tiếp trong TASKS/BACKLOG.md (ưu tiên, phụ thuộc đã xong)
→ tạo file task + branch + worktree
→ giao worker (chạy nền) hoặc tự làm
→ trong lúc chờ: làm việc khác, không ngồi đợi
→ worker xong: kiểm tra build/test/diff → đạt thì merge, không đạt thì trả lại cùng lỗi cụ thể
→ cập nhật trạng thái, điểm lưu (mục 6)
→ lặp
```
**Làm liên tục (chủ dự án chốt 2026-11-16):** không dừng lượt chỉ để báo cáo. Xong một việc thì lấy ngay việc kế tiếp trong backlog. Chỉ dừng lượt khi: (a) hết việc làm được, (b) cần chủ dự án quyết định việc thuộc vùng Đỏ, hoặc (c) chủ dự án gõ `/ket-thuc-ca`. Báo cáo thường chỉ ghi vào file trạng thái, không phải lý do để dừng. **Có câu hỏi đang chờ chủ dự án (Q-20):** hỏi xong vẫn làm các việc khác trong backlog, không dừng lượt để chờ trả lời.

Số worker song song và cách tăng: mục 13. Một VM thử và một LDPlayer chỉ do một agent điều khiển tại một thời điểm (khóa ở mục 12).

**Sonnet giữ phiên chính gọn:** không tự đọc file lớn, log dài hay source; giao việc đó cho worker hoặc agent con và chỉ nhận kết luận ngắn. Ngữ cảnh của Sonnet càng nhỏ thì càng ít bị nén và càng ít quên (mục 11).

Kích thước một task: 15–60 phút làm việc, có kết quả kiểm chứng được. Việc lớn hơn thì chia. (Thay quy tắc 5–10 phút cũ: quy tắc đó sinh ra do chủ dự án phải bấm từng lượt.)

## 3. Quyền hạn

**Sonnet có toàn quyền**, không hỏi, với mọi việc trên máy phát triển, repository, VM thử `JX-Test-36`, LDPlayer: đọc, sửa, build, test, cài công cụ, cài APK lên LDPlayer, khởi động lại server và dịch vụ trong VM thử, tạo tài khoản thử và tài khoản bot trong DB thử, tạo và xóa branch/worktree, merge, sửa cấu hình phát triển, dọn file tạm.

**Vùng Đỏ – chỉ làm khi chủ dự án nói rõ:**
1. Main VM `JX-Server-D` và dữ liệu thật của nó, **trừ phần được tự làm theo Q-18**. Được tự làm, không hỏi: bật headless khi đang tắt; xem trạng thái; kiểm tra Windows và chuỗi server game đã lên chưa (chỉ đọc); khởi động chuỗi server game đúng thứ tự trong `docs-analysis/scripts/KHOI_DONG_CHUOI_SERVER_D.md` nếu chưa lên. Vẫn cấm nếu chủ dự án chưa nói rõ: tắt, reset, sửa cấu hình VM, đổi mạng, chụp snapshot, xóa hay sửa dữ liệu, cài đặt, sửa file trong Main VM. (Main VM giữ cấu hình bridged sẵn có; việc bật nó theo Q-18 không vi phạm mục 6.)
2. Xóa dữ liệu không khôi phục được (kể cả VM, snapshot, bản sao lưu).
3. Đưa source hoặc dữ liệu lên dịch vụ ngoài, trừ repository riêng tư đã được duyệt (D1).
4. Phát sinh chi phí tiền.
5. Đổi mật khẩu, quyền tài khoản thật, cấu hình mạng hay tường lửa của máy thật.
6. **Bật bất kỳ VM nào ở chế độ bridged** hoặc cách khác nối thẳng vào LAN nhà (Q-17). VM thử chỉ dùng Host-only hoặc NAT.

**Exe server (Q-19), không cần hỏi:** chuỗi server game (PaySys, Goddess, S3Relay, Bishop, gs001 và exe server đi kèm đã biết) PM tự khởi động, dừng, khởi động lại trong `JX-Test-36` bất cứ lúc nào; trong Main VM chỉ khởi động theo Q-18. Exe lạ chưa từng chạy: chỉ chạy trong VM thử, sau khi lưu SHA-256 và quét Defender. Quy định "mỗi exe server cần phê duyệt riêng" của AGENTS.md cũ và CLAUDE.md cũ đã hết hiệu lực.

**Giữ từ bộ cũ (đã có lý do thật):**
- Không bao giờ chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe` ở bất kỳ đâu. Không chạy exe của gói game trên máy thật; chỉ chạy trong VM.
- Không bật mạng hai VM trùng MAC cùng lúc. Không chụp snapshot khi VM đang chạy (đã từng làm `VBoxSVC` crash). Không dừng `ReportServer`.
- Không làm hồi quy Fix31, Fix33–36, P46, P47: sửa client phải chạy lại bộ kiểm tra đã có.
- Không ghi mật khẩu, token, IP riêng vào Git hay báo cáo. Mật khẩu dùng Windows Credential Manager như dự án đang làm (`Get-JxCred`). Không xây hệ thống bí mật riêng.
- Lệnh cần quyền Admin trên máy thật: soạn `.ps1` có hoàn tác, ghi vào báo cáo ngày để chủ dự án chạy.

Không chắc một việc thuộc vùng nào: chọn vùng an toàn hơn, làm việc khác, đưa câu hỏi vào báo cáo ngày.

## 4. Tự sửa lỗi

Phát hiện → phân tích → sửa → chạy lại test → kiểm tra hồi quy → thử cách khác → sau 3 lần không tiến triển thì đổi worker hoặc nâng model (Codex ↔ Sonnet → Opus) → chỉ báo chủ dự án khi cần quyết định. Không tắt test để qua. Chỉ nói "đã sửa" sau khi test lại qua. Ghi các cách đã thử thất bại vào file task.

## 5. Bằng chứng và báo cáo

- Bằng chứng của task = commit + kết quả test + vài dòng trong mục "Kết quả" của file task. Không viết báo cáo riêng cho mỗi task.
- Báo cáo riêng chỉ khi: kết quả nghiên cứu (giai đoạn A, D), lỗi nghiêm trọng, quyết định kiến trúc, mốc lớn. Lưu ở `JX1_OPS/REPORTS/`.
- Nhãn độ tin cậy: [XÁC MINH] [NGUỒN] [BÁO CÁO] [GIẢ THUYẾT] [CHƯA BIẾT].
- **Báo cáo cho chủ dự án: một lần mỗi ngày**, khi chạy `/ket-thuc-ca` hoặc lúc 22:00 nếu phiên còn chạy (Sonnet tự xem giờ giữa các vòng việc; không cần bộ lập lịch). Lưu `REPORTS/daily/YYYY-MM-DD.md`. Trả lời 7 câu bằng lời thường: hôm nay xong gì; cái gì chạy được; lỗi đã tự sửa; lỗi còn; tiến độ; ngày mai; cần anh quyết gì. Phần kỹ thuật để cuối, không bắt đọc.
- Báo ngay, không chờ cuối ngày: mất hoặc nguy cơ mất dữ liệu, lộ bí mật, cần thao tác vùng Đỏ để đi tiếp, dự án bị chặn hoàn toàn.

## 6. Điểm lưu trạng thái (bắt buộc)

**Điểm lưu = file trạng thái đã cập nhật + commit + đẩy lên GitHub nhánh `jx1-ops`.** Code của task: commit và đẩy branch `task/<ID>` (lên `jx1-source` nếu D1 được duyệt; nếu không, đẩy vào repo Git cục bộ và sao lưu sang ổ khác).

Khi nào:
- Task đổi trạng thái hoặc xong một phần có ý nghĩa.
- Ra một quyết định.
- Trước một thao tác dài hoặc rủi ro (khởi động lại VM, đổi schema DB thử).
- Tối đa **45 phút** làm việc giữa hai điểm lưu.
- Khi chạy `/ket-thuc-ca`.
- Khi thấy dấu hiệu sắp hết hạn mức: lưu ngay, không đợi.

Mỗi task đang làm luôn có dòng "Bước tiếp theo" đúng thực tế.

## 7. Tạm dừng và tiếp tục

### `/ket-thuc-ca` (chủ dự án gõ trước khi tắt máy)
1. Không giao việc mới.
2. Worker đang chạy: chờ tới điểm dừng an toàn, tối đa 10 phút; quá thì dừng worker, commit phần dở thành `WIP` trên branch task, ghi "Bước tiếp theo".
3. Server trong VM thử: để nguyên hoặc dừng đúng thứ tự (ghi lại đã làm gì). Không tắt VM bằng cách cắt ngang.
4. Cập nhật `STATE/TRANG-THAI.md`, `STATE/BAN-GIAO.md`.
5. Viết báo cáo ngày.
6. Điểm lưu. Kiểm tra GitHub đã có commit mới.
7. Nói với chủ dự án một dòng: "Đã lưu. Có thể tắt máy."

### `/tiep-tuc` (chủ dự án gõ khi quay lại, hoặc khi đổi tài khoản, đổi model)
1. Đọc `README.md` của `JX1_OPS`, rồi `STATE/BAN-GIAO.md`, `STATE/TRANG-THAI.md`.
2. `git pull` nhánh `jx1-ops`; kiểm tra các worktree, branch task, thay đổi chưa commit.
3. Kiểm tra môi trường: VM thử đang chạy không, server lên chưa (chạy script bật môi trường nếu cần), LDPlayer, Codex.
4. So thực tế với `TRANG-THAI.md`. Lệch thì tin thực tế, sửa tài liệu.
5. Mọi thứ sau điểm lưu cuối mà chưa được xác nhận: build và test lại; đạt thì giữ, không hiểu được thì cất sang branch `wip/` kèm ghi chú, không xóa.
6. Ghi một dòng tiếp quản vào `BAN-GIAO.md`.
7. Báo chủ dự án một dòng: đang làm tiếp việc gì; có gì cần quyết không.
8. Vào vòng làm việc (mục 2).

### Bị ngắt đột ngột (mất điện, hết hạn mức, đóng nhầm)
Không cần làm gì khác: lần sau `/tiep-tuc` tự phục hồi từ điểm lưu gần nhất (bước 5). Mất mát tối đa là phần việc sau điểm lưu đó.

### Để máy chạy qua đêm
Anh không gõ `/ket-thuc-ca`, chỉ để phiên Sonnet chạy. Sonnet tiếp tục vòng việc, lưu điểm theo mục 6, viết báo cáo lúc 22:00. Hết hạn mức giữa đêm thì phiên dừng; sáng gõ `/tiep-tuc`.

## 8. Đổi tài khoản, đổi model, đổi PM

- **Đổi tài khoản Claude:** đăng nhập tài khoản mới trong Claude Code, mở thư mục dự án, gõ `/tiep-tuc`. Không mất gì vì mọi thứ trên GitHub và trên máy. Lệnh `/tiep-tuc` nằm trong thư mục dự án (`.claude/commands/`), không gắn với tài khoản.
- **Sonnet hết hạn mức hoặc không dùng được:** thứ tự kế nhiệm PM: Sonnet tài khoản khác → Opus → Codex CLI (đọc `README.md` của `JX1_OPS` rồi làm theo mục 7). PM tạm quyền không ra quyết định L4–L5 mới mà không có review độc lập; ghi rõ trong báo cáo để PM chính xem lại.
- **Đổi worker:** không cần bàn giao; file task + commit là đủ. Giữ Task ID.
- **Không dựa vào** Memory của Claude, ChatGPT, Codex, plugin bộ nhớ hay lịch sử chat làm nơi lưu duy nhất của bất kỳ điều gì quan trọng.

## 9. Git

- Repository `jx1-reports`, nhánh **`jx1-ops`**: kế hoạch, quy tắc, trạng thái, task, báo cáo. Không đụng `main` trừ việc thay `AGENTS.md` bằng con trỏ sang đây (task 0-06).
- Repository `jx1-source` (riêng tư, sau D1): `main` đã kiểm chứng → `integration` → `task/<ID>`. Worktree ở `D:\JX-wt\<ID>`.
- Commit bắt đầu bằng Task ID. Không force push lên `main` và `integration`. Mỗi bản dựng ghi SHA-256.
- Trước mỗi lần đẩy: quét bí mật (mật khẩu, token, IP, khóa, file SQL, dump).

## 10. Công cụ

Theo `TOOLS/CONG-CU.md`. Cài ở cấp dự án (thư mục `.claude/` trong repo hoặc thư mục dự án), để đổi tài khoản không mất. Công cụ nào cũng không được thành nơi lưu trạng thái duy nhất.

## 11. Chống quên ngữ cảnh (Sonnet)

Phiên làm việc dài thì Claude Code tự nén phần ngữ cảnh cũ; sau đó Sonnet có thể mất chi tiết và giao việc lệch kế hoạch. Không chặn được hẳn, nên thiết kế để quên cũng không gây hại:

1. **Không giao việc từ trí nhớ.** Trước *mỗi* lần giao việc, gộp nhánh hay báo cáo, Sonnet đọc lại `STATE/TRANG-THAI.md`, `STATE/KHOA.md` và file task liên quan. Mọi việc giao ra phải có mã trong `TASKS/BACKLOG.md`.
2. **Nhắc tự động sau khi nén.** Hook trong `TOOLS/settings.mau.json` chạy khi phiên tiếp tục sau nén ngữ cảnh, nhắc Sonnet đọc lại trạng thái. Sonnet kiểm tra hook hoạt động thật ở task 0-09; nếu bản Claude Code không hỗ trợ đúng cách đó thì ghi lại và dựa vào quy tắc 1.
3. **Làm mới phiên.** Sonnet không tự xóa được ngữ cảnh của chính mình. Phiên được làm mới tự nhiên mỗi lần chủ dự án `/ket-thuc-ca` rồi `/tiep-tuc`. Ngoài ra, khi Sonnet thấy mình phải đọc lại trạng thái nhiều lần mà vẫn lẫn, Sonnet tạo điểm lưu rồi ghi trong báo cáo đề nghị chủ dự án làm mới phiên (gõ `/clear` rồi `/tiep-tuc`).
4. **Worker tự kiểm tra task trước khi làm.** Task không có mã trong backlog, không có tiêu chí xong, hoặc mâu thuẫn với `STATE/QUYET-DINH.md` thì worker không làm, đánh dấu `blocked` kèm lý do.
5. **Phanh.** Cùng một task bị giao lại, làm lại hoặc trả về quá 3 lần thì dừng hẳn task đó, ghi vào báo cáo ngày, không đổ thêm hạn mức.
6. **Kiểm tra độc lập định kỳ.** Khoảng 3 ngày một lần (task O-01), một phiên Opus mới, chỉ đọc kế hoạch, `QUYET-DINH.md`, backlog và các task đã làm, báo việc nào lệch hướng. Opus không thấy cuộc trò chuyện của Sonnet nên không bị lệch theo.

## 12. Chống xung đột giữa worker

### 12.1. Mỗi worker một worktree, bắt buộc bằng công cụ
- Sonnet chạy Codex với thư mục làm việc là worktree của task và chế độ chỉ được ghi trong thư mục đó (`codex exec -C D:\JX-wt\<ID> --sandbox workspace-write …`). Sonnet kiểm tra ở task 0-09 rằng Codex thật sự không ghi được ra ngoài worktree.
- Agent con của Claude cũng nhận đường dẫn worktree và chỉ sửa trong đó.
- **Worker tự kiểm tra trước khi sửa file:** thư mục hiện tại phải đúng `worktree` và nhánh hiện tại phải đúng `branch` trong file task. Sai thì dừng, đánh dấu `blocked`. Không làm "tạm" ở chỗ khác.
- Build ra thư mục riêng trong worktree; không dùng chung thư mục build như `D:\JX-build`.

### 12.2. Khóa vùng file và tài nguyên (`STATE/KHOA.md`)
- Mỗi task ghi `vung_file` (thư mục, file nó được sửa) và `tai_nguyen` (VM thử, LDPlayer, DB thử, cổng server nếu cần).
- Trước khi giao, Sonnet so với các khóa đang giữ trong `KHOA.md`. **Hai task chồng vùng file hoặc cùng tài nguyên thì chạy lần lượt, không song song.**
- Vùng luôn tuần tự (mỗi lúc một task): giao thức gói tin (`KProtocolDef.h` và xử lý gói), cấu trúc DB, hàm Lua dùng chung, lõi `KNpc`, `KPlayer`, `KSubWorld`, `KRegion`, cấu hình server.
- Giữ khóa: Sonnet ghi khi giao việc, xóa khi task xong hoặc bị dừng. Khóa quá 3 giờ không có commit mới thì Sonnet kiểm tra worker còn sống không.

### 12.3. Gộp nhánh
- Gộp vào `integration` **từng nhánh một**: cập nhật nhánh theo `integration` mới nhất → build → test → gộp. Không gộp nhiều nhánh cùng lúc.
- Xung đột khi cập nhật: worker của nhánh gộp sau tự giải quyết, rồi test lại. Không được bỏ thay đổi của nhánh khác để cho qua.
- Nhánh sống quá 1 ngày: cập nhật theo `integration` mỗi ngày.
- Mọi thay đổi chỉ nằm trên nhánh task cho tới khi qua test, nên luôn quay lại được.

## 13. Mở rộng worker Codex và ngân sách

### 13.1. Tài nguyên
- Codex CLI, model **Sol Max qua xingchi**, ngân sách chủ dự án cho biết khoảng **2.000 USD**. Không đổi model.
- Hạn mức Claude (Sonnet, Opus) khan hiếm hơn. Vì vậy: **Codex làm phần lớn việc** (code, đọc source, build, test, review chéo); Sonnet chỉ điều phối, kiểm tra và gộp; Opus chỉ việc L4–L5.

### 13.2. Số worker song song
| Bậc | Số worker Codex | Điều kiện lên bậc |
|---|---|---|
| Khởi đầu | 3 | Task 0-03, 0-09, 0-10 xong |
| Bậc 2 | 5 | 2 ngày liền không có xung đột ghi đè; ≥ 80% task qua kiểm tra lần đầu; máy còn dư CPU và RAM |
| Bậc 3 | 8 | Như trên, thêm: Sonnet vẫn kịp kiểm tra và gộp trong ngày (không dồn hàng chờ quá 1 ngày) |

Xuống bậc ngay khi: có xung đột ghi đè, tỉ lệ trả về tăng, máy quá tải (VM thử chậm, build lỗi vì thiếu tài nguyên), hoặc Sonnet không theo kịp.

**Việc hợp chạy song song nhiều:** nghiên cứu source giai đoạn A theo từng thư mục; kiểm kê hoạt động D-01 theo từng nhóm script; công cụ quản trị C; bộ đo P-02; các mô-đun client không giao diện của Bot sau này.
**Việc luôn tuần tự:** mọi thứ cần VM thử hoặc LDPlayer (một khóa), các vùng ở 12.2.
Nếu việc cần VM thử dồn hàng chờ, Sonnet được tạo thêm một VM thử thứ hai (bản sao `JX-Test-36`, MAC mới, mạng Host-only như báo cáo 42) khi máy đủ RAM và đĩa. Không đụng Main VM.

### 13.3. Kiểm soát chi tiêu
- Task 0-10: chạy vài task mẫu, ghi chi phí thật mỗi task nếu Codex hoặc trang tài khoản cho xem được. Không có số liệu thì ghi "không có dữ liệu", không ước đoán.
- Đặt trần ngày ban đầu: tối đa khoảng 5% ngân sách mỗi ngày (khoảng 100 USD), Sonnet chỉnh theo số đo.
- Mỗi báo cáo ngày ghi: đã dùng hôm nay, tổng đã dùng, còn lại (khi có số liệu).
- Báo chủ dự án ngay khi đã dùng 50% và 80% tổng ngân sách.
- Review chéo bằng một phiên Codex khác (không phải phiên đã viết code) được tính là kiểm tra độc lập cho task L2. L3 Sonnet kiểm tra; L4–L5 Opus.
