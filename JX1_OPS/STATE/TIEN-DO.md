# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 17:51, đừng sửa tay)

ĐANG LÀM: R-05b, R-06c
KẾ TIẾP: K-02
BỊ CHẶN: A-07, R-04b, R-05a, R-05c, R-05d, R-06a, R-07a, R-07b, T-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    R_05b["R-05b chạy"]
    R_06c["R-06c chạy"]
    A_07["A-07 chặn"]
    R_04b["R-04b chặn"]
    R_05a["R-05a chặn"]
    R_05c["R-05c chặn"]
    R_05d["R-05d chặn"]
    R_06a["R-06a chặn"]
    R_07a["R-07a chặn"]
    R_07b["R-07b chặn"]
    K_02["K-02 chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
  end
```

Tổng: 85 việc, 2 đang làm (+0 chết, 0 chờ gộp), 1 chờ, 9 bị chặn, 73 xong.
