# 1
from random import randint


def generate_ip() -> str:
    return f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"


# 2
from random import choice, randrange
from string import ascii_uppercase as uppercase


def generate_index() -> str:
    return f"{choice(uppercase)}{choice(uppercase)}{randrange(100)}_{randrange(100)}{choice(uppercase)}{choice(uppercase)}"


# 3
from random import shuffle

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# for row in matrix:
#     shuffle(row)

# shuffle(matrix)

items = [item for row in matrix for item in row]
shuffle(items)
matrix = [[items.pop() for _ in range(len(matrix))] for _ in range(len(matrix))]


# 4
from random import randint

tickets: set[str] = set()


def generate_ticket() -> str:
    ticket = f"{randint(1,7)}"
    for _ in range(6):
        ticket += str(randint(0, 7))
    return ticket


while len(tickets) < 100:
    tickets.add(generate_ticket())

print(*tickets, sep="\n")


# 5
from random import shuffle

letters = list(input())
shuffle(letters)

print("".join(letters))


# 6
from random import sample

size = 5
random_numbers = sample(list(range(1, 75 + 1)), size * size)
card = [
    [str(random_numbers.pop()).ljust(3) for _x in range(size)] for _y in range(size)
]
card[size // 2][size // 2] = str(0)

for row in card:
    print(*row)


# 7
n = int(input())
students = [input() for _ in range(n)]
pairs = [[student, ""] for student in students]

while len(students):
    student = students.pop()

    for pair in pairs:
        if not pair[1] and pair[0] != student:
            pair[1] = student
            break

for pair in pairs:
    print(" - ".join(pair))


# 8
from random import choice
from string import ascii_letters, digits

bad_symbols = {"l", "I", "1", "o", "O", "0"}
symbols = [symbol for symbol in (ascii_letters + digits) if symbol not in bad_symbols]


def generate_password(length: int) -> str:
    result = ""

    for _ in range(length):
        result += choice(symbols)

    return result


def generate_passwords(count: int, length: int) -> list[str]:
    result: list[str] = []

    for _ in range(count):
        result.append(generate_password(length))

    return result


for password in generate_passwords(int(input()), int(input())):
    print(password)


# 9
from random import sample
from string import ascii_letters, digits

bad_symbols = {"l", "I", "1", "o", "O", "0"}
symbols = [symbol for symbol in (ascii_letters + digits) if symbol not in bad_symbols]


def is_strong_password(password: str) -> bool:
    return all(
        (
            any(symbol.isdigit() for symbol in password),
            any(symbol.islower() for symbol in password),
            any(symbol.isupper() for symbol in password),
        )
    )


def generate_password(length: int) -> str:
    password = ""

    while not is_strong_password(password):
        password = "".join(sample(symbols, length))

    return password


def generate_passwords(count: int, length: int) -> list[str]:
    passwords: list[str] = []

    for _ in range(count):
        passwords.append(generate_password(length))

    return passwords


for password in generate_passwords(int(input()), int(input())):
    print(password)
