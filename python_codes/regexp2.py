import re
str1="waaa! this is@awesome dude"
res1=re.sub(r"\W","\n",str1)
print(res1)
print("------------------------")
res2=re.findall(r"\w\w\W",str1)
print(res2)
print("------------------------")
res3=re.search(r"\w[a]*3",str1)
print(res3)
print("------------------------")



