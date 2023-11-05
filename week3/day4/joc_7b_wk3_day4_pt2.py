#Joy of Coding 7 Basics Week 3 Day 4 Pt2 Strings Lists and Whiles
#by Anthony Rodriguez

'''def average_neg_evens(num_list):
    neg_evens_list = []
    for i in num_list:
        if i < 0 and i % 2 == 0:
            neg_evens_list.append(i)
    neg_evens_avg = sum(neg_evens_list) / len(neg_evens_list)
    return neg_evens_avg'''

'''def count_letter(string_list, string_letter):
    letter_count = 0
    for string in string_list:
        upperlist = string.upper()
        for letter in string_letter.upper():
            letter_count += upperlist.count(letter)
    return letter_count'''
   
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