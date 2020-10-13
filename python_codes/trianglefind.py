import math
def angle(ab,bc):
    k=(ab*ab)+(bc*bc)
    ac=math.sqrt(k)
    cm=ac/2
    s=cm/bc
    p=math.asin(s)
    q=math.degrees(p)
    return q
if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    result =angle(ab,bc)
    result1=round(result)
    print(str(result1)+"°")
