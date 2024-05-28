# 1
numbers: list[float] = []

print(*map(lambda number: round(number, 2), numbers), sep="\n")


# 2
numbers: list[int] = []

print(
    *map(
        lambda number: number**3,
        filter(lambda number: 99 < number < 1000 and number % 5 == 2, numbers),
    ),
    sep="\n"
)


# 3
# from functools import reduce

numbers: list[int] = []

# print(reduce(lambda acc, number: acc + number**2, numbers, 0))

print(sum(map(lambda number: number**2, numbers)))


# 4
numbers: list[int] = []

print(
    sum(number**2 for number in numbers if 9 < abs(number) < 100 and number % 7 == 0)
)


# 5
from typing import Callable, TypeVar

P = TypeVar("P")
R = TypeVar("R")


def func_apply(f: Callable[[P], R], l: list[P]) -> list[R]:
    return list(map(f, l))
