# ENVIRONMENT AND TOOLS

Phiên bản v0.3 – khung do Fable soạn. **Nội dung do Opus điền và giữ cho đúng**; Fable chưa truy cập máy nên mọi ô dưới đây còn trống.

Mục đích: AI kế nhiệm đọc file này là dùng được máy và công cụ hiện có mà không hỏi ai. Viết theo kiểu "làm X thì chạy lệnh Y ở thư mục Z". Cập nhật ngay khi cài, gỡ hoặc đổi cấu hình một công cụ. Không ghi mật khẩu hay token vào đây.

## 1. Máy và thư mục
| Thứ | Ở đâu | Ghi chú |
|---|---|---|
| Thư mục dự án | `C:\Jx1CocoV3` | |
| Repository GitHub | | |
| Source JX1 gốc (chỉ đọc) | | |
| Các worktree | | |

## 2. Thứ nằm ngoài Git
Git không chứa mọi thứ. Liệt kê để không ai tưởng là đã mất hoặc đã được sao lưu.
| Thứ | Ở đâu | Có sao lưu không | Là production? |
|---|---|---|---|
| Server clone / VM | | | |
| Database | | | |
| CDN | | | |
| Tailscale | | | |
| Tài nguyên dung lượng lớn | | | |

## 3. Công cụ AI
| Công cụ | Phiên bản | Dùng để | Cách khởi động | Cấu hình nằm ở |
|---|---|---|---|---|
| Claude Code | | | | |
| Codex CLI | | | | |
| Orchestrator (nếu dùng) | | | | |
| Plugin khác | | | | |

Cấu hình cần cho dự án phải nằm trong repository (cấp dự án), không nằm trong thiết lập riêng của một tài khoản. Nếu buộc phải nằm ngoài, ghi ở đây cách dựng lại.

## 4. Lệnh thường dùng
| Việc | Lệnh | Chạy ở |
|---|---|---|
| Build client | | |
| Build server | | |
| Chạy toàn bộ test | | |
| Khởi động server thử nghiệm | | |
| Mở game để xem | | |
| Sinh lại bảng trạng thái task | | |
| Gửi báo cáo cuối ngày | | |

## 5. Khi đổi tài khoản hoặc nhà cung cấp
| Bước | Ai làm |
|---|---|
| Đăng nhập tài khoản mới vào công cụ (Claude Code, Codex…) | Chủ dự án (việc duy nhất cần họ làm) |
| Kiểm tra model nào dùng được, cập nhật `agents/registry/` | AI mới |
| Kiểm tra từng công cụ ở mục 3 còn chạy | AI mới |
| Theo `START-HERE.md` | AI mới |

## 6. Bẫy đã gặp
*(Lỗi môi trường đã mất thời gian và cách xử lý.)*
