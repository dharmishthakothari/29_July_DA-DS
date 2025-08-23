# find whether list contains another list or not
# to check list contains sublist or not
lst_name = ['Apple','Microsoft','HP',1,23.45]
for i in lst_name:
    if type(i) is list:
        print("List contains another list ")
        break
    