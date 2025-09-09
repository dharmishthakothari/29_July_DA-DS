def square(num):
    return num*num
lst_numbers=[1,6,45,87]
lst_sq_numbers=[]
# for i in lst_numbers:
#     lst_sq_numbers.append(square(i))

lst_sq_numbers=list(map(square,lst_numbers))
print(lst_sq_numbers)

lst_upper=list(map(str.upper,['ronak','monak']))
print(lst_upper)
