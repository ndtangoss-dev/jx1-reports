# Sonnet checkpoint

Cập nhật: 2026-11-12 (Phase 48)

- `EXPLORATION_MODE=OFF` — chủ dự án đã yêu cầu dừng tự khám phá để tiết kiệm hạn mức (sau Phase 47). Chỉ bật lại khi chủ dự án nói "Tiếp tục Sonnet".
- `BUG_FIX_QA_MODE=ON` — Sonnet vẫn làm QA kỹ thuật đã duyệt (Phase 48: thao tác gameplay cho Mốc B).

## Tiến độ khám phá (dừng tại đây)
- Đã VERIFIED: xác minh lỗi nhấp nháy (P47-diag) và bản sửa P47 (TEST_RESULTS/47-p47-verification.md); đặt FPS game 90 (LDPlayer thực ~60).
- Đang dở khi dừng (Phase 47): hồ sơ nhân vật C1 (một phần, knowledge/stats/diem-tiem-nang.md), thí nghiệm tiềm năng C2, kỹ năng C3, vũ khí/trang bị C4 — CHƯA làm hết.
- Bước tiếp theo khi "Tiếp tục Sonnet": hoàn thành C1 (knowledge/characters/jxt36a.md), rồi C2 (+1 điểm từng thuộc tính, experiments/potential.csv), C3 (Đại Lực Kim Cang Chưởng, experiments/skill-damage.csv), C4.

## Trạng thái nhân vật test
- jxt36a, cấp 200, hệ Kim, tay không, phím chính Đại Lực Kim Cang Chưởng, Bộ Kim Phong, ngựa Đích Lô, Ngưng Thần đan ở ô nhanh (~892,198), Lệnh bài GM. Vị trí cuối: Ba Lăng Huyện ngoài thành.
- APK trên LDPlayer: P47 thử (jx-p47-test.apk).

## Phase 48 Moc B (2026-11-12)
- Model: Sonnet 5.5. EXPLORATION_MODE van OFF. Game DANG DANG NHAP (jxt36a, Ba Lang Huyen ~177/191) de chu du an lam Moc C.
- Dang nhap ~15:26 (may that), cho 60 s, T0=1794472060 (epoch may that). Bo do: collect-B.log samples=600/600, conn_samples=67.
- Doan (epoch may that): dung_yen 1794472060-1794472240; di_chuyen 1794472245-1794472450 (8 chang run46, 180/195,203/198,190/185,165/200...); chien_dau 1794472455-1794472655 (217 lan nhan nut danh ~0,6-0,9 s, 1 thuoc noi luc, Dai Luc Kim Cang Chuong la phim chinh). File: experiments/server-resource/phase48-segments-B.csv.
- Su co: nhan vat da o tren ngua san luc dang nhap, nen nut ngua (830,260) lam di_chuyen chay BO HANH (xuong ngua), chien_dau lai len ngua (danh van hoat dong). Script driver tu thoat sau khi ghi n=217 nen epoch ket thuc chien_dau suy ra tu moc 595 s + log (sai so vai giay).
- Trang thai cuoi: cap 200, HP 1653/2118 (78%), MP 5748/5748, the luc 933/1312, dang tren ngua, 6 thuoc noi luc; khong rut lui.

## Phase 48 Moc C bo sung (2026-11-12, Opus thao tac LDPlayer)
- EXPLORATION_MODE van OFF. jxt36a o Ba Lang Huyen, van dang nhap. Moc C3 da do xong va push (cba0480).
