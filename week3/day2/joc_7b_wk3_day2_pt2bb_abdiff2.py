#JoC 7 Basics Week 3 Day 2 Pt 2BB
# by Anthony Rodriguez

def abdiff(inta, intb):
    if(( inta < 0 ) and (intb < 0) and (inta < intb)):
        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(inta)) - (abs(intb))))
    elif(( inta < 0 ) and (intb < 0) and (inta > intb)):
        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(intb)) - (abs(inta))))
    elif((inta < 0) and (intb > 0)):
        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(inta)) + (abs(intb))))
    elif((inta > 0) and (intb < 0)):
        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(inta)) + (abs(intb))))
    elif((inta > 0) and (intb > 0) and (inta < intb)):
        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(intb)) - (abs(inta))))
    else:
        print("The absolute diference of ", inta, "and ", intb, "is: ", ((abs(inta)) - (abs(intb))))
    


abdiff(-24, -17)
abdiff(-100, 100)
abdiff(4, 8)
abdiff(92, 45)
abdiff(-44, -65)    