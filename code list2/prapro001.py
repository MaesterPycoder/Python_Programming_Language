a=[]
for i in range(2000,3201):
    if i%7==0:
        if i%5!=0:
            a.append(str(i))
print(a,sep=',')       
