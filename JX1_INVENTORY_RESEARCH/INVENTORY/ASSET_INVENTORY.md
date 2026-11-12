# Asset Inventory

Legend: VERIFIED = metadata/header or source evidence; PROBABLE = format inference; UNKNOWN = internal contents or runtime use not established; BLOCKED = intentionally not opened/extracted.

## Asset-bearing branches

- **VERIFIED** — Client loose resources: Folder/Client2912-20260116T044348Z-3-001/Client2912/Client/Resources — 947 files, 78,035,592 bytes.
- **VERIFIED** — Client data directory: .../Client2912/Client/data — 58 files, 15,694,774 bytes.
- **VERIFIED** — CDN tree data_cdn — 51 files total, about 3.76 GiB; includes apk and data subdirectories.
- **VERIFIED** — Runtime/server package: Folder/ServerNew-20260116T043145Z-3-001/ServerNew/_bin_v2_ — part of an 8,402-file ServerNew subtree; includes settings, Lua scripts, map/package files, runtime binaries, logs and dumps by metadata.
- **VERIFIED** — Separate server source and build outputs are under SwordOnline/SwordOnline/jxOnline.

## Loose media and game data (whole repository counts)

| Type | Extension(s) | Count | Notes |
|---|---|---:|---|
| Raster images | PNG | 970 | 646 are under client Resources |
| Raster images | JPG/JPEG | 14 | Includes client and server/runtime data |
| Raster/source art | PSD | 6 | Source-art files are present |
| Raster images | BMP | 4 | Loose files |
| Fonts | TTF | 32 | 20 under client Resources |
| Fonts | FNT | 7 | Client font resources present |
| Audio | OGG | 111 | 103 under client Resources |
| Audio | MP3 | 5 | Four under client data |
| Audio | WAV | 11 | Loose audio files |
| Audio banks | BANK | 9 | Exact FMOD bank contents/version unknown |
| Atlas/shader metadata | PLIST | 6 | One client .tps project; atlas membership not exhaustively checked |
| Shader files | FSH/VSH/FRAG | Present | Client Resources/Shaders includes blur.fsh and blur.vsh |
| Map-like files | MAP/WOR | 115 MAP; 1 WOR | Extensions alone do not validate map data |
| Scripts/config | LUA/INI | 4,030 LUA; 928 INI | Contents may include sensitive settings and were not read wholesale |

No loose .spr, .ani, .dds or .pvr extension was found in the manifest. This does not mean those formats are absent inside archives or encoded with other extensions. The client has a KSprControl module and the CDN includes spr.pak, but their internal frames were not inspected.

## Archives and packaged assets

- **VERIFIED** — 46 files ending in .pak total 3,443,376,374 bytes across the repository. Forty are in data_cdn/data and total approximately 3.41 GB.
- **VERIFIED** — data_cdn/data has packages named for update, sprites, images, maps, resources, skills, sound, fonts and UI. Names indicate intended grouping only; they do not prove archive contents.
- **VERIFIED** — 9 APK files total 743,167,187 bytes; FILE_MANIFEST.csv contains SHA-256 for 40 CDN PAK files and 8 CDN APK files (48 hashes total). The ninth APK is outside the hashed CDN selection.
- **VERIFIED** — A 16-byte header sample from CDN PAK files begins with ASCII PACK followed by binary fields. This supports a custom/container-like package hypothesis; format/version/index layout is UNKNOWN.
- **VERIFIED** — The .pack extension also occurs in Git object storage; it is not counted as a game asset format without path context.
- **VERIFIED** — Archive types also include ZIP (10), RAR (17), and 7Z (3); none were extracted or converted.
- **VERIFIED** — No file with a .fsjx extension was found. Files named FsjxClient.ini exist. FSJX format semantics are UNKNOWN.
- **VERIFIED** — Three CDN files sound.pak, sound-old.pak and sound-old1.pak have identical SHA-256 values in FILE_MANIFEST.csv; hash equality verifies byte-identical contents, not whether the duplicate files are redundant at runtime.
- **UNKNOWN/BLOCKED** — Internal PAK/ZIP/RAR/7Z/APK file lists, actual image dimensions/color formats, sprite frame counts, animation timing, compression, archive index integrity and asset completeness. Archives were intentionally not unpacked.

## Hashing and privacy

SHA-256 was computed for 40 files under data_cdn/data with .pak extension and 8 CDN APK files. Hashes are in FILE_MANIFEST.csv. No hashes were computed for key stores, configuration secrets, logs, dumps, database files, Git objects or non-CDN binaries. The manifest redacts sensitive-looking filename segments while retaining file rows, sizes and timestamps.