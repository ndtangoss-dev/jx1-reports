"""B-04a draft: offline only, stdlib, never imports BOT or opens sockets.

Tick regex is supplied by PM after checking actual gs001 log semantics.
Packet input contains cumulative per-connection byte counters at window edges.
"""
import argparse
import csv
import math
import re
import statistics
from pathlib import Path


def number(value):
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise ValueError('Expected finite nonnegative numeric value')
    return result


def rows(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def write(path, records):
    with path.open('x', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def percentile(values, quantile):
    return sorted(values)[max(0, math.ceil(len(values) * quantile) - 1)]


def packet_counters(args):
    """Count metadata exported from one capture vantage, never payload bytes.

    Roster proves idle connections exist; reconnect must use a new run instead.
    Capture elapsed_s must use the same t=0 as CPU/log (PM aligns clocks).
    """
    start, stop = args.warmup, args.duration
    if stop - start < 300:
        raise ValueError('Need >=300 measured seconds')
    roster = rows(args.roster)
    sessions = [row['session_id'] for row in roster]
    if (len(set(sessions)) != 120 or len(sessions) != 120 or
            sum(bool(re.fullmatch(r'bot[0-9]{3}', s)) for s in sessions) != 100 or
            sum(bool(re.fullmatch(r'human[0-9]{3}', s)) for s in sessions) != 20):
        raise ValueError('Roster requires 100 bot + 20 human aliases')
    counts = {s: {start: [0, 0], stop: [0, 0]} for s in sessions}
    last = -1.0
    for row in rows(args.events):
        elapsed = number(row['elapsed_s'])
        size = int(row['bytes'])
        session = row['session_id']
        direction = row['direction']
        if elapsed < last or size < 0 or direction not in ('rx', 'tx') or session not in counts:
            raise ValueError('Invalid packet metadata/order/session')
        last = elapsed
        for edge in (start, stop):
            if elapsed < edge:
                counts[session][edge][0 if direction == 'rx' else 1] += size
    # Capture completeness (including a quiet tail) must be proven externally.
    result = []
    for session in sorted(counts):
        for edge in (start, stop):
            rx, tx = counts[session][edge]
            result.append(dict(elapsed_s=edge, session_id=session, rx_bytes=rx, tx_bytes=tx))
    write(Path(args.out), result)


def analyze(args):
    start, stop = args.warmup, args.duration
    if stop - start < 300 or args.bots != 100 or args.humans != 20:
        raise ValueError('O-01 requires 100 bots + 20 humans and >=300 measured seconds')
    pattern = re.compile(args.tick_regex)
    if not {'elapsed_s', 'tick_ms'} <= set(pattern.groupindex):
        raise ValueError('Regex needs named groups elapsed_s and tick_ms')
    ticks, timestamps, ignored = [], [], 0
    with Path(args.tick_log).open(encoding=args.log_encoding, errors='strict') as stream:
        for line in stream:
            match = pattern.fullmatch(line.rstrip('\r\n'))
            if not match:
                ignored += 1
                continue
            elapsed = number(match['elapsed_s'])
            tick = number(match['tick_ms'])
            if timestamps and elapsed <= timestamps[-1]:
                raise ValueError('Tick timestamps must strictly increase; check duplicates/restarts')
            timestamps.append(elapsed)
            if start <= elapsed < stop:
                ticks.append(tick)
    window = stop - start
    if len(ticks) < math.ceil(window * args.hz * 0.9):
        raise ValueError('Missing tick evidence: <90% expected per-tick samples')
    cpu_area, cpu_coverage, cpu_values = 0.0, 0.0, []
    previous_end = 0.0
    for row in rows(args.cpu):
        end = number(row['elapsed_s'])
        length = number(row['interval_s'])
        value = number(row['cpu_percent'])
        begin = end - length
        if length <= 0 or value > 100.01 or abs(begin - previous_end) > 0.0001:
            raise ValueError('CPU intervals must be contiguous, positive, CPU in [0,100]')
        previous_end = end
        # Only whole intervals: never invent CPU utilization for a partial interval.
        if begin >= start and end <= stop:
            cpu_area += value * length
            cpu_coverage += length
            cpu_values.append(value)
    if cpu_coverage < window * 0.9:
        raise ValueError('Missing CPU evidence: <90% measured-window coverage')
    sessions = {}
    for row in rows(args.packets):
        session = row['session_id']
        if not re.fullmatch(r'(?:bot|human)[0-9]{3}', session):
            raise ValueError('Use anonymous session IDs bot001/human001, never account identifiers')
        elapsed = number(row['elapsed_s'])
        if elapsed not in (start, stop):
            raise ValueError('Packet counters require exactly the two window edges')
        # int rejects fractions; counters are arbitrary-precision nonnegative bytes.
        rx, tx = int(row['rx_bytes']), int(row['tx_bytes'])
        if rx < 0 or tx < 0:
            raise ValueError('Negative byte counters')
        edges = sessions.setdefault(session, {})
        if elapsed in edges:
            raise ValueError('Duplicate session/edge; counters must have one owner')
        edges[elapsed] = (rx, tx)
    if (sum(s.startswith('bot') for s in sessions) != args.bots or
            sum(s.startswith('human') for s in sessions) != args.humans):
        raise ValueError('Need all 120 O-01 connection counters, including idle sessions')
    per_session = []
    for session, edges in sorted(sessions.items()):
        if set(edges) != {start, stop}:
            raise ValueError('Missing packet counter edge')
        rx, tx = (edges[stop][i] - edges[start][i] for i in (0, 1))
        if min(rx, tx) < 0:
            raise ValueError('Counter reset/reconnect: rerun with stable sessions')
        per_session.append(dict(run_id=args.run_id, session_id=session,
                                rx_bytes=rx, tx_bytes=tx,
                                total_bytes=rx + tx, bytes_per_s=(rx + tx) / window))
    total = sum(row['total_bytes'] for row in per_session)
    summary = dict(run_id=args.run_id, pair_id=args.pair_id, variant=args.variant,
                   hz=args.hz, bots=args.bots, humans=args.humans,
                   warmup_s=start, duration_s=stop, window_s=window,
                   tick_count=len(ticks), tick_mean_ms=statistics.mean(ticks),
                   tick_p95_ms=percentile(ticks, 0.95), tick_max_ms=max(ticks),
                   tick_over_budget_percent=100 * sum(t > 1000 / args.hz for t in ticks) / len(ticks),
                   cpu_mean_percent=cpu_area / cpu_coverage,
                   cpu_max_percent=max(cpu_values), cpu_coverage_s=cpu_coverage,
                   total_bytes=total, bytes_per_s=total / window,
                   ignored_log_lines=ignored, byte_basis=args.byte_basis)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    write(out / 'summary.csv', [summary])
    write(out / 'sessions.csv', per_session)


def compare(args):
    base_rows, after_rows = rows(args.before), rows(args.after)
    if len(base_rows) != 1 or len(after_rows) != 1:
        raise ValueError('Expected one run per summary')
    base, after = base_rows[0], after_rows[0]
    for field in ('pair_id', 'hz', 'bots', 'humans', 'window_s', 'warmup_s', 'byte_basis'):
        if base[field] != after[field]:
            raise ValueError('Incomparable runs: ' + field)
    if (base['variant'], after['variant']) not in {
            ('original', 'disabled'), ('disabled', 'enabled')}:
        raise ValueError('Compare original -> disabled or disabled -> enabled')
    checks = []
    for field, limit, absolute in (
            ('tick_p95_ms', args.tick_growth_percent, False),
            ('cpu_mean_percent', args.cpu_growth_pp, True),
            ('bytes_per_s', args.byte_growth_percent, False)):
        before, later = number(base[field]), number(after[field])
        if not absolute and before == 0:
            status, change = 'CHUA_KIEM', ''
        else:
            change = later - before if absolute else 100 * (later / before - 1)
            status = 'PASS' if change <= limit else 'FAIL'
        checks.append(dict(metric=field, before=before, after=later, change=change,
                           limit=limit, unit='percentage_points' if absolute else 'percent',
                           status=status, criteria='PM_PROPOSED_NOT_O01_APPROVAL'))
    budget = 1000 / number(after['hz'])
    checks.append(dict(metric='tick_p95_budget_ms', before='', after=after['tick_p95_ms'],
                       change='', limit=budget, unit='ms',
                       status='PASS' if number(after['tick_p95_ms']) <= budget else 'FAIL',
                       criteria='PM_PROPOSED_NOT_O01_APPROVAL'))
    write(Path(args.out), checks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    counters = commands.add_parser('packet-counters')
    for option in ('roster', 'events', 'out'):
        counters.add_argument('--' + option, required=True)
    counters.add_argument('--warmup', type=number, default=60)
    counters.add_argument('--duration', type=number, default=660)
    counters.set_defaults(action=packet_counters)
    collect = commands.add_parser('analyze')
    for option in ('run-id', 'pair-id', 'tick-log', 'tick-regex', 'cpu', 'packets', 'out'):
        collect.add_argument('--' + option, required=True)
    collect.add_argument('--variant', choices=('original', 'disabled', 'enabled'), required=True)
    collect.add_argument('--hz', type=int, choices=(18, 36), required=True)
    collect.add_argument('--bots', type=int, default=100)
    collect.add_argument('--humans', type=int, default=20)
    collect.add_argument('--warmup', type=number, default=60)
    collect.add_argument('--duration', type=number, default=660)
    collect.add_argument('--log-encoding', default='utf-8-sig')
    collect.add_argument('--byte-basis', choices=('socket_payload', 'wire'), required=True)
    collect.set_defaults(action=analyze)
    comparison = commands.add_parser('compare')
    for option in ('before', 'after', 'out'):
        comparison.add_argument('--' + option, required=True)
    comparison.add_argument('--tick-growth-percent', type=number, default=5)
    comparison.add_argument('--cpu-growth-pp', type=number, default=5)
    comparison.add_argument('--byte-growth-percent', type=number, default=5)
    comparison.set_defaults(action=compare)
    args = parser.parse_args()
    try:
        args.action(args)
    except (OSError, ValueError, KeyError, LookupError, re.error) as error:
        # Never print raw lines/paths/exception contents from private input logs.
        parser.exit(2, 'B-04a: invalid/incomplete input or output conflict (' + type(error).__name__ + '). See input contract.\n')


if __name__ == '__main__':
    main()
