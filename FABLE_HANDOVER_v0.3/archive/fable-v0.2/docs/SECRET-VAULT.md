# SECRET VAULT – KHO BÍ MẬT MỘT FILE TRÊN MÁY LOCAL

Phiên bản v0.2 – 2026-11-16 – Fable soạn thiết kế. Opus lựa chọn công cụ cuối cùng, triển khai và kiểm thử.

> Đây là bản thiết kế. Fable chưa thử công cụ nào trên máy của chủ dự án. Tên công cụ và lệnh cụ thể Opus xác minh khi triển khai.

---

## 1. Dành cho chủ dự án (đọc phần này là đủ)

- Mọi mật khẩu, token, khóa của dự án nằm trong **một file đã mã hóa** trên máy anh. File này không bao giờ lên GitHub, không vào file ZIP, không xuất hiện trong báo cáo.
- Chìa khóa mở file do Windows giữ, gắn với tài khoản đăng nhập Windows của anh. Anh không phải gõ mật khẩu mỗi lần AI làm việc.
- Anh giữ **một mã khôi phục** (in ra giấy hoặc lưu trong trình quản lý mật khẩu cá nhân, không lưu trên máy này). Chỉ dùng khi đổi máy, cài lại Windows hoặc quên mật khẩu.
- Muốn thêm hoặc đổi một mật khẩu: bảo Opus "cập nhật bí mật X". Opus mở cửa sổ để anh tự nhập. Anh không dán mật khẩu vào khung chat.
- Nếu nghi bị lộ: bảo Opus "thu hồi X". Opus hướng dẫn từng bước đổi ở nơi cấp, rồi cập nhật kho.

## 2. Yêu cầu

| ID | Yêu cầu |
|---|---|
| SV-01 | Một file dữ liệu bí mật duy nhất trên máy local. |
| SV-02 | Không vào Git, ZIP bàn giao, báo cáo. |
| SV-03 | Không ghi mật khẩu, token, API key, credential, khóa vào task, log, commit. |
| SV-04 | Worker không đọc toàn bộ kho. Chỉ nhận đúng phần cần cho việc đang làm. |
| SV-05 | Quyền truy cập file bị giới hạn. |
| SV-06 | Sao lưu và khôi phục an toàn. |
| SV-07 | Mã hóa phù hợp với Windows. |
| SV-08 | Có hướng dẫn thay đổi và thu hồi credential. |
| SV-09 | Không lưu mật khẩu giải mã cạnh file dữ liệu. |
| SV-10 | Chủ dự án không cần hiểu kỹ thuật mã hóa. |

## 3. Thiết kế

```
Chủ dự án ──(mã khôi phục, giữ ngoài máy)
                 │
Windows Credential Manager ── giữ khóa chính, bảo vệ bằng tài khoản Windows
                 │
        ┌────────▼─────────┐
        │  File vault mã hóa │  ngoài repo, ví dụ %USERPROFILE%\.jx1-vault\vault.<định dạng>
        └────────┬─────────┘
                 │ chỉ công cụ "secret broker" được mở
        ┌────────▼─────────┐
        │   Secret broker    │  script nhỏ: nhận tên bí mật + phạm vi, cấp đúng giá trị cho đúng tiến trình
        └────────┬─────────┘
     ┌───────────┼────────────┐
  build/deploy   test DB     công cụ admin   ← nhận bí mật qua biến môi trường của tiến trình, không qua chat
```

### 3.1. Vị trí và quyền
- File nằm **ngoài** thư mục repo, để không thể vô tình commit. Thêm quy tắc `.gitignore` và hook chặn commit làm lớp thứ hai.
- Quyền thư mục: chỉ tài khoản Windows của chủ dự án.

### 3.2. Mã hóa và khóa
- File được mã hóa bằng một khóa chính ngẫu nhiên.
- Khóa chính lưu trong Windows Credential Manager, không nằm trong thư mục chứa file (SV-09).
- Mã khôi phục là bản sao của khóa chính, chủ dự án giữ ngoài máy.

### 3.3. Cấu trúc bên trong: một file, nhiều phạm vi
Mỗi bí mật có tên, phạm vi và ghi chú, ví dụ:

| Tên | Phạm vi | Ai được dùng |
|---|---|---|
| `db/dev/password` | dev | Worker server, database, test |
| `db/prod/password` | prod | Chỉ Opus, sau khi chủ dự án đồng ý |
| `github/token` | git | Opus, công cụ CI |
| `tailscale/authkey` | infra | Chỉ Opus |
| `ai/codex/key` | ai | Trình khởi chạy worker |

Task ghi **tên** bí mật nó cần (ví dụ `secrets: [db/dev/password]`), không bao giờ ghi giá trị.

