#Joc Mod1 7b wk2 day5_10 cake_py
# by Anthony Rodriguez

import turtle

turtle.color("orange")

def rectangle(width):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(width / 6)
        turtle.right(90)

def triangle(width):
    for i in range(3):
        turtle.forward(width / 3)
        turtle.left(120)
    

def next_layer(width):# positions pen for next cake layer
    turtle.penup()
    turtle.left(90)
    turtle.forward(width / 6)
    turtle.right(90)
    turtle.pendown()

def cake(width):
    rectangle(width)
    next_layer(width)
    rectangle(width)
    next_layer(width)
    rectangle(width)
    candle(width)
    
def candle(width): #positions pen for drawing of candle
    turtle.penup()
    turtle.forward(width / 2 - width / 6)
    turtle.pendown()
    triangle(width)

def move_pen(width):
    turtle.penup()
    turtle.backward(width + 50)
    turtle.pendown()

width = 200
cake(width)
move_pen(width)
turtle.color("green")
cake(width - 50)

turtle.exitonclick()