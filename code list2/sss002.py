class solution:
    def solve(self,a):
        b=[]
        l=len(a)//2
        for i in a:
            if (a.count(i)>l) and (i not in b):
                b.append(i)
        for j in b:
            print(j)
s=solution()
s.solve([1,2,1,2,1,2,2,3,1,2,1,2,2,2,2,2,2,2,2,2,1])