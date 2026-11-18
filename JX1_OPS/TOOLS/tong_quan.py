#!/usr/bin/env python
"""TONG QUAN (#118, L9): nguoi duy nhat quan tieu yeu. Moi lan chay = mot vong, Task Scheduler goi moi 3 phut (JX-TongQuan).
Moi vong: xet song/im/treo/chet (#117), commit ho khi xong, chay lai khi chet (cho 2/5/15 phut, toi da 3 lan),
giao viec status=ready, rai khoa (<=3 tieu yeu/khoa, het cho thi ghi CAN KHOA MOI), sinh STATE/TIEU-YEU.md va TIEN-DO.md.
Khong push (PM/guard commit file STATE). Khong doc gia tri khoa, chi ten khoa. Chay: python -I TOOLS/tong_quan.py [--dry]"""
import shutil, glob, json, os, re, subprocess, sys, time

# #165: chay bang pythonw (khong console): stdout/stderr = None -> chuyen vao tep; moi lenh con them CREATE_NO_WINDOW
if sys.stdout is None or sys.stderr is None:
    try:
        _lg = open(r'D:\JX-wt	ong_quan\stdout.log', 'a', encoding='utf-8', errors='replace')
    except OSError:
        _lg = open(os.devnull, 'w')
    sys.stdout = sys.stdout or _lg
    sys.stderr = sys.stderr or _lg
if os.name == 'nt':
    _Popen = subprocess.Popen

    class _NoWinPopen(_Popen):
        def __init__(self, *a, **k):
            k['creationflags'] = k.get('creationflags', 0) | 0x08000000   # CREATE_NO_WINDOW
            super().__init__(*a, **k)
    subprocess.Popen = _NoWinPopen

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
WT = r'D:\JX-wt'
KEYS = r'C:\Users\PC\.jx1keys'
GD = os.path.join(WT, 'tong_quan')
MAXKEY = 3  # #205 (Q-57): buoc 1 (2->3), quan sat >=5 phut. Hoan tac: khoi phuc tong_quan.py.bak-205 (MAXKEY = 2, MAXALL = 10)
# #183 (Q-51): K5, K6 toi da 2 viec; viec moi xoay sang K4, K3 truoc. Hoan tac: bo 2 dong KEY_CAP/KEY_ORDER va 2 cho dung chung trong pick_key
KEY_CAP = {'JX-K5': 2, 'JX-K6': 2}
KEY_ORDER = ['JX-K4', 'JX-K3', 'JX-K2', 'JX-K6', 'JX-K5']
HOLD_H = (17, 19)   # #183: viec moi khong gap (priority >= 2) khong giao trong khung 17h-19h; viec chay lai khi chet khong bi chan
MAXALL = 15  # #205: tran dong thoi (buoc 1)
WAITS = (0, 0, 0)       # #132: chet -> chay lai o vong ke (<=2 phut); toi da 3 lan loi cua viec roi CHET-BO
IM, TREO = 20, 60       # phut im: song / im-nhung-song / treo
DRY = '--dry' in sys.argv
os.makedirs(GD, exist_ok=True)


def now():
    return time.time()


def ps(cmd):
    r = subprocess.run(['powershell', '-NoProfile', '-Command', cmd], capture_output=True, text=True, timeout=90)
    return r.stdout


def front(p):
    try:
        s = open(p, encoding='utf-8').read()
    except OSError:
        return None
    m = re.match(r'---\s*\n(.*?)\n---', s, re.S)
    if not m:
        return None
    d = {}
    for ln in m.group(1).splitlines():
        k, _, v = ln.partition(':')
        if _:
            d[k.strip()] = v.strip().strip('"')
    return d


def load(p, default):
    try:
        return json.load(open(p, encoding='utf-8'))
    except (OSError, ValueError):
        return default


def save(p, v):
    json.dump(v, open(p, 'w', encoding='utf-8'))


def read_log(p, n=60000):
    try:
        b = open(p, 'rb').read()[-n:]
    except OSError:
        return ''
    return b.replace(b'\x00', b'').decode('utf-8', 'ignore')


def newest(wt):
    """mtime moi nhat cua file trong worktree (bo .git)"""
    best = 0
    for d, dirs, files in os.walk(wt):
        dirs[:] = [x for x in dirs if x != '.git']
        for f in files:
            try:
                best = max(best, os.path.getmtime(os.path.join(d, f)))
            except OSError:
                pass
    return best


def mt(p):
    try:
        return os.path.getmtime(p)
    except OSError:
        return 0


def done_exit(i):
    try:
        t = open(os.path.join(WT, i + '.done'), 'rb').read().replace(b'\x00', b'').decode('utf-8', 'ignore')
    except OSError:
        return None
    m = re.search(r'exit=(-?\d+)', t)
    return int(m.group(1)) if m else -1


