class num_prime:
    def __init__(self):
        self.num=int(input("Enter number:"))
        assert self.num>1,"Not possible"
        self.count=0
    def prime_expresser(self):
        if self.isprime(self.num):
            self.count+=1
        else:
            self.possibility(self.num)
        print("expressed in:",self.count)
        return self.count
    def possibility(self,n):
        p=self.nearest_prime(n)
        if p is None:
            print("Not possibe")
            return None
        d=self.num-p
        if d==1:
            p=self.nearest_prime(p)
            d=self.num-p
        self.count+=1
        if self.isprime(d):
            self.count+=1          
    def isprime(self,n):
        if n==2:
            return 1
        for i in range(2,n):
            if n%i==0:
                return 0
        return 1
    def nearest_prime(self,p):
        if p<2:
            return None
        if self.isprime(p):
            return n
        else:
            self.nearest_prime(n-1)       
n=num_prime()
n.prime_expresser()