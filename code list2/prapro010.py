class student:
    def __init__(self, name="", exam="", marks=0):
        self.name=name
        self.exam=exam
        self.marks=marks
    def display(self):
        print("HI ",self.name)
        print("You got "+str(self.marks)+" in "+self.exam)
    def Grade(self):
        if(self.marks>=90):
            print("You secured 'A+' grade in ",self.exam)
        elif(self.marks>=80):
            print("You secured 'A' grade in",self.exam)
        elif(self.marks>=70):
            print("You secured 'B' grade in",self.exam)
        elif(self.marks>=60):
            print("You secured 'C' grade in ",self.exam)
        elif(self.marks>=50):
            print("You secured 'D' grade in  ",self.exam)
        elif(self.marks>=32):
            print("You secured 'P' grade in ",self.exam)
        else:
            print("You are failed in "+self.exam+"Please write supplementary exam.")
n=int(input("Enter no.of students:"))
i=1
while(i<=n):
    name=input("Enter name:")
    exam=input("Enter exam name :")
    marks=int(input("Enter marks:"))
    s1=student(name,exam,marks)
    s1.display()
    s1.Grade()
    i+=1
    print("-----------------------------------------------------------------------------------")
