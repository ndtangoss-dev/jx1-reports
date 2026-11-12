# TEAM_ROLES — Phòng ban và AI phụ trách

| Mã | Phòng ban | AI chính | Hỗ trợ/thực thi |
|---|---|---|---|
| CTRL | Điều phối tổng thể | ChatGPT cửa sổ hiện tại | — |
| ENG | Engineering | Claude Code | ChatGPT review |
| VIS | Visual Quality | ChatGPT Visual | Claude Code đọc source/đo theo task |
| GAME | Gameplay & Systems | ChatGPT Gameplay | Claude Code triển khai sau duyệt |
| SRV | Server & Backend | ChatGPT Server | Claude Code |
| QA | QA & Performance | ChatGPT QA | Claude Code; Sonnet QA theo trạng thái |
| AST | Asset & Content | ChatGPT Asset | Claude Code kiểm kê chỉ-đọc |
| REL | Build & Release | ChatGPT Release | Claude Code |
| SEC | Security & Reliability | ChatGPT Security | Claude Code |

Tên model có thể thay đổi; quy định vai trò mới là chuẩn. ChatGPT chuyên môn không tự có quyền sửa source. Claude Code là executor dùng chung, không nhận nhiều lệnh sửa chồng chéo. Không AI nào tự phê duyệt thay chủ dự án.

- ENG: client/server source, bug fix, tối ưu code, tích hợp.
- VIS: render, camera, animation, UI, effects, hình ảnh, chi phí hiển thị. Workspace hiện hữu: `JX1_VISUAL/`.
- GAME: combat, skill, quest, progression, economy, BOT behavior và cân bằng.
- SRV: server, protocol, database, network, persistence, BOT server-side, scaling.
- QA: test plan, bug reproduction, regression, profiling, benchmark.
- AST: inventory/coverage, PAK/SPR, map, texture, animation, audio, font, nội dung.
- REL: toolchain, build, APK, versioning, release checklist.
- SEC: secrets, auth, licensing, backup/restore, reliability, threat/risk.
