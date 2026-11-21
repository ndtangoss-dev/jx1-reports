# ĐANG CHẠY TRƯỚC KHI TẮT MÁY (B ghi 21/11 10:25, #B-086)
Dùng khi `/tiep-tuc` để bật lại đúng.

| Thành phần | Trạng thái trước tắt | B đã làm | Bật lại thế nào |
|---|---|---|---|
| JX-TongQuan (tong_quan.py, 3 phút) | Ready, chạy lần cuối 10:25:27 | **DISABLE** lúc 10:25 (đã kiểm: Status Disabled) | `python -I TOOLS/tong_quan.py --dry` rồi `schtasks /Change /TN JX-TongQuan /ENABLE` + `/Run` |
| JX-codex-* (≈190 tác vụ, ID như SO-01, XD-*, HG-*, SC-00x) | TẤT CẢ trạng thái Ready, KHÔNG cái nào Running; log codex mới nhất SC-002 00:36, SC-006 00:22 (sáng 21/11) | Không có worker Codex đang chạy nên không cần /End, không có WIP mới | Tổng quản tự giao lại việc status=ready sau khi ENABLE |
| SC-006 (TASKS status=running) | do B (Sonnet) làm tay, không phải tác vụ Codex; PARTIAL; nhánh sc-006b local ở D:\JX-wt\SC-006B | Không dừng gì; tiếp khi bật lại theo BAN-GIAO-B.md | B đọc BAN-GIAO-B.md |
| JX-Guard | Disabled sẵn | Giữ nguyên | Không cần bật trừ khi Chat bảo |
| JX-LDCanh | Ready (không chạy) | Không đổi; pythonw bộ canh LD (PID 141016 ghi trước đây) chưa kiểm còn sống | Bật theo A nếu cần LD |
| JX-Forwarder-T36 | **Running** | KHÔNG đụng (thuộc VM Test-36, phần A: tắt cùng VM) | A bật cùng chuỗi VM |
| JX1-Task-Dispatcher | **Running** (pythonw jx1_task_dispatcher.py ở C:\Jx1CocoV3\docs-analysis\scripts) | KHÔNG đụng (hạ tầng của A/chủ, ngoài việc B giao; AGENTS ghi không dùng Dispatcher) | Chủ/A quyết dừng hay giữ |
| JX-CDN-8080, JX-Forwarder-Tailscale | Ready | Không đổi | Theo A |
| gs001 / VM Test-36 | phần A | B không đụng | A |

KHOA.md: bảng "Đang giữ" rất cũ (16-18/11), không còn worker thật tương ứng; không sửa (không phải việc đợt này).
Ghi chú: tiến trình python nền cũ (nhiều PID từ 14-20/11) KHÔNG xác minh được lệnh (wmic/CIM không dùng được); B không kill tiến trình lạ.
