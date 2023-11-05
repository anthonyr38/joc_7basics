# Create a file with numbers.
# by Anthony Rodriguez.

numPrompt = "Please enter a number greater than 0, use zero to end your list: "

num_file_name = input("Please provide filename with extension: ") 
# requests user to input a string that will be used as data for implemented variable.



num_file = open(num_file_name, "w")
# creates a new file, in write mode, which will erase or replace existing file and its data.
# using the file name provided by num_file_name.


numInput = 1


while numInput != 0:
    numInput = eval(input(numPrompt))
    if numInput != 0:
        print(numInput, file=num_file)


print()
print("Output file", num_file_name, "created with the following contents: ")


num_file.close()

num_read = open(num_file_name, "r")

fileContent = num_read.read()

print(fileContent)

num_read.close()









          