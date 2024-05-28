# 1
ДНК_to_РНК = {"G": "C", "C": "G", "T": "A", "A": "U"}

print("".join(list(ДНК_to_РНК[n] for n in input())))


# 2
from collections import defaultdict

words = input().split()
word_to_counter: defaultdict[str, int] = defaultdict(int)

for word in words:
    word_to_counter[word] += 1
    print(word_to_counter[word], end=" ")


# 3
from typing import Final

score: Final = {
    1: ("A", "E", "I", "L", "N", "O", "R", "S", "T", "U"),
    2: ("D", "G"),
    3: ("B", "C", "M", "P"),
    4: ("F", "H", "V", "W", "Y"),
    5: ("K"),
    8: ("J", "X"),
    10: ("Q", "Z"),
}
char_to_score = {l: s for s in score for l in score[s]}

print(sum(char_to_score[c] for c in input()))


# 4
from typing import Any


def build_query_string(d: dict[str, Any]) -> str:
    return "&".join(f"{k}={v}" for (k, v) in sorted(d.items()))


# 5
from collections import defaultdict
from typing import Any


def merge(l: list[dict[str, Any]]) -> dict[str, set[Any]]:
    dd: defaultdict[str, set[Any]] = defaultdict(set)

    for d in l:
        for k in d:
            dd[k].add(d[k])

    return dd


# 6
name_to_permission: dict[str, set[str]] = {}
operation_to_permission = {"read": "R", "write": "W", "execute": "X"}

for _ in range(int(input())):
    name, *permission = input().split()
    name_to_permission[name] = set(permission)

for _ in range(int(input())):
    operation, name = input().split()
    has_access = operation_to_permission[operation] in name_to_permission[name]
    print("OK" if has_access else "Access denied")


# 7
carts: dict[str, dict[str, int]] = {}

for _ in range(int(input())):
    [buyer, product, amount] = input().split()
    amount = int(amount)

    if buyer in carts:
        cart = carts[buyer]

        if product in cart:
            cart[product] += amount
        else:
            cart[product] = amount
    else:
        carts[buyer] = {product: amount}

for buyer in sorted(carts):
    cart = carts[buyer]

    print(f"{buyer}:")

    for product in sorted(cart):
        amount = cart[product]

        print(product, amount)
