#Joy of Coding 7 Basics Week 3 Day 5 Pt2
# by Anthony Rodriguez
# Writes content from a user to a file


PROMPT = "Enter the next line in the file: "

outfilename = input("What is the name of your output file? ")
numLines = eval(input("how many lines do you want to write? "))

#create a new file object in write mode
datafile = open(outfilename, "w") # a to append

for x in range(numLines):
    userinput = input(PROMPT)# write the users input to the file
    print(userinput, file=datafile)

#close the file with the method close
datafile.close()
    