#!/usr/bin/env python3
"""Sinh bảng Markdown từ front matter của các file TASKS/*.md."""

import argparse
from pathlib import Path
import sys


COLUMNS = ("id", "title", "status", "agent", "branch", "updated")


def read_front_matter(path):
    """Đọc các cặp khóa: giá trị trong phần front matter đầu file."""
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, separator, value = line.split("#", 1)[0].partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    return None


def markdown_row(values):
    cells = [value.replace("\\", "\\\\").replace("|", "\\|") for value in values]
    return "| " + " | ".join(cells) + " |"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Thư mục chứa TASKS (mặc định: JX1_OPS tính từ vị trí script).",
    )
    args = parser.parse_args()

    tasks = []
    for path in sorted((args.root / "TASKS").glob("*.md")):
        if path.name.startswith("_") or not path.is_file():
            continue
        fields = read_front_matter(path)
        if fields is not None:
            tasks.append(fields)

    print(markdown_row(COLUMNS))
    print(markdown_row(["---"] * len(COLUMNS)))
    for fields in sorted(tasks, key=lambda task: task.get("id", "")):
        print(markdown_row([fields.get(column, "") for column in COLUMNS]))


if __name__ == "__main__":
    main()
