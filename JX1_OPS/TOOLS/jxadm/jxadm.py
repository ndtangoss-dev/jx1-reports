"""Offline SQL Server account plans; no driver, sockets, or automatic connection.

Run: python -I JX1_OPS/TOOLS/jxadm/jxadm.py COMMAND ...
Only an explicitly injected adapter can execute a plan. See C-01-jxadm.md.
"""

import argparse
import getpass
import hashlib
import ipaddress
import json
import os
import re
import sys
import warnings
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import PurePosixPath, PureWindowsPath
from typing import Any, Callable, Protocol


MAIN_VM = ipaddress.ip_address("192.168.1.50")
LOCK_MARKER = "!" * 32  # Outside the hexadecimal MD5 domain; not a password.
REDACTED = "<redacted:cPassword>"


def validate_host(host: str) -> str:
    """No DNS/DSN/instance names, URL, port, zone ID, or legacy IPv4 notation."""
    if not isinstance(host, str) or "%" in host:
        raise ValueError("host must be a numeric IP literal")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        raise ValueError("host must be a numeric IP literal") from None
    if address == MAIN_VM or getattr(address, "ipv4_mapped", None) == MAIN_VM:
        raise ValueError("Main VM 192.168.1.50 is blocked")
    return str(address)


def validate_account(account: str) -> str:
    # Explicit CLI profile; no silent case conversion or guessed SQL length.
    if not re.fullmatch(r"[a-z0-9_]+", account):
        raise ValueError("account must contain lowercase ASCII letters, digits or _")
    return account


def parse_date(value: str) -> datetime:
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError("date must be YYYY-MM-DDTHH:MM:SS (server local time)") from None
    if parsed.year < 1753:
        raise ValueError("date must be in SQL Server datetime range")
    return parsed


@dataclass(frozen=True)
class Secret:
    value: Any = field(default=None, repr=False)

    def __repr__(self) -> str:
        return REDACTED


def password_parameter(password: str | None) -> Secret:
    if password is None:
        return Secret()  # SQL preview works without acquiring a real password.
    if not password or not password.isascii() or not password.isprintable():
        raise ValueError("password must be nonempty printable ASCII; other encodings unverified")
    # Legacy wire/storage compatibility from A-02, not a new password scheme.
    digest = hashlib.md5(password.encode("ascii"), usedforsecurity=False).hexdigest().upper()
    return Secret(digest)


@dataclass(frozen=True)
class Statement:
    sql: str
    parameters: tuple = field(default=(), repr=False)
    expected_rows: int | None = None

    def preview(self) -> dict:
        return {"sql": self.sql,
                "parameters": [REDACTED if isinstance(p, Secret) else p
                               for p in self.parameters],
                "expected_rows": self.expected_rows}


@dataclass(frozen=True)
class SqlPlan:
    operation: str
    host: str
    statements: tuple[Statement, ...]
    notes: tuple[str, ...] = ()

    def preview(self) -> dict:
        return {"mode": "dry-run", "operation": self.operation,
                "host": self.host, "database": "account",
                "statements": [s.preview() for s in self.statements],
                "notes": list(self.notes)}


