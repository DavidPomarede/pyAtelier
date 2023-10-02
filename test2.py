import turtle
import random
import logging
 
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
first = random.choice(list1) + random.choice(list2)

#logging.debug(msg)
#logging.info()
#turtle.down()
#turtle.forward(random.choice(list1) + random.choice(list2))
#turtle.right(random.choice(list1) + random.choice(list2))
#turtle.forward(random.choice(list1) + random.choice(list2))
#turtle.right(random.choice(list1) + random.choice(list2))
#turtle.forward(random.choice(list1) + random.choice(list2))
#turtle.right(random.choice(list1) + random.choice(list2))
#turtle.forward(random.choice(list1) + random.choice(list2))
#turtle.left(random.choice(list1) + random.choice(list2))
#
#next_choice = random.choice(list1)
#if next_choice <= 6 : {
#    turtle.right(random.choice(list1) + random.choice(list2))
#    turtle.forward(random.choice(list1) + random.choice(list2))
#}
#
#if next_choice >= 6 : {
#    turtle.left(random.choice(list1) + random.choice(list2))
#    turtle.forward(random.choice(list1) + random.choice(list2))
#}

turtle.speed(100)

cond1 = False


if (turtle.xcor() <= 0) or (turtle.xcor() >= 1000) :
    cond1 = True

elif (turtle.ycor() <= 0) or (turtle.ycor() >= 1000) :
    cond1 = True

if cond1 :
    turtle.right(90)
    cond1 = False





for side in range(5000):
    next_choice = random.choice(list1)
    if next_choice <= 6 :
        turtle.right(10 * (random.choice(list1) + random.choice(list2)))
        turtle.forward(random.choice(list1) * 10)
        #turtle.

    if next_choice >= 6 :
        turtle.left(10 * (random.choice(list1) + random.choice(list2)))
        turtle.forward(random.choice(list1) * 10)


turtle.done()


#t = turtle
#for i in range(100):
#    steps = (random.choice(list) * 100)
#    angle = (random.choice(list) * 360)
#    t.right(angle)
#    t.fd(steps)
#
#t.screen.mainloop()
