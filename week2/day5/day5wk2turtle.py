import turtle
turtle.shape("arrow")
turtle.color("orange")
turtle.speed(0)
turtle.pensize(5)

def back(bdist):
    turtle.penup()
    turtle.backward(bdist)
    turtle.pendown()


def square(sqlength):
    for i in range(4):
        turtle.forward(sqlength)
        turtle.left(90)

def rectangle_vertical(rectsidex):
    for k in range(2):
        turtle.forward(rectsidex)
        turtle.right(90)
        turtle.forward(rectsidex * 2)
        turtle.right(90)

def rectangle_horizontal(rectsidex):
    for k in range(2):
        turtle.forward(rectsidex * 2)
        turtle.right(90)
        turtle.forward(rectsidex)
        turtle.right(90)

def triangle(trilength):
    for j in range(3):
        turtle.forward(trilength)
        turtle.left(120)


#rectangle(200, 80)

def rocket_draw(rktsize):
    for l in range(1):

        turtle.color("blue")

        rectangle_vertical(rktsize)
        
        turtle.penup()
        turtle.backward(20)
        turtle.pendown()

        turtle.color("red")

        triangle(rktsize+40)
        
        turtle.penup()
        turtle.right(90)
        turtle.forward(rktsize*2)
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()

        turtle.color ("orange")

        turtle.right(135)
        turtle.forward(rktsize)
        turtle.left(145)
        turtle.forward(rktsize-20)
        turtle.right(135)
        turtle.forward(rktsize + 20)
        turtle.left(145)
        turtle.forward(rktsize + 20)
        turtle.right(40)
        turtle.forward(rktsize + 20)
        turtle.left(145)
        turtle.forward(rktsize + 20)
        turtle.right(135)
        turtle.forward(rktsize-20)
        turtle.left(145)
        turtle.forward(rktsize)
        turtle.left(45)

        turtle.penup()
        turtle.forward(12)
        turtle.pendown()

        square(rktsize-20)




rocket_draw(100)



'''square(100)
back(200)
turtle.color("green")
square(100)
back(200)


turtle.color("cyan")
square(100)
turtle.color("blue")
triangle(100)

back(200)
turtle.color("cyan")
square(100)
back(30)
turtle.color("blue")
triangle(160)'''

'''turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.penup()
turtle.backward(200)
turtle.pendown()

turtle.color("purple")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)'''

turtle.ht()
turtle.Screen().exitonclick()