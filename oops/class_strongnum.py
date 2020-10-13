class strong:
    def __init__(self):
        n=k=int(input("Enter a number:"))
        self.n=n
        self.k=k
    def find(self):
        s=0
        while self.n>0:
            r=self.n%10
            f=1
            for i in range(1,r+1):
                f=f*i
            s+=f
            self.n//=10
        if self.k==s:
            print("It is a stong number")
        else:
            print("It is not a strong number")
strong().find()
        
        
    
