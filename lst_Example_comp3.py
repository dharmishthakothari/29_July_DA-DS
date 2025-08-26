# convert into upper if length is more 5 letter
lst_names=['dharmishtha','juhi','utsav','Shreyansh'] 
#lst_upper_names=[i.upper() for i in lst_names]
#print(lst_upper_names)

# for i in lst_names:
#     if len(i)>5:
#         print(i.upper())

lst_upper_by_len=[i.upper() for i in lst_names if len(i)>5]   
print(lst_upper_by_len)

