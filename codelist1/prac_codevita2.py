a=int(input())
b=float(input())
_time=(a/360)*b
hrs=int(_time)
_min=int(60*(_time-hrs))
if _min==0:
    print("{:.2f}".format(0))
else:
    val=(_min//5)-hrs
    res=(360/a)*val
    print("{:0.2f}".format(res))
