class Testing:
    num=10
    @staticmethod
    def increment(staticmethod,num):
        num+=1
        return num
t1=Testing()
t2=Testing()
x=t1.increment()
y=t2.increment()
print(x) 
print(y)