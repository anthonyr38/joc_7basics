 

import turtle

turtle.color("green")

#length = 80 

def back(dist):
  turtle.penup()
  turtle.backward(dist)
  turtle.pendown()

def forward(fwddist):
  turtle.penup()
  turtle.forward(fwddist)
  turtle.pendown()


def triangle(length):
  for i in range(3):
    turtle.forward(length)
    turtle.left(120)

def square(length):
  for i in range(4):
    turtle.forward(length)
    turtle.left(90)

triangle(150)
back(100)
triangle(100)
back(50)
triangle(50)

turtle.color("cyan")

square(50)
forward(50)
square(100)
forward(100)
square(150)


input("Hit Enter")
