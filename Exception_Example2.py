import traceback
try:
    no=int(input("Enter number "))
    print(no)
    print(no/0)
    print("END TRY")
except ValueError:
    print("Entered value is incorrect")
except ZeroDivisionError:
    print("No number can not divide by zero ")
    traceback.print_exc()
