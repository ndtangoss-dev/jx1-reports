"""Mỗi bot một process; timeout hủy cả bot để không để bước treo chạy nền."""

from contextlib import redirect_stderr, redirect_stdout
from dataclasses import dataclass, field
import hashlib
import math
import multiprocessing
import os
import re
import time


@dataclass(frozen=True)
class Step:
    name: str
    run: object
    expected: str
    timeout: float = 3.0
    severity: str = "major"

    def __post_init__(self):
        if not self.name or not callable(self.run) or not self.expected:
            raise ValueError("Bước cần tên, hàm chạy và kỳ vọng")
        if not math.isfinite(self.timeout) or self.timeout <= 0:
            raise ValueError("Thời hạn phải hữu hạn và >0")
        if self.severity not in ("blocker", "major", "minor"):
            raise ValueError("Độ nặng không hợp lệ")


@dataclass(frozen=True)
class Scenario:
    name: str
    steps: tuple

    def __post_init__(self):
        if not re.fullmatch(r"[a-z][a-z0-9_]*", self.name) or not self.steps:
            raise ValueError("Kịch bản cần tên an toàn và ít nhất một bước")
        if len({step.name for step in self.steps}) != len(self.steps):
            raise ValueError("Tên bước không được trùng")


@dataclass(frozen=True)
class Config:
    host: str
    port: int
    secrets: tuple = ()

    def __post_init__(self):
        # E-05a chỉ cho máy chủ giả cục bộ. Không sửa guard của BOT.
        if (self.host != "127.0.0.1" or isinstance(self.port, bool)
                or not isinstance(self.port, int) or not 1 <= self.port <= 65535):
            raise ValueError("E-05a chỉ cho 127.0.0.1 và cổng 1..65535 của máy chủ giả")


class Redactor:
    def __init__(self, secrets=()):
        values = list(secrets) + [value for key, value in os.environ.items()
                                 if re.search(r"PASSWORD|PASSWD|SECRET|TOKEN|KEY|ACCOUNT|ROLE", key, re.I)]
        variants = set()
        for value in values:
            if not value:
                continue
            value = str(value)
            raw = value.encode("utf-8")
            variants.update((value, raw.hex(), raw.hex().upper(), hashlib.md5(raw).hexdigest(),
                             hashlib.md5(raw).hexdigest().upper()))
            try:
                number = int(value, 0)
                if 0 <= number <= 0xFFFFFFFF:
                    variants.update((str(number), hex(number), number.to_bytes(4, "little").hex()))
            except ValueError:
                pass
        self.values = sorted(variants, key=len, reverse=True)

    def clean(self, value, limit=1600):
        text = str(value)
        for secret in self.values:
            text = text.replace(secret, "[ẨN]")
        text = re.sub(r"(?i)\b(password|passwd|token|secret|client_key|account|role|key)\s*[:=]\s*(?:\"[^\"]*\"|'[^']*'|[^\s,;]+)",
                      r"\1=[ẨN]", text)
        text = "".join(char if char in "\n\t" or ord(char) >= 32 else "?" for char in text)
        return text[:limit] + ("…[cắt]" if len(text) > limit else "")


@dataclass
class Result:
    bot: str
    step: str
    status: str
    seconds: float
    message: str
    logs: list = field(default_factory=list)
    packets: list = field(default_factory=list)


class SkipStep(Exception):
    """Kịch bản chủ động bỏ qua bước không áp dụng."""


class Context:
    def __init__(self, bot, config, redactor, connection):
        self.bot, self.config = bot, config
        self.redactor, self.connection = redactor, connection
        self.state = {}
        self.logs, self.packets = [], []

    def log(self, message):
        if len(self.logs) < 20:
            self.logs.append(self.redactor.clean(message, 400))
            self.connection.send(("evidence", self.logs, self.packets))

    def packet(self, direction, payload):
        if direction not in ("gửi", "nhận") or not payload or len(self.packets) >= 4:
            return
        # Không ghi raw auth/GUID/key/unknown body. Giữ ID + độ dài + hex đã che.
        # Mọi byte ngoài ID bị thay bằng 00, kể cả ID chưa hỗ trợ.
        data = bytes(payload[:256])
        self.packets.append({"direction": direction, "id": data[0], "size": len(payload),
                             "hex": (data[:1] + bytes(len(data) - 1)).hex(),
                             "masked": True})
        self.connection.send(("evidence", self.logs, self.packets))

    def write(self, text):
        # Không đưa stdout/stderr tự do ra console; log có giới hạn ở trên.
        return len(text)

    def flush(self):
        pass


