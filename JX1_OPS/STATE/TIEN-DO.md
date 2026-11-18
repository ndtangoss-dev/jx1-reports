# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-19 00:21, đừng sửa tay)

ĐANG LÀM: HG-02, HG-03, HG-05, KC-01, KC-02, SO-03, SO-04, SO-05, SO-06, TK-01
KẾ TIẾP: 0-08, B-05, D-02, E-04, E-06, P-01
BỊ CHẶN: T-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    HG_02["HG-02 chạy"]
    HG_03["HG-03 chạy"]
    HG_05["HG-05 chạy"]
    KC_01["KC-01 chạy"]
    KC_02["KC-02 chạy"]
    SO_03["SO-03 chạy"]
    SO_04["SO-04 chạy"]
    SO_05["SO-05 chạy"]
    SO_06["SO-06 chạy"]
    TK_01["TK-01 chạy"]
    HG_01["HG-01 chờ gộp"]
    HG_04["HG-04 chờ gộp"]
    SO_01["SO-01 chờ gộp"]
    SO_02["SO-02 chờ gộp"]
    0_08["0-08 chờ"]
    B_05["B-05 chờ"]
    D_02["D-02 chờ"]
    E_04["E-04 chờ"]
    E_06["E-06 chờ"]
    P_01["P-01 chờ"]
    P_03["P-03 chờ"]
    X_05["X-05 chờ"]
  end
```

Tổng: 150 việc, 10 đang làm (+0 chết, 4 chờ gộp), 8 chờ, 1 bị chặn, 127 xong.
