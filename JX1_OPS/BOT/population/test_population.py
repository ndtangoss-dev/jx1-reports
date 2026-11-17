"""Offline tests; no sockets or executable game files."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import unittest

from population import Bot, Config, MapConfig, Planner


NOW = datetime(2026, 11, 17, 19, tzinfo=timezone.utc)


def config(**overrides):
    values = dict(maps=(MapConfig("a", 3, 60), MapConfig("b", 1, 60)),
                  hourly_curve=(1,) * 24, jitter_seconds=0)
    values.update(overrides)
    return Config(**values)


def apply(current, commands):
    state = {bot.bot_id: bot for bot in current}
    for command in commands:
        if command.action == "despawn":
            del state[command.bot_id]
        else:
            if command.bot_id in state:
                raise AssertionError("duplicate spawn")
            state[command.bot_id] = Bot(command.bot_id, command.map)
    return list(state.values())


class PopulationTests(unittest.TestCase):
    def test_default_cap_and_redistribution(self):
        planner = Planner(config())
        self.assertEqual(planner.config.total_cap, 100)
        self.assertEqual(planner.desired(NOW), {"a": 60, "b": 40})

    def test_weighted_rounding(self):
        self.assertEqual(Planner(config(total_cap=7)).desired(NOW), {"a": 5, "b": 2})

    def test_map_capacity_and_zero(self):
        self.assertEqual(Planner(config(total_cap=1000)).desired(NOW), {"a": 60, "b": 60})
        self.assertEqual(sum(Planner(config(total_cap=0)).desired(NOW).values()), 0)
        self.assertEqual(Planner(config(maps=(MapConfig("a", 1, 0),))).desired(NOW), {"a": 0})

    def test_peak_hours(self):
        cfg = Config.from_json(Path(__file__).with_name("population.example.json"))
        planner = Planner(cfg)
        self.assertEqual(sum(planner.desired(NOW).values()), 100)
        self.assertEqual(sum(planner.desired(NOW.replace(hour=3)).values()), 20)

    def test_rolling_window_across_minute_boundary(self):
        planner = Planner(config(max_changes_per_minute=3))
        start = NOW.replace(second=59)
        commands = planner.plan([], start)
        current = apply([], commands)
        self.assertEqual(len(commands), 3)
        self.assertEqual(planner.plan(current, start + timedelta(seconds=2)), [])
        self.assertEqual(len(planner.plan(current, start + timedelta(seconds=60))), 3)

    def test_busy_bots_survive_and_block_spawns(self):
        planner = Planner(config(total_cap=2, max_changes_per_minute=10))
        bots = [Bot(str(i), "unknown", True) for i in range(3)]
        self.assertEqual(planner.plan(bots, NOW), [])

    def test_idle_unknown_bots_removed_first(self):
        planner = Planner(config(total_cap=2))
        commands = planner.plan([Bot("old", "unknown")], NOW)
        self.assertEqual(commands[0].action, "despawn")
        self.assertEqual(len(apply([Bot("old", "unknown")], commands)), 2)

    def test_seed_reproducible_and_jitter_delays(self):
        cfg = config(maps=(MapConfig("a", 1, 10),), total_cap=10,
                     max_changes_per_minute=2, jitter_seconds=120, seed=0)
        first, second = Planner(cfg), Planner(cfg)
        commands = first.plan([], NOW)
        self.assertEqual(commands, second.plan([], NOW))
        current = apply([], commands)
        for elapsed in (60, 121, 182, 303):
            time = NOW + timedelta(seconds=elapsed)
            left, right = first.plan(current, time), second.plan(current, time)
            self.assertEqual(left, right)
            if elapsed == 60:
                self.assertEqual(left, [])  # seed 0: delay is about 101 seconds
            current = apply(current, left)

    def test_converges_and_caps_after_each_command(self):
        planner = Planner(config(max_changes_per_minute=7, jitter_seconds=4))
        current = [Bot("population-1", "b", True)]
        for minute in range(30):
            commands = planner.plan(current, NOW + timedelta(minutes=minute))
            self.assertLessEqual(len(commands), 7)
            for command in commands:
                current = apply(current, [command])
                self.assertLessEqual(len(current), 100)
                for name in ("a", "b"):
                    self.assertLessEqual(sum(bot.map == name for bot in current), 60)
        self.assertEqual(len(current), 100)
        self.assertIn(Bot("population-1", "b", True), current)
        self.assertEqual(planner.plan(current, NOW + timedelta(minutes=31)), [])

    def test_despawn_rate_and_busy(self):
        planner = Planner(config(hourly_curve=(0,) * 24, max_changes_per_minute=2))
        bots = [Bot(str(i), "a", i == 0) for i in range(6)]
        commands = planner.plan(bots, NOW)
        self.assertEqual(len(commands), 2)
        self.assertTrue(all(command.action == "despawn" and command.bot_id != "0"
                            for command in commands))

    def test_invalid_config(self):
        for kwargs in (dict(total_cap=True), dict(total_cap=-1),
                       dict(max_changes_per_minute=0), dict(jitter_seconds=float("nan")),
                       dict(hourly_curve=(1,) * 23), dict(hourly_curve=(2,) * 24),
                       dict(maps=()), dict(maps=(MapConfig("a", 0, 3),)),
                       dict(maps=(MapConfig("a", 1, -1),)),
                       dict(maps=(MapConfig("a", 1, 3), MapConfig("a", 2, 4)))):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                config(**kwargs)

    def test_invalid_snapshot_and_time(self):
        planner = Planner(config())
        for bots in ([Bot("same", "a"), Bot("same", "b")], [Bot("", "a")],
                     [Bot("a", "b", 1)]):
            with self.assertRaises(ValueError):
                planner.plan(bots, NOW)
        planner.plan([], NOW)
        with self.assertRaises(ValueError):
            planner.plan([], NOW - timedelta(seconds=1))


if __name__ == "__main__":
    unittest.main()
