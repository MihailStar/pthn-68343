# 1
with open("./output.txt", "w") as file:
    file.write(input())


# 2
from random import randrange

with open("./random.txt", "w") as file:
    for _index in range(25):
        print(randrange(111, 778), file=file)


# 3
with open("./input.txt", "r") as input, open("./output.txt", "w") as output:
    for number, line in enumerate(input, 1):
        output.write(f"{number}) {line}")


# 4
with open("./class_scores.txt") as input, open("new_scores.txt", "w") as output:
    for line in input:
        name, rating = line.rstrip().split()
        rating = int(rating)
        new_rating = rating + 5
        new_rating = 100 if new_rating > 100 else new_rating

        print(name, new_rating, file=output)


# 5
from collections import Counter

with open("./goats.txt") as input, open("./answer.txt", "w") as output:
    for line in input:
        if line.startswith("GOATS"):
            break

    goats = [line.rstrip() for line in input.readlines()]
    goat_to_number_of: Counter[str] = Counter(goats)

    output.writelines(
        sorted(
            map(
                lambda item: item[0] + "\n",
                filter(
                    lambda item: item[1] >= len(goats) * 0.07,
                    goat_to_number_of.items(),
                ),
            )
        )
    )


# 6
with open("./output.txt", "a") as output:
    for _ in range(int(input())):
        with open(input()) as file:
            for line in file:
                output.write(line)


# 7
with open("./logfile.txt", encoding="utf-8") as file, open(
    "./output.txt", "w", encoding="utf-8"
) as output:
    for line in file:
        username, login_time, logout_time = line.split(", ")
        login_hour, login_minute = map(int, login_time.split(":"))
        logout_hour, logout_minute = map(int, logout_time.split(":"))
        online = (logout_hour * 60 + logout_minute) - (login_hour * 60 + login_minute)
        if online > 59:
            print(username, file=output)
