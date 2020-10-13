def summ(lst):
    s=0
    for i in range(n):
        s+=int(lst[i])
    return s
n,m,k=list(int(x) for x in input().split(" "))
lst=list()
lt=list()
for _ in range(n):
    lst.append(input())
lst.sort()
for i in range(n):
    lt.append("0b"+lst[i])
s=summ(lt)
    
while k>0:
    for i in range(n-1,-1,-1):
        st=lst[i]
        if st[-1]!="1":
            lst[i]=int("0b"+lst[i],2)^0b111
            k-=1
