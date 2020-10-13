import itertools as it
T=int(input("Enter tests:"))
for _ in range(T):
    N=int(input("no.of numbers:"))
    l=list(int(x) for x in input("Enter:").split(" "))
    s=int(input("sum:"))
    if (s in l) or s==0:
        print("YES")
        continue
    f=0
    for k in range(2,N):
        p=list(it.combinations(l,k))
        for i in range(len(l)):
            sum=0
            for j in range(k):
                sum+=p[i][j]
            if sum==s:
                f+=1
    if f>0:
        print("YES")
    else:
        print("NO")
