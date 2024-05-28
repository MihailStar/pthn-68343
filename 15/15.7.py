# 1
from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words: list[str] = []
numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda word: len(word) > 4 and word == word[::-1], words))
reduce_result = reduce(lambda acc, num: acc * num, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)


# 2
from functools import reduce

data: list[list[str | int]] = []

print(
    "Cities:",
    ", ".join(
        sorted(
            map(
                lambda city: city[0],
                filter(
                    lambda city: city[1] > 10_000_000 and city[2] == "primary", data
                ),
            )
        ),
    ),
)
