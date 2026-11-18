# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 09:54, đừng sửa tay)

ĐANG LÀM: R-03, R-04b, R-05a, R-05b, R-05c
KẾ TIẾP: F-01, K-02, K-03, R-02, R-04, R-05d
BỊ CHẶN: A-07

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    R_03["R-03 chạy"]
    R_04b["R-04b chạy"]
    R_05a["R-05a chạy"]
    R_05b["R-05b chạy"]
    R_05c["R-05c chạy"]
    A_07["A-07 chặn"]
    K_02["K-02 chờ"]
    K_03["K-03 chờ"]
    R_02["R-02 chờ"]
    R_04["R-04 chờ"]
    R_05d["R-05d chờ"]
    R_06a["R-06a chờ"]
    R_06c["R-06c chờ"]
    R_07a["R-07a chờ"]
    R_07b["R-07b chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_02["T-02 chờ"]
    T_03["T-03 chờ"]
    T_04["T-04 chờ"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    F_01["F-01 chờ"]
  end
  K_03 --> K_02
```

Tổng: 79 việc, 5 đang làm (+0 chết, 0 chờ gộp), 13 chờ, 1 bị chặn, 60 xong.
