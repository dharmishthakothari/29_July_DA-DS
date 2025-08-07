# To check multiple conditions we have to use elif
name=input("Enter your name ")
age = int(input("Enter age "))
if age>0 and age<=2:
    print(f"{name} is infant ")
elif age>3 and age<18:
    print(f"{name} is minor ")
elif age>=18 and age<50:
    print(f"{name} is Adult")
else :
    print(f"{name} is senior" )
