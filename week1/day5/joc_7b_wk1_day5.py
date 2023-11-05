
# Joy of Coding 7 Basics Week 1 Day 4

# by Anthony Rodriguez


# Quintessential first program

#print("Hello World!")

# Begin Day 2

import turtle # brings in turtle module / library

turtle.color("blue") # changes turtle pen color to blue

'''turtle.forward(50) # moves turtle in a specific direction relative to where it is facing
turtle.right(120) # rotates turtle a certain number of degrees
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)'''


'''tri_side = 80

turtle.forward(tri_side) # moves turtle in a specific direction relative to where it is facing
turtle.right(120) # rotates turtle a certain number of degrees
turtle.forward(tri_side)
turtle.right(120)
turtle.forward(tri_side)
turtle.right(120)

turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)'''


tri_side1 = 100

'''for side in range(3):
    turtle.forward(tri_side1)
    turtle.left(120)'''

# begin Day 4

def add(x, y):
    print("I will add the numbers %d and %d" % (x, y))
    return x + y

sum = add(5, 7)
print("=", sum)



def triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

'''triangle(100)
triangle(50)
triangle(25)'''

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def movefor(dist):
    back(-1 * dist)

'''triangle(100)
back(75)
triangle(50)
back(50)
triangle(25)'''

def polygon(poly_sides, side_length):
    for i in range(poly_sides):
        turtle.forward(side_length)
        turtle.left(360 / poly_sides)


def square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

'''polygon(4, 100)
back(75)
polygon(3, 50)
back(50)
polygon(6, 25)'''


for n in range (3, 10):
    back(-50)
    polygon(n, 100)
    back(50)
    turtle.right(360 / 7)

def spiral(length, angle):
    for i in range(length, 5, -5):
        turtle.forward(i)
        turtle.right(angle)


spiral(75, 45)

movefor(150)

spiral(100,90)




turtle.Screen().exitonclick() # prevents turtle graphics from closing until you click on it