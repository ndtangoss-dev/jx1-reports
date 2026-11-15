# AMOLX-10 — Fix manifest 404 and reach the login screen

## Objective
Remove the current AMOLX updater blocker and get the installed AMOLX client to the login screen as quickly as possible. Work only on the AMOLX copy and an isolated/test CDN location. Do not disturb the working Cocos client or live CDN.

## Verified starting point
- AMOLX-09 report: TEST_RESULTS/AMOLX-09-SIGN-AND-INSTALL-20261116.md
- APK is already installed on LDPlayer 9 emulator-5554 and launches.
- AMOLX-04 signing identity was recovered; the signed AMOLX-07 APK updated successfully while preserving app data.
- Runtime evidence: HEAD request for data/paklist_vn.ini returns HTTP 404 three times; updater aborts with state=3.
- Runtime log: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx09-runtime-filtered.log
- Screenshot: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx09-screen.png
- Cocos CDN baseline previously reported at C:\Jx1CocoV3\data_cdn; Cocos client requests data/paklist.ini. Do not alter or overwrite its live files.

## Work — one focused execution
1. Read AMOLX-09 report and inspect only the AMOLX manifest URL/configuration and the existing local CDN directory layout needed to explain the exact 404. Do not repeat broad audits or re-check server/VM/network state.
2. Determine whether the 404 is caused by wrong manifest filename, wrong base URL/path, or missing manifest on the configured test origin. Prove the exact cause from source/config/files and a targeted request/log; do not guess.
3. Preferred fix: change only the AMOLX copy to request the manifest that is actually present and compatible, OR create an AMOLX-specific manifest at an isolated staging root. Do not change Cocos source or its canonical data_cdn contents. Do not modify the currently serving Cocos CDN configuration, service, or live files.
4. Before using any Cocos PAK, verify the AMOLX manifest's required filenames and compatibility. Do not fabricate a complete manifest, copy a large asset set, or claim compatibility based only on matching names. If a minimal compatible set is proven, stage only that set in an isolated AMOLX test root.
5. Rebuild only the AMOLX copy if source/config changes are needed. Sign the resulting APK using the already-verified AMOLX-04 signing identity at C:\Users\PC\.android\debug.keystore. Do not expose its password/private key. Verify certificate fingerprint matches AMOLX-04.
6. Install/update on the already-confirmed LDPlayer 9 emulator-5554 with adb install -r, preserving app data. Launch and capture updater logs/screenshot. Do not connect to the JX1 game server yet. Target is to pass updater and reach login screen; if that cannot be done without touching live CDN/server, stop at the precise blocker.
7. If a safe manifest/path correction requires editing the live Cocos CDN, restarting its service, changing server/VM/firewall/Tailscale/ports, or altering Cocos data, DO NOT do it. Instead use an isolated test origin only if its address and serving mechanism are already explicitly grounded in existing project configuration and can be started without affecting Cocos; otherwise report the exact missing prerequisite.
8. Do not uninstall, clear app data, reset emulator, alter package identity, rebuild the Cocos client, or perform broad environment/model/config checks.
9. Produce one report TEST_RESULTS/AMOLX-10-MANIFEST-404-LOGIN-20261116.md, commit and push. Include proven 404 cause, exact AMOLX-only changes, build/sign/install result, updater progress, whether login screen was reached, and sanitized log/screenshot paths.

## Completion
- DONE only if updater passes and login screen is visibly reached with evidence.
- PARTIAL if manifest is fixed but asset download or another stage blocks.
- BLOCKED if safe resolution requires a prohibited live CDN/server change or a missing prerequisite.

## User priority
Speed matters: do not create intermediate reports, do not ask about ordinary safe steps, and do not repeat completed diagnostics. Execute the smallest end-to-end path and report once.