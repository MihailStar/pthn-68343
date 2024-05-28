# 1
from random import randint

n = int(input())

for _i in range(n):
    print(("Орел", "Решка")[randint(0, 1)])


# 2
from random import randrange

n = int(input())

for _i in range(n):
    print(randrange(1, 6 + 1))


# 3
from random import randint, randrange

length = int(input())
start_code = (ord("A"), ord("a"))[randint(0, 1)]

for _i in range(length):
    code = randrange(start_code, start_code + 26)
    print(chr(code), end="")


# 4
from random import randint

numbers: set[int] = set()

while len(numbers) < 7:
    number = randint(1, 49)
    numbers.add(number)

print(*sorted(numbers))
