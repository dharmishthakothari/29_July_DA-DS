# Use match case 
number1=int(input("Enter number 1 "))
number2=int(input("Enter number 2 "))

print("1. Addition ")
print("2. Subtraction ")
choice = int(input(" Enter your choice "))
match choice:
    case 1 : print(number1+number2)
    case 2 : print(number1-number2)
    case _ :print("Invalid choice ")

