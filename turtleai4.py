import turtle as t
import random

# Set up the Turtle screen
t.bgcolor("black")
t.speed(0)
t.pensize(2)

# Function to draw a colorful gradient-filled shape
def draw_gradient_shape(sides, size, gradient_colors):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    angle = 360 / sides
    for _ in range(sides):
        t.color(random.choice(gradient_colors))
        t.begin_fill()
        for _ in range(2):
            t.forward(size)
            t.right(90)
        t.end_fill()
        size -= 5
        t.right(angle)

# Define gradient color palettes
palettes = [
    ["#ff6b6b", "#ffb997", "#ffe4e1", "#ffc3a0"],
    ["#94c5d6", "#c5e0e6", "#edf4f7", "#ffffff"],
    ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf"],
]

# Draw a series of gradient-filled shapes
for _ in range(36):
    sides = random.randint(6, 12)
    size = random.randint(30, 100)
    gradient_colors = random.choice(palettes)
    draw_gradient_shape(sides, size, gradient_colors)
    t.right(10)

# Close the Turtle graphics window when clicked
t.exitonclick()