def account_plan(operation: str, account: str | None = None, *,
                 host: str = "127.0.0.1", password: str | None = None,
                 begin: str | None = None, end: str | None = None,
                 is_bot: bool | None = None) -> SqlPlan:
    host = validate_host(host)  # Must precede password work or adapter access.
    if operation not in {"create", "lock", "unlock", "reset-password", "online", "mark-bot"}:
        raise ValueError("unsupported operation")
    if account is not None:
        account = validate_account(account)
    elif operation != "online":
        raise ValueError("account is required")
    notes = ["Live schema, constraints, column sizes and defaults: unverified."]
    if operation == "create":
        if begin is None or end is None or parse_date(end) <= parse_date(begin):
            raise ValueError("create requires explicit begin < end")
        statements = (
            Statement("IF EXISTS (SELECT 1 FROM [Account_Info] WITH (UPDLOCK, HOLDLOCK) "
                      "WHERE [cAccName] = ?) OR EXISTS (SELECT 1 FROM [Account_Habitus] "
                      "WITH (UPDLOCK, HOLDLOCK) WHERE [cAccName] = ?) "
                      "THROW 50001, 'Account already exists or is incomplete', 1;",
                      (account, account)),
            Statement("INSERT INTO [Account_Info] ([cAccName], [cPassword], [iClientID]) "
                      "VALUES (?, ?, ?);", (account, password_parameter(password), 0), 1),
            Statement("INSERT INTO [Account_Habitus] ([cAccName], [iFlag], [dBeginDate], "
                      "[dEndDate], [iLeftSecond], [nExtPoint], [iClientID]) "
                      "VALUES (?, ?, CONVERT(datetime, ?, 126), CONVERT(datetime, ?, 126), ?, ?, ?);",
                      (account, 0, begin, end, 0, 0, 0), 1),
        )
        notes.append("Proposed time-billing profile: iFlag=0; counters/client IDs initially 0.")
    elif operation in {"lock", "unlock", "reset-password"}:
        value = Secret(LOCK_MARKER) if operation == "lock" else password_parameter(password)
        statements = (Statement("UPDATE [Account_Info] SET [cPassword] = ? "
                                "WHERE [cAccName] = ?;", (value, account), 1),)
        notes.append("Lock proposes a non-MD5 marker; unlock replaces it with a NEW password. "
                     "Ordinary MD5 login only; existing sessions and super-password: unverified.")
    elif operation == "online":
        query = "SELECT [cAccName], [iClientID], [dLoginDate], [dLogoutDate] FROM [Account_Info]"
        statements = (Statement(query + (" WHERE [cAccName] = ?;" if account else ";"),
                                (account,) if account else ()),)
        notes.append("Session observations only: online interpretation of iClientID/dates is unverified; "
                     "no authoritative online count or automatic filtering.")
    else:
        if type(is_bot) is not bool:
            raise ValueError("mark-bot requires a boolean value")
        statements = (Statement(
            "IF NOT EXISTS (SELECT 1 FROM [Account_Info] WITH (UPDLOCK, HOLDLOCK) "
            "WHERE [cAccName] = ?) THROW 50002, 'Account does not exist', 1; "
            "UPDATE [Account_BotMetadata] WITH (UPDLOCK, HOLDLOCK) SET [is_bot] = ? "
            "WHERE [cAccName] = ?; IF @@ROWCOUNT = 0 "
            "INSERT INTO [Account_BotMetadata] ([cAccName], [is_bot]) VALUES (?, ?);",
            (account, int(is_bot), account, account, int(is_bot))),)
        notes.append("Account_BotMetadata is proposed by A-02, not provisioned here; verify unique "
                     "cAccName/type/collation/FK before migration. No row means is_bot=false.")
    return SqlPlan(operation, host, statements, tuple(notes))


def local_path(value: str) -> str:
    windows = PureWindowsPath(value)
    if (value.startswith(("\\", "//")) or "://" in value or
            not (windows.is_absolute() or PurePosixPath(value).is_absolute()) or
            ".." in windows.parts or ".." in PurePosixPath(value).parts):
        raise ValueError("backup paths must be absolute local paths, without .. or network paths")
    return value


@dataclass(frozen=True)
class BackupPlan:
    host: str
    source: str
    destination: str

    def preview(self) -> dict:
        return {"mode": "dry-run", "operation": "backup-characters", "host": self.host,
                "source": self.source, "destination": self.destination,
                "scope": "complete Berkeley DB environment (roledb, indexes, recovery logs)",
                "requires": ["verified local paths and cold/consistent source",
                             "new destination, no overwrite; hash manifest and restore verification"],
                "notes": ["No SQL: character data is not in the account SQL tables.",
                          "This is an adapter request; no files are read or copied in dry-run."]}


def backup_plan(source: str, destination: str, *, host: str = "127.0.0.1") -> BackupPlan:
    host = validate_host(host)
    source, destination = local_path(source), local_path(destination)
    # Lexical rejection without accessing potentially live data.
    src, dst = PureWindowsPath(source), PureWindowsPath(destination)
    if src == dst or src in dst.parents or dst in src.parents:
        raise ValueError("backup paths must be separate, non-nested directories")
    return BackupPlan(host, source, destination)


class SqlConnection(Protocol):
    autocommit: bool

    def cursor(self) -> Any: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def close(self) -> None: ...


