def make_chocolate(small,big,goal):
    for i in range(big,0,-1):
        if(i*5<=goal):
            t=goal-i*5
            if(t==0):
                return 0
            elif(t<=small):
                return t
            else:
                return -1
if(__name__=='__main__'):
    small=int(input("Enter small:"))
    big=int(input("Enter big:"))
    goal=int(input("Enter goal:"))
    result=make_chocolate(small,big,goal)
    print(result)
