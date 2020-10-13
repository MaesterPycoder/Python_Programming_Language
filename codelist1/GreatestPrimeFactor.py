import math 
def maxPrimeFactor(n):
    if n<2:
        return None
    maxPrime = -1
    while n % 2 == 0: 
        maxPrime = 2
        n //= 2     #This is also correct        n >>= 1  
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
    if n > 2: 
        maxPrime = n 
    return int(maxPrime) 
if __name__ == '__main__':
    n=int(input("Enter number (>2): "))
    print(maxPrimeFactor(n))
