# 1
with open("./text.txt") as file:
    line = file.readline().rstrip()

    print("".join(reversed(line)))


# 2
with open("./data.txt") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.rstrip())


# 3
with open("./lines.txt") as file:
    lines = file.readlines()

longest_line = max(lines, key=len)

for line in lines:
    if len(line) == len(longest_line):
        print(line.rstrip())


# 4
with open("./numbers.txt") as file:
    for line in file:
        numbers = (int(digit) for digit in line.strip().split())

        print(sum(numbers))


# 5
from re import sub

total = 0

with open("./nums.txt") as file:
    for line in file:
        total += sum(map(int, sub(r"[^\d]+", " ", line).strip().split()))

print(total)


# 6
from re import sub

statistics = {"letters": 0, "words": 0, "lines": 0}

with open("./file.txt") as file:
    for line in file:
        words = line.rstrip().split()

        statistics["letters"] += sum(
            map(lambda word: len(sub(r"[^A-Za-z]", "", word)), words)
        )
        statistics["words"] += len(words)
        statistics["lines"] += 1


print("Input file contains:")
print(f"{statistics['letters']} letters")
print(f"{statistics['words']} words")
print(f"{statistics['lines']} lines")


# 7
from random import choice

with open("first_names.txt") as first_file, open("last_names.txt") as last_file:
    first_names = [first_name.rstrip() for first_name in first_file.readlines()]
    last_names = [last_name.rstrip() for last_name in last_file.readlines()]

for _ in range(3):
    print(f"{choice(first_names)} {choice(last_names)}")


# 8
with open("./population.txt") as file:
    for line in file:
        title, in_number = line.rstrip().split("\t")
        in_number = int(in_number)

        if title.startswith("G") and in_number > 500_000:
            print(title)


# 9
def read_csv() -> list[dict[str, str]]:
    with open("./data.csv") as file:
        result: list[dict[str, str]] = []
        keys = file.readline().rstrip().split(",")
        values = []

        for line in file:
            values = line.rstrip().split(",")

            row: dict[str, str] = {}

            for key, value in zip(keys, values):
                row[key] = value

            result.append(row)

        return result
