lst1=[1,1.23,56,'hello',2.7890]
print(lst1)
for i in lst1:
    print(i)
# multiple all elements of list
lst2=[1,4,5,7,'hello',8,10]
mul=1
for i in lst2:
    if type(i)==int:
        mul=mul*i
print(f"Summation list elements are {mul}")