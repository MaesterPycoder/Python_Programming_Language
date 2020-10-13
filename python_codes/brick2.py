def making_goal(m,n,p):
    if(n*5<=p):
        t=p-n*5
        if(t<=m):
            print("True")
            return True
        else:
            print("False")
            return False
    else:
        t=decre(n)
        making_goal(m,t,p)
def decre(n):
    if(n!=0):
        n-=1
        return n
    else:
        print("False")
        return False
making_goal(3,1,8)
making_goal(1,4,12)
