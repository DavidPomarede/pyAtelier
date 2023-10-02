import sys
import turtle
import random

#from turtle import turtle
from turtle import Screen



# Creating the screen object
screen = Screen()
screen.bgcolor("black")
# Setting the screen color-mode
screen.colormode(255)
turtle.pen(pensize=10)
# Changing the color of the pen the turtle carries
turtle.pencolor(255, 0, 0)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list2 = ["white", "black", "red", "orange", "yellow", "green", "purple", "blue"]
first = random.choice(list1) + random.choice(list1)

width, height = turtle.window_width(), turtle.window_height()

minX, maxX = -width/2, width/2
minY, maxY = -height/2, height/2

turtle.speed(1000)
#turtle.pen(fillcolor="black", pencolor="red", pensize=10, shearfactor=0.1)
def repeated_code():

    #turtle.forward(random.choice(list1))
    for side in range(5000):
        next_choice2 = random.choice(list1)
        next_choice3 = random.randrange(0, 255)
        next_choice4 = random.randrange(0, 255)
        next_choice5 = random.randrange(0, 255)
        
        print(random.choice(list1), next_choice4, next_choice5)
        x = range(10)
        for n in x:
            turtle.pencolor(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            turtle.pen(pensize=random.randrange(1, 100))
            turtle.right(10)
            turtle.forward(random.randrange(1, 10))
            print(turtle.pencolor())
            
        if next_choice2 <= 6 :
            
            print(".test1")
            turtle.right(100 * (random.choice(list1) + random.choice(list1)))
            turtle.forward(random.randrange(1, 25))
#            turtle.pencolor(next_choice3, next_choice4, next_choice5)
            turtle.pen(pensize=random.randrange(1, 100))
        if next_choice2 >= 6 :
            print("..test2")
            turtle.left(100 * (random.choice(list1) + random.choice(list1)))
            turtle.forward(random.randrange(1, 25))
#            turtle.pencolor(next_choice3, next_choice4, next_choice5)
            turtle.pen(pensize=random.randrange(1, 100))
            
        if not minX <= turtle.xcor() <= maxX or not minY <= turtle.ycor() <= maxY:
            next_choice = random.choice(list1)

            if next_choice <= 6 :
                print("...test3")
                turtle.right(100 * (random.choice(list1) + random.choice(list1)))
                turtle.forward(random.randrange(1, 25))
#                turtle.pencolor(next_choice3, next_choice4, next_choice5)
                turtle.pen(pensize=random.randrange(1, 100))
            if next_choice >= 6 :
                print("....test4")
                turtle.left(100 * (random.choice(list1) + random.choice(list1)))
                turtle.forward(random.randrange(1, 25))
#                turtle.pencolor(next_choice3, next_choice4, next_choice5)
                turtle.pen(pensize=random.randrange(1, 100))
            else :
#                turtle.pencolor(next_choice3, next_choice4, next_choice5)
                turtle.pen(pensize=random.randrange(1, 100))
                turtle.home()


#turtle.done()

 #   if not minX <= turtle.xcor() <= maxX or not minY <= turtle.ycor() <= maxY:
  #      turtle.right(180)
        
    turtle.ontimer(repeated_code, 100)  # repeat every 1/10th of a second

repeated_code()

turtle.mainloop()  # turn over control to tkinter event loop

