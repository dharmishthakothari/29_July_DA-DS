# list methods 

lst_names = ['Apple','Microsoft','Dell']
# add item at end
lst_names.append('Google')
print(lst_names)
# add item at index position
lst_names.insert(2,'HP')
print(lst_names)

# work with another list 
lst_tem=[2,3,4]
# lst_names.append(lst_tem)
# print(lst_names)
lst_names.extend(lst_tem)
print(lst_names)

# to clear list 
#lst_names.clear()
#print(lst_names)

lst_c_names=lst_names.copy()
print("This is new list ",lst_c_names)
print(lst_names.count('Dell'))
lst_tem = ['Google','Google','HP','Google']
print("Index of Google item ",lst_tem.index('Google',2))

# remove/pop item from list 
print("POP ",lst_names.pop())
print(lst_names)

#remove item from 2nd index
print("POP ",lst_names.pop(2))
print(lst_names)

lst_names.remove('Microsoft')
print("After remove ",lst_names)
