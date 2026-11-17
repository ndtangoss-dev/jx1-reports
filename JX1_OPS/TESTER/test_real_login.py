"""E-09a: policy offline và codec qua loopback; không gọi endpoint VM."""

from contextlib import redirect_stderr
from datetime import date
import hashlib
import io
import os
from pathlib import Path
import secrets
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

from test_full_cycle import cycle_server
from JX1_OPS.BOT import packets
from JX1_OPS.TESTER.core import Config, Context, Redactor, Scenario, run_scenario
from JX1_OPS.TESTER.real_login import REAL_LOGIN, guarded_channel, login_real
from JX1_OPS.TESTER.run import main
from JX1_OPS.TESTER.scenarios import connect_fake, login_cycle
from JX1_OPS.TESTER.visibility import connect_visibility


def environment(port):
    account = secrets.token_hex(6)
    return {"JX1_BOT01_" + name: value for name, value in {
        "ACCOUNT": account, "PASSWORD": secrets.token_hex(8), "ROLE": account,
        "CLIENT_KEY": str(port), "REGION": "1", "ENTER_MAP": "1", "OBSERVED_ONLINE": "0",
    }.items()}


class RealLoginTests(unittest.TestCase):
    def context(self, config):
        return Context("bot01", config, Redactor(), Mock())

    def test_exact_allowlist_before_any_socket_or_dns(self):
        hosts = ("192.168.1.50", "192.168.56.151", "192.168.56.149", "0.0.0.0",
                 "localhost", "example.invalid", "::1", "::ffff:192.168.56.150",
                 "192.168.056.150", "192.168.56.150 ", "3232249990", "127.0.0.2")
        with patch.object(socket, "socket") as raw, patch.object(socket, "getaddrinfo") as dns, \
                patch.object(socket, "create_connection") as connect:
            with self.assertRaises(ValueError):
                Config("192.168.56.150", 56722)
            for host in hosts:
                for opt_in in (False, True):
                    with self.subTest(host=host, opt_in=opt_in), self.assertRaises(ValueError):
                        Config(host, 56722, allow_test_vm=opt_in)
            allowed = Config("192.168.56.150", 56722, allow_test_vm=True)
            for host in (*hosts, "127.0.0.1"):
                with self.subTest(redirect=host), self.assertRaises(ValueError):
                    guarded_channel(self.context(allowed), host, 51189, game=True)
            for port in (0, 80, 56722, 65536, True, "51189"):
                with self.subTest(port=port), self.assertRaises(ValueError):
                    guarded_channel(self.context(allowed), allowed.host, port, game=True)
            for port in (51189, 80, True):
                with self.assertRaises(ValueError):
                    Config(allowed.host, port, allow_test_vm=True)
            for entry in (connect_fake, login_cycle, connect_visibility):
                with self.assertRaises(ValueError):
                    entry(self.context(allowed))
            connect.assert_not_called()
            dns.assert_not_called()
            raw.assert_not_called()

    def test_opt_in_endpoints_use_guard_with_mock_only(self):
        config = Config("192.168.56.150", 56722, allow_test_vm=True)
        with patch.object(socket, "create_connection") as connect, \
                patch("JX1_OPS.TESTER.real_login.Channel") as channel:
            context = self.context(config)
            guarded_channel(context, config.host, 56722)
            guarded_channel(context, config.host, 51189, game=True)
            self.assertEqual([call.args[0] for call in connect.call_args_list],
                             [(config.host, 56722), (config.host, 51189)])
            self.assertEqual(channel.return_value.handshake.call_count, 2)
        with patch.object(socket, "create_connection") as connect:
            with self.assertRaises(ValueError):
                guarded_channel(self.context(Config("127.0.0.1", 12345, allow_test_vm=True)),
                                config.host, 51189, game=True)
            connect.assert_not_called()

    def test_cli_rejects_unsafe_modes_without_worker(self):
        with patch("JX1_OPS.TESTER.run.run_scenario") as run, redirect_stderr(io.StringIO()):
            for scenario, host, extra in (("real_login", "192.168.56.150", []),
                    ("real_login", "192.168.1.50", ["--allow-test-vm"]),
                    ("full_cycle", "192.168.56.150", ["--allow-test-vm"]),
                    ("visibility", "127.0.0.1", ["--allow-test-vm"])):
                with self.subTest(scenario=scenario, host=host), self.assertRaises(SystemExit) as error:
                    main(["--scenario", scenario, "--bots", "bot01", "--host", host,
                          "--port", "56722", "--out", ".", *extra])
                self.assertEqual(error.exception.code, 2)
            run.assert_not_called()

    def test_missing_or_invalid_environment_before_socket(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(socket, "create_connection") as connect:
            with self.assertRaisesRegex(ValueError, "Thiếu biến"):
                login_real(self.context(Config("127.0.0.1", 12345)))
            values = environment(12345)
            for name, invalid in (("CLIENT_KEY", secrets.token_hex(10)), ("OBSERVED_ONLINE", "100"),
                                  ("REGION", "0"), ("ROLE", "")):
                with patch.dict(os.environ, {**values, "JX1_BOT01_" + name: invalid}), \
                        self.subTest(name=name), self.assertRaises(ValueError):
                    login_real(self.context(Config("127.0.0.1", 12345)))
            connect.assert_not_called()

    def test_cli_loopback_login_role_sync_hold_30s_and_redaction(self):
        with tempfile.TemporaryDirectory() as temp:
            with cycle_server(real=True) as (config, records, errors):
                values = environment(config.port)
                completed = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("run.py")),
                    "--scenario", "real_login", "--bots", "bot01", "--host", config.host,
                    "--port", str(config.port), "--out", temp], env={**os.environ, **values},
                    capture_output=True, timeout=42)
            self.assertEqual(completed.returncode, 0, completed.stderr.decode("utf-8"))
            self.assertEqual(errors, [])
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0][2], [])  # Không RUN/SKILL trong real_login.
            self.assertEqual(records[0][1][:3], [packets.C2S.PING, packets.C2S.SYNC_END, packets.C2S.CP_LOCK])
            self.assertGreater(records[0][1].count(packets.C2S.PING), 10)
            report = (Path(temp) / f"{date.today().isoformat()}-real_login.md").read_text(encoding="utf-8")
            self.assertEqual(report.count("PASS ("), 5)
            self.assertRegex(report, r"\| bot01 \| PASS \([^\n]*\| PASS \(30\.")
            self.assertIn("[CHƯA KIỂM]", report)
            self.assertNotIn("không đăng nhập thật", report)
            evidence = report + completed.stdout.decode("utf-8") + completed.stderr.decode("utf-8")
            for name in ("ACCOUNT", "PASSWORD", "ROLE", "CLIENT_KEY"):
                value = values["JX1_BOT01_" + name]
                for variant in (value, value.encode().hex(), hashlib.md5(value.encode()).hexdigest().upper()):
                    self.assertNotIn(variant, evidence)
            self.assertEqual(len(list(Path(temp).glob("BUG-*.md"))), 0)

    def test_permit_redirects_rejected_before_second_socket(self):
        short = Scenario("real_redirect", REAL_LOGIN.steps[:3])
        for host, port in (("192.168.1.50", 51189), ("192.168.56.151", 51189),
                           ("192.168.56.150", 51189)):
            with self.subTest(host=host), cycle_server(real=True, permit_host=host, permit_port=port) as (config, records, errors):
                context = self.context(config)
                with patch.dict(os.environ, environment(config.port)):
                    try:
                        # Dùng socket thật chỉ cho Bishop loopback; mọi redirect phải bị chặn
                        # trước create_connection lần hai (không mock thành kết nối thành công).
                        short.steps[0].run(context)
                        short.steps[1].run(context)
                        with patch.object(socket, "create_connection") as connect, self.assertRaises(ValueError):
                            short.steps[2].run(context)
                        connect.assert_not_called()
                    finally:
                        for name in ("gateway", "session"):
                            value = context.state.get(name)
                            if value is not None:
                                value.close()
            self.assertEqual(records, [])
            self.assertEqual(errors, [])

    def test_missing_role_fails_and_stops_remaining_steps(self):
        with cycle_server(real=True, missing=True) as (config, records, errors):
            with patch.dict(os.environ, environment(config.port)):
                results = run_scenario(REAL_LOGIN, ["bot01"], config)
        self.assertEqual([result.status for result in results], ["PASS", "FAIL", "BỎ QUA", "BỎ QUA", "BỎ QUA"])
        self.assertEqual(records, [])
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
