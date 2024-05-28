# 1
my_dict = {
    1.12: "aa",
    67.9: 45,
    3.11: "ccc",
    7.9: "dd",
    9.2: "ee",
    7.1: "ff",
    0.12: "qq",
    1.91: "aa",
    10.12: [1, 2, 3],
    99.0: {9, 0, 1},
}

print(min(my_dict) + max(my_dict))


# 2
users = [
    {"name": "Todd", "phone": "551-1414", "email": "todd@gmail.com"},
    {"name": "Helga", "phone": "555-1618", "email": "helga@mail.net"},
    {"name": "Olivia", "phone": "449-3141", "email": ""},
    {"name": "LJ", "phone": "555-2718", "email": "lj@gmail.net"},
    {"name": "Ruslan", "phone": "422-145-9098", "email": "rus-lan.cha@yandex.ru"},
    {"name": "John", "phone": "233-421-32", "email": ""},
    {"name": "Lara", "phone": "+7998-676-2532", "email": "g.lara89@gmail.com"},
    {"name": "Alina", "phone": "+7948-799-2434", "email": "ali.ch.b@gmail.com"},
    {"name": "Robert", "phone": "420-2011", "email": ""},
    {"name": "Riyad", "phone": "128-8890-128", "email": "r.mahrez@mail.net"},
    {"name": "Khabib", "phone": "+7995-600-9080", "email": "kh.nurmag@gmail.com"},
    {"name": "Olga", "phone": "6449-314-1213", "email": ""},
    {"name": "Roman", "phone": "+7459-145-8059", "email": "roma988@mail.ru"},
    {"name": "Maria", "phone": "12-129-3148", "email": "m.sharapova@gmail.com"},
    {"name": "Fedor", "phone": "+7445-341-0545", "email": ""},
    {"name": "Tim", "phone": "242-449-3141", "email": "timm.ggg@yandex.ru"},
]

print(
    *sorted(
        map(
            lambda user: user["name"],
            filter(lambda user: user["phone"].endswith("8"), users),
        )
    )
)


# 3
users = [
    {"name": "Todd", "phone": "551-1414", "email": "todd@gmail.com"},
    {"name": "Helga", "phone": "555-1618"},
    {"name": "Olivia", "phone": "449-3141", "email": ""},
    {"name": "LJ", "phone": "555-2718", "email": "lj@gmail.net"},
    {"name": "Ruslan", "phone": "422-145-9098", "email": "rus-lan.cha@yandex.ru"},
    {"name": "John", "phone": "233-421-32", "email": ""},
    {"name": "Lara", "phone": "+7998-676-2532", "email": "g.lara89@gmail.com"},
    {"name": "Alina", "phone": "+7948-799-2434"},
    {"name": "Robert", "phone": "420-2011", "email": ""},
    {"name": "Riyad", "phone": "128-8890-128", "email": "r.mahrez@mail.net"},
    {"name": "Khabib", "phone": "+7995-600-9080", "email": "kh.nurmag@gmail.com"},
    {"name": "Olga", "phone": "6449-314-1213", "email": ""},
    {"name": "Roman", "phone": "+7459-145-8059"},
    {"name": "Maria", "phone": "12-129-3148", "email": "m.sharapova@gmail.com"},
    {"name": "Fedor", "phone": "+7445-341-0545", "email": ""},
    {"name": "Tim", "phone": "242-449-3141", "email": "timm.ggg@yandex.ru"},
]

print(
    *sorted(
        map(
            lambda user: user["name"],
            filter(lambda user: "email" not in user or user["email"] == "", users),
        )
    )
)


# 4
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = list(input())

print(*(words[int(digit)] for digit in digits))


# 5
schedule: dict[str, tuple[int, str, str]] = {
    "CS101": (3004, "Хайнс", "8:00"),
    "CS102": (4501, "Альварадо", "9:00"),
    "CS103": (6755, "Рич", "10:00"),
    "NT110": (1244, "Берк", "11:00"),
    "CM241": (1411, "Ли", "13:00"),
}
course_number = input()
course_info = schedule[course_number]

print("{}: {}, {}, {}".format(course_number, *course_info))


# 6
keyboard = (" ", ".,?!:", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")
char_to_buttons: dict[str, str] = {}

for button_index, chars in enumerate(keyboard):
    for char_index, char in enumerate(chars):
        char_to_buttons[char] = str(button_index) * (char_index + 1)

for char in input():
    print(char_to_buttons.get(char.upper(), ""), end="")


# 7
from typing import Final

morse: Final[dict[str, str]] = {
    **{"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": "."},
    **{"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---"},
    **{"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---"},
    **{"P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-"},
    **{"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--"},
    **{"Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--"},
    **{"4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---.."},
    **{"9": "----."},
}

print(*(morse[char.upper()] for char in input() if char.upper() in morse))
