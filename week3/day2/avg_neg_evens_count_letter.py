#Joy of Coding 7b wk3 day2
#by Anthony Rodriguez


   
def average_neg_evens(num_list):
    num_sum = 0
    count = 0
    i = 0 #loop index variable
    while i < len(num_list):#loop condition
        neg_evens_list = num_list[i]#index of value in list
        if neg_evens_list < 0 and neg_evens_list % 2 == 0:
            num_sum += neg_evens_list
            count += 1
        i += 1
    return num_sum / count

def count_letter(string_list, string_letter):
    letter_count = 0
    string_letter = string_letter.upper()
    
    #for string in string_list:
    i = 0 #loop variable
    while i < len(string_list): #loop condition
        upperlist = string_list[i]
        letter_count += upperlist.upper().count(string_letter)
        i += 1
    return letter_count


def main():
    print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
    print((average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])) == -3)

    print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4, -6, -9]))
    print((average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4, -6, -9])) == -4)
                       
    list1 = ["HELLO", "goodbye", "1234 Oooh!"]
         
    print(count_letter(list1, "O"))

    print((count_letter(list1, "O")) == 6)
                   
main()