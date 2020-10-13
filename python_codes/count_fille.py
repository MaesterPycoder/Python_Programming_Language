import os,sys
f=input("Enter filename:")
if os.path.isfile(f):
    f=open(f,"r")
else:
    print("file that you entered is not found")
    sys.exit()
cl=cw=cc=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)
print("No. of lines:",cl)
print("No. of words:",cw)
print("No. of characters:",cc)
