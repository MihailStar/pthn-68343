# 1
from typing import Any


def count_args(*args: Any) -> int:
    return len(args)


# 2
def sq_sum(*args: int) -> int:
    return sum(arg**2 for arg in args)


# 3
from typing import Any


def mean(*args: Any) -> float:
    nums = [arg for arg in args if type(arg) == int or type(arg) == float]

    if len(nums) == 0:
        return 0.0

    return sum(nums) / len(nums)


# 4
def greet(name: str, *names: str) -> str:
    names = (name,) + names

    return f"Hello, {' and '.join(names)}!"


# 5
from typing import Any


def print_products(*args: Any) -> None:
    products = [arg for arg in args if isinstance(arg, str) and len(arg)]

    if len(products) == 0:
        print("Нет продуктов")

    for index, product in enumerate(products):
        print(f"{index + 1}) {product}")


# 6
from typing import Any


def info_kwargs(**kwargs: Any) -> None:
    for key in sorted(kwargs):
        print(f"{key}: {kwargs[key]}")


info_kwargs(first_name="Timur", last_name="Guev", age=28, job="teacher")
