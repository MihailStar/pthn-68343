# 1
countries = ("Russia", "Argentina", "Spain", "Slovakia", "Canada", "Slovenia", "Italy")
last = countries[len(countries) - 1]
last = countries[-1]

print(last)


# 2
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)

print(primes[:6])


# 3
countries = (
    "Russia",
    "Argentina",
    "Slovakia",
    "Canada",
    "Slovenia",
    "Italy",
    "Spain",
    "Ukraine",
    "Chile",
    "Cameroon",
)

print(countries[2:])


# 4
countries = (
    "Russia",
    "Argentina",
    "Slovakia",
    "Canada",
    "Slovenia",
    "Italy",
    "Spain",
    "Ukraine",
    "Chile",
    "Cameroon",
)

print(countries[:-3])


# 5
countries = (
    "Russia",
    "Argentina",
    "Slovakia",
    "Canada",
    "Slovenia",
    "Italy",
    "Spain",
    "Ukraine",
    "Chile",
    "Cameroon",
)

print(countries[3:-2])


# 6
countries = (
    "Romania",
    "Poland",
    "Estonia",
    "Bulgaria",
    "Slovakia",
    "Slovenia",
    "Hungary",
)
number = len(countries)

print(number)


# 7
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)

print(sum((min(numbers), max(numbers))))


# 8
countries = ("Russia", "Argentina", "Spain", "Slovakia", "Canada", "Slovenia", "Italy")
index = countries.index("Slovenia")

print(index)


# 9
countries = (
    "Russia",
    "Argentina",
    "Spain",
    "Slovakia",
    "Canada",
    "Slovenia",
    "Italy",
    "Spain",
    "Ukraine",
    "Chile",
    "Spain",
    "Cameroon",
)
number = countries.count("Spain")

print(number)


# 10
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)

print(numbers1 * 2 + numbers2 * 9 + numbers3)


# 11
city_name = input()
city_year = int(input())
city = (city_name, city_year)

print(city)


# 12
tuples = [
    (),
    (),
    ("",),
    ("a", "b"),
    (),
    ("a", "b", "c"),
    (1,),
    (),
    (),
    ("d",),
    ("", ""),
    (),
]
non_empty_tuples = list(filter(bool, tuples))

print(non_empty_tuples)


# 13
tuples = [
    (10, 20, 40),
    (40, 50, 60),
    (70, 80, 90),
    (10, 90),
    (1, 2, 3, 4),
    (5, 6, 10, 2, 1, 77),
]
new_tuples = [tuple[:-1] + (100,) for tuple in tuples]

print(new_tuples)
