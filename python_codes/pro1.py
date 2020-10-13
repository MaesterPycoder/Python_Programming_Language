d=[]
s=input("Enter you array:")
j=0
for i in range(len(s)):
    f=0
    for j in range(i+1,len(s)):
         if (s[i]==s[j]):
            f+=1
    if (f==0):
        d.append(s[i])
print(d.(","))             
 
 
