import time
with open("ext.txt","a") as f:
    for i in range(10):
        f.write(str(i)+"This is written")
        print("yo!")
        f.write(time.ctime())
        print("yes")
        f.write("\n"+"-"*200)