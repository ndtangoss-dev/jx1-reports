# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 16:39, đừng sửa tay)

ĐANG LÀM: K-03c
KẾ TIẾP: K-02, R-06a
BỊ CHẶN: A-07, R-04b, R-05a, T-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    K_03c["K-03c chạy"]
    R_05b["R-05b chờ gộp"]
    R_05c["R-05c chờ gộp"]
    R_05d["R-05d chờ gộp"]
    R_06c["R-06c chờ gộp"]
    R_07a["R-07a chờ gộp"]
    R_07b["R-07b chờ gộp"]
    A_07["A-07 chặn"]
    R_04b["R-04b chặn"]
    R_05a["R-05a chặn"]
    K_02["K-02 chờ"]
    R_06a["R-06a chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
  end
```

Tổng: 85 việc, 1 đang làm (+0 chết, 6 chờ gộp), 2 chờ, 4 bị chặn, 72 xong.