def _worker(connection, scenario, bot, config, redactor):
    context = Context(bot, config, redactor, connection)
    try:
        with redirect_stdout(context), redirect_stderr(context):
            for index, step in enumerate(scenario.steps):
                context.logs, context.packets = [], []
                connection.send(("start", index))
                started = time.monotonic()
                try:
                    answer = step.run(context)
                    if answer is False:
                        raise AssertionError("Không đạt kỳ vọng")
                    status, message = "PASS", "Đạt kỳ vọng"
                except SkipStep as error:
                    status, message = "BỎ QUA", redactor.clean(error)
                except BaseException as error:
                    status = "FAIL"
                    message = redactor.clean(type(error).__name__ + ": " + str(error))
                elapsed = time.monotonic() - started
                if elapsed > step.timeout:
                    status, message = "FAIL", "Timeout: vượt thời hạn bước"
                connection.send(("result", Result(bot, step.name, status, elapsed, message,
                                                   context.logs, context.packets)))
                if status == "FAIL":
                    break
    except BaseException:
        # Parent đánh FAIL nếu IPC/worker kết thúc sớm. Không phát traceback chứa bí mật.
        pass
    finally:
        # Cleanup cũng thuộc vòng giám sát của parent, không join vô hạn.
        with redirect_stdout(context), redirect_stderr(context):
            for value in context.state.values():
                try:
                    close = getattr(value, "close", None)
                    if close:
                        close()
                except BaseException:
                    pass
        try:
            connection.close()
        except OSError:
            pass


def _stop(process):
    if process.is_alive():
        process.terminate()
        process.join(0.1)
    if process.is_alive():
        process.kill()
        process.join(0.1)
    else:
        process.join(0)
    if process.is_alive():
        raise RuntimeError("Không thể dừng worker; dừng toàn lượt tester")
    process.close()


def run_scenario(scenario, bots, config, workers=1):
    """Tuần tự workers=1, song song tối đa 5; state độc lập trong từng process.

    Callable phải ở cấp module (pickle được trên Windows spawn). Bước FAIL dừng bot;
    bot khác tiếp tục. False = FAIL, None/True = PASS, SkipStep = BỎ QUA.
    """
    if workers not in range(1, 6) or not bots or len(bots) != len(set(bots)):
        raise ValueError("Cần bot không trùng và workers 1..5")
    if any(not re.fullmatch(r"bot0[1-5]", bot) for bot in bots):
        raise ValueError("Chỉ cho bí danh bot01..bot05")
    redactor = Redactor(config.secrets)
    pending, active, results = list(bots), [], {}
    mp = multiprocessing.get_context("spawn")
    try:
        while pending or active:
            while pending and len(active) < workers:
                bot = pending.pop(0)
                parent, child = mp.Pipe(duplex=False)
                process = mp.Process(target=_worker, args=(child, scenario, bot, config, redactor), daemon=True)
                process.start()
                child.close()
                active.append({"bot": bot, "pipe": parent, "process": process, "index": None,
                               "deadline": time.monotonic() + 10, "start": time.monotonic(),
                               "logs": [], "packets": []})
                results[bot] = []
            for item in active[:]:
                pipe, process, bot = item["pipe"], item["process"], item["bot"]
                finished = False
                # Giới hạn số message mỗi lượt để worker không làm đói watchdog.
                for _ in range(32):
                    if time.monotonic() >= item["deadline"]:
                        break
                    try:
                        if not pipe.poll():
                            break
                        message = pipe.recv()
                    except (EOFError, OSError):
                        finished = True
                        break
                    if message[0] == "start":
                        item.update(index=message[1], start=time.monotonic(), logs=[], packets=[])
                        item["deadline"] = item["start"] + scenario.steps[item["index"]].timeout
                    elif message[0] == "evidence":
                        item["logs"], item["packets"] = message[1:]
                    elif message[0] == "result":
                        results[bot].append(message[1])
                        item["index"] = None
                        item["deadline"] = time.monotonic() + 1  # cleanup/start kế tiếp
                        if message[1].status == "FAIL" or len(results[bot]) == len(scenario.steps):
                            finished = True
                            break
                expired = time.monotonic() >= item["deadline"]
                if expired or finished or (not process.is_alive() and not pipe.poll()):
                    if len(results[bot]) < len(scenario.steps) and not any(r.status == "FAIL" for r in results[bot]):
                        index = len(results[bot])
                        results[bot].append(Result(bot, scenario.steps[index].name, "FAIL",
                            time.monotonic() - item["start"],
                            "Timeout: vượt thời hạn bước" if expired else "Worker kết thúc trước khi trả kết quả",
                            item["logs"], item["packets"]))
                    _stop(process)
                    pipe.close()
                    active.remove(item)
                    for step in scenario.steps[len(results[bot]):]:
                        results[bot].append(Result(bot, step.name, "BỎ QUA", 0,
                                                   "Bot đã dừng sau lỗi bước trước"))
            if active:
                time.sleep(0.005)
    finally:
        for item in active:
            _stop(item["process"])
            item["pipe"].close()
    return [result for bot in bots for result in results[bot]]
