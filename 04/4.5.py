# 1
n, m = map(int, (input() for _ in range(2)))
mult = [[str(y * x).ljust(3) for x in range(m)] for y in range(n)]

for row in mult:
    print(*row, sep="")


# 2
n, m = (int(input()) for _ in range(2))

print(
    *map(
        abs,
        max(
            [
                (n, -y, -x)
                for y in range(n)
                for x, n in enumerate(map(int, input().split()))
            ]
        )[1:],
    )
)


# 3
n, m = (int(input()) for _ in range(2))
matrix = [[int(d) for d in input().split()] for _ in range(n)]
i, j = (int(d) for d in input().split())

for y in range(n):
    matrix[y][i], matrix[y][j] = matrix[y][j], matrix[y][i]
    print(*matrix[y])


# 4
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

for y in range(n):
    for x in range(n):
        if (y > x or y < x) and matrix[y][x] != matrix[x][y]:
            print("NO")
            break
    else:
        continue
    break
else:
    print("YES")


# 5
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

for y in range(n):
    matrix[y][y], matrix[n - 1 - y][y] = matrix[n - 1 - y][y], matrix[y][y]

# @tutorial https://stepik.org/lesson/416755/step/5?discussion=4198294&reply=4263111&thread=solutions&unit=406263
for y in range(n):
    print(*matrix[y])


# 6
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

for y in range(n // 2):
    matrix[y], matrix[len(matrix) - 1 - y] = matrix[len(matrix) - 1 - y], matrix[y]

for y in range(n):
    print(*matrix[y])


# 7
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]

for x in range(n):
    for y in range(n - 1, -1, -1):
        print(matrix[y][x], end=" ")
    print()


# 8
a, b = input()
y_N, x_N = 8 - int(b), "abcdefgh".index(a)
field = [["." for _ in range(8)] for _ in range(8)]
field[y_N][x_N] = "N"

for y, x in filter(
    lambda y_x: -1 < y_x[0] < 8 and -1 < y_x[1] < 8,
    [
        (y_N - 2, x_N - 1),
        (y_N - 2, x_N + 1),
        (y_N - 1, x_N + 2),
        (y_N + 1, x_N + 2),
        (y_N + 2, x_N + 1),
        (y_N + 2, x_N - 1),
        (y_N + 1, x_N - 2),
        (y_N - 1, x_N - 2),
    ],
):
    field[y][x] = "*"

for row in field:
    print(*row)


# 9
from typing import Literal

n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]
sum_first_row = sum(matrix[0])


def foo() -> Literal["YES", "NO"]:
    nums = set(range(1, n**2 + 1))

    for row in matrix:
        for num in row:
            if num in nums:
                nums.remove(num)

    if nums:
        return "NO"

    for y in range(1, n):
        row = matrix[y]

        if sum(row) != sum_first_row:
            return "NO"

    for x in range(n):
        column = [matrix[y][x] for y in range(n)]

        if sum(column) != sum_first_row:
            return "NO"

    main_diagonal: list[int] = []
    side_diagonal: list[int] = []

    for y in range(n):
        for x in range(n):
            if y == x:
                main_diagonal.append(matrix[y][x])

            if y + x + 1 == n:
                side_diagonal.append(matrix[y][x])

    if sum(main_diagonal) != sum_first_row or sum(side_diagonal) != sum_first_row:
        return "NO"

    return "YES"


print(foo())
