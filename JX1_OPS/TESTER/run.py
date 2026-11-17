"""CLI smoke offline. Chạy file trực tiếp để bootstrap package với python -I."""

import argparse
from pathlib import Path
import re
import sys

if __package__ in (None, ""):
    import importlib.util
    spec = importlib.util.spec_from_file_location("tester_bootstrap", Path(__file__).with_name("bootstrap.py"))
    bootstrap = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bootstrap)
    bootstrap.load_packages()
    __package__ = "JX1_OPS.TESTER"

from .core import Config, run_scenario
from .reporting import write_report
from .scenarios import FULL_CYCLE, SMOKE_LOGIN
from .visibility import VISIBILITY


def bot_list(value):
    match = re.fullmatch(r"bot0([1-5])\.\.bot0([1-5])", value)
    if match:
        first, last = map(int, match.groups())
        if first <= last:
            return [f"bot{index:02d}" for index in range(first, last + 1)]
    bots = value.split(",")
    if bots and all(re.fullmatch(r"bot0[1-5]", bot) for bot in bots) and len(set(bots)) == len(bots):
        return bots
    raise argparse.ArgumentTypeError("Dùng bot01..bot05 hoặc danh sách bot01,bot02 không trùng")


def main(argv=None):
    scenarios = {scenario.name: scenario for scenario in (SMOKE_LOGIN, FULL_CYCLE, VISIBILITY)}
    parser = argparse.ArgumentParser(description="TESTER offline với máy chủ giả; gs001 thật chưa kiểm")
    parser.add_argument("--scenario", choices=tuple(scenarios), required=True)
    parser.add_argument("--bots", type=bot_list, required=True)
    parser.add_argument("--host", required=True, help="Chỉ 127.0.0.1")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--workers", type=int, choices=range(1, 6), default=1)
    args = parser.parse_args(argv)
    try:
        config = Config(args.host, args.port)
    except ValueError as error:
        parser.error(str(error))
    try:
        scenario = scenarios[args.scenario]
        results = run_scenario(scenario, args.bots, config, args.workers)
        path = write_report(args.out, scenario, args.bots, results)
    except (OSError, RuntimeError, ValueError):
        print("Không chạy/ghi báo cáo được; kiểm tra cấu hình, quyền ghi và .tester.lock.", file=sys.stderr)
        return 2
    print("Báo cáo: " + str(path))
    return 1 if any(result.status == "FAIL" for result in results) else 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