def execute_sql(plan: SqlPlan, connect: Callable[..., SqlConnection]) -> list:
    """Embedding API only. Adapter must target the validated literal and DB account.

    Caller must review schema/lock semantics first. No connection implementation ships.
    All statements share a transaction; mismatched row counts roll everything back.
    """
    host = validate_host(plan.host)
    bound = []
    for statement in plan.statements:
        values = []
        for value in statement.parameters:
            if isinstance(value, Secret):
                if value.value is None:
                    raise ValueError("execution requires a password from environment or runtime input")
                value = value.value
            values.append(value)
        bound.append((statement, tuple(values)))
    connection = connect(host=host, database="account")
    cursor = None
    try:
        connection.autocommit = False
        cursor = connection.cursor()
        results = []
        for statement, values in bound:
            cursor.execute(statement.sql, values)
            if statement.expected_rows is not None and cursor.rowcount != statement.expected_rows:
                raise ValueError("unexpected affected row count; transaction rolled back")
            if cursor.description:
                results.append(cursor.fetchall())
        connection.commit()
        return results
    except BaseException:
        connection.rollback()
        raise
    finally:
        try:
            if cursor is not None:
                cursor.close()
        finally:
            connection.close()


class CharacterBackupAdapter(Protocol):
    def backup_environment(self, *, source: str, destination: str) -> Any:
        """Verify cold/local source, refuse overwrite, copy full environment, hash files.

        Never open a live B-tree with generic dbm, drop recovery logs, or rename a .bak
        dump into roledb. Verify restore separately on a disposable copy.
        """
        ...


def execute_backup(plan: BackupPlan, adapter: CharacterBackupAdapter, *, cold_confirmed: bool = False) -> Any:
    checked = backup_plan(plan.source, plan.destination, host=plan.host)
    if not cold_confirmed:
        raise ValueError("cold/consistent character environment has not been confirmed")
    return adapter.backup_environment(source=checked.source, destination=checked.destination)


class SafeArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        kwargs["allow_abbrev"] = False
        super().__init__(*args, **kwargs)

    def error(self, message):
        # argparse's default error can echo an accidental secret from argv.
        self.exit(2, "jxadm: invalid or missing argument; use --help\n")


def parser() -> argparse.ArgumentParser:
    root = SafeArgumentParser(description="jxadm: offline account SQL and character backup plans")
    commands = root.add_subparsers(dest="command", required=True)
    for name in ("create", "lock", "unlock", "reset-password", "online", "mark-bot", "backup-characters"):
        command = commands.add_parser(name)
        command.add_argument("--host", default="127.0.0.1", help="numeric IP; Main VM blocked")
        command.add_argument("--dry-run", action="store_true", default=True,
                             help="default and only CLI mode; never connects")
        if name == "backup-characters":
            command.add_argument("--source", required=True)
            command.add_argument("--destination", required=True)
            continue
        command.add_argument("--account", required=name != "online")
        if name in {"create", "unlock", "reset-password"}:
            password = command.add_mutually_exclusive_group()
            password.add_argument("--password-env", metavar="NAME")
            password.add_argument("--prompt-password", action="store_true")
        if name == "create":
            command.add_argument("--begin", required=True, help="YYYY-MM-DDTHH:MM:SS")
            command.add_argument("--end", required=True, help="YYYY-MM-DDTHH:MM:SS")
        if name == "mark-bot":
            command.add_argument("--value", choices=("true", "false"), required=True)
    return root


def main(argv: list[str] | None = None) -> int:
    # Do not echo unknown argv: it may contain an accidentally supplied password.
    cli = parser()
    args, unknown = cli.parse_known_args(argv)
    if unknown:
        print("jxadm: unsupported argument(s); passwords cannot be passed on the command line", file=sys.stderr)
        return 2
    try:
        validate_host(args.host)
        password = None
        if getattr(args, "password_env", None):
            password = os.environ.get(args.password_env)
            if not password:
                raise ValueError("password environment variable is missing or empty")
        elif getattr(args, "prompt_password", False):
            with warnings.catch_warnings():
                warnings.simplefilter("error", getpass.GetPassWarning)
                password = getpass.getpass("Password (hidden): ")
        if args.command == "backup-characters":
            plan = backup_plan(args.source, args.destination, host=args.host)
        else:
            plan = account_plan(args.command, args.account, host=args.host, password=password,
                                begin=getattr(args, "begin", None), end=getattr(args, "end", None),
                                is_bot=(args.value == "true") if args.command == "mark-bot" else None)
        print(json.dumps(plan.preview(), indent=2, ensure_ascii=True))
        return 0
    except ValueError as error:
        # Validators above use fixed messages without interpolating user input.
        print("jxadm: " + str(error), file=sys.stderr)
        return 2
    except (EOFError, getpass.GetPassWarning):
        print("jxadm: hidden password input is unavailable", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
