# JoC 7 Basics Week 3 PT1 Act3
# Count Lines
# by Anthony Rodriguez


def main():
    count_words_new_file = open("counts.txt", "w")
    file_list("files_list.txt")
    count_words_new_file.close()

    
def file_list(file_name):
    data_file = open(file_name, "r")
    data_read = data_file.readlines()
    for line in data_read:
        read_count(line.rstrip())


def read_count(file_name):
    #print()
    data_file = open(file_name, "r")
    data_read = data_file.readlines()
    line_count = 0
    count_file = open("counts.txt", "a")
    
    for line in data_read:
        if line != "":
            line_count += 1

    print(file_name, ":", line_count, file=count_file)
    
    count_file.close()
    data_file.close()




main()
