from functools import reduce
def add(no1,no2):
    return no1+no2
lst_numbers = [1,2,3,4,5]
ans=reduce(add,lst_numbers)
print(ans)