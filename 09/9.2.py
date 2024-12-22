# 1
n, m, k, p = (int(input()) for _ in range(4))
print(n - ((m - p) + p + (k - p)))


# 2
data = [int(item) for item in input().split()]
print(len(data) - len(set(data)))


# 3
cities = [input() for _ in range(int(input()) + 1)]
print("OK" if len(cities) - len(set(cities)) == 0 else "REPEAT")


# 4
m, n = (int(input()) for _ in range(2))
library = set(input() for _ in range(m))
for _ in range(n):
    print("YES" if input() in library else "NO")


# 5
a = set(int(item) for item in input().split())
b = set(int(item) for item in input().split())
intersection = a.intersection(b)
if intersection:
    print(*sorted(intersection, reverse=True))
else:
    print("BAD DAY")


# 6
print("YES" if set(input().split()) == set(input().split()) else "NO")


# 7
m, n = (int(input()) for _ in range(2))
a = set(input() for _ in range(m))
b = set(input() for _ in range(n))
print(len(a.difference(a.intersection(b))))


# 8
m, n = (int(input()) for _ in range(2))
a = set(input() for _ in range(m))
b = set(input() for _ in range(n))
intersection = a.intersection(b)
print(len(a.difference(intersection)) + len(b.difference(intersection)) or "NO")


# 9
a = set(input().split())
b = set(input().split())
print(*sorted(a.union(b)))


# 10
m, n = (int(input()) for _ in range(2))
pupils = [input() for _ in range(m + n)]
print(len(pupils) - (len(pupils) - len(set(pupils))) * 2 or "NO")


# 11
true_pupils = set[str]()
for lesson_number in range(1, int(input()) + 1):
    pupils_in_class = set(input() for _ in range(int(input())))
    if lesson_number == 1:
        true_pupils.update(pupils_in_class)
    else:
        # @tutorial AI
        true_pupils.intersection_update(pupils_in_class)
print(*sorted(true_pupils), sep="\n")
