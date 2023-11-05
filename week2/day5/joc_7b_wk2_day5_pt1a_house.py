#JoC 7 Basics Week 2 Day 5 Pt 1A
# by Anthony Rodriguez



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
        turtle.right(90)



def triangle(trilength):
    for j in range(3):
        turtle.forward(trilength)
        turtle.left(120)




def house_draw(housesize):
    for l in range(1):

        turtle.color("blue")

        square(housesize)
        
        turtle.penup()
        turtle.backward(20)
        turtle.pendown()

        turtle.color("red")

        triangle(housesize+40)
        
        


house_draw(100)
back(300)
house_draw(200)       





turtle.ht()
turtle.Screen().exitonclick()