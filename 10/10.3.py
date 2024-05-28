# 1
result = {}

for num in range(1, 15 + 1):
    result[num] = num * num


# 2
dict1 = {"a": 100, "z": 333, "b": 200, "c": 300, "d": 45, "e": 98, "t": 76, "q": 34, "f": 90, "m": 230}
dict2 = {"a": 300, "b": 200, "d": 400, "t": 777, "c": 12, "p": 123, "w": 111, "z": 666}
result = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in sorted(dict1 | dict2)}


# 3
from collections import Counter

text = "footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff"
result = Counter(text)


# 4
from collections import Counter

s = "orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley"
items = Counter(s.split()).items()
most = max(items, key=lambda item: item[1])

print(
    sorted(filter(lambda item: item[1] == most[1], items), key=lambda item: item[0])[0][0]
)


# 5
pets = [
    ("Hatiko", "Parker", "Wilson", 50),
    ("Rusty", "Josh", "King", 25),
    ("Fido", "John", "Smith", 28),
    ("Butch", "Jake", "Smirnoff", 18),
    ("Odi", "Emma", "Wright", 18),
    ("Balto", "Josh", "King", 25),
    ("Barry", "Josh", "King", 25),
    ("Snape", "Hannah", "Taylor", 40),
    ("Horry", "Martha", "Robinson", 73),
    ("Giro", "Alex", "Martinez", 65),
    ("Zooma", "Simon", "Nevel", 32),
    ("Lassie", "Josh", "King", 25),
    ("Chase", "Martha", "Robinson", 73),
    ("Ace", "Martha", "Williams", 38),
    ("Rocky", "Simon", "Nevel", 32),
]
result: dict[tuple[str, str, int], list[str]] = {}

for p in pets:
    owner = p[1:]
    pet = p[0]
    result[owner] = result.get(owner, []) + [pet]


# 6
from collections import Counter
from re import sub

words = sub(r"[.,!?:;-]+", "", input().lower()).split()
items = Counter(words).items()
most = min(items, key=lambda item: item[1])
print(
    sorted(filter(lambda item: item[1] == most[1], items), key=lambda item: item[0])[0][0]
)


# 7
from collections import defaultdict

temporary: defaultdict[str, int] = defaultdict(int)

for identifier in input().split():
    print(
        identifier
        if temporary[identifier] == 0
        else f"{identifier}_{temporary[identifier]}",
        end=" ",
    )
    temporary[identifier] += 1
