class reverse:
    def __init__(self):
        n=int(input("Enter any number>0:"))
        self.n=n
    def make(self):
        r=0
        while self.n>0:
            r=r*10+self.n%10
            self.n//=10
        print("Reversed number=",r)
reverse().make()
        
            
