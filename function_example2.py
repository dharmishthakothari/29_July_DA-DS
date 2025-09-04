def isPositive(number):
    if number>0:
        #print("Positive")
        return "Positive"
    else:
        #print("Negative")
        return "Negative"
def isEvenOdd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
ans=isPositive(23)
if ans=="Positive":
    ans1=isEvenOdd(23)
    print(ans1)