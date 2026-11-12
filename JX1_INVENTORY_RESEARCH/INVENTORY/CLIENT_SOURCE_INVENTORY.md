# Client Source Inventory

Legend: VERIFIED = directly supported by a file or configuration; PROBABLE = inference from structure/symbols; UNKNOWN = not established from source inspection; BLOCKED = intentionally not inspected or not runnable in this inventory.

## Root and technology

- **VERIFIED** — Client project: Folder/Client2912-20260116T044348Z-3-001/Client2912/Client.
- **VERIFIED** — C++/C application using bundled Cocos2d-x. cocos2d/CHANGELOG:1 identifies cocos2d-x 3.17.2.
- **VERIFIED** — Root CMakeLists.txt uses CMake minimum 3.6, APP_NAME projectdebug, project(), bundled cocos2d path, and adds the Cocos engine; see lines 26-54 and 58 onward.
- **VERIFIED** — Android project is proj.android (Gradle + external native build). Build files include proj.android/settings.gradle, build.gradle, app/build.gradle, app/jni/Android.mk and app/jni/Application.mk. Android launch files include app/src/org/cocos2dx/cpp/AppActivity.java and app/AndroidManifest.xml.
- **VERIFIED** — Android properties set compile SDK 34, minimum SDK 25, target SDK 34, NDK 25.2.9519653, and configured ABIs armeabi-v7a, arm64-v8a, x86. Evidence: proj.android/gradle.properties:21,24,27,37 and app/build.gradle:15,54. Signing configuration is present but its secrets were not read or recorded.
- **VERIFIED** — iOS/macOS project directory proj.ios_mac exists. Its build was not run.
- **UNKNOWN** — Exact installed CMake/Gradle/Java/NDK tool versions and the build currently used to make any APK; this inventory did not run a build or inspect local machine installations.

## Entry point and render configuration

- **VERIFIED** — AppDelegate::applicationDidFinishLaunching initializes Director/OpenGLView and starts KUpdateLayerVN::scene(); AppDelegate.cpp:76-83, 102-134, 179-185.
- **VERIFIED** — Requested OpenGL context attributes are RGBA 8/8/8/8, depth 24, stencil 8, multisample count 3. AndroidManifest.xml declares GLES 3.0 with required=false and landscape orientation (lines 14 and 28).
- **VERIFIED** — Director projection is 2D, depth testing is disabled, animation interval is 1/60 second, design resolution uses EXACT_FIT, and display statistics are disabled; AppDelegate.cpp:102-134.
- **PROBABLE** — 60 FPS is a requested frame interval, not a measured or guaranteed rate.
- **UNKNOWN** — Actual render backend selected on a particular phone/emulator, GPU/driver behavior, frame time, draw calls, overdraw, memory usage and thermal behavior. No device or emulator profiling was performed.

## Source modules

Classes has these top-level modules. Counts are filesystem entries under each module, including non-code files where present:

| Module | Files | C/C++ translation units | Headers | Evidence / role |
|---|---:|---:|---:|---|
| engine | 213 | 91 | 94 | File I/O, codecs, custom package readers, Lua, timers, containers |
| gamecore | 157 | 72 | 84 | Player, NPC, map, objects, skills, items, protocol and core game data |
| gamescene | 29 | 13 | 16 | Game world and scene/update layers |
| gameui | 174 | 87 | 87 | Game UI and shared UI state |
| ImageStore | 2 | 1 | 1 | Image storage/decoding bridge |
| manager | 7 | 4 | 3 | Client managers |
| network | 21 | 10 | 11 | Client networking |
| tools | 2 | 1 | 1 | Client utilities |
| vn | 131 | 64 | 65 | Vietnamese-specific scene/UI implementations |
| Root Classes files | 5 | — | — | AppDelegate and HelloWorldScene entry/sample files are present |

The CMake source list starts at CMakeLists.txt:58 and explicitly lists application files and these module trees.

## Cocos2d-x, extensions and third-party libraries

