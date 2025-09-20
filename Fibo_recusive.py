def fibo(n):
    # 0 1 1 2 3 5
    if n==0:
        return 0
    if n==1:
        return 1        
    return fibo(n-1)+fibo(n-2)
for i in range(15):
    print(fibo(i))