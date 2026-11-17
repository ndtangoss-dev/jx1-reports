"""Nạp package cạnh file khi -I không đưa cwd vào sys.path."""

from pathlib import Path
import sys


def load_packages():
    root = str(Path(__file__).resolve().parents[2])
    if root not in sys.path:
        # Đường dẫn tuyệt đối từ __file__, không dùng cwd/PYTHONPATH. Spawn kế thừa.
        sys.path.insert(0, root)
