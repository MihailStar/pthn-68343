# 1
from typing import Callable

func: Callable[[int], bool] = lambda n: n % 19 == 0 or n % 13 == 0


# 2
from typing import Callable

func: Callable[[str], bool] = lambda s: s.startswith(("A", "a")) and s.endswith(
    ("A", "a")
)


# 3
from re import fullmatch
from typing import Callable

is_non_negative_num: Callable[[str], bool] = (
    lambda n: fullmatch(r"\d+(?:\.\d+)?", n) != None
)


# 4
from re import fullmatch
from typing import Callable

is_num: Callable[[str], bool] = lambda n: fullmatch(r"-?\d+(?:\.\d+)?", n) != None


# 5
words: list[str] = []

print(*sorted(filter(lambda word: len(word) == 6, words)))


# 6
numbers: list[int] = []

print(
    *map(
        lambda number: number // 2 if number % 2 == 0 else number,
        filter(lambda number: not (number % 2 == 1 and number > 47), numbers),
    )
)


# 7
data: list[tuple[int, str]] = []

for t in sorted(data, key=lambda t: t[1][-1], reverse=True):
    print(t[1], t[0], sep=": ")


# 8
data: list[str] = []

data.sort(key=lambda w: (len(w), w))

print(*data, sep=" ")


# 9
mixed_list: list[str | int] = []

print(max(filter(lambda v: type(v) == int, mixed_list)))


# 10
mixed_list: list[str | int] = []

print(*sorted(mixed_list, key=str))


# 11
print(*map(lambda c: 255 - int(c), input().split()))


# 12
from functools import reduce
from operator import add


def evaluate(coefficients: list[int], x: int) -> int:
    length = len(coefficients)

    return reduce(
        add, (coefficients[i] * x ** (length - 1 - i) for i in range(length)), 0
    )


print(evaluate(list(map(int, input().split())), int(input())))
