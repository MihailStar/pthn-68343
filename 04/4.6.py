# 1
n, m = map(int, input().split())

for y in range(n):
    for x in range(m):
        print("." if (y + x) % 2 == 0 else "*", end=" ")
    print()


# 2
n = int(input())

for y in range(n):
    for x in range(n):
        if y < n - 1 - x:
            print("0", end=" ")
        elif y > n - 1 - x:
            print("2", end=" ")
        else:
            print("1", end=" ")
    print()


# 3
n, m = map(int, input().split())
c = 0
ш_matrix = [[str(c := c + 1).ljust(3) for _x in range(m)] for _y in range(n)]

for r in ш_matrix:
    print(*r, sep="")


# 4
n, m = map(int, input().split())
c = 0
matrix = [[0] * m for _ in range(n)]

for x in range(m):
    for y in range(n):
        c += 1
        matrix[y][x] = c

print("\n".join(map(lambda r: " ".join(map(lambda n: str(n).ljust(3), r)), matrix)))


# 5
n = int(input())
matrix = [[1 if y == x or y == n - 1 - x else 0 for x in range(n)] for y in range(n)]

print("\n".join(map(lambda r: " ".join(map(lambda n: str(n).ljust(3), r)), matrix)))


# 6
n = int(input())
matrix = [
    [
        1 if y <= x and y <= n - 1 - x or y >= x and y >= n - 1 - x else 0
        for x in range(n)
    ]
    for y in range(n)
]

for r in matrix:
    print(*r, sep="  ")


# 7
n, m = map(int, input().split())
r = [*range(1, m + 1)]
matrix = [[*r[i % m :], *r[: i % m]] for i in range(n)]

print("\n".join(map(lambda r: " ".join(map(lambda n: str(n).ljust(3), r)), matrix)))


# 8
n, m = map(int, input().split())

for i in range(n):
    for j in range(1, m + 1) if i % 2 == 0 else range(m, 0, -1):
        print(str(j + m * i).ljust(3), end=" ")
    print()


# 9
n, m = map(int, input().split())
c = 1
matrix = [[0] * m for _ in range(n)]


def fill_down(y: int, x: int) -> None:
    global c
    global matrix
    matrix[y][x] = c
    while True:
        x, y, c = x - 1, y + 1, c + 1
        if x < 0 or y > n - 1:
            break
        matrix[y][x] = c


for x in range(m):
    y = 0
    fill_down(y, x)

for y in range(1, n):
    x = m - 1
    fill_down(y, x)

print("\n".join(map(lambda r: " ".join(map(lambda n: str(n).ljust(3), r)), matrix)))


# 10
from enum import Enum
from itertools import cycle

n, m = map(int, input().split())
y, x, c, matrix = 0, 0, 1, [[0] * m for _ in range(n)]


class Direction(Enum):
    Right = 1
    Bottom = 2
    Left = 3
    Top = 0


def move_to_next_cell(direction: Direction) -> None:
    global y, x
    if direction == Direction.Right:
        x += 1
    elif direction == Direction.Bottom:
        y += 1
    elif direction == Direction.Left:
        x -= 1
    elif direction == Direction.Top:
        y -= 1
    else:
        raise ValueError("Invalid direction")


def fill_in(direction: Direction) -> None:
    try:
        global y, x, c, matrix
        while True:
            if matrix[y][x] != 0:
                raise IndexError("Filled cell")
            matrix[y][x] = c
            c += 1
            move_to_next_cell(direction)
    except IndexError:
        if direction == Direction.Right:
            move_to_next_cell(Direction.Left)
        elif direction == Direction.Bottom:
            move_to_next_cell(Direction.Top)
        elif direction == Direction.Left:
            move_to_next_cell(Direction.Right)
        elif direction == Direction.Top:
            move_to_next_cell(Direction.Bottom)


for direction in cycle(
    (Direction.Right, Direction.Bottom, Direction.Left, Direction.Top)
):
    if c > n * m:
        break
    fill_in(direction)
    if direction == Direction.Right:
        move_to_next_cell(Direction.Bottom)
    elif direction == Direction.Bottom:
        move_to_next_cell(Direction.Left)
    elif direction == Direction.Left:
        move_to_next_cell(Direction.Top)
    elif direction == Direction.Top:
        move_to_next_cell(Direction.Right)


print("\n".join(map(lambda r: " ".join(map(lambda n: str(n).ljust(3), r)), matrix)))
