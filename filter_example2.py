def findLenght(s):
    if len(s)>5:
        return s

lst_cities = ['rajkot','ahmedababd','surat']
lst_len=list(filter(findLenght,lst_cities))
print(lst_len)
#lst_upper = list(map(str.upper,lst_len))
lst_upper = list(map(str.upper,list(filter(findLenght,lst_cities))))
print(lst_upper)