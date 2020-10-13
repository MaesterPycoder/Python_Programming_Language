def B_checker(s,n):
    count=0
    for i in range(n-1,0,-1):
        if s[i]!="B":
            break
        else:
            count+=1
    print("last B's=",count)
    return count
def maker(s):
    lst=list(s)
    lst.sort()
    st="".join(lst)
    return st
def check(s,N):
    count=0
    p=0
    if s==maker(s):
        return count
    st=maker(s)
    for i in range(N):
        if s[i] != st[i]:
            p+=1
    print("p=",p)
    ca=s.count("A")
    cb=s.count("B")
    k=B_checker(s,N)
    if min(ca,cb)>p:
        count=p
    else:
        count=min(ca,cb)
    return count-k

if __name__=='__main__':
    lst=["AAABAAABBBABBB"]
    N=len(lst[0])
    for i in range(len(lst)):
        s=lst[i]
        ans=check(s,N)
        print(ans)
