import turtle
import math

DEG36 = 36 * math.pi / 180
DEG54 = 54 * math.pi / 180

# some constants to allow flexibility in construction
GRADS = 36
RUFFLES = 5
SIDE = 100
SHORTSIDE = SIDE * math.sin(DEG36) / math.sin(DEG54)

# convenience function to draw a left parol tail
def draw_left_tail(turt):
    for i in range(1, RUFFLES + 1):
        ruff_len = SIDE * 0.1 * i
        turt.seth(-30)
        turt.forward(ruff_len)
        turt.seth(180)
        turt.forward(ruff_len * 2)
        if i != RUFFLES:
            turt.seth(-30)
            turt.forward(ruff_len)

# convenience function to draw a right parol tail
def draw_right_tail(turt):
    for i in range(1, RUFFLES + 1):
        ruff_len = SIDE * 0.1 * i
        turt.seth(-150)
        turt.forward(ruff_len)
        turt.seth(0)
        turt.forward(ruff_len * 2)
        if i != RUFFLES:
            turt.seth(-150)
            turt.forward(ruff_len)

# set up the turtle's world; let's call him Leo
leo = turtle.Turtle()
turtle.bgcolor("BLACK")

leo.speed(8)
leo.shape("turtle")
leo.penup()

# let's draw the ruffly outer ring of the parol
leo.home()
leo.color("RED")
leo.pensize(1)
for i in range(GRADS * 2):
    leo.penup()
    leo.forward(SIDE * 1.25)
    leo.dot(SIDE / 10)
    leo.back(SIDE * 1.25)
    leo.left(360 / GRADS / 2)

# let's draw the rings themselves
leo.home()
leo.color("RED")
leo.dot(2.5 * SIDE)
leo.color("GREEN")
leo.dot(2.4 * SIDE)
leo.color("RED")
leo.dot(2.1 * SIDE)
leo.color("BLACK")
leo.dot(2.0 * SIDE)

# let's draw some creases on the rings
leo.home()
leo.color("WHITE")
leo.pensize(1)
for i in range(GRADS):
    leo.penup()
    leo.forward(SIDE * 1.1)
    leo.pendown()
    leo.forward(SIDE * 0.05)
    leo.penup()
    leo.back(SIDE * 1.15)
    leo.left(360 / GRADS)

# let's draw the star!
leo.home()
leo.color("RED", "YELLOW")
leo.setheading(90)
leo.forward(SIDE)

leo.setheading(-72)
leo.pensize(3)

leo.pendown()
leo.begin_fill()
for i in range(5):
    leo.forward(SHORTSIDE)
    leo.left(72)
    leo.forward(SHORTSIDE)
    leo.right(144)
leo.end_fill()
leo.penup()

# let's draw some tail ruffles
leo.home()
leo.seth(-54)
leo.forward(1 * SIDE)
start = leo.position()

leo.color("GOLD")
leo.pensize(8)
leo.pendown()
draw_right_tail(leo)

leo.penup()
leo.setpos(start)
leo.color("RED")
leo.pensize(2)
leo.pendown()
draw_right_tail(leo)

leo.penup()
leo.home()
leo.seth(-54 - 72)
leo.forward(1 * SIDE)
start = leo.position()

leo.color("GOLD")
leo.pensize(8)
leo.pendown()
draw_left_tail(leo)

leo.penup()
leo.setpos(start)
leo.color("RED")
leo.pensize(2)
leo.pendown()
draw_left_tail(leo)

# let's hide Leo for now
leo.hideturtle()
