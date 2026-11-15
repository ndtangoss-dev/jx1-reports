# AMOLX-08 — Run the already-prepared LDPlayer ADB smoke test

## Objective
Immediately execute the already-prepared AMOLX-07 ADB smoke-test script outside the sandbox so the newly built AMOLX APK is installed and launched on the user's running LDPlayer 9. The user has explicitly approved this operation, including running ADB outside the sandbox.

## Known state — do not repeat
- AMOLX-07 report: `TEST_RESULTS/AMOLX-07-ASSET-UPDATER-GAMEPLAY-20261116.md`
- Existing script: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client\build\run-amolx07-smoke.ps1`
- New APK: `C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client\proj.android\app\build\outputs\apk\debug\jx1client-debug.apk`
- Expected package: `com.kull.jx1client`
- Expected APK SHA-256: `7FC4CCBC1B7DCFE1806E474888169239519B713D2C681A45F8E371389659E7B1`
- LDPlayer 9 ADB serial was previously confirmed in AMOLX-05 as `device`.
- AMOLX-07 build succeeded. Do not rebuild.
- Previous sandbox attempts to run the external ADB script timed out on approval; user has now explicitly approved. Do not ask again.

## Execution
1. Read only the existing smoke-test script and inspect its exact commands. Do not perform a broad audit.
2. Verify the APK exists and its SHA-256 matches the expected value above.
3. Identify the already-confirmed LDPlayer 9 device using ADB. If multiple devices or ambiguity exists, stop and report the ambiguity; do not guess.
4. Before installation, inspect the installed package. Proceed only if it is the expected AMOLX package `com.kull.jx1client`. If it is absent, install the APK normally. If a different package/version or app identity is present, stop without uninstalling or altering data.
5. Install/update the APK using ADB in a way that preserves existing app data. Never run uninstall, clear/clear-data, wipe, factory reset, or emulator reset.
6. Launch the app. Capture the relevant startup/updater logs and screenshot if available. Wait only long enough to observe the updater's result; do not leave an unbounded process running.
7. Do not connect to the JX1 server in this task. Do not change server, VM, CDN process, firewall, Tailscale, port forwarding, credentials, or network settings.
8. Do not edit source, rebuild, copy assets, create manifests, or repeat AMOLX-03 through AMOLX-07 diagnosis.
9. If a command fails, diagnose only that failure and retry a safe equivalent once. Do not repeatedly request approval; the user has approved this scoped ADB operation.
10. Produce one concise final report at `TEST_RESULTS/AMOLX-08-LDPLAYER-ADB-RUN-20261116.md` and commit/push it. Include device serial (redact unrelated identifiers), APK hash verification, package state before/after, install/launch result, updater progress and sanitized logs, screenshot path if any, and exact next blocker. Do not include credentials or tokens.

## Safety boundaries
- No destructive app-data operation.
- No server or VM operations.
- No Cocos canonical client edits.
- No broad environment/config/model preflight.
- Stop if the target emulator/package cannot be identified unambiguously.

## Completion status
Use DONE only if the APK is installed and launched and the observed result is recorded. Use PARTIAL/BLOCKED if any step cannot be completed. Do not claim updater/login/gameplay success unless directly observed.
