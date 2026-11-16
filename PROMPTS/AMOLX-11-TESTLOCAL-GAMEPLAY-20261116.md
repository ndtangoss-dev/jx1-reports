# AMOLX-11 — Use testlocal and complete an in-game smoke test

## Objective
Continue from the currently running AMOLX session on LDPlayer 9. The user reports Codex has remained at the AMOLX login screen for a long time. Do not wait passively: inspect the current screen/logs, use the test account below, log in, and proceed into the game world to test gameplay.

## User-provided test identity
- Username: testlocal
- The supplied screenshot is from the Cocos V3 client and confirms the username only.
- The password field in that screenshot is masked; the password is NOT known from the image. Do not guess, infer, print, or attempt password cracking.
- First inspect whether AMOLX already has a saved/pre-filled password for testlocal in its own login UI or its own app storage. If a password is already populated in AMOLX, use it without revealing it in logs or screenshots.
- Do not extract credentials from Cocos V3 or unrelated applications. If AMOLX has no usable saved password, stop and ask the user for the test password; do not waste time retrying guesses.

## Starting context
- Continue using the already-installed AMOLX package com.kull.jx1client on LDPlayer 9 serial emulator-5554.
- AMOLX-09 confirmed the app launches and the updater previously reached the server-selection UI after the signing issue was fixed.
- User manually tapped all three displayed 'Server Test 1' entries and each returned 'Không thể kết nối tới máy chủ...'. The three labels may be duplicate display names; inspect actual endpoints rather than assuming they are three separate servers.
- The user now reports Codex has stayed on the AMOLX login screen for a long time. Check current state before doing anything else.
- Existing Cocos JX1 client has previously logged into the cloned JX1 server through the documented Tailscale/forwarder route. Reuse only exact endpoint and route values already documented in repository reports/config. Do not guess or scan.

## Execution steps
1. Inspect current LDPlayer screen and recent AMOLX logs. Determine whether the app is genuinely waiting for user input, blocked on a network request, or stuck due to an error. Do not leave it idle for an arbitrary long period.
2. If on login UI, enter username testlocal. Use an already-populated AMOLX password only if the field is visibly/populated in AMOLX or available through AMOLX's own normal saved-login mechanism. Never log or disclose the password.
3. Submit login once. Observe the exact response and sanitized logs. If authentication fails, do not repeatedly retry; record the error and ask the user for the correct password only if required.
4. If server selection appears, inspect the three records' actual name/ID/IP/port/protocol from the AMOLX config/source and compare with the previously verified Cocos route. Identify the exact JX1 test endpoint using existing evidence. Do not assume identical labels mean identical endpoints.
5. If all three entries are duplicate references to the same endpoint, use the verified endpoint only. Do not modify server list or delete entries in this task.
6. Continue through character selection and enter the actual game map. Do not stop at login or server selection.
7. Once in-world, verify and record: character movement, one basic attack against a monster/target, one skill if available, and one NPC/interactable action if available. Capture screenshots and sanitized logs.
8. If connection fails, diagnose from the actual error stage (DNS/TCP/connect/handshake/auth/protocol). Compare AMOLX endpoint and protocol behavior with existing Cocos evidence. Make only narrowly scoped AMOLX-side fixes supported by evidence.
9. Do not restart/stop server EXEs, modify VM/SQL data, firewall, Tailscale, port forwarding, CDN service/live files, or the canonical Cocos client. Do not clear app data, uninstall, reset emulator, or change account password.
10. Do not expose credentials, tokens, private keys, or full sensitive endpoint details in screenshots/logs/reports. Sanitize report output.
11. Create one report TEST_RESULTS/AMOLX-11-TESTLOCAL-GAMEPLAY-20261116.md, commit and push. Include initial stuck state, whether AMOLX had a saved password (yes/no only), login result, selected endpoint reference (redacted as appropriate), world-entry result, gameplay action results, screenshot/log paths, and precise blocker if not completed.

## Completion criteria
- DONE only if testlocal enters the game world and movement plus one attack are verified.
- PARTIAL if authentication or world entry succeeds but gameplay validation is incomplete.
- BLOCKED if the password is unavailable, authentication fails, or safe connection requires a prohibited server/network change.
- A login screen or server-selection screen is not a gameplay test.

## Priority
Proceed immediately and efficiently. No repeated audits, no passive waiting, no guessed credentials, no unnecessary questions. Report once with evidence.