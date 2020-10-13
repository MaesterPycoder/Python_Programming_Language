d=[3,1,5,2,6,4,0]
for i in range(7):
    for j in range(6-i):
        if(d[j]>d[j+1]):
            d[j],d[j+1]=d[j+1],d[j]
print(d)           
