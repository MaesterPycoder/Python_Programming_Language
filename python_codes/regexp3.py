import re
str1="Hardhik 21 2-2-1999, Harsh 22 24-03-1998, Dhoni 19 19-09-2000, Kohli 4 6-8-1963"
res1=re.findall(r"\d{2}-\d{2}-\d{4}",str1)
print(res1)
res2=re.findall(r"\d?2",str1)
print(res2)
res3=re.findall(r"\d\d-\d\d-\d\d\d\d",str1)
print(res3)
