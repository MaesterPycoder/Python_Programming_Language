class solution:
    def solve(self,A):
        G=1
        count=0
        for i in range(len(A)):
            G*=A[i]
        for i in range(2,G):
            if G%i==0:
                if self.isprime(i):
                    count+=1
        return count
    def isprime(self,n):
        if n==2:
            return 1
        else:
            f=0
            for i in range(2,n):
                if n%i==0:
                    f+=1
                    break
            if f==0:
                return 1
            return 0
s=solution()
#print(s.solve([1,2,3,4]))
print(s.solve([98,96,5,41,80]))