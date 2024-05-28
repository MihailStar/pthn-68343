# 1
numbers: list[int] = []
result = {i: n**2 for i, n in enumerate(numbers)}


# 2
from typing import Optional

colors: dict[str, Optional[str]] = {}
result = {k: colors[k] for k in colors if colors[k]}


# 3
favorite_numbers: dict[str, int] = {}
result = {
    k: favorite_numbers[k]
    for k in favorite_numbers
    if 9 < abs(favorite_numbers[k]) < 100
}


# 4
from typing import Final

months: Final = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
result = {s: n for (n, s) in months.items()}


# 5
s = "1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice"
result = {int(pair.split(":")[0]): pair.split(":")[1] for pair in s.split()}


# 6
numbers: list[int] = []
result = {n: [d for d in range(1, n + 1) if n % d == 0] for n in numbers}


# 7
words = ["hello", "bye", "yes", "no", "python", "apple", "maybe", "stepik", "beegeek"]
result = {w: [ord(c) for c in w] for w in words}


# 8
letters: dict[int, str] = {}
remove_keys = set([1, 5, 7, 12, 17, 19, 21, 24])
result = {k: v for (k, v) in letters.items() if k not in remove_keys}


# 9
students: dict[str, tuple[int, int]] = {}
result = {s: info for (s, info) in students.items() if info[0] > 167 and info[1] < 75}


# 10
tuples: list[tuple[int, int, int]] = []
result = {t[0]: t[1:] for t in tuples}


# 11
student_ids: list[str] = []
student_names: list[str] = []
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
result = [
    {id: {n: g}} for (id, n, g) in zip(student_ids, student_names, student_grades)
]
