# Write your code here
import re
st=input("Enter string:")
res=re.findall(r"(\w+?)(\d+)",st)
st1=list(res)
st2=""
for i in range(len(st1)):
    p=int(st1[i][1])
    st2+=(st1[i][0]*p)
l=list(st2)
l.sort()
st3="".join(l)
T=int(input("Enter tests:"))
for i in range(T):
    k=int(input("Enter:"))
    if k-1<=len(st3):
        print(st3[k-1])
    else:
        print("-1")
