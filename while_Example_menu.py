# Use match case 

while True:
    number1 = int(input("Enter number 1 "))
    number2 = int(input("Enter number 2 "))

    print("1. Addition ")
    print("2. Substraction ")
    print("3. exit ")
    choice = int(input("Enter choice "))
    match choice:
        case 1:print(number1+number2) 
        case 2:print(number1-number2) 
        case 3:break
        case _:print(" Invalid choice ")
