import itertools as it
l=[]
num=int(input("Enter number:"))
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
x=len(prime_nums)
if(prime_nums[x-1]==num):
    print(1)
    print(num)
else:
    for k in range(2,len(prime_nums)):
        l=list(it.combinations(prime_nums,k))
        for i in range(len(l)):
            sum=0
            for j in range(0,k):
                sum=sum+l[i][j]
            if sum==num:
                print("min no. of pairs required"+str(k))
                print("pair is:",l[i][j])
                break
            break
