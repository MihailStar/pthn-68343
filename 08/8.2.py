# 1
# Формула включения-исключения
# ∣A∪B∪C∣ = ∣A∣ + ∣B∣ + ∣C∣ − ∣A∩B∣ − ∣B∩C∣ − ∣C∩A∣ + ∣A∩B∩C∣
# ∣A∣ - Мощность (Cardinality), количество элементов
# A∪B - Объединение (Union)
# A∩B - Пересечение (Intersection)
d = {
    "∣n∣": int(input()),    # на море
    "∣m∣": int(input()),    # в деревню
    "∣k∣": int(input()),    # в горы
    "∣n∩m∣": int(input()),  # и на море и в деревню
    "∣m∩k∣": int(input()),  # и в деревню и в горы
    "∣k∩n∣": 0,             # и в горы и на море
    "∣n∩m∩k∣": 0,           # и на море и в деревню и в горы
    "z": int(input()),      # не ездили
}
number_of_pupils = (
    d["∣n∣"] + d["∣m∣"] + d["∣k∣"] - d["∣n∩m∣"] - d["∣m∩k∣"] - d["∣k∩n∣"] + d["∣n∩m∩k∣"]
) + d["z"]
print(number_of_pupils)


# 2
# @tutorial https://stepik.org/lesson/479457/step/15?discussion=7958675&unit=470432
d = {
    "∣n∣": int(input()),      # первую
    "∣m∣": int(input()),      # вторую
    "∣k∣": int(input()),      # третью
    "∣n∪m∣": int(input()),    # или первую или вторую или обе
    "∣m∪k∣": int(input()),    # или вторую или третью или обе
    "∣k∪n∣": int(input()),    # или третью или первую или обе
    "∣n∩m∩k∣": int(input()),  # и первую и вторую и третью
    "a": int(input()),        # учеников
}
only_1_and_2 = d["∣n∣"] + d["∣m∣"] - d["∣n∪m∣"] - d["∣n∩m∩k∣"]
only_2_and_3 = d["∣m∣"] + d["∣k∣"] - d["∣m∪k∣"] - d["∣n∩m∩k∣"]
only_3_and_1 = d["∣k∣"] + d["∣n∣"] - d["∣k∪n∣"] - d["∣n∩m∩k∣"]
only_two_book = only_1_and_2 + only_2_and_3 + only_3_and_1
only_1 = d["∣n∣"] - only_1_and_2 - only_3_and_1 - d["∣n∩m∩k∣"]
only_2 = d["∣m∣"] - only_1_and_2 - only_2_and_3 - d["∣n∩m∩k∣"]
only_3 = d["∣k∣"] - only_2_and_3 - only_3_and_1 - d["∣n∩m∩k∣"]
only_one_book = only_1 + only_2 + only_3
print(only_one_book)
print(only_two_book)
print(d["a"] - only_one_book - only_two_book - d["∣n∩m∩k∣"])
