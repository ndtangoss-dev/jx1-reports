# JX1 Cường Hóa UI – Asset handoff

## Files
- `JX1_CuongHoa_UI_Atlas.png` — generated UI atlas, 1536x1024 RGBA.

## Atlas layout (approximate pixel regions; origin is top-left)
- Main assembled enhancement-window reference: x=0..1150, y=0..800
- Reusable slot/frame samples: x=1170..1535, y=0..250
- Bùa May Mắn / Phù Bảo Hộ sample tiles: x=1290..1530, y=140..250
- Connector-line samples: x=1170..1535, y=250..410
- Info panel sample: x=1160..1535, y=410..550
- Header/banner strip sample: x=1160..1535, y=560..620
- Button and close-button samples: x=1150..1535, y=620..710
- Currency icon samples: x=1160..1380, y=710..800
- Decorative border/corner samples: x=0..1150, y=810..1024 and x=1170..1535, y=900..1024

## Integration notes for Claude / Cocos2d-x
1. Treat this as a visual source atlas, not a ready-made Cocos `.plist`/`.pvr.ccz` atlas.
2. Crop individual sprites into separate transparent PNGs; preserve alpha and trim transparent margins.
3. Use 9-slice scaling for panel backgrounds, title bars, buttons and slot frames where appropriate.
4. Rebuild labels and dynamic values as Cocos labels rather than baking text into the artwork:
   - Nguyên liệu cần
   - Cần bạc
   - Tỉ lệ thành công
   - Chú ý
   - Cường Hóa
5. Keep the equipment grid on the right side of the enhancement window. The two currency displays belong directly below that grid.
6. Do not add a left-side function menu or a separate Hành Trang window in this enhancement screen.
7. Keep actual JX1 equipment/item icons from the existing game assets whenever available. The atlas is primarily for UI chrome, frames, panels, connectors and buttons.
8. This atlas is generated concept art. Verify each crop at native resolution and replace any inaccurate or malformed glyphs with native Cocos text/assets before shipping.
