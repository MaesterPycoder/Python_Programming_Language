def reverse(n):
  rn=0
  while n>0:
    rn = rn*10+n%10
    n=n//10
  return rn

lst=[10,9,8,7,5,1,6,2,4,3]

for i in range(len(lst)-1):
  for j in range(0,len(lst)-i-1):
    if(lst[j+1]<lst[j]):
      lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
