def len_chec(n):
    l=16-len(n)
    lst=['0']*l
    nlst="".join(lst)+n
    return nlst
def rotate(st,m,c):
    if c=='L':
        st=st[m:]+st[:m]
        return st
    else:
        st=st[-m:]+st[:-m]
        return st
for _ in range(2):
    N,m,c=list(x for x in input("Enter:").split(" "))
    X=bin(int(N)).replace('0b',"")
    y=len_chec(X)
    ans=rotate(y,int(m),c)
    print(int(ans,2))
