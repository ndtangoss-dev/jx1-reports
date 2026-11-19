"""Kiểm tra tên vai offline theo hợp đồng của task BOT-02."""
from __future__ import annotations

import re
from collections.abc import Iterable

_TEN_HOP_LE = re.compile(r"[A-Za-z]{6,16}\Z", re.ASCII)
_CHU_CAI = re.compile(r"[A-Za-z]*\Z", re.ASCII)


def _ascii_text(value: object) -> str | None:
    """Trả chuỗi ASCII của tên; dữ liệu không phải tên ASCII trả None."""
    if isinstance(value, str):
        try:
            value.encode("ascii")
        except UnicodeEncodeError:
            return None
        return value
    if isinstance(value, bytes):
        try:
            return value.decode("ascii")
        except UnicodeDecodeError:
            return None
    return None


def _existing_names(da_co: Iterable[str | bytes] | str | bytes | None) -> tuple[str, ...] | None:
    if da_co is None:
        return ()
    if isinstance(da_co, (str, bytes)):
        values = (da_co,)
    else:
        try:
            values = tuple(da_co)
        except TypeError:
            return None
    return tuple(text.casefold() for value in values
                 if (text := _ascii_text(value)) is not None)


def kiem_ten(ten: str | bytes, da_co: Iterable[str | bytes] | str | bytes | None) -> tuple[bool, str]:
    """Kiểm tra tên dài 6–16 byte, chỉ gồm chữ ASCII và chưa bị trùng."""
    if isinstance(ten, str):
        try:
            byte_length = len(ten.encode("utf-8"))
        except UnicodeEncodeError:
            return False, "Tên chỉ được gồm chữ cái ASCII."
        text = _ascii_text(ten)
    elif isinstance(ten, bytes):
        byte_length = len(ten)
        text = _ascii_text(ten)
    else:
        return False, "Tên phải là chuỗi."

    if not 6 <= byte_length <= 16:
        return False, "Tên phải dài 6–16 byte."
    if text is None or _TEN_HOP_LE.fullmatch(text) is None:
        return False, "Tên chỉ được gồm chữ cái ASCII."

    names = _existing_names(da_co)
    if names is None:
        return False, "Danh sách tên hiện có không hợp lệ."
    if text.casefold() in names:
        return False, "Tên đã tồn tại."

    return True, "Tên hợp lệ."


def _alpha_index(index: int) -> str:
    """Mã hóa số thứ tự không âm thành hậu tố chữ cái: a..z, aa.."""
    result = ""
    while True:
        index, remainder = divmod(index, 26)
        result = chr(ord("a") + remainder) + result
        if index == 0:
            return result
        index -= 1


def gen_ten(prefix: str, n: int, da_co: Iterable[str | bytes] | str | bytes | None) -> str:
    """Sinh tên duy nhất bằng hậu tố chữ cái, bắt đầu từ thứ tự n (tính từ 1)."""
    if not isinstance(prefix, str) or _CHU_CAI.fullmatch(prefix) is None or not prefix:
        raise ValueError("Tiền tố chỉ được gồm chữ cái ASCII.")
    if len(prefix) > 15:
        raise ValueError("Tiền tố quá dài để thêm hậu tố.")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("Thứ tự tên phải là số nguyên dương.")

    names = _existing_names(da_co)
    if names is None:
        raise ValueError("Danh sách tên hiện có không hợp lệ.")
    known = set(names)

    min_suffix_length = max(1, 6 - len(prefix))
    first_index = (26 ** min_suffix_length - 26) // 25
    index = n - 1 + first_index
    while True:
        suffix = _alpha_index(index)
        candidate = prefix + suffix
        if len(candidate) > 16:
            raise ValueError("Không thể sinh tên 6–16 byte từ tiền tố này.")
        if candidate.casefold() not in known:
            return candidate
        index += 1
