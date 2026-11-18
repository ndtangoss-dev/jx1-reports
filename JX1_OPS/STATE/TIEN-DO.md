# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 11:49, đừng sửa tay)

ĐANG LÀM: F-01
KẾ TIẾP: K-02, R-06a
BỊ CHẶN: A-07

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
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
    R_05c["R-05c chết"]
    R_05d["R-05d chết"]
    R_06c["R-06c chết"]
    R_07a["R-07a chết"]
    R_07b["R-07b chết"]
    A_07["A-07 chặn"]
    K_02["K-02 chờ"]
    R_06a["R-06a chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_03["T-03 chết"]
    T_04["T-04 chết"]
    T_02["T-02 chờ gộp"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    F_01["F-01 chạy"]
  end
```

Tổng: 85 việc, 1 đang làm (+18 chết, 1 chờ gộp), 2 chờ, 1 bị chặn, 62 xong.
