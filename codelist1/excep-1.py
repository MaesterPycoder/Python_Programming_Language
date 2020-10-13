try:
    z=2/0
    print("value of z =",z)
except ZeroDnivisionError as m:
    m="you entered incorrect division format"
    print(m)
