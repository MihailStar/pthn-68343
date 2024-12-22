# 1
for _ in range(int(input())):
    print(len(set(input().lower())))


# 2
unique_chars = set[str]()
for _ in range(int(input())):
    unique_chars |= set(input().lower())
print(len(unique_chars))


# 3
from string import punctuation
print(len({word.strip(punctuation).lower() for word in input().split()}))


# 4
memory = set[int]()
for number in (int(digit.lstrip("0")) for digit in input().split()):
    print("YES" if number in memory else "NO")
    memory.add(number)
memory.clear()


# 5
from math import modf
all_solution = int(input())
true_solution = 0
true_users = set[str]()
for _ in range(all_solution):
    user, result = input().split(": ")
    if result == "Correct":
        true_solution += 1
        true_users.add(user)
if not true_solution:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print(f"Верно решили {len(true_users)} учащихся")
    fractional, integer = modf(true_solution / all_solution * 100)
    print(
        f"Из всех попыток {int(integer if fractional < 0.5 else integer + 1)}% верных"
    )
