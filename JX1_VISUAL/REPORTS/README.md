# REPORTS — Báo cáo kết quả của Claude

Đặt tên: `V001_ten-bao-cao.md`, mã tăng tuần tự, không tái sử dụng. Cấu trúc báo cáo xem [README gốc](../README.md).

| Mã | Báo cáo | Ngày | Nhiệm vụ | Ghi chú |
|---|---|---|---|---|
| V001 | [V001_asset-format-research.md](V001_asset-format-research.md) | 2026-11-12 | (khởi đầu, chưa có nhiệm vụ Visual) | Định dạng PAK/SPR, hash đường dẫn, đối chiếu 1.113 literal ↔ chỉ mục PAK |
| V002 | [V002_full-technical-feasibility-audit.md](V002_full-technical-feasibility-audit.md) | 2026-11-12 | (chỉ thị trực tiếp của người dùng, không qua TASKS/) | Thẩm định toàn diện: hệ animation và số khung, cơ chế giới hạn khung, làm chủ asset, client/server riêng, 4 phương án, khuyến nghị |

**Về V001:** bản sao nguyên văn, không hiệu chỉnh (đã rà: chỉ nêu *tên* hai khóa `accinfo`/`accpint`, không có giá trị). Báo cáo trích dẫn các file `data/*.csv` và `scripts/*.py` ở máy nghiên cứu; các file đó **không** được đưa lên. Các tham chiếu tới báo cáo khác (ví dụ `INVENTORY_GAPS_AND_RISKS.md`) nằm trong [JX1_INVENTORY_RESEARCH](../../JX1_INVENTORY_RESEARCH/README.md).

Chưa đưa vào đây (không thuộc Visual): `TECHNICAL_ARCHITECTURE_REVIEW`, `CLIENT_SERVER_DEPENDENCY_MAP`, `INVENTORY_GAPS_AND_RISKS`, `PHASE_2_RESEARCH_PLAN` và 6 báo cáo kiểm kê.

**Về V002:** bản sao nguyên văn, không hiệu chỉnh (đã rà: không có mật khẩu, token, IP, giá trị cấu hình nhạy cảm). Phạm vi rộng hơn Visual (gồm cả client/server), đặt ở đây theo yêu cầu của người dùng. Báo cáo trích dẫn script và CSV ở máy nghiên cứu cùng các báo cáo nội bộ của dự án (`docs-analysis/reports`); các file đó **không** được đưa lên.
