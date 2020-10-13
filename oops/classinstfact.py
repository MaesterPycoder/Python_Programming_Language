class fact:
    def __init__(self):
        n=int(input("Enter any number:"))
        self.n=n
    def find(self):
        f=1
        for i in range(1,self.n+1):
            f=f*i
        print("Factorial of a number:",f)
fact().find()