def keys():
    return sorted(os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(KEYS, 'JX-K*.txt')))


def pick_key(assign, alive_ids):
    alive_ids = list(alive_ids)
    use = {}
    for i in alive_ids:
        k = assign.get(i)
        if k:
            use[k] = use.get(k, 0) + 1
    if len(alive_ids) >= MAXALL:
        return None
    ks = [k for k in keys() if use.get(k, 0) < KEY_CAP.get(k, MAXKEY)]
    return min(ks, key=lambda k: (KEY_ORDER.index(k) if k in KEY_ORDER else 9, use.get(k, 0))) if ks else None


def model_of(i):
    m = load(os.path.join(GD, 'model.json'), {}).get(i)
    if m:
        return m
    try:
        return 'astra' if i in open(os.path.join(GD, 'astra.txt')).read().split() else 'sol'
    except OSError:
        return 'sol'


def pid_of(i):
    try:
        return int(re.sub(r'\D', '', open(os.path.join(WT, i + '.pid'), 'rb').read().replace(bytes([0]), b'').decode('utf-8', 'ignore')) or 0)
    except (OSError, ValueError):
        return 0


def pid_alive(pid):
    if pid <= 0:
        return None
    out = subprocess.run(['tasklist', '/FI', 'PID eq %d' % pid, '/NH'], capture_output=True, text=True).stdout
    if str(pid) in out:
        return True
    return False if 'No tasks' in out else None   # #145: ket qua rong/la -> khong ket luan


def pid_txt(i, running):
    p = pid_of(i)
    a = pid_alive(p)
    return '-' if a is None else ('%d song' % p if a else '%d mat' % p)


def cho_token(tail):
    """#147: da gui yeu cau (turn.started), chua co su kien item/loi nao sau do."""
    k = tail.rfind('"type":"turn.started"')
    if k < 0:
        return False
    rest = tail[k:]
    return '"type":"item.' not in rest and 'turn.failed' not in rest and '"type":"error"' not in rest


def ttft_txt(i):
    v = load(os.path.join(GD, 'ttft.json'), {}).get(i)
    return '-' if v is None else '<=%d' % v


def astra_ok(d, i):
    # #164: astra bi xingchi tra 404 (18/11) -> khong chuyen sang astra nua; bat lai bang cach doi dong tren
    # return str(d.get('astra', '')).lower() == 'ok' or i.startswith('R-')   # #143: viec doc/viet bao cao
    return False


def set_astra(i):
    """#143: dua viec vao astra.txt + dan nhac ghi bao cao."""
    ap = os.path.join(GD, 'astra.txt')
    try:
        cur = open(ap).read().split()
    except OSError:
        cur = []
    if i not in cur:
        open(ap, 'a').write(i + chr(10))
    pf = os.path.join(WT, i + '.prompt.txt')
    try:
        t = open(pf, encoding='utf-8').read()
        if 'KET THUC bang viec ghi bao cao' not in t:
            open(pf, 'a', encoding='utf-8').write(chr(10) + 'KET THUC bang viec ghi bao cao vao JX1_OPS/REPORTS/%s.md; khong ghi thi coi nhu chua xong. Lam tung buoc nho, moi buoc mot cau hoi ro, ghi bao cao som roi bo sung.' % i + chr(10))
    except OSError:
        pass


def report_empty(i):
    r = os.path.join(WT, i, 'JX1_OPS', 'REPORTS', i + '.md')
    try:
        return os.path.getsize(r) < 200
    except OSError:
        return True


RAMP = [0]


def ramp_ok(sched):
    """#145.3: 1 viec -> song >3 phut -> 3 viec -> toi tran. Moi vong toi da 1 viec neu chua co viec astra nao song >3 phut, nguoc lai 3."""
    old = 0
    for x, st in sched.items():
        if st == 'Running' and model_of(x) == 'astra':
            pf = os.path.join(WT, x + '.pid')
            if mt(pf) and now() - mt(pf) > 180:
                old += 1
    return RAMP[0] < (3 if old else 1)


def task_field(i, name, default=''):
    try:
        t = open(os.path.join(ROOT, 'TASKS', i + '.md'), encoding='utf-8-sig').read().split('---')[1]
        m = re.search(r'(?m)^%s:\s*(.+?)\s*$' % name, t)
        return m.group(1).strip(chr(34) + chr(39)) if m else default
    except (OSError, IndexError):
        return default


def hold_now(i):
    """#183: True = viec moi khong gap, dang trong khung 17h-19h -> de lai vong sau."""
    h = time.localtime().tm_hour
    if not (HOLD_H[0] <= h < HOLD_H[1]):
        return False
    return task_field(i, 'priority', '3') not in ('0', '1')


