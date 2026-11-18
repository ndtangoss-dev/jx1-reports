# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 13:23, đừng sửa tay)

ĐANG LÀM: R-05b
KẾ TIẾP: K-02, R-06a
BỊ CHẶN: A-07, R-04b

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    R_05b["R-05b chạy"]
    K_03a["K-03a chết"]
    K_03b["K-03b chết"]
    K_03c["K-03c chết"]
    K_03d["K-03d chết"]
    K_03e["K-03e chết"]
    R_03["R-03 chờ gộp"]
    R_05a["R-05a chờ gộp"]
    R_05c["R-05c chờ gộp"]
    R_05d["R-05d chờ gộp"]
    R_06c["R-06c chờ gộp"]
    R_07a["R-07a chờ gộp"]
    R_07b["R-07b chờ gộp"]
    A_07["A-07 chặn"]
    R_04b["R-04b chặn"]
    K_02["K-02 chờ"]
    R_06a["R-06a chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_03["T-03 chết"]
    T_04["T-04 chết"]
    T_02["T-02 chờ gộp"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    F_01["F-01 chết"]
  end
```

Tổng: 85 việc, 1 đang làm (+8 chết, 8 chờ gộp), 2 chờ, 2 bị chặn, 64 xong.
