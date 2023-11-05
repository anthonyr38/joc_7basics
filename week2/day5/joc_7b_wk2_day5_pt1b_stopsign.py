#JoC 7 Basics Week 2 Day 5 Pt 1B
# by Anthony Rodriguez

import turtle

turtle.shape("arrow")
turtle.color("red")
turtle.speed(0)
turtle.pensize(5)

def back(bdist):
    turtle.penup()
    turtle.backward(bdist)
    turtle.pendown()

def octagon(octosize):
    for i in range (8):
        turtle.forward(octosize)
        turtle.left(45)

def rectangle(rectsize):
    for j in range(2):
        turtle.forward(rectsize / 5)
        turtle.right(90)
        turtle.forward(rectsize * 2)
        turtle.right(90)

def stop_Sign(stopsize):
    turtle.color("red")

    octagon(stopsize)

    turtle.penup()
    turtle.forward(((stopsize / 5) * 2))
    turtle.pendown()

    turtle.color("gray")

    rectangle(stopsize)

stop_Sign(100)

back(400)

stop_Sign(300)

turtle.ht()
turtle.Screen().exitonclick()