def absdif(num1, num2):
    diff = abs(num1 - num2)
    return diff    

def main():
    print("difference 5 10", absdif(5, 10) == 5)
    print("difference 10 5", absdif(10, 5) == 5)
    print("diference 200 -200", absdif(200, -200) == 400)

main()