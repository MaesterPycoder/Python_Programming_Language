import logging as l
 l.basicconfig(filename="mylogs.txt", level=l.ERROR)
try:
    a=10
    b=20
    c=a/b
except Exception as e:
    l.exception(e)
else:
    print("The result of division=",c)
    
    
