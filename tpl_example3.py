tpl_numbers = (1,2,3,4)
# for i in tpl_numbers:
#     print(i)

tpl_new_numbers=(i for i in tpl_numbers)

print(tuple(tpl_new_numbers))