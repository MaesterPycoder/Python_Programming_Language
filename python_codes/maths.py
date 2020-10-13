import math
def anglo(ab,bc):
    k=(ab*ab)+(bc*bc)
    ac=math.sqrt(k)
    cm=ac/2
    bm=((bc*bc)+(cm*cm)-(2*bc*cm*(bc/ac)))
    k=(((bm*bm)+(bc*bc)-(cm*cm))/(2*bm*bc))
    q=math.acos(k)
    return q
if __name__ == '__main__':
    ab = 10
    bc = 10
    res=anglo(ab,bc)
    print("result=",res)
    #result1=round(res)
    print(str(res)+"°")
