# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-20 12:33, đừng sửa tay)

ĐANG LÀM: KT-01, KT-02, KT-03A, KT-03B, KT-03C, KT-03D, KT-04, KT-06
KẾ TIẾP: 0-08, B-05, D-02, E-04, E-06, KT-05
BỊ CHẶN: T-04, TS-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    KT_01["KT-01 chạy"]
    KT_02["KT-02 chạy"]
    KT_03A["KT-03A chạy"]
    KT_03B["KT-03B chạy"]
    KT_03C["KT-03C chạy"]
    KT_03D["KT-03D chạy"]
    KT_04["KT-04 chạy"]
    KT_06["KT-06 chạy"]
    TS_04["TS-04 chặn"]
    0_08["0-08 chờ"]
    B_05["B-05 chờ"]
    D_02["D-02 chờ"]
    E_04["E-04 chờ"]
    E_06["E-06 chờ"]
    KT_05["KT-05 chờ"]
    P_01["P-01 chờ"]
    P_03["P-03 chờ"]
    X_05["X-05 chờ"]
  end
  KT_01 --> KT_05
```

Tổng: 274 việc, 8 đang làm (+0 chết, 0 chờ gộp), 9 chờ, 2 bị chặn, 255 xong.
