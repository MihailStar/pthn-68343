# 1
chars = input().split()
n = int(input())
result: list[list[str]] = [[] for _ in range(n)]

for index, char in enumerate(chars):
    result[index % n].append(char)

print(result)


# 2
n = int(input())

print(
    max(
        int(digit)
        for y in range(n)
        for x, digit in enumerate(input().split())
        if y <= x and y >= n - 1 - x or y >= x and y > n - 1 - x
    )
)


# 3
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

for x in range(n):
    for y in range(n):
        print(matrix[y][x], end=" ")
    print()


# 4
n = int(input())

for y in range(n):
    for x in range(n):
        if y == n // 2 or x == n // 2 or y == x or y == n - 1 - x:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()


# 5
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

# @tutorial https://stepik.org/lesson/416759/step/5?discussion=4099407&unit=406267
for y in range(n):
    for x in range(n):
        if matrix[y][x] != matrix[n - x - 1][n - y - 1]:
            print("NO")
            break
    else:
        continue
    break
else:
    print("YES")


# 6
def is_latin_square(matrix: list[list[int]]) -> bool:
    reference = set(range(1, len(matrix) + 1))

    for row in matrix:
        if set(row) != reference:
            return False

    for x in range(len(matrix)):
        col = [matrix[y][x] for y in range(len(matrix))]
        if set(col) != reference:
            return False

    return True


n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

print("YES" if is_latin_square(matrix) else "NO")


# 7
from typing import Callable

a, b = input()
y_Q, x_Q = 8 - int(b), "abcdefgh".index(a)
field = [["." for _ in range(8)] for _ in range(8)]
field[y_Q][x_Q] = "Q"

directions: list[Callable[[int, int], tuple[int, int]]] = [
    lambda y, x: (y - 1, x),
    lambda y, x: (y - 1, x + 1),
    lambda y, x: (y, x + 1),
    lambda y, x: (y + 1, x + 1),
    lambda y, x: (y + 1, x),
    lambda y, x: (y + 1, x - 1),
    lambda y, x: (y, x - 1),
    lambda y, x: (y - 1, x - 1),
]

for direction in directions:
    y, x = y_Q, x_Q
    while True:
        y, x = direction(y, x)
        if y < 0 or y > 7 or x < 0 or x > 7:
            break
        field[y][x] = "*"

for row in field:
    print(*row)


# 8
n = int(input())
line = [*range(n)]

for i in range(n):
    print(*line[i::-1] + line[1 : n - i])
