# A-11 - So sanh gpt-6.1-sol va gpt-6-astra (qua xingchi) - DO DANG

Trang thai: **moi co T1**; T4/T5 dang chay lai (lan truoc bi treo >2 gio o T4, da them gioi han 400 s). Cap nhat khi xong.
Dieu kien: effort low, sandbox read-only, `codex exec`, 1 lan/mo hinh/bai (chua lap lai).

| Bai | Mo hinh | Giay | 429 | input tok (cache) | output tok | Dung/sai |
|---|---|---|---|---|---|---|
| T1 tom tat A-05 thanh 5 dong | sol | 26 | khong | 79.879 (4.096) | 175 | Dung noi dung, 5 dong, tieng Viet |
| T1 | astra | 20 | khong | 68.390 (55.680) | 180 | Dung noi dung, 5 dong, tieng Viet |
| T4 soan file task | sol | chua co | - | - | - | chua chay xong |
| T4 | astra | chua co | - | - | - | chua chay xong |
| T5 tom tat D-01 theo mau TOM TAT | sol | chua co | - | - | - | chua chay |
| T5 | astra | chua co | - | - | - | chua chay |

Nhan xet so bo (chi T1, 1 lan): astra nhanh hon ~23%, token input it hon, cache tot hon; chat luong T1 ngang nhau. Chua du de ket luan; khong dung cho viec can sua ma/lap luan dai khi chua co T4/T5.
Ghi chu: lan chay dau T1 hai mo hinh deu 0 s do thieu `--skip-git-repo-check` (loi cau hinh, da sua). Doc ket qua tieng Viet can UTF-8 (raw bi mojibake khi xem bang console).
