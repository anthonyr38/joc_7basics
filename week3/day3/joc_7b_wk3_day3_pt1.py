#Joy of Coding 7 Basics Week 3 Day 3 Pt1
#by Anthony Rodriguez
#20 number average

import random

randomlist = []

def random_list():
    for num in range (0, 20):
        num = (random.randint(1,100))
        randomlist.append(num)
        list_avg = sum(randomlist) / len(randomlist)
    print(randomlist)
    print(list_avg)
        
def main():
    
    random_list()
    

main()