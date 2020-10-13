for _ in range(int(input("Enter no. of testcases:"))):
    n=int(input("Enter n="))
    k=int(input("Enter k="))
    arr=list(range(n))
    i=1
    print("----------------------------------------------------------\n------------------------------------------------")
    while len(arr)>1:
        print("initial length of array=",len(arr))
        print("initial array=",arr)
        print("k=",k)
        if k>0:
            print("Current but not popping=",i)
            k-=1
            i=(i+2)%len(arr)
        else:
            print("Current popping=",i)
            p=i
            i=(i+2)%len(arr)
            if i not in arr:
                arr.pop(i)
            else:
                arr.remove(p)
        print("next poping=",i)
        print("updated length of array=",len(arr))
        print("updated array=",arr)
        print("-----------------------------------------------------------")
    print(arr[0]+1)
