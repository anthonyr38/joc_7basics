# Joc 7b wk1 day5 mad program
# by Anthony Rodriguez

# input prompt
prompt = "Enter a phrase: "

# declare variable
phrase = input(prompt)



def main():
    print(phrase.upper())
    print(confused(phrase))
    print("The maddest: ", phrase.isprintable())


#define a function to replace the e's with x's and returns the new string
def confused(phrase): 
    e_E = "e"
    new_char = "x"
    c_phrase = phrase.lower().replace(e_E, new_char) 
    return c_phrase

    
main()