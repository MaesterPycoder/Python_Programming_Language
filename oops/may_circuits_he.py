def great_factor(n,k):
    while n%k==0:
        n=n//k
    return n
for _ in range(1):
    n,k =100,11
    s=0
    a=(n*(n+1))//2
    l=n//k
    b=((l*(l+1))//2)
    if l<k:
        print(a-b*k+l)
    
    # for m in range(1,l+1):
    #     s+=great_factor(m,k)
    # print(a+s-(b*k))