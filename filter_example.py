def findEven(num):
    if num%2==0:
        return num

lst_numbers = [12,33,56,71,80]
lst_num_even = []
# for i in lst_numbers:
#     #print(findEven(i))
#     lst_num_even.append(findEven(i))
lst_num_even = list(filter(findEven,lst_numbers))
print(lst_num_even)