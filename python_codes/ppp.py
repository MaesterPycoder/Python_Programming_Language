T=int(input("Enter T:"))
for p in range(T):
    N=int(input("Enter size:"))
    A=list(int(x) for x in input("Enter:").split(" "))
    s=max(A)
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            p=(A[i] and A[j])^(A[i] or A[j])
            if p<s:
                s=p
    print("Answer=",s)
