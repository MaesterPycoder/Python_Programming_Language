from time import time
def func1(a,b):
    #sss code
    return a+b
def func2(a,b):
    #shanmu code
    c=a**b
    return c
if __name__=='__main__':
    init=time()
    for i in range(0,100000):
        func1(2,3)
    print("Time of sss code=",time()-init)
    init=time()
    for _ in range(0,1000):
        func2(10,20)
    print("Time for shanmu code=",time()-init)
# Better to use the timeit module