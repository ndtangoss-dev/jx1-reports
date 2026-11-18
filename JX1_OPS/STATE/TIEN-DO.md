# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 22:53, đừng sửa tay)

ĐANG LÀM: W-01a, W-01b
KẾ TIẾP: 0-05, 0-08, B-05, CL-01, D-02, E-04
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
    W_01a["W-01a chạy"]
    W_01b["W-01b chạy"]
    W_01c["W-01c chờ gộp"]
    W_01d["W-01d chờ gộp"]
    0_05["0-05 chờ"]
    0_08["0-08 chờ"]
    B_05["B-05 chờ"]
    CL_01["CL-01 chờ"]
    D_02["D-02 chờ"]
    E_04["E-04 chờ"]
    E_06["E-06 chờ"]
    P_01["P-01 chờ"]
    P_03["P-03 chờ"]
    X_05["X-05 chờ"]
  end
```

Tổng: 133 việc, 2 đang làm (+0 chết, 2 chờ gộp), 10 chờ, 1 bị chặn, 118 xong.
