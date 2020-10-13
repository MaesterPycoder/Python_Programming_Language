for _ in range(3):
    n,p,k=list(int(x) for x in input("Enter:").split(" "))
    print("n=",n)
    print("p=",p)
    print("k=",k)
    arr=list(range(0,n))
    print(arr)
    i=0
    c=k
    lst=[]
    lst.append(i)
    while c>0:
        i=(i+p)%n
        lst.append(i)
        if arr[i]==0:
            lst.append(i)
            break
        c-=1
    print(lst[k-1])