### 3.4. Secret broker
- Một script duy nhất được phép mở vault.
- Cách dùng chính: "chạy lệnh này với các bí mật sau": broker đưa giá trị vào biến môi trường của tiến trình con rồi thoát. Giá trị không in ra màn hình, không vào log.
- Broker ghi nhật ký: thời điểm, agent, tên bí mật (không ghi giá trị).
- Broker từ chối tên nằm ngoài phạm vi của task.
- **AI làm việc với tên, không cần thấy giá trị.** Nội dung AI đọc được đều được gửi tới nhà cung cấp model, nên giá trị bí mật không nên đi vào ngữ cảnh của bất kỳ AI nào, kể cả Opus, trừ khi không còn cách khác.

### 3.5. Sao lưu và khôi phục
- Sao lưu chính file đã mã hóa (an toàn vì đã mã hóa) sang một vị trí thứ hai do chủ dự án chọn, tự động sau mỗi lần thay đổi.
- Khôi phục = file sao lưu + mã khôi phục.
- Opus phải **thử khôi phục thật một lần** ngay sau khi dựng, trước khi coi vault là dùng được.

### 3.6. Thay đổi và thu hồi
Opus viết hướng dẫn ngắn `docs/11-SECURITY-RULES.md` cho từng loại credential: đổi ở đâu, cập nhật vault thế nào, kiểm tra lại ra sao. Khi nghi lộ: thu hồi ở nơi cấp trước, cập nhật vault sau, rồi rà Git và log xem giá trị cũ có xuất hiện không. Báo chủ dự án ngay (sự cố nghiêm trọng).

## 4. Phương án công cụ để Opus đánh giá

| Phương án | Mô tả | Điểm mạnh | Điểm yếu |
|---|---|---|---|
| A. File KeePass (KDBX) | Một file `.kdbx`, khóa chính trong Credential Manager, đọc bằng công cụ dòng lệnh | Định dạng phổ biến, có nhóm/phạm vi, chủ dự án mở được bằng giao diện khi cần, sao lưu chỉ là copy file | Cần cài thêm công cụ |
| B. PowerShell SecretManagement + SecretStore | Kho bí mật của Microsoft cho PowerShell | Sẵn cho Windows, ít phụ thuộc | Ít tiện phân phạm vi, khó dùng từ công cụ không phải PowerShell |
| C. File mã hóa bằng DPAPI | JSON mã hóa bằng cơ chế bảo vệ dữ liệu của Windows | Không cần cài gì, không cần quản lý khóa | Gắn chặt với tài khoản và máy: mất Windows là mất dữ liệu nếu không có bản xuất khôi phục riêng |
| D. SOPS + age | File YAML mã hóa từng giá trị | Tốt cho tự động hóa | Thêm hai công cụ, kém thân thiện với chủ dự án |

Đề xuất sơ bộ của Fable: **A**, vì đáp ứng đúng mô tả "một file mã hóa mở bằng Windows Credential Manager" và khôi phục đơn giản. Opus xác minh trên máy thật rồi ghi ADR.

## 5. Giới hạn cần biết

Nếu mọi AI đều chạy dưới **cùng một tài khoản Windows** với quyền chạy lệnh tùy ý, thì broker chỉ là kỷ luật quy trình: về kỹ thuật, một worker vẫn có thể tự gọi Credential Manager và mở cả kho. Yêu cầu SV-04 chỉ được bảo đảm thật khi có ranh giới của hệ điều hành, ví dụ worker chạy dưới một tài khoản Windows riêng ít quyền, hoặc trong container/VM, còn broker chạy dưới tài khoản chủ.

Opus chọn mức phù hợp và nói rõ cho chủ dự án đang ở mức nào:
- **Mức 1 – kỷ luật:** cùng tài khoản, broker + hook chặn + nhật ký. Dựng nhanh.
- **Mức 2 – cách ly:** worker ở tài khoản hoặc môi trường riêng. Nên đạt trước khi vault chứa bất kỳ bí mật production nào.

Ngoài ra: bí mật production và bí mật dev luôn là hai giá trị khác nhau, để lộ dev không ảnh hưởng production.

## 6. Tiêu chí nghiệm thu khi Opus triển khai

- [ ] Chỉ có một file vault; tìm trong repo và lịch sử Git không thấy bí mật nào.
- [ ] Hook chặn được commit có chứa chuỗi giống bí mật (thử bằng giá trị giả).
- [ ] Một task dev không lấy được bí mật phạm vi prod qua broker.
- [ ] Log của một lần build/deploy mẫu không chứa giá trị bí mật.
- [ ] Khôi phục từ bản sao lưu + mã khôi phục thành công trên thư mục sạch.
- [ ] Chủ dự án thêm được một bí mật mới theo hướng dẫn mà không cần hỗ trợ kỹ thuật.
- [ ] ZIP bàn giao và báo cáo ngày được quét tự động trước khi gửi.
