# TỐI ƯU SAU NÀY - 90 FPS (giai đoạn 1) rồi 120 FPS (giai đoạn 2)

Quyết định Q-43. Chỉ ghi, chưa sửa. Mức tối đa của thanh trượt là 90 (KuiOptions.cpp:182-192).

| # | Việc | Nguồn | Giai đoạn |
|---|---|---|---|
| 1 | Logic, đạn, hiệu ứng bám thời gian thật (accumulator + nội suy hiển thị) | H-13, H-15 | 1 |
| 2 | Va chạm quét theo đoạn thay vì điểm | H-15 | 1 |
| 3 | Joystick gửi theo thời gian thay vì theo khung | H-15 | 1 |
| 4 | Hit event theo ngưỡng vượt chứ không bằng nhau | H-15 | 1 |
| 5 | Mất khung hiệu ứng glow/sét khi vung kiếm | H-14 | 1 |
| 6 | Khung giữa bằng nội suy (đánh giá ở J-06) | J-05, J-06 | 2 |
| 7 | Làm mượt hình ảnh giữ nét gốc | L-01 | 1-2 |
| 8 | Chi phí vẽ trên máy mạnh (draw call, batch) | BASELINE, J-05 | 2 |

Quy trình sửa: đo H-15 ở 30/60/90 → đề xuất gửi Chat duyệt → sửa trên bản sao client → APK thử tên riêng → đo trước/sau → chủ chơi thử.