def run_launch(i, key):
    env = dict(os.environ, JX_CODEX_KEY=key)
    eff = task_field(i, 'effort', '')   # #183: effort: high trong file task = thu high thay max cho viec doc-tom
    if eff in ('low', 'medium', 'high', 'max'):
        env['JX_CODEX_EFFORT'] = eff
    args = ['powershell', '-NoProfile', '-File', os.path.join(ROOT, 'TOOLS', 'chay_codex.ps1'), '-Id', i]
    try:   # #113.3: viec ghi trong astra.txt chay bang gpt-6-astra (thu thay sol khi sol loi Chat Completions)
        if i in open(os.path.join(GD, 'astra.txt')).read().split():
            args += ['-Model', 'gpt-6-astra']
    except OSError:
        pass
    r = subprocess.run(args,
                       env=env, cwd=ROOT, capture_output=True, text=True, timeout=120)
    if r.returncode == 0:
        mp = os.path.join(GD, 'model.json')
        m = load(mp, {})
        m[i] = 'astra' if '-Model' in args else 'sol'
        save(mp, m)
    return r.returncode == 0


def ensure_worktree(i):
    wt = os.path.join(WT, i)
    if not os.path.isdir(wt):
        repo = os.path.dirname(ROOT)
        subprocess.run(['git', '-C', repo, 'worktree', 'add', '-B', 'task/' + i, wt, 'jx1-ops'], capture_output=True)
        # task file phai co trong worktree
        src = os.path.join(ROOT, 'TASKS', i + '.md')
        dst = os.path.join(wt, 'JX1_OPS', 'TASKS', i + '.md')
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            open(dst, 'wb').write(open(src, 'rb').read())
    pf = wt + '.prompt.txt'
    if not os.path.exists(pf):
        open(pf, 'w', encoding='utf-8').write(
            'Ban la worker Codex cua du an JX1. Lam dung task %(i)s: doc file JX1_OPS/TASKS/%(i)s.md trong worktree D:\\JX-wt\\%(i)s (nhanh task/%(i)s), lam theo Muc tieu, Nguon can doc, Pham vi. Doc truoc JX1_OPS/DESIGN/CHUAN-BAO-CAO.md. '
            'Dung skill trong .agents/skills (jx1-retrofit, jx1-read-server, jx1-read-client, jx1-parameters, jx1-knowledge, jx1-report). Chi sua dung vung_file. Khong sua ma nguon, khong chay VM/exe/mang, khong doi ket luan cu. '
            'Viet bao cao JX1_OPS/REPORTS/%(i)s.md, ghi muc Ket qua cuoi file task. Khong ghi mat khau/khoa. Tai lieu tieng Viet co dau.\n\n'
            'NHIP: ghi file D:\\JX-wt\\%(i)s.nhip (gio, buoc dang lam, %% uoc tinh) o moi moc lon: bat dau, moi phan xong, sap xong. Khong can commit: Tong quan commit ho.\n'
            'TIEP TUC: truoc khi lam, xem git status trong worktree; file da co thi KHONG lam lai, chi lam tiep phan con thieu.\n'
            'TIET KIEM TOKEN (Q-51): lap danh sach tep can doc tu muc Nguon cua task roi chi doc cac tep do; KHONG quet ca thu muc lon (khong liet ke de quy Folder/, SwordOnline/, D:\\JX-wt\\ khi chua loc ten); moi lan doc toi da ~400 dong (offset/limit hoac tim chuoi), tep lon doc tung doan; khong doc lai tep da doc; cat gon ket qua lenh.\n' % {'i': i})
    return wt


