# csv to dictionary
# by Anthony Rodriguez

import statistics #module for some math operations

#data variables
spring = []
fall = []

# definitions of functions
def stat_output(list):
    print("Mean:   ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD:    ", statistics.stdev(list))
    print()

def term_sort(csv_filename): #read in the file
    csv_file = open(csv_filename)
    for line in csv_file: #for every line in the file
        student_list = line.rstrip().split(",")#remove new line and use comma to split the values
        if student_list[1] == "Spring 2016":
            spring.append(eval(student_list[2]))#adds to spring list
        else:
            fall.append(eval(student_list[2]))#adds to fall list
    csv_file.close()

def main():
    term_sort("sample_grades.csv")
    print()
    print("Fall 2016:")
    stat_output(fall)

    print("Spring 2016: ")
    stat_output(spring)

main()