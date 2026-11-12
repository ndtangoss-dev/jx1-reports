"""Phan tich so lieu Phase 48 (guest VM). python -I analyze_phase48.py <thu_muc> <tick_log.txt> [A B C]
- CPU guest: \\Processor(_Total)\\% Processor Time = % cua TOAN BO vCPU (0-100).
- CPU tien trinh: \\Process(x)\\% Processor Time = % cua MOT vCPU (0-100*so vCPU); bao cao them quy doi % toan VM.
- RAM guest used = tong RAM guest - Available MBytes. Working Set (RSS tuong duong) va Private Bytes theo tien trinh;
  khong cong may moc (co trang dung chung).
- Network: tong cac card (bo loopback/isatap/teredo).
- Doan hoat dong (Moc B/C): file phase48-segments-<M>.csv (segment,epoch_start,epoch_end)."""
import csv, sys, os, re, statistics as st

D = sys.argv[1]; TICK = sys.argv[2]; MS = sys.argv[3:] or ['A', 'B']
VCPU, RAM_MB = 4, 6125
PROCS = ['gs001', 'bishop', 'goddess', 'sword3paysys', 'sqlservr', 'wsmprovhost']

def pct(v, p):
    v = sorted(v); return v[min(len(v) - 1, int(round(p / 100 * (len(v) - 1))))] if v else float('nan')
def stats(v):
    return dict(n=len(v), avg=st.mean(v) if v else float('nan'), med=st.median(v) if v else float('nan'),
                p95=pct(v, 95), p99=pct(v, 99), max=max(v) if v else float('nan'))
def col(rows, key):
    return [float(r[key]) for r in rows if r.get(key) not in (None, '')]
def net(rows, what):
    out = []
    for r in rows:
        s = 0.0; ok = False
        for k, v in r.items():
            if k.startswith('network_interface(') and k.endswith(what) and not re.search('loopback|isatap|teredo', k):
                if v not in ('', None): s += float(v); ok = True
        if ok: out.append(s)
    return out

ticks = []
for l in open(TICK, encoding='utf-8', errors='replace'):
    m = re.match(r'(\d+)\s.*SvrFPS=\s*(\d+)/(\d+), tick avg=(\d+)us max=(\d+)us over=(\d+)', l)
    if m: ticks.append(tuple(int(x) for x in m.groups()))

summary = []
for M in MS:
    rawp = os.path.join(D, f'phase48-raw-{M}.csv')
    if not os.path.exists(rawp): continue
    rows = list(csv.DictReader(open(rawp, encoding='utf-8-sig')))
    segs = [('toan_bo', int(rows[0]['epoch']), int(rows[-1]['epoch']))]
    sp = os.path.join(D, f'phase48-segments-{M}.csv')
    if os.path.exists(sp):
        segs += [(r['segment'], int(r['epoch_start']), int(r['epoch_end'])) for r in csv.DictReader(open(sp, encoding='utf-8-sig'))]
    conn = list(csv.DictReader(open(os.path.join(D, f'phase48-conn-{M}.csv'), encoding='utf-8-sig')))
    ep = [int(r['epoch']) for r in rows]
    gaps = sum(max(0, b - a - 1) for a, b in zip(ep, ep[1:]))
    for name, a, b in segs:
        R = [r for r in rows if a <= int(r['epoch']) <= b]
        if not R: continue
        rec = dict(milestone=M, segment=name, epoch_start=a, epoch_end=b, samples=len(R), missing_s=gaps if name == 'toan_bo' else '')
        def add(tag, v, scale=1.0):
            s = stats([x * scale for x in v])
            for k in ('avg', 'p95', 'p99', 'max'): rec[f'{tag}_{k}'] = round(s[k], 3)
        add('cpu_guest_pct', col(R, 'processor(_total)\\%_processor_time'))
        add('ram_used_mb', [RAM_MB - x for x in col(R, 'memory\\available_mbytes')])
        add('commit_mb', col(R, 'memory\\committed_bytes'), 1 / 2**20)
        add('pagefile_pct', col(R, 'paging_file(_total)\\%_usage'))
        add('pages_per_s', col(R, 'memory\\pages/sec'))
        add('net_rx_Bps', net(R, '\\bytes_received/sec')); add('net_tx_Bps', net(R, '\\bytes_sent/sec'))
        add('net_rx_pps', net(R, '\\packets_received/sec')); add('net_tx_pps', net(R, '\\packets_sent/sec'))
        for p in PROCS:
            add(f'{p}_cpu_pct_1core', col(R, f'process({p})\\%_processor_time'))
            add(f'{p}_ws_mb', col(R, f'process({p})\\working_set'), 1 / 2**20)
            add(f'{p}_priv_mb', col(R, f'process({p})\\private_bytes'), 1 / 2**20)
        C = [c for c in conn if a <= int(c['epoch']) <= b]
        rec['players_max'] = max((int(c['gs_players']) for c in C), default='')
        rec['bishop_clients_max'] = max((int(c['bishop_clients']) for c in C), default='')
        T = [t for t in ticks if a - 30 <= t[0] <= b + 30]
        if T:
            rec['tick_lines'] = len(T); rec['svrfps_min'] = min(t[1] for t in T); rec['svrfps_target'] = T[0][2]
            rec['tick_avg_us_mean'] = round(st.mean(t[3] for t in T)); rec['tick_max_us'] = max(t[4] for t in T); rec['tick_over_sum'] = sum(t[5] for t in T)
        summary.append(rec)
keys = []
for r in summary:
    for k in r:
        if k not in keys: keys.append(k)
with open(os.path.join(D, 'phase48-summary.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(summary)
for r in summary:
    print(f"{r['milestone']}/{r['segment']}: n={r['samples']} cpu avg/p95/max={r['cpu_guest_pct_avg']}/{r['cpu_guest_pct_p95']}/{r['cpu_guest_pct_max']}% "
          f"ram used avg/max={r['ram_used_mb_avg']}/{r['ram_used_mb_max']}MB gs001 cpu(1core) avg/p95={r['gs001_cpu_pct_1core_avg']}/{r['gs001_cpu_pct_1core_p95']} "
          f"gs001 ws={r['gs001_ws_mb_avg']}MB wsm cpu avg={r['wsmprovhost_cpu_pct_1core_avg']} net rx/tx avg={r['net_rx_Bps_avg']}/{r['net_tx_Bps_avg']}B/s "
          f"players={r.get('players_max')} tick fps_min={r.get('svrfps_min')} over={r.get('tick_over_sum')} max_us={r.get('tick_max_us')}")
