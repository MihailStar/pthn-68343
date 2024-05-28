# 1
dictionary: dict[str, str] = {}

for _ in range(int(input())):
    word, definition = input().split(": ")
    dictionary[word.lower()] = definition

for _ in range(int(input())):
    word = input()
    definition = dictionary.get(word.lower(), "Не найдено")

    print(definition)


# 2
from collections import Counter

(a, b) = (input(), input())
char_to_counter = Counter(a)

if len(a) == len(b):
    for char in b:
        if char_to_counter.get(char, -1) < 1:
            print("NO")
            break
        else:
            char_to_counter[char] -= 1
    else:
        print("YES")
else:
    print("NO")


# 3
(a, b) = ([char.lower() for char in input() if char.isalpha()] for _ in range(2))

print("YES" if sorted(a) == sorted(b) else "NO")


# 4
dictionary: dict[str, str] = {}

for _ in range(int(input())):
    [a, b] = input().split()

    dictionary[a] = b
    dictionary[b] = a

print(dictionary[input()])


# 5
dictionary: dict[str, str] = {}

for _ in range(int(input())):
    [country, *cities] = input().split()
    for city in cities:
        dictionary[city] = country

for _ in range(int(input())):
    city = input()

    print(dictionary[city])


# 6
d: dict[str, list[str]] = {}

for _ in range(int(input())):
    p, n = input().lower().split()
    d[n] = d.get(n, []) + [p]

for _ in range(int(input())):
    n = input().lower()
    print(*d.get(n, ["абонент не найден"]))


# 7
from collections import Counter

encrypted_word = input()
char_to_counter = Counter(encrypted_word)
counter_to_char: dict[int, str] = {}

for _ in range(int(input())):
    char, counter = input().split(": ")
    counter_to_char[int(counter)] = char

decrypted_word = ""

for char in encrypted_word:
    decrypted_word += counter_to_char[char_to_counter[char]]

print(decrypted_word)
