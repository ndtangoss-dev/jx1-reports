#!/usr/bin/env python
"""TONG QUAN (#118, L9): nguoi duy nhat quan tieu yeu. Moi lan chay = mot vong, Task Scheduler goi moi 3 phut (JX-TongQuan).
Moi vong: xet song/im/treo/chet (#117), commit ho khi xong, chay lai khi chet (cho 2/5/15 phut, toi da 3 lan),
giao viec status=ready, rai khoa (<=3 tieu yeu/khoa, het cho thi ghi CAN KHOA MOI), sinh STATE/TIEU-YEU.md va TIEN-DO.md.
Khong push (PM/guard commit file STATE). Khong doc gia tri khoa, chi ten khoa. Chay: python -I TOOLS/tong_quan.py [--dry]"""
import shutil, glob, json, os, re, subprocess, sys, time

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
WT = r'D:\JX-wt'
KEYS = r'C:\Users\PC\.jx1keys'
GD = os.path.join(WT, 'tong_quan')
MAXKEY = 3
MAXALL = 10  # tran dong thoi tam thoi (#137)
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
    ks = [k for k in keys() if use.get(k, 0) < MAXKEY]
    return min(ks, key=lambda k: use.get(k, 0)) if ks else None


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


def astra_ok(d, i):
    return str(d.get('astra', '')).lower() == 'ok' or i.startswith('R-')   # #143: viec doc/viet bao cao


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


def run_launch(i, key):
    env = dict(os.environ, JX_CODEX_KEY=key)
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
            'TIEP TUC: truoc khi lam, xem git status trong worktree; file da co thi KHONG lam lai, chi lam tiep phan con thieu.\n' % {'i': i})
    return wt


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
            if now() - br['probe_start'] > 180:
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
        pa = pid_alive(pid_of(i))   # #132.2: SONG = PID con; Scheduler bao Running ma PID mat = chet
        _act = max(mt(os.path.join(WT, i + '.codex.log')), mt(os.path.join(WT, i + '.nhip')))
        if running and pa is False and (now() - _act) > 300:
            running = False
            ps("Stop-ScheduledTask -TaskName 'JX-codex-%s'" % i)
            if done_exit(i) is None and not DRY:
                open(os.path.join(WT, i + '.done'), 'w').write('exit=3 pid mat')
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
            if level == 'TREO' and not DRY:
                ps("Stop-ScheduledTask -TaskName 'JX-codex-%s'" % i)
                notes.append('%s TREO >%d phut, da dung de chay lai' % (i, TREO))
                open(os.path.join(WT, i + '.done'), 'w').write('exit=2 treo')
                level = 'CHET'
        elif ex == 0 and not os.path.exists(os.path.join(wt, 'JX1_OPS', 'REPORTS', i + '.md')) and not subprocess.run(['git', '-C', wt, 'status', '--porcelain'], capture_output=True, text=True).stdout.strip():
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
        elif ex is None and now() - last < 120:
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
            elif (now() - fin) / 60 >= WAITS[n] and not DRY and budget[0] > 0:
                alive_ids_now = [x for x in sched if sched[x] == 'Running']
                k = pick_key(assign, alive_ids_now)
                if k:
                    lan[i] = n + 1
                    assign[i] = k
                    try:
                        os.remove(os.path.join(WT, i + '.done'))
                    except OSError:
                        pass
                    budget[0] -= 1
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
               '| Mã | Mức | Khóa | Log cuối | Dấu hiệu sống cuối | Lỗi cuối | Lần chạy lại | Mô hình | PID |', '|---|---|---|---|---|---|---|---|---|']
        for r in rows:
            out.append('| ' + ' | '.join(str(x) for x in r) + ' |')
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
        dead = [r for r in rows if r[1].startswith('CHET') or r[1] == 'TREO']
        if notes and (force_note or len(dead) >= 3 or any('TREO' in n or 'KHOA MOI' in n for n in notes)):
            TQ_NOTE[0] = '[TỔNG QUẢN %s] ' % time.strftime('%d/%m %H:%M') + '; '.join(notes)
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
        files = ['STATE/TIEU-YEU.md', 'STATE/KHOA-XINGCHI.md', 'STATE/TIEN-DO.md']
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
