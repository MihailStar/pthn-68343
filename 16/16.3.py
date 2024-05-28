# 1
def concat(*args: object, sep: str = " ") -> str:
    return sep.join(map(str, args))


# 2
from functools import reduce
from operator import mul


def product_of_odds(data: list[int]) -> int:
    return reduce(mul, filter(lambda n: n % 2 == 1, data), 1)


# 3
words = "the world is mine take a look what you have started".split()

print(*map(lambda word: f'"{word}"', words))


# 4
numbers: list[int] = []

print(*filter(lambda number: list(str(number)) != list(reversed(str(number))), numbers))


# 5
numbers: list[tuple[int, ...]] = []

sorted_numbers = sorted(numbers, key=lambda t: sum(t) / len(t), reverse=True)

print(sorted_numbers)


# 6
from typing import Callable, Literal, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def call(f: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R:
    return f(*args, **kwargs)


# 7
def compose(f, g):
    return lambda x: f(g(x))


# 8
from operator import add, mul, sub, truediv
from typing import Any, Callable, Literal


def arithmetic_operation(
    operation: Literal["*", "+", "-", "/"]
) -> Callable[[Any, Any], Any]:
    return {"*": mul, "+": add, "-": sub, "/": truediv}[operation]


# 9
print(*sorted(input().split(), key=lambda word: word.lower()))


# 10
from functools import reduce
from operator import add

words: list[str] = []
word_to_word_num: dict[str, int] = {}

for _ in range(int(input())):
    words.append(input())
    word = words[-1]

    word_to_word_num[word] = reduce(
        add, (ord(char.upper()) - ord("A") for char in word), 0
    )

print(*sorted(words, key=lambda word: (word_to_word_num[word], word)), sep="\n")


# 11
from functools import reduce
from operator import add

ips: list[str] = []
ip_to_ip_num: dict[str, int] = {}

for _ in range(int(input())):
    ips.append(input())
    ip_to_ip_num[ips[-1]] = reduce(
        add,
        (
            int(ip_part) * 256 ** (4 - index)
            for index, ip_part in enumerate(ips[-1].split("."), start=1)
        ),
        0,
    )

print(*sorted(ips, key=lambda ip: ip_to_ip_num[ip]), sep="\n")
