import itertools as it
N=6
arr=[1,3,2,1,2,1]
lst=[]
for k in range(2,N+1):
    lst+=list(map(list,list(it.combinations(arr,k)))) 
print(lst)
count=0
def OR(ar):
    res=ar[0]
    for j in range(1,len(ar)):
        res=res or j
    return res
def AND(ar):
    res=ar[0]
    for j in range(1,len(ar)):
        res=res and j
    return res
def XOR(ar):
    res=ar[0]
    for j in range(1,len(ar)):
        res=res ^ j
    return res 
for i in range(len(lst)):
    if OR(lst[i])==AND(lst[i])==XOR(lst[i]):
        count+=1
print("result=",count)
