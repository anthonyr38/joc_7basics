'''def well(x):
    t = -3
    while t < x:
        if t < 0:
            t += x
        else:
            t *= 2
    return t
print(well(5))
    

list = ["madison", "NJ", "Rose City", "Dodgers"]

print(list[:2])

print("NJ" in list)

song = "Happy Birthday!"
print(song[-4:])'''

'''
prompt = "Enter a number ('Q' to quit)?"
user = 0
count = 0
while user != "Q":
    user = input(prompt)
    count += user.count("0")
print("you entered", count, "zeroes")'''

'''
list = ["Zebra", "lightsaber", "1234 JOYS!"]

def count_fricataves(list):
    frics = "fsvz"
    count = 0
    for string in list:
        for let in frics.upper():
            count += string.upper().count(let)
    return count

print(count_fricataves(list))'''

'''
string = "hello"
string[2] = "y"'''

user = input("Enter a phrase: ")

def count_u(user):
    target = "u"
    count = 0
    for l in user:
        for c in target.upper():
            count += l.upper().count(c)
    if count >= 1:    
        return count
    else:
        return -1   
        

print(count_u(user))

list = ["Zebra", "lightsaber", "1234 JOYS!"]

def avg_vowels(list):
    vowels = "aeiou"
    count = 0
    lcount = 0
    for string in list:
        for let in vowels.upper():
            count += string.upper().count(let)
        for letr in list:
            lcount += list.count(letr)
    return round(lcount / count)

print(avg_vowels(list))


def why11(list):
    y=1
    j=0
    while j < len(list) and y < 11:
        x = list[j]
        if x < 0:
            y -= x
        elif x % 2 == 0:
            y *= x
        else:
            y += x
        j += 2
    return y

print(why11([4, -1, -5, 2, 1, 3, 7, -8]))