import turtle
import random

turtle.colormode(255)
turtle.pensize(7)

for i in range(1, 1000):
    turtle.forward(random.randrange(0, 30))
    turtle.right(random.randrange(0,90))
    turtle.pencolor(random.randrange(245,255), random.randrange(1,255), random.randrange(1,255))


