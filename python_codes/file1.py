f=open("myfile.txt","a")
print("Enter string with @ at the end:")
while str!="over":
    str=input()
    if str!="over":
        f.write(str+"\n")
f.close()       
