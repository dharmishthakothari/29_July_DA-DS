dict1={1:"test@gmail.com",
       2:"pouuy@gmail.com",
       3:"szcxv@gmail.com",
        56:"testuser@gmail.com" }
print(dict1)
#dict1.clear()
#print(dict1)
dic2=dict1.copy()
print(dic2)
print(dict1.get('1'))
print(dict1[1])
dict1.setdefault(56,"user@gmail.com")
print(dict1)