def sonnet_song():
    """#197: mtime lich su phien Claude Code + commit cuoi cua Sonnet + RAM; khong goi claude."""
    import ctypes, csv, io
    now = time.time()
    fs = glob.glob(os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'C--Jx1CocoV3', '*.jsonl'))
    last = max([os.path.getmtime(f) for f in fs] or [0])
    cm = 0
    try:
        r = subprocess.run(['git', '-C', ROOT, 'log', '-1', '--grep=Sonnet', '--format=%ct', 'origin/jx1-ops'],
                           capture_output=True, text=True, timeout=30)
        cm = int(r.stdout.strip() or 0)
    except Exception:
        pass
    try:
        nt = os.path.getmtime(os.path.join(ROOT, 'HOP-THU', 'NHIP-TIM.md'))  # #200: cho_thu.py dang cho = con song
    except Exception:
        nt = 0
    last = max(last, nt, cm)
    mins = (now - last) / 60 if last else 9999
    lv = 'SONG' if mins < 10 else ('IM' if mins <= 30 else 'TREO')
    hm = lambda t, f: time.strftime(f, time.localtime(t)) if t else '?'

    class MS(ctypes.Structure):
        _fields_ = [('l', ctypes.c_ulong), ('ml', ctypes.c_ulong)] + [(n, ctypes.c_ulonglong) for n in ('tp', 'ap', 'tpf', 'apf', 'tv', 'av', 'ae')]
    m = MS()
    m.l = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    gb = lambda x: x / 2**30
    top = []
    try:
        o = subprocess.run(['powershell', '-NoProfile', '-Command',
                            'Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 5 | ForEach-Object { $_.ProcessName + "," + $_.WorkingSet64 }'],
                           capture_output=True, text=True, timeout=60).stdout
        for ln in o.splitlines():
            n, _, v = ln.strip().partition(',')
            if v.isdigit():
                top.append((int(v) / 2**30, n))
    except Exception:
        pass
    top = sorted(top, reverse=True)[:5]
    return ('Sonnet: hoạt động cuối %s (%d phút trước); commit cuối %s; mức %s (<10 SONG / 10-30 IM / >30 TREO). Cập nhật %s\n'
            'RAM%s: trống %.1f/%.1f GB (%.0f%%). Top 5 bộ nhớ: %s') % (
        hm(last, '%H:%M:%S'), mins, hm(cm, '%H:%M'), lv, time.strftime('%H:%M:%S'),
        ' RAM-THAP (<8 GB hoac <15%, #199/#200)' if (gb(m.ap) < 8 or 100.0 * m.ap / m.tp < 15) else '', gb(m.ap), gb(m.tp), 100.0 * m.ap / m.tp, '; '.join('%s %.2f GB' % (n, v) for v, n in top))


def ld_dong():
    """#200: neu co cua so LDPlayer dang hien thi them dong LD-HIEN (chi doc, xem kiem_ld.py)."""
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import kiem_ld
        r = kiem_ld.ld_hien()
        return ('\nLD-HIEN: %d (%s)' % (len(r), '; '.join(t or c for t, c in r[:3]))) if r else ''
    except Exception as e:
        return '\nLD-HIEN: loi kiem (%s)' % type(e).__name__


