"""Offline population planning only; no server or transport integration.

Apply returned commands to the authoritative snapshot before calling plan again.
Use one persistent Planner per population; now is a nondecreasing datetime.
"""

from collections import deque
from dataclasses import dataclass
from datetime import datetime
import json
import math
from pathlib import Path
import random


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(name + " must be an integer >= " + str(minimum))
    return value


def _number(value, name, positive=False):
    if (type(value) not in (int, float) or not math.isfinite(value)
            or value < 0 or (positive and value == 0)):
        raise ValueError(name + " must be finite and nonnegative (positive for weights)")
    return value


@dataclass(frozen=True)
class MapConfig:
    name: str
    weight: float
    cap: int


@dataclass(frozen=True)
class Config:
    maps: tuple
    hourly_curve: tuple
    total_cap: int = 100
    max_changes_per_minute: int = 10
    jitter_seconds: float = 2.0
    seed: int = 0

    def __post_init__(self):
        object.__setattr__(self, "maps", tuple(self.maps))
        object.__setattr__(self, "hourly_curve", tuple(self.hourly_curve))
        _integer(self.total_cap, "total_cap")
        _integer(self.max_changes_per_minute, "max_changes_per_minute", 1)
        _integer(self.seed, "seed")
        _number(self.jitter_seconds, "jitter_seconds")
        if len(self.hourly_curve) != 24:
            raise ValueError("hourly_curve must contain hours 0..23")
        for value in self.hourly_curve:
            if _number(value, "hourly_curve") > 1:
                raise ValueError("hourly_curve values must be in [0, 1]")
        names = set()
        if not self.maps:
            raise ValueError("maps must not be empty")
        for entry in self.maps:
            if not isinstance(entry, MapConfig) or not isinstance(entry.name, str) or not entry.name:
                raise ValueError("each map needs a nonempty string name")
            if entry.name in names:
                raise ValueError("duplicate map name")
            names.add(entry.name)
            _number(entry.weight, "weight", positive=True)
            _integer(entry.cap, "map cap")
        if not math.isfinite(sum(entry.weight for entry in self.maps)):
            raise ValueError("sum of weights must be finite")

    @classmethod
    def from_json(cls, path):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        data["maps"] = tuple(MapConfig(**entry) for entry in data["maps"])
        return cls(**data)


@dataclass(frozen=True)
class Bot:
    bot_id: str
    map: str
    busy: bool = False


@dataclass(frozen=True)
class Command:
    action: str
    bot_id: str
    map: str


class Planner:
    def __init__(self, config):
        self.config = config
        self._rng = random.Random(config.seed)
        self._events = deque()
        self._last_now = None
        self._next_change = float("-inf")
        self._serial = 0

    def desired(self, now):
        """Hour uses the supplied datetime's local hour; curve is stepwise.

        Allocate floor(total_cap * hourly_curve[hour]) by capped weighted
        largest remainders. Unfillable seats are redistributed to other maps.
        """
        if not isinstance(now, datetime):
            raise ValueError("now must be a datetime")
        maps = self.config.maps
        counts = {entry.name: 0 for entry in maps}
        remaining = min(math.floor(self.config.total_cap * self.config.hourly_curve[now.hour]),
                        sum(entry.cap for entry in maps))
        while remaining:
            active = [entry for entry in maps if counts[entry.name] < entry.cap]
            # Normalize first to avoid overflow of remaining * weight.
            weight = sum(entry.weight for entry in active)
            quotas = {entry.name: remaining * (entry.weight / weight) for entry in active}
            saturated = [entry for entry in active
                         if quotas[entry.name] >= entry.cap - counts[entry.name]]
            if saturated:
                for entry in saturated:
                    remaining -= entry.cap - counts[entry.name]
                    counts[entry.name] = entry.cap
                continue
            assigned = 0
            for entry in active:
                amount = min(entry.cap - counts[entry.name], math.floor(quotas[entry.name]))
                counts[entry.name] += amount
                assigned += amount
            remaining -= assigned
            if remaining:
                ordered = sorted(active, key=lambda e: (-(quotas[e.name] % 1), e.name))
                for entry in ordered:
                    if remaining and counts[entry.name] < entry.cap:
                        counts[entry.name] += 1
                        remaining -= 1
        return counts

    def plan(self, current, now):
        """Return ordered despawn/spawn commands, respecting rolling limits.

        Busy bots may keep an already over-cap snapshot above its target;
        only idle bots can be removed. No spawn increases an exceeded cap.
        Jitter inserts a seeded random delay between nonempty batches.
        """
        targets = self.desired(now)
        stamp = now.timestamp()
        if self._last_now is not None and stamp < self._last_now:
            raise ValueError("now must not go backwards")
        bots = list(current)
        ids = set()
        for bot in bots:
            if (not isinstance(bot, Bot) or not isinstance(bot.bot_id, str)
                    or not bot.bot_id or not isinstance(bot.map, str)
                    or not bot.map or type(bot.busy) is not bool):
                raise ValueError("current must contain valid Bot records")
            if bot.bot_id in ids:
                raise ValueError("duplicate bot_id")
            ids.add(bot.bot_id)
        self._last_now = stamp
        while self._events and stamp - self._events[0] >= 60:
            self._events.popleft()
        budget = self.config.max_changes_per_minute - len(self._events)
        if budget <= 0 or stamp < self._next_change:
            return []
        counts = {name: 0 for name in targets}
        for bot in bots:
            counts[bot.map] = counts.get(bot.map, 0) + 1
        commands = []
        idle = sorted((bot for bot in bots if not bot.busy), key=lambda b: b.bot_id)
        self._rng.shuffle(idle)
        total = len(bots)
        for bot in idle:
            if len(commands) >= budget:
                break
            if counts[bot.map] > targets.get(bot.map, 0):
                commands.append(Command("despawn", bot.bot_id, bot.map))
                counts[bot.map] -= 1
                total -= 1
        names = sorted(targets)
        self._rng.shuffle(names)
        for name in names:
            while (len(commands) < budget and counts[name] < targets[name]
                   and total < self.config.total_cap):
                self._serial += 1
                bot_id = "population-" + str(self._serial)
                if bot_id in ids:
                    continue
                ids.add(bot_id)
                commands.append(Command("spawn", bot_id, name))
                counts[name] += 1
                total += 1
        if commands:
            self._events.extend([stamp] * len(commands))
            self._next_change = stamp + self._rng.uniform(0, self.config.jitter_seconds)
        return commands
