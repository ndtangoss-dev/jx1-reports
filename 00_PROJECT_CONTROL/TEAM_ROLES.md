# TEAM_ROLES — PHÒNG BAN VÀ AI PHỤ TRÁCH

| Mã | Phòng ban | AI phân tích/điều phối | Hỗ trợ/thực thi |
|---|---|---|---|
| CTRL | Điều phối tổng thể | ChatGPT cửa sổ hiện tại | — |
| ENG | Engineering | ChatGPT Engineering | Codex CLI thực thi sau duyệt |
| VIS | Visual Quality | ChatGPT Visual | Codex CLI đọc source/đo theo task |
| GAME | Gameplay & Systems | ChatGPT Gameplay | Codex CLI triển khai sau duyệt |
| SRV | Server & Backend | ChatGPT Server | Codex CLI |
| QA | QA & Performance | ChatGPT QA | Codex CLI; agent QA độc lập chỉ khi giao riêng |
| AST | Asset & Content | ChatGPT Asset | Codex CLI kiểm kê chỉ-đọc |
| REL | Build & Release | ChatGPT Release | Codex CLI |
| SEC | Security & Reliability | ChatGPT Security | Codex CLI |

**Executor mặc định cho JX1 hiện tại: Codex CLI được người dùng kích hoạt trực tiếp.** Dispatcher là legacy và không được dùng trong quy trình Direct CLI. Claude Code/agent khác chỉ tham gia khi được giao riêng cho QA, review hoặc nhiệm vụ phụ; không đồng thời sửa cùng file/nhánh với Codex.

ChatGPT chuyên môn không tự có quyền sửa source. Không AI nào tự phê duyệt thay chủ dự án.

- ENG: client/server source, bug fix, tối ưu code, tích hợp.
- VIS: render, camera, animation, UI, effects, hình ảnh, chi phí hiển thị. Workspace: `JX1_VISUAL/`.
- GAME: combat, skill, quest, progression, economy, BOT behavior và cân bằng.
- SRV: server, protocol, database, network, persistence, BOT server-side, scaling.
- QA: test plan, bug reproduction, regression, profiling, benchmark.
- AST: inventory/coverage, PAK/SPR, map, texture, animation, audio, font, nội dung.
- REL: toolchain, build, APK, versioning, release checklist.
- SEC: secrets, auth, licensing, backup/restore, reliability, threat/risk.

Quy trình chi tiết: [WORKFLOW_JX1.md](../WORKFLOW_JX1.md). Quy tắc Codex: [CODEX_DIRECT_CLI_RULES.md](../PROMPTS/CODEX_DIRECT_CLI_RULES.md).
