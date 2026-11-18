#!/usr/bin/env python
"""TONG QUAN (#118, L9): nguoi duy nhat quan tieu yeu. Moi lan chay = mot vong, Task Scheduler goi moi 3 phut (JX-TongQuan).
Moi vong: xet song/im/treo/chet (#117), commit ho khi xong, chay lai khi chet (cho 2/5/15 phut, toi da 3 lan),
giao viec status=ready, rai khoa (<=3 tieu yeu/khoa, het cho thi ghi CAN KHOA MOI), sinh STATE/TIEU-YEU.md va TIEN-DO.md.
Khong push (PM/guard commit file STATE). Khong doc gia tri khoa, chi ten khoa. Chay: python -I TOOLS/tong_quan.py [--dry]"""
import glob, json, os, re, subprocess, sys, time

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
WT = r'D:\JX-wt'
KEYS = r'C:\Users\PC\.jx1keys'
GD = os.path.join(WT, 'tong_quan')
MAXKEY = 3
WAITS = (2, 5, 15)      # phut cho truoc lan chay lai 1, 2, 3
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
    use = {}
    for i in alive_ids:
        k = assign.get(i)
        if k:
            use[k] = use.get(k, 0) + 1
    ks = [k for k in keys() if use.get(k, 0) < MAXKEY]
    return min(ks, key=lambda k: use.get(k, 0)) if ks else None


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
    # cau dao nghen dich vu: >=4 viec chet trong 10 phut gan day -> moi vong chi duoc phep 1 lan giao/chay lai
    recent = 0
    for f in glob.glob(os.path.join(WT, '*.done')):
        if now() - mt(f) < 600 and done_exit(os.path.basename(f)[:-5]) not in (0, None):
            recent += 1
    budget = [1 if recent >= 4 else 99]
    if recent >= 4:
        notes_pre = 'NGHEN: %d viec chet trong 10 phut, moi vong chi giao 1 viec' % recent
    else:
        notes_pre = ''

    def st_of(i):
        return tasks.get(i, {}).get('status', '').lower()

    # 1) xet cac viec dang chay / da chet
    for i, d in sorted(tasks.items()):
        wt = os.path.join(WT, i)
        if not os.path.isdir(wt) or st_of(i) not in ('running', 'dang chay', 'in_progress', 'doing', 'failed'):
            continue
        running = sched.get(i) == 'Running'
        log = os.path.join(WT, i + '.codex.log')
        last = max(mt(log), mt(os.path.join(WT, i + '.nhip')), newest(wt))
        silent = (now() - last) / 60 if last else 9999
        ex = done_exit(i)
        err = ''
        tail = read_log(log, 20000)
        if 'Chat Completions' in tail:
            err = 'xingchi Chat Completions'
        elif re.search(r'\b429\b', tail[-6000:]):
            err = '429'
        if running:
            level = 'SONG' if silent < IM else ('IM-NHUNG-SONG' if silent < TREO else 'TREO')
            if level == 'TREO' and not DRY:
                ps("Stop-ScheduledTask -TaskName 'JX-codex-%s'" % i)
                notes.append('%s TREO >%d phut, da dung de chay lai' % (i, TREO))
                open(os.path.join(WT, i + '.done'), 'w').write('exit=2 treo')
                level = 'CHET'
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
        if level == 'CHET':
            n = lan.get(i, 0)
            fin = mt(os.path.join(WT, i + '.done')) or last
            if n >= len(WAITS):
                level = 'CHET-BO'
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
                        time.sleep(20)
                else:
                    notes.append('%s can chay lai nhung CAN KHOA MOI (moi khoa da du %d tieu yeu)' % (i, MAXKEY))
        rows.append((i, level, assign.get(i, '(tay/mac dinh)'), time.strftime('%H:%M', time.localtime(mt(log))) if mt(log) else '-',
                     time.strftime('%H:%M', time.localtime(last)) if last else '-', err or '-', lan.get(i, 0)))

    # 2) giao viec ready
    for i, d in sorted(tasks.items()):
        if st_of(i) != 'ready':
            continue
        dep = [x for x in re.findall(r'[A-Z0-9]+-[0-9a-z]+', d.get('depends_on', '')) if x in tasks]
        if any(tasks[x].get('status', '').lower() not in ('done', 'xong', 'merged', 'closed', 'active') for x in dep):
            continue
        if budget[0] <= 0:
            continue
        k = pick_key(assign, [x for x in sched if sched[x] == 'Running'])
        if not k:
            notes.append('%s ready nhung CAN KHOA MOI (Sonnet tao 1 khoa, cach nhau >=1 phut)' % i)
            continue
        if DRY:
            rows.append((i, 'SE-GIAO', k, '-', '-', '-', 0))
            continue
        ensure_worktree(i)
        assign[i] = k
        budget[0] -= 1
        if run_launch(i, k):
            sched[i] = 'Running'
            subprocess.run([sys.executable, '-I', os.path.join(ROOT, 'TOOLS', 'set_status.py'), i, 'running', 'Tong quan giao bang ' + k], capture_output=True)
            notes.append('%s giao bang %s' % (i, k))
            rows.append((i, 'SONG', k, '-', time.strftime('%H:%M'), '-', 0))
            time.sleep(60)  # gian 1 phut giua hai lan giao

    if notes_pre:
        notes.insert(0, notes_pre)
    # 3) ghi bang
    if not DRY:
        save(os.path.join(GD, 'khoa.json'), assign)
        save(os.path.join(GD, 'lan.json'), lan)
        use = {}
        for i in sched:
            if sched[i] == 'Running' and assign.get(i):
                use[assign[i]] = use.get(assign[i], 0) + 1
        out = ['# TIỂU YÊU (Tổng quản tự sinh lúc %s, đừng sửa tay)' % time.strftime('%Y-%m-%d %H:%M'), '',
               'Mức: SONG / IM-NHUNG-SONG (20–60 phút) / TREO (>60, bị dừng chạy lại) / CHET / CHET-BO (quá 3 lần) / XONG-CHO-GOP. "Dấu hiệu sống cuối" = max(log, nhịp, file worktree).', '',
               '| Mã | Mức | Khóa | Log cuối | Dấu hiệu sống cuối | Lỗi cuối | Lần chạy lại |', '|---|---|---|---|---|---|---|']
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
        if notes and (len(dead) >= 3 or any('TREO' in n or 'KHOA MOI' in n for n in notes)):
            with open(os.path.join(ROOT, 'HOP-THU', 'TU-SONNET.md'), 'a', encoding='utf-8') as f:
                f.write('\n[TỔNG QUẢN %s] ' % time.strftime('%d/%m %H:%M') + '; '.join(notes) + '\n')
    else:
        for r in rows:
            print(r)
        print(notes)


