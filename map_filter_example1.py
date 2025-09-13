# list of string which have vowel in string
def findString(city):
    for i in city:
        if i in "aeiouAEIOU":
            return city

lst_cities = ['rajkot','ahmedababd','surat','lynn']
lst_city_vowel=[]

lst_city_vowel=list(map(lambda city:any(ch in "aeiou" for ch in city ) ,lst_cities))
print(any(ch in "aeiou" for ch in lst_cities ))


# for i in lst_cities:
#     lst_city_vowel.append(findString(i))
print(lst_city_vowel)
