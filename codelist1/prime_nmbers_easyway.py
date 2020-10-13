def prime_list(num):
    limitin=num+1
    not_prime_num=set()
    prime_nums=[]
    for i in range(2,limitin):
        if i in not_prime_num:
            continue
        for f in range(i*2,limitin,i):
            not_prime_num.add(f)
        prime_nums.append(i)
    print(prime_nums)
prime_list(30)
