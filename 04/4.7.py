# 1
n, m = map(int, input().split())
m1 = [[int(d) for d in input().split()] for _ in range(n)]
input()
m2 = [[int(d) for d in input().split()] for _ in range(n)]

print(
    "\n".join(
        [
            " ".join([str(m2[y][x] + n) for x, n in enumerate(r)])
            for y, r in enumerate(m1)
        ]
    )
)


# 2
from numpy import dot

n, m = map(int, input().split())
a = [[int(d) for d in input().split()] for _ in range(n)]
input()
m, k = map(int, input().split())
b = [[int(d) for d in input().split()] for _ in range(m)]
c: list[list[int]] = dot(a, b).tolist()

for row in c:
    print(*row)


# 3
from numpy import linalg

n = int(input())
matrix = [[int(d) for d in input().split()] for _ in range(n)]
m = int(input())
c: list[list[int]] = linalg.matrix_power(matrix, m).tolist()

for row in c:
    print(*row)