- **VERIFIED** — Bundled engine directories include cocos2d/cocos, cocos2d/extensions and cocos2d/external.
- **VERIFIED** — External directory contains Box2D, Bullet, Chipmunk, curl, FMOD, FreeType, GLFW, iconv, JPEG, PNG, OpenSSL, Recast, SQLite, TIFF, WebP, websockets, zlib, xxhash, xxtea, and other platform support libraries. Exact linked subset per Android ABI is UNKNOWN without build output.
- **VERIFIED** — Client root includes FMOD shared libraries; Resources also contains FMOD libraries. Exact FMOD SDK/runtime version was not established.
- **UNKNOWN** — Whether all bundled third-party modules are included in the shipping client or which versions are active in each target.

## Resource loading and management

- **VERIFIED** — CMake declares Resources as the game resource folder; CMakeLists.txt:47-54.
- **VERIFIED** — Custom package/file code exists in Classes/engine/KPakFile.cpp/.h, KPakList.cpp/.h, XPackFile.cpp/.h, KFile.cpp/.h, KFilePath.cpp/.h, KCodec.cpp/.h and KCodecLzo.cpp/.h. A downloader exists at Classes/engine/KDownLoadFile.cpp.
- **VERIFIED** — Package/index filenames present include Resources/package.ini, Resources/paklist.ini, data/data/package.ini, data/data/paklist.ini and data_cdn/data/paklist.ini. Their contents were not included in this report.
- **PROBABLE** — Client combines loose Cocos resources with legacy indexed/packed game resources. The PAK file headers and loader files support this; archive contents were not enumerated.
- **UNKNOWN** — Full cache ownership/cleanup lifecycle, exact decompression/encryption variants, update ordering, whether every listed index is active, and texture upload/release behavior.
- **BLOCKED** — Package and endpoint configuration values, signing material, logs and crash dumps were excluded to avoid disclosing secrets or personal data.

## Visual/game systems found in source

- **VERIFIED** — Map/world: Classes/gamescene/KUpdateLayer.cpp and vn/gamescence/KUpdateLayerVN.cpp; Classes/gamecore/KSubWorld.cpp, KSubWorldSet.cpp, KRegion.cpp and KMapMusic.cpp.
- **VERIFIED** — Characters/NPCs: Classes/gamecore/KPlayer.cpp, KNpc.cpp, KNpcAI.cpp, KNpcRes.cpp, KNpcTemplate.cpp and related resource/set files.
- **VERIFIED** — Objects/projectiles/skills: KObj.cpp/KObjSet.cpp, KMissle.cpp, KMissleRes.cpp, KSkillList.cpp, KSkillManager.cpp, KSkills.cpp, KSkillSpecial.cpp and related files.
- **VERIFIED** — Items, inventory, tasks, factions, trade, teams, PK and protocol processing have dedicated modules under Classes/gamecore (for example KItem.cpp, KInventory.cpp, KPlayerTask.cpp, KPlayerFaction.cpp, KPlayerTrade.cpp, KPlayerPK.cpp and KProtocolProcess.cpp).
- **VERIFIED** — Sprite/resource control code includes KSprControl.cpp; source scan also found Cocos SpriteFrameCache, SpriteBatchNode and TextureCache references.
- **VERIFIED** — Loose resources include Resources/TextureAtlas/default.png, Resources/Shaders/blur.fsh and blur.vsh, image/UI folders, font files and audio.
- **UNKNOWN** — Whether the shader pair is used in the active scene, atlas packing efficiency, all animation formats/frames, custom camera/culling policy, LOD, and exact particle/effect coverage. Symbol presence alone does not prove runtime use.
- **NOT TESTED** — No APK launch, scene transition, asset decode, rendering, device capture or regression test was run.

## Inventory and source limits

- Client Resources contains 947 files (78,035,592 bytes); client data contains 58 files (15,694,774 bytes). These are metadata counts, not proof that all referenced game assets are present.
- proj.android/app/assets has no files in the manifest; Android may package resources through other build rules, which were not executed.
- Source code line-level references to resource-like literals are reported in ASSET_REFERENCE_COVERAGE.md.
- No code or asset was changed; no APK was built or replaced.