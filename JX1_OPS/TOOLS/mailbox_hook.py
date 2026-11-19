#!/usr/bin/env python
"""Hook PostToolUse/UserPromptSubmit (Q-40): toi da 10 phut/lan, git fetch jx1-ops, so so thu trong CHO-SONNET.md voi lan doc cuoi
(tep trang thai cuc bo ngoai kho), co thu moi thi nhac doc DUNG phan moi bang 1 dong. Luon nhac mo dau 'Bam dai vuong,'. Loi bat ky: im lang."""
import json, os, re, subprocess, sys, time

_B = os.environ.get('JX1_SONNET', 'A').upper() == 'B'
WT = r'D:\JX-wt\SONNET-B' if _B else r'D:\jx1-ops-wt'
STATE = r'D:\JX-tools\mailbox_state_B.json' if _B else r'D:\JX-tools\mailbox_state.json'
PERIOD = 600


def main():
    try:
        st = json.load(open(STATE, encoding='utf-8'))
    except Exception:
        st = {'last': 0, 'read': 0, 'check': 0}
    now = time.time()
    if now - st.get('check', 0) < PERIOD:
        return
    st['check'] = now
    subprocess.run(['git', '-C', WT, 'fetch', '-q', 'origin', 'jx1-ops'], timeout=40, capture_output=True)
    txt = subprocess.run(['git', '-C', WT, 'show', 'origin/jx1-ops:JX1_OPS/HOP-THU/' + ('CHO-SONNET-B.md' if os.environ.get('JX1_SONNET', 'A').upper() == 'B' else 'CHO-SONNET.md')], timeout=20,
                         capture_output=True).stdout.decode('utf-8', 'replace')
    isb = os.environ.get('JX1_SONNET', 'A').upper() == 'B'
    # #250: nhan ca "## #N ..." / "## #B-N ..." va kieu cu "## ... Thu #N"
    pat = r'^## (?:#B-(\d+)|.*?Th[uư] #B-(\d+))' if isb else r'^## (?:#(\d+)|.*?Th[uư] #(\d+))'
    nums = [int(a or b) for a, b in re.findall(pat, txt, re.M)]
    top = max(nums) if nums else 0
    urgent = 'CẦN-CHAT-GẤP' in txt[txt.rfind('## '):] if txt else False
    new = top > st.get('read', 0)
    json.dump(st, open(STATE, 'w', encoding='utf-8'))
    if new:
        msg = ('NHAC JX1: co thu moi trong CHO-SONNET.md (den #%d, da doc den #%d). git pull jx1-ops, doc CHI phan moi, ghi "Da doc den #%d luc HH:MM" vao TU-SONNET.md, '
               'roi cap nhat %s (read). %s' % (top, st.get('read', 0), top, STATE, 'CO [CAN-CHAT-GAP]: xu ly truoc. ' if urgent else ''))
    else:
        return
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': msg + ' Moi khoi van ban gui chu may mo dau "Bam dai vuong,".'}}))


try:
    main()
except Exception:
    pass
