f=open("mytxt.txt","a")
f.write("---------------------------------------------------------------")
f.write("\n")
for i in range(10):
    str=input("Enter name %d:"%i)
    f.write(str)
    f.write("\n")
f.close()
