"""Offline tests only: generated synthetic inputs and in-memory adapters."""

import contextlib
import hashlib
import io
import json
import os
import secrets
import socket
import unittest
from dataclasses import replace
from unittest.mock import Mock, patch

import jxadm


ACCOUNT = "offline_fixture"
BEGIN = "2026-11-17T00:00:00"
END = "2026-11-18T00:00:00"


class FakeCursor:
    def __init__(self, fail_at=None, rowcount=1, rows=None):
        self.calls = []
        self.fail_at = fail_at
        self.rowcount = rowcount
        self.description = ("columns",) if rows is not None else None
        self.rows = rows
        self.closed = False

    def execute(self, sql, parameters):
        self.calls.append((sql, parameters))
        if len(self.calls) == self.fail_at:
            raise RuntimeError("synthetic database failure")

    def fetchall(self):
        return self.rows

    def close(self):
        self.closed = True


class FakeConnection:
    def __init__(self, **kwargs):
        self.autocommit = True
        self.handle = FakeCursor(**kwargs)
        self.committed = self.rolled_back = self.closed = False

    def cursor(self):
        return self.handle

    def commit(self):
        self.committed = True

    def rollback(self):
        self.rolled_back = True

    def close(self):
        self.closed = True


class PlansTest(unittest.TestCase):
    def setUp(self):
        self.password = secrets.token_hex(16)

    def create(self):
        return jxadm.account_plan("create", ACCOUNT, password=self.password, begin=BEGIN, end=END)

    def test_create_binds_both_tables_and_explicit_dates(self):
        plan = self.create()
        self.assertEqual(len(plan.statements), 3)
        info, habitus = plan.statements[1:]
        self.assertEqual(info.sql, "INSERT INTO [Account_Info] ([cAccName], [cPassword], [iClientID]) VALUES (?, ?, ?);")
        self.assertEqual(info.parameters[0], ACCOUNT)
        digest = hashlib.md5(self.password.encode("ascii"), usedforsecurity=False).hexdigest().upper()
        self.assertEqual(info.parameters[1].value, digest)
        self.assertEqual(habitus.parameters, (ACCOUNT, 0, BEGIN, END, 0, 0, 0))
        self.assertIn("[Account_Habitus]", habitus.sql)
        self.assertIn("UPDLOCK, HOLDLOCK", plan.statements[0].sql)

    def test_every_sql_parameter_is_bound(self):
        plans = [self.create(), jxadm.account_plan("lock", ACCOUNT),
                 jxadm.account_plan("unlock", ACCOUNT, password=self.password),
                 jxadm.account_plan("reset-password", ACCOUNT, password=self.password),
                 jxadm.account_plan("mark-bot", ACCOUNT, is_bot=True),
                 jxadm.account_plan("online", ACCOUNT), jxadm.account_plan("online")]
        for plan in plans:
            for statement in plan.statements:
                with self.subTest(operation=plan.operation):
                    self.assertEqual(statement.sql.count("?"), len(statement.parameters))
                    self.assertNotIn(ACCOUNT, statement.sql)
                    self.assertNotIn(self.password, statement.sql)
                    self.assertNotIn("ServerList", statement.sql)

    def test_lock_and_unlock_do_not_guess_session_or_billing_flags(self):
        lock = jxadm.account_plan("lock", ACCOUNT)
        self.assertEqual(lock.statements[0].parameters[0].value, jxadm.LOCK_MARKER)
        self.assertIsNone(__import__("re").fullmatch(r"[0-9A-F]{32}", jxadm.LOCK_MARKER))
        for name in ("lock", "unlock", "reset-password"):
            statement = jxadm.account_plan(name, ACCOUNT, password=self.password).statements[0]
            self.assertEqual(statement.sql, "UPDATE [Account_Info] SET [cPassword] = ? WHERE [cAccName] = ?;")
        self.assertIn("NEW password", lock.notes[-1])

    def test_bot_metadata_only_with_both_values(self):
        for flag in (True, False):
            statement = jxadm.account_plan("mark-bot", ACCOUNT, is_bot=flag).statements[0]
            self.assertIn("[Account_BotMetadata]", statement.sql)
            self.assertIn("IF @@ROWCOUNT = 0", statement.sql)
            self.assertEqual(statement.parameters, (ACCOUNT, int(flag), ACCOUNT, ACCOUNT, int(flag)))
            self.assertNotIn("[iFlag]", statement.sql)
        with self.assertRaises(ValueError):
            jxadm.account_plan("mark-bot", ACCOUNT, is_bot=1)

    def test_online_reports_observations_without_claiming_online_predicate(self):
        plan = jxadm.account_plan("online")
        self.assertEqual(plan.statements[0].sql,
                         "SELECT [cAccName], [iClientID], [dLoginDate], [dLogoutDate] FROM [Account_Info];")
        self.assertIn("unverified", plan.notes[-1])

    def test_invalid_inputs_are_rejected(self):
        for account in ("", "MixedCase", "x'; DROP TABLE Account_Info;--", "x\n", "tên"):
            with self.subTest(account=account), self.assertRaises(ValueError):
                jxadm.account_plan("lock", account)
        for begin, end in ((END, BEGIN), (BEGIN, BEGIN), ("bad", END),
                           ("1700-01-01T00:00:00", END)):
            with self.subTest(begin=begin), self.assertRaises(ValueError):
                jxadm.account_plan("create", ACCOUNT, begin=begin, end=end)
        for password in ("", "nonascii-\u00e9", "line\nbreak"):
            with self.assertRaises(ValueError):
                jxadm.password_parameter(password)

    def test_password_and_hash_absent_from_preview_and_repr(self):
        plan = self.create()
        digest = plan.statements[1].parameters[1].value
        for output in (json.dumps(plan.preview()), repr(plan), repr(plan.statements),
                       repr(plan.statements[1].parameters)):
            self.assertNotIn(self.password, output)
            self.assertNotIn(digest, output)
        self.assertIn(jxadm.REDACTED, json.dumps(plan.preview()))


