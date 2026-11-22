#!/usr/bin/env python
"""Hook UserPromptSubmit: do % ngu canh phien nay, in 1 dong (nhu bai Hai Dang).
Doc transcript_path tu stdin (JSON cua Claude Code), lay usage cua tin tro ly cuoi.
Cua so = JX1_CTX_WINDOW (mac dinh 1000000); nguong nen = CLAUDE_AUTOCOMPACT_PCT_OVERRIDE (mac dinh 30). Loi bat ky -> im lang, khong chan."""
import json, os, sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    d = json.loads(sys.stdin.read() or '{}')
    p = d.get('transcript_path')
    win = int(os.environ.get('JX1_CTX_WINDOW', '1000000'))
    thr = int(os.environ.get('CLAUDE_AUTOCOMPACT_PCT_OVERRIDE', '30'))
    used = 0
    if p and os.path.exists(p):
        for line in open(p, encoding='utf-8', errors='replace').read().splitlines()[-400:]:
            try:
                u = json.loads(line).get('message', {}).get('usage')
            except Exception:
                continue
            if u:
                used = (u.get('input_tokens', 0) + u.get('cache_read_input_tokens', 0)
                        + u.get('cache_creation_input_tokens', 0))
    if used:
        print('[Hook do context] Context phien nay: %d%% (%s / %s token). Nguong compact: %d%%' % (
            round(used * 100 / win), format(used, ',').replace(',', '.'), format(win, ',').replace(',', '.'), thr))
except Exception:
    pass
