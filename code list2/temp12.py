from time import time
init=time()
for _ in range(int(input("Enter no. of testcases:"))):
    N=int(input("Enter n="))
    k=int(input("Enter k="))
    lst=[]
    l=N
    i=1
    while len(lst)<N:
        if k>0:
            k-=1
        else:
            if i not in lst:
                lst.append(i)
            else:
                while(True):
                    i+=1
                    if i not in lst:
                        break
                lst.append(i)
        i=(i+2)%N
    print(i+2)
print("This code taken=",time()-init)
        
        
        
