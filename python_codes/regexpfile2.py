import re
f1=open("sdata.txt","r")
f2=open("@_sdata.txt","a")
for line in f1:
    res1=re.search(r"\d{4}",line)
    res2=re.search(r"\d{4,}.\d{2}",line)
    print(res1.group(),res2.group())
    f2.write(res1.group()+"\t")
    f2.write(res2.group()+"\n")
f2.write("---------------------------------------------")
f2.write("\n")
f1.close()
f2.close()
    
