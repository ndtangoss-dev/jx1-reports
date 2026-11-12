# JX1 Inventory & Technical Research

Bộ tài liệu kiểm kê và nghiên cứu kỹ thuật cho source JX1 Cocos V3 (client Cocos2d-x, server C/C++ kiểu Windows, gói tài nguyên PAK).
Mục đích: để người đọc (kể cả ChatGPT) đọc trực tiếp, phân tích chéo và giải thích lại cho chủ dự án.

- **Ngày cập nhật:** 2026-11-12
- **Nguồn dữ liệu:** các báo cáo do Claude tạo từ cây thư mục làm việc của dự án. Giai đoạn 1 lưu ở thư mục kiểm kê của máy chủ dự án, giai đoạn nghiên cứu lưu ở thư mục nghiên cứu riêng. Bản trong repo này là bản sao nguyên văn.
- **Chỉ có báo cáo.** Repo này không chứa mã nguồn, asset, APK, log, dump, cơ sở dữ liệu hay dữ liệu người chơi.

## Hai giai đoạn

### Giai đoạn 1: kiểm kê metadata (thư mục `INVENTORY/`)
Quét đệ quy toàn bộ cây thư mục: đếm file, thư mục, dung lượng, loại file, các nhánh gốc, mã nguồn client/server, nhóm asset, và đối chiếu các literal tài nguyên trong mã client với file rời. **Chỉ đọc metadata**, không mở bên trong gói PAK.

| File | Nội dung |
|---|---|
| [INVENTORY_MASTER.md](INVENTORY/INVENTORY_MASTER.md) | Tổng quan: số file/thư mục, nhánh gốc, thống kê đuôi file, cây thư mục kèm dung lượng, tên trùng, bất thường (file lớn, ~2 MB) |
| [CLIENT_SOURCE_INVENTORY.md](INVENTORY/CLIENT_SOURCE_INVENTORY.md) | Công nghệ client, các mô-đun, điểm vào, cấu hình render, hệ nạp tài nguyên |
| [SERVER_SOURCE_INVENTORY.md](INVENTORY/SERVER_SOURCE_INVENTORY.md) | Hai cây mã server (gameserver, gateway), mô-đun, dự án Visual Studio, điểm vào |
| [ASSET_INVENTORY.md](INVENTORY/ASSET_INVENTORY.md) | Asset rời, gói PAK/APK/archive, băm SHA-256 chọn lọc |
| [ASSET_REFERENCE_COVERAGE.md](INVENTORY/ASSET_REFERENCE_COVERAGE.md) | Đối chiếu literal tài nguyên trong mã client với file rời (815 mục "UNRESOLVED") |
| [FILE_MANIFEST.csv](INVENTORY/FILE_MANIFEST.csv) | Danh sách từng file: đường dẫn, đuôi, dung lượng, thời gian, nhóm, SHA-256 (chỉ cho CDN PAK/APK). Tên nhạy cảm đã được ẩn trong nguồn |

### Giai đoạn nghiên cứu tiếp theo (thư mục `TECHNICAL_RESEARCH/`)
Đọc sâu kết quả kiểm kê và đối chiếu với mã thật: giải mã định dạng PAK từ mã nguồn client rồi kiểm lại trên 40 file PAK thật (chỉ đọc header và bảng chỉ mục, **không giải nén nội dung**), tính lại hash đường dẫn để đối chiếu 1.113 literal, so khớp bảng ID giao thức client/server, đánh giá kiến trúc và rủi ro.

| File | Nội dung |
|---|---|
| [TECHNICAL_ARCHITECTURE_REVIEW.md](TECHNICAL_RESEARCH/TECHNICAL_ARCHITECTURE_REVIEW.md) | Kiến trúc client và server, chất lượng nguồn, hiệu năng, điểm chưa rõ |
| [ASSET_FORMAT_RESEARCH.md](TECHNICAL_RESEARCH/ASSET_FORMAT_RESEARCH.md) | Định dạng PAK, hash đường dẫn, nén, SPR, kết quả đối chiếu literal ↔ chỉ mục PAK |
| [CLIENT_SERVER_DEPENDENCY_MAP.md](TECHNICAL_RESEARCH/CLIENT_SERVER_DEPENDENCY_MAP.md) | Sơ đồ thành phần, giao thức, so khớp ID giao thức, dữ liệu dùng chung |
| [INVENTORY_GAPS_AND_RISKS.md](TECHNICAL_RESEARCH/INVENTORY_GAPS_AND_RISKS.md) | Lỗ hổng của kiểm kê, rủi ro xếp ưu tiên |
| [PHASE_2_RESEARCH_PLAN.md](TECHNICAL_RESEARCH/PHASE_2_RESEARCH_PLAN.md) | Kế hoạch nghiên cứu tiếp theo (đề xuất, **chưa triển khai**) |

Đọc theo thứ tự gợi ý: `INVENTORY_GAPS_AND_RISKS` → `TECHNICAL_ARCHITECTURE_REVIEW` → `ASSET_FORMAT_RESEARCH` → `CLIENT_SERVER_DEPENDENCY_MAP` → `PHASE_2_RESEARCH_PLAN`.

## Nhãn mức chắc chắn
Mọi nhận định được gắn một trong bốn nhãn:

- **VERIFIED**: đã kiểm chứng trực tiếp (đọc mã, đọc dữ liệu, tính toán lại).
- **PROBABLE**: có cơ sở nhưng chưa xác minh đầy đủ.
- **UNKNOWN**: chưa đủ dữ liệu để kết luận.
- **BLOCKED**: chưa thể hoặc cố ý không tiếp cận/phân tích (ví dụ nội dung cấu hình nhạy cảm, bên trong gói PAK ở giai đoạn 1).

Lưu ý khi đọc: "UNRESOLVED" trong `ASSET_REFERENCE_COVERAGE.md` nghĩa là "chưa đối chiếu được với file rời", **không** phải "thiếu tài nguyên". Phần nghiên cứu giải thích lại con số này.

## Bảo mật
Không có mật khẩu, token, khóa riêng, khóa ký, giá trị cấu hình nhạy cảm hay dữ liệu tài khoản trong repo này. Một số tên file nhạy cảm đã được ẩn trong bản kiểm kê gốc (`[REDACTED-SENSITIVE-NAME]`) và một tên file dữ liệu tài khoản được ẩn thêm trong các báo cáo nghiên cứu. Dữ liệu thô và script phân tích của giai đoạn nghiên cứu **không** được đưa lên.
