import turtle
import random

# Set up the Turtle screen
turtle.setup(400, 400)

turtle.colormode(255)

# Create a Turtle for drawing the face
face = turtle.Turtle()
face.penup()
face.goto(0, -100)
face.pendown()
face.begin_fill()
face.pen(pencolor=(random.randrange(245, 255), random.randrange(1, 255), random.randrange(1, 255)))

# Draw the face (a circle)
face.circle(100)
face.end_fill()

# Create a Turtle for drawing the eyes
eye = turtle.Turtle()
eye.penup()
eye.goto(-40, 50)
eye.pendown()
eye.begin_fill()
eye.pen(pencolor=(random.randrange(245, 255), random.randrange(1, 255), random.randrange(1, 255)))

# Draw the left eye (a circle)
eye.circle(25)
eye.end_fill()

eye.penup()
eye.goto(40, 50)
eye.pendown()
eye.begin_fill()

# Draw the right eye (a circle)
eye.circle(25)
eye.end_fill()

# Create a Turtle for drawing the mouth
mouth = turtle.Turtle()
mouth.penup()
mouth.goto(0, 20)
mouth.pendown()
mouth.pen(pencolor=(random.randrange(245, 255), random.randrange(1, 255), random.randrange(1, 255)))
mouth.width(2)

# Draw the mouth (a smile)
mouth.circle(40, 180)

# Hide the Turtles
face.hideturtle()
eye.hideturtle()
mouth.hideturtle()

# Randomize the colors and shapes for the face
turtle.pensize(7)
turtle.speed(0)
turtle.penup()
for i in range(1, 1000):
    turtle.forward(random.randrange(0, 30))
    turtle.right(random.randrange(0, 90))
    turtle.pen(pencolor=(random.randrange(245, 255), random.randrange(1, 255), random.randrange(1, 255)))
