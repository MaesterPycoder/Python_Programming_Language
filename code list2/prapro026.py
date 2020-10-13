import sys
import math
sys.setrecursionlimit(100)
def fac(n):
    if n==0 or n==1:
        return 1
    return n*fac(n-1)
#print(math.factorial(1500))
try:
    n=int(input())
    print(fac(n))
except RecursionError:
    print("Alright!, I will correct it.")
    print("I'm fixing it.")
finally:
    sys.setrecursionlimit(1000)
    print("Error may occur due to reccursion limit for n beyound",sys.getrecursionlimit()-1)