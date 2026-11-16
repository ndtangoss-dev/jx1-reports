# QUY TẮC VẬN HÀNH ĐỘI AI JX1

Phiên bản 1 – 2026-11-16 – Opus soạn. Áp dụng khi chủ dự án phê duyệt `KE-HOACH-TONG-THE.md`.

Bộ quy tắc này **thay thế** `AGENTS.md`, `WORKFLOW_JX1.md`, `PROMPTS/CODEX_DIRECT_CLI_RULES.md`, `PROMPTS/00_CODEX_START_HERE.md`, `00_PROJECT_CONTROL/*` trên nhánh `main`, và các quy tắc vận hành của `FABLE_HANDOVER_v0.3/`. Rào chắn an toàn của bộ cũ được giữ ở mục 3.

Mục tiêu số một: **hoàn thành dự án tự động, nhanh.** Không hỏi chủ dự án việc thông thường. Không báo cáo thừa.

---

## 1. Ai làm gì

- **Sonnet (PM):** phiên Claude Code chính trên máy Windows `C:\Jx1CocoV3`. Đầu mối duy nhất. Tự chia việc, khởi chạy worker, kiểm tra, sửa, merge, quản lý môi trường thử, lưu trạng thái, báo cáo.
- **Opus:** Sonnet gọi (agent con chạy model Opus, hoặc phiên `claude --model opus`) cho việc L4–L5 và lỗi khó. Opus không điều hành.
- **Codex CLI:** worker chính. Sonnet gọi `codex exec` chạy nền trong worktree của task, prompt chỉ trỏ tới file task. Không đổi cấu hình tài khoản Codex của chủ dự án; được chọn model cho từng lệnh nếu cần.
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
Song song tối đa 3 worker lúc đầu; Sonnet tăng giảm theo số đo. Một VM thử và một LDPlayer chỉ do một agent điều khiển tại một thời điểm.

Kích thước một task: 15–60 phút làm việc, có kết quả kiểm chứng được. Việc lớn hơn thì chia. (Thay quy tắc 5–10 phút cũ: quy tắc đó sinh ra do chủ dự án phải bấm từng lượt.)

## 3. Quyền hạn

**Sonnet có toàn quyền**, không hỏi, với mọi việc trên máy phát triển, repository, VM thử `JX-Test-36`, LDPlayer: đọc, sửa, build, test, cài công cụ, cài APK lên LDPlayer, khởi động lại server và dịch vụ trong VM thử, tạo tài khoản thử và tài khoản bot trong DB thử, tạo và xóa branch/worktree, merge, sửa cấu hình phát triển, dọn file tạm.

**Vùng Đỏ – chỉ làm khi chủ dự án nói rõ:**
1. Mọi thao tác trên Main VM `JX-Server-D` và dữ liệu thật của nó.
2. Xóa dữ liệu không khôi phục được (kể cả VM, snapshot, bản sao lưu).
3. Đưa source hoặc dữ liệu lên dịch vụ ngoài, trừ repository riêng tư đã được duyệt (D1).
4. Phát sinh chi phí tiền.
5. Đổi mật khẩu, quyền tài khoản thật, cấu hình mạng hay tường lửa của máy thật.

**Giữ từ bộ cũ (đã có lý do thật):**
- Không bao giờ chạy `JxStudio.exe`, `str_tool.exe`, `Autoupdate.exe`. Exe trong gói game chỉ chạy trong VM.
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
