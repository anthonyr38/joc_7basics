import turtle
turtle.color("purple")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

size = 100
  
#def triangle(size):
#  for i in range(3):
#    turtle.forward(size)
#    turtle.left(120)

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

def move(len):
  back(-1 * len)

def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)

spiral(75, 45)
move(150)
turtle.color("teal")
spiral(100, 90)


#for n in range(3, 10):
#  move(50)
#  polygon(n, 100 / n)
#  back(50)
#  turtle.right(360 / 7)


#triangle(100)
#back(75)
#triangle(50)
#back(50)
#triangle(25)

#def square(size):
#  for j in range(4):
#    turtle.forward(size)
#    turtle.left(90)

#square(100)
#back(125)
#square(50)

#polygon(3, 100)
#back(125)
#polygon(4, 50)

#if (num < 3):
#  print("not enough sides")