def push_state():
    """#124/#125: day STATE/TIEU-YEU.md, KHOA-XINGCHI.md, TIEN-DO.md len kho moi >=5 phut; git khong hoi mat khau, timeout 120 giay."""
    stamp = os.path.join(GD, 'push.stamp')
    if time.time() - mt(stamp) < 300:
        return
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    repo = os.path.dirname(ROOT)

    def g(*a):
        return subprocess.run(['git', '-C', repo] + list(a), env=env, capture_output=True, text=True, timeout=120)
    try:
        files = ['JX1_OPS/STATE/TIEU-YEU.md', 'JX1_OPS/STATE/KHOA-XINGCHI.md', 'JX1_OPS/STATE/TIEN-DO.md']
        g('add', '--', *files)
        if g('diff', '--cached', '--quiet', '--', *files).returncode == 0:
            open(stamp, 'w').write('x')
            return
        g('commit', '-qm', 'Tong quan: cap nhat TIEU-YEU/KHOA/TIEN-DO', '--', *files)
        g('pull', '-q', '--rebase', '--autostash', 'origin', 'jx1-ops')
        r = g('push', '-q', 'origin', 'HEAD:jx1-ops')
        open(stamp, 'w').write('x')
        with open(os.path.join(GD, 'push.log'), 'a') as f:
            f.write('%s push rc=%s %s\n' % (time.strftime('%H:%M'), r.returncode, r.stderr.strip()[:200]))
    except Exception as e:
        with open(os.path.join(GD, 'push.log'), 'a') as f:
            f.write('%s push loi %s\n' % (time.strftime('%H:%M'), e))


try:
    main()
    if not DRY:
        push_state()
except Exception as e:
    print('[tong_quan loi: %s]' % e)
