for _ in range(1):
    count=0
    n=6
    lst=[1,2,3,6,5,4]
    for i in range(n-1):
        if lst[i]>lst[i+1]:
            count+=1
            while lst[i]>=lst[i+1]:
                lst[i+1]+=1
        elif lst[i]==lst[i+1]:
            lst[i+1]+=1
            count+=1
    print(count)
            
