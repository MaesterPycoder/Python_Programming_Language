def bool_fun(s):
    one=0
    zero=0
    for i in range(len(s)-1,-1,-1):
        if s[i] is '0':
            zero+=1
        else:
            one+=1
        if zero > one:
            return False
    return True
print(bool_fun("10011"))
        
