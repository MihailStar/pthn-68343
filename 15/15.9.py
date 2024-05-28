# 1
def ignorecommand(command: str) -> bool:
    ignores = [
        "alias",
        "configuration",
        "ip",
        "sql",
        "select",
        "update",
        "exec",
        "del",
        "truncate",
    ]

    return any(map(lambda ignore: ignore in command, ignores))


# 2
countries = ["Russia", "USA", "UK", "Germany", "France", "India"]
capitals = ["Moscow", "Washington", "London", "Berlin", "Paris", "Delhi"]
population = [145934462, 331002651, 80345321, 67886011, 65273511, 1380004385]

for t in zip(capitals, countries, population):
    print(f"{t[0]} is the capital of {t[1]}, population equal {t[2]} people.")


# 3
abscissas, ordinates, applicates = (
    [float(digit) for digit in input().split()] for _ in range(3)
)
r = 2

print(
    all(
        x**2 + y**2 + z**2 <= r**2
        for x, y, z in zip(abscissas, ordinates, applicates)
    )
)


# 4
from re import fullmatch

reg_exp = r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"

print(
    all(
        map(
            lambda part: fullmatch(reg_exp, part.lstrip("0") or "0") is not None,
            input().split("."),
        )
    )
)


# 5
a, b = (int(input()) for _ in range(2))

print(
    *(
        digits
        for digits in (str(n) for n in range(a, b + 1))
        if all(
            map(lambda digit: digit != "0" and int(digits) % int(digit) == 0, digits)
        )
    )
)


# 6
from string import ascii_lowercase, ascii_uppercase, digits

password = input()

print(
    "YES"
    if len(password) > 6
    and all(
        (
            any(map(lambda char: char in ascii_lowercase, password)),
            any(map(lambda char: char in ascii_uppercase, password)),
            any(map(lambda char: char in digits, password)),
        )
    )
    else "NO"
)


# 7
print(
    "YES"
    if all(
        any([input().split()[1] == "5" for _ in range(int(input()))])
        for _ in range(int(input()))
    )
    else "NO"
)
