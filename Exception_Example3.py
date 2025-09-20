import traceback
try:
    dict = {   1:"Banana",    2:"Apple",    3:"Orange"}
    print(dict[2])
    print(23/10)
    print(dict[4])
except ZeroDivisionError:
    print("Error ZeroDivisionError")
except:
    traceback.print_exc()
