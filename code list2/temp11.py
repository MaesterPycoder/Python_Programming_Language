n,m=[8,4]
a=[2,2,1,4,4,2,4,4]
h=[1,2,3,4]
for _ in range(6):
    l=int(input("Enter l="))
    r=int(input("Enter r="))
    st=a[l-1:r-1]
    f=0
    for i in h:
        c=a.count(i)
        if c==0:
            continue
        if c>0 and c==i:
            f+=1
        else:
            print(0)
            break
    if f>0:
        print(1)


