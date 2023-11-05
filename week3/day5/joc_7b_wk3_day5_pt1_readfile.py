#Joy of Coding 7 Basics Week3 Day 5 Pt 1 Read File
#by Anthony Rodriguez
#Reading a txt file and displaying it to screen

dataFile = open("add.txt")
for line in dataFile:
    print(line.rstrip())
dataFile.close