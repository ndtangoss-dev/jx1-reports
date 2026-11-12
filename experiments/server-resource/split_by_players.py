"""Tach so lieu tung giay theo so nguoi choi thuc te (mau ket noi 5 s gan nhat). python -I split_by_players.py <thu_muc> <milestone...>"""
import csv, sys, statistics as st
D = sys.argv[1]
CPU = 'processor(_total)\\%_processor_time'; AVAIL = 'memory\\available_mbytes'
p95 = lambda v: sorted(v)[int(0.95 * (len(v) - 1))]
for m in sys.argv[2:]:
    C = [(int(r['epoch']), int(r['gs_players'])) for r in csv.DictReader(open(f'{D}/phase48-conn-{m}.csv', encoding='utf-8-sig'))]
    R = list(csv.DictReader(open(f'{D}/phase48-raw-{m}.csv', encoding='utf-8-sig')))
    pl = lambda e: min(C, key=lambda c: abs(c[0] - e))[1]
    for want in (2, 1):
        S = [r for r in R if pl(int(r['epoch'])) == want]
        if not S: continue
        tx = [sum(float(v) for k, v in r.items() if k.endswith('bytes_sent/sec') and v) for r in S]
        rx = [sum(float(v) for k, v in r.items() if k.endswith('bytes_received/sec') and v) for r in S]
        cpu = [float(r[CPU]) for r in S]; ram = [6125 - float(r[AVAIL]) for r in S]
        print(f'{m} players={want}: n={len(S)} cpu avg/p95={st.mean(cpu):.1f}/{p95(cpu):.1f} ram avg/max={st.mean(ram):.0f}/{max(ram):.0f} '
              f'tx avg/p95={st.mean(tx):.0f}/{p95(tx):.0f} rx avg={st.mean(rx):.0f}')
