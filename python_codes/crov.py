N=int(input("Enter no. of persons:"))
A=int(input("Enter positon:"))
B=int(input("Enter position preceding to required position:"))
st=list(range(0,N))
i=A
f=1
d=B+1-A
while(f>0):
    i+=d
    i=i%N
    if(st[i]==A):
        if(f>1):
            print("No.of turns=",f)
            break
    f+=1
