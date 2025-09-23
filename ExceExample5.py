class AgeInvalidException(Exception):
    pass
try:
    age=int(input("Enter Age "))
    if age<=18:
        raise AgeInvalidException(f"{age} is not valid ,Please enter valid age")
except AgeInvalidException as e:
    #print("Enter Valid Age ")
    print(e)
#PasswordIncorrect --> check length should be more then 8 letters and one letter must be digit
