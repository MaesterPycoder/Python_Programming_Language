def EuclidGCD(a,b):
    if b==0:
        return a
    else:
        d=a%b
        return EuclidGCD(b,d)
if __name__=="__main__":
    a=int(input())
    b=int(input())
    re=EuclidGCD(a,b)
    print("GCD of",str(a)," and",str(b)," is=",str(re))
