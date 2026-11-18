# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 09:24, đừng sửa tay)

ĐANG LÀM: R-03, R-04b, R-05a, R-05b, R-05c
KẾ TIẾP: K-02, K-03, T-02, T-03, T-04
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
    R_02["R-02 chết"]
    R_05d["R-05d chết"]
    R_06a["R-06a chết"]
    R_06c["R-06c chết"]
    R_07a["R-07a chết"]
    R_07b["R-07b chết"]
    A_07["A-07 chặn"]
    K_02["K-02 chờ"]
    K_03["K-03 chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_02["T-02 chờ"]
    T_03["T-03 chờ"]
    T_04["T-04 chờ"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
  end
  K_03 --> K_02
```

Tổng: 79 việc, 5 đang làm (+6 chết, 0 chờ gộp), 5 chờ, 1 bị chặn, 62 xong.
