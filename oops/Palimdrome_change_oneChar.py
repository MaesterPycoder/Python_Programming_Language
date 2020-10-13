class solution:
    def solve(self,A):
        self.A=A
        p=self.palimdromeByChangingOneChar(A)
        print(p)
    def isPalimdrome(self,A):
        s=A[ : :-1]
        if s==A:
            return True
        else:
            return False
    def palimdromeByChangingOneChar(self,a):
        low=f=0
        high=len(a)-1
        while(low<=high):
            if(a[low]==a[high]):
                if(low==high):
                    return "YES"
                low+=1
                high-=1
            else:
                l=list(a)
                l[low]=l[high]
                a="".join(l)
                if self.isPalimdrome(a):
                    f=1
                    return "Yes"
                else:
                    return"No"
                break
        if(low>high and f==0):
            return "NO"
s=solution()
s.solve("abcdffe")
s.solve("abcep")
s.solve("abcda")
s.solve("abba")
s.solve("aba")
