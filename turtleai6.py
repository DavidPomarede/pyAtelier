import turtle as t
import random

# Set up the Turtle screen
t.bgcolor("black")
t.speed(0)
t.pensize(2)
t.color("green")

# Function to draw a fractal tree
def draw_fractal_tree(branch_length, angle, depth):
    if depth > 0:
        t.pencolor("brown")
        t.forward(branch_length)
        t.right(angle)
        draw_fractal_tree(branch_length * random.uniform(0.6, 0.8), angle * random.uniform(0.6, 0.8), depth - 1)
        t.left(angle * 2)
        draw_fractal_tree(branch_length * random.uniform(0.6, 0.8), angle * random.uniform(0.6, 0.8), depth - 1)
        t.right(angle)
        t.penup()
        t.backward(branch_length)
        t.pendown()

# Function to create colorful flowers
def draw_flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    colors = ["red", "orange", "yellow", "pink", "purple"]
    for _ in range(6):
        t.color(random.choice(colors))
        t.begin_fill()
        t.circle(10, 180)
        t.left(120)
        t.end_fill()

# Set initial position and angle
t.penup()
t.goto(0, -200)
t.setheading(90)
t.pendown()

# Draw the fractal tree
draw_fractal_tree(100, 30, 8)

# Draw colorful flowers at the end of branches
for _ in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, -50)
    draw_flower(x, y)

# Hide the turtle
t.hideturtle()

# Close the Turtle graphics window when clicked
t.exitonclick()
