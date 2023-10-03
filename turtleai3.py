import turtle as t
import random

# Set up the Turtle screen
t.bgcolor("black")
t.speed(0)
t.pensize(2)

# Function to draw a colorful flower-like pattern
def draw_flower(x, y, petals, petal_size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 360 / petals
    for _ in range(petals):
        t.color(random.choice(["red", "orange", "yellow", "pink", "purple", "blue", "green"]))
        t.begin_fill()
        for _ in range(2):
            t.circle(petal_size, 60)
            t.circle(petal_size // 2, 60)
        t.left(180 - angle)
        t.end_fill()

# Draw multiple flower-like patterns at random positions
for _ in range(12):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    petals = random.randint(6, 12)
    petal_size = random.randint(30, 100)
    draw_flower(x, y, petals, petal_size)

# Close the Turtle graphics window when clicked
t.exitonclick()
