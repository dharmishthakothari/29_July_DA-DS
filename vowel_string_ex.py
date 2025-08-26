#find vowel from string

# name="Khushali"
# vowel="aeiou"
# for i in name:
#     if i in vowel:
#         print(i)

#find vowel and count from list elements 
lst_names=['khushali','juhi']
lst_name_countVowel=[]
count=0
for i in lst_names:
    count=0
    print(f"{i}")
    for char in i:
        if char in "aeiouAEIOU":
            count+=1
    lst_name_countVowel.append(count)
print(lst_name_countVowel)
