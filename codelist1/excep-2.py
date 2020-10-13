def con(a,b):
    print(a+b)
try:
    con("hai",56)
except TypeError as k:
    k='''sorry,'int' can't be concatenated with 'str'.so convert 56 into string explicitly.Because 'str' cannot be converted to 'int' implicitly.'''
    print("TypeError: ",k)
finally:
    print("program executed succussfully")
