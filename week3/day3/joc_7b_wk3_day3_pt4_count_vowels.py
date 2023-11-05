#Joy of Coding 7 Basics Week 3 Day 3 Pt4 Count Vowels
#by Anthony Rodriguez




#def count_e(string_list):
#    to_list1 = list(''.join(string_list))
#    count_the_eE = to_list1.count('e') + to_list1.count('E')
#    return count_the_eE'''


#def count_vowels(string_list1):
#    
#    to_list2 = list(''.join(string_list1))
#    count_the_a = to_list2.count('a') + to_list2.count('A')
#    count_the_e = to_list2.count('e') + to_list2.count('E')
#    count_the_i = to_list2.count('i') + to_list2.count('I')
#    count_the_o = to_list2.count('o') + to_list2.count('O')
#    count_the_u = to_list2.count('u') + to_list2.count('U') 
#    count_the_vwls = count_the_a + count_the_e + count_the_i + count_the_o + count_the_u
#    return count_the_vwls

def count_e(list):
    num_e = 0
    for string in list:
        num_e += string.upper().count("E")

    return num_e

def count_vowels(list):
    num_vwls = 0
    for string in list:
        upperlist = string.upper()
        for vowel in "AEIOU":
            num_vwls += upperlist.count(vowel)
    return num_vwls



print(count_e(["hi", "hello", "EEK!", "crab", "cake"]))

print(count_vowels(["hi", "hello", "EEK!", "Alphabet", "Unicorn", "Outside", "Inside"]))
   