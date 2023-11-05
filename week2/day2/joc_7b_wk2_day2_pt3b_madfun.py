# JoC 7 Basics Week 2 Day 2 Part 3B
# by Anthony Rodriguez

import math


num = eval(input("please enter a decimal number: "))




print("you entered", num)
print("The absolute value of your number is: ", abs(num))
print("The rounded value of your number is: ", round(num, 0))
print("The square root of the rounded numbers absolute value is: ", math.sqrt(round(abs(num))))
