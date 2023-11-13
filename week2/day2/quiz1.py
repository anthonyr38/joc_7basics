'''for i in range(-3, 4, 2):
    print(i, end=":")
print()

for z in range(5):
    print(5, end="")
print()

phrase = "hello"
for x in phrase:
    print(x, end="--")
print("END")
print()

phrase = "hope"
for c in phrase:
    print(c*4, end = " ")
print()

string = "Last Jedi"
x = 0
for s in string:
    print(x, s, end=" ")
    x += 1
print()

for r in range(45, -45, -25):
    print(r, end = "|")
print()

for q in range(34, 5):
    print(q)
print()

phrase = "OOMPAH!"
for i in phrase:
    print(i)

num = 0
for i in range(5): 
    if num == 0:
        print(num, end = " ")
        num += 1
    if num >= 1 and num <= 256:
        print(num, end = " ")
        num = num * 4 

print()



def hyphen(phrase):
    return "--".join(phrase) + "!"
    
print(hyphen("HALLELUJAH"))

sum = 0
for num in range(-400, 401):
    if num % 2 == 0:
        sum = sum + num
    print("sum = ", sum)'''

'''s = 0

for k in range(5):
    num = float (input ("Please enter a number: "))
    s += num

print("Current average: ", s / 5)'''
'''
saying = "howdy"
for u in saying.upper():
    print(saying.upper(), end="!! ")

t = 20
for v in range(2, 12, 2):
    t += v
print(t) 

print()'''

# exercise 1
for i in range(5, 26, 5):
    print(i)


#exercise 2

for j in range(5, 9):
    print(j, end="...") 
print(" who do we apreciate?")

#exercise 3
phrase = "goodbye"
print("-".join(phrase.upper())+"!")


#exercise 4
for k in range(3):
    k = input("Please enter a team name: ")
    print("Go... ", k.upper())

#exercise 5

num_sq_sum = 0

for num in range(5):
    num_input = eval(input("Please enter a number: "))
    num_sq = num_input ** 2
    num_sq_sum += num_sq

print("Average of the squares: ", num_sq_sum / 5)