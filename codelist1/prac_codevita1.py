import itertools as it
a,b=list(int(x) for x in input().split(" "))
def check(n):
    if  n>b:
        return n
st=str(a)
stlm=str(b)
n=len(st)
lm=len(stlm)
lt=list(st)
if(n<lm):
    print(-1)
else:
    lst=list(it.permutations(lt,n))
    arr=[]
    for l in lst:
        arr.append("".join(l))
    arr=list(map(int,arr))
    arr1=list(filter(check,arr))
    if len(arr1)>0:
        print(min(arr1))
    else:
        print(-1)
