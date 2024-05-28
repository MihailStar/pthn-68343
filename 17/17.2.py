# 1
file = open(input())
content = file.read()

print(content)

file.close()


# 2
file = open(input())
lines = file.readlines()

print(lines[-2].rstrip())

file.close()


# 3
from random import choice

file = open("./lines.txt", encoding="utf-8")
lines = file.readlines()

print(choice(lines).rstrip())

file.close()


# 4
file = open("./numbers.txt")
lines = file.readlines()
numbers = [int(line.rstrip()) for line in lines]

file.close()

print(sum(numbers))


# 5
file = open("./nums.txt")
numbers = (int(digit) for digit in file.read().strip().split())

file.close()

print(sum(numbers))


# 6
file = open("./prices.txt", encoding="utf-8")
total_price = 0

for line in file:
    number_of, price = map(int, line.rstrip().split("\t")[1:])
    total_price += number_of * price

file.close()

print(total_price)
