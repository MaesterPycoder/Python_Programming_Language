Rco=Gco=Bco=Yco=Cco=Mco=Wco=Blco=0
#T,R,G,B=list(int(x) for x in input().split(" "))
T,R,G,B=[12,2,3,5]
Ba=[]
Ra=[]
Ga=[]
def arrayGen(lst,N,T):
    count=0
    size=0
    for _ in range(0,T,N):
        if count%2==0:
            for _ in range(N):
                if size != T:
                    size+=1
                    lst.append(0)
            count+=1
        else:
            for _ in range(N):
                if size != T:
                    size+=1
                    lst.append(1)
            count+=1
    return lst
def color(R,G,B):
    global Rco,Bco,Gco,Yco,Mco,Blco,Cco,Wco
    if R and not G and not B:
        Rco+=1
        return
    if not R and G and not B:
        Gco+=1
        return
    if not R and not G and B:
        Bco+=1
        return
    if R and G and not B:
        Yco+=1
        return
    if not R and G and B:
        Cco+=1
        return
    if R and not G and B:
        Mco+=1
        return
    if R and G and B:
        Wco+=1
        return
    if not R and not G and not B:
        Blco+=1
        return
Ba=arrayGen(Ba,B,T)
Ga=arrayGen(Ga,G,T)
Ra=arrayGen(Ra,R,T)
print(Ra)
print(Ga)
print(Ba)
for i in range(T):
    color(Ra[i],Ga[i],Ba[i])
lst1=map(str,[Rco,Gco,Bco,Yco,Cco,Mco,Wco,Blco])
res=" ".join(lst1)
print(res)
'''@ bEST SOLUTION
from itertools import cycle, islice
nsecs, red, green, blue = [int(x) for x in input().split()]
 
seq = zip(*[cycle([0]*secs + [1]*secs) for secs in [red, green, blue]])
R, G, B, Y, C, M, W, BL = (0, 0, 0, 0, 0, 0, 0, 0)
 
for rgb in islice(seq, 0, nsecs):
    if rgb == (0, 0, 0):
        BL += 1
    elif rgb == (1, 0, 0):
        R += 1
    elif rgb == (0, 1, 0):
        G += 1
    elif rgb == (0, 0, 1):
        B += 1
    elif rgb == (1, 1, 0):
        Y += 1
    elif rgb == (0, 1, 1):
        C += 1
    elif rgb == (1, 0, 1):
        M += 1
    elif rgb == (1, 1, 1):
        W += 1
 
print(R, G, B, Y, C, M, W, BL)
Language: Python 3
'''