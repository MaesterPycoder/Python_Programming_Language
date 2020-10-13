def is_ugly_num(n):
    flag=0
    while n!=1:
        if n%5==0:
            n=n//5
        elif n%3==0:
            n=n//3
        elif n%2==0:
            n=n//2
        else:
            flag=1
            break
    if flag==0:
        return 1
    else:
        return 0
    
for _ in range(2):
    num=int(input("Enter:"))
    ugly_num=[1,]
    i=2
    while len(ugly_num)<num:
        if is_ugly_num(i):
            ugly_num.append(i)
            i+=1
        else:
            i+=1
    print(ugly_num[num-1])
