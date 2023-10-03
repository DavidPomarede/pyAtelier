import turtle as t
import random

# Set up the Turtle screen
t.bgcolor("black")
t.speed(0)
t.pensize(2)

# Function to draw a colorful starburst pattern
def draw_starburst(x, y, arms, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 360 / arms
    for _ in range(arms):
        t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        t.forward(size)
        t.right(45)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(45)
        t.forward(size)
        t.right(180 - angle)

# Draw multiple starburst patterns at random positions
for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    arms = random.randint(6, 12)
    size = random.randint(50, 150)
    draw_starburst(x, y, arms, size)

# Close the Turtle graphics window when clicked
t.exitonclick()

