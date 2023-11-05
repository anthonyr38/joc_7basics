#JoC 7 Basics Week 3 Day 2 Pt 2B
# by Anthony Rodriguez

#def abdiff(inta, intb):
#    if((abs(inta))<(abs(intb))):
#        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(intb))-(abs(inta))))
#    else:
#        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(inta))-(abs(intb))))'''

def absdif(num1, num2):
    diff = abs(num1 - num2)
    return diff    

def main():
    print("difference 5 10", absdif(5, 10) == 5)
    print("difference 10 5", absdif(10, 5) == 5)
    print("diference 200 -200", absdif(200, -200) == 400)

main()
    

#print(absdif(-24, -17))
#print(absdif(-100, 100))
#print(absdif(4, 8))
#print(absdif(92, 45))
#print(absdif(-44, -65))      