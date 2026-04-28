import re
from typing import Callable

ValidatorFn = Callable[[str], bool]


def not_empty() -> ValidatorFn:
    return lambda val: bool(val.strip())


def alpha_space(min_len: int = 2) -> ValidatorFn:
    def _validate(val: str) -> bool:
        v = val.strip()
        return (
            bool(v)
            and len(v) >= min_len
            and bool(re.fullmatch(r"[A-Za-z\s]+", v))
        )
    return _validate


def min_chars(n: int) -> ValidatorFn:
    return lambda val: len(val.strip()) >= n


def has_digit() -> ValidatorFn:
    return lambda val: bool(val.strip()) and bool(re.search(r"\d", val.strip()))


def all_of(*fns: ValidatorFn) -> ValidatorFn:
    return lambda val: all(fn(val) for fn in fns)
