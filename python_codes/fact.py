n=int(input("Enter a number greator than or equal to zero:"))
if n==0:
    print("It's factorial is =1")
else:
    f=1
    for i in range(n,0,-1):
        f=f*i
    print("It's factorial is=",f)
