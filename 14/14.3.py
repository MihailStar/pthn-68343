# 1
import turtle

turtle.hideturtle()
turtle.speed(0)

color = "blue"
turtle.pencolor(color)
turtle.fillcolor(color)
turtle.begin_fill()
turtle.goto(24, 0)
turtle.goto(24, -24)
turtle.goto(-24, -24)
turtle.goto(-24, -0)
turtle.goto(0, -0)
turtle.end_fill()

color = "brown"
turtle.pencolor(color)
turtle.fillcolor(color)
turtle.begin_fill()
turtle.goto(32, 0)
turtle.goto(0, 32)
turtle.goto(-32, 0)
turtle.goto(0, 0)
turtle.end_fill()


# 2
import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-(32 + 16), 64 + 16 + 64 + 16)
turtle.pendown()
turtle.begin_fill()
turtle.forward(16 + 64 + 16)
turtle.right(90)
turtle.forward(16 + 64 + 16 + 64 + 16 + 64 + 16)
turtle.right(90)
turtle.forward(16 + 64 + 16)
turtle.right(90)
turtle.forward(16 + 64 + 16 + 64 + 16 + 64 + 16)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 64 + 16 + 32)
turtle.pencolor("red")
turtle.dot(64)

turtle.goto(0, 32)
turtle.pencolor("yellow")
turtle.dot(64)

turtle.goto(0, -(16 + 32))
turtle.pencolor("green")
turtle.dot(64)
turtle.pendown()


# 3
import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-40, -22)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for _ in range(3):
    turtle.forward(80)
    turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, 22)
for _ in range(3):
    turtle.forward(80)
    turtle.right(120)
    turtle.dot(20)
turtle.pendown()
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for _ in range(3):
    turtle.forward(80)
    turtle.right(120)
turtle.end_fill()


# 4
import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.Screen().colormode(255)  # -

for i in range(10, 0, -1):
    turtle.penup()
    turtle.goto(0, -10 * i)
    turtle.pendown()
    turtle.fillcolor((25 * i, 25 * i, 25 * i))
    turtle.begin_fill()
    turtle.circle(10 * i)
    turtle.end_fill()


# 5
import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.Screen().bgcolor("blue")

turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(85)
turtle.end_fill()

