# Lỗi 429 và token của tiểu yêu (đợt #181, 18/11/2026)

**TÓM TẮT 5 DÒNG**
1. Đọc 136 nhật ký tiểu yêu (16–18/11, xingchi, `gpt-6.1-sol` là chính): lỗi 429 thật chỉ có **15 lần trong 5 việc**; lỗi mạng chủ yếu là "stream đóng giữa chừng" (137 lần, 37 việc) và "Upstream request failed" (128 lần, 9 việc).
2. 429 tập trung ở khóa **K5** (12/15) và khi chạy cùng lúc **3–4** việc (11/15). "Upstream failed" dồn vào **17h–19h ngày 18/11** (126/128), không phụ thuộc rõ số song song.
3. Token: 127 việc có số liệu, tổng **450,8 triệu token vào** (82% là cache), 3,8 triệu ra. Trung bình 3,5 triệu vào/việc, nặng nhất 13,9 triệu. Đầu ra rất nhỏ so với đầu vào: tốn ở **đọc nhiều lượt**, không phải viết.
4. Mức suy luận `max` tốn trung bình 4,46 triệu vào/việc, `high` 3,08 triệu (chênh khoảng 45%).
5. Nên làm trước: hạ `max`→`high` cho việc đọc-tóm, chỉ rõ tệp cần đọc, tránh K5 và giờ 17h–19h. Chưa áp dụng gì. Cần tôi quyết định: không (Chat chọn).

## 1. Cách đếm và giới hạn của số liệu
Nguồn: `D:\JX-wt\<ID>.codex.log` (136 tệp, UTF-16) và `<ID>.run.ps1` (tên khóa, mức suy luận, mô hình). Chỉ đếm sự kiện `"type":"error"` của Codex, **không** đếm chữ "429"/"timeout" nằm trong nội dung mã mà tiểu yêu đọc (lần đếm thô cho số lớn gấp nhiều lần, sai). Giới hạn:
- Dòng nhật ký không có giờ. Giờ bắt đầu lấy từ `run.ps1`, kết thúc từ giờ sửa nhật ký; số việc chạy cùng lúc là **ước lượng** từ khoảng thời gian chồng nhau.
- Token chỉ có ở việc hoàn tất (127/136). Việc chết giữa chừng không có số, nên **không đo được token bỏ phí** khi chạy lại.
- 36 việc không đọc được tên khóa (ghi `?`).
- 15 lần 429 là mẫu quá nhỏ để kết luận chắc về ngưỡng song song.

## 2. Lỗi theo loại
| Loại | Sự kiện | Số việc | Ví dụ |
|---|---|---|---|
| Reconnect (stream đóng trước khi xong) | 137 | 37 | `Reconnecting... 1/5` |
| Upstream request failed | 128 | 9 | `stream disconnected before completion: Upstream request failed` |
| 429 | 15 | 5 | `exceeded retry limit, last status: 429` |
| Khác | 4 | 4 | `gpt-6.1-sol requires Responses for tool calls; this account only supports Chat Completions` (18/11 sáng 09h) |
| Timeout thật | 0 | 0 | — |

Việc kết thúc `exit=1`: A-08c, B-02b, D-01, H-02. Việc không có `.done`: R-05, R-06, R-07, T-01, U-03 (kết quả chưa biết từ nhật ký).

## 3. Theo giờ
Reconnect dày: 17/11 15h, 18/11 00h–01h. **"Upstream failed" dồn 18/11 17h–19h (126/128).** 429 lẻ tẻ, đỉnh 17/11 10h–11h.

## 4. Theo số việc chạy cùng lúc (ước lượng lúc bắt đầu)
| Cùng lúc | Việc | 429 | Upstream | Reconnect |
|---|---|---|---|---|
| 1–2 | 56 | 3 | 22 | 74 |
| 3–4 | 39 | 11 | 63 | 37 |
| 5–7 | 25 | 1 | 39 | 13 |
| 8+ | 16 | 0 | 4 | 13 |

Không có đường tăng đều theo số song song. Kết luận thận trọng: trần song song **không phải** nguyên nhân duy nhất; chất lượng đường xingchi theo giờ và theo khóa quan trọng hơn.

## 5. Theo khóa (chỉ tên khóa)
| Khóa | Việc | 429 | Upstream | Reconnect |
|---|---|---|---|---|
| K2 | 27 | 3 | 21 | 22 |
| K3 | 26 | 0 | 23 | 19 |
| K4 | 17 | 0 | 1 | 7 |
| K5 | 23 | **12** | **62** | 50 |
| K6 | 7 | 0 | 20 | 25 |
| ? | 36 | 0 | 1 | 14 |

K5 xấu nhất, K4 sạch nhất.

## 6. Token
| Mức suy luận | Việc | Vào/việc | Ra/việc |
|---|---|---|---|
| max | 51 | 4.464.797 | 46.797 |
| high | 70 | 3.078.250 | 19.396 |
| medium | 4 | 1.811.963 | 9.675 |
| low | 2 | 176.896 | 769 |

