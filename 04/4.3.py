# 1
n = int(input())

print(*([i for i in range(1, n + 1)] for _ in range(n)), sep="\n")


# 2
n = int(input())

# for end in range(2, n + 2):
#     print([num for num in range(1, end)])

print(*([num for num in range(1, end)] for end in range(2, n + 2)), sep="\n")


# 3
from math import factorial

n = int(input())
row: list[int] = []


def get_value(y: int, x: int) -> int:
    """@tutorial https://ru.wikipedia.org/wiki/Треугольник_Паскаля"""
    return int(factorial(y) / (factorial(x) * factorial(y - x)))


for x in range(n + 1):
    row.append(get_value(n, x))

print(row)


# 4
from math import factorial

n = int(input())
triangle: list[list[int]] = []


def get_value(y: int, x: int) -> int:
    return int(factorial(y) / (factorial(x) * factorial(y - x)))


def get_row(y: int) -> list[int]:
    return [get_value(y, x) for x in range(y + 1)]


for y in range(n):
    print(*get_row(y))


# 5
chars = input().split()
result: list[list[str]] = [[chars[0]]]

for index in range(1, len(chars)):
    char = chars[index]

    if char in result[-1]:
        result[-1].append(char)
        continue

    result.append([char])

print(result)


# 6
def chunked(lst: list[str], size: int) -> list[list[str]]:
    result: list[list[str]] = []

    for start in range(0, len(lst), size):
        result.append(lst[start : start + size])

    return result


print(chunked(input().split(), int(input())))


# 7
chars = input().split()

# print(chars[0:1])  # -> ['a']
# print(chars[1:2])  # -> ['b']
# print(chars[2:3])  # -> ['v']

# print(chars[0:2])  # -> ['a', 'b']
# print(chars[1:3])  # -> ['b', 'v']

# print(chars[0:3])  # -> ['a', 'b', 'v']

result: list[list[str]] = [[]]

for i in range(len(chars)):
    for start in range(len(chars) - i):
        result.append(chars[start : start + 1 + i])

print(result)
