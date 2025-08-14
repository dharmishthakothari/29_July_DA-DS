import random
for i in range(5):
    a=random.randint(1,100)
    print(a)
print("With while ")
i=1
while True:
    if i==10:
        break
    a=random.randint(1,100)
    print(a)
    i+=1
    