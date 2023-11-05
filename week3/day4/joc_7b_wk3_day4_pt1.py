#Joy of Coding 7 Basics Week 3 Day 4 Pt 1 Writing While Loops
#by Anthony Rodriguez

def to_five():
    num = 1
    while num < 6:
        print(num)
        num += 1

def plus_3():
    num = 2
    while num < 12:
        print(num)
        num += 3

def neg_evens():
    num = -10
    while num < 1:
        print(num, end = '')
        num -= -2

def four_star():
    stars = "****"
    i = 1
    while i < 5:
        print(stars)
        i += 1

def comp_sci_150():
    i = 0
    j = "CSCI 150"
    while i < len(j):
        print(j[i])
        i += 1

def number_list():
    num_list = []
    num_enter = 1
    while num_enter != 0:
        num_enter = eval(input("Please enter a number to add to a list, use 0 to finish generating list: "))
        num_list.append(num_enter)
    del num_list[-1]
    number_sum = sum(num_list)
    number_avg = number_sum / len(num_list)
    print("Your list of numbers: ", (sorted(num_list)), "The sum of your list of numbers: ", number_sum, "The average of your list: ", number_avg)
    








def main():
    to_five()
    
    print("~" * 10)
    
    neg_evens()
    
    print("~" * 10)
    
    plus_3()
    
    print("~" * 10)
    
    four_star()
    
    print("~" * 10)

    comp_sci_150()

    print("~" * 10)

    number_list()


main()
