# Đề xuất mở A-07 (gốc rễ crash gs001 tự dựng) — CHỈ ĐỀ XUẤT, CHƯA LÀM

Đợt #168, 18/11/2026. Không chạm VM, exe hay build ở đợt này.

## 1. Điều kiện mở
- **0-04 là gì:** cài Graphify và dựng đồ thị cho source server/client (`TASKS/BACKLOG.md:12`). Đồ thị đã dựng được (server 51.690 nút, client 20.871 nút); chỉ còn bước cài hook `graphify install`. A-07 chỉ chặn vì ghi `depends_on: [0-04]`, không vì Graphify. [TỰ QUYẾT] Coi 0-04 đủ điều kiện cho A-07.
- **A-07 thật sự còn chặn vì:** phần dựng Debug và chạy dưới debugger chưa làm. Báo cáo PARTIAL đã có (`REPORTS/A-07-goc-re-crash-gs001.md`) và 3 script ở `TOOLS/a07/` (đã kiểm cú pháp, chưa chạy).
- **Đã có từ phân tích tĩnh:** exe gốc là x64, linker 10.00; bản tự dựng x64, linker 14.44, bật thêm High Entropy ASLR. Bản tự dựng truyền con trỏ clone bằng r8 (64-bit), bản gốc dùng r8d (32-bit). Bốn nghi vấn có số dòng: bỏ qua HRESULT của QueryInterface (KSOServer.cpp:944), callback shell NULL (:4966), con trỏ qua unsigned int (:960), `long dir=_findfirst` (KSortScript.cpp:328). Chưa xác định dòng crash thật.

## 2. Các bước cần duyệt (mỗi bước làm riêng, có hoàn tác)
| # | Bước | Chạm gì | Hoàn tác | Rủi ro |
|---|---|---|---|---|
| 1 | Chạy `build-debug-a07.ps1` dựng Debug /MT /Od /Zi /RTC1 trên **bản copy** | Máy thật, chỉ ghi `D:\JX-build\a07` (script từ chối thư mục đã có). Không chạy exe. | Xóa `D:\JX-build\a07` | Thấp. Có thể gặp lỗi link `__imp___iob_func` (xem báo cáo 35). |
| 2 | Kiểm VM thử `JX-Test-36` (đang treo): mạng host-only/NAT, không bridged | VM thử, chưa bật | Không đổi gì | Thấp |
| 3 | Chụp snapshot VM (đang tạm dừng snapshot vì từng làm VBoxSVC crash) | VM thử | Xóa snapshot | Trung bình; cần chủ cho phép riêng |
| 4 | Copy exe + PDB mới vào gói thử có đủ DLL/config giả; lưu SHA-256, quét Defender | Trong VM thử | Xóa gói thử | Thấp (Q-19 cho phép chạy exe lạ trong VM thử sau SHA-256 + Defender) |
| 5 | `enable-wer-localdumps.ps1` (Admin trong VM) | Registry VM | Chạy lại với `-Disable` (khôi phục khóa cũ) | Thấp, trong VM |
| 6 | `debug-gs001.ps1` chạy gs001 dưới cdb, bắt first-chance AV, lưu dump rồi dừng | Trong VM thử | Tắt tiến trình, xóa dump | Thấp; dump có thể chứa dữ liệu giả, không xuất ra báo cáo |

Bước 3–6 cần duyệt rõ vì chạm VM/exe. Bước 1 và báo cáo kết quả có thể giao ngay.

## 3. Đề xuất
Làm bước 1 trước (không chạm VM); nếu dựng được, xin chủ duyệt các bước 2–6 gộp thành một đợt. Chủ có thể từ chối; khi đó A-07 dừng ở phân tích tĩnh. Ghi [CAN-CHU] cho bước 3 (snapshot) và 6.
