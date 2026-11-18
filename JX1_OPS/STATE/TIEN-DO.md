# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-18 08:58, đừng sửa tay)

ĐANG LÀM: U-01, U-02, U-03
KẾ TIẾP: K-03, R-01, R-02, R-03, S-01, T-02
BỊ CHẶN: A-07

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
    U_01["U-01 chạy"]
    A_07["A-07 chặn"]
    K_03["K-03 chờ"]
    R_01["R-01 chờ"]
    R_02["R-02 chờ"]
    R_03["R-03 chờ"]
    S_01["S-01 chờ"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    U_02["U-02 chạy"]
    T_02["T-02 chờ"]
    T_03["T-03 chờ"]
    T_04["T-04 chờ"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    U_03["U-03 chạy"]
    <MA_TASK>["<MA-TASK> chờ"]
  end
```

Tổng: 79 việc, 3 đang làm, 9 chờ, 1 bị chặn, 66 xong.
