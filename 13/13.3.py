# 1
z1 = complex(input())
z2 = complex(input())

print(z1, "+", z2, "=", z1 + z2)
print(z1, "-", z2, "=", z1 - z2)
print(z1, "*", z2, "=", z1 * z2)


# 2
numbers: list[complex] = []
max_number = max(numbers, key=abs)

print(max_number)
print(abs(max_number))


# 3
n = int(input())
z1 = complex(input())
z2 = complex(input())

print(z1**n + z2**n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))
