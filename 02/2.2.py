# 1
from typing import Literal, TypeAlias, Union

Quadrant: TypeAlias = Union[Literal[1], Literal[2, 3], Literal[4]]
quadrant_to_number_of_points: dict[Quadrant, int] = {1: 0, 2: 0, 3: 0, 4: 0}

for _ in range(int(input())):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        quadrant_to_number_of_points[1] += 1
    elif x < 0 and y > 0:
        quadrant_to_number_of_points[2] += 1
    elif x < 0 and y < 0:
        quadrant_to_number_of_points[3] += 1
    elif x > 0 and y < 0:
        quadrant_to_number_of_points[4] += 1

print(f"Первая четверть: {quadrant_to_number_of_points[1]}")
print(f"Вторая четверть: {quadrant_to_number_of_points[2]}")
print(f"Третья четверть: {quadrant_to_number_of_points[3]}")
print(f"Четвертая четверть: {quadrant_to_number_of_points[4]}")


# 2
numbers = list(map(int, input().split()))
prev_number = numbers[0]
counter = 0

for index in range(1, len(numbers)):
    curr_number = numbers[index]

    if prev_number < curr_number:
        counter += 1

    prev_number = curr_number

print(counter)


# 3
numbers = list(map(int, input().split()))

for index in range(1, len(numbers), 2):
    numbers[index - 1], numbers[index] = numbers[index], numbers[index - 1]

print(*numbers)


# 4
numbers = list(map(int, input().split()))

numbers.insert(0, numbers.pop())

print(*numbers)


# 5
numbers = list(map(int, input().split()))
counter = 1

for index in range(1, len(numbers)):
    if numbers[index - 1] != numbers[index]:
        counter += 1

print(counter)


# 6
*numbers, product_of_numbers = [int(input()) for _ in range(int(input()) + 1)]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue
        if numbers[i] * numbers[j] == product_of_numbers:
            print("ДА")
            break
    else:
        continue
    break
else:
    print("НЕТ")


# 7
t, r = input(), input()

if t == r:
    print("ничья")
elif (
    t == "камень"
    and r == "ножницы"
    or t == "ножницы"
    and r == "бумага"
    or t == "бумага"
    and r == "камень"
):
    print("Тимур")
else:
    print("Руслан")


# 8
t, r = input(), input()

if t == r:
    print("ничья")
elif (
    t == "камень"
    and (r == "ножницы" or r == "ящерица")
    or t == "ножницы"
    and (r == "бумага" or r == "ящерица")
    or t == "бумага"
    and (r == "камень" or r == "Спок")
    or t == "ящерица"
    and (r == "бумага" or r == "Спок")
    or t == "Спок"
    and (r == "камень" or r == "ножницы")
):
    print("Тимур")
else:
    print("Руслан")


# 9
print(len(max(input().split("О"), key=len)))


# 10
from re import fullmatch

refrigerators = [input() for _ in range(int(input()))]

print(
    *[
        index + 1
        for index, refrigerator in enumerate(refrigerators)
        if fullmatch(r".*a.*n.*t.*o.*n.*", refrigerator)
    ]
)


# 11
from typing import Final

ABC: Final = [chr(code) for code in range(ord("а"), ord("я") + 1)]
text = f"{input()} запретил букву"

for letter in ABC:
    if letter in text:
        print(f"{text} {letter}")
        text = text.replace(letter, "").replace("  ", " ").strip()
