import re
str1="man mop map mat sun run"
res=re.findall(r"m\w\w",str1)
if res:
    print(res)
    print(res[2])
else:
    print("Not found")
