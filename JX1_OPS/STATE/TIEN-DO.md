# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-19 05:07, đừng sửa tay)

ĐANG LÀM: HG-14, HG-16, XD-B05, XD-E04, XD-P03
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
    HG_14["HG-14 chạy"]
    HG_16["HG-16 chạy"]
    XD_B05["XD-B05 chạy"]
    XD_E04["XD-E04 chạy"]
    XD_P03["XD-P03 chạy"]
    XD_D02["XD-D02 chờ gộp"]
    XD_E06["XD-E06 chờ gộp"]
    XD_HG14["XD-HG14 chờ gộp"]
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

Tổng: 232 việc, 5 đang làm (+0 chết, 3 chờ gộp), 8 chờ, 1 bị chặn, 215 xong.
