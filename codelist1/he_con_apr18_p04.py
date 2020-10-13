def last_ver(arr,k,n):
    i=-1
    k+=1
    while len(arr)>1:
        i=(i+2)%len(arr)
        print("At vertex=",i+1)
        if k>0:
            k-=1
        elif k<=0:
            arr.pop(i)
        print("k=",k)
        print("array=",arr)
    return arr[0]  






if __name__=='__main__':
    for _ in range(1):
        n,k=list(int(x) for x in input("Enter=").split(" "))
        arr=list(range(1,n+1))
        ans=last_ver(arr,k,n)
        print(ans)
