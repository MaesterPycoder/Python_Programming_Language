for _ in range(4):
    N=int(input("Enter no.of elements="))
    k=int(input("Enter num k="))
    arr=list(range(1,N+1))
    if N%2 !=0:
        i=0
    else:
        i=-1
    while len(arr)>0:
        if len(arr)>2:
            i=(i+2)%(len(arr))
        if len(arr)==1:
            print(arr[0])
            break
        if k>0:
            k-=1
        else:
            arr.pop(i)
    print("-------------------------------------------------------------------------------------------")