Tổng: 450.783.820 vào (cache 82,4%), 3.784.681 ra. Việc ngốn nhất (vào): A-07b 13,9 M; R-05b 12,9 M; R-05a 11,9 M; R-04b 10,4 M; A-06 10,2 M; A-05 10,2 M; R-06c 8,8 M; N-05 8,6 M; K-03c 8,3 M. Mỗi lượt công cụ gửi lại toàn bộ ngữ cảnh đã đọc, nên token vào tăng theo số lượt và cỡ tệp đã đọc. Chênh `max`/`high` có thể lẫn với việc nặng hơn được gán `max`; chưa kiểm.

## 7. Đề xuất (xếp theo lợi/rủi ro, CHƯA áp dụng)
| # | Đề xuất | Tiết kiệm | Rủi ro | Hoàn tác |
|---|---|---|---|---|
| 1 | Việc đọc-tóm dùng `high` thay `max` | khoảng 30% token vào/việc nếu chất lượng giữ | báo cáo nông hơn; thử 2–3 việc so mẫu trước | trả về `max` |
| 2 | Prompt nêu sẵn danh sách tệp cần đọc, cấm quét cả thư mục lớn, giới hạn cỡ tệp đọc một lần | lớn về lý thuyết, **chưa đo** | bỏ sót nguồn | sửa lại mẫu prompt |
| 3 | Tránh K5 (xoay sang K4/K3), tránh phát việc 17h–19h | giảm lỗi mạng rõ nhất theo số liệu | cần theo dõi thêm 1–2 ngày | bỏ luật |
| 4 | Khi gặp 429/Upstream: chờ lùi dần rồi nối lại, thay vì khởi động lại từ đầu | tránh mất 3,5 M/lần chạy lại; mức bỏ phí hiện không đo được | thấp | tắt |
| 5 | Giữ trần 3 việc/khóa; thử 2 việc/khóa riêng với K5 | giảm 429 | chạy chậm hơn | trả về 3 |
| 6 | Gộp các việc rất nhỏ | nhỏ | mất song song | tách lại |
| 7 | Rút gọn `AGENTS.md` cho tiểu yêu chỉ đọc | chưa đo; cache 82% nên lợi nhỏ | mất luật | khôi phục |

Không dùng: Gemini miễn phí (hạn mức 20 lượt/ngày, xem `SO-SANH-NHA-CUNG-CAP.md`).

## 8. Chưa kiểm tra
- Token bỏ phí khi việc chết rồi chạy lại: không có số.
- Nguyên nhân "Upstream failed" 17h–19h (phía xingchi hay mạng): chưa rõ.
- Bốn việc `exit=1` không phải do 429 (lỗi Responses/Chat); chưa xem hết 5 việc không có `.done`.

## 9. Đã áp dụng theo Q-51 (#183, 18/11 ~22:50) và kết quả thử
| Việc | Thay đổi | Hoàn tác |
|---|---|---|
| (a) | `tong_quan.py`: `KEY_CAP` (K5, K6 tối đa 2 việc), `KEY_ORDER` (việc mới xoay K4, K3, K2, K6, K5). Thử hàm: sau khi K4/K3/K2 đủ 3 việc thì sang K6 rồi K5, đúng thứ tự | khôi phục `tong_quan.py.bak-181` |
| (b) | `hold_now`: việc `ready` mới có `priority` ≥ 2 không giao trong 17h–19h (ghi chú vào TONG-QUAN-GHI); việc chạy lại khi chết và việc `priority` 0/1 không bị chặn | đặt `HOLD_H = (0, 0)` |
| (c) | Mẫu prompt mặc định thêm đoạn "TIẾT KIỆM TOKEN": chỉ đọc tệp liệt kê ở mục Nguồn, không quét thư mục lớn, mỗi lần đọc ≤ ~400 dòng, không đọc lại. Chỉ áp cho prompt MỚI sinh (prompt đã có giữ nguyên) | xóa đoạn đó trong `ensure_worktree` |
| (d) | `chay_codex.ps1` đọc `JX_CODEX_EFFORT`; `tong_quan.py` lấy từ trường `effort:` của tệp task. Không có trường = `max` như cũ | bỏ trường `effort:` |

Kiểm: cú pháp Python đạt, `tong_quan.py --dry` chạy không lỗi, hàm `pick_key`/`task_field` thử trực tiếp. Chưa dừng Tổng quản đang chạy; thay đổi có hiệu lực ở lần Tổng quản khởi động lại.

**Kết quả thử (d): CHƯA CÓ.** Hiện không có việc đọc-tóm `ready` nào để đặt `effort: high` (không tạo việc giả tốn token). Khi có 2–3 việc đọc-tóm mới, đặt `effort: high`, so độ đủ và token với báo cáo `max` trước đó rồi ghi vào đây.
