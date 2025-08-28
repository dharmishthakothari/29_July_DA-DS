tpl_numbers = (1,2,3,4)
for i in tpl_numbers:
    print(i)
tpl_numbers1=1,2,3,4
print(type(tpl_numbers1))
tpl_numbers2=(1,)
print(type(tpl_numbers2))

# convert 
lst=list(tpl_numbers1)
tpl_1=tuple(lst)