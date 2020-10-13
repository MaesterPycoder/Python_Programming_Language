try:
    f=open("file1.txt","a")
    f.write("Entered values are :")
    a=int(input("Enter 'a' value:"))
    b=int(input("Enter 'b' value:"))
    c=a/b
    print(c)
    f.write("\n")
    f.write("Program succussfully executed without any Error")
except ZeroDivisionError:
    f.write("ZeroDivisionError occurred,Don't enter denominator 0")
    print("ZeroDivisionError occurred,Don't enter denominator 0")
finally:
    f.write("\n")
    f.write("---------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.close()
    print("File Closed")