def main():
    tasks = {}
    for p in glob.glob(os.path.join(ROOT, 'TASKS', '*.md')):
        if os.path.basename(p).startswith('_'):
            continue
        d = front(p)
        if d and d.get('id'):
            tasks[d['id']] = d
    sched = {}
    for ln in ps("Get-ScheduledTask -TaskName 'JX-codex-*' | ForEach-Object { $_.TaskName + '=' + $_.State }").splitlines():
        n, _, st = ln.strip().partition('=')
        if n:
            sched[n.replace('JX-codex-', '')] = st
    assign = load(os.path.join(GD, 'khoa.json'), {})
    lan = load(os.path.join(GD, 'lan.json'), {})
    rows = []
    notes = []
    alive_ids = [i for i, s in sched.items() if s == 'Running']
    # #123: cau dao 3 trang thai. DONG -> MO (>=4 loi dich vu/10 phut: ngung giao, moi 10 phut thu 1 viec) -> NUA-MO (thu song >3 phut thi DONG)
    brp = os.path.join(GD, 'breaker.json')
    br = load(brp, {'s': 'dong', 'since': 0, 'probe_at': 0, 'probe_id': '', 'probe_start': 0, 'warn': 0})
    recent = 0
    for f in glob.glob(os.path.join(WT, '*.done')):
        if now() - mt(f) < 600 and done_exit(os.path.basename(f)[:-5]) not in (0, None):
            recent += 1
    if br['s'] == 'dong' and recent >= 4:
        br.update(s='mo', since=now(), probe_at=now())
    elif br['s'] == 'nua-mo':
        pid = br.get('probe_id', '')
        if sched.get(pid) == 'Running':
            if now() - br['probe_start'] > 180 and not (cho_token(read_log(os.path.join(WT, pid + '.codex.log'), 20000)) and now() - br['probe_start'] < 900):
                br['s'] = 'dong'
        elif done_exit(pid) not in (0, None):
            br.update(s='mo', probe_at=now() + 120)
        else:
            br['s'] = 'dong'
    budget = [99 if br['s'] == 'dong' else 0]
    notes_pre = 'CAU DAO xingchi: %s' % br['s'].upper()
    force_note = False
    probed = [False]
    if br['s'] != 'dong' and br.get('since') and (now() - br['since']) > 3600 and now() - br.get('warn', 0) > 3600:
        notes.append('xingchi sap > 60 phut (cau dao mo tu %s)' % time.strftime('%H:%M', time.localtime(br['since'])))
        br['warn'] = now()
        force_note = True
    if br['s'] == 'dong':
        br['since'] = 0

    def st_of(i):
        return tasks.get(i, {}).get('status', '').lower()

    # 1) xet cac viec dang chay / da chet
    for i, d in sorted(tasks.items()):
        wt = os.path.join(WT, i)
        if not os.path.isdir(wt) or st_of(i) not in ('running', 'dang chay', 'in_progress', 'doing', 'failed'):
            continue
        running = sched.get(i) == 'Running'
        # #146: PID chi la can cu phu (hien o cot PID). KHONG dung PID de dung/giet tieu yeu.
        log = os.path.join(WT, i + '.codex.log')
        last = max(mt(log), mt(os.path.join(WT, i + '.nhip')), newest(wt))
        silent = (now() - last) / 60 if last else 9999
        ex = done_exit(i)
        err = ''
        tail = read_log(log, 20000)
        svc = True
        if 'Chat Completions' in tail or 'requires Responses' in tail:
            err = 'xingchi Chat Completions'
        elif '401' in tail[-3000:] and i not in assign:
            err = '401 khoa mac dinh'   # #131: khoa mac dinh da go, 401 la loi dich vu
        elif 'upstream_error' in tail:
            err = 'upstream_error'
        elif re.search(r'\b429\b', tail[-6000:]):
            err = '429'
        elif re.search(r'(?i)stream disconnected|connection (reset|refused|closed)|timed out|dns error', tail[-6000:]):
            err = 'loi mang'
        else:
            svc = False
        if running:
            level = 'SONG' if silent < IM else ('IM-NHUNG-SONG' if silent < TREO else 'TREO')
            ct = cho_token(tail)
            if ct:   # #147: cho token dau: <15 phut SONG, 15-30 canh bao, >=30 TREO
                level = 'CHO-TOKEN' if silent < 15 else ('CHO-TOKEN-LAU' if silent < 30 else 'TREO')
                if level == 'CHO-TOKEN-LAU' and lan.get(i + '#ct') != 1:
                    lan[i + '#ct'] = 1
                    notes.append('%s cho token dau > 15 phut (chua loi, chua dung)' % i)
            elif not DRY:
                tf = load(os.path.join(GD, 'ttft.json'), {})
                st0 = mt(os.path.join(WT, i + '.pid'))
                if i not in tf and st0 and 'turn.started' in tail:
                    tf[i] = max(0, int(min(now(), mt(log)) - st0))   # can tren (do theo nhip 2 phut)
                    save(os.path.join(GD, 'ttft.json'), tf)
            if level == 'TREO' and not DRY:
                ps("Stop-ScheduledTask -TaskName 'JX-codex-%s'" % i)
                _ls = [x.strip() for x in tail.replace(chr(0), '').splitlines() if x.strip()]
                notes.append('%s TREO >%d phut (log, nhip, file deu khong doi tu %s), da dung de chay lai; dong log cuoi: %s' % (i, TREO, time.strftime('%H:%M', time.localtime(last)) if last else '?', (_ls[-1][:160] if _ls else '(log trong)')))
                open(os.path.join(WT, i + '.done'), 'w').write('exit=2 treo')
                level = 'CHET'
        elif ex == 0 and not glob.glob(os.path.join(wt, 'JX1_OPS', 'REPORTS', i + '[-.]*')) and not subprocess.run(['git', '-C', wt, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip():
            level = 'CHET'   # #133.3: exit=0 ma worktree sach, khong bao cao = rong
            err = 'rong (exit=0, khong thay doi)'
            svc = False
        elif ex == 0 and model_of(i) == 'astra' and report_empty(i):
            level = 'CHET'   # #143: astra xong ma bao cao rong/thieu
            err = 'bao cao rong (astra)'
            svc = False
            if lan.get(i, 0) >= 2:
                lan[i + '#astra'] = 1
        elif ex == 0:
            level = 'XONG-CHO-GOP'
            if not DRY:
                subprocess.run(['git', '-C', wt, 'add', '-A', 'JX1_OPS'], capture_output=True)
                r = subprocess.run(['git', '-C', wt, 'commit', '-qm', 'Tong quan commit ho %s' % i], capture_output=True)
        elif ex is None and not running and os.path.exists(os.path.join(wt, 'JX1_OPS', 'REPORTS', i + '.md')) and now() - last > 600:
            level = 'XONG-CHO-GOP'   # khong co .done (wrapper chet) nhung da co bao cao; PM xac nhan khi gop
        elif ex is None and now() - last < 300:
            level = 'SONG'      # vua giao, chua kip thay
        else:
            level = 'CHET'
        if level == 'CHET' and not err and not svc:
            ls = [x.strip() for x in tail.replace(chr(0), '').splitlines() if x.strip()]
            err = 'khong ro: exit=%s, %s' % (ex, (ls[-1][:120] if ls else 'log trong'))
        if level == 'CHET' and svc:
            lan[i] = 0   # #123: loi dich vu khong cong vao 3 lan chay lai
            level = 'CHO-XINGCHI'
            fin = mt(os.path.join(WT, i + '.done')) or last
            if br['s'] != 'dong' and astra_ok(tasks.get(i, {}), i) and model_of(i) != 'astra' and not DRY and ramp_ok(sched):
                alive_n = len([x for x in sched if sched[x] == 'Running'])
                k = pick_key(assign, [x for x in sched if sched[x] == 'Running']) if alive_n < MAXALL else None
                if k:
                    set_astra(i)
                    assign[i] = k
                    try:
                        os.remove(os.path.join(WT, i + '.done'))
                    except OSError:
                        pass
                    if run_launch(i, k):
                        sched[i] = 'Running'
                        RAMP[0] += 1
                        level = 'CHAY-ASTRA'
                        notes.append('%s xingchi loi, chuyen sang astra bang %s' % (i, k))
                        time.sleep(10)
                        rows.append((i, level, assign.get(i, '-'), '-', time.strftime('%H:%M'), err or '-', lan.get(i, 0), model_of(i), pid_txt(i, True)))
                        continue
            probe = br['s'] == 'mo' and now() >= br['probe_at'] and not probed[0]
            if not DRY and ((br['s'] == 'dong' and (now() - fin) / 60 >= WAITS[0] and budget[0] > 0) or probe):
                k = pick_key(assign, [x for x in sched if sched[x] == 'Running'])
                if k:
                    assign[i] = k
                    try:
                        os.remove(os.path.join(WT, i + '.done'))
                    except OSError:
                        pass
                    if run_launch(i, k):
                        sched[i] = 'Running'
                        level = 'THU-LAI-XINGCHI'
                        notes.append('%s cho xingchi, thu lai bang %s%s' % (i, k, ' (thu cau dao)' if probe else ''))
                        if probe:
                            probed[0] = True
                            br.update(s='nua-mo', probe_id=i, probe_start=now())
                        time.sleep(10)
        elif level == 'CHET':
            n = lan.get(i, 0)
            fin = mt(os.path.join(WT, i + '.done')) or last
            if n >= len(WAITS) or (model_of(i) == 'astra' and n >= 2):
                level = 'CHET-BO'
                if lan.get(i + '#bao') != 1:
                    lan[i + '#bao'] = 1
                    notes.append('%s CHET-BO (loi viec, qua %d lan)' % (i, len(WAITS)))
                    force_note = True
            elif (now() - fin) / 60 >= WAITS[n] and not DRY and (budget[0] > 0 or (br['s'] != 'dong' and astra_ok(tasks.get(i, {}), i) and ramp_ok(sched))):
                _viaastra = budget[0] <= 0   # #151: cau dao mo -> budget 0; viec astra van duoc chay lai, tang dan 1->3
                alive_ids_now = [x for x in sched if sched[x] == 'Running']
                k = pick_key(assign, alive_ids_now)
                if k:
                    lan[i] = n + 1
                    assign[i] = k
                    if _viaastra:
                        RAMP[0] += 1
                        set_astra(i)
                    try:
                        os.remove(os.path.join(WT, i + '.done'))
                    except OSError:
                        pass
                    budget[0] -= 0 if _viaastra else 1
                    if run_launch(i, k):
                        sched[i] = 'Running'
                        notes.append('%s chet, chay lai lan %d bang %s' % (i, n + 1, k))
                        level = 'CHAY-LAI-%d' % (n + 1)
                        time.sleep(10)
                else:
                    notes.append('%s can chay lai nhung CAN KHOA MOI (moi khoa da du %d tieu yeu)' % (i, MAXKEY))
        rows.append((i, level, assign.get(i, '-'), time.strftime('%H:%M', time.localtime(mt(log))) if mt(log) else '-',
                     time.strftime('%H:%M', time.localtime(last)) if last else '-', err or '-', lan.get(i, 0), model_of(i), pid_txt(i, running)))

    # 2) giao viec ready
    for i, d in sorted(tasks.items()):
        if st_of(i) != 'ready':
            continue
        dep = [x for x in re.findall(r'[A-Z0-9]+-[0-9a-z]+', d.get('depends_on', '')) if x in tasks]
        if any(tasks[x].get('status', '').lower() not in ('done', 'xong', 'merged', 'closed', 'active') for x in dep):
            continue
        if hold_now(i):
            notes.append('%s ready, cho ngoai khung %dh-%dh (Q-51)' % (i, HOLD_H[0], HOLD_H[1]))
            continue
        use_astra = False
        if budget[0] <= 0:
            if br['s'] != 'dong' and astra_ok(d, i) and ramp_ok(sched):
                use_astra = True
            else:
                continue
        k = pick_key(assign, [x for x in sched if sched[x] == 'Running'])
        if not k:
            notes.append('%s ready nhung CAN KHOA MOI (Sonnet tao 1 khoa, cach nhau >=1 phut)' % i)
            continue
        if DRY:
            rows.append((i, 'SE-GIAO', k, '-', '-', '-', 0, model_of(i), '-'))
            continue
        ensure_worktree(i)
        if use_astra:
            RAMP[0] += 1
            set_astra(i)
        assign[i] = k
        budget[0] -= 0 if use_astra else 1
        if run_launch(i, k):
            sched[i] = 'Running'
            subprocess.run([sys.executable, '-I', os.path.join(ROOT, 'TOOLS', 'set_status.py'), i, 'running', 'Tong quan giao bang ' + k], capture_output=True)
            notes.append('%s giao bang %s' % (i, k))
            rows.append((i, 'SONG', k, '-', time.strftime('%H:%M'), '-', 0, model_of(i), '-'))
            time.sleep(10)  # #132.5: gian 10 giay giua hai lan giao

    if notes_pre:
        notes.insert(0, notes_pre)
    # 3) ghi bang
    if not DRY:
        save(os.path.join(GD, 'khoa.json'), assign)
        save(os.path.join(GD, 'lan.json'), lan)
        save(brp, br)
        use = {}
        for i in sched:
            if sched[i] == 'Running' and assign.get(i):
                use[assign[i]] = use.get(assign[i], 0) + 1
        out = ['# TIỂU YÊU (Tổng quản tự sinh lúc %s, đừng sửa tay)' % time.strftime('%Y-%m-%d %H:%M'), '',
               '**CẦU DAO xingchi: %s**' % {'dong': 'ĐÓNG (bình thường)', 'mo': 'MỞ (ngừng giao, mỗi 2 phút thử 1 việc)', 'nua-mo': 'NỬA-MỞ (đang thử 1 việc)'}[br['s']], '',
               'Mức: SONG / IM-NHUNG-SONG (20–60 phút) / TREO (>60, bị dừng chạy lại) / CHET / CHET-BO (quá 3 lần) / XONG-CHO-GOP. "Dấu hiệu sống cuối" = max(log, nhịp, file worktree).', '',
               '| Mã | Mức | Khóa | Log cuối | Dấu hiệu sống cuối | Lỗi cuối | Lần chạy lại | Mô hình | PID | Chờ token (giây) |', '|---|---|---|---|---|---|---|---|---|---|']
        for r in rows:
            out.append('| ' + ' | '.join(str(x) for x in r) + ' | ' + ttft_txt(r[0]) + ' |')
        out += ['', 'Khóa đang dùng: ' + (', '.join('%s=%d' % kv for kv in sorted(use.items())) or '(không)') + ' / khóa có: ' + ', '.join(keys()),
                'Đang chạy theo Task Scheduler: %d.' % len([1 for s in sched.values() if s == 'Running'])]
        if notes:
            out += ['', 'Việc vòng này:'] + ['- ' + n for n in notes]
        open(os.path.join(ROOT, 'STATE', 'TIEU-YEU.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
        ping = load(os.path.join(GD, 'ping.json'), {})
        kt = ['# KHÓA XINGCHI (Tổng quản tự sinh lúc %s; KHÔNG chứa giá trị khóa)' % time.strftime('%Y-%m-%d %H:%M'), '',
              'Trần 20 khóa / ≤%d tiểu yêu mỗi khóa. Quy trình: `DESIGN/QUY-TRINH-TAO-KHOA.md`.' % MAXKEY, '',
              '| Tên khóa | Nhóm | Ngày tạo (theo file) | Ping /v1/models | Tiểu yêu đang dùng |', '|---|---|---|---|---|']
        for k in keys():
            kf = os.path.join(KEYS, k + '.txt')
            kt.append('| %s | JX-Kn | %s | %s | %d |' % (k, time.strftime('%Y-%m-%d', time.localtime(os.path.getctime(kf))), ping.get(k, 'chưa ping (đã chạy được việc thật)'), use.get(k, 0)))
        kt += ['', 'Số khóa: %d / 20.' % len(keys())]
        open(os.path.join(ROOT, 'STATE', 'KHOA-XINGCHI.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(kt) + '\n')
        # #197: nhip tim doc lap cua Sonnet + RAM. Hoan tac: khoi phuc tong_quan.py.bak-197
        try:
            open(os.path.join(ROOT, 'STATE', 'SONNET-SONG.md'), 'w', encoding='utf-8', newline='\n').write(sonnet_song() + ld_dong() + '\n')
        except Exception as e:
            print('SONNET-SONG loi:', e)
        dead = [r for r in rows if r[1].startswith('CHET') or r[1] == 'TREO']
        # #153.A: chi danh thuc Sonnet khi co su kien that: CHET-BO moi, TREO, can khoa moi, cau dao doi trang thai, XONG-CHO-GOP moi (toi da 1 lan/gio cho canh bao chung)
        _lanq = load(os.path.join(GD, 'lan.json'), {})
        _gop = sorted(r[0] for r in rows if r[1] == 'XONG-CHO-GOP')
        _imp = force_note or any('TREO' in n or 'KHOA MOI' in n for n in notes)
        if br['s'] != _lanq.get('#brs'):
            _imp = True
            _lanq['#brs'] = br['s']
        if _gop and _gop != _lanq.get('#gop'):
            _imp = True
            _lanq['#gop'] = _gop
        elif not _gop:
            _lanq['#gop'] = []
        save(os.path.join(GD, 'lan.json'), _lanq)
        _txt = '[TỔNG QUẢN %s] ' % time.strftime('%d/%m %H:%M') + '; '.join(notes)
        if notes:   # #158/#159: moi ghi chu (ke ca su kien) chi vao TONG-QUAN-GHI.md, Sonnet doc khi bat dau dot; KHONG ghi TU-SONNET, khong danh thuc ai
            try:
                open(os.path.join(ROOT, 'STATE', 'TONG-QUAN-GHI.md'), 'a', encoding='utf-8', newline='\n').write(_txt + '\n')
            except OSError:
                pass
    else:
        for r in rows:
            print(r)
        print(notes)


TQ_NOTE = [None]


def push_state(tq_note=None):
    """#128.3: Tong quan day bang worktree RIENG (D:/JX-wt/tq) (detached, khong dung chung voi PM). STATE >=5 phut/lan; tq_note (su kien [TONG QUAN]) day NGAY."""
    stamp = os.path.join(GD, 'push.stamp')
    if not tq_note and time.time() - mt(stamp) < 300:
        return
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    repo = os.path.dirname(ROOT)
    tq = 'D:/JX-wt/tq'

    def g(cwd, *a):
        return subprocess.run(['git', '-C', cwd] + list(a), env=env, capture_output=True, text=True, timeout=120)
    try:
        g(repo, 'fetch', '-q', 'origin', 'jx1-ops')
        if not os.path.isdir(tq):
            g(repo, 'worktree', 'add', '--detach', tq, 'origin/jx1-ops')
        g(tq, 'reset', '-q', '--hard', 'origin/jx1-ops')
        files = ['STATE/TIEU-YEU.md', 'STATE/KHOA-XINGCHI.md', 'STATE/TIEN-DO.md', 'STATE/SONNET-SONG.md'] + (['STATE/TONG-QUAN-GHI.md'] if os.path.exists(os.path.join(ROOT, 'STATE', 'TONG-QUAN-GHI.md')) else [])
        for f in files:
            shutil.copyfile(os.path.join(ROOT, f), os.path.join(tq, 'JX1_OPS', f))
        if tq_note:
            with open(os.path.join(tq, 'JX1_OPS', 'HOP-THU', 'TU-SONNET.md'), 'a', encoding='utf-8', newline=chr(10)) as fh:
                fh.write(chr(10) + tq_note + chr(10))
        g(tq, 'add', '-A', 'JX1_OPS')
        if g(tq, 'diff', '--cached', '--quiet').returncode == 0:
            open(stamp, 'w').write('x')
            return
        g(tq, 'commit', '-qm', 'Tong quan: ' + ('su kien TONG QUAN' if tq_note else 'cap nhat TIEU-YEU/KHOA/TIEN-DO'))
        r = g(tq, 'push', '-q', 'origin', 'HEAD:jx1-ops')
        if r.returncode != 0:
            g(tq, 'pull', '-q', '--rebase', 'origin', 'jx1-ops')
            r = g(tq, 'push', '-q', 'origin', 'HEAD:jx1-ops')
        open(stamp, 'w').write('x')
        with open(os.path.join(GD, 'push.log'), 'a') as f:
            f.write('%s push rc=%s %s' % (time.strftime('%H:%M'), r.returncode, r.stderr.strip()[:200]) + chr(10))
    except Exception as e:
        with open(os.path.join(GD, 'push.log'), 'a') as f:
            f.write('%s push loi %s' % (time.strftime('%H:%M'), e) + chr(10))


try:
    main()
    if not DRY:
        push_state(TQ_NOTE[0])
except Exception as e:
    print('[tong_quan loi: %s]' % e)
