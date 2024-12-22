# 1
print("NO" if set(input()).isdisjoint(input()) else "YES")


# 2
print("YES" if set(input()).issuperset(input()) else "NO")


# 3
print(
    *sorted(
        set(input().split()).intersection(input().split()).difference(input().split()),
        key=int,
        reverse=True,
    )
)


# 4
grades = [set(input().split()), set(input().split()), set(input().split())]
print(
    *sorted(
        (grades[0].union(grades[1]).union(grades[2]))
        - (grades[0].intersection(grades[1]).intersection(grades[2])),
        key=int,
    )
)


# 5
grades = [set(input().split()), set(input().split()), set(input().split())]
print(
    *sorted(
        grades[2].difference(grades[0].union(grades[1])),
        key=int,
        reverse=True,
    )
)


# 6
print(
    *sorted(
        set(range(0, 11)).difference(
            set(map(int, input().split()))
            .union(map(int, input().split()))
            .union(map(int, input().split()))
        )
    )
)
