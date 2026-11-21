# Phi phong: ngũ hành, dòng ẩn, nhãn tên (A, 21/11/2026)
Nhãn THẤY = đo trên LD Test-36; MÃ = đọc mã, chưa chạy; CHƯA KIỂM = chưa thử.

## Hệ và yêu cầu (THẤY, tooltip)
k1 Lăng Vân Thủy 6000; k3 Phá Quân Thổ 7800; k4 Kinh Lôi Kim 9600; k6 Ngự Phong Kim 10500; k11 Cao cấp Hỏa 15000. Yêu cầu tài phú = 6000+900(k-1).
Ba dòng cuối tooltip là tên bộ: dòng của chính món màu xanh, hai món kề màu xám.

## Chỉ số khi mặc (THẤY)
Sinh lực/nội lực +200k, thể lực +100k. Né tránh và kháng KHÔNG đổi theo cấp hay hệ (Né tránh 480).

## Dòng ẩn (MÃ, KItemList.cpp:54-71, 2674)
`ms_ActivedEquip`: mỗi bộ phận có 3 bộ phận "kích hoạt"; phi phong xuất hiện cùng ấn (yinjian), trang sức (shiping), ngựa, mặt nạ. nActive = min(3, số quan hệ tương sinh). CHƯA KIỂM: dòng ẩn của phi phong có bật khi đi cùng ấn/trang sức tương sinh.

## Nhãn tên cạnh nhân vật (MÃ)
`KgameWorld.cpp PaintPifeng` giữ nhãn cũ nếu node còn → không đổi khi đổi phi phong. Bản sửa [pfl] ở D:\JX-build\qh9A (so getUserData với loại, khác thì gỡ và tạo lại), chưa kiểm trên máy.
