for _ in range(int(input("Enter no.of testcases="))):
    n=int(input("Enter no. of elements="))
    k=int(input("Enter k="))           
    arr=list(range(n))
    l=len(arr)
    i=1
    while True:
        if k>0:
            k-=1
            i=(i+2)%len(arr)
        else:
            k=i
            if len(arr)==2:
                i=i%len(arr)
                arr.pop(i)
                print(arr[0]+1)
                break
            i=(i+2)%len(arr)
            arr.pop(k)
