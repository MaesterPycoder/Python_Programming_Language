'''import os,sys,re
f1=input("Enter filename:")
if os.path.isfile(f1):
    f1=open(f1,"r+")
else:
    print("sorry\n")
    print("File %s you entered is not found"%(fname))
f2=open("retrieveddata.txt","a")                   
for line in f1:
    res1=re.search(r"\b[A-Z]\D+\b",line)
    print(res1)
    res11.append(res1)
    f2.write(res11+"\t")
f1.close()
f2.close()'''


#program ERROR


#Work On Progress.
