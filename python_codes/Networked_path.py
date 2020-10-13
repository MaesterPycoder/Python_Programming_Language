def move_right(x,y):
    return x+1,y
def move_up(x,y):
    return x,y+1
x=212072634227239451
n,m=list(int(x) for x in input("Enter n,m:").split(" "))
count=0
lst=list()
for _ in range(n):
    lst.append(list(int(x) for x in input("Enter values:").split(" ")))
a,b=n-1,m-1
x,y=0,0
arr=[[0,0],[0,1],[1,0],[1,1]]


