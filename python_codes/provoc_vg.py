al=list(str(x) for x in input().split(" "))
min_base=float("infinity")
for a in al:
    sa=list(a)
    sa.sort(reverse=True)
    x=ord(sa[0])
    if x in range(65,91):
        base=x-54  
    elif x in range(48,58):
        base=x-47
    ma=int(a,base)
    if min_base>ma:
        min_base=ma
print(min_base)
    

        
        
