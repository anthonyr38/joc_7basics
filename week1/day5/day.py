#Joc 7b bc wk1 day5 activity: using functions
# by Anthony Rodriguez



# import math module
import math

# input prompts
prompt1 = "Please enter your favorite month: "
prompt2 = "Enter your favorite day of the month: "


# declare variables
fav_month = input(prompt1)
fav_day = input(prompt2)


# define main function
def main():
    print(fav_month.capitalize(), fav_day + ", 2020")
    print("Is the month alphanumeric? ", fav_month.isalnum())
    print("How many 2's ", count_twos(fav_day))
    print("Factorial: ", math.factorial((eval(fav_day))))
    print("Log base 2: ", math.log2((eval(fav_day))))


# define a function to count number of 2's
def count_twos(fav_day):
    count = 0               # declaring a variable to use as a counter
    for i in fav_day:       # loop to count number of 2's
        if i == "2":
            count += 1
    return count            # returns total count once done looping

# call main function   
main()

