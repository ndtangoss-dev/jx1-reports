# AMOLX-09 — Recover AMOLX-04 signing identity and install AMOLX-07

## Goal
Unblock the LDPlayer test immediately. Find the existing signing identity used for the installed AMOLX-04 APK, sign the already-built AMOLX-07 APK with that same identity, then update-install it while preserving app data and launch it.

User explicitly wants to proceed quickly. Do not ask for another approval for these non-destructive steps.

## Ground truth
- AMOLX-08 report: TEST_RESULTS/AMOLX-08-LDPLAYER-ADB-RUN-20261116.md
- LDPlayer 9 serial: emulator-5554
- Installed package: com.kull.jx1client
- Installed AMOLX-04 base APK was pulled and verified: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\build\amolx07-installed-before.apk
- AMOLX-04 SHA-256: D3C2B7DBEF476B495CEB19C0F1B70CE8BBE3C7E420302348C93EE863C07F4FC1
- New AMOLX-07 APK: C:\Jx1CocoV3\amolx-work\AMOLX-04-20261115\client\proj.android\app\build\outputs\apk\debug\jx1client-debug.apk
- AMOLX-07 SHA-256: 7FC4CCBC1B7DCFE1806E474888169239519B713D2C681A45F8E371389659E7B1
- Previous install failed only because signing certificates differ. No uninstall or data wipe occurred.

## Execute
1. Inspect the exact AMOLX-04 build/signing configuration, Gradle properties used by that project, and narrowly search relevant project/workspace build folders for existing Android signing keystores (.jks/.keystore) and their associated config. Do not scan unrelated user directories or entire disks.
2. Compare candidate certificate fingerprints against the installed AMOLX-04 APK certificate using Android build tools (apksigner verify --print-certs or equivalent). The matching certificate fingerprint is the acceptance criterion; filename alone is not proof.
3. Check whether the matching private key and required password are already available through the project's existing local signing configuration or environment. Never print, commit, upload, or include passwords/private key material in logs or the report. Do not ask user to paste secrets into chat.
4. If exact matching private key is available, sign a COPY of the AMOLX-07 APK with it. Verify resulting APK certificate fingerprint matches installed AMOLX-04 exactly, package name remains com.kull.jx1client, and APK integrity passes.
5. Update-install with adb install -r on the already-confirmed emulator-5554; do not uninstall, clear data, reset emulator, or change app identity. Confirm install success, launch app, collect filtered runtime/updater logs and screenshot. Do not connect to game server yet.
6. If exact private key/password cannot be found quickly, stop and report exactly what was checked and what is missing. Do not generate a new key and pretend it matches; do not modify installed app or its data. Do not switch to a separate application ID in this task.
7. Do not rebuild source unless signing the existing APK proves impossible for a concrete technical reason. Do not modify Cocos client, server, VM, CDN, firewall, Tailscale, ports, or network.
8. Create one report TEST_RESULTS/AMOLX-09-SIGN-AND-INSTALL-20261116.md, commit and push. State matching certificate fingerprints (fingerprints are safe), signing outcome, install/launch result, updater state, log/screenshot paths, and next blocker. No secrets.

## Completion
- DONE only if matching certificate is verified, update-install succeeds, and app launch/runtime observation is recorded.
- PARTIAL/BLOCKED if signing key is unavailable or install/launch fails.