# JoC 7 Basics Week 3 PT1 Act3
# Count Lines
# by Anthony Rodriguez

def main():
    count_words_new_file = open("count_words.txt", "w")
    file_list("files_list.txt")
    count_words_new_file.close()


def file_list(file_name):
    data_file = open(file_name, "r")
    data_read = data_file.readlines()

    w_c_list = []
    l_c_list = []

    for line in data_read:
        #word_count(line.rstrip())
        w_c_list.append(word_count(line.rstrip()))
        #read_count(line.rstrip())
        l_c_list.append(read_count(line.rstrip()))

    count_words_new_file = open("count_words.txt", "a")
    print("TOTAL: ", sum(l_c_list),  "lines, ", sum(w_c_list), "words", file=count_words_new_file )
    count_words_new_file.close()

    
def word_count(file_name):
    data_file = open(file_name, "rt")
    w_count = data_file.read()
    count_w = w_count.split()
    words_c = len(count_w)
    data_file.close()
    return words_c



def read_count(file_name):
    data_file = open(file_name, "rt")
    data_read = data_file.readlines()

    count_words_file = open("count_words.txt", "a")
    line_count = 0

    for line in data_read:

        if line != "":
            line_count += 1


    word_count(file_name)

    print(file_name, ":", line_count, "lines", word_count(file_name), "words", file=count_words_file)

    return line_count


main()
