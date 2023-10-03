import turtle as t
import random

# Set up the Turtle screen
t.bgcolor("black")
t.speed(0)
t.pensize(2)

# Function to draw a colorful geometric pattern
def draw_geometric_pattern(sides, size, repetitions, angle):
    for _ in range(repetitions):
        t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        t.begin_fill()
        for _ in range(sides):
            t.forward(size)
            t.right(360 / sides)
        t.end_fill()
        t.right(angle)

# Draw a series of colorful geometric patterns
draw_geometric_pattern(3, 100, 10, 36)
draw_geometric_pattern(4, 80, 10, -45)
draw_geometric_pattern(5, 60, 10, 60)
draw_geometric_pattern(6, 40, 10, -72)

# Hide the turtle
t.hideturtle()

# Close the Turtle graphics window when clicked
t.exitonclick()
