# 1
print(len(set(input().split()).intersection(input().split())))


# 2
print(*sorted(set(input().split()).intersection(input().split()), key=int))


# 3
print(*sorted(set(input().split()).difference(input().split()), key=int))


# 4
print(*sorted(set[str].intersection(*(set(input()) for _ in range(int(input()))))))
