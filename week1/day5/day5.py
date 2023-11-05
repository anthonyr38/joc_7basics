 

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

def polygon(sides, polyLength):
  if (sides < 3):
    print("Not a polygon.")
  if (sides > 3):
    for i in range(sides):
      turtle.forward(polyLength)
      turtle.left(360 / sides)

#polygon(2, 100)
      

#triangle(150)
#back(150)
#triangle(100)
#back(100)
#triangle(50)

#turtle.color("cyan")

#square(50)
#forward(100)
#square(100)
#forward(150)
#square(150)


#input("Hit Enter")

def move(dist):
  back(-1 * dist)


#for n in range(3, 10):
#  move(50)
#  polygon(n, 100 )
#  back(50)
#  turtle.right(360 / 7)

def spiral(length, angle):
  for s in range(length, 5, -5):
    turtle.forward(s)
    turtle.right(angle)

spiral(75, 45)
move(200)
spiral(200, 80)




input("Hit Enter")