# 1
import turtle


def rectangle(width, height):
    """
    Parameters:
    width (int)
    height (int)

    Returns:
    None
    """
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


width, height = 100, 50

turtle.penup()
turtle.goto(-width / 2, height / 2)
turtle.pendown()

rectangle(width, height)


# 2
import turtle


def triangle(side):
    """
    Parameters:
    side (int)

    Returns:
    None
    """
    turtle.left(60)

    for _ in range(3):
        turtle.right(120)
        turtle.forward(side)

    turtle.right(60)


side = 100

turtle.penup()
turtle.goto(0, side / 2)
turtle.pendown()

triangle(side)

turtle.right(90)


# 3
import turtle


def square(side):
    """
    Parameters:
    side (int)

    Returns:
    None
    """
    for _ in range(2):
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)


tilt = 30

turtle.left(90 + 45)
square(100)
turtle.left(tilt)
square(100)
turtle.right(tilt * 2)
square(100)
turtle.right(tilt / 2)


# 4
import turtle


def square(side):
    """
    Parameters:
    side (int)

    Returns:
    None
    """
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)


for _ in range(2):
    for _ in range(4):
        square(100)
        turtle.right(90)

    turtle.right(45)


# 5
import turtle


def hexagon(side):
    """
    Parameters:
    side (int)

    Returns:
    None
    """
    for _ in range(6):
        turtle.forward(side)
        turtle.right(180 - 120)


hexagon(100)


# 6
import turtle


def hexagon(side):
    """
    Parameters:
    side (int)

    Returns:
    None
    """
    for _ in range(6):
        turtle.backward(side)
        turtle.right(60)


side = 50

for _ in range(6):
    hexagon(side)
    turtle.penup()
    turtle.right(60)
    turtle.forward(side)
    turtle.pendown()


# 7
import turtle

side = 50

for _ in range(2):
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(60 * 2)


# 8
import turtle

side = 50

turtle.right(6)

for _ in range(10):
    for _ in range(2):
        turtle.forward(side)
        turtle.right(60)
        turtle.forward(side)
        turtle.right(60 * 2)
    turtle.right(360 / 10)

turtle.hideturtle()


# 9
import turtle

n = 12
size = 50

for _ in range(n):
    turtle.forward(size)
    turtle.penup()
    turtle.backward(size)
    turtle.pendown()
    turtle.right(360 // n)

turtle.right(90)
turtle.penup()
turtle.forward(size * 1.25)
turtle.pendown()


# 10
import turtle

size = 100

turtle.penup()
turtle.goto(-size / 2, size / 2)
turtle.pendown()

for _ in range(5):
    turtle.forward(size)
    turtle.right(144)


# 11
import turtle

turtle.right(180)


def square(side):
    """
    Parameters:
    side (int)

    Returns:
    None
    """
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)


for i in range(32):
    square(15 + 5 * i)


# 12
import turtle

turtle.left(90)

for i in range(1, 24 + 1):
    for _ in range(2):
        turtle.forward(8 * i)
        turtle.left(90)

turtle.forward(8 * (i + 1))
