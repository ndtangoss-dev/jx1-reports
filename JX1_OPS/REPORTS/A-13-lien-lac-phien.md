# A-13 - Liên lạc giữa phiên, subagent lồng

## TÓM TẮT
1. Claude Code 2.1.325 (>= 2.1.172): có công cụ Agent (subagent), SendMessage, danh sách phiên (`list_sessions`).
2. Thử b: subagent Sonnet đọc `E-01b-thieu-giao-thuc.md` và trả 5 dòng TÓM TẮT đúng định dạng, nội dung khớp báo cáo (50 ID cố định, 25 biến độ dài, 41 test). Chưa đo token chính xác (phiên không có số liệu trước/sau); kết quả chỉ nằm trong ngữ cảnh ~15 dòng thay vì cả báo cáo.
3. Lưu ý: bản tóm tắt cũ còn nói "commit bị chặn" dù PM đã commit; subagent chỉ đọc nên phản ánh đúng ghi chú trong file, không cập nhật trạng thái sau. PM phải đối chiếu trạng thái thực.
4. Thử c: `list_sessions` trả "No other sessions found"; phiên Chat (claude.ai cloud) không hiện trong máy này, không gửi tin được. Hộp thư repo giữ làm kênh chính.
5. Khuyến nghị: dùng subagent Sonnet cho báo cáo > 200 dòng, PM kiểm lại dòng trạng thái/commit. Không chạy claude lồng qua shell.

Cần tôi quyết định: không
