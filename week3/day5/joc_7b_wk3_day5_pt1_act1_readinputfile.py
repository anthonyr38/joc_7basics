#Joy of Coding 7 Basics Week3 Day 5 Pt 1 Read File
#Reading a txt file and displaying it to screen
#by Anthony Rodriguez

dataFile = open("input_file.txt")
for line in dataFile:
    print("-", line.rstrip())
dataFile.close