import os
import sys
f=input("Enter file name:")
if os.path.isfile(f):
    f=open(f,"r")
else:
    print("Sorry! File that you are looking is not found.")
    sys.exit()
print("File contents are:")
str=f.read()
print(str)
f.close()
