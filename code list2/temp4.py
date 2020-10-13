N,M=list(int(x) for x in input().split(" "))
A=list(int(x) for x in input().split(" "))
T=list(int(x) for x in input().split(" "))
def left(A,n):
    for i in range(n):
        k=A.pop(0)
        A.append(k)
    return A
def right(A,n):
    for _ in range(n):
        k=A.pop(-1)
        A.insert(0,k)
    return A
def is_equal(B,T):
    if B==T:
        return 1
    return 0
for _ in range(M):
    op,m=list(str(x) for x in input().split(" "))
    n=int(m)
    if op=="L":
        B=left(A,n)
        if is_equal(B,T):
            print(M)
            break
    if op=="R":
        B=right(A,n)
        if is_equal(B,T):
            print(M)
            break
        
        









