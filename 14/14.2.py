# 1
import turtle

size = 20

turtle.pensize(size)

for i in range(3):
    turtle.dot()
    turtle.penup()
    turtle.forward(size * 2 + size // 2)
    turtle.pendown()

turtle.hideturtle()


# 2
import turtle

width, height = 100, 50


def dot(size=5):
    turtle.pensize(size)
    turtle.dot()
    turtle.pensize()


for i in range(2):
    turtle.forward(width)
    dot()
    turtle.right(90)

    turtle.forward(height)
    dot()
    turtle.right(90)

turtle.hideturtle()


# 3
import turtle

n = 8

turtle.dot(22)

for i in range(n):
    turtle.forward(100)
    turtle.shape("arrow" if i % 2 else "triangle")
    turtle.stamp()
    turtle.shape("classic")
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.right(360 / n)

turtle.hideturtle()


# 4
import turtle

n = 10

turtle.shape("turtle")
turtle.stamp()
turtle.penup()

for _i in range(n):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(360 / n)

turtle.hideturtle()


# 5
import turtle

turtle.shape("turtle")
turtle.pensize(4)
turtle.penup()
turtle.Screen().bgcolor("azure")

for _ in range(12):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(16)
    turtle.pendown()
    turtle.backward(12)
    turtle.penup()
    turtle.backward(100 - 16 - 12)
    turtle.right(360 / 12)


# 6
import turtle

turtle.shape("turtle")
turtle.penup()
turtle.Screen().bgcolor("aquamarine")

for i in range(55):
    turtle.stamp()
    turtle.forward(i)
    turtle.right(15)


# 7
import turtle

colors = ("red", "blue", "yellow", "green", "purple", "orange")

turtle.hideturtle()

for i in range(45):
    turtle.pencolor(colors[i % len(colors)])
    turtle.pensize(int(i * (3 / 5)))
    turtle.forward(i * 3)
    turtle.left(45)


# 8
import turtle

for _ in range(6):
    for _ in range(3):
        turtle.forward(40)
        turtle.left(120)
    turtle.forward(40)
    turtle.right(60)


# 9
import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(0, 100)

for sign in (-1, 1):
    for i in range(1, 6):
        turtle.pendown()
        turtle.pencolor("green")
        turtle.goto(sign * 32 * i - sign * 32 / 2, -100)
        turtle.pencolor("blue")
        turtle.dot(4)
        turtle.penup()
        turtle.goto(0, 100)

turtle.pencolor("red")
turtle.dot(4)


# 10
# import turtle

# radius = 64
# offset = 8
# positions = (
#     (-radius * 2 - -offset * 2, 0),
#     (0, 0),
#     (radius * 2 - offset * 2, 0),
#     (-radius - -offset, -radius * 2 - -offset * 4),
#     (radius - offset, -radius * 2 - -offset * 4),
# )
# colors = ("blue", "black", "red", "yellow", "green")

# turtle.hideturtle()
# turtle.pensize(4)

# for color, position in zip(colors, positions):
#     turtle.penup()
#     turtle.goto(position)
#     turtle.pendown()
#     turtle.pencolor(color)
#     turtle.circle(radius)

import turtle

radius = 64
positions = (
    (radius + 2, -radius * 1.5),
    (-radius * 2 + -2, 0),
    (0, 0),
    (radius * 2 + 2, 0),
    (-radius + -2, -radius * 1.5),
    (radius + 2, -radius * 1.5),
)
colors = ("green", "blue", "black", "red", "yellow")

turtle.hideturtle()
turtle.pensize(4)

for color, position in zip(colors, positions):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.circle(radius)


# 11
import turtle

turtle.hideturtle()

turtle.circle(76)

turtle.circle(44)

turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.goto(0, 64)
turtle.circle(8 - 1)

turtle.penup()
turtle.goto(-32 + -8, 76 + 8)
turtle.pendown()
turtle.dot(8 * 2)

turtle.penup()
turtle.goto(32 + 8, 76 + 8)
turtle.pendown()
turtle.dot(8 * 2)

turtle.penup()
turtle.goto(-64, 128)
turtle.pendown()
turtle.circle(24)

turtle.penup()
turtle.goto(64, 128)
turtle.pendown()
turtle.circle(24)


# 12
import turtle
from random import choice, randrange

colors = ("lightBlue", "royalBlue", "skyBlue", "steelBlue")

turtle.hideturtle()
turtle.speed(0)

for _ in range(5):
    size = randrange(4, 12 + 1, 2)

    turtle.pencolor(choice(colors))
    turtle.penup()
    turtle.goto(**{key: randrange(-150, 150, 20) for key in "xy"})
    turtle.pendown()

    for _ in range(8):
        for _ in range(3):
            turtle.forward(size)
            turtle.left(45)
            turtle.forward(size)
            turtle.backward(size)
            turtle.right(45 * 2)
            turtle.forward(size)
            turtle.backward(size)
            turtle.left(45)
        turtle.forward(size + 2)
        turtle.penup()
        turtle.backward(size * 4 + 2)
        turtle.pendown()
        turtle.right(360 / 8)
