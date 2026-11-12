# PATCH_NOTES

Repo này không chứa mã nguồn. Bảng dưới chỉ ghi tên và mục đích của các patch nằm ở máy phát triển (`docs-analysis/patches/`, không public).

| Patch (chỉ tên) | Mục đích | Báo cáo |
|---|---|---|
| `31-client-tick-smooth.diff` + test | Làm mượt nhịp xử lý client | [CLIENT/31](../CLIENT/31-toi-uu-nhip-xu-ly-client.md) |
| `33-client-skill-guard.diff` + test | Chặn lỗi kỹ năng/sát thương | [FIX_HISTORY/33](../FIX_HISTORY/33-fix-skill-damage-and-smoothness.md) |
| `34-client-missile-interp.diff` + test | Nội suy đạn bay | [FIX_HISTORY/34](../FIX_HISTORY/34-toi-uu-toan-dien-do-muot.md) |
| `a2-cmdlane/a2-cmdlane.diff` | A2 Command Lane: làn lệnh di chuyển riêng phía server | [39](39-a2-command-lane.md) |
| `fix-findfirst/` | Sửa `_findfirst` dùng `intptr_t` (crash x64); kèm bộ gỡ lỗi nhỏ | [fix-findfirst-README](fix-findfirst-README.md), [FIX_HISTORY/44](../FIX_HISTORY/44-dieu-tra-a2-thoat-som.md) |
| Fix35/Fix36 (sửa trực tiếp trên bản sao mã) | `FindRegion`, format `KPlayer`, dọn texture theo ngưỡng, 7 struct gói, `uintptr_t`, `LogicFps`/nửa bước 36Hz | [FIX_HISTORY/45](../FIX_HISTORY/45-fix36-giat-ban-do-va-36hz.md) |
