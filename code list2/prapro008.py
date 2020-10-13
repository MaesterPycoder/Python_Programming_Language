class student:
    def __init__(self):
        name=input("Enter name :")
        self.name=name
        exam=input("Enter exam name :")
        self.exam=exam
        marks=int(input("Enter marks:"))
        self.marks=marks
    def display(self):
        print("HI ",self.name)
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
s1=student()
s1.display()
