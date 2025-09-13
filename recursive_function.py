def fact(n):
    #base
    if n==0:
        return 1
    # recusive
    else:
        return n * fact(n-1)
def sumNumbers(num):
    if num==0:
        return 0
    else:
        return num + sumNumbers(num-1)
print(fact(5))
print(sumNumbers(10))