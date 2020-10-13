import math
class amstrong:
    def __init__(self):
        n=k=int(input("Enter any number >0="))
        self.n=n
        self.k=k
    def check(self):
        s=0
        while self.n>0:
            r=self.n%10
            s+=math.pow(r,3)
            self.n//=10
        print("value of r=",s)
        if self.k==s:
            print("It is an amstrong number")
        else:
            print("It is not an amstrong number")
amstrong().check()
