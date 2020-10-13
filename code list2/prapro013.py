import math
class Square:
    @staticmethod
    def calsqrt(x):
        return math.sqrt(x)
n=float(input("Enter number:"))
print("result is=",Square.calsqrt(n))
