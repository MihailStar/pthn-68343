# 1
from typing import overload


@overload
def matrix(y: int, x: int, value: int) -> list[list[int]]:
    ...


@overload
def matrix(y: int, x: int) -> list[list[int]]:
    ...


@overload
def matrix(y: int) -> list[list[int]]:
    ...


@overload
def matrix() -> list[list[int]]:
    ...


def matrix(y: int = 1, x: int | None = None, value: int = 0) -> list[list[int]]:
    if x is None:
        x = y

    return [[value for _ in range(x)] for _ in range(y)]
