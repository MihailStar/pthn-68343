# 1
items = [
    10,
    "30",
    30,
    10,
    "56",
    34,
    "12",
    90,
    89,
    34,
    45,
    "67",
    12,
    10,
    90,
    23,
    "45",
    56,
    "56",
    1,
    5,
    "6",
    5,
]
myset = set(map(int, items))
print(*sorted(myset))


# 2
words = [
    "Plum",
    "Grapefruit",
    "apple",
    "orange",
    "pomegranate",
    "Cranberry",
    "lime",
    "Lemon",
    "grapes",
    "persimmon",
    "tangerine",
    "Watermelon",
    "currant",
    "Almond",
]
print(*sorted({word[0].lower() for word in words}))


# 3
from string import punctuation
sentence = """My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges."""
print(*sorted({word.strip(punctuation).lower() for word in sentence.split()}))


# 4
from string import punctuation
sentence = """My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges."""
print(
    *sorted(
        {
            stripped_word.lower()
            for word in sentence.split()
            if len(stripped_word := word.strip(punctuation)) < 4
        }
    )
)


# 5
files = [
    "python.png",
    "qwerty.py",
    "stepik.png",
    "beegeek.org",
    "windows.pnp",
    "pen.txt",
    "phone.py",
    "book.txT",
    "board.pNg",
    "keyBoard.jpg",
    "Python.PNg",
    "apple.jpeg",
    "png.png",
    "input.tXt",
    "split.pop",
    "solution.Py",
    "stepik.org",
    "kotlin.ko",
    "github.git",
]
print(
    *sorted(
        {
            lowered_file
            for file in files
            if (lowered_file := file.lower()).endswith(".png")
        }
    )
)
