def fibo(a,b,n):
    n-=1
    if(n==0):
        return None
    else:
        print(a)
        c=a
        a=a+b
        return fibo(a,c)
re=fibo(0,1,3)
print(re)
