# list slicing
lst=['123','345','567']
lst1=lst[:1]
print(lst1)
lst1=lst[1:3]
print(lst1)
lst[1]='hello'
print(lst)

del lst[2]
print(lst)
del lst
#print(lst)