TÓM TẮT 1: Groq (gói miễn phí, khóa lưu ở C:\Users\PC\.jx1keys\JX-GROQ.txt, ngoài kho) đo ngày 17/11/2026 bằng HTTP trực tiếp, không qua Codex.
TÓM TẮT 2: openai/gpt-oss-120b: độ trễ chữ đầu 0,8–1,7 s, sinh ~530–563 tok/s (3 lần đo, ~1.200–1.400 token ra mỗi lần); openai/gpt-oss-20b: ~1.164 tok/s (1 lần đo). So với gpt-6.1-sol ~27–34 tok/s: nhanh hơn khoảng 16–20 lần (120b) và hơn 35 lần (20b).
TÓM TẮT 3: llama-3.3-70b-versatile trả 404 (không có quyền/không tồn tại trên khóa này).
TÓM TẮT 4: Hạn mức theo thư #049 (30 RPM, 1.000 yêu cầu/ngày, 200K token/ngày, 8K token/phút cho gpt-oss-120b) lấy từ Chat, đã đối chiếu header thật 17/11: x-ratelimit-limit-requests=1000 (theo ngày), x-ratelimit-limit-tokens=8000 (theo phút), cả gpt-oss-120b và 20b; TPD 200K chưa thấy trong header, [CHƯA KIỂM]; mỗi việc tiểu yêu ~6,5M token vào nên không dùng làm tiểu yêu chính.
TÓM TẮT 5: Chỉ dùng cho việc ngắn, không nhạy cảm (tóm tắt, soạn/ chia task, phân loại); KHÔNG gửi mã nguồn jx1-source. Codex CLI không nối trực tiếp được (chỉ wire_api=responses), cần proxy nếu muốn.

# F-02 - Đo tốc độ API nhanh (Groq)
Đề đo: đoạn tóm tắt tiếng Việt ~400 từ (đề công khai, 123 token vào), stream, max_tokens 1500. Script: `JX1_OPS/TOOLS/groq_speed.py` (đọc khóa từ file ngoài kho, không in khóa).

| Model | Độ trễ chữ đầu (s) | Tổng (s) | Token ra | tok/s sinh |
|---|---|---|---|---|
| gpt-oss-120b #1 | 1,71 | 4,20 | 1400 | 563 |
| gpt-oss-120b #2 | 0,77 | 3,22 | 1302 | 530 |
| gpt-oss-120b #3 | 1,45 | 3,64 | 1211 | 553 |
| gpt-oss-20b #1 | 1,86 | 2,87 | 1173 | 1164 |
| llama-3.3-70b-versatile | - | - | - | 404 |

Việc hợp "làn nhanh": tóm tắt báo cáo, soạn task từ mẫu, phân loại log/lỗi, kiểm chính tả; ví dụ ≤8K token/phút nên nhồi ngữ cảnh lớn không được.
Chi phí nếu trả phí: [CHƯA KIỂM] (gói Developer ~10x hạn mức theo Chat; chưa thêm thẻ, chưa trả gì).
Việc cần làm tiếp nếu muốn dùng thường xuyên: đo header giới hạn thật (x-ratelimit-*), thử gpt-oss-120b với reasoning thấp, bọc thành công cụ `fast_summarize.py` cho PM.

## Header hạn mức thật (17/11/2026)
Cả hai model: limit-requests 1000 (reset ~86400 s), limit-tokens 8000 (reset theo phút, ~0,6 s sau 1 yêu cầu nhỏ). Số liệu 30 RPM/200K TPD của Chat chưa thấy trong header: coi 8K TPM + 1.000 yêu cầu/ngày là hạn mức chắc, phần còn lại chưa kiểm.
