# TIẾN ĐỘ (tự sinh bằng TOOLS/tien_do.py lúc 2026-11-19 03:23, đừng sửa tay)

ĐANG LÀM: SO-27, SO-28, XD-C01, XD-E05, XD-P02
KẾ TIẾP: 0-08, B-05, D-02, E-04, E-06, P-01
BỊ CHẶN: T-04

Ba chặng #091: 1 hiểu game (chuẩn hóa) → 2 đường truyền + exe → 3 tick/độ phản hồi/đồ họa.

```mermaid
flowchart LR
  subgraph S1["Chặng 1 hiểu game"]
  end
  subgraph S2["Chặng 2 truyền tải + exe"]
    T_04["T-04 chặn"]
  end
  subgraph S3["Chặng 3 tick và đồ họa"]
    SO_27["SO-27 chạy"]
    SO_28["SO-28 chạy"]
    XD_C01["XD-C01 chạy"]
    XD_E05["XD-E05 chạy"]
    XD_P02["XD-P02 chạy"]
    SO_25["SO-25 chờ gộp"]
    SO_26["SO-26 chờ gộp"]
    XD_C03["XD-C03 chờ gộp"]
    XD_E01["XD-E01 chờ gộp"]
    0_08["0-08 chờ"]
    B_05["B-05 chờ"]
    D_02["D-02 chờ"]
    E_04["E-04 chờ"]
    E_06["E-06 chờ"]
    P_01["P-01 chờ"]
    P_03["P-03 chờ"]
    X_05["X-05 chờ"]
  end
```

Tổng: 204 việc, 5 đang làm (+0 chết, 4 chờ gộp), 8 chờ, 1 bị chặn, 186 xong.
