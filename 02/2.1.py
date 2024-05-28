# 1
a, b = (int(input()) for _ in range(2))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a**10 + b**10) ** 0.5)


# 2
масса, рост = (float(input()) for _ in range(2))
индекс_массы_тела = масса / (рост * рост)

if индекс_массы_тела < 18.5:
    print("Недостаточная масса")
elif индекс_массы_тела > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")


# 3
string = input()
price = divmod(len(string) * 60, 100)

print(f"{price[0]} р. {price[1]} коп.")


# 4
print(len(input().split()))


# 5
year = int(input())
horoscope = {
    2000: "Дракон",
    2001: "Змея",
    2002: "Лошадь",
    2003: "Овца",
    2004: "Обезьяна",
    2005: "Петух",
    2006: "Собака",
    2007: "Свинья",
    2008: "Крыса",
    2009: "Бык",
    2010: "Тигр",
    2011: "Заяц",
}
animals = [*horoscope.values()]
modulo = 2000 % len(horoscope)
twelve = animals[-modulo:] + animals[:-modulo:]

print(twelve[year % len(horoscope)])


# 6
string = input()

print(int(string[:-5] + string[-5:][::-1]))


# 7
# :fill align sign # 0 width sep .precision type
# :sep (',' либо '_')
# @tutorial https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting

print("{:,}".format(int(input())))


# 8
n, k = (int(input()) for _ in range(2))
numbers = [*range(1, n + 1)]
index = 0
counter = 0

while len(numbers) > 1:
    counter += 1

    if counter == k:
        del numbers[index]
        counter = 0
    else:
        index = (index + 1) % len(numbers)

print(numbers[0])
