class even:
    def __init__(self,x):
        self.x=x
    def check(self):
        if self.x%2==0:
            print("It is even number")
        else:
            print("It is odd number")
x=int(input("Enter a number:"))
e=even(x)
e.check()
input("Press to exit the program <enter>")

