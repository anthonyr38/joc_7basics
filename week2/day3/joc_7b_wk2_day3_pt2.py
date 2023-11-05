#JoC 7 Basics Week 2 Day 3 Pt 2
# by Anthony Rodriguez


for i in range(10, 26, 5):
    print(i, end = " ")
print()

for j in range(-3, 21, 3):
    print(j, end = ", ")
print(j + 3)


s = 0

for k in range(10):
    num = float (input ("Please enter a number: "))
    
    s += num
print("Average: ", s / 10)