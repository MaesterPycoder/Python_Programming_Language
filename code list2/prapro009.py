print("USING CLASS VARIABLE")
class student:
    n=10#class variable
    @classmethod
    def modify(self):
        self.n+=1
s1=student()
s2=student()
print(s1.n)
print(s2.n)
s1.modify()
print(s1.n)
print(s2.n)
print("----------------------------------------------------------------")
print("USING  INSTANCE VARIABLE")
class stud:
    def __init__(self):
        self.p=10#instance variable
    def modify(self):
        self.p+=1
p1=stud()
p2=stud()
print(p1.p)
print(p2.p)
p1.modify()
print(p1.p)
print(p2.p)

        
