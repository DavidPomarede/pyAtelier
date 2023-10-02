import turtle
import random
 
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
first = random.choice(list1) + random.choice(list2)



turtle.down()
turtle.forward(random.choice(list1) + random.choice(list2))
turtle.right(random.choice(list1) + random.choice(list2))
turtle.forward(random.choice(list1) + random.choice(list2))
turtle.right(random.choice(list1) + random.choice(list2))
turtle.forward(random.choice(list1) + random.choice(list2))
turtle.right(random.choice(list1) + random.choice(list2))
turtle.forward(random.choice(list1) + random.choice(list2))
turtle.right(random.choice(list1) + random.choice(list2))

for side in range(random.choice(list1) + random.choice(list2)):
    turtle.forward(random.choice(list1) + random.choice(list2))
    turtle.right(random.choice(list1) + random.choice(list2))
turtle.done()


