n=int(input("Enter a number (>0):"))
k=n
r=0
while(n>0):
    r=r*10+n%10
    n=n//10
print("Reversed number of %d is:%d"%(k,r))
