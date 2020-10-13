class student:
    def setname(self,name):#using mutator method
        self.name=name
    def getname(self):#using accessor methods
        return self.name
    def setmarks(self,marks):#using mutator methods
        self.marks=marks
    def getmarks(self):#using accessor methods
        return self.marks
#creating class instance
n=int(input("Enter no. of students:"))
i=1
while(i<=n):
    s=student()
    #Giving data to the class
    name=input("Enter name :")
    s.setname(name)
    marks=int(input("Enter marks :"))
    s.setmarks(marks)
    #Retriving data from the class
    print("Hi! ",s.getname()+" you got "+str(s.getmarks())+" out of 700 marks")
    i+=1
    print("-----------------------------------------------------------------------------------")
    