class AdapterTest(unittest.TestCase):
    def test_create_transaction_commit_and_bound_digest(self):
        password = secrets.token_hex(16)
        plan = jxadm.account_plan("create", ACCOUNT, password=password, begin=BEGIN, end=END)
        connection = FakeConnection()
        connect = Mock(return_value=connection)
        self.assertEqual(jxadm.execute_sql(plan, connect), [])
        connect.assert_called_once_with(host="127.0.0.1", database="account")
        self.assertFalse(connection.autocommit)
        self.assertTrue(connection.committed and connection.closed and connection.handle.closed)
        self.assertFalse(connection.rolled_back)
        self.assertEqual(connection.handle.calls[1][1][1], plan.statements[1].parameters[1].value)

    def test_failure_of_second_insert_rolls_back_everything(self):
        plan = jxadm.account_plan("create", ACCOUNT, password=secrets.token_hex(16), begin=BEGIN, end=END)
        connection = FakeConnection(fail_at=3)
        with self.assertRaises(RuntimeError):
            jxadm.execute_sql(plan, Mock(return_value=connection))
        self.assertTrue(connection.rolled_back and connection.closed and connection.handle.closed)
        self.assertFalse(connection.committed)

    def test_missing_or_duplicate_target_rolls_back(self):
        for rowcount in (0, 2):
            connection = FakeConnection(rowcount=rowcount)
            with self.assertRaises(ValueError):
                jxadm.execute_sql(jxadm.account_plan("lock", ACCOUNT), Mock(return_value=connection))
            self.assertTrue(connection.rolled_back)
            self.assertFalse(connection.committed)

    def test_unresolved_password_fails_before_connection(self):
        connect = Mock()
        with self.assertRaises(ValueError):
            jxadm.execute_sql(jxadm.account_plan("unlock", ACCOUNT), connect)
        connect.assert_not_called()

    def test_query_results_are_returned_by_adapter(self):
        rows = [(ACCOUNT, 0, None, None)]
        connection = FakeConnection(rows=rows)
        self.assertEqual(jxadm.execute_sql(jxadm.account_plan("online"), Mock(return_value=connection)), [rows])

    def test_main_vm_and_alias_forms_rejected_before_any_adapter(self):
        for host in ("192.168.1.50", "::ffff:192.168.1.50", "::ffff:c0a8:132", "MainVM",
                     "192.168.001.050", "3232235826", "192.168.1.50,1433",
                     "tcp:192.168.1.50", "192.168.1.50\\SQLEXPRESS", "::1%loopback"):
            with self.subTest(host=host):
                connect = Mock()
                plan = replace(jxadm.account_plan("online"), host=host)
                with self.assertRaises(ValueError):
                    jxadm.execute_sql(plan, connect)
                connect.assert_not_called()
                with self.assertRaises(ValueError):
                    jxadm.account_plan("online", host=host)


