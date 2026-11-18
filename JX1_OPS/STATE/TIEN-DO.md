# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 10:49, đừng sửa tay)

ĐANG LÀM: R-05c
KẾ TIẾP: K-02
BỊ CHẶN: A-07

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    R_05c["R-05c chạy"]
    K_03a["K-03a chết"]
    K_03b["K-03b chết"]
    K_03c["K-03c chết"]
    K_03d["K-03d chết"]
    K_03e["K-03e chết"]
    R_02["R-02 chết"]
    R_03["R-03 chết"]
    R_04["R-04 chết"]
    R_04b["R-04b chết"]
    R_05a["R-05a chết"]
    R_05b["R-05b chết"]
    R_05d["R-05d chết"]
    R_06c["R-06c chết"]
    R_07a["R-07a chết"]
    R_07b["R-07b chết"]
    R_06a["R-06a chờ gộp"]
    A_07["A-07 chặn"]
    K_02["K-02 chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_02["T-02 chết"]
    T_03["T-03 chết"]
    T_04["T-04 chết"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    F_01["F-01 chết"]
  end
```

Tổng: 85 việc, 1 đang làm (+19 chết, 1 chờ gộp), 1 chờ, 1 bị chặn, 62 xong.
