# HƯỚNG DẪN CHO CHỦ DỰ ÁN

Viết cho người không lập trình. Anh chỉ cần làm các bước dưới đây.

---

## 1. Xem và duyệt kế hoạch

Đọc `KE-HOACH-TONG-THE.md`, ít nhất Phần 0 (tóm tắt) và Phần 11 (quyết định).

Đã ghi các quyết định của anh: đưa source lên GitHub riêng tư; bỏ hẳn AMOLX; Codex giữ model Sol Max, dùng nhiều worker. D3–D6: nếu đồng ý mặc định thì không cần nói gì.

---

## 2. Bàn giao cho Sonnet (làm một lần)

Trên máy Windows có thư mục `C:\Jx1CocoV3`:

1. Mở **Claude Code** trong thư mục `C:\Jx1CocoV3` (như anh vẫn mở).
2. Gõ `/model` và chọn **Sonnet**.
3. Dán nguyên đoạn dưới đây rồi Enter:

```
Bạn là Project Manager của dự án JX1, toàn quyền điều hành theo kế hoạch đã duyệt.
Kế hoạch và quy trình ở repository ndtangoss-dev/jx1-reports, nhánh jx1-ops, thư mục JX1_OPS.
Lấy nhánh đó về máy, đọc JX1_OPS/README.md và làm theo thứ tự đọc của PM.

Tôi đã duyệt KE-HOACH-TONG-THE.md. Các quyết định đã ghi trong STATE/QUYET-DINH.md.
D3–D6: dùng mặc định. Ghi thành quyết định rồi bắt đầu giai đoạn 0 trong TASKS/BACKLOG.md.
Codex giữ nguyên model và cấu hình hiện tại.
Làm tự động, không hỏi tôi việc thông thường. Báo tôi một lần mỗi ngày.
```

4. Sonnet sẽ tự cài lệnh `/tiep-tuc`, `/ket-thuc-ca`, `/bao-cao` vào dự án trong ngày đầu (task 0-01). Từ đó trở đi anh dùng ba lệnh này.

Nếu Sonnet hỏi xin quyền chạy lệnh trong ngày đầu: bấm cho phép. Sau task 0-01, các lệnh thông thường sẽ không hỏi nữa.

---

## 3. Mỗi ngày

| Anh muốn | Gõ |
|---|---|
| Bắt đầu làm việc (sau khi mở máy) | `/tiep-tuc` |
| Xem nhanh tình hình, không dừng việc | `/bao-cao` |
| Nghỉ, tắt máy | `/ket-thuc-ca` → chờ dòng **"Đã lưu. Có thể tắt máy."** rồi mới tắt |
| Để máy chạy qua đêm | Không gõ gì. Sonnet tự làm tiếp và viết báo cáo lúc 22:00 |

Báo cáo ngày nằm trên GitHub: `JX1_OPS/REPORTS/daily/`. Anh xem được trên điện thoại.

---

## 4. Tình huống đặc biệt

| Tình huống | Làm gì |
|---|---|
| Mất điện, máy tắt đột ngột, Claude Code bị đóng | Mở lại, gõ `/tiep-tuc`. Sonnet tự phục hồi từ lần lưu gần nhất (không quá 45 phút việc) |
| Hết hạn mức tài khoản Claude, chuyển sang tài khoản cũ | Đăng xuất, đăng nhập tài khoản cũ trong Claude Code, mở thư mục `C:\Jx1CocoV3`, gõ `/model` chọn Sonnet, gõ `/tiep-tuc` |
| Không còn Sonnet, phải dùng Opus hoặc model khác | Chọn model đó, gõ `/tiep-tuc`. Model đó sẽ làm PM tạm quyền |
| Chỉ còn Codex | Mở Codex trong `C:\Jx1CocoV3`, dán: `Đọc JX1_OPS/README.md trên nhánh jx1-ops của ndtangoss-dev/jx1-reports và làm theo mục /tiep-tuc trong QUY-TAC-VAN-HANH.md. Bạn là PM tạm quyền.` |
| Lệnh `/tiep-tuc` không hiện ra | Dán đoạn bàn giao ở mục 2 thay cho lệnh |
| Sonnet báo cần anh quyết | Trả lời ngắn theo lựa chọn Sonnet đưa ra |

---

## 5. Sonnet sẽ hỏi anh khi nào

Chỉ khi:
- Cần đụng **Main VM** `JX-Server-D` hoặc dữ liệu thật.
- Cần **xóa** thứ không lấy lại được.
- Cần **tiêu tiền** hoặc đưa dữ liệu ra dịch vụ ngoài.
- Cần đổi mật khẩu, mạng, tường lửa của máy thật.
- Một **quyết định gameplay** chưa chốt (ví dụ: hoạt động nào cho người thật thấy nhau, bao nhiêu người).
- Mốc quan trọng cần anh **thử trên điện thoại**.
- Ngân sách Codex đã dùng tới **50%** và **80%**.

Mọi việc khác Sonnet tự làm.

---

## 6. Điều nên biết

- Khi máy tắt, những việc cần VM thử hoặc LDPlayer sẽ dừng. Đây là giới hạn của việc chạy trên máy cá nhân, không phải lỗi.
- Vì source sẽ nằm trên GitHub riêng tư, có thể giao Claude trên web hoặc điện thoại làm việc đọc source khi máy tắt. Không bắt buộc.
- Nếu thấy Sonnet làm lẫn lộn (giao việc lặp, quên việc đang làm), gõ `/ket-thuc-ca`, rồi `/clear`, rồi `/tiep-tuc`. Phiên mới đọc lại mọi thứ từ GitHub.
- Kế hoạch đánh giá việc chuyển server là khả thi, nhưng thời gian thật chỉ biết sau giai đoạn A. Sonnet sẽ báo con số thật, không đoán.

## Cấp quyền Admin tự chủ một lần (Q-28)
Mở PowerShell bằng *Run as administrator*, chạy:

```powershell
powershell -ExecutionPolicy Bypass -File D:\jx1-ops-wt\JX1_OPS\TOOLS\setup_quyen_admin.ps1
```

1. Script tạo thư mục `C:\ProgramData\JX1_ADMIN` (chỉ Admin sửa được) và 4 task SYSTEM cho đúng 4 việc cố định: diệt VBoxHeadless của `JX-Test-36` (từ chối `JX-Server-D`), luật tường lửa `JX1-AUTO-*`, TrustedHosts, bật dịch vụ.
2. Mỗi việc chỉ nhận cổng, IP, dịch vụ nằm trong `config\allowed.json` (anh sửa file này bằng Admin, thêm IP điện thoại Tailscale vào `ips` nếu cần); mọi lần chạy ghi `log\admin.log`.
3. Gỡ bỏ: `powershell -ExecutionPolicy Bypass -File ...\setup_quyen_admin.ps1 -Remove` (xóa 4 task và các luật `JX1-AUTO-*`).
