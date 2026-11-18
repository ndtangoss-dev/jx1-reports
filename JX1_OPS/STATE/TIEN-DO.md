# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 20:39, đừng sửa tay)

ĐANG LÀM: K-02, K-02b, K-02c, K-02f, R-05a
KẾ TIẾP: 0-05, 0-08, B-05, D-02, E-04, E-06
BỊ CHẶN: CL-01, T-04, X-05

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    K_02["K-02 chạy"]
    K_02b["K-02b chạy"]
    K_02c["K-02c chạy"]
    K_02f["K-02f chạy"]
    R_05a["R-05a chạy"]
    K_02e["K-02e chờ gộp"]
    R_04b["R-04b chờ gộp"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    CL_01["CL-01 chặn"]
    X_05["X-05 chặn"]
    0_05["0-05 chờ"]
    0_08["0-08 chờ"]
    B_05["B-05 chờ"]
    D_02["D-02 chờ"]
    E_04["E-04 chờ"]
    E_06["E-06 chờ"]
    P_01["P-01 chờ"]
    P_03["P-03 chờ"]
  end
```

Tổng: 129 việc, 5 đang làm (+0 chết, 2 chờ gộp), 8 chờ, 3 bị chặn, 111 xong.
