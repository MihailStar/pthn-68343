# 1
from functools import reduce

numbers = (
    *(2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31),
    *(-6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1),
)

print(reduce(lambda acc, number: acc * number, numbers, 1))


# 2
data = "Python для продвинутых!"

print(tuple(data))


# 3
poet_data = ("Пушкин", 1799, "Санкт-Петербург")
poet_data = poet_data[:2] + ("Москва",)

print(poet_data)


# 4
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

print([sum(numbers[index]) / len(numbers[index]) for index in range(len(numbers))])


# 5
(a, b, c) = map(int, (input(), input(), input()))

print((-((b) / (2 * a)), (4 * a * c - b**2) / (4 * a)))


# 6
students = [tuple(input().split()) for _ in range(int(input()))]

for student in students:
    print(*student)

print()

for student in filter(lambda student: student[1] in ("4", "5"), students):
    print(*student)


# 7
def tribonacci(n: int) -> list[int]:
    result = [1, 1, 1]

    for _ in range(n - 3):
        result.append(result[-1] + result[-2] + result[-3])

    return result[:n]


print(*tribonacci(int(input())))
