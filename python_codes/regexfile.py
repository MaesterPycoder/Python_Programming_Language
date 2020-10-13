import os,sys,re
f1=input("Enter filename:")
if os.path.isfile(f):
    f1=open(f1,"r+")
else:
    print("sorry\n")
    print("File %s you entered is not found"%(fname))
f2=open("retrieveddata.txt","w+")
for line in f1:
    res1=re.findall(r"[A-Z][a-z]*5")
    f.write(res1)
f1.close()
f2.close()


