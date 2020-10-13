class Prime:
    def __init__(self):
        k=n=int(input("Enter a number >0:"))
        self.n=n
        self.k=k
    def check(self):
        flag=0
        for i in range(2,self.k):
            if self.n%i==0:
                flag+=1
        if flag==0:
            print("It is a prime number")
        else:
            print("It is not a prime number")
p=Prime()
p.check()

