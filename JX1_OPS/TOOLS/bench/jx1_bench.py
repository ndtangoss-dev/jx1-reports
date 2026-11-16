#!/usr/bin/env python3
"""Phan tich bo so lieu P-02 ma khong ket noi VM/server.

Lenh mac dinh doc sample_metrics.json cung thu muc va in bang ket qua.
Du lieu dau vao co ba mang:

* tick_samples: {"tick_ms": number}
* network_mode: "cumulative" (time_s, rx_bytes, tx_bytes) hoac "interval" (interval_s, rx_bytes, tx_bytes)
* frame_samples: frames hoac fps, moi mau luon co interval_s > 0

Bo phan tich khong tu thu thap du lieu. Collector PowerShell (neu co) chi
can xuat ve schema tren roi chay lai lenh nay.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence

MAIN_VM_IP = "192.168.1.50"
TEST_VM_NAME = "JX-Test-36"
TEST_VM_IP = "192.168.56.150"


class InputError(ValueError):
    """Loi du lieu dau vao khong hop le hoac vuot hang rao dia chi."""


def _number(value: Any, label: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{label} phai la so")
    result = float(value)
    if not math.isfinite(result) or result < 0 or (positive and result <= 0):
        suffix = "> 0" if positive else ">= 0"
        raise InputError(f"{label} phai {suffix}")
    return result


def _reject_main_vm(value: Any) -> None:
    """Chan moi tham chieu den Main VM truoc khi phan tich du lieu."""
    if isinstance(value, str):
        if MAIN_VM_IP in value:
            raise InputError("Main VM bi chan; chi cho phep JX-Test-36")
        return
    if isinstance(value, Mapping):
        for child in list(value.keys()) + list(value.values()):
            _reject_main_vm(child)
        return
    if isinstance(value, (list, tuple)):
        for child in value:
            _reject_main_vm(child)


def load_payload(path: Path) -> Dict[str, Any]:
    """Doc JSON cuc bo; tu choi UNC/network path truoc khi mo file."""
    _reject_main_vm(str(path))
    if str(path).startswith(("\\\\", "//")) or path.drive.startswith("\\\\"):
        raise InputError("chi doc file cuc bo; UNC/network path bi chan")
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError) as exc:
        raise InputError(f"khong doc duoc input: {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise InputError(f"JSON khong hop le: {path}: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise InputError("input phai la mot object JSON")
    _reject_main_vm(payload)

    target = payload.get("target")
    if not isinstance(target, Mapping):
        raise InputError("thieu target")
    if target.get("name") != TEST_VM_NAME or target.get("ip") != TEST_VM_IP:
        raise InputError(
            f"target phai la {TEST_VM_NAME} ({TEST_VM_IP}); khong chay target khac"
        )
    return payload


def _samples(payload: Mapping[str, Any], key: str) -> List[Mapping[str, Any]]:
    values = payload.get(key)
    if not isinstance(values, list) or not values:
        raise InputError(f"{key} phai la mang khong rong")
    if not all(isinstance(item, Mapping) for item in values):
        raise InputError(f"{key} phai gom cac object")
    return list(values)


def percentile(values: Sequence[float], fraction: float) -> float:
    """Percentile noi suy tuyen tinh, voi danh sach da co it nhat mot phan tu."""
    if not values:
        raise InputError("khong co mau de tinh percentile")
    if not 0 <= fraction <= 1:
        raise ValueError("fraction phai nam trong [0, 1]")
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * weight


def _tick_summary(payload: Mapping[str, Any]) -> Dict[str, float]:
    samples = _samples(payload, "tick_samples")
    values = [_number(item.get("tick_ms"), "tick_ms") for item in samples]
    return {
        "avg_ms": sum(values) / len(values),
        "p95_ms": percentile(values, 0.95),
        "min_ms": min(values),
        "max_ms": max(values),
        "samples": float(len(values)),
    }


def _network_summary(payload: Mapping[str, Any]) -> Dict[str, float]:
    samples = _samples(payload, "network_samples")
    mode = payload.get("network_mode")
    total_rx = total_tx = total_seconds = 0.0
    if mode == "cumulative":
        if len(samples) < 2:
            raise InputError("counter cong don can it nhat 2 mau")
        previous = None
        for item in samples:
            current = (
                _number(item.get("time_s"), "time_s"),
                _number(item.get("rx_bytes"), "rx_bytes"),
                _number(item.get("tx_bytes"), "tx_bytes"),
            )
            if previous is not None:
                elapsed = current[0] - previous[0]
                if elapsed <= 0:
                    raise InputError("time_s phai tang nghiem ngat")
                if current[1] < previous[1] or current[2] < previous[2]:
                    raise InputError("counter reset/wrap; tach lan do moi")
                total_seconds += elapsed
                total_rx += current[1] - previous[1]
                total_tx += current[2] - previous[2]
            previous = current
    elif mode == "interval":
        for item in samples:
            interval = _number(item.get("interval_s"), "interval_s", positive=True)
            total_rx += _number(item.get("rx_bytes"), "rx_bytes")
            total_tx += _number(item.get("tx_bytes"), "tx_bytes")
            total_seconds += interval
    else:
        raise InputError('network_mode phai la "cumulative" hoac "interval"')
    return {
        "rx_mbps": total_rx * 8 / total_seconds / 1_000_000,
        "tx_mbps": total_tx * 8 / total_seconds / 1_000_000,
        "total_mbps": (total_rx + total_tx) * 8 / total_seconds / 1_000_000,
        "samples": float(len(samples)),
        "seconds": total_seconds,
    }

def _frame_summary(payload: Mapping[str, Any]) -> Dict[str, float]:
    samples = _samples(payload, "frame_samples")
    fps_values: List[float] = []
    weighted_frames = weighted_seconds = 0.0
    for item in samples:
        if ("fps" in item) == ("frames" in item):
            raise InputError("moi mau khung hinh can dung mot trong fps/frames")
        if "fps" in item:
            fps = _number(item.get("fps"), "fps")
            interval = _number(item.get("interval_s"), "interval_s", positive=True)
            weighted_frames += fps * interval
            weighted_seconds += interval
        else:
            frames = _number(item.get("frames"), "frames")
            interval = _number(item.get("interval_s"), "interval_s", positive=True)
            fps = frames / interval
            weighted_frames += frames
            weighted_seconds += interval
        fps_values.append(fps)
    return {
        "avg_fps": weighted_frames / weighted_seconds,
        "min_fps": min(fps_values),
        "p05_fps": percentile(fps_values, 0.05),
        "samples": float(len(fps_values)),
    }


def analyze_payload(payload: Mapping[str, Any]) -> Dict[str, Any]:
    """Tinh cac chi so tu payload da duoc nap/kiem tra."""
    _reject_main_vm(payload)
    target = payload.get("target")
    if (
        not isinstance(target, Mapping)
        or target.get("name") != TEST_VM_NAME
        or target.get("ip") != TEST_VM_IP
    ):
        raise InputError(
            f"target phai la {TEST_VM_NAME} ({TEST_VM_IP}); khong chay target khac"
        )
    return {
        "target": {"name": TEST_VM_NAME, "ip": TEST_VM_IP},
        "tick": _tick_summary(payload),
        "network": _network_summary(payload),
        "frames": _frame_summary(payload),
    }


def _fmt(value: float, digits: int = 2) -> str:
    return f"{value:.{digits}f}"


def render_table(result: Mapping[str, Any]) -> str:
    rows = [
        ("gs001 tick trung binh", _fmt(result["tick"]["avg_ms"]), "ms", int(result["tick"]["samples"])),
        ("gs001 tick p95", _fmt(result["tick"]["p95_ms"]), "ms", int(result["tick"]["samples"])),
        ("guest RX", _fmt(result["network"]["rx_mbps"]), "Mbps", int(result["network"]["samples"])),
        ("guest TX", _fmt(result["network"]["tx_mbps"]), "Mbps", int(result["network"]["samples"])),
        ("guest tong", _fmt(result["network"]["total_mbps"]), "Mbps", int(result["network"]["samples"])),
        ("client FPS trung binh", _fmt(result["frames"]["avg_fps"]), "FPS", int(result["frames"]["samples"])),
        ("client FPS thap nhat", _fmt(result["frames"]["min_fps"]), "FPS", int(result["frames"]["samples"])),
        ("client FPS p05", _fmt(result["frames"]["p05_fps"]), "FPS", int(result["frames"]["samples"])),
    ]
    headers = ("chi so", "gia tri", "don vi", "so mau")
    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(str(cell)))
    line = " | ".join(headers[index].ljust(widths[index]) for index in range(4))
    divider = "-+-".join("-" * width for width in widths)
    body = [" | ".join(str(row[index]).ljust(widths[index]) for index in range(4)) for row in rows]
    target = result["target"]
    return "target: {name} ({ip})\n{line}\n{divider}\n{body}".format(
        name=target["name"], ip=target["ip"], line=line, divider=divider, body="\n".join(body)
    )


def main(argv: Iterable[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=here / "sample_metrics.json",
        help="JSON metrics; mac dinh la du lieu mau offline",
    )
    parser.add_argument("--json", action="store_true", help="in ket qua dang JSON")
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        result = analyze_payload(load_payload(args.input))
    except InputError as exc:
        print(f"LOI: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(render_table(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
