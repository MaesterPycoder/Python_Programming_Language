arr=[1,2,3,4]
n=4
k=2
i=1
l=n
while l>1:
    i%=l
    if k>0:
        k-=1
        i+=2
    else:
        arr.pop(i)
        i=i+2
        l-=1

print(arr[0]+)
