#d=[["Harsh",20],["Beria",20],["Varun",19],["Kakunami",19],["Vikas",21]]
#d=[["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]
d=[["Rachel",-50],["Mawer",-50],["Sheen",-50],["Shaheen",-50]]
#finding all the names of people having second last value in d
for j in range(len(d)):
    for i in range(len(d)-j-1):
        if(d[i][1]>d[i+1][1]):
            d[i],d[i+1]=d[i+1],d[i]
        elif(d[i][1]==d[i+1][1]):
            if(d[i][0]>d[i+1][0]):
                if(d[i][0]>d[i+1][0]):
                   d[i+1],d[i]=d[i],d[i+1]
print(d)
d.append([0,0])
d.append([0,0])
d.append([0,0])
print(d)
a=[]
for i in range(len(d)-2):
    if(d[i][1]<d[i+1][1]):
        if(d[i+1][1]<d[i+2][1]):
            a.append(d[i+1])
            break
        else:
            for j in range(i+1,len(d)):
                if(d[j][1]==d[i+1][1]):
                    a.append(d[j])
        break
for i in range(len(a)):
    print(a[i][0])

