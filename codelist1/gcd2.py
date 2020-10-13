def gcd(m,n):
    if(n==0):
        return m
    else:
        p=m%n
        return gcd(n,p)
x=gcd(14,21)
y=gcd(21,14)
print(x)
print(y)
