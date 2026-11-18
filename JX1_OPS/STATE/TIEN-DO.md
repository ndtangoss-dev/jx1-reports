# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 18:22, đừng sửa tay)

ĐANG LÀM: N-01, N-02, N-03, N-04, R-05b, R-05c, R-05d, R-06c, R-07a, R-07b
KẾ TIẾP: K-02, N-05, N-06
BỊ CHẶN: A-07, R-04b, R-05a, T-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    R_05b["R-05b chạy"]
    R_05c["R-05c chạy"]
    R_05d["R-05d chạy"]
    R_06c["R-06c chạy"]
    R_07a["R-07a chạy"]
    R_07b["R-07b chạy"]
    R_06a["R-06a chờ gộp"]
    A_07["A-07 chặn"]
    R_04b["R-04b chặn"]
    R_05a["R-05a chặn"]
    K_02["K-02 chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    N_01["N-01 chạy"]
    N_02["N-02 chạy"]
    N_03["N-03 chạy"]
    N_04["N-04 chạy"]
    T_04["T-04 chặn"]
    N_05["N-05 chờ"]
    N_06["N-06 chờ"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
  end
```

Tổng: 91 việc, 10 đang làm (+0 chết, 1 chờ gộp), 3 chờ, 4 bị chặn, 73 xong.
