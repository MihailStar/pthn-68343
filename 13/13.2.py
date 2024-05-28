# 1
from fractions import Fraction

numbers: list[str] = []

for number in numbers:
    print(number, "=", Fraction(number))


# 2
from fractions import Fraction

s = "0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021"

fractionss = [Fraction(digit) for digit in s.split()]

print(min(fractionss) + max(fractionss))


# 3
from fractions import Fraction

print(Fraction(int(input()), int(input())))


# 4
from fractions import Fraction

a, b = input(), input()
fraction_a, fraction_b = Fraction(a), Fraction(b)

print(f"{a} + {b}", "=", fraction_a + fraction_b)
print(f"{a} - {b}", "=", fraction_a - fraction_b)
print(f"{a} * {b}", "=", fraction_a * fraction_b)
print(f"{a} / {b}", "=", fraction_a / fraction_b)


# 5
from fractions import Fraction

n = int(input())
s = Fraction(0)

for i in range(1, n + 1):
    s += Fraction(1, i**2)

print(s)


# 6
from fractions import Fraction
from math import factorial

n = int(input())
s = Fraction(0)

for i in range(1, n + 1):
    s += Fraction(1, factorial(i))

print(s)


# 7
from math import gcd


def find_largest_irreducible_fraction(n: int) -> tuple[int, int]:
    """@tutorial AI"""
    max_fraction = (0, 1)

    for numerator in range(1, n // 2 + 1):
        denominator = n - numerator

        if (
            gcd(numerator, denominator) == 1
            and numerator / denominator > max_fraction[0] / max_fraction[1]
        ):
            max_fraction = (numerator, denominator)

    return max_fraction


n = int(input())
numerator, denominator = find_largest_irreducible_fraction(n)

print(f"{numerator}/{denominator}")


# 8
from fractions import Fraction

n = int(input())
fractions: set[Fraction] = set()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j:
            fractions.add(Fraction(i, j))

print(*sorted(fractions), sep="\n")
