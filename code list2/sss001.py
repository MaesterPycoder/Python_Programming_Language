class solution:
    def solve(self,str):
        min_len=len(str)
        for word in str:
            if min_len>len(word):
                min_len=len(word)
        for word in str:
            if len(word)==min_len:
                print(word)
                break
s=solution()
s.solve("abc de ghihjk a uvw h j")