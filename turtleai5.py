import turtle as t
import random

# Set up the Turtle screen
t.bgcolor("black")
t.speed(0)
t.pensize(2)
t.color("green")

# Function to draw a fractal tree
def draw_fractal_tree(branch_length, turt):
    if branch_length < 10:
        t.pencolor(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        t.forward(branch_length)
        t.penup()
        t.backward(branch_length)
        t.pendown()
    else:
        t.pencolor("brown")
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - random.randint(10, 20), t)
        t.left(40)
        draw_fractal_tree(branch_length - random.randint(10, 20), t)
        t.right(20)
        t.pencolor(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        t.backward(branch_length)

# Function to create colorful leaves
def draw_leaves(num_leaves, size):
    t.speed(0)
    for _ in range(num_leaves):
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 0))
        t.pendown()
        t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        t.begin_fill()
        t.circle(size)
        t.end_fill()

# Set initial position and angle
t.penup()
t.goto(0, -200)
t.setheading(90)
t.pendown()

# Draw the fractal tree
draw_fractal_tree(100, t)

# Draw colorful leaves at the end of branches
draw_leaves(100, 10)

# Hide the turtle
t.hideturtle()

# Close the Turtle graphics window when clicked
t.exitonclick()