turtle.goto(25, 0)
turtle.pencolor("blue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(85)
turtle.end_fill()


# 6
import turtle

turtle.hideturtle()
turtle.tracer(0, 32)

turtle.Screen().bgcolor("blue")
turtle.dot(100, "yellow")

shadow = turtle.Turtle()
shadow.hideturtle()
shadow.penup()

while True:
    for i in range(100, -100, -1):
        shadow.clear()
        shadow.goto(i, 0)
        shadow.dot(100, "blue")
        # @tutorial https://stepik.org/lesson/502329/step/7?discussion=6067370&unit=494030
        turtle.update()


# 7
import turtle
from random import randint, randrange

turtle.hideturtle()
turtle.speed(0)
turtle.Screen().colormode(255)  # -

for _ in range(64):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    size = randrange(4, 20 + 1, 2)

    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(**{key: randrange(-176, 176 + 1, 16) for key in "xy"})
    turtle.pendown()
    turtle.right(randint(0, 90))
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


# 8
import turtle
from math import pow, radians, sin, sqrt, tan
from random import randint

turtle.hideturtle()
turtle.speed(0)
turtle.Screen().colormode(255)  # -


def draw_polygon(number_of_sides, side_length):
    # @tutorial https://skysmart.ru/articles/mathematic/radius-okruzhnosti
    radius = side_length / (2 * sin(radians(180 / number_of_side)))
    offset_angle = 360 / number_of_sides + (180 - 360 / number_of_sides) / 2
    turtle.penup()
    turtle.left(offset_angle)
    turtle.forward(radius)
    turtle.right(offset_angle)
    turtle.pendown()

    turtle.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.begin_fill()
    for _ in range(number_of_sides):
        turtle.forward(side_length)
        turtle.right(360 / number_of_sides)
    turtle.end_fill()


def calculate_area(number_of_sides, side_length):
    area = (number_of_sides * pow(side_length, 2)) / (
        4 * tan(radians(180 / number_of_sides))
    )
    return area


def calculate_side_length(number_of_sides, area):
    side_length = sqrt(area * 4 * tan(radians(180 / number_of_sides)) / number_of_sides)
    return side_length


canvas_width = turtle.window_width()
canvas_height = turtle.window_height()
r = 24
gap = 12
number_of_sides = (
    (3, 6, 4, 3, 5),
    (6, 3, 4, 5, 3),
    (4, 7, 3, 6, 7),
    (3, 6, 4, 3, 5),
    (5, 4, 6, 7, 8),
)

for y, row in enumerate(number_of_sides):
    for x, number_of_side in enumerate(row):
        turtle.penup()
        turtle.goto(
            -(r * 2 + gap) * (len(number_of_sides) // 2) + (r * 2 + gap) * x,
            -(r * 2 + gap) * (len(number_of_sides) // 2) + (r * 2 + gap) * y + -r,
        )
        turtle.pendown()

        turtle.circle(r)

for y, row in enumerate(reversed(number_of_sides)):
    for x, number_of_side in enumerate(row):
        turtle.penup()
        turtle.goto(
            -(r * 2 + gap) * (len(number_of_sides) // 2) + (r * 2 + gap) * x,
            -(r * 2 + gap) * (len(number_of_sides) // 2) + (r * 2 + gap) * y,
        )
        turtle.pendown()

        draw_polygon(
            number_of_side,
            calculate_side_length(number_of_side, calculate_area(3, r * 2)),
        )


# 9
import turtle

number_of_cells = 5
cell_side = 20

turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-cell_side * (number_of_cells / 2), cell_side * (number_of_cells / 2))
turtle.pendown()


def square(side, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.end_fill()


for y in range(5):
    for x in range(number_of_cells):
        square(cell_side, "black" if (y + x) % 2 == 0 else "white")
        turtle.penup()
        turtle.forward(cell_side)
        turtle.pendown()
    turtle.penup()
    turtle.backward(cell_side * number_of_cells)
    turtle.goto(turtle.position()[0], turtle.position()[1] - cell_side)
    turtle.pendown()

for _i in range(4):
    turtle.forward(cell_side * number_of_cells)
    turtle.left(90)


# 10
import turtle

font_size = 10

turtle.hideturtle()
turtle.speed(0)

for title, align, indent in (
    ("Восток", "left", (0, -font_size // 2)),
    ("Юг", "center", (0, -font_size)),
    ("Запад", "right", (0, -font_size // 2)),
    ("Север", "center", (0, 0)),
):
    turtle.forward(100)
    turtle.penup()
    turtle.forward(font_size)
    turtle.goto(turtle.position()[0] + indent[0], turtle.position()[1] + indent[1])
    turtle.write(title, align=align, font=("sans-serif", font_size, "normal"))
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.right(90)

turtle.penup()
turtle.goto(0, -30)
turtle.pendown()

turtle.circle(30)


# 12
import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-80 / 2, 80 * 1.25)
turtle.pendown()

for index, color in enumerate(("black", "white", "red")):
    turtle.penup()
    turtle.goto(turtle.position()[0] + 2 / 2, turtle.position()[1] - 2)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(8):
        turtle.forward(80 - 2 * index)
        turtle.right(360 / 8)
    turtle.end_fill()

turtle.penup()
turtle.goto(0, -20)
turtle.pendown()
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.write("STOP", align="center", font=("sans-serif", 40, "normal"))


# 13
import turtle
from random import randint, randrange

turtle.hideturtle()
turtle.tracer(0)

turtle.Screen().colormode(255)  # -
turtle.Screen().bgcolor((0, 30, 66))


def goto_without_line(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_star(x, y, size):
    star_color = (255, 252, 138)
    goto_without_line(x, y)
    turtle.dot(size, star_color)


def draw_stars(number_of):
    half_width_of_canvas = turtle.Screen().window_width() // 2
    half_height_of_canvas = turtle.Screen().window_height() // 2
    starting_position = (turtle.xcor(), turtle.ycor())
    for _ in range(number_of):
        x = randint(-half_width_of_canvas, half_width_of_canvas)
        y = randint(-half_height_of_canvas, half_height_of_canvas)
        size = randint(1, 4)
        draw_star(x=x, y=y, size=size)
    goto_without_line(*starting_position)


def draw_building(windows_in_width, windows_in_height, window_size):
    building_color = (2, 67, 160)
    window_color = (255, 252, 138)
    width = 12 + window_size * windows_in_width + 8 * (windows_in_width - 1) + 12
    height = 24 + window_size * windows_in_height + 8 * (windows_in_height - 1) + 24
    starting_position = (turtle.xcor(), turtle.ycor())
    turtle.pencolor(building_color)
    turtle.fillcolor(building_color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    for _ in range(windows_in_width // 2 + windows_in_height // 2):
        w, h = randint(0, windows_in_width - 1), randint(0, windows_in_height - 1)
        goto_without_line(
            starting_position[0] + (12 + window_size * w + 8 * w),
            starting_position[1] - (24 + window_size * h + 8 * h),
        )
        turtle.fillcolor(window_color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(window_size)
            turtle.right(90)
        turtle.end_fill()
        goto_without_line(*starting_position)


def draw_buildings(number_of):
    for _ in range(number_of):
        goto_without_line(
            randrange(
                -turtle.Screen().window_width() // 2 + -24,
                turtle.Screen().window_width() // 2 - 24,
                24,
            ),
            randrange(
                -turtle.Screen().window_height() // 4,
                24,
                24,
            ),
        )
        draw_building(
            windows_in_width=randint(4, 8),
            windows_in_height=randint(8, 16),
            window_size=randint(8, 12),
        )
        goto_without_line(0, 0)


draw_stars(number_of=40)
draw_buildings(number_of=4)

goto_without_line(
    -turtle.Screen().window_width() // 2, -turtle.Screen().window_height() // 4
)

turtle.pencolor((2, 67, 160))
turtle.fillcolor((2, 67, 160))
turtle.begin_fill()
for _ in range(2):
    turtle.forward(turtle.Screen().window_width())
    turtle.right(90)
    turtle.forward(turtle.Screen().window_height() // 4)
    turtle.right(90)
turtle.end_fill()

turtle.update()


# 14
import turtle
from math import cos, pi, sin

turtle.hideturtle()

turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()

t = 0

while t <= 2 * pi:
    x = 128 * sin(t) ** 3
    y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
    t += 0.01

    turtle.goto(x, y)

turtle.end_fill()


# 15
import turtle as t
from random import randrange

t.hideturtle()
t.tracer(0)

turtle.Screen().colormode(255)  # -
t.Screen().bgcolor("black")


def draw_star(number_of_ends=5):
    pre_angel = randrange(0, 360 + 1)
    color = (randrange(0, 255 + 1), randrange(0, 255 + 1), randrange(0, 255 + 1))
    size = randrange(8, 32 + 1, 4)

    t.right(pre_angel)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(number_of_ends):
        t.forward(size)
        t.right(180 - 180 / number_of_ends)
    t.end_fill()
    t.left(pre_angel)


def onclick_handle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    draw_star(randrange(5, 11 + 1, 2))

    t.update()


t.Screen().onclick(onclick_handle)
t.Screen().listen()
