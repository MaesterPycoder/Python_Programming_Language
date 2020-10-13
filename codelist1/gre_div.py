import math as m
import time
init=time.time()
def ispower(y,x):
    res1=m.log(y)//m.log(x)
    res2=m.log(y)/m.log(x)
    return res1==res2
for  _ in range(1):
    n,k=10000000,97
    psum=0
    for i in range(1,n+1):
        if i//k==0:
            psum+=i
        elif ispower(i,k):
            psum+=1
        elif (i%k==0 and i//k!=0):
            psum+=i//k
        else:
            psum+=i
    print(psum)
print("Time taken=",time.time()-init)
