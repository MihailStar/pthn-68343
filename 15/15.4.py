# 1
numbers: list[tuple[int, ...]] = []

print(min(numbers, key=lambda t: sum(t) / len(t)))
print(max(numbers, key=lambda t: sum(t) / len(t)))


# 2
points: list[tuple[int, int]] = []

points.sort(key=lambda point: (point[0] ** 2 + point[1] ** 2) * 0.5)

print(points)


# 3
numbers: list[tuple[int, int, int]] = []

numbers.sort(key=lambda t: min(t) + max(t))

print(numbers)


# 4
index = int(input()) - 1
athletes: list[tuple[str, int, int, int]] = []

for athlete in sorted(athletes, key=lambda t: t[index]):
    print(*athlete)


# 5
from math import sin, sqrt
from typing import Callable

num, func_name = int(input()), input()
func: dict[str, Callable[[int], float]] = {
    "квадрат": lambda num: num**2,
    "куб": lambda num: num**3,
    "корень": lambda num: sqrt(num),
    "модуль": lambda num: abs(num),
    "синус": lambda num: sin(num),
}

print(func[func_name](num))


# 6
print(*sorted(input().split(), key=lambda digit: sum(map(int, digit))))


# 7
print(*sorted(input().split(), key=lambda digit: (sum(map(int, digit)), int(digit))))
