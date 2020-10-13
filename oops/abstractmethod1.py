from abc import ABC, abstractmethod
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
class sub1(Myclass):
    def calculate(self,x):
        print("Square of number=",x*x)
import math
class sub2(Myclass):
    def calculate(self,x):
        print("Squareroot of the number=",math.sqrt(x))
class sub3(Myclass):
    def calculate(self,x):
        print("Cube of the number=",x**3)
obj1=sub1()
obj1.calculate(16)
obj2=sub2()
obj2.calculate(16)
obj3=sub3()
obj3.calculate(16)
