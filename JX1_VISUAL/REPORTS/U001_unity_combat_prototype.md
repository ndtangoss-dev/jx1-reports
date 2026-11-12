# U001 – JX1 Unity Combat Prototype — Báo cáo bàn giao + checkpoint

Ngày: 2026-11-13. Trạng thái: **XONG phạm vi chính** (nhân vật, quái, kỹ năng chạy trong Unity Editor, đã kiểm chứng tự động trong Play Mode).

## TÓM TẮT
1. Project Unity riêng `D:\JX1_Unity_U001` (Unity **6000.2.14f1**), scene `Assets/Scenes/U001_CombatDemo.unity`.
2. Dùng **asset JX1 thật** (chuyển SPR → PNG từ PAK gốc, chỉ đọc): nhân vật nam tay không (ghép 4 bộ phận), quái `enemy003`, kỹ năng Nga My "Từ Hàng Phổ Độ" (đạn 20 khung + nổ 18 khung).
3. Play Mode (chạy tự động trong Editor, batchmode): **0 lỗi, 0 cảnh báo**; kỹ năng hiện **đủ 20/20 khung đạn, 18/18 khung nổ**.
4. Phím 1 đánh, 2 kỹ năng, 3 phát lại; có nút bấm và 3 thanh trượt FPS (4–60) trên màn hình.
5. **MCP Unity CHƯA kết nối** với Claude Code trong phiên này. Project được tạo và kiểm chứng bằng Unity batchmode thay thế.

## 1. Môi trường
| Mục | Kết quả | Mức |
|---|---|---|
| Unity Editor | `C:\Program Files\Unity\Hub\Editor\6000.2.14f1` | VERIFIED |
| Unity MCP | `claude mcp list` chỉ có "Claude Docs"; `~/.claude.json` có `"mcpServers": {}`. Gói `com.coplaydev.unity-mcp` có trong project **khác** (`C:\UnityProjects\MzuIdle_Unity`), có log server cũ ở `%LOCALAPPDATA%\UnityMCP\Logs` (cập nhật lần cuối 11/11). Không có công cụ MCP nào trong phiên Claude này | VERIFIED: **chưa kết nối** |
| Thao tác Editor / Hierarchy / Console | Không qua MCP. Thay bằng script Editor chạy batchmode: dựng scene, vào Play Mode, chụp ảnh, đếm lỗi Console | VERIFIED |
| Render pipeline | Built-in 2D (SpriteRenderer). **Không cài URP** để không thêm package; đổi sang URP sau được | Quyết định |
| Input | Input Manager cũ (`activeInputHandler: 0`), dùng `UnityEngine.Input` + IMGUI. Không cài package | VERIFIED |
| Source JX1 / V001 / V002 / công cụ | `C:\Jx1CocoV3`; báo cáo ở `C:\Jx1CocoV3_RESEARCH` và GitHub `JX1_VISUAL/REPORTS`; công cụ PAK `C:\Jx1CocoV3\docs-analysis\tools\pak_extract.py` | VERIFIED |

**Để bật MCP cho phiên sau (người dùng làm, ~2 phút, chưa làm):** mở `D:\JX1_Unity_U001` bằng Unity Hub → Window > Package Manager > + > Add package from git URL: `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity` → trong Unity mở cửa sổ MCP for Unity, chọn cấu hình cho Claude Code (hoặc chạy lệnh đăng ký mà cửa sổ đó hiển thị) → **khởi động lại Claude Code** (công cụ MCP chỉ nạp khi mở phiên mới). Tôi chưa tự cài vì cần tải gói từ Internet và cần phiên Claude mới mới dùng được.

