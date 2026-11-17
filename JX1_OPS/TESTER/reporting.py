"""Markdown đã che bí mật; BUG tăng số và khử trùng trong vùng lock."""

from contextlib import contextmanager
from datetime import date
import hashlib
import os
from pathlib import Path
import re
import subprocess

from .core import Redactor


def cell(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(
        ">", "&gt;").replace("|", "&#124;").replace("`", "&#96;").replace("\n", "<br>")


def revision():
    root = Path(__file__).resolve().parents[2]
    values = []
    for args in (("branch", "--show-current"), ("rev-parse", "HEAD")):
        try:
            completed = subprocess.run(["git", *args], cwd=root, capture_output=True,
                                       text=True, timeout=2, check=True)
            values.append(completed.stdout.strip())
        except (OSError, subprocess.SubprocessError):
            values.append("chưa xác định")
    return tuple(values)


@contextmanager
def report_lock(out):
    lock = out / ".tester.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise RuntimeError("Thư mục báo cáo đang khóa; kiểm tra lượt chạy trước, không ghi đè") from None
    try:
        os.close(descriptor)
        yield
    finally:
        lock.unlink()


def evidence(result, redactor):
    lines = ["Log:"] + ["- " + cell(redactor.clean(log, 400)) for log in result.logs[:20]]
    if not result.logs:
        lines.append("- Không có log")
    lines.append("Gói tin lỗi (tối đa 256 byte/gói; body đã che bằng 00):")
    for packet in result.packets[:4]:
        # Tái che tại ranh giới ghi file, không tin dữ liệu Result truyền vào.
        packet_id = int(packet["id"])
        if not 0 <= packet_id <= 255 or packet["direction"] not in ("gửi", "nhận"):
            raise ValueError("Bằng chứng gói không hợp lệ")
        size = max(1, int(packet["size"]))
        safe_hex = (bytes([packet_id]) + bytes(min(size, 256) - 1)).hex()
        lines.append(f'- {packet["direction"]}; ID=0x{packet_id:02x}; {size} byte; hex={safe_hex}')
    if not result.packets:
        lines.append("- Không có gói tin lỗi quan sát được")
    return "\n".join(lines)


def _bug(out, scenario, step, result, branch, commit, redactor):
    message = redactor.clean(result.message)
    fingerprint = hashlib.sha256((scenario.name + "\0" + step.name + "\0" + message).encode()).hexdigest()
    largest = 0
    for path in sorted(out.glob("BUG-*.md")):
        match = re.fullmatch(r"BUG-(\d+)\.md", path.name)
        if not match:
            continue
        largest = max(largest, int(match[1]))
        text = path.read_text(encoding="utf-8")
        if f"Fingerprint: {fingerprint}\n" in text and re.search(r"^Status: OPEN$", text, re.M):
            count = len(re.findall(r"^tái hiện lần \d+", text, re.M)) + 2
            with path.open("a", encoding="utf-8") as stream:
                stream.write(f"\ntái hiện lần {count}: {date.today().isoformat()}, {result.bot}; "
                             f"nhánh {cell(redactor.clean(branch))}; commit {cell(redactor.clean(commit))}\n")
            return path.name
    path = out / f"BUG-{largest + 1:03d}.md"
    reproduction = "\n".join(f"{index}. {cell(redactor.clean(s.name))}" for index, s in
                              enumerate(scenario.steps[:scenario.steps.index(step) + 1], 1))
    text = (f"# {path.stem}\n\nStatus: OPEN\nFingerprint: {fingerprint}\n\n"
            f"Kịch bản: {scenario.name}\n\nBot: {result.bot}\n\n"
            f"Bước lỗi: {cell(redactor.clean(step.name))}\n\nĐộ nặng: {step.severity}\n\n"
            f"Nhánh: {cell(redactor.clean(branch))}\n\nCommit: {cell(redactor.clean(commit))}\n\n"
            f"Bước tái hiện (cùng endpoint đã duyệt và cấu hình lượt chạy):\n\n{reproduction}\n\n"
            f"Kỳ vọng: {cell(redactor.clean(step.expected))}\n\nThực tế: {cell(message)}\n\n"
            f"Thời gian: {result.seconds:.3f}s\n\n{evidence(result, redactor)}\n")
    with path.open("x", encoding="utf-8") as stream:
        stream.write(text)
    return path.name


def write_report(out, scenario, bots, results, secrets=(), branch=None, commit=None):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    redactor = Redactor(secrets)
    if branch is None or commit is None:
        branch, commit = revision()
    with report_lock(out):
        bugs = {}
        for result in results:
            if result.status == "FAIL":
                step = next(s for s in scenario.steps if s.name == result.step)
                bugs[(result.bot, result.step)] = _bug(out, scenario, step, result, branch, commit, redactor)
        scope = ("Kịch bản real_login; PASS chỉ xác nhận bước theo profile BOT tại endpoint được cấu hình. "
                 "ABI/gameplay/lưu dữ liệu gs001 thật: **[CHƯA KIỂM]**."
                 if scenario.name == "real_login" else
                 "gs001 thật: **chưa kiểm**. Chỉ máy chủ giả cục bộ; không đăng nhập thật.")
        lines = [f"# {scenario.name} — {date.today().isoformat()}", "", scope, "",
                 f"Nhánh: {cell(redactor.clean(branch))}; commit: {cell(redactor.clean(commit))}", "",
                 "| Bot | " + " | ".join(cell(redactor.clean(s.name)) for s in scenario.steps) + " |",
                 "| --- | " + " | ".join("---" for _ in scenario.steps) + " |"]
        lookup = {(r.bot, r.step): r for r in results}
        for bot in bots:
            cells = [f"{lookup[bot, step.name].status} ({lookup[bot, step.name].seconds:.3f}s)"
                     for step in scenario.steps]
            lines.append("| " + bot + " | " + " | ".join(cells) + " |")
        for result in results:
            lines.extend(("", f"## {result.bot} / {cell(redactor.clean(result.step))}", "",
                          cell(redactor.clean(result.message)), "", evidence(result, redactor)))
            if (result.bot, result.step) in bugs:
                lines.extend(("", f"BUG: [{bugs[result.bot, result.step]}]({bugs[result.bot, result.step]})"))
        base = out / f"{date.today().isoformat()}-{scenario.name}.md"
        # Giữ lịch sử khi chạy lại cùng ngày; báo cáo đầu giữ đúng tên yêu cầu.
        path, count = base, 2
        while path.exists():
            path = base.with_name(f"{base.stem}-{count}.md")
            count += 1
        with path.open("x", encoding="utf-8") as stream:
            stream.write("\n".join(lines) + "\n")
    return path
