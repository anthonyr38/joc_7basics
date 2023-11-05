# What does this program output?

my_list = ["one", "two", "three", "four", "five"]

print(my_list[0])
print(my_list[-1])
print(my_list[2:4])

for num in my_list:
    if num.count("o") > 0:
        print(num)

phrase = "Green Eggs & Ham"
print("green" in phrase)
print("Green" in phrase)
print("two" in my_list)

phrase = "Monty Python"
for letter in phrase:
    print(letter, end="-")
print()

# Assume the user enters the following numbers:
# 5 10 15 20 25
numbers = []
for i in range(5):
    numbers.append(eval(input("Please enter a number: ")))
print(sum(numbers))
