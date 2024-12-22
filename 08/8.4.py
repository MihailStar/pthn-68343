# 1
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(sum((min(numbers), max(numbers))))


# 2
from statistics import mean
numbers = {
    20,
    6,
    8,
    18,
    18,
    2,
    4,
    6,
    8,
    10,
    12,
    14,
    16,
    18,
    20,
    12,
    8,
    8,
    10,
    4,
    2,
    2,
    2,
    16,
    20,
}
average = float(mean(numbers))
print(average)


# 3
numbers = {
    9089,
    -67,
    -32,
    1,
    78,
    23,
    -65,
    99,
    9089,
    34,
    -32,
    0,
    -67,
    1,
    11,
    111,
    111,
    1,
    23,
}
print(sum(number**2 for number in numbers))


# 4
fruits = {
    "apple",
    "banana",
    "cherry",
    "avocado",
    "pineapple",
    "apricot",
    "banana",
    "avocado",
    "grapefruit",
}
print(*sorted(fruits, reverse=True), sep="\n")


# 5
print(len(set(input())))


# 6
digits = input()
print("YES" if len(digits) == len(set(digits)) else "NO")


# 7
digits = input() + input()
print("YES" if len(set(digits)) == 10 else "NO")


# 8
print("YES" if set(input()) == set(input()) else "NO")


# 9
word1, word2, word3 = input().split()
print("YES" if set(word1) == set(word2) == set(word3) else "NO")
