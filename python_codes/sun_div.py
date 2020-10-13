import time
init=time.time()
def great_factor(n,k):
    while n%k==0:
        n=n//k
    return n
for _ in range(1):
    n,k =100,11
    s=0
    a=(n*(n+1))//2
    print("a-",a)
    l=n//k
    print("l=",l)
    b=k*((l*(l+1))//2)
    print("b=",b)
    nsum=a-b
    print("nsum=",nsum)
    for m in range(1,l+1):
        s+=great_factor(m,k)
    print(s+nsum)
print("Time taken=",time.time()-init)