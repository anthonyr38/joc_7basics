#writing function exercises part 2 (week3 day 2)
#by Anthony Rodriguez

def is_even(num):
    if (num == 0):
        print("Number is zero")
        return num == 0
    elif((num % 2) == 0):
        print("number is even")
        return num % 2 == 0
    else:
        print("Number is odd")
        return num % 2 == 0


def calculate_total(meal, tax_rate, tip_rate):
    tip = (meal * tip_rate)
    tax_amt = (meal * tax_rate)
    total_cost = (meal + tax_amt + tip)
    print ("Restaurant Receipt")
    print()
    print("Meal: $", meal)
    print()
    print("Tax: $", tax_amt)
    print()
    print("Tip: $", tip)
    print()
    print("Total: $", total_cost)


def hey(inta):
    return (inta * inta)


def there(n):
    if (n < 0):
        return 0
    # else: #optional
    return (2 ** n)

#    if (n > 0):
#        return (2 ** n)
    # else: #optional
#    return 0

def are_we(num, string1):
        print("Are we %s yet? " %(string1) * num)




def main():
    is_even(6)
    print(is_even(6))
    is_even(21)
    print(is_even(21))
    is_even(0)
    print(is_even(0))

    print("-" * 10)

    calculate_total(53.48, .07, .18)
    calculate_total(40.00, .05, .20)

    print("-" * 10)

    print(hey(5) == 25)
    print(hey(0) == 0)
    print(hey(-3) == 9)

    print("-" * 10)

    print(there(5) == 32)
    print(there(0) == 1)
    print(there(3) == 8)
    print(there(-2) == 0)
    print(there(-6) == 0)

    print("-" * 10)

    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey!")


main()