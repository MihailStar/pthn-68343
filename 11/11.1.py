# 1
my_dict: dict[str, list[int]] = {}
my_dict = {k: [n for n in my_dict[k] if n < 21] for k in my_dict}


# 2
emails = {
    "nosu.edu": ["timyr", "joseph", "svetlana.gaeva", "larisa.mamuk"],
    "gmail.com": ["ruslan.chaika", "rustam.mini", "stepik-best"],
    "msu.edu": ["apple.fruit", "beegeek", "beegeek.school"],
    "yandex.ru": ["surface", "google"],
    "hse.edu": ["tomas-henders", "cream.soda", "zivert"],
    "mail.ru": ["angel.down", "joanne", "the.fame.moster"],
}

print(*sorted([f"{u}@{d}" for d, us in emails.items() for u in us]), sep="\n")
