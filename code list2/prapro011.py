f=open("Gradesheet.txt","a")
from datetime import *
datetime=datetime.now()
f.write("Date & Time:::"+str(datetime))
f.write("\n")
f.write("DETAILS OF EXAM WRITTEN :")
f.write("\n")
f.write("-------------------------------------------------------------------------------------")
f.write("\n")
f.write("                               ***************                                                            ")
f.write("\n")
f.write("-------------------------------------------------------------------------------------")
f.write("\n")
class student:
    def __init__(self, name="",exam="", marks=0):
        self.name=name
        self.exam=exam
        self.marks=marks
    def display(self):
        print("HI ",self.name)
        f.write("HI "+self.name)
        f.write("\n")
        print("You got "+str(self.marks)+" in "+self.exam)
        f.write("You got "+str(self.marks)+" in "+self.exam)
        f.write("\n")
    def Grade(self):
        if(self.marks>=90):
            print("You secured 'A+' grade in ",self.exam)
            f.write("You secured 'A+' grade in "+self.exam)
        elif(self.marks>=80):
            print("You secured 'A' grade in",self.exam)
            f.write("You secured 'A' grade in "+self.exam)
            f.write("\n")
        elif(self.marks>=70):
            print("You secured 'B' grade in",self.exam)
            f.write("You secured 'B' grade in "+self.exam)
            f.write("\n")
        elif(self.marks>=60):
            print("You secured 'C' grade in ",self.exam)
            f.write("You secured 'C' grade in "+self.exam)
            f.write("\n")
        elif(self.marks>=50):
            print("You secured 'D' grade in  ",self.exam)
            f.write("You secured 'D' grade in "+self.exam)
            f.write("\n")
        elif(self.marks>=32):
            print("You secured 'P' grade in ",self.exam)
            f.write("You secured 'P' grade in "+self.exam)
            f.write("\n")
        else:
            print("You are failed in "+self.exam+". Please write supplementary exam.")
            f.write("You are failed in "+self.exam+". Please write supplementary exam.")
            f.write("\n")
n=int(input("Enter no.of students:"))
i=1
while(i<=n):
    name=input("Enter name:")
    exam=input("Enter exam name :")
    marks=float(input("Enter marks:"))
    s1=student(name,exam,marks)
    s1.display()
    s1.Grade()
    i+=1
    print("-----------------------------------------------------------------------------------")
    f.write("\n")
    f.write("-----------------------------------------------------------------------------------")
    f.write("\n")
f.close()
