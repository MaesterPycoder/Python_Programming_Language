def find(sr):
    n=len(sr)
    f=0
    for i in range(n-3):
       if(sr[i:i+3]=="xyz"):
           if(i==0):
               f+=1
           if(i>0):
               if(sr[i-1]!="."):
                   f+=1
    if(f>0):
        return True
    else:
        return False
for _ in range(20):
    p=find(input("Enter string :"))
    print(p)