class BackupTest(unittest.TestCase):
    def setUp(self):
        self.plan = jxadm.backup_plan("D:/offline_fixture/database", "D:/offline_fixture_backup")

    def test_request_covers_full_environment_without_sql_or_file_access(self):
        output = self.plan.preview()
        self.assertNotIn("statements", output)
        self.assertIn("recovery logs", output["scope"])
        adapter = Mock()
        with self.assertRaises(ValueError):
            jxadm.execute_backup(self.plan, adapter)
        adapter.backup_environment.assert_not_called()
        adapter.backup_environment.return_value = {"fixture": "copied by fake"}
        result = jxadm.execute_backup(self.plan, adapter, cold_confirmed=True)
        self.assertEqual(result, {"fixture": "copied by fake"})
        adapter.backup_environment.assert_called_once_with(source=self.plan.source, destination=self.plan.destination)

    def test_network_relative_same_and_nested_paths_rejected(self):
        for source, destination in (("\\\\192.168.1.50\\database", "D:/backup"),
                                    ("//other/database", "D:/backup"), ("relative", "D:/backup"),
                                    ("D:/source/../database", "D:/backup"),
                                    ("D:/db", "d:/DB"), ("D:/db", "D:/db/backup"),
                                    ("D:/db/sub", "D:/db")):
            with self.subTest(source=source), self.assertRaises(ValueError):
                jxadm.backup_plan(source, destination)

    def test_main_vm_rechecked_before_backup_adapter(self):
        adapter = Mock()
        with self.assertRaises(ValueError):
            jxadm.execute_backup(replace(self.plan, host="192.168.1.50"), adapter, cold_confirmed=True)
        adapter.backup_environment.assert_not_called()


class CliTest(unittest.TestCase):
    def invoke(self, arguments):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network forbidden")), \
                patch.object(socket, "getaddrinfo", side_effect=AssertionError("DNS forbidden")):
            result = jxadm.main(arguments)
        return result, out.getvalue(), err.getvalue()

    def test_all_commands_default_to_dry_run(self):
        commands = [["create", "--account", ACCOUNT, "--begin", BEGIN, "--end", END],
                    ["lock", "--account", ACCOUNT], ["unlock", "--account", ACCOUNT],
                    ["reset-password", "--account", ACCOUNT], ["online"],
                    ["mark-bot", "--account", ACCOUNT, "--value", "true"],
                    ["backup-characters", "--source", "D:/fixture/db", "--destination", "D:/backup"]]
        for arguments in commands:
            with self.subTest(command=arguments[0]):
                code, output, error = self.invoke(arguments)
                self.assertEqual((code, error), (0, ""))
                self.assertEqual(json.loads(output)["mode"], "dry-run")

    def test_environment_and_hidden_runtime_input_redacted(self):
        password = secrets.token_hex(16)
        digest = hashlib.md5(password.encode("ascii"), usedforsecurity=False).hexdigest().upper()
        with patch.dict(os.environ, {"JXADM_OFFLINE_TEST_PASSWORD": password}):
            code, output, error = self.invoke(["reset-password", "--account", ACCOUNT,
                                               "--password-env", "JXADM_OFFLINE_TEST_PASSWORD", "--dry-run"])
        self.assertEqual(code, 0)
        self.assertNotIn(password, output + error)
        self.assertNotIn(digest, output + error)
        with patch.object(jxadm.getpass, "getpass", return_value=password) as prompt:
            code, output, error = self.invoke(["unlock", "--account", ACCOUNT, "--prompt-password"])
        self.assertEqual(code, 0)
        prompt.assert_called_once()
        self.assertNotIn(password, output + error)

    def test_missing_environment_and_echoing_prompt_fail_safely(self):
        with patch.dict(os.environ, {}, clear=True):
            code, output, error = self.invoke(["reset-password", "--account", ACCOUNT,
                                               "--password-env", "JXADM_OFFLINE_TEST_PASSWORD"])
        self.assertEqual((code, output), (2, ""))
        with patch.object(jxadm.getpass, "getpass", side_effect=jxadm.getpass.GetPassWarning):
            code, output, error = self.invoke(["unlock", "--account", ACCOUNT, "--prompt-password"])
        self.assertEqual((code, output), (2, ""))

    def test_main_vm_rejected_before_password_prompt(self):
        with patch.object(jxadm.getpass, "getpass") as prompt:
            code, output, error = self.invoke(["unlock", "--account", ACCOUNT,
                                               "--host", "192.168.1.50", "--prompt-password"])
        self.assertEqual((code, output), (2, ""))
        self.assertIn("Main VM 192.168.1.50 is blocked", error)
        prompt.assert_not_called()

    def test_password_argument_and_execute_flag_rejected_without_echo(self):
        password = secrets.token_hex(16)
        for extra in (["--password", password], ["--execute"], ["--password=" + password]):
            with self.subTest(option=extra[0].split("=")[0]):
                code, output, error = self.invoke(["lock", "--account", ACCOUNT] + extra)
                self.assertEqual((code, output), (2, ""))
                self.assertNotIn(password, error)

    def test_no_password_option_abbreviation_or_parser_error_echo(self):
        password = secrets.token_hex(16)
        code, output, error = self.invoke(["reset-password", "--account", ACCOUNT,
                                          "--password", password])
        self.assertEqual((code, output), (2, ""))
        self.assertNotIn(password, error)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err), self.assertRaises(SystemExit):
            jxadm.main(["mark-bot", "--account", ACCOUNT, "--value", password])
        self.assertNotIn(password, out.getvalue() + err.getvalue())


if __name__ == "__main__":
    unittest.main()
