#Joy of Coding 7 Basics Week 3 Day 3 Pt2 Mangle
#by Anthony Rodriguez

def mangle(string1):
    upstring = string1.upper()
    stringlist = list(upstring)
    del stringlist[2]
    del stringlist[-3]
    string2 = ''.join(stringlist)
    return string2



def main():
    print(mangle("hellothere"))
    print(mangle("hellothere") == "HELOTHRE")

    print(mangle("42 degees Celsius"))
    print(mangle("42 degees Celsius") == "42DEGEES CELSUS")

    print(mangle("eeeeeee"))
    print(mangle("eeeeeee") == "EEEEE")


main()