def gcd(m,n):
    if(m<n):
        m,n=n,m
    if((m%n)==0):
        return n
    else:
        df=m-n
        return gcd(n,df)
x=gcd(21,14)
print(x)
        
