# 1
n, m = map(int, (input(), input()))

for _ in range(n):
    for _ in range(m):
        print(input(), end=" ")

    print()


# 2
n, m = map(int, (input(), input()))
matrix: list[list[str]] = []

for _ in range(n):
    row: list[str] = []
    for _ in range(m):
        row.append(input())
    matrix.append(row)
    print(*row)

print()

for x in range(m):
    for y in range(n):
        print(matrix[y][x], end=" ")
    print()


# 3
n = int(input())
s = 0

for y in range(n):
    s += int(input().split()[y])

print(s)


# 4
n = int(input())
matrix = [[int(dig) for dig in input().split()] for _ in range(n)]
a = [sum(row) / len(row) for row in matrix]

print(
    *[len([num for num in row if num > a[y]]) for (y, row) in enumerate(matrix)],
    sep="\n",
)


# 5
n = int(input())

print(
    max(mx(int(d) for x, d in enumerate(input().split()) if y >= x) for y in range(n))
)


# 6
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]
mx = matrix[0][0]

for y, row in enumerate(matrix):
    for x, item in enumerate(row):
        if (y > x and y < n - 1 - x or y < x and y > n - 1 - x) and item > mx:
            mx = item

print(mx)


# 7
n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]
qs: list[list[int]] = [[], [], [], []]

for y in range(n):
    for x in range(n):
        if y < x and y < n - 1 - x:
            qs[0].append(matrix[y][x])
        if y < x and y > n - 1 - x:
            qs[1].append(matrix[y][x])
        if y > x and y > n - 1 - x:
            qs[2].append(matrix[y][x])
        if y > x and y < n - 1 - x:
            qs[3].append(matrix[y][x])


print(f"Верхняя четверть: {sum(qs[0])}")
print(f"Правая четверть: {sum(qs[1])}")
print(f"Нижняя четверть: {sum(qs[2])}")
print(f"Левая четверть: {sum(qs[3])}")
