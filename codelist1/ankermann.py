def A(n,m):
    if(n==0):
        return m+1
    elif(n>0 and m==0):
        return A(n-1,1)
    else:
        return A(n-1,A(n,m-1))
print(A(1,2))
