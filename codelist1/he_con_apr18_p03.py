n,m=[8,4]
a=[2,2,1,4,4,2,4,4]
h=[1,2,3,4]
def solve(st):
    f=[]
    for i in h:
        c=st.count(i)
        if c!=i and c!=0:
            return 0
    return 1

for _ in range(6):
    l=int(input("Enter l="))
    r=int(input("Enter r="))
    if l==r:
        if a[l-1] != 1:
            print(0)
        else:
            print(1)
    else:
        st=a[l-1:r]
        print(solve(st))
    
