def last_ver(arr,k,n):
    for i in range(0,n,2):
        if k>0 and len(arr)>1:
            k=-1
        elif k<=0 and len(arr)>1:
            arr.pop(i)
        if len(arr)==1:
            return arr[0]
        i=i%n
if __name__=='__main__':
    for _ in range(4):
        n,k=list(int(x) for x in input().split(" "))
        arr=list(range(1,n+1))
        ans=last_ver(arr,k,n)
        print(ans)
