# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-19 02:29, đừng sửa tay)

ĐANG LÀM: HG-14, HG-16, KC-01b, SO-17, SO-19, SO-23, T-01
KẾ TIẾP: 0-08, B-05, D-02, E-04, E-06, P-01
BỊ CHẶN: T-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_01["T-01 chạy"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    HG_14["HG-14 chạy"]
    HG_16["HG-16 chạy"]
    KC_01b["KC-01b chạy"]
    SO_17["SO-17 chạy"]
    SO_19["SO-19 chạy"]
    SO_23["SO-23 chạy"]
    HG_15["HG-15 chờ gộp"]
    SO_16["SO-16 chờ gộp"]
    SO_20["SO-20 chờ gộp"]
    SO_21["SO-21 chờ gộp"]
    SO_22["SO-22 chờ gộp"]
    SO_24["SO-24 chờ gộp"]
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

Tổng: 190 việc, 7 đang làm (+0 chết, 6 chờ gộp), 8 chờ, 1 bị chặn, 168 xong.
