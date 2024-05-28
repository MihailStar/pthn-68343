# 1
with open(input()) as file:
    print(len(file.readlines()))


# 2
with open("./ledger.txt") as file:
    print("$", sum(int(line[1:]) for line in file.readlines()), sep="")


# 3
with open("./grades.txt") as file:
    counter = 0
    for line in file:
        score_1, score_2, score_3 = map(int, line.split()[1:])
        if all(map(lambda score: score > 64, (score_1, score_2, score_3))):
            counter += 1
    print(counter)


# 4
with open("./words.txt") as file:
    words = file.read().strip().split()
max_len = len(max(words, key=len))
for word in filter(lambda word: len(word) == max_len, words):
    print(word)


# 5
with open(input()) as file:
    lines: list[str] = []
    for line in file:
        if len(lines) > 9:
            lines.pop(0)
        lines.append(line.rstrip())
    print("\n".join(lines))


# 6
with open("./forbidden_words.txt") as file:
    forbidden_words = file.read().rstrip().split()

with open(input()) as file:
    for line in file:
        line = line.rstrip()
        lower_line = line.lower()
        for forbidden_word in forbidden_words:
            start_index = 0
            while True:
                start_index = lower_line.find(forbidden_word, start_index)
                if start_index == -1:
                    break
                end_index = start_index + len(forbidden_word)
                line = line[:start_index] + "*" * len(forbidden_word) + line[end_index:]
                start_index += 1
        print(line)


# 7
from typing import Final

X: Final = {
    **{"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "jo"},
    **{"ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m"},
    **{"н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u"},
    **{"ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "shh", "ъ": "*"},
    **{"ы": "y", "ь": "'", "э": "je", "ю": "ju", "я": "ya"},
}

with open("./cyrillic.txt", encoding="utf-8") as file, open(
    "./transliteration.txt", "w", encoding="utf-8"
) as output:
    for line in file:
        new_line = ""
        for char in line.rstrip():
            char_lower = char.lower()
            char_isupper = char.isupper()
            new_line += (
                (
                    X[char_lower][0].upper() + X[char_lower][1:]
                    if char_isupper
                    else X[char_lower]
                )
                if char_lower in X
                else char
            )
        print(new_line, file=output)


# 8
with open(input(), encoding="utf-8") as file:
    names: list[str] = []
    prev_line = ""
    for line in file:
        if line.startswith("def ") and not prev_line.startswith("#"):
            names.append(line[4 : line.index("(")])
        prev_line = line
    print("\n".join(names) if names else "Best Programming Team")
