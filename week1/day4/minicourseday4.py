import turtle
turtle.color("purple")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

size = 100
  
def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)

triangle(100)
back(75)
triangle(50)
back(50)
triangle(25)

def square(size):
  for j in range(4):
    turtle.forward(size)
    turtle.left(90)

square(100)
back(125)
square(50)