# AMOLX-10 — Fix updater, connect to JX1, and verify real gameplay

## Objective — gameplay test, not merely app launch/login
Deliver a usable AMOLX client session on the existing JX1 server: pass updater, log in, select a character, enter the world/map, and perform basic gameplay actions. A login screen alone is NOT completion.

Work only on the AMOLX copy and an isolated/test asset staging area. Preserve the working Cocos client, live CDN, and current JX1 server/VM.

## Verified starting point
- AMOLX-09 report: TEST_RESULTS/AMOLX-09-SIGN-AND-INSTALL-20261116.md
- APK is installed on LDPlayer 9 emulator-5554 and launches.
- AMOLX-04 signing identity recovered; signed AMOLX-07 updated successfully while preserving app data.
- Runtime evidence: HEAD request for data/paklist_vn.ini returns HTTP 404 three times; updater aborts with state=3.
- Runtime log: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx09-runtime-filtered.log
- Screenshot: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx09-screen.png
- Cocos CDN baseline previously reported at C:\Jx1CocoV3\data_cdn; Cocos client requests data/paklist.ini. Do not alter or overwrite its live files.
- Historical Cocos client test successfully logged into the cloned JX1 server over the existing Tailscale/forwarder route. Reuse only exact endpoints/ports already documented in project reports/config; never guess.

## Required end-to-end work
1. Read AMOLX-09 report and inspect only AMOLX manifest URL/configuration and the existing local CDN directory layout needed to explain the exact 404. Do not repeat broad audits or re-check server/VM/network state.
2. Prove whether 404 is caused by wrong manifest filename, wrong base URL/path, or missing manifest on configured origin. Use source/config/files and a targeted request/log; do not guess.
3. Fix only the AMOLX copy to request a manifest that is actually present and compatible, OR create an AMOLX-specific manifest at an isolated staging root. Never change Cocos source, canonical data_cdn files, or the live Cocos CDN service/configuration.
4. Verify manifest entries and PAK compatibility before using any Cocos assets. Do not fabricate a manifest, copy a large asset set, or claim compatibility from filenames alone. Stage only proven compatible required assets in an isolated AMOLX test root.
5. Rebuild only AMOLX if required. Sign with the already-verified AMOLX-04 signing identity at C:\Users\PC\.android\debug.keystore. Never expose password/private key. Verify certificate fingerprint matches AMOLX-04.
6. Install/update on emulator-5554 using adb install -r, preserving app data. Launch and verify updater completes and assets load.
7. Once updater has passed, connect to the existing JX1 server using only the exact endpoint/port and route already grounded in prior JX1 reports or AMOLX/Cocos configuration. Reuse the existing tested route. Do not scan ports, guess addresses, or change VM/server/firewall/Tailscale/forwarder/CDN settings.
8. Continue through login, server selection, character selection, and enter the world/map. If login fails, inspect AMOLX client logs and compare with known-good Cocos protocol/config evidence. Fix only AMOLX-side incompatibilities that can be established safely.
9. In-world, perform and record at least: character movement, one basic attack against a monster or target, one skill action if available, and one NPC/interactable interaction if available. Capture screenshots and sanitized logs. Do not claim an action succeeded unless visibly/logically confirmed.
10. If any step would require changing the live Cocos CDN, running/restarting server EXEs, modifying VM/SQL data, changing firewall/Tailscale/ports/forwarder, or risking existing game data, stop and report the exact blocker rather than making that change.
11. Do not uninstall, clear app data, reset emulator, alter package identity, rebuild Cocos, or run broad environment/model/config checks.
12. Produce one report TEST_RESULTS/AMOLX-10-GAMEPLAY-TEST-20261116.md, commit and push. Include the proven 404 cause, AMOLX-only changes, build/sign/install, updater completion, connection/login result, map/character entry, each gameplay action result, screenshots, sanitized logs, and remaining blockers.

## Completion criteria
- DONE only when the client enters the game world/map and at least movement plus one attack are verified. Record skill/NPC results too, if available.
- PARTIAL if updater/login succeeds but world entry or gameplay actions fail.
- BLOCKED if safe completion requires a prohibited live server/CDN/network change or a missing prerequisite.
- A splash screen or login screen is not completion.

## User priority
Speed matters. Do not create intermediate reports, ask about ordinary safe steps, repeat completed diagnostics, or stop at login. Execute the smallest safe end-to-end path and report once.