## 2. Đường dẫn
- Project: `D:\JX1_Unity_U001`
- Scene demo: `D:\JX1_Unity_U001\Assets\Scenes\U001_CombatDemo.unity`
- Script chạy: `Assets/Scripts/JX1FrameAnimator.cs`, `Assets/Scripts/U001DemoController.cs`
- Script Editor: `Assets/Editor/U001Setup.cs` (menu **Tools > U001 > Build Demo Scene**), `Assets/Editor/U001Verify.cs` (kiểm chứng tự động)
- Workspace phụ: `D:\JX1_Unity_U001_work` (công cụ `tools\spr2png.py`, ảnh bằng chứng `evidence\`, log `*.log`, báo cáo này)

## 3. Asset JX1 đã dùng (bản sao PNG, file gốc không đổi)
Chuyển bằng `D:\JX1_Unity_U001_work\tools\spr2png.py`: đọc PAK trong `C:\Jx1CocoV3\data_cdn\data` theo thứ tự `paklist.ini` (chỉ đọc), giải nén nrv2b bằng hàm của `pak_extract.py`, giải RLE 256 màu theo `Kgetinidata.cpp`, ghép khung lên khung 320×320 tại vị trí gốc. **Không sửa màu, không vẽ thêm.** Mỗi thư mục có `meta.json` ghi file SPR, PAK, kiểu nén, số khung.

| Thành phần | SPR gốc | PAK | Hướng × khung |
|---|---|---|---|
| Nhân vật – đứng chiến đấu | `\spr\npcres\man\MA_{BD,LH,RH,HD}_001_ST03.spr` | spr.pak | 8 × 11 |
| Nhân vật – chạy | `MA_*_001_RN01.spr` | spr.pak | 8 × 11 |
| Nhân vật – đánh tay không | `MA_*_001_AT01.spr` | spr.pak | 8 × 18 |
| Nhân vật – phép tay không | `MA_*_001_MG02.spr` | spr.pak | 8 × 12 |
| Nhân vật – bị thương | `MA_*_001_IJ01.spr` | spr.pak | 8 × 9 |
| Quái enemy003 – đứng/đi/đánh/bị đánh/chết | `\spr\npcres\enemy\enemy003\enemy003_{st,wlk,at,bat,die}.spr` | spr.pak | 8 × 6/14/14/7/13 |
| Kỹ năng – đạn | `\spr\skill\峨嵋\mag_em_12_慈航普渡.spr` (Missles.txt id 5) | skills.pak | 1 × 20 |
| Kỹ năng – nổ | `\spr\skill\峨嵋\mag_bz_bin5_爆炸效果.spr` | skills.pak | 1 × 18 |

Tổng 958 PNG (4,5 MB) trong `Assets/JX1Assets`. Bộ phận **vai (SH) và tóc (HR)** của bộ trang phục 001 không có trong PAK cho các động tác này → bỏ qua, nhân vật gồm thân, 2 tay, đầu (đầu 001 là đầu trọc). Thứ tự vẽ dùng tạm: thân → tay trái → tay phải → đầu; chưa áp bảng `男主角贴图顺序表` (đúng ở hướng 6 và 2 đang dùng, kiểm bằng mắt; các hướng khác có thể sai lớp tay).

**Phần do Unity tạo (KHÔNG phải asset JX1)**: vòng sáng cộng màu khi trúng đòn (`UnityFX_Glow.png`, vật liệu Additive; bật/tắt bằng ô "Hiệu ứng Unity bổ sung"), nền đất (`UnityFX_Ground.png`), màu nền camera.

## 4. Hoạt ảnh và kỹ năng đã hoàn thành
- `JX1FrameAnimator`: phát theo **thời gian thực** (`Time.deltaTime`), FPS từng clip + hệ số tốc độ; **không gắn nhịp 18 Hz**; tùy chọn `neverSkipFrames` (mặc định bật) bảo đảm mỗi khung gốc hiện ít nhất 1 lần dù máy giật (vấn đề cắt đuôi hiệu ứng của client cũ, V002 mục 5 #12).
- Nhân vật: đứng (lặp), chạy tới / chạy về (hướng 6 / 2), đánh 18 khung, phép 12 khung, bị thương.
- Quái: đứng (lặp), phản ứng **bị đánh** 7 khung rồi về đứng. Có sẵn clip đi, đánh, chết (chưa gắn phím).
- Đánh thường (phím 1): chạy tới → đánh → ở 60% khung (theo JX1 `ATTACKACTION_EFFECT_PERCENT 60`) quái bị đánh + vòng sáng Unity → chạy về.
- Kỹ năng (phím 2): phép → thả đạn ở 60% khung phép → đạn bay hết **20/20 khung** → nổ **18/18 khung** tại quái + quái bị đánh + vòng sáng Unity → kết thúc.
- Phát lại (phím 3): lặp lại hành động vừa làm.

## 5. Bằng chứng (Play Mode tự động, `U001Verify.Run`)
`D:\JX1_Unity_U001_work\evidence\`: `verify_result.txt` (errors=0, warnings=0, "dan 20/20 khung, no 18/18 khung"), ảnh `01_idle`, `02_attack_run`, `03_attack_hit`, `04_monster_hurt`, `05_cast`, `06_skill_fly`, `07_skill_explode` (1280×720, ảnh từ camera, không có lớp nút OnGUI), `seq\skill_000…124.png` (chuỗi ảnh kỹ năng thay cho video; máy không có ffmpeg để ghép video).
Log: `build_scene3.log`, `verify3.log`.

## 6. Lỗi còn tồn tại / chưa hoàn thành
| Vấn đề | Mức |
|---|---|
| Unity MCP chưa kết nối với Claude Code (mục 1) | Cần người dùng làm |
| Nền đất do Unity tạo không hiện trong ảnh chụp (nền chỉ là màu đặc) | Nhỏ, chưa sửa |
| Thứ tự lớp bộ phận nhân vật chưa theo bảng gốc; chỉ đúng ở 2 hướng đang dùng | Nhỏ |
| Nhân vật thiếu vai/tóc (không có SPR cho bộ 001) | Do asset |
| Chưa có video thật (chỉ chuỗi ảnh) | Nhỏ |
| Chưa chạy bằng tay trong cửa sổ Editor có giao diện (chỉ batchmode) | **Người dùng kiểm sáng mai** |
| Chưa build Android (ngoài phạm vi ưu tiên) | Chưa làm |
| Chưa dùng URP | Quyết định có chủ ý |

## 7. Cách mở và chạy demo
1. Mở **Unity Hub** → **Add** (hoặc Open) → chọn thư mục `D:\JX1_Unity_U001` → mở bằng 6000.2.14f1.
2. Trong cửa sổ **Project**: `Assets/Scenes` → bấm đúp `U001_CombatDemo`.
3. Bấm nút **Play** (▶) ở giữa trên cùng.
4. Bấm vào cửa sổ **Game**, rồi: phím **1** đánh, **2** kỹ năng, **3** phát lại — hoặc bấm nút trên màn hình. Kéo thanh **FPS** để đổi tốc độ khung (18 = tốc độ JX1 gốc). Bỏ chọn "Hiệu ứng Unity bổ sung" để xem chỉ asset gốc.
5. Nếu scene bị hỏng: menu **Tools > U001 > Build Demo Scene** dựng lại.

## 8. Checkpoint và hướng tiếp tục chính xác
- Đã lưu: project, scene, script, asset, bằng chứng (tất cả trên ổ D, ngoài repo). Không có tác vụ nền đang chạy.
- Không có thay đổi nào trong `C:\Jx1CocoV3`, PAK gốc, server, VM, database. Không commit/push source hay asset game.
- Nếu tiếp tục (theo thứ tự, vẫn trong phạm vi U001):
  1. Người dùng chạy thử bằng tay (mục 7) và nhận xét.
  2. Sửa nền đất (kiểm `MakeGroundSprite` trong `U001Setup.cs`, có thể `LoadAssetAtPath<Sprite>` trả null).
  3. Áp bảng thứ tự vẽ `男主角贴图顺序表.ini` cho đủ 8 hướng.
  4. Kết nối MCP (mục 1) để thao tác trực tiếp Hierarchy/Scene/Console.
  5. (Tùy chọn) Build Android.
- Lệnh dựng lại không cần giao diện: `Unity.exe -batchmode -nographics -projectPath D:\JX1_Unity_U001 -executeMethod U001Setup.BuildBatch -quit`; kiểm chứng: `Unity.exe -batchmode -projectPath D:\JX1_Unity_U001 -executeMethod U001Verify.Run -logFile D:\JX1_Unity_U001_work\verify.log`